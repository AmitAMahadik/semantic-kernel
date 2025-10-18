import asyncio
from azure.identity import AzureCliCredential
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

async def main():
    # Initialize a chat agent with basic instructions
    # Using Azure CLI authentication (no API key needed)
    agent = ChatCompletionAgent(
        service=AzureChatCompletion(
            credential=AzureCliCredential(),
            deployment_name="demo-gpt-4.1-nano",  # This is the Azure deployment name
            endpoint="https://oai-demo-search.openai.azure.com/",
        ),
        name="Agent_Smith",  # Agent name (no periods allowed)
        instructions="You are a helpful assistant.",
    )

    # Get a response to a user message
    response = await agent.get_response(messages="Write a haiku about Semantic Kernel.")
    print(response.content)

asyncio.run(main()) 

# Output:
# Language's essence,
# Semantic threads intertwine,
# Meaning's core revealed.