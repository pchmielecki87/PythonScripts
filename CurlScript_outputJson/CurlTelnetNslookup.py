import subprocess
import json
from datetime import datetime

# commands
commands = [
    {"type": "curl", "url": "https://google.com/", "port": 80},
    {"type": "curl", "url": "https://google.com/", "port": 443},
    {"type": "curl", "url": "https://microsoft.com/", "port": 443},
    {"type": "curl", "url": "https://aws.amazon.com/", "port": 443},
    {"type": "telnet", "host": "microsoft.com", "port": 80},
    {"type": "nslookup", "ip": "8.8.8.8"},
    {"type": "nslookup", "ip": "127.0.0.1"}
]

# curl
def run_curl(url, port=None):
    try:
        if port:
            url = f"{url}:{port}"
        
        curl_command = f"curl -o /dev/null -w '%{{http_code}}' {url}"
        result = subprocess.run(curl_command, shell=True, capture_output=True, text=True, check=True)
        http_status_code = result.stdout.strip()  # Pobierz kod statusu HTTP
        return http_status_code
    
    except subprocess.CalledProcessError as e:
        return "000"  # if status code is 000

# telnet
def run_telnet(host, port):
    try:
        telnet_command = f"timeout 5 telnet {host} {port}" # 5s timeout
        result = subprocess.run(telnet_command, shell=True, capture_output=True, text=True)
        
        if "Connected" in result.stdout:
            return "SUCCESS"
        else:
            return "FAILED"
    except Exception as e:
        return "ERROR"

# nslookup
def run_nslookup(ip):
    try:
        nslookup_command = f"nslookup {ip}"
        result = subprocess.run(nslookup_command, shell=True, capture_output=True, text=True, check=True)
        
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return "ERROR"

# run commands
for cmd in commands:
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    if cmd["type"] == "curl":
        http_status_code = run_curl(cmd["url"], cmd.get("port"))
        data = {
            "status": "INFO",
            "timestamp": timestamp,
            "message": f"curl {cmd['url']}" + (f" (port: {cmd['port']})" if "port" in cmd else ""),
            "http": {
                "url": cmd["url"],
                "status_code": http_status_code,
                "method": "GET",
                "port": cmd.get("port", "default")
            }
        }
        domain = cmd["url"].split("//")[1].split("/")[0].replace(".", "_")
        filename = f"curl_{domain}_{datetime.utcnow().strftime('%Y%m%d')}.json"
    
    elif cmd["type"] == "telnet":
        telnet_result = run_telnet(cmd["host"], cmd["port"])
        data = {
            "status": "INFO",
            "timestamp": timestamp,
            "message": f"telnet {cmd['host']}:{cmd['port']}",
            "telnet": {
                "host": cmd["host"],
                "port": cmd["port"],
                "result": telnet_result
            }
        }
        domain = cmd["host"].replace(".", "_")
        filename = f"telnet_{domain}_{datetime.utcnow().strftime('%Y%m%d')}.json"
    
    elif cmd["type"] == "nslookup":
        nslookup_result = run_nslookup(cmd["ip"])
        data = {
            "status": "INFO",
            "timestamp": timestamp,
            "message": f"nslookup {cmd['ip']}",
            "nslookup": {
                "ip": cmd["ip"],
                "result": nslookup_result
            }
        }
        ip_clean = cmd["ip"].replace(".", "_")
        filename = f"nslookup_{ip_clean}_{datetime.utcnow().strftime('%Y%m%d')}.json"
    
    # save as JSON
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"Saved as: {filename}")