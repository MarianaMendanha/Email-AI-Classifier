# 📧 Email AI Classifier & Responder

**Solução inteligente para gestão de fluxos de comunicação financeira.**

Este projeto automatiza a triagem de altos volumes de emails, utilizando Inteligência Artificial para classificar mensagens entre **Produtivas** (que exigem ação) e **Improdutivas** (informativas ou irrelevantes), sugerindo automaticamente uma resposta contextualizada.

---

## 🚀 Links do Projeto

- **Aplicação em Produção:** [Railway App Link](https://email-ai-classifier-production-e8a2.up.railway.app/)
- **Vídeo Demonstrativo:** [Link do YouTube Aqui]

---

## 🔹 Funcionalidades Principais

- **Processamento Multimodal:** Aceita entrada de texto direta e/ou upload de arquivos (**PDF/TXT**).
- **Classificação Inteligente:** Separa emails críticos de mensagens de "Feliz Natal" ou agradecimentos.
- **Geração de Resposta:** Cria rascunhos profissionais automáticos no mesmo idioma do email original.
- **Interface de Alta Usabilidade (UX):**
  - Sistema de Autenticação (Login/Logout).
  - Drag & Drop para arquivos com validação de formato e tamanho (2MB).
  - Feedback visual de processamento (Loading states).
  - Recurso de "Clique para Copiar" a resposta sugerida.

---

## 🛠 Arquitetura e Decisões Técnicas

A aplicação foi construída seguindo princípios de **Clean Architecture** e **Modularidade**:

- **Backend:** Django, estruturado em Apps para separação de responsabilidades.
- **Orquestração de IA:** Utilização da biblioteca **LlamaIndex** para gerenciar o fluxo de dados entre o usuário e os modelos de linguagem.
- **Agentes Especializados:** O sistema utiliza dois agentes distintos (Classifier e Responder), cada um com prompts de sistema otimizados para evitar alucinações.
- **Structured Outputs:** Implementação de saídas estruturadas via **Pydantic/JSON Mode**, garantindo que a comunicação entre a IA e o Backend seja sempre estável e tipada.
- **LLMs:** \* **Produção:** Llama-3.3-70B (via Groq Cloud) para altíssima performance e baixa latência.
  - **Desenvolvimento:** Llama-3.1-8B (via Ollama) para testes locais e privacidade.

---

## ⚡ Estrutura do Repositório

```text
├── backend
│   ├── apps
│   │   ├── ai            # Core da IA: Agentes, Prompts, Schemas e Orquestrador
│   │   ├── emails        # Lógica de negócio, Views e Processamento de arquivos
│   │   └── users         # Autenticação e Gestão de usuários
│   ├── services          # Utilitários de arquivo e orquestração de sistema
│   ├── templates         # Interface Web (Django Templates + Vanilla JS)
│   └── manage.py
├── .github/workflows
└── requirements.txt      # Dependências (Django, LlamaIndex, Groq, PyPDF2)
```

---

## 💻 Instalação Local

### 1️⃣ Requisitos

- Python 3.10+
- Ollama (opcional para rodar localmente)

### 2️⃣ Configuração

```bash
# Clone o repositório
git clone https://github.com/SeuUsuario/Email-AI-Classifier
cd email-ai-classifier/backend

# Virtualenv
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Dependências
pip install -r requirements.txt
```

### 3️⃣ Variáveis de Ambiente

Crie um arquivo `.env` na pasta `backend/` e adicione sua chave (se for usar Groq):

```env
GROQ_API_KEY=sua_chave_aqui
SECRET_KEY=sua_chave_django
DEBUG=True
```

### 4️⃣ Execução

```bash
python manage.py migrate
python manage.py runserver
```

---

## 📈 Evoluções Futuras (Roadmap)

Se este projeto fosse escalado para um ambiente corporativo de grande porte, as próximas etapas seriam:

1.  **Processamento Assíncrono:** Uso de Celery/Redis para processar arquivos muito pesados sem travar a interface.
2.  **Fine-Tuning:** Treinar o modelo com o histórico real de emails da empresa para captar gírias e termos técnicos específicos do setor financeiro.
3.  **Integração via API:** Conectar diretamente com Microsoft Graph (Outlook) ou Gmail API para leitura automática da caixa de entrada.
4.  **Hospedagem Enterprise:** Migração para AWS (ECS/Fargate) com auto-scaling.
