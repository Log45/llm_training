# llm_training

## Goals:

Make an app that is able to plug and play train LLMs on your machine (eventually connected to cloud)

Final goal: similar to LM Studio (lmstudio.ai) 

First step: Pipeline for training model locally with local data, and then compare to original with some testing data.

- User registration
- Multiple projects

## Plan:

1. Make a CLI that will take the model name, local dataset, and training parameters and run training
    - Create class for converting local datasets to HF Dataset
    - Create a class to load the proper model and tokenizer and utilize training and inference functions 
2. Utilize either Gradio or Streamlit to create a frontend