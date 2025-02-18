def withdrawMoney(balance, amount):
    try:
        if balance < 0 or amount < 0:
            return 'Current Balance or Withdrawal Amount should not be negative.'
        elif amount <= balance:
            return f'New balance = {balance - amount}'
        else:
            raise ValueError('Insufficient funds')
    except ValueError as e:
        return str(e)

# print(withdrawMoney(1000, 2400))  
# print(withdrawMoney(1000, 300))  
print(withdrawMoney(1000, -300))  
