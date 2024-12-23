# configurations for AWS Bedrock or Azure OpenAI's API

import os

# AWS configurations
AWS_S3_BUCKET = 'your-default-bucket-name'
AWS_REGION = 'your-default-region'
AWS_BEDROCK_ENDPOINT = 'your-bedrock-endpoint'
KNOWLEDGE_BASE_ID = 'your-knowledge-base-id' # https://console.aws.amazon.com/bedrock/home?#/knowledge-bases
MODEL_NAME = "anthropic.claude-3-sonnet-20240229-v1:0" # https://console.aws.amazon.com/bedrock/home?#/foundation-models"