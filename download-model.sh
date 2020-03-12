#!/bin/bash
mkdir distilgpt2
wget https://s3.amazonaws.com/models.huggingface.co/bert/distilgpt2-config.json -O distilgpt2/config.json
wget https://s3.amazonaws.com/models.huggingface.co/bert/distilgpt2-pytorch_model.bin -O distilgpt2/pytorch_model.bin
wget https://s3.amazonaws.com/models.huggingface.co/bert/distilgpt2-vocab.json -O distilgpt2/vocab.json
wget https://s3.amazonaws.com/models.huggingface.co/bert/distilgpt2-merges.txt -O distilgpt2/merges.txt
