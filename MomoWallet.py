class MomoWallet:
    
    def __init__(self, owner_name, balance=0, currency="ugx"):
        self.owner_name = owner_name
        self.__balance = balance
        self.currency = currency

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = value + self.__balance
        
        
Pop_wallet = MomoWallet("Pop", 1000, "ugx") 
Pop_wallet.balance = 7000
print(f"{Pop_wallet.owner_name} wallet balanace is : {Pop_wallet.balance} {Pop_wallet.currency}")


### Not having Property:
class MomoWallet:
    
    def __init__(self, owner_name, balance=0, currency="ugx"):
        self.owner_name = owner_name
        self.balance = balance
        self.currency = currency

    def balance(self):
        return self.balance
        
Pop_wallet = MomoWallet("Pop", 1000, "ugx") 
print(Pop_wallet.owner_name, Pop_wallet.balance, Pop_wallet.currency)