balance = 20000
withdrawal = 8000
daily_limit = 10000

if withdrawal <= 0:
    print("Invalid amount")

else:
    if balance >= withdrawal:
        if withdrawal <= daily_limit:
            print("Withdrawal approved!")

        else:
            print("Daily limit exceeded")
    else:
        print("Insufficient balance")