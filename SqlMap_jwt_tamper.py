#!/usr/bin/env python2

"""
Copyright (c) 2018-2019 zi0Black
"""

import base64

from lib.core.enums import PRIORITY
from lib.core.settings import UNICODE_ENCODING

__priority__ = PRIORITY.LOW

def dependencies():
    pass

def tamper(payload, **kwargs):

    header="{'alg': 'HS256','typ': 'JWT','kid': %s}" % (payload)
    payload_signature="eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    return base64.b64encode(header.encode(UNICODE_ENCODING)+'.'+payload_signature) if payload else payload
