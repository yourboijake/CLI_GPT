import openai
import argparse
import tiktoken
import json

CONTEXT_TOKEN_LIMIT = 3096 #gpt 3.5 turbo has 4096 context len. subtract 1000 for max_tokens in completion
SYSTEM_CONTEXT_PROMPT = "You are a helpful and succinct AI assistant."
context = [{"role": "system", "content": SYSTEM_CONTEXT_PROMPT}]

#set up credentials for OpenAI API
config_json = json.loads(open('/home/jacob/Desktop/Programming/AI/CLI_Tool/config.json', 'rb').read())
openai.organization = config_json['organization']
openai.api_key = config_json['api_key']

#boilerplate, runs GPT API call
def run_chat_completion(context_dict_list, model='gpt-3.5-turbo', temperature=0.2, max_tokens=1000):
    completion = openai.ChatCompletion.create(
        model=model,
        messages=context_dict_list,
        temperature=temperature,
        max_tokens=max_tokens)
    
    return completion.choices[0].message.content

#count number of tokens used in context
def count_context_tokens(context_dict_list):
    #convert all context in to a single string
    context_str = " ".join([d['content'] for d in context_dict_list])

    #encode and count number of tokens
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    num_tokens = len(encoding.encode(context_str))

    return num_tokens

#reduce number of tokens in context, using 1 of 2 methods:
# method 1: summarize the context with OpenAI API call
# method 2: cycle out previous prompts from context window 
def consolidate_prompt(context_dict_list, num_tokens, method='window'):
    if method == 'summarize':
        chat_summary_prompt = [{'role': 'system', 'content': 'summarize the following chat logs as concisely as possible.'}]
        chat_summary_prompt += context_dict_list
        summary_completion = run_chat_completion(chat_summary_prompt)
        new_context_dict_list = [{'role': 'system', 'content': SYSTEM_CONTEXT_PROMPT}, 
                                    summary_completion]
    elif method == 'window':
        new_context_dict_list = context_dict_list.copy()
        while num_tokens > CONTEXT_TOKEN_LIMIT and len(new_context_dict_list) >= 2:
            del new_context_dict_list[1]
            num_tokens = count_context_tokens(new_context_dict_list)
    return new_context_dict_list

#initialize context
print("welcome to CLI GPT. type 'quit' to exit chat session, or 'count' to count the number of tokens in the prompt context")
print('enter your prompt below')
while True:
    #retrieve prompt from user
    prompt = input("> ")
    if prompt == 'quit': break
    if prompt == 'count': 
        print(count_context_tokens(context))
        continue

    #append context to include user prompt
    prompt_dict = {"role": "user", "content": prompt}
    context.append(prompt_dict)

    #check/correct prompt context if too many tokens in context
    num_tokens = count_context_tokens(context)
    if num_tokens > CONTEXT_TOKEN_LIMIT:
        context = consolidate_prompt(context)

    #generate text completion
    completion = run_chat_completion(context)
    context.append({'role': "assistant", "content": completion})
    print(completion + '\n')

