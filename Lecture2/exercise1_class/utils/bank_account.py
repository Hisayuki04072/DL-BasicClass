

class BankAccount:

    """ コンストラクタ """
    def __init__(self, name):
        self.name = name # 名前
        self.balance = 0 # 預金
        self.interest_rate = 0.01 # 金利





    """ 名前を出力する関数 """
    def get_name(self):
        return self.name

    """ 預金を出力する関数 """
    def get_balance(self):
        return self.balance
    
    """ 預金を追加する関数 """
    def deposit(self, amount):
        self.balance += amount
    
    """ 預金を引き出す関数 """
    def withdraw(self, amount):
        self.balance -= amount

    """ 金利を設定する関数 """
    def set_interest_rate(self, rate):
        self.interest_rate = rate

    """ 金利を適用する関数 """
    def apply_interest(self):
        self.balance += int(self.balance * self.interest_rate) # 端数は切り捨て