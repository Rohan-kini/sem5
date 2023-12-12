def worstfit(mb, ps):
    allocation = [-1] * len(ps)

    for i in range(len(ps)):
        worst_index = -1  # Initialize the index of the block with worst fit
        for j in range(len(mb)):
            if mb[j] >= ps[i]:
                if worst_index == -1 or mb[j] > mb[worst_index]:
                    worst_index = j

        if worst_index != -1:
            allocation[i] = worst_index
            mb[worst_index] -= ps[i]

    return allocation

if __name__ == "__main__":
    memory_blocks = [100, 200, 300, 400, 500]
    process_size = [99, 101, 150, 401]
    allocation = worstfit(memory_blocks, process_size)

    print("Process no.\tProcess Size\tBlock no.")
    for i in range(len(process_size)):
        print(f"{i+1}\t\t{process_size[i]}\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")
