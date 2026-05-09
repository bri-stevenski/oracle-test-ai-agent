from agent.llm.client import LLMClient

_llm = LLMClient()

def generate_response(prompt: str) -> str:
    """
    Simple wrapper used by Oracle orchestrator
    """

    messages = [
        {
            "role": "system",
            "content": "You are Oracle, a senior test automation engineer."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    return _llm.generate(messages)