'''
A few ways of generating random strings
'''

import hashlib
import random
import string
import uuid
import os


def generate_unique_id():
    # bf47b209-b4b2-4edc-a0e8-75b9eb48bc09
    return str(uuid.uuid4())


def generate_secret(length=32):
    # This could be used, for example, for passwords, or for app secrets
    # KlW5ISSRgJZNHFT2KcFNb2OVEdPGDMBE
    return ''.join(random.choice(
        string.ascii_letters + string.digits) for x in xrange(length))


def generate_secret_crypto(length=32):
    # This could be used as an alternative to generate_secret(). The result
    # should be good enough that's suitable for cryptographic use.
    # 7cbe8bd81672699cca5796f523cf6ed4946586bb28305d2f75842ce521815e73
    return os.urandom(length).encode('hex')


def generate_key():
    # Returns a python long int with 256 random bits. For example:
    # 110541642560575068150163131946313287475321532576990646525066748601962842052091
    random_bits = str(random.getrandbits(256))

    # Then hash it. For example:
    # b6dc7b0d72cc12d253efe5c6eee0c88a6f8c2f3607f127d117295106de176f29
    return hashlib.sha256(random_bits).hexdigest()
