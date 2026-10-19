def compound_interest(p,r,t):
    amount = p * (1+r/100) ** t
    return round(amount,2)
print(compound_interest(10000,10,2))