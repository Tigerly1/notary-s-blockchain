def from_hex(cls, h):
    return cls(hex_to_bytes(h))


private, public = generate_keypair(512)

txt = 'deadbeef'
message = Message.from_hex(txt)
message.encrypt(public)
print("Encrypted message", message)
message.decrypt(private)
print("Decrypted message", message.hex())


message.encrypt(private)
message.decrypt(public)

message = Message.from_str('Very important message')
signature = message.sign(private)
print(message.verify(signature, public))
assert message.verify(signature, public)
