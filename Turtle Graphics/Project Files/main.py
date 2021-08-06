# from turtle import Turtle, Screen
# # import another_module
#
# # print(another_module.another_variable)
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color('blue4')
# timmy.fd(100)
#
# my_screen = Screen()
#
# my_screen.exitonclick()
import prettytable

table = prettytable.PrettyTable()

table.add_column("Pokemon Name", ['Pikachu', "Squirtle", 'Charmander'])
table.add_column("Type", ["Electric", 'Water', "Fire"])
table.align = 'l'
print(table)
