def best_fit(mb,ps):
    allocation=[-1]*len(ps)

    for i in range(len(ps)):
        best_index=-1
        for j in range(len(mb)):
            if mb[j]>=ps[i]:
                if best_index==-1:
                    best_index=j
                elif mb[j]<mb[best_index]:
                    best_index=j
        
        if best_index!=-1:
            allocation[i]=best_index
            mb[best_index]-=ps[i]
    return allocation


if__name__="__main__"

memory_blocks=[100,200,300,400,500]
process_size=[101,150,350,401]
allocation=best_fit(memory_blocks,process_size)

print(f"Process No. \t Process Size \t Block No.")
for i in range (len(process_size)):
    print(f"{i+1}\t\t{process_size[i]}\t\t",end="")
    if allocation[i]!=-1:
        print(allocation[i]+1)
    else:
        print("Not Allocated")