import random
import turtle

# Screen settings
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Catch The Turtle Game")

# Global variables
game_over = False
score = 0
high_score = 0
FONT = ('Arial', 20, 'normal')  # Reduced font size
grid_size = 10

# List to hold all the turtles
turtle_list = []

# Turtles for displaying score and countdown/game over message
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()

def update_scoreboard():
    """Updates the scoreboard with the current score and high score."""
    score_turtle.clear()
    score_turtle.write("Score: {}   High Score: {}".format(score, high_score),
                       move=False, align='center', font=FONT)

def setup_score_turtle():
    """Sets up the turtle that displays the score."""
    score_turtle.hideturtle()
    score_turtle.color("blue")
    score_turtle.penup()
    top_height = screen.window_height() / 2
    score_y = top_height - top_height / 8  # Position for score display
    score_turtle.setposition(0, score_y)
    update_scoreboard()

def make_turtle(x, y):
    """Creates a turtle at the given grid coordinates and sets up its click event."""
    t = turtle.Turtle()
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)

    def handle_click(x_click, y_click):
        global score
        if not game_over:
            score += 1
            # Randomize turtle color on click for a fun effect
            t.color(random.choice(["green", "red", "blue", "purple", "orange"]))
            update_scoreboard()
            print("Clicked at:", x_click, y_click)

    t.onclick(handle_click)

def setup_turtles():
    """Initializes all turtles used in the game."""
    x_coordinates = [-20, -10, 0, 10, 20]
    y_coordinates = [20, 10, 0, -10]
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    """Hides all turtles from the screen."""
    for t in turtle_list:
        t.hideturtle()

def show_random_turtle():
    """Randomly displays one turtle and repeats this action every 500ms."""
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_random_turtle, 500)

def countdown(time_left):
    """Displays a countdown timer. Ends the game when time runs out."""
    global game_over, high_score, score
    top_height = screen.window_height() / 2
    score_y = top_height - top_height / 250
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.setposition(0, score_y - 70)  # Position further below the score
    countdown_turtle.clear()

    if time_left > 0:
        countdown_turtle.write("Time: {}".format(time_left),
                               move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time_left - 1), 1000)
    else:
        game_over = True
        # Update high score if the current score is higher
        if score > high_score:
            high_score = score
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write("Game Over! Press 'R' to Restart",
                               align='center', font=FONT)
        screen.onkey(restart_game, "r")
        screen.listen()

def restart_game():
    """Restarts the game if it is over."""
    global game_over, score
    if game_over:
        score = 0
        game_over = False
        update_scoreboard()
        countdown_turtle.clear()
        hide_turtles()
        show_random_turtle()
        screen.ontimer(lambda: countdown(10), 10)

def start_game():
    """Starts the game by initializing score, turtles, and timers."""
    global game_over, score
    game_over = False
    score = 0
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_random_turtle()
    turtle.tracer(1)
    # Start a 10-second countdown
    screen.ontimer(lambda: countdown(10), 10)

# Start the game
start_game()
turtle.mainloop()
