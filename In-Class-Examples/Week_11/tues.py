# Topic 1: Turtle
# ---------------
    # What = Is for graphics and drawing on a canvas.
    # Why = For educational purposes for younger upcoming programmers (Kids).
    
import turtle

def about_turtle():
    # Set-Up:
    turtle.shape('turtle')
    turtle.shapesize(2)
    turtle.speed(10)
    turtle.color('green')
    turtle.pensize(2)
    # Heading = 0, Position = {0,0}
    
    # Control:
    for _ in range(20):
        turtle.forward(250)
        turtle.left(215)
        
    import random
    for _ in range(20):
        turtle.right(random.randint(0,360))
        turtle.goto(0,0)
        turtle.setheading(0)
        
    turtles = [turtle.Turtle() for _ in range(100)]
    turtleColors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple','black']
    for t in turtles:
        t.shape('turtle')
        t.shapesize(random.randint(0,5))
        t.speed(random.randint(1,10))
        t.color(random.choice(turtleColors))
        t.goto(random.randint(-200,200),random.randint(-200,200))
    
    # Finish:
    turtle.done()
    
about_turtle()

# Topic 2: Debugging
# ------------------
    # What = Fixing Errors or "Bugs" in a program.
        # - Syntax Errors: print("hello world"
        # - Runtime Errors: crash, average = / 0
        # - Semantic / Logical Errors: results are wrong, 2 + 2 = 5
    
    # How = Use the built in debugging tools in the IDE.
        # - Breakpoints, Stepping(In, Out, Over), Watching.
        
        


# Topic 3: Git & GitHub
#----------------------
    # My GitHub = https://github.com/N-McClure 
    
    # What is Git = Version control system.
        # - Used to track all changes in a project.
    
    # What is GitHub = A website used to store local Git repositories remotely.