from llama_index.core.llms import ChatMessage
from apps.ai.llm import get_llm
from apps.ai.schemas.email_response import EmailResponse


class ResponseAgent:
    def __init__(self, system_prompt: str):
        llm = get_llm()
        self.llm = llm.as_structured_llm(EmailResponse)
        self.system_prompt = system_prompt

    async def run(self, text: str) -> EmailResponse:
        messages = [
            ChatMessage(role="system", content=self.system_prompt),
            ChatMessage(role="user", content=text),
        ]

        response = await self.llm.achat(messages)

        return response.message.content
