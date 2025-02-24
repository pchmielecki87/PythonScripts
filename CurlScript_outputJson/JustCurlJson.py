import subprocess
import json
from datetime import datetime

commands = [
    "curl https://microsoft.com/",
    "curl https://google.com/",
    "curl https://yandex.ru/"
]

# run curl
def run_curl(command):
    try:
        curl_command = f"{command} -o /dev/null -w '%{{http_code}}'"
        result = subprocess.run(curl_command, shell=True, capture_output=True, text=True, check=True)
        http_status_code = result.stdout.strip()  # get HTTP
        return http_status_code
    except subprocess.CalledProcessError as e:
        return "000"  # case of code 000

# loop
for cmd in commands:
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    http_status_code = run_curl(cmd)
    
    # Prepare JSON
    data = {
        "status": "INFO",
        "timestamp": timestamp,
        "message": cmd,
        "http": {
            "url": cmd.split()[1],  # get url
            "status_code": http_status_code,
            "method": "GET"
        }
    }

    # save as file    
    domain = cmd.split()[1].split("//")[1].split("/")[0].replace(".", "_")
    filename = f"curl_{domain}_{datetime.utcnow().strftime('%Y%m%d')}.json"

    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"Saved as: {filename}")