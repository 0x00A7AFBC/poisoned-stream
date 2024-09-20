# Poisoned stream
## Usage
### Response sniffer with updog as an example target
```$ updog```</br>
```$ mitmdump --mode reverse:http://127.0.0.1:9090 -s response-sniffer.py```
## Example config
### Static file replacer (files-to-replace.json)</br>
```
{
"/some/arbitrary/endpoint.txt":"/path/to/file/to/replace"
}
```
# TODO
- **[⏳]** Implement replacing files when matching
- **[❌]** Implement dynamic shellcode injection into codecaves
  - **[❌]** Windows
  - **[❌]** Linux
  - **[❌]** MacOS
- **[❌]** Implement custom js injection

