def probability(favourable, total):
    if total <= 0:
        return None
    if favourable < 0 or favourable > total:
        return None
    return round(favourable/total,3)
print(probability(1,6))
print(probability(3,6))
print(probability(5,10))
    
    