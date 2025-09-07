"""Simple alarm clock with multiple alarms and custom sound support."""

import datetime
import os
import time

import pygame


def play_sound(sound_file: str) -> None:
    """Play the provided sound file until completion."""
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)


def set_alarm(alarm_time: str, sound_file: str) -> None:
    """Wait until *alarm_time* and then play *sound_file*."""
    print(f"Alarm set for {alarm_time}")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Your time is up")
            play_sound(sound_file)
            break
        time.sleep(1)


def main() -> None:
    alarm_input = input(
        "Set alarm time(s) (HH:MM:SS, separated by commas): "
    )
    alarm_times = [t.strip() for t in alarm_input.split(",") if t.strip()]

    sound_file = input("Enter path to sound file (default alarm.wav): ").strip() or "alarm.wav"
    if not os.path.exists(sound_file):
        print(f"Sound file '{sound_file}' not found")
        return

    for alarm_time in alarm_times:
        set_alarm(alarm_time, sound_file)


if __name__ == "__main__":
    main()

