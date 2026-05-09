# agent/core/framework_registry.py

import json
from pathlib import Path
from typing import Dict, List, Optional, Any


class FrameworkRegistry:
    def __init__(self, registry_path: str = None):
        base_dir = Path(__file__).resolve().parents[1]
        self.registry_path = registry_path or base_dir / "frameworks" / "registry.json"
        self._registry = self._load_registry()

    def _load_registry(self) -> Dict[str, Any]:
        with open(self.registry_path, "r") as f:
            return json.load(f)

    def get_all_frameworks(self) -> List[Dict]:
        return self._registry.get("frameworks", [])

    def get_by_category(self, category: str) -> List[Dict]:
        return [
            f for f in self.get_all_frameworks()
            if f.get("category") == category
        ]

    def get_preferred_by_category(self, category: str) -> Optional[Dict]:
        frameworks = self.get_by_category(category)

        # Prefer explicit "preferred"
        for f in frameworks:
            if f.get("status") == "preferred":
                return f

        return frameworks[0] if frameworks else None

    def find_by_name(self, name: str) -> Optional[Dict]:
        for f in self.get_all_frameworks():
            if f.get("name") == name:
                return f
        return None

    def match_by_language(self, language: str) -> List[Dict]:
        return [
            f for f in self.get_all_frameworks()
            if language in f.get("languages", [])
        ]