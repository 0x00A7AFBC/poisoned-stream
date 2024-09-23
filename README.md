# Poisoned stream
Reverse HTTP(S) proxy based on mitmproxy to inject shellcode into file streams and other fun things :3
## Usage
```
usage: poison.py [-h] -u URL [-p PORT] -c CONFIG [-m MODULE] [--cert CERT]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     Url to proxy
  -p PORT, --port PORT  Port to listen in
  -c CONFIG, --config CONFIG
                        Path to your configuration file
  -m MODULE, --module MODULE
                        Add custom modules
  --cert CERT           Path to ssl certificate to use. If not provided default to mitmproxy cert
```
## Example config</br>
```json
{
    "replace":{
        "/arbitrary/endpoint":"/path/to/file"
    },
    "inject":{
        "pre":"<script>alert(1)</script>",
        "post":"/path/to/file"
    }
}
```
# Setup
```sh
pip install -r requirements.txt
```
# TODO
- **[✅]** Implement replacing files when matching
- **[❌]** Implement dynamic shellcode injection into codecaves
  - **[❌]** Windows
  - **[❌]** Linux
  - **[❌]** MacOS
- **[✅]** Implement custom js injection
- **[✅]** Create cli
  - **[✅]** Add arg for selecting custom config

