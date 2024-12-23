# Python Built-Ins:
from concurrent.futures import ThreadPoolExecutor
import json

# External Dependencies:
import boto3  # General Python SDK for AWS (including Bedrock)
from datasets import Dataset  # For use with Ragas
from langchain_community.embeddings import BedrockEmbeddings as LangChainBedrockEmbed
from langchain_aws import ChatBedrock as LangChainBedrock
import pandas as pd  # For working with tabular data
import ragas
# import sagemaker  # Just used for looking up default bucket
from tqdm.notebook import tqdm  # Progress bars

botosess = boto3.Session()
region = botosess.region_name
bedrock = botosess.client("bedrock")
br_agents_runtime = botosess.client("bedrock-agent-runtime")

from config import AWS_S3_BUCKET, KNOWLEDGE_BASE_ID, AWS_REGION, MODEL_NAME
from llm_testgen.rag_testgen import rag_testgen

# input generated data from extract_data_aws.py
# feed that data through RAG eval lib and the hosted and selected challenger model to get test data
y_test = rag_testgen()


# feed the test data to the LLM model to get the output
for i in y_test:
    rag_resp = br_agents_runtime.retrieve_and_generate(
        input={"text": "In what country is Normandy located?"},
        retrieveAndGenerateConfiguration={
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": KNOWLEDGE_BASE_ID,
                "modelArn": f"arn:aws:bedrock:{AWS_REGION}::foundation-model/{MODEL_NAME}",
            },
            "type": "KNOWLEDGE_BASE",
        },
        # Optional session ID can help improve results for follow-up questions:
        # sessionId='string'
    )

    print("Plain text response:")
    print("--------------------")
    print(rag_resp["output"]["text"], end="\n\n\n")

    print("Full API output:")
    print("----------------")
    rag_resp



# compare the output with the original data to get the metrics
y_test vs y_pred