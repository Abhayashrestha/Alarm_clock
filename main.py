import time
import datetime
import pygame


def play_sound(sound_file: str) -> None:
    """Play an alarm sound until it finishes."""
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)


def set_alarm(alarm_time: str, sound_file: str = "alarm.wav") -> None:
    """Check the current time and play a sound when the alarm time is reached.

    After the alarm triggers, the user may choose to snooze for a number of
    minutes. This sets a new alarm relative to the current time.
    """
    print(f"Alarm set for {alarm_time}")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if alarm_time == current_time:
            print("Your time is up")
            play_sound(sound_file)
            snooze_choice = input("Snooze? (y/n): ").strip().lower()
            if snooze_choice == "y":
                minutes = int(input("Snooze duration in minutes: "))
                alarm_time = (
                    datetime.datetime.now() + datetime.timedelta(minutes=minutes)
                ).strftime("%H:%M:%S")
                print(
                    f"Snoozed for {minutes} minutes. New alarm at {alarm_time}."
                )
            else:
                break
        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Set alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
