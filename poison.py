import argparse
import os
import subprocess

def main():
    parser = argparse.ArgumentParser(
        description='Reverse HTTP(S) proxy based on mitmproxy to inject shellcode into file streams '
    )

    parser.add_argument('-u', '--url', help='Url to proxy', action='store', required=True)
    parser.add_argument('-p', '--port', help='Port to listen in', action='store', default=8080, type=int)
    parser.add_argument('-c', '--config', help='Path to your configuration file', action='store', required=True)
    parser.add_argument('--cert', help='Path to ssl certificate to use. If not provided default to mitmproxy cert', action='store')

    args = parser.parse_args()

    os.environ['PROXY_CONFIG'] = args.config

    opts = ['--listen-port', str(args.port), '--mode', f'reverse:{args.url}']

    if args.cert:
        opts += ['--certs', f'*={args.cert}']

    scripts = ['-s', './modules/replace-file-static.py', '-s', './modules/inject-js.py']

    proxy_args = ['mitmdump'] + opts + scripts

    subprocess.run(proxy_args)


if __name__ == '__main__':
    main()