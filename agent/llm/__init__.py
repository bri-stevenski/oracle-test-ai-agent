from agent.llm.client import LLMClient

_llm = None

def get_llm():
    global _llm
    if _llm is None:
        _llm = LLMClient()
    return _llm

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

    return get_llm().generate(messages)