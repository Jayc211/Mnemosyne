import base64

#Paste the xor encrypted payload from mnemosyne.py
payload = ""

#Paste the xor encrypted key from mnemosyne.py
key = ""

xor_function = bytes([a ^ b for a, b in zip(payload, key)])
decrypt = base64.b64decode(xor_function).decode("utf-8")

exec(decrypt)
