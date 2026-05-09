# agent/core/orchestrator.py

from pathlib import Path
from datetime import datetime

from agent.core.classifier import TestClassifier
from agent.core.recommender import FrameworkRecommender
from agent.llm import generate_response


class OracleOrchestrator:

    def __init__(self):
        self.classifier = TestClassifier()
        self.recommender = FrameworkRecommender()

        self.output_dir = Path(__file__).resolve().parents[2] / "tests" / "generated"
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def run(self, user_prompt: str) -> dict:
        """
        Main entrypoint for Oracle pipeline
        """

        # 1. Classify intent
        classification = self.classifier.classify(user_prompt)

        # 2. Recommend framework
        recommendation = self.recommender.recommend(classification)

        framework = recommendation["framework"]

        # 3. Build generation prompt
        generation_prompt = self._build_prompt(
            user_prompt,
            classification.test_type,
            framework
        )

        # 4. Generate test code
        generated_code = generate_response(generation_prompt)

        # 5. Write file
        file_path = self._write_test_file(generated_code, framework)

        return {
            "input": user_prompt,
            "test_type": classification.test_type,
            "framework": framework,
            "reason": recommendation["reason"],
            "output_file": str(file_path)
        }

    def _build_prompt(self, user_prompt: str, test_type: str, framework: str) -> str:
        """
        Constructs framework-aware generation prompt
        """

        return f"""
You are Oracle, a senior test automation engineer.

Generate high-quality {framework} tests for the following requirement:

--- REQUIREMENT ---
{user_prompt}

--- CONTEXT ---
Test Type: {test_type}
Framework: {framework}

--- RULES ---
- Follow best practices for {framework}
- Write clean, maintainable tests
- Avoid brittle selectors
- Include comments explaining key logic
- Ensure code is production-ready
"""

    def _write_test_file(self, code: str, framework: str) -> Path:
        """
        Writes generated test to file system
        """

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_name = f"{framework}_test_{timestamp}.spec.ts"

        file_path = self.output_dir / file_name

        with open(file_path, "w") as f:
            f.write(code)

        return file_path