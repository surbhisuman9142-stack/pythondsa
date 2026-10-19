def percentage_change():
    value = 100
    value = value*1.20
    value = value*0.80
    change = value - 100
    percentage = (change/100)*100
    return percentage
print(percentage_change())