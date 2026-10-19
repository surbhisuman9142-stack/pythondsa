def train_crossing(length,speed_kmh):
    speed_ms = speed_kmh*5/18
    time = length/speed_ms
    return time
print(train_crossing(200,72))
    
    