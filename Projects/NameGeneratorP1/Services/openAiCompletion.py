import openai
import os


def textCompletionService(prompt: str):
    # set up your OpenAI API key
    openai.api_key = os.environ['API_KEY_OPENAPI']
    limit = int(os.environ['GAMERTAGS_LIMIT'])

    # Define the parameters for the OpenAI GPT-3 API request
    # For more details: https://platform.openai.com/docs/api-reference/completions
    model_engine = "text-davinci-002"
    max_tokens = 50
    temperature = 0.5
    top_p = 1.0
    frequency_penalty = 0.5
    presence_penalty = 0.5

    # Make the API request
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        n=1,
        stop=None
    )
    return response


