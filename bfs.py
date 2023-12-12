def bfs(graph,root,destination):
    open,close=[],[]
    open.append(root)
    close.append(root)

    while open:
        vertex=open.pop()
        print(vertex,end="")

        for neigbors in graph[vertex]:
            if neigbors not in close:
                close.append(neigbors)
                open.append(neigbors)

        print(open,end="")
        print(destination)

        if vertex==destination:
            print(f"Goal node {destination} found")
            return
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
bfs(graph,0,7)