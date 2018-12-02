from os import system
import sys, tty, termios


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def say(msg, *args):
    if args:
        msg = msg % args
    system('say -v Mei-jia %s' % msg)

if __name__ == '__main__':
    print(getch())
