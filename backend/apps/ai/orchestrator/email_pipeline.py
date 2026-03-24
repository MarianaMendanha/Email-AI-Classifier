from apps.ai.agents.classifier_agent import ClassifierAgent
from apps.ai.agents.response_agent import ResponseAgent
from apps.ai.schemas.email_pipeline_result import EmailPipelineResult
from apps.ai.schemas.email_classification import EmailClassification
from apps.ai.schemas.email_response import EmailResponse
from apps.ai.prompts import (
    CLASSIFIER_PROMPT,
    RESPONSE_PROMPT,
)

import json

MAX_CHARS = 8000


def smart_truncate(text: str, max_length: int = MAX_CHARS) -> str:
    if len(text) <= max_length:
        return text

    print(
        f"[WARNING] Texto excede {max_length} caracteres. Aplicando corte...")

    head = max_length // 2
    tail = max_length // 2

    truncated_text = f"{text[:head]}\n\n[... PARTE DO TEXTO REMOVIDA POR TAMANHO ...]\n\n{text[-tail:]}"
    return truncated_text


classifier_agent = ClassifierAgent(system_prompt=CLASSIFIER_PROMPT)
response_agent = ResponseAgent(system_prompt=RESPONSE_PROMPT)


async def run_email_pipeline(full_text: str) -> EmailPipelineResult:
    print("\n================ EMAIL PIPELINE START ================")

    full_text = smart_truncate(full_text)
    print(f"[INPUT]\n{full_text}\n")

    try:
        # 1. Classificação
        print("[STEP 1] Running classifier agent...")
        classification = await classifier_agent.run(full_text)

        classification_dict = json.loads(
            classification)
        classification_obj = EmailClassification(
            **classification_dict)

        print(f"[DEBUG] Raw classification: {classification}")

        category = classification_obj.category.upper()

        print(f"[RESULT] Category: {category}")

        # fallback de segurança
        if category not in ["PRODUTIVO", "IMPRODUTIVO"]:
            print("[WARNING] Invalid category returned. Defaulting to IMPRODUTIVO")
            category = "IMPRODUTIVO"

        # 2. Geração de resposta
        print("\n[STEP 2] Running response agent...")

        response_input = f"""
                            Categoria do email: {category}

                            Email:
                            {full_text}
                        """

        print(f"[DEBUG] Response input:\n{response_input}")

        response = await response_agent.run(response_input)

        print(f"[DEBUG] Raw response: {response}")

        response_dict = json.loads(
            response)
        response_obj = EmailResponse(
            **response_dict)

        print(f"[DEBUG] Response subject: {response_obj.subject}")
        print(f"[DEBUG] Response body: {response_obj.body}")

        print("================ EMAIL PIPELINE END ================\n")

        return EmailPipelineResult(
            category=category,
            response=f"{response_obj.subject}\n\n{response_obj.body}",
        )

    except Exception as e:
        print("[ERROR] Pipeline failed:", str(e))
        return EmailPipelineResult(
            category="ERROR",
            response=f"Erro ao processar email: {str(e)}"
        )
