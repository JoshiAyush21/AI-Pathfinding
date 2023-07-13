import os

size_str = ""
size_option = int(input("Maze Size : \n 1. Tiny \n 2. Medium \n 3. Big \n 4. Custom \n>> "))

size_option_list = ["tinyMaze","mediumMaze","bigMaze -z 0.5 ", "customMaze"]

if size_option == 1:
    size_str = "tinyMaze"

elif size_option == 2:
    size_str = "mediumMaze"

elif size_option == 3:
    size_str = "bigMaze -z 0.5 "

elif size_option == 4:
    # size_str = "customMaze -z 0.5 "
    print("Layout Options")
    layout_options = os.listdir("./TeamProjectLayouts/cleanLayouts/randomLayouts")

    option = {i+1 : file for i,file in enumerate(layout_options)}

    for key in option.keys():
        print(key, ":", option[key])
    
    layout_selected = int(input("Select your option(int) : "))

    size_str = "./TeamProjectLayouts/cleanLayouts/randomLayouts/"+str(option[layout_selected])




agent_str = ""
agent_option = int(input("Agent: \n 1. BFS \n 2. DFS \n 3. A_Star \n 4. UCS \n 5. MM0 \n 6. MM \n>> "))

agent_option_list = ["bfs","dfs","astar","ucs","mm0","mm"]


os.system("python pacman.py -l " + size_str + " -p SearchAgent -a fn=" + agent_option_list[agent_option-1])

# else:
#     for option in agent_option_list:
#         os.system("python3 pacman.py -l " + size_str + " -p SearchAgent -a fn=" + option)

# os.system("python3 pacman.py -l " + size_str + " -p SearchAgent -a fn=" + agent_str)


# python3 pacman.py -l customMaze -p SearchAgent -a fn=mm0 -z 0.5