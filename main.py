# here is main.py


from myllmservice import  MyLLMService

my_llm_service=MyLLMService()

generation_result = my_llm_service.translate_to_russian("hey what you doing" )

print(generation_result.content)

#
# # from llm_service import LLMService
# import time
# import re
#
# def merge_paragraphs(paragraphs, output_file='output.txt'):
#     # Join the list of paragraphs with two newlines as separators
#     merged_text = '\n\n'.join(paragraphs)
#
#     # Write the merged text to a .txt file
#     with open(output_file, 'w', encoding='utf-8') as file:
#         file.write(merged_text)
#
#     print(f"Text has been saved to {output_file}")
#
#
#
# def read_paragraphs(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#         # Normalize line endings
#         content = content.replace('\r\n', '\n').replace('\r', '\n')
#         # First split on two or more newlines
#         temp_paragraphs = re.split(r'\n\s*\n', content)
#         final_paragraphs = []
#         for para in temp_paragraphs:
#             # Further split on indentation if necessary
#             sub_paras = re.split(r'\n(?=\s)', para)
#             for sub_para in sub_paras:
#                 clean_para = sub_para.strip()
#                 if clean_para:
#                     final_paragraphs.append(clean_para)
#         return final_paragraphs
#
# # Example usage
# file_path = 'Toplam.txt'
# paragraphs = read_paragraphs(file_path)
# print(len(paragraphs))
#
# llmservice= LLMService()
# # r=generation_engine.translate_to_russian(paragraphs[4])
# # print(r)
#
# translated_paragraphs=[]
# for p in tqdm(paragraphs):
#
#     r=llmservice.translate_to_russian(p)
#     translated_paragraphs.append(r.content)
#     # time.sleep()
#
# merge_paragraphs(translated_paragraphs)
#
# # print(paragraphs[4])
#



#
# #here is llm_service.py
#
# from typing import Optional, Dict, Any
# import logging
# from datetime import datetime
# import os
# from generation_engine import GenerationEngine
# from usage_stats import UsageStats
#
#
# def indent_log_pretty(logger_object, dictonary, lvl):
#     for key, value in dictonary.items():
#         logger_object.debug(f"{key}: %s", {value}, lvl=lvl)
#
#
# class LLMService:
#     def __init__(self, logger=None, allowed_models: Optional[list] = None):
#         self.logger = logger
#         # self.allowed_models = allowed_models or ['gpt-4o-2024-08-06']
#         self.allowed_models = allowed_models or ['gpt-4o-mini']
#         self.usage_stats = UsageStats()
#
#         self.gm = GenerationEngine(logger=self.logger,model_name=self.allowed_models[0])
#
#     def reset_usage(self):
#         self.usage_stats = UsageStats()
#
#     def translate_to_russian(self, input_paragraph):
#
#         data_for_placeholders = {
#             'input_paragraph': input_paragraph,
#         }
#         order = ["input_paragraph", "translate_to_russian"]
#
#         unformatted_prompt = self.gm.craft_prompt(data_for_placeholders, order)
#
#         generation_result = self.gm.generate_output(unformatted_prompt, data_for_placeholders)
#
#         return generation_result
#
#
#

