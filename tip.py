def total_cal(billamt, perctip):
    total=billamt*(1+0.01*perctip)
    total=round(total, 2)
    print(f"Please pay ${total}")
total_cal(100, 20)