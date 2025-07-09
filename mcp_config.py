mcp_config = {
    "name": "SentimentAnalyzer",
    "description": "Predicts sentiment (positive, neutral, negative) from text input",
    "input_schema": {
        "text": "string"
    },
    "output_schema": {
        "sentiment": "string",
        "confidence": "float"
    },
    "version": "1.0",
    "model_type": "bert",
    "owner": "anil"
}
