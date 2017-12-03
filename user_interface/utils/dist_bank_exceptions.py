# dist_bank_exceptions.py
"""
Global definitons of project errors and exceptions.
"""

class AccountNotExistError(Exception):
    """
    Account not exist error.
    """
    def __repr__(self):
        return "Account not exist error."

class DatabaseOptFailure(Exception):
    """
    Methods in dist_bank_resources failed to operate database properly.
    """
    def __repr__(self):
        return "Methods in dist_bank_resources failed to operate database properly."

