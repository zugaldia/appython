'''
It uses utils/generators.py to create a few random strings that can be
useful in different scenarios.
'''

from appython.utils.generators import generate_unique_id
from appython.utils.generators import generate_secret
from appython.utils.generators import generate_secret_crypto
from appython.utils.generators import generate_key

for x in range(5):
    print '    unique_id: %s' % generate_unique_id()

for x in range(5):
    print '       secret: %s' % generate_secret()

for x in range(5):
    print 'secret_crypto: %s' % generate_secret_crypto()

for x in range(5):
    print '          key: %s' % generate_key()
