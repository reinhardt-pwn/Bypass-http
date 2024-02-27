
import src.utils
import src.request
import time

def try_other_http_methods(ip, port, path, version, seconds, headers):
    src.request.send_request_socket(ip, port, path, "GET", version, headers)
    time.sleep(seconds)
    src.request.send_request_socket(ip, port, path, "POST", version, headers)
    time.sleep(seconds)
    src.request.send_request_socket(ip, port, path, "DELETE", version, headers)
    time.sleep(seconds)
    src.request.send_request_socket(ip, port, path, "HEAD", version, headers)
    time.sleep(seconds)
    src.request.send_request_socket(ip, port, path, "OPTIONS", version, headers)
    time.sleep(seconds)
    src.request.send_request_socket(ip, port, path, "PATCH", version, headers)
    time.sleep(seconds)
    src.request.send_request_socket(ip, port, path, "PUT", version, headers)
    time.sleep(seconds)


def path_fuzzing(ip, port, path, version, method, seconds, headers):
    payload = src.utils.get_payload("lists/path.txt")
    formatted_path = src.utils.conform_path(path)
    payload = src.utils.conform_payload(formatted_path, payload)

    for current in payload:
        src.request.send_request_socket(ip, port, current.strip(), method, version, headers)
        time.sleep(seconds)


def agent_fuzzing(ip, port, path, version, method, seconds, headers):
    payload = src.utils.get_payload(path)

    for current in payload:
        headers['User-Agent'] = current.strip()
        src.request.send_request_socket(ip, port, path, method, version, headers)
        time.sleep(seconds)


def headers_fuzzing(ip, port, path, version, method, seconds, headers):
    payload_h = src.utils.get_payload("lists/headers.txt")
    payload_v = src.utils.get_payload("lists/headers_value.txt")

    for current_h in payload_h:
        for current_v in payload_v:
            headers[current_h.strip()] = current_v.strip()
            src.request.send_request_socket(ip, port, path, method, version, headers)
            time.sleep(seconds)


def downgrade_protocol_version(ip, port, path, method, seconds, headers):
    versions = ["HTTP/0.9", "HTTP/1.0", "HTTP/1.1", "HTTP/2.0"]
    if 'Host' in headers:
        del headers['Host']

    for current in versions:
        src.request.send_request_socket(ip, port, path, method, current, headers)
        time.sleep(seconds)


def run_exploits(ip, port, path, version, method, seconds):
    default_headers = src.utils.get_default_headers("default_headers.txt")

    # Testing all HTTP methods
    print("\t[1st step] -> Testing all HTTP Methods\n")
    try_other_http_methods(ip, port, path, version, seconds, default_headers)

    # Path fuzzing
    print("\n\n\t[2nd step] -> Path fuzzing")
    path_fuzzing(ip, port, path, version, method, seconds, default_headers)

    # Downgrade protocol version
    print("\n\n\t[3rd step] -> Downgrade protocol version\n")
    downgrade_protocol_version(ip, port, path, method, seconds, default_headers)

    # Headers fuzzing
    print("\n\n\t[4th step] -> Headers fuzzing")
    headers_fuzzing(ip, port, path, version, method, seconds, default_headers)
    default_headers = src.utils.get_default_headers("default_headers.txt")

    # User-Agent fuzzing
    print("\n\n\t[5th step] -> User-Agent fuzzing\n")
    agent_fuzzing(ip, port, path, version, method, seconds, default_headers)
