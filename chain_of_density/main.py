import openai
import os
import configparser
from .msg_templates import create_system_message


def perform_checks():
    # Check if OPENAI_API_KEY is set
    if "OPENAI_API_KEY" not in os.environ:
        raise EnvironmentError("OPENAI_API_KEY environment variable is not set.")

    print("Checks passed")


def main():
    perform_checks()

    # Initialize config file
    config = configparser.ConfigParser()
    config.read("config.ini")

    # Get system message
    sys_msg = create_system_message(config)

    # Load input file
    here = os.path.abspath(os.path.dirname(__file__))
    input_file_path = config["DEFAULT"]["INPUT_FILE"]
    input_text = ""
    print(os.path.join(here, input_file_path))
    
    if os.path.exists(input_file_path):
        # Load input file
        with open(input_file_path, "r") as f:
            input_text = f.read()
    elif os.path.exists( os.path.join(here, input_file_path)):
        # Load input file from main folder
        with open(f'{os.path.join(here, input_file_path)}', "r") as f:
            input_text = f.read()
    else:
        raise FileNotFoundError(f"Input file not found at path: {input_file_path}")

    print(input_text)
        
        

    # Initialize OpenAI API
    openai.api_key = os.getenv("OPENAI_API_KEY")

