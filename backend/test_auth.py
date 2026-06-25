"""Smoke test for password hashing. Run: python test_auth.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from app.api import hash_password, verify_password

# correct password verifies
h = hash_password("secret123")
assert h.startswith("scrypt$")
assert verify_password("secret123", h)

# wrong password rejected
assert not verify_password("wrong", h)

# salts differ -> same password hashes differently
assert hash_password("secret123") != hash_password("secret123")

# legacy plaintext still verifies (backward compat), whitespace-tolerant
assert verify_password("oldpass", "oldpass")
assert verify_password(" oldpass ", "oldpass")
assert not verify_password("nope", "oldpass")

# empty stored -> reject
assert not verify_password("x", "")

print("auth self-check passed")
