import asyncio
from apps.ai.orchestrator.email_pipeline import run_email_pipeline
from apps.ai.schemas.email_pipeline_result import EmailPipelineResult


def process_email(full_text: str) -> dict:
    """
    Processa o email usando o pipeline e retorna um dict seguro.
    """
    try:
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        result = loop.run_until_complete(run_email_pipeline(full_text))
        return result.model_dump()

    except Exception as e:
        return {
            "category": "ERROR",
            "response": str(e),
        }
