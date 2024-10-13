# my_llm_service.py

import asyncio
from llmservice.base_service import BaseLLMService
from llmservice.generation_engine import GenerationRequest, GenerationResult
from typing import Optional, Union


# add default model param to init.

class MyLLMService(BaseLLMService):
    def __init__(self, logger=None, max_concurrent_requests=5):
        super().__init__(
            logger=logger,
            model_name="gpt-4o",
            yaml_file_path='prompts.yaml',
            max_rpm=60,
            max_concurrent_requests=max_concurrent_requests,
        )
        # No need for a semaphore here, it's handled in BaseLLMService

    def translate_to_russian(self, input_paragraph: str, request_id: Optional[Union[str, int]] = None) -> GenerationResult:
        data_for_placeholders = {'input_paragraph': input_paragraph}
        order = ["input_paragraph", "translate_to_russian"]

        unformatted_prompt = self.generation_engine.craft_prompt(data_for_placeholders, order)

        generation_request = GenerationRequest(
            data_for_placeholders=data_for_placeholders,
            unformatted_prompt=unformatted_prompt,
            model="gpt-4o",
            output_type="str",
            use_string2dict=False,
            operation_name="translate_to_russian",
            request_id=request_id
        )

        # Execute the generation synchronously
        generation_result = self.execute_generation(generation_request)
        return generation_result

    async def translate_to_russian_async(self, input_paragraph: str, request_id: Optional[Union[str, int]] = None) -> GenerationResult:
        # Concurrency control is handled in BaseLLMService
        data_for_placeholders = {'input_paragraph': input_paragraph}
        order = ["input_paragraph", "translate_to_russian"]

        unformatted_prompt = self.generation_engine.craft_prompt(data_for_placeholders, order)

        generation_request = GenerationRequest(
            data_for_placeholders=data_for_placeholders,
            unformatted_prompt=unformatted_prompt,
            model="gpt-4o-mini",
            output_type="str",
            use_string2dict=False,
            operation_name="translate_to_russian",
            request_id=request_id
        )

        # Execute the generation asynchronously
        generation_result = await self.execute_generation_async(generation_request)
        return generation_result
