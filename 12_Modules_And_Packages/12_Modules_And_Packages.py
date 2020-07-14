# game.py
# import the draw module
import draw


def play_game():
    ...



# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()

# In this example, the game module imports the draw module, which enables it to use functions implemented 
# in that module. The main function would use the local function play_game to run the game, and then draw 
# the result of the game using a function implemented in the draw module called draw_game. To use the function 
# draw_game from the draw module, we would need to specify in which module the function is implemented, 
# using the dot operator. To reference the draw_game function from the game module, we would need to import
# the draw module and only then call draw.draw_game().

# When the import draw directive will run, the Python interpreter will look for a file in the directory
# which the script was executed from, by the name of the module with a .py prefix, so in our case it will 
# try to look for draw.py. If it will find one, it will import it. If not, he will continue to look for 
# built-in modules.

# You may have noticed that when importing a module, a .pyc file appears, which is a compiled Python file. 
# Python compiles files into Python bytecode so that it won't have to parse the files each time modules are 
# loaded. If a .pyc file exists, it gets loaded instead of the .py file, but this process is transparent to 
# the user.

#---importing module objects to the current namespace----
# We may also import the function draw_game directly into the main script's namespace, by using the from command.

def main():
    result = play_game()
    draw.draw_game(result)

# You may have noticed that in this example, draw_game does not precede with the name of the module it is 
# imported from, because we've specified the module name in the import command.

# The advantages of using this notation is that it is easier to use the functions inside the current module
# because you don't need to specify which module the function comes from. However, any namespace cannot have
# two objects with the exact same name, so the import command may replace an existing object in the namespace.

# ----Importing all objects from a module-----
