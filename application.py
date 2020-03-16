import os
import connexion
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

cwd = os.getcwd()
model_path = cwd + '/distilgpt2'
model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)


def generate(seed):
    input_ids = torch.tensor(tokenizer.encode(seed)).unsqueeze(0)
    outputs = model.generate(input_ids=input_ids, max_length=200)
    return(tokenizer.decode(outputs[0], skip_special_tokens=True))


application = connexion.App(__name__, specification_dir='.')
application.add_api('api.yaml')

if __name__ == "__main__":
    application.run()
