"""
Examples of different ways to configure AzureChatCompletion for ChatCompletionAgent.
Choose the approach that best fits your needs.
"""

import asyncio
from azure.identity import AzureCliCredential
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion


# ========================================
# OPTION 1: Using Environment Variables
# ========================================
# Create a .env file in this directory with:
#   GLOBAL_LLM_SERVICE="AzureOpenAI"
#   AZURE_OPENAI_API_KEY="your-api-key"
#   AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
#   AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="gpt-4"
#   AZURE_OPENAI_API_VERSION="2024-02-15-preview"

async def example_env_variables():
    agent = ChatCompletionAgent(
        service=AzureChatCompletion(),  # Reads from environment variables automatically
        name="Assistant",
        instructions="You are a helpful assistant.",
    )
    response = await agent.get_response(messages="Hello!")
    print(response.content)


# ========================================
# OPTION 2: Using Azure CLI Authentication
# ========================================
# Requires: az login (one-time setup)
# Best for: Development when you're already logged into Azure CLI

async def example_azure_cli_auth():
    agent = ChatCompletionAgent(
        service=AzureChatCompletion(
            credential=AzureCliCredential(),
            deployment_name="gpt-4",  # Your deployment name
            endpoint="https://your-resource.openai.azure.com/",
        ),
        name="Assistant",
        instructions="You are a helpful assistant.",
    )
    response = await agent.get_response(messages="Hello!")
    print(response.content)


# ========================================
# OPTION 3: Using API Key (Explicit)
# ========================================
# Best for: Production or when you need full control

async def example_explicit_api_key():
    from azure.core.credentials import AzureKeyCredential
    
    agent = ChatCompletionAgent(
        service=AzureChatCompletion(
            api_key="your-api-key-here",  # Or use AzureKeyCredential
            deployment_name="gpt-4",
            endpoint="https://your-resource.openai.azure.com/",
            api_version="2024-02-15-preview",
        ),
        name="Assistant",
        instructions="You are a helpful assistant.",
    )
    response = await agent.get_response(messages="Hello!")
    print(response.content)


# ========================================
# OPTION 4: Using Environment File Path
# ========================================

async def example_custom_env_file():
    agent = ChatCompletionAgent(
        service=AzureChatCompletion(
            env_file_path="/path/to/your/.env",  # Custom path to .env file
        ),
        name="Assistant",
        instructions="You are a helpful assistant.",
    )
    response = await agent.get_response(messages="Hello!")
    print(response.content)


if __name__ == "__main__":
    # Uncomment the example you want to try:
    # asyncio.run(example_env_variables())
    # asyncio.run(example_azure_cli_auth())
    # asyncio.run(example_explicit_api_key())
    # asyncio.run(example_custom_env_file())
    print("Choose an example to run by uncommenting one of the asyncio.run() lines above.")

