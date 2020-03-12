# AWS Elastic Beanstalk GPT-2 NLG API

Demo of deploying a Python Flask Connexion OpenAPI that generates natural language texts using Huggingface's GPT-2 transformer on AWS Elastic Beanstalk.

## Run locally
- `python3 -m venv .`
- `source ./bin/activate`
- `pip install -r requirements.txt`
- `.ebextensions/download-model.sh`
- `python application.py`

## Deploy to AWS Elastic Beanstalk
- `brew install awsebcli`
- `eb init`
- `eb create`
- `eb deploy`
- `eb open`