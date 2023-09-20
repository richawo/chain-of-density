import openai
import time

def make_chat_completion_request(
    config,
    messages,
    temperature=1.0,
    top_p=1.0,
    n=1,
    stream=False,
    stop=None,
    max_tokens=None,
    presence_penalty=0,
    frequency_penalty=0,
    functions=[],
    function_call="auto"
):
    
    parameters = {
        "model": config["DEFAULT"]["MODEL"],
        "messages": messages,
        "temperature": temperature,
        "top_p": top_p,
        "n": n,
        "stream": stream,
        "stop": stop,
        "max_tokens": max_tokens,
        "presence_penalty": presence_penalty,
        "frequency_penalty": frequency_penalty,
    }

    if functions is not None and len(functions) > 0:
        parameters["functions"] = functions
        parameters["function_call"] = function_call

    
    max_attempts = 10  # Maximum number of retry attempts
    retry_gap = 3.0  # Initial gap between retries in seconds

    for attempt in range(max_attempts):
        try:
            completion = openai.ChatCompletion.create(**parameters)
            return completion
        except Exception as e:
            print(f"Request failed on attempt {attempt + 1}. Error: {str(e)}")
            if attempt < max_attempts - 1:
                retry_gap *= 1.5  # Increase the retry gap exponentially
                time.sleep(retry_gap)
    
    return None  # If all retry attempts fail
