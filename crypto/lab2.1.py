def mod(a, m):
    return a % m

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None
    else:
        return x % m

def poly_add(p, q):
    n = max(len(p), len(q))
    res = [0]*n
    for i in range(n):
        res[i] = ((p[i] if i < len(p) else 0) ^ (q[i] if i < len(q) else 0))
    return res

def poly_mul(p, q):
    res = [0]*(len(p)+len(q)-1)
    for i in range(len(p)):
        for j in range(len(q)):
            res[i+j] ^= p[i] & q[j]
    return res

# --- Гараас утга авах хэсэг ---

a = int(input("a = "))
b = int(input("b = "))
m = int(input("m = "))

print("\n--- Modular Arithmetic ---")
print(f"{a} mod {m} = {mod(a, m)}")

print("\n--- GCD ---")
print(f"GCD({a}, {b}) = {gcd(a, b)}")

print("\n--- Extended GCD ---")
g, x, y = extended_gcd(a, b)
print(f"Extended GCD({a}, {b}) = {g}, x = {x}, y = {y}")

print("\n--- Modular Inverse ---")
inv = mod_inverse(a, m)
if inv is None:
    print(f"No modular inverse for {a} mod {m}")
else:
    print(f"Inverse of {a} mod {m} = {inv}")

print("\n--- Polynomials over GF(2) ---")
f = list(map(int, input("Enter polynomial f(x) coefficients (space separated): ").split()))
g = list(map(int, input("Enter polynomial g(x) coefficients (space separated): ").split()))
print("f(x)+g(x) =", poly_add(f, g))
print("f(x)*g(x) =", poly_mul(f, g))
