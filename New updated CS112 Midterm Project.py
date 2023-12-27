import turtle
import pyttsx3

def ask_question(question):
    font_size = 20
    turtle.write(question, align="center", font=("Arial", font_size, "normal"))
    turtle.forward(50)
    turtle.update()

    turtle.color("green")  # Change color to green for a voter-related theme
    turtle.circle(10, 180)
    turtle.color("black")

    turtle.delay(300)

    response = turtle.textinput("Voter's Eligibility Checker", "")
    turtle.clear()
    return response

def draw_check_mark():
    turtle.penup()
    turtle.goto(-20, 0)
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    turtle.goto(20, 0)
    turtle.pendown()
    turtle.circle(5)

def draw_cross_mark():
    turtle.penup()
    turtle.goto(-20, 0)
    turtle.pendown()
    turtle.left(45)
    for _ in range(4):
        turtle.forward(10)
        turtle.backward(10)
        turtle.left(90)
    turtle.right(45)

def display_message(message, eligibility):
    turtle.clear()
    turtle.write(message, align="center", font=("Arial", 16, "normal"))
    if eligibility:
        turtle.penup()
        turtle.goto(0, -50)
        turtle.pendown()
        turtle.circle(50)
        draw_check_mark()
    else:
        turtle.penup()
        turtle.goto(0, -50)
        turtle.pendown()
        turtle.circle(50)
        draw_cross_mark()
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()

def speak_message(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def draw_welcome_design():
    turtle.color("blue")
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(-200, 150)
    turtle.pendown()
    turtle.write("👋 Welcome to the Voter's Eligibility Checker!", align="left", font=("Arial", 18, "normal"))
    turtle.forward(400)
    turtle.penup()
    turtle.goto(-200, 120)
    turtle.pendown()
    turtle.write("🎉 Let's check if you are eligible to vote. 🗳️", align="left", font=("Arial", 16, "normal"))
    turtle.penup()
    turtle.goto(-200, 90)
    turtle.pendown()
    turtle.forward(400)

def draw_exit_button():
    turtle.penup()
    turtle.goto(-380, -280)
    turtle.pendown()
    turtle.color("red")
    turtle.write("Exit", align="left", font=("Arial", 14, "normal"))

def is_exit_clicked(x, y):
    return -380 <= x <= -320 and -290 <= y <= -270

def on_exit_click(x, y):
    if is_exit_clicked(x, y):
        turtle.bye()

# Main program
turtle.title("Voter's Eligibility Checker")
turtle.bgcolor("lightgray")
turtle.speed(1)
turtle.setup(width=800, height=600)

draw_welcome_design()

turtle.penup()
turtle.goto(0, 200)
turtle.pendown()

name = ask_question("What is your name?")

age_str = ask_question("Hello, " + name + "!\nHow old are you? 🎂")
age = int(age_str)

citizenship = ask_question("Are you a citizen of this country? (Yes/No) 🗽")

criminal_record = ask_question("Do you have any felony convictions? (Yes/No) ⚖️")

voter_eligibility_age = 18

if age >= voter_eligibility_age and citizenship.lower() == "yes" and criminal_record.lower() == "no":
    display_message("Congratulations, " + name + "!\nYou are eligible to vote in the upcoming elections! 🗳️✅", True)
    speak_message("Great news! You meet all the criteria and are eligible to vote. Exercise your right!")
else:
    display_message("Sorry, " + name + ".\nYou are not eligible to vote at the moment.\nMake sure to check the requirements. 🚫😢", False)
    speak_message("Sorry, " + name + ". Make sure to meet all the criteria to be eligible to vote in the future.")

draw_exit_button()

turtle.hideturtle()
turtle.listen()
turtle.onscreenclick(on_exit_click)
turtle.mainloop()
