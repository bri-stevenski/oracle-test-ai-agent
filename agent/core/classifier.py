# agent/core/classifier.py

from dataclasses import dataclass
from typing import Optional


@dataclass
class ClassificationResult:
    intent: str
    test_type: str
    confidence: float


class TestClassifier:

    def classify(self, prompt: str) -> ClassificationResult:
        p = prompt.lower()

        # --- PERFORMANCE ---
        if "performance" in p or "load test" in p or "stress test" in p:
            return ClassificationResult(
                intent="generate_tests",
                test_type="performance",
                confidence=0.95
            )

        # --- API TESTING ---
        if "api" in p or "endpoint" in p or "request" in p:
            return ClassificationResult(
                intent="generate_tests",
                test_type="api",
                confidence=0.85
            )

        # --- FRONTEND UNIT / COMPONENT ---
        if "component" in p or "react" in p or "frontend" in p:
            return ClassificationResult(
                intent="generate_tests",
                test_type="frontend_unit",
                confidence=0.9
            )

        # --- DEFAULT E2E ---
        if "login" in p or "checkout" in p or "user flow" in p:
            return ClassificationResult(
                intent="generate_tests",
                test_type="e2e_ui",
                confidence=0.8
            )

        # fallback
        return ClassificationResult(
            intent="generate_tests",
            test_type="e2e_ui",
            confidence=0.5
        )