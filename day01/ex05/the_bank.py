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
        print(check_account.__dict__)
        list_account = list(check_account.__dict__)
        menu = input("Type menu.(Add or Delete)\n")
        if menu == "Add":
            attribute = input("Type attribute want to change\n")
            for elem in list_account:
                if elem == attribute:
                    to_change = input(f"Type {elem}'s changes\n")
                    dic = {attribute: to_change}
                    check_account.__dict__.update(dic)
                    print(f'The content of {attribute} is changed to "{to_change}"')
                    print(check_account.__dict__)
                    return (True)
            no_exist = input("The attribute is not in account. Would you like to add new attribute? (Y or N)\n")
            while (not no_exist == 'Y' and not no_exist == 'N'):
                if no_exist == 'Y':
                    to_change = input(f"Type {attribute}'s content\n")
                    dic = {attribute: to_change}
                    check_account.__dict__.update(dic)
                    print(f"The content of {attribute} is added")
                    print(check_account.__dict__)
                    return (True)
                elif no_exist == 'N':
                    break
                print("Type 'Y' or 'N' only")
                no_exist = input()
            return (False)
        elif menu == "Delete":
            attribute = input("Type attribute want to delete\n")
            for elem in list_account:
                if elem == attribute:
                    del check_account.__dict__[attribute]
                    print("Delete completed")
                    print(check_account.__dict__)
                    return (True)
            print("The attributes is not existed")
            return (False)
        print("Input is wrong. Type Add or Delete.")
        return (False)

