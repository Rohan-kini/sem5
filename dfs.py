def dfs(graph,root,destination):
    visited=[]
    stack=[root]

    while stack:
        print(stack,end="")
        vertex=stack.pop()

        print(visited,end="\t")
        print(destination)

        if vertex not in visited:
            visited.append(vertex)

        if vertex==destination:
            print(f"Goal node {destination} found")
            return

        for neighbors in reversed(graph[vertex]):
            if neighbors not in visited:
                stack.append(neighbors)

    print("Goal node not found")

graph={0:[1,2],
       1:[3,4,5],
       2:[5,6],
       3:[],
       4:[],
       5:[7],
       6:[],
       7:[]}

print("Following is the graph traversal")
dfs(graph,0,7)
