from mitmproxy import http, ctx

class ResponseSniffer:
    def response(self, flow: http.HTTPFlow) -> None:
        print(flow.response)
        print(flow.response.text)

addons = [ResponseSniffer()]
