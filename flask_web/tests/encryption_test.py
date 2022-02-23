import pytest
from passlib.hash import sha256_crypt

from controller.encryption import hash_password

def test_hash_password():
    hash_function = hash_password("test_hash_password")
    hash_verify = sha256_crypt.verify("test_hash_password", hash_function)
    assert hash_verify == True