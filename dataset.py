"""
Resources: 
- https://huggingface.co/learn/llm-course/chapter5/1?fw=pt
- https://huggingface.co/docs/datasets/loading#local-and-remote-files 

Universal Dataloader to load datasets from local files to HF datasets

Must work with any type that is supported by the Hugging Face datasets library.
# Text based datasets:
- CSV
- JSON
- Parquet
- Text
- Arrow
- SQL
- WebDataset
- Pandas (.pkl)

# Potentially expand to other modes: image, audio, video, etc.
"""
import datasets

class Dataset: # this can probably be a function instead of a class
    """"""