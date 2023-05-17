This is a simple script to add GPT to your terminal.

The openai_session.py file establishes a chat session with Chat GPT 3.5 turbo, then allows the user to engage with GPT 3.5 in a similar way to the online chat interface users may be familiar with.
The openai_session script handles issues relating to the context, cycling previous prompts out of the chat context where the number of tokens reaches a point at which the GPT3.5 context prompt length might be exceeded.

Linux Instructions:
- clone this repo
- create a "config.json" file, containing api_key and organization
- edit the bash file to the appropriate global path to the repo location
- move the bash script to your /usr/local/bin folder to make the "askgpt" command globally accessible
(assuming /usr/local/bin is in your $PATH)

Example chat session:
```console
jacob@jacob-ThinkPad-T440p:~/Desktop/Programming/AI/CLI_Tool$ askgpt
welcome to CLI GPT. type 'quit' to exit chat session, or 'count' to count the number of tokens in the prompt context
enter your prompt below
> Hi GPT! Tell me about Immanuel Kant
Immanuel Kant was an 18th-century German philosopher who is widely considered to be one of the most important figures 
in modern philosophy. He is known for his works on ethics, metaphysics, epistemology, and aesthetics, among other topics. 
Kant's philosophy is characterized by his emphasis on reason and the importance of the individual's ability to think for 
themselves. He is perhaps best known for his concept of the "categorical imperative," which is a moral principle that 
states that one should always act in a way that could be made into a universal law.

> count
131
> quit
```
