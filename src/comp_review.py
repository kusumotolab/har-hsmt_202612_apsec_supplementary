"""Source code used to run STEP 1 and STEP 2 of the completeness review with an LLM.
 
This script was used for the evaluation reported in the paper. It sends a system
prompt and 14 prompts to the LLM in order as a single multi-turn conversation,
and saves the output of each turn together with the total execution time.
 
The contents of prompt1 to prompt14 have been removed from this file because they
contained confidential project data. The prompts themselves are published in
prompts/prompts_ja.md (as used in the paper) and prompts/prompts_en.md (English
translation). This file is provided for reference and is not intended to be run as is.
"""
 
from openai import OpenAI
from dotenv import load_dotenv
import time
import os
 
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
 
MODEL = "gpt-5"
 
# System prompt used in the paper (in Japanese).
# English translation:
#   You are an expert in software requirements definition and review.
#   You will now receive 14 prompts in sequence.
#   Taking into account each prompt and all of your own previous responses,
#   provide consistent responses.
SYSTEM_PROMPT = """
あなたはソフトウェア要件定義とレビューの専門家です。
これから、14個のプロンプトを順番に受け取ります。
それぞれのプロンプトと、あなた自身の過去の回答をすべて踏まえて、一貫した回答をしてください。
""".strip()
 
# prompt1 to prompt14 are defined here as string variables.
# Their contents correspond to Turns 1 to 14 in prompts/prompts_ja.md,
# with the meeting minutes and the SRS inserted at the placeholder positions.
# (Removed for confidentiality.)
 
 
def main():
    start_time = time.time()
 
    # The conversation history is accumulated so that each prompt is answered
    # in the context of all previous prompts and responses.
    conversation = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
 
    results = {}
 
    for i in range(1, 15):
        prompt_var_name = f"prompt{i}"
        out_var_name = f"out{i}"
 
        prompt_value = globals().get(prompt_var_name)
 
        if not prompt_value:
            print(f"[Warning] {prompt_var_name} is empty. Skipping.")
            results[out_var_name] = None
            continue
 
        print(f"=== Running {prompt_var_name} ===")
 
        conversation.append({"role": "user", "content": prompt_value})
 
        response = client.responses.create(
            model=MODEL,
            reasoning={"effort": "high"},
            input=conversation
        )
 
        output = response.output_text
 
        conversation.append({"role": "assistant", "content": output})
 
        results[out_var_name] = output
 
        print(f"--- {out_var_name} ---")
        print(output)
 
    end_time = time.time()
    execution_time = end_time - start_time
 
    with open("experiment_outputs_out1_to_out14.txt", "w", encoding="utf-8") as f:
        for i in range(1, 15):
            key = f"out{i}"
            value = results.get(key)
 
            f.write(f"{key}\n")
            if value is None:
                f.write("(No output for this turn)\n\n")
                continue
 
            f.write(value)
            if not value.endswith("\n"):
                f.write("\n")
            f.write("\n")
 
        f.write("execution_time\n")
        f.write(f"{execution_time:.2f} seconds\n")
 
    print("=== Done: results saved to experiment_outputs_out1_to_out14.txt ===")
 
 
if __name__ == "__main__":
    main()
 