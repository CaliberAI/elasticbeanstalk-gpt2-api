# AWS Elastic Beanstalk GPT-2 NLG API

Demo of deploying a Python Flask Connexion OpenAPI that generates natural language texts using Huggingface's GPT-2 transformer on AWS Elastic Beanstalk.

This demo uses the smallest GPT-2 model called `distilgpt2`. You can change this to `gpt-2` or `gpt2-medium` but note you will need a larger AWS isntance type with more memory.

## Run locally
- `python3 -m venv .`
- `source ./bin/activate`
- `pip install -r requirements.txt`
- `.ebextensions/download-model.sh`
- `python application.py`

## Deploy to AWS Elastic Beanstalk
- `brew install awsebcli`
- `eb init`
- `eb create eb-gpt2-api-production`
- `eb deploy`
- `eb open`