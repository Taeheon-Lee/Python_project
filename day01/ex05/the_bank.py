class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def check_corrupted(self, account):
        check_zip = 0
        check_addr = 0
        list_keys = list(account.__dict__.keys())
        for elem in list_keys:
            if (elem[0] == 'b'):
                return (True)
            if elem[:3:] == 'zip':
                check_zip = 1
            if elem[:4:] == 'addr':
                check_addr = 1
        if (len(list_keys) % 2 == 0
            or ('name' in list_keys) is False
            or ('id' in list_keys) is False
            or ('value' in list_keys) is False
            or (check_zip == 0 and check_addr == 0)):
            return (True)
        return (False)

    def find_account(self, name_or_id):
        if not isinstance(name_or_id, str) and not isinstance(name_or_id, int):
            raise TypeError("Input name or ID number")
        for elem in self.account:
            if name_or_id in elem.__dict__.values():
                return (elem)
        return (None)

    def transfer(self, origin, dest, amount):
        """
            @origin:    int(id) or str(name) of the first account
            @dest:      int(id) or str(name) of the destination account
            @amount:    float(amount) amount to transfer
            @return         True if succes, False if an error occured
        """
        account_origin = self.find_account(origin)
        account_dest = self.find_account(dest)
        if (account_origin == None or account_dest == None or account_origin == account_dest
            or self.check_corrupted(account_origin) or self.check_corrupted(account_dest)):
            print("Error: An account is not correct.")
            return (False)
        if not isinstance(amount, float):
            print("TypeError: Amount of money should be float.")
            return (False)
        if account_origin.value < amount:
            print(f"ValueError: Insufficient {account_origin.name}'s deposit balance.")
            return (False)
        account_origin.transfer(-amount)
        account_dest.transfer(amount)
        return (True)

    def fix_account(self, account):
        """
            fix the corrupted account
            @account:   int(id) or str(name) of the account
            @return         True if succes, False if an error occured
        """
        check_account = self.find_account(account)
        if check_account == None:
            print("ValueError: Incorrect account")
            return (False)
        if not self.check_corrupted(check_account):
            print("Error: This account is not corrupted")
            return (False)
        return (False)
