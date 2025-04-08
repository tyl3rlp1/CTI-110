import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
tyler = turtle.Turtle()    # Create a turtle, assign to alex

for i in [0,1,2,3]:
    tyler.forward(50)
    tyler.left(90)
    
wn.mainloop()             # Wait for user to close window
