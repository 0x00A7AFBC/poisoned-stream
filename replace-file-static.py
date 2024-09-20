import json
import os

from mitmproxy import http, addonmanager

class ReplaceFiles:
    def load(self, loader: addonmanager.Loader):
        with open(os.environ['PROXY_CONFIG'], 'r') as file:
            config = file.read()
            self.config = json.loads(config)

    def response(self, flow: http.HTTPFlow) -> None:#
        endpoint = flow.request.path
        
        if endpoint in self.config:
            flow.intercept()

            abs_to_file = os.path.abspath(self.config[endpoint])

            with open(abs_to_file, 'r') as file:
                content = file.read()
                flow.response.text = content

            flow.resume()

addons = [ReplaceFiles()]

