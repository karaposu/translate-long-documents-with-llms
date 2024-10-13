import asyncio
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

async def main():
    file_path = 'Toplam.txt'
    paragraphs = read_paragraphs(file_path)
    my_llm_service = MyLLMService()

    tasks = []
    for idx, paragraph in enumerate(paragraphs):
        # Schedule the translation asynchronously
        task = asyncio.create_task(
            my_llm_service.translate_to_russian_async(paragraph, request_id=idx)
        )
        tasks.append(task)

    # Prepare a list to store results in the original order
    translated_paragraphs = [None] * len(paragraphs)

    # Use tqdm to show progress
    for future in tqdm(asyncio.as_completed(tasks), total=len(tasks)):
        try:
            result = await future
            idx = result.request_id
            if result.success:
                translated_paragraphs[idx] = result.content
            else:
                print(f"Error in request {idx}: {result.error_message}")
                translated_paragraphs[idx] = ""
        except Exception as e:
            print(f"Exception occurred: {e}")
            # Handle exception and assign empty string to maintain order
            translated_paragraphs[idx] = ""

    merge_paragraphs(translated_paragraphs)

if __name__ == '__main__':
    asyncio.run(main())
