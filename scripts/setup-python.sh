#!/usr/bin/env bash
# Setup Python 3.13 + project venv for oracle-test-ai-agent.
# Run from any directory: bash scripts/setup-python.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PYTHON_VERSION="3.13"
BREW_PREFIX="$(brew --prefix 2>/dev/null || true)"
PYTHON_BIN="${BREW_PREFIX}/bin/python${PYTHON_VERSION}"
if [[ -z "${BREW_PREFIX}" || ! -x "${PYTHON_BIN}" ]]; then
  echo "Error: python${PYTHON_VERSION} not found at ${PYTHON_BIN}." >&2
  echo "Install it with: brew install python@${PYTHON_VERSION}" >&2
  exit 1
fi
VENV_DIR="${REPO_ROOT}/.venv"

echo "==> Installing Python ${PYTHON_VERSION} via Homebrew..."
brew install "python@${PYTHON_VERSION}"

echo ""
echo "==> Creating venv at ${VENV_DIR}..."
"${PYTHON_BIN}" -m venv "${VENV_DIR}"

echo ""
echo "==> Installing project + dev dependencies..."
"${VENV_DIR}/bin/pip" install --quiet --upgrade pip
"${VENV_DIR}/bin/pip" install -e "${REPO_ROOT}"
"${VENV_DIR}/bin/pip" install pytest

echo ""
echo "==> Verifying..."
"${VENV_DIR}/bin/python" --version
"${VENV_DIR}/bin/pytest" --version

echo ""
echo "Done. Activate the venv with:"
echo "  source .venv/bin/activate"
echo ""
echo "Then run tests with:"
echo "  pytest tests/unit/ -v"
