import time
from playsound import playsound

def alarm_clock():
    try:
        alarm_time = input("Set your alarm to HH:MM format: ")
        while True:
            current_time = time.strftime("%H:%M")
            if current_time == alarm_time:
                print("Wake up time!!")
                playsound("C:\\Users\\HP\\Downloads\\AUD-20230921-WA0001_.mp3")
                break
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nAlarm clock stopped.")

if __name__ == "__main__":
    alarm_clock()
