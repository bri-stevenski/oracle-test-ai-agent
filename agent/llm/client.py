# agent/llm/client.py

import os
from typing import List, Dict, Any

from openai import OpenAI


class LLMClient:
    """
    Central LLM abstraction for Oracle.

    Keeps model logic isolated so we can:
    - swap models later
    - add caching
    - add retries / logging
    """

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # You can change this later (important for flexibility)
        self.model = "gpt-5.3-mini"

    def generate(self, messages: List[Dict[str, str]]) -> str:
        """
        Generic chat completion interface
        """

        response = self.client.responses.create(
            model=self.model,
            input=messages
        )

        return response.output_text