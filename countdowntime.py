from __future__ import print_function
import time
import argparse



def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Done!\n\a\a\a\a\a')

def main():
    parser = argparse.ArgumentParser(description="Countdown timer")
    parser.add_argument("-s","--seconds" , type=int, help="Time in seconds", default=60)
    args = parser.parse_args()
    countdown(args.seconds)



if __name__ == "__main__":
    main()
