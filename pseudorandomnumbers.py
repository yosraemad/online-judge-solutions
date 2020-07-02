import math
import sys


def checkInput(steps, mods):
    i = 0
    while(i < len(steps)):
        if math.gcd(steps[i], mods[i]) == 1:
            sys.stdout.write("%10d %10d    Good Choice\n" %
                             (steps[i], mods[i]))
        else:
            sys.stdout.write("%10d %10d    Bad Choice\n" % (steps[i], mods[i]))
        print()
        i += 1


def main():
    steps = []
    mods = []
    while (1):
        try:
            step, mod = input().split()
        except ValueError:
            break
        if int(step) < 1:
            return
        if int(mod) > 100000:
            return
        steps.append(int(step))
        mods.append(int(mod))

    checkInput(steps, mods)


if __name__ == "__main__":
    main()
