from __future__ import print_function
import time
import argparse
from multiprocessing import Process
import os


def announce(msg, sleepseconds=0.0, daemon=True):
    process = Process(target=announce_inner,
                      args=(msg, sleepseconds,), daemon=daemon)
    process.start()


if os.name == "nt":
    import win32com.client as wincl

    def _say(sentence, sleepseconds=0.5):
        try:
            speaker = wincl.Dispatch("SAPI.SpVoice")
            speaker.Speak(sentence)
            time.sleep(sleepseconds)
        except Exception as ex:
            print("Error in speaking: ".format(ex.msg))
else:
    def _say(sentence, sleepseconds=0.5):
        os.system("say {0}".format(sentence))
        time.sleep(sleepseconds)


def announce_inner(msg, sleepseconds):
    _say(msg, sleepseconds)


def countdown(t, sayit):
    time2voice = []
    if sayit:
        time2voice = list(range(sayit*60, t, sayit*60))
    # print(time2voice)
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        if t in time2voice:
            msg = "{} mins remaining.".format(mins)
            announce(msg)
        t -= 1
    announce("Times up buddy!", daemon=False)
    print('Done!\n\a\a\a\a\a')



def main():
    parser = argparse.ArgumentParser(description="Countdown timer")
    parser.add_argument("-s", "--seconds", type=int,
                        help="Time in seconds", default=60)
    parser.add_argument("-v", "--say", type=int, default=0,
                        help="Say the remaining every minute")
    args = parser.parse_args()

    process = Process(target=countdown,
                      args=(args.seconds, args.say,), daemon=False)
    process.start()


if __name__ == "__main__":
    main()
