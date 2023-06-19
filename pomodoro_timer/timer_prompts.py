import time
from msvcrt import getch, kbhit
from pomodoro import Pomodoro


def sixty_minutes(pom):
    """Initiates 60 minute break.

    Start the Pomodoro timer and informs the user when the timer is expected to finish.

    Args:
        pom (Pomodoro): A pomodoro class object that holds a Time object and modifies time values
    """
    pom.start_timer()
    # Prints out expected time - users may be interested when pomodoro will end
    print(
        "You've just begun the 60 minute timer - Your expected time to finish is",
        time.strftime("%I %M %p", time.localtime(time.time() + 60 * 60)),
    )


def thirty_minutes(pom):
    """Initiates 30 minute break.

    Start the Pomodoro timer and informs the user when the timer is expected to finish.

    Args:
        pom (Pomodoro): A pomodoro class object that holds a Time object and modifies time values
    """
    pom.start_timer()
    print(
        "You've just begun the 30 minute timer - Your expected time to finish is",
        time.strftime("%I %M %p", time.localtime(time.time() + 30 * 60)),
    )


def twenty_min_break(pom):
    """Initiates 20 minute break.

    Stops the Pomodoro timer and informs the user that a 20-minute break has begun

    Args:
        pom (Pomodoro): A pomodoro class object that holds a Time object and modifies time values
    """


def health_break(pom):
    """Initiates health break until user input.

    Pauses the Pomodoro timer and queries for user to unpause. User must perform physical activities
    during the break.

    Args:
        pom (Pomodoro): A pomodoro class object that holds a Time object and modifies time values
    """
    pom.pause_timer()
    while True:
        space = input(
            "You've hit the 30 minute mark. You need to stand up, \
            walk around for a little, and come back. \
            Press [ENTER] when ready. "
        )
        if space == "":
            return
        print("What? Did you finish? Get back up and go, then press [ENTER] when done!")


def display(pom):
    print(True)


def grab_user_input(pom):
    try:
        length = input("How many minutes? [30/60] Press [ENTER] to quit: ")
        if length == "":
            print()
            print("Thanks for using pomodoro")
            return length

        length = int(length)
        if length == 30:
            thirty_minutes(pom)
        elif length == 60:
            sixty_minutes(pom)
        else:
            print("You've entered an invalid time. Please try again")
            grab_user_input(pom)
    except:
        print("Are you trying to quit? If so, press enter, or provide a time. ")
        length = grab_user_input(pom)
    return length


def stop_clock(pom):
    pass


if __name__ == "__main__":
    p = Pomodoro()

    while True:
        length = grab_user_input(p)
        if length == "":
            break
        print("D to display time - P to pause - S to stop ")
        x = round(p.current_time()) + 30 * 60

        while True:
            if kbhit():  # True if user presses a key
                key = ord(getch()) - 97
                if key == 3:
                    display(p)

            if round(p.current_time()) >= 30 * 60:
                if length == 60:
                    print()
                    health_break(p)
                    x += x
                    length = 30

                elif length == 30:
                    stop_clock(p)
                    print()
                    print("Congratulations! You've finished 1 30-minute pomodoro")
                    break
