from Bank_accounts import *


sagar=BankAccount(1000,"sagar")

smita=BankAccount(2000,"smita")



sagar.deposit(500)
sagar.withdraw(00)

sagar.transfer(100,smita)



jim=InterestRewardsAcct(5000,"Jim")

jim.get_balance()

jim.deposit(100)

jim.transfer(200,sagar)

Shrasti=SavingsAcct(4000,"Shrasti")

Shrasti.get_balance()
Shrasti.deposit(200)

Shrasti.transfer(2000, sagar)
