class RemovedInPyjwt3Warning(DeprecationWarning):
    """Warning for features that will be removed in PyJWT 3."""

    pass


class InsecureKeyLengthWarning(UserWarning):
    """Warning emitted when a cryptographic key is shorter than the minimum
    recommended length (RFC 7518 Section 3.2 for HMAC keys, NIST SP 800-131A
    for RSA keys)."""

    pass
