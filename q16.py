def celsius_to_fahrenheit(start,stop,step):
    result = []
    for c in range(start, stop + 1, step):
        f = (c * 9/5) + 32
        result.append((c,f))
    return result
print(celsius_to_fahrenheit(0, 30 ,5))
