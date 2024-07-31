import requests
from urllib.parse import quote


message = '线上系统发生故障，立刻修复'

body = {
    'url': f'ticktick://x-callback-url/v1/add_task?title={quote(message)}',
    'body': message
}
resp = requests.post('https://api.day.app/YLAHUidBBsRKp5oFtGaJ6A/', json=body).json()
print(resp)