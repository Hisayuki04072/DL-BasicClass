from utils.bank_account import BankAccount


    
if __name__ == "__main__":
    bank_account = BankAccount("Alice")
    bank_account.deposit(1000) # 預金を預ける
    print(bank_account.get_balance())
    bank_account.withdraw(900) # 預金を引き出す
    print(bank_account.get_balance())
    bank_account.set_interest_rate(0.1) # 預金の設定
    bank_account.apply_interest() # 預金の適用
    print(bank_account.get_balance())




