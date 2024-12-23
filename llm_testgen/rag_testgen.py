from llm_testgen.config_testgen import config

from langchain_aws import ChatBedrockConverse
from langchain_aws import BedrockEmbeddings
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper

from ragas.testset import TestsetGenerator

from base_func.extract_data_aws import extract_documents_from_s3

generator_llm = LangchainLLMWrapper(ChatBedrockConverse(
    credentials_profile_name=config["credentials_profile_name"],
    region_name=config["region_name"],
    base_url=f"https://bedrock-runtime.{config['region_name']}.amazonaws.com",
    model=config["llm"],
    temperature=config["temperature"],
))
generator_embeddings = LangchainEmbeddingsWrapper(BedrockEmbeddings(
    credentials_profile_name=config["credentials_profile_name"],
    region_name=config["region_name"],
    model_id=config["embeddings"],
))

def rag_testgen():
    generator = TestsetGenerator(llm=generator_llm, embedding_model=generator_embeddings)

    docs = extract_documents_from_s3(bucket_name=config["aws_s3_bucket"], prefix="your-prefix")
    dataset = generator.generate_with_langchain_docs(docs, testset_size=10)

    return dataset.to_pandas()
