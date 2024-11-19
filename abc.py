def generate_public_key(prime, base, private_key):
    return pow(base, private_key, prime)

def generate_shared_secret(public_key, private_key, prime):
    return pow(public_key, private_key, prime)

# Input for prime, base, and private keys
prime = int(input("Enter a large prime number (recommended > 2048 bits): "))
base = int(input("Enter a base (primitive root modulo of prime number): "))
alice_private = int(input("Alice, enter your private key (a random integer less than the prime): "))
alice_public = generate_public_key(prime, base, alice_private)
print("Alice's public key:", alice_public)

bob_private = int(input("Bob, enter your private key (a random integer less than the prime): "))
bob_public = generate_public_key(prime, base, bob_private)
print("Bob's public key:", bob_public)

# Generate shared secrets
alice_shared = generate_shared_secret(bob_public, alice_private, prime)
bob_shared = generate_shared_secret(alice_public, bob_private, prime)

print("Alice's shared secret:", alice_shared)
print("Bob's shared secret:", bob_shared)

if alice_shared == bob_shared:
    print("Success! The shared secret is:", alice_shared)
else:
    print("Error: Shared secrets do not match")
