# here is main.py


from myllmservice import  MyLLMService
import re
from tqdm import tqdm

def merge_paragraphs(paragraphs, output_file='output.txt'):
    # Join the list of paragraphs with two newlines as separators
    merged_text = '\n\n'.join(paragraphs)

    # Write the merged text to a .txt file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(merged_text)

    print(f"Text has been saved to {output_file}")



def read_paragraphs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Normalize line endings
        content = content.replace('\r\n', '\n').replace('\r', '\n')
        # First split on two or more newlines
        temp_paragraphs = re.split(r'\n\s*\n', content)
        final_paragraphs = []
        for para in temp_paragraphs:
            # Further split on indentation if necessary
            sub_paras = re.split(r'\n(?=\s)', para)
            for sub_para in sub_paras:
                clean_para = sub_para.strip()
                if clean_para:
                    final_paragraphs.append(clean_para)
        return final_paragraphs




def simple_test():
    my_llm_service = MyLLMService()
    generation_result = my_llm_service.translate_to_russian("hey what you doing" )
    print(generation_result)
    print(" ")
    print(generation_result.content)
    print(" ")


def main():
    file_path = 'Toplam.txt'
    paragraphs = read_paragraphs(file_path)

    my_llm_service=MyLLMService()

    translated_paragraphs=[]
    for p in tqdm(paragraphs):

        r=my_llm_service.translate_to_russian(p)
        translated_paragraphs.append(r.content)


    merge_paragraphs(translated_paragraphs)



if __name__ == '__main__':
    main()








# def process_statements_sync(statements):
#     service = MyLLMService()
#
#     for idx, statement in enumerate(statements):
#         result = service.translate_to_russian(input_paragraph=statement, request_id=idx)
#         if result.success:
#             print(f"Translated content: {result.content}")
#         else:
#             print(f"Error: {result.error_message}")






# import asyncio
#
# async def process_bank_statements(bank_statements):
#     service = MyLLMService()
#     tasks = []
#
#     for idx, statement in enumerate(bank_statements):
#         task = service.translate_to_russian_async(input_paragraph=statement, request_id=idx)
#         tasks.append(task)
#
#     results = await asyncio.gather(*tasks, return_exceptions=True)
#
#     for result in results:
#         if isinstance(result, Exception):
#             print(f"Error processing statement: {result}")
#         else:
#             print(f"Processed result: {result.content}")
#
# # Assuming bank_statements is a list of strings
# bank_statements = ["Statement 1", "Statement 2", "Statement 3", ...]  # List of statements
#
# asyncio.run(process_bank_statements(bank_statements))

