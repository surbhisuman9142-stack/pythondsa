import time
def practice_timer():
    minutes = 30
    seconds = minutes*60
    print("your 30-minute practice starts now!")
    while seconds > 0:
        mins = seconds // 60
        secs = seconds %  60
        
        print(f"\rTime left: {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1
    print("\nTime is up! Review your answers.")

practice_timer()         