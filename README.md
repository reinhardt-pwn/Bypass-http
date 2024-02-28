# Bypass-http
Automatized tool to bypass 403 and 401 HTTP status, created by Reinhardt (@Reinhardt_pwn).

## 🚨 Attention Users:
This repository contains a tool designed for educational purposes only ans is intended solely for testing, learning, and demonstrating cybersecurity practices.
Don't use this code and knowledge to attack / pentest unauthorized targets.

## Usage article
Here is a link to a medium article about how to use this tool, with a detailled example : https://medium.com/@reinhardt.pwn/tool-guide-bypass-http-a-python-tool-to-find-403-401-bypass-b46ff0bd6978

## Guide
### Usage
```
Usage: bypass_http.py [-h] -i I -a A [-p P] [-v V] [-m M] [-s S]
Arguments:
  -h, --help  show this help message and exit
  -i I        IP of the target, **Required**
  -a A        PATH of the target, **Required**
  -p P        PORT of the target, 80 by default
  -v V        VERSION of the target protocol, HTTPS/2.0 by default
  -m M        METHOD of the inital error, GET by default
  -s S        SECONDS between each request sent, 1 by default
```
Add the default headers in the default_headers.txt like this:
```
  Host: 159.65.20.166:31008
  User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Connection: close
  Upgrade-Insecure-Requests: 1
```

### What this tool does
This tool test multiple 403 and 401 bypass tricks in this order (form most to less common exploits):
```
  Testing all HTTP methods
  Path fuzzing
  Downgrade protocol version
  Headers fuzzing
  User-Agent fuzzing
```

If you want to learn more about these tricks, see this article: https://blog.vidocsecurity.com/blog/401-and-403-bypass-how-to-do-it-right/

### Custom
If you want to custom the different tests of this tool, you can change the .txt files in lists/
```
  agent.txt -> different User-Agent tested
  headers.txt -> differents headers tested
  headers_value.txt -> differents values for the previous headers
  path.txt -> differents paths tested to bypass, 'admin' is replaced by the real path during the tests
```

## In the future
### Adding features
Many features will be added in the future, like case-switching and Hop-By-Hop exploits.
Don't hesitate to contact me for collaborations.
Twitter: @Reinhardt_pwn
  
