def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

def trial_division(n):
    d = 2
    while d * d <= n:
        if (n % d) == 0:
            return d, n // d
        d += 1
    raise Exception('Failed to factorize modulus N')

def rsa_decrypt(ciphertext, d, N):
    # Split the ciphertext into parts
    ciphertext_parts = ciphertext.split('|')
    print(f"Ciphertext parts: {ciphertext_parts}")
    
    # Convert each part from hex to integer
    ciphertext_ints = [int(c, 16) for c in ciphertext_parts]
    print(f"Ciphertext ints: {ciphertext_ints}")
    
    # Decrypt each integer using the private key
    decrypted_ints = [pow(c, d, N) for c in ciphertext_ints]
    print(f"Decrypted ints: {decrypted_ints}")
    
    # Convert the decrypted integers to characters to form the plaintext
    plaintext = ''.join([chr(num) for num in decrypted_ints])
    return plaintext


def main():
    # Prompt the user for inputs
    ciphertext = input("Enter the RSA encrypted message: ")
    N = int(input("Enter the public modulus (N): "))
    e = int(input("Enter the public exponent (e): "))

    # Factorize N to find p and q
    p, q = trial_division(N)
    # Compute φ(N)
    phi_N = (p - 1) * (q - 1)
    # Compute the private exponent d
    d = mod_inverse(e, phi_N)

    # Decrypt the message
    plaintext = rsa_decrypt(ciphertext, d, N)

    # Output the decrypted message
    print(f"Decrypted Message: {plaintext}")

if __name__ == "__main__":
    main()

