from openai import AsyncOpenAI

from app.llm.models import LLMRequest, LLMResponse
from app.llm.provider import LLMProvider


class OpenAIProvider(LLMProvider):
    """OpenAI chat completions adapter."""

    def __init__(
        self,
        *,
        api_key: str,
        default_model: str = "gpt-4o-mini",
        client: AsyncOpenAI | None = None,
    ) -> None:
        self._default_model = default_model
        self._client = client or AsyncOpenAI(api_key=api_key)

    async def generate(self, request: LLMRequest) -> LLMResponse:
        model = request.model or self._default_model
        payload: dict[str, object] = {
            "model": model,
            "messages": [
                {"role": message.role, "content": message.content}
                for message in request.messages
            ],
        }
        if request.temperature is not None:
            payload["temperature"] = request.temperature

        response = await self._client.chat.completions.create(**payload)
        choice = response.choices[0]
        usage = response.usage

        return LLMResponse(
            content=choice.message.content or "",
            model=response.model,
            prompt_tokens=usage.prompt_tokens if usage else None,
            completion_tokens=usage.completion_tokens if usage else None,
        )
