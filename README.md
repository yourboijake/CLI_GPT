This is a simple script to add GPT to your terminal.

The openai_session.py file establishes a chat session with Chat GPT 3.5 turbo, then allows the user to engage with GPT 3.5 in a similar way to the online chat interface users may be familiar with.
The openai_session script handles issues relating to the context, cycling previous prompts out of the chat context where the number of tokens reaches a point at which the GPT3.5 context prompt length might be exceeded.

Linux Instructions:
- clone this repo
- edit the bash file to the appropriate global path to the repo location
- move the bash script to your /usr/local/bin folder to make the "askgpt" command globally accessible
(assuming /usr/local/bin is in your $PATH)
