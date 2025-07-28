SHELL := /bin/bash
.PHONY: help check-deps install-deps setup-dev lint format test clean run

PYTHON_VERSION := 3.10

default: help

# ====================================================================================
# HELP
# ====================================================================================

help:
	@echo "🎯 Frank-Daemon - Ambiente de Desenvolvimento Local"
	@echo "========================================================================"
	@echo ""
	@echo "Comandos disponíveis:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-25s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "💡 Quick start:"
	@echo "   1. make setup-dev"
	@echo "   2. make run"
	@echo ""

# ====================================================================================
# SETUP & DEPENDENCIES
# ====================================================================================

check-deps: ## Verifica se as dependências (pyenv, poetry) estão instaladas.
	@echo "🔍 Verificando dependências..."
	@command -v pyenv >/dev/null 2>&1 || { echo "❌ pyenv não encontrado. Execute 'make install-deps'"; exit 1; }
	@command -v poetry >/dev/null 2>&1 || { echo "❌ poetry não encontrado. Execute 'make install-deps'"; exit 1; }
	@echo "✅ Todas as dependências foram encontradas!"

install-deps: ## Mostra instruções para instalar as ferramentas de desenvolvimento.
	@echo "📦 Instruções de Instalação:"
	@echo "--------------------------------------------------"
	@echo "1. Instale o pyenv (gerenciador de versão do Python):"
	@echo "   curl https://pyenv.run | bash"
	@echo ""
	@echo "2. Instale o poetry (gerenciador de dependências):"
	@echo "   curl -sSL https://install.python-poetry.org | python3 -"
	@echo ""
	@echo "3. Após a instalação, configure seu shell (e.g., ~/.zshrc ou ~/.bashrc) e reinicie o terminal."

setup-dev: check-deps ## Configura o ambiente de desenvolvimento completo (Python, dependências).
	@echo "🐍 Configurando ambiente Python com pyenv..."
	@if ! pyenv versions --bare | grep -q "^$(PYTHON_VERSION)$$"; then \
		echo "   Python $(PYTHON_VERSION) não encontrado, instalando via pyenv (isso pode levar alguns minutos)..."; \
		pyenv install $(PYTHON_VERSION); \
	else \
		echo "   Python $(PYTHON_VERSION) já está disponível."; \
	fi
	@pyenv local $(PYTHON_VERSION)
	@poetry config virtualenvs.in-project true
	@echo "📦 Instalando dependências do projeto com Poetry..."
	@poetry install
	@echo "🎉 Ambiente de desenvolvimento configurado com sucesso!"

# ====================================================================================
# DEVELOPMENT & CODE QUALITY
# ====================================================================================

run: ## Executa a aplicação principal.
	@echo "⚡ Executando Frank-Daemon..."
	@poetry run python src/main.py

lint: ## Executa os linters para verificar a qualidade do código.
	@echo "🎨 Verificando formatação e qualidade do código..."
	@poetry run flake8 src/ tests/
	@poetry run black --check src/ tests/
	@poetry run isort --check-only src/ tests/

format: ## Formata o código usando black e isort.
	@echo "✨ Formatando o código..."
	@poetry run black src/ tests/
	@poetry run isort src/ tests/

test: ## Executa os testes unitários.
	@echo "🧪 Executando testes..."
	@poetry run pytest

# ====================================================================================
# CLEANING
# ====================================================================================

clean: ## Remove arquivos temporários e de build.
	@echo "🧹 Limpando arquivos temporários..."
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.py[co]' -delete
	@rm -f .coverage
	@rm -rf .pytest_cache .mypy_cache build/ dist/ *.egg-info/
	@if [ -d .venv ]; then rm -rf .venv; fi
	@echo "🧼 Limpeza completa."
