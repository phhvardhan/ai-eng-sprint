Step 1: User sends a prompt to the LLM (What's the weather in Dallas?)
step-2: LLM identifies the appropriate tool and generates structured arguments
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            },
            "required": ["city"]
        }
    }
}]
    )

step-3: the LLM uses Tool call to look for the city weather 
{
    "name": "weather",
    "arguments": {
        "a": dallas,
    }
}

step-4: Application executes the tool and returns the result
weather = weather("dallas")

step-5 : Weather is XX in Dallas



1. LLM is usually built on basic english and works in a concept called tokenization and when telugu is used it needs more tokenization to split the wordings and understand the sentence in some cases it even might be single letter which incereases the usage of more tokens 
2. the words in prod-sku-7841x is scramblled in multiple parts it is needed to work per tokens and same tokenization works here for the model to understrand the word need to split into tokens since prod can be derivated to production the llm needs understanding of - and sku etc which uses more tokens and as we pay per tokens not words it can increase the costs 