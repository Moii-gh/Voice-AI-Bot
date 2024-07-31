import requests
import json

class GPT:
    def __init__(self):
        self.name = "GPT"
        self.type = "ChatCompletion"
        self.default_model = "gpt-4"
        self.url = "https://nexra.aryahcr.cc/api/chat/gpt"

    def fetch_data(self, messages, options=None):
        if options is None:
            options = {}
        headers = {'Content-Type': 'application/json'}
        data = {
            'messages': messages,
            'prompt': messages[-1]['content'],
            'model': options.get('model', "gpt-4"),
            'markdown': options.get('markdown', False)
        }
        proxy = options.get('proxy')
        proxies = self.create_proxy_config(proxy) if proxy else {}
        response = requests.post(self.url, headers=headers, json=data, proxies=proxies)
        return self.handle_response(response.text)

    def create_proxy_config(self, proxy):
        return {'http': proxy, 'https': proxy}

    def handle_response(self, text):
        try:
            obj = json.loads(text)
            if 'gpt' not in obj:
                raise Exception("Invalid response.")
            return obj['gpt']
        except json.JSONDecodeError:
            raise Exception("Invalid response.")
