from the_bank import Account, Bank

THbank = Bank()
acc1 = Account("test", value=100, zip=75000, addr='1 Boulevard Bessieres')
acc2 = Account("test2", value=50, zip=3454, addr='rgreg')
acc3 = Account("test3")
print(acc1.__dict__)
print(acc2.__dict__)
print(acc3.__dict__)
THbank.add(acc1)
THbank.add(acc2)
THbank.add(acc3)
THbank.transfer('test', 'test2', 50.0)
THbank.transfer('test', 'test3', 50.0)
print(acc1.__dict__)
print(acc2.__dict__)
print(acc3.__dict__)

