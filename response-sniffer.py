from mitmproxy import http, ctx

def response(flow: http.HTTPFlow) -> None:
    print(flow)
