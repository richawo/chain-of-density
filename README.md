Here is the README with a TODO list added:

# Chain-of-Density 

This project implements the chain-of-density text summarization approach from the paper ["From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting"](https://arxiv.org/pdf/2309.04269.pdf) by researchers at Salesforce, MIT, Columbia, etc.

It implementation takes a long text input (e.g. articles, blogs, whitepapers, documents), extracts important entities, and iteratively generates increasingly concise and entity-dense summaries.

## Usage

To run the summarizer:

1. Install dependencies:

```
poetry install 
```

2. Create a .env file and set your OpenAI API key:

```
OPENAI_API_KEY=<your-key>
```

3. Update config.ini with the input text file path and output location.

4. Run the summarizer: 

```
poetry run cod
```

This will load the input text, run the chain-of-density summarization, and save the output to the configured file.

## Implementation

The main logic is in main.py. It:

- Loads the input text
- Gets the OpenAI API key from the .env file  
- Sends a prompt to the OpenAI API with the text
- Gets back a chain of 5 increasingly dense summaries
- Exports the result to the .txt

The prompt largely follows the methodology outlined in the paper aside from minor adjustments. 

Config options like input/output paths are stored in config.ini.

## TODO

- Parse output as JSON
- Collate the list of entities and additional missing entities
- Allow for the sequential merging and summarisations of multiple inputs

## References

- ["From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting"](https://arxiv.org/pdf/2309.04269.pdf)
- ["Annotated + Unannotated CoD Summaries on Hugging Face"](https://huggingface.co/datasets/griffin/chain_of_density/)