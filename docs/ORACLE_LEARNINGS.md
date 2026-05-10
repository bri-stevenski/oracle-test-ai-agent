# Oracle — Engineering Learnings

## 1. Registry-driven architecture is foundational

Framework selection is data-driven via registry.json rather than hardcoded logic.

## 2. Separation of concerns is critical

System is split into:

- classifier (intent detection)
- recommender (framework selection)
- orchestrator (workflow engine)
- LLM client (model abstraction)

This prevents logic entanglement and improves extensibility.

## 3. Orchestrator is the system kernel

All execution flows through orchestrator:
User input → classification → recommendation → generation → output

## 4. LLM abstraction is mandatory early

Abstracting model access enables:

- model swapping
- future caching
- prompt centralization
- cleaner architecture

## 6. Lazy LLM initialization is crucial for DX

Coupling module imports to API credential checks breaks non-generative commands (like `--version`) and unit tests. Initializing the LLM client only at the moment of execution (lazy loading) ensures the tool remains usable in restricted or non-connected environments.

## 7. Recommendation-only mode bridges the trust gap

Providing a `--recommend-only` flag allows users to validate Oracle's engineering decisions before committing to a full generation cycle. This transparency builds trust and saves tokens.
