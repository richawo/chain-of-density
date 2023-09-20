import openai
from .chat_completion import make_chat_completion_request
import os
import configparser
from .msg_templates import create_system_message

# Load config file and setup variables
here = os.path.abspath(os.path.dirname(__file__))
config = configparser.ConfigParser()
config.read("config.ini")
openai.api_key = os.getenv("OPENAI_API_KEY")


def perform_checks():
    # Check if OPENAI_API_KEY is set
    if "OPENAI_API_KEY" not in os.environ:
        raise EnvironmentError("OPENAI_API_KEY environment variable is not set.")

    input_file_path = config["DEFAULT"]["INPUT_FILE"]
    if (
        not (
            os.path.exists(input_file_path)
            or os.path.exists(os.path.join(here, input_file_path))
        )
        or input_file_path == ""
    ):
        raise FileNotFoundError(f"Input file not found at path: {input_file_path}")

    print("Checks passed")


def load_file():
    input_file_path = config["DEFAULT"]["INPUT_FILE"]

    if os.path.exists(input_file_path):
        # Load input file
        with open(input_file_path, "r") as f:
            return f.read()
    elif os.path.exists(os.path.join(here, input_file_path)):
        # Load input file from main folder
        with open(f"{os.path.join(here, input_file_path)}", "r") as f:
            return f.read()
    else:
        raise FileNotFoundError(f"Input file not found at path: {input_file_path}")


def main():
    # Perform sense checks
    perform_checks()

    # Get system message
    msg = create_system_message(config)

    # Load input file
    input_text = load_file()

    msg.append(
        {
            "role": "user",
            "content": f"Here is the input text for you to summarise using the 'Missing_Entities' and 'Denser_Summary' approach:\n\n{input_text}",
        }
    )

    completion = make_chat_completion_request(config, msg, n=1)
    content  = completion["choices"][0]["message"]["content"]
    print(content)

    # Write the output to file
    with open(config["DEFAULT"]["OUTPUT_FILE"], "w") as f:
        f.write(content)


