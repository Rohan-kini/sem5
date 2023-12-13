graph = {
    'A' :{'B':9,'C':4,'D':7},
    'B' :{'E':11},
    'C' :{'E':17,'F':12},
    'D' :{'F':14},
    'E' :{'Z':5},
    'F' :{'Z':9}
}

graph_heu = {
    'A': 21,
    'B': 14,
    'C': 18,
    'D': 18,
    'E': 5,
    'F': 8,
    'Z':0
}

curr_node=input("Enter start node:")
goal_node=input("Enter goal node:")

def fnoffn(g1,cn):
    g=0
    print(g1,cn)
    for i in range (len(g1)-1):
        g+=graph[g1[i]][g1[i+1]]

    g+=graph[g1[-1]][cn]+graph_heu[cn]
    return g

open_list=[]
close_list=[]
open_list.append([curr_node,graph_heu[curr_node],[curr_node]])
print(open_list)

try:
    while True:
        parent_node=open_list[0][0]
        close_list.append(parent_node)
        print(open_list)
        curr_path=open_list[0][2]
        if parent_node==goal_node:
            break
        print(f"Currently at node : {parent_node}")
        for j in graph[open_list[0][0]]:
            open_list.append([j,fnoffn(curr_path,j),curr_path+[j]])
            open_list=sorted(open_list,key=lambda x: x[1])
        for i in open_list:
            if i[0]==parent_node:
                open_list.remove(i)
        print(f"Open list is {open_list}.\nClose list is {close_list}")
    print(f"So the optimized path is from {open_list[0][2][0]} to {goal_node} is {open_list[0][2]} with distance : {open_list[0][1]}")
except:
    print(f"Something error goal node not found")




