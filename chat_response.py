class ChatCompletionMessage:
    def __init__(self, content, role, function_call=None, tool_calls=None):
        self.content = content
        self.role = role
        self.function_call = function_call
        self.tool_calls = tool_calls

class Choice:
    def __init__(self, finish_reason, index, logprobs, message):
        self.finish_reason = finish_reason
        self.index = index
        self.logprobs = logprobs
        self.message = ChatCompletionMessage(**message)

class ChatCompletion:
    def __init__(self, id, choices, created, model, object, service_tier=None, system_fingerprint=None, usage=None):
        self.id = id
        self.choices = [Choice(**choice) for choice in choices]
        self.created = created
        self.model = model
        self.object = object
        self.service_tier = service_tier
        self.system_fingerprint = system_fingerprint
        self.usage = usage

response_data = {
    'id': 'chatcmpl-9kUQwT4WYVAIxeScQglmhtWGgNilW',
    'choices': [
        {
            'finish_reason': 'stop',
            'index': 0,
            'logprobs': None,
            'message': {
                'content': "I think that would be a great idea! It would be wonderful if all Coles stores offered a lobster discount. Just keep in mind that if it becomes really popular, they might sell out quickly. But it's definitely worth a try!",
                'role': 'assistant',
                'function_call': None,
                'tool_calls': None
            }
        }
    ],
    'created': 1720867102,
    'model': 'gpt-3.5-turbo-0125',
    'object': 'chat.completion',
    'service_tier': None,
    'system_fingerprint': None,
    'usage': {
        'completion_tokens': 48,
        'prompt_tokens': 47,
        'total_tokens': 95
    }
}

# Create a ChatCompletion instance from the response data
response = ChatCompletion(**response_data)
