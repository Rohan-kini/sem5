graph = {
  'A': ['B', 'C'],
  'B': ['A','D','E'],
  'C': ['A','F','G'],
  'D': [],
  'E': [],
  'F': ['H','I'],
  'G': [],
  'H': [],
  'I': []
}


def dfid(graph,curr_node,goal_node,visited,path,depth):
    for i in range(1,depth+1):
        print(f"Depth:{i}")
        path,status=dfs(graph,curr_node,goal_node,[],[],0,i)
    
    return path,status

def dfs(graph,curr_node,goal_node,visited,path,curr_depth,depth):
    if curr_depth<=depth:
        if curr_node not in visited:
            path.append(curr_node)
            visited.append(curr_node)
            not_visited=[i for i in graph.keys() if i not in visited]

            if curr_node==goal_node:
              print(f"{visited}\t\t{not_visited}\t\tTrue")
              return path,True
            print(f"{visited}\t\t{not_visited}\t\tFalse")

            for i in graph[curr_node]:
               path,status=dfs(graph,i,goal_node,visited,path,curr_depth+1,depth)
               if status==True:
                     return path,True
        return path,False

    else:
        return path,False
    

path1,status=dfid(graph,'A','G',[],[],3)

if status:
    print(f"Found path:\n{path1}")
else:
    print("not found")