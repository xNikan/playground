from pomodoro import Pomodoro
import time     



def sixty_minutes(pom):
    pom.start_timer()
    print("You've just begun the 60 minute timer - Your expected time to finish is", \
           time.strftime("%I %M %p",time.localtime(time.time() + 60*60)))
    return 

def thirty_minutes(pom):
    pom.start_timer()
    print("You've just begun the 30 minute timer - Your expected time to finish is", \
          time.strftime("%I %M %p",time.localtime(time.time() + 30*60)))
    return 

def twenty_min_break(pom):
    pass 

def health_break(pom):
    pass

def display(pom):
    pass

def grab_user_input(pom):
    try:
        length = int(input("How many minutes? [30/60]: "))

        if (length == 30):
            thirty_minutes(pom) 
        elif (length == 60):
            sixty_minutes(pom)
        else:
            print("You've entered an invalid time. Please try again")
            grab_user_input(pom)
    except:
        print("Invalid entry. Please enter an int")
        grab_user_input(pom)
    return length

def stop_clock(pom):
    pass

if __name__ == "__main__":
    p = Pomodoro()


    length = grab_user_input(p)


    while True:
        if (round(p.current_time()) >= 3):
            if (length == 60):
                health_break(p)
            else:
                


                
        break


  






 