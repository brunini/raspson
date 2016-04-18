# raspson
Control all GPIOs pins from your Raspberry Pi using JSON-RPC 2.0 over http.

-> You really should consider use another implementation.



If you really choose raspson, look at the examples below.


Get status of pins:

```bash
curl -i -X POST  -H "Content-Type: application/json; indent=4" \
-d '{
"jsonrpc": "2.0",
"method": "get_all_status",
"params": {"username": "flask", "password": "JSON-RPC"},
"id": "1"
}' http://IP_OF_YOUR_RASPBERRY:5000/api
```

Toogle some pin V between 1 or 0:

```bash
curl -i -X POST  -H "Content-Type: application/json; indent=4" \
-d '{
"jsonrpc": "2.0",
"method": "toggle_output",
"params": {"username": "flask", "password": "JSON-RPC", "pin": 12},
"id": "1"
}' http://IP_OF_YOUR_RASPBERRY:5000/api
```

Set some pin V between 1 or 0:

```bash
curl -i -X POST  -H "Content-Type: application/json; indent=4" \
-d '{
"jsonrpc": "2.0",
"method": "set_output",
"params": {"username": "flask", "password": "JSON-RPC", "pin": 12, "new_state": 1},
"id": "1"
}' http://IP_OF_YOUR_RASPBERRY:5000/api
```

Now you can use this examples on your bash scripts, or even use requests library for your python application as the example below.

```python
import json
import requests
url = 'http://192.168.8.24:5000/api'
headers = {'content-type': 'application/json'}
payload = {"method": "toggle_output", "params": {"username": "flask", "password": "JSON-RPC", "pin": 0}, "id": "1"h}
requests.post(url, data=json.dumps(payload), headers=headers)
```

As you can see, this implementation chooses to use GPIO.BOARD instead other modes, because its simpler to locate the pin in the device.

I hope you enjoy and please feel free to improve the funcionality of raspson, fork it!