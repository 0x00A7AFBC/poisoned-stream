import json
import os

from mitmproxy import http, addonmanager

class InjectJS:
    def load(self, loader: addonmanager.Loader):
        with open(os.environ['PROXY_CONFIG'], 'r') as file:
            config = file.read()
            self.config = json.loads(config)

    def response(self, flow: http.HTTPFlow) -> None:
        if 'Content-Type' not in flow.response.headers:
            return

        if 'text/html' in flow.response.headers['Content-Type']:
            if 'inject' in self.config:
                flow.intercept()

                content = flow.response.text

                if 'pre' in self.config['inject']:
                    path = self.config['inject']['pre']

                    if os.path.exists(path):
                        script = open(os.path.abspath(path), 'r').read()
                        content = f'<script>{script}</script>' + content
                    else:
                        content = self.config['inject']['pre'] + content

                
                if 'post' in self.config['inject']:
                    path = self.config['inject']['post']

                    if os.path.exists(path):
                        script = open(os.path.abspath(path), 'r').read()
                        
                        content += f'<script>{script}</script>'
                    else:
                        content += self.config['inject']['post']

                flow.response.text = content

                flow.resume()

addons = [InjectJS()]

