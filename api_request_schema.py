def get_model_ids():
    return list(api_request_list.keys())

api_request_list = {
    'anthropic.claude-3-5-haiku-20241022-v1:0': {
        'modelId': 'anthropic.claude-3-5-haiku-20241022-v1:0',
        'contentType': 'application/json',
        'accept': 'application/json',
        'body': {
            'anthropic_version': 'bedrock-2023-05-31',
            'max_tokens': 1024,
            'temperature': 0.7,
            'top_p': 0.9,
            'top_k': 250,
            'stop_sequences': [],
            'system': 'あなたは親切で知識豊富なアシスタントです。日本語で簡潔に答えてください。',
            'messages': []
        }
    }
}
