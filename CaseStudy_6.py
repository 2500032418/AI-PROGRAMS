"""Bank Balance check"""
balance=1000
withdraw=2000
if balance>withdraw:
    print("withdraw allows")
elif balance<withdraw:
    print("insufficient balance")
else:
    print("transaction failed")
