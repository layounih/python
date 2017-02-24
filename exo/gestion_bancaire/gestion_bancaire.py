class Account:
    def __init__(self, id, balance, overdraft=True):
        self._id = id
        self._balance = balance
        self.overdraft = overdraft

    def deposit (self, value):
        if value >= 0:
            self._balance = self._balance + float(value)
        else:
            raise ValueError("valeur négative")



    def withdraw (self, value):
        self._balance = self._balance - float(value)
        if float(self._balance) < 0:
            raise ValueError('Solde de ne peut pas être inférieur à 0, il est de {}'.format(self._balance))

class Person:
    def __init__(self, id, first_name, last_name):
        self._id = id
        self.first_name = first_name
        self.last_name = last_name
        self._accounts = {}

    def manage_account(self, account):
        self._accounts[account._id] = account

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self._accounts)

class courant(Account):
    def __init__(self, balance, overdraft, limite):
        Account.__init__(self, balance, overdraft)
        self.limte = limite
    pass

class differ(Account):
    def __init__(self, balance, overdraft):
        Account.__init__(self, balance, overdraft)
        self.liste_operations = []
    pass


class BusinessError(Exception):
    """
    Exception destinée à identifier des erreurs métier.
    """
    def __init__(self, value, cause=None):
        super(BusinessError, self)\
            .__init__(value + u', caused by ' + repr(cause))
        self.cause = cause

    def __str__(self):
        return repr(self._value)
