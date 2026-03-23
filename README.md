# 📧 Email Classifier

**Descrição:**
Solução web para **classificação automática de emails** e sugestão de respostas, liberando tempo da equipe de atendimento. A aplicação distingue emails **Produtivos** de **Improdutivos** e gera respostas automáticas usando IA.

---

## 🔹 Funcionalidades

- Upload de emails em **.txt** ou **.pdf** e/ou inserção direta de texto.
- Classificação automática do email em **Produtivo** ou **Improdutivo**.
- Geração de resposta sugerida baseada no conteúdo do email.
- UI moderna e interativa com:
  - Área de arrastar e soltar arquivos.
  - Hover em resultado para copiar a resposta com feedback visual.

- Limite de upload de arquivos configurável (1MB).
- Backend em **Django + Python**, com integração a IA para NLP.

---

## 🛠 Tecnologias

- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JS
- **IA/NLP:** Ollama - llama3.1
- **Deploy:** Heroku

---

## ⚡ Estrutura do Projeto

```
C:.
│   .prettierrc
│   db.sqlite3
│   manage.py
│   requirements.txt
│
├───apps
│   ├───ai
│   │   │   admin.py
│   │   │   apps.py
│   │   │   llm.py             # Cliente Ollama + integração Llama3.1
│   │   │   models.py
│   │   │   tests.py
│   │   │   views.py
│   │   │   __init__.py
│   │   │
│   │   ├───agents           # Agentes separados para classificação e resposta
│   │   ├───orchestrator     # Pipelines de processamento de emails
│   │   ├───prompts          # Prompts de classificação e resposta
│   │   └───schemas          # Schemas de entrada/saída do processamento
│   │
│   ├───core
│   ├───emails               # Upload, views, templates e serializers
│   └───users                # Sistema de login e autenticação
│
├───config                   # Configuração do Django (settings, urls, wsgi)
├───domain
├───services                 # Orquestrador e utils
└───templates                # Base HTML
```

---

## 🚀 Instalação Local

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/MarianaMendanha/Email-AI-Classifier
cd email-ai-classifier/backend
```

### 2️⃣ Crie e ative o ambiente virtual

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3️ Instale dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Rode migrações do Django

```bash
python manage.py migrate
```

### 5️⃣ Execute o servidor

```bash
python manage.py runserver
```

Acesse a aplicação em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 💡 Uso

1. Preencha o formulário:
   - Digite o **subject** e/ou **body** do email e/ou envie um arquivo `.txt` ou `.pdf`.

2. Clique em **Processar Email**.
3. O resultado aparecerá na caixa de resultado:
   - **Categoria**: Produtivo / Improdutivo
   - **Resposta sugerida**: texto gerado pela IA

4. Passe o mouse sobre a caixa de resultado para aparecer o ícone de **[copiar]** e clique para copiar a resposta.

---

## 🌐 Deploy

- **Heroku:** [https://www.heroku.com/](https://www.heroku.com/)

> link <>

---

## 📝 Licença
