# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle,Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("chocolate")
# timmy.fd(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()  # table --> object from PrettyTable class
print(table)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Carmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
table.align = "r"
print(table)
