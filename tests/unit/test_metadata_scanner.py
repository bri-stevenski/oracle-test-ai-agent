"""Unit tests for MetadataScanner."""

import json
import tempfile
import unittest
from pathlib import Path

from agent.core.metadata_scanner import MetadataScanner, ProjectMetadata


class TestProjectMetadataIsEmpty(unittest.TestCase):

    def test_empty_by_default(self):
        self.assertTrue(ProjectMetadata().is_empty)

    def test_not_empty_with_js_deps(self):
        m = ProjectMetadata(js_dependencies={"playwright": "^1.40.0"})
        self.assertFalse(m.is_empty)

    def test_not_empty_with_python_packages(self):
        m = ProjectMetadata(python_packages={"pytest": "==7.4.0"})
        self.assertFalse(m.is_empty)

    def test_not_empty_with_tsconfig(self):
        m = ProjectMetadata(tsconfig={"strict": True})
        self.assertFalse(m.is_empty)


class TestScanPackageJson(unittest.TestCase):

    def setUp(self):
        self.scanner = MetadataScanner()
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_reads_dependencies_and_dev_dependencies(self):
        pkg = {
            "dependencies": {"react": "^18.0.0"},
            "devDependencies": {"@playwright/test": "^1.40.0", "vitest": "^1.0.0"},
        }
        (self.root / "package.json").write_text(json.dumps(pkg))
        metadata = self.scanner.scan(str(self.root))
        self.assertEqual(metadata.js_dependencies["react"], "^18.0.0")
        self.assertIn("@playwright/test", metadata.js_dependencies)
        self.assertIn("vitest", metadata.js_dependencies)

    def test_missing_package_json_leaves_empty(self):
        metadata = self.scanner.scan(str(self.root))
        self.assertEqual(metadata.js_dependencies, {})

    def test_invalid_json_leaves_empty(self):
        (self.root / "package.json").write_text("not json {{{")
        metadata = self.scanner.scan(str(self.root))
        self.assertEqual(metadata.js_dependencies, {})

    def test_package_json_with_no_deps_keys(self):
        (self.root / "package.json").write_text(json.dumps({"name": "my-app"}))
        metadata = self.scanner.scan(str(self.root))
        self.assertEqual(metadata.js_dependencies, {})

    def test_null_dependencies_field_leaves_empty(self):
        pkg = {"dependencies": None, "devDependencies": None}
        (self.root / "package.json").write_text(json.dumps(pkg))
        metadata = self.scanner.scan(str(self.root))
        self.assertEqual(metadata.js_dependencies, {})


class TestScanRequirementsTxt(unittest.TestCase):

    def setUp(self):
        self.scanner = MetadataScanner()
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_parses_pinned_versions(self):
        (self.root / "requirements.txt").write_text("pytest==7.4.0\nrequests==2.31.0\n")
        metadata = self.scanner.scan(str(self.root))
        self.assertEqual(metadata.python_packages["pytest"], "==7.4.0")
        self.assertEqual(metadata.python_packages["requests"], "==2.31.0")

    def test_parses_range_specifiers(self):
        (self.root / "requirements.txt").write_text("httpx>=0.25\nanthropics~=0.40\n")
        metadata = self.scanner.scan(str(self.root))
        self.assertEqual(metadata.python_packages["httpx"], ">=0.25")
        self.assertEqual(metadata.python_packages["anthropics"], "~=0.40")

    def test_ignores_comments_and_blank_lines(self):
        content = "# test deps\n\npytest==7.4.0\n# end\n"
        (self.root / "requirements.txt").write_text(content)
        metadata = self.scanner.scan(str(self.root))
        self.assertIn("pytest", metadata.python_packages)
        self.assertEqual(len(metadata.python_packages), 1)

    def test_ignores_flag_lines(self):
        (self.root / "requirements.txt").write_text("-r base.txt\npytest==7.4.0\n")
        metadata = self.scanner.scan(str(self.root))
        self.assertNotIn("-r base.txt", metadata.python_packages)
        self.assertIn("pytest", metadata.python_packages)

    def test_package_with_no_version(self):
        (self.root / "requirements.txt").write_text("pytest\n")
        metadata = self.scanner.scan(str(self.root))
        self.assertEqual(metadata.python_packages["pytest"], "")

    def test_missing_file_leaves_empty(self):
        metadata = self.scanner.scan(str(self.root))
        self.assertEqual(metadata.python_packages, {})


class TestScanPyprojectToml(unittest.TestCase):

    def setUp(self):
        self.scanner = MetadataScanner()
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_reads_project_dependencies(self):
        toml = '[project]\nname = "myapp"\ndependencies = [\n    "pytest>=7.0",\n    "httpx>=0.25",\n]\n'
        (self.root / "pyproject.toml").write_text(toml)
        metadata = self.scanner.scan(str(self.root))
        self.assertIn("pytest", metadata.python_packages)
        self.assertEqual(metadata.python_packages["pytest"], ">=7.0")

    def test_no_dependencies_key_returns_empty(self):
        toml = '[project]\nname = "myapp"\n'
        (self.root / "pyproject.toml").write_text(toml)
        metadata = self.scanner.scan(str(self.root))
        self.assertEqual(metadata.python_packages, {})

    def test_does_not_cross_section_boundaries(self):
        toml = (
            '[project]\nname = "myapp"\n\n'
            '[tool.other]\ndependencies = [\n    "something>=1.0",\n]\n'
        )
        (self.root / "pyproject.toml").write_text(toml)
        metadata = self.scanner.scan(str(self.root))
        self.assertEqual(metadata.python_packages, {})

    def test_requirements_txt_takes_priority_over_pyproject(self):
        (self.root / "requirements.txt").write_text("pytest==7.4.0\n")
        toml = '[project]\ndependencies = [\n    "httpx>=0.25",\n]\n'
        (self.root / "pyproject.toml").write_text(toml)
        metadata = self.scanner.scan(str(self.root))
        self.assertIn("pytest", metadata.python_packages)
        self.assertNotIn("httpx", metadata.python_packages)


class TestScanTsconfig(unittest.TestCase):

    def setUp(self):
        self.scanner = MetadataScanner()
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_reads_compiler_options(self):
        tsconfig = {"compilerOptions": {"strict": True, "target": "ES2020", "module": "commonjs"}}
        (self.root / "tsconfig.json").write_text(json.dumps(tsconfig))
        metadata = self.scanner.scan(str(self.root))
        self.assertTrue(metadata.tsconfig["strict"])
        self.assertEqual(metadata.tsconfig["target"], "ES2020")

    def test_missing_compiler_options_returns_empty(self):
        (self.root / "tsconfig.json").write_text(json.dumps({"extends": "./base.json"}))
        metadata = self.scanner.scan(str(self.root))
        self.assertEqual(metadata.tsconfig, {})

    def test_invalid_json_leaves_empty(self):
        (self.root / "tsconfig.json").write_text("not json")
        metadata = self.scanner.scan(str(self.root))
        self.assertEqual(metadata.tsconfig, {})

    def test_missing_file_leaves_empty(self):
        metadata = self.scanner.scan(str(self.root))
        self.assertEqual(metadata.tsconfig, {})


class TestScanEmptyDirectory(unittest.TestCase):

    def test_all_empty_when_no_files(self):
        scanner = MetadataScanner()
        with tempfile.TemporaryDirectory() as tmp:
            metadata = scanner.scan(tmp)
        self.assertTrue(metadata.is_empty)
