import datetime
import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%I:%M:%S") # Get the current time
        
        print("Current time", current_time)
        print("Alarm time", alarm_time)

        if current_time == alarm_time:
            print("Wake up!")
            winsound.PlaySound("Paramore Decode-.wav", winsound.SND_ASYNC)
            break
        else:
            print("Sleeping...")
            time.sleep(1)

alarm_time = input("Enter the alarm time in 'HH:MM:SS' format: " )

set_alarm(alarm_time)