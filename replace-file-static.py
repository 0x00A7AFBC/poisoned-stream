import json

from mitmproxy import http, addonmanager

class ReplaceFiles:
    def load(self, loader: addonmanager.Loader):
        with open('./files-to-replace.json', 'r') as file:
            config = file.read()
            self.config = json.loads(config)

    def response(self, flow: http.HTTPFlow) -> None:#
        endpoint = flow.request.path
        
        if endpoint in self.config:
            flow.intercept()

            with open(config[endpoint], 'r') as file:
                content = file.read()
                flow.response.text = content

            flow.resume()

addons = [ReplaceFiles()]

