#!/usr/bin/env python3

from binascii import (
    hexlify, unhexlify
)

import pytest

from hdwallet.libs.base58 import (
    check_encode, check_decode, decode, encode, string_to_int
)


RAW: str = "0488ade405d5bc481680000000b5b40efbdef2e0a2e8ee6fa9d371f951f93e3b1e3c1b50fb31f9ea36cfc7c88100b9d3f3" \
           "12b38951361597219c8979e177d99349fd0213bac55508c8469d02064f"

ENCODED_RAW: str = "xpub6GzA69ujvGDmXQDwJnCnyDBr5FxBFri57tFBzD1Q3HTUkRRS35eZND12MPL1d7iXT15tLwbKmvxhJDFtExNc7SU" \
                   "efgYGNE7xCQan6Cmhp8f"


def test_base58():

    assert check_encode(raw=unhexlify(RAW)) == "xprvA3zogeNr5tfUJv9UCkfnc5F7XE7grPzDkfKbBpbnUwvVsd6HVYLJp" \
                                               "QgYWCBjXwZw3GdtSVUQ7BDEgmi6MHt4MatV9gDtWuJuGYhYL7nj6aa"

    assert hexlify(check_decode(enc=ENCODED_RAW)).decode() == \
        "0488b21e05d5bc481680000000b5b40efbdef2e0a2e8ee6fa9d371f951f93e3b1e3c1b50fb31f9ea36cfc7c88100b9d3" \
        "f312b38951361597219c8979e177d99349fd0213bac55508c8469d02064f"

    with pytest.raises(TypeError, match="string argument without an encoding"):
        assert string_to_int(str("meherett"))


    assert decode("111233QC4") == b'\x00\x00\x00(\x7f\xb4\xcd'


    assert encode(decode("111233QC4")) == "111233QC4"


def test_keccak():
    """Keccak 256 hash is required by several crypto algorithms.  Ensure our hash implementations
    are correct.

    From: https://cryptobook.nakov.com/cryptographic-hash-functions/hash-functions-examples

    """
    import hashlib, binascii

    text = 'hello'
    data = text.encode("utf8")

    sha256hash = hashlib.sha256(data).digest()
    print("SHA-256:   ", binascii.hexlify(sha256hash))
    assert binascii.hexlify(sha256hash) == b'2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'

    sha3_256 = hashlib.sha3_256(data).digest()
    print("SHA3-256:  ", binascii.hexlify(sha3_256))
    assert binascii.hexlify(sha3_256) == b'3338be694f50c5f338814986cdf0686453a888b84f424d792af4b9202398f392'

    blake2s = hashlib.new('blake2s', data).digest()
    print("BLAKE2s:   ", binascii.hexlify(blake2s))
    assert binascii.hexlify(blake2s) == b'19213bacc58dee6dbde3ceb9a47cbb330b3d86f8cca8997eb00be456f140ca25'

    ripemd160 = hashlib.new('ripemd160', data).digest()
    print("RIPEMD-160:", binascii.hexlify(ripemd160))
    assert binascii.hexlify(ripemd160) == b'108f07b8382412612c048d07d13f814118445acd'

    # # Old pysha3 (deprecated) keccak-256 implementation
    # from sha3 import keccak_256
    # keccak256 = keccak_256()
    # keccak256.update(data)
    # keccak256_sha3 = keccak256.digest()
    # print("Keccak256:", binascii.hexlify(keccak256_sha3), "(pysha3)")
    # assert binascii.hexlify(keccak256_sha3) == b'1c8aff950685c2ed4bc3174f3472287b56d9517b9c948127319a09a7a36deac8'

    # New pycryptodome keccak-256 implementation
    from Crypto.Hash import keccak
    keccak256_pycryptodome = keccak.new(data=data, digest_bits=256).digest()
    print("Keccak256:", binascii.hexlify(keccak256_pycryptodome), " (pycryptodome)")
    assert binascii.hexlify(keccak256_pycryptodome) == b'1c8aff950685c2ed4bc3174f3472287b56d9517b9c948127319a09a7a36deac8'

