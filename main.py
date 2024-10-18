# import another_module
#
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
#
# timmy = Turtle() # Assigned Turtle class to timmy, making an object
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkMagenta")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight) # Prints an attribute canvheight of my_screen object
# my_screen.exitonclick() # Method exitonclick of my_screen object is triggered, will exit the screen when it's clicked

# Creating a table in ASCII with prettytable package (not build in)
# To see source code of a package, right click, go to, implementation(s)
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table.align)
print(table)
