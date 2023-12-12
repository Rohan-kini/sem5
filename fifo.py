def fifo(p,f):
    frames=[-1]*f
    frame_set=set()
    hit=0
    print(f"Pages are {p}\n")

    for page in p:
        if page not in frame_set:
            if len(frame_set)<f:
                frame_set.add(page)
                frames[len(frame_set)-1]=page
            
            else:
                out=frames.pop()
                frame_set.remove(out)
                frame_set.add(page)
                frames.append(page)
            print(f"Page {page} caused page fault.Page order {frames}")
        
        else:
            hit=hit+1
            print(f"Page {page} caused page hit.Page order {frames}")

    print(f"Page hits {hit}|Page faults {len(p)-hit}")

page_req=[1,2,3,4,3,2,5]
fsize=3
fifo(page_req,fsize)