# Oracle — Current State

## 🧠 System Status

Oracle is a functional AI-assisted test automation CLI tool. It can classify user intent, recommend frameworks, and generate production-ready test code.

## ✅ Implemented Components

- Framework registry (registry.json with extension support)
- Test classifier (rule-based intent detection)
- Framework recommender (engineering decision layer)
- Orchestrator (end-to-end pipeline)
- LLM abstraction layer (lazy initialization, client + service wrapper)
- CLI Interface (oracle generate, version)

## ⚙️ Architecture Summary

User Prompt → CLI → Orchestrator → Classifier → Recommender → LLM → Generated Test Output

## ❗ Current Limitation

Generated tests are not yet automatically executed or verified by Oracle.

## 🎯 Next Step

Implement Execution Feedback Loop:
- `oracle run <file>` or automatic execution after generation
