def playList(songs):
    songSet=set()
    l=0
    res=0
    for r in range(len(songs)):
       while songs[r] in songSet:
           songSet.remove(songs[l])
           l+=1
       songSet.add(songs[r])
       res=max(res,r-l+1)
    return res

print(playList([1,2,1,3,5,4,3,1]))


def max_length(songs):
    n=len(songs)
    pos={}
    start,length=0,0
    for i,song in enumerate(songs):
        if song in pos:
            start=max(start,pos[song]+1)
        length=max(length,i-start+1)
        pos[song]=i
    return length