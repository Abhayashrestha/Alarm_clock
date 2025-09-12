import time
import datetime
import pygame


def set_alarm(alarm_time_str):
    """Set an alarm for the given time string in HH:MM:SS format."""
    target = datetime.datetime.strptime(alarm_time_str, "%H:%M:%S")
    now = datetime.datetime.now()
    alarm_dt = now.replace(hour=target.hour, minute=target.minute, second=target.second, microsecond=0)

    if alarm_dt <= now:
        alarm_dt += datetime.timedelta(days=1)

    sleep_seconds = (alarm_dt - now).total_seconds()
    print(f"Alarm set for {alarm_dt.strftime('%H:%M:%S')}")
    time.sleep(sleep_seconds)

    print("your time is up")
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Set alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
