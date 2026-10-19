def combined_work(a,b):
    rate_a = 1/a
    rate_b = 1/b
    total_rate = rate_a  + rate_b
    days = 1/total_rate
    return days
print(combined_work(12,18))