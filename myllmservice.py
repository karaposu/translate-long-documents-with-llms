from llmservice.base_service import BaseLLMService
from llmservice.generation_engine import GenerationEngine, GenerationRequest, GenerationResult
import logging

from typing import Optional, Union

class MyLLMService(BaseLLMService):
    def __init__(self, logger=None):
        super().__init__(logger=logger)
        self.generation_engine = GenerationEngine(logger=self.logger, model_name="gpt-4")
        self.generation_engine.load_prompts('prompts.yaml')

    def translate_to_russian(self, input_paragraph: str, request_id: Optional[Union[str, int]] = None) -> GenerationResult:
        data_for_placeholders = {'input_paragraph': input_paragraph}
        order = ["input_paragraph", "translate_to_russian"]

        unformatted_prompt = self.generation_engine.craft_prompt(data_for_placeholders, order)

        generation_request = GenerationRequest(
            data_for_placeholders=data_for_placeholders,
            unformatted_prompt=unformatted_prompt,
            output_type="str",
            use_string2dict=False,
            operation_name="translate_to_russian",
            request_id=request_id
        )

        generation_result = self.generation_engine.generate_output(generation_request)

        return generation_result
