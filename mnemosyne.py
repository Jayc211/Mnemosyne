import secrets

#The payload in base64 format
print("Enter your base64_payload::")
base64_payload = str(input())

#Generating a key that's the same byte size as the payload
length = len(base64_payload)
print("Payload length::",length)

#Generating the XOR encryption key
key = secrets.token_bytes(length)
print("XOR encryption key::",key)

#XOR encryption part
final_payload = base64_payload.encode()
encrypted_payload = bytes([a ^ b for a, b in zip(final_payload, key)])

print("Encrypted payload::", encrypted_payload)

  
 




