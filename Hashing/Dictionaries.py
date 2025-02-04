weights = {}

weights["apina"] = 100
weights["banaani"] = 1
weights["cembalo"] = 500

weights = {"apina": 100, "banaani": 1, "cembalo": 500}

print(weights["apina"]) # 100
weights["apina"] = 150
print(weights["apina"]) # 150

#in if the key is in the dict
print("apina" in weights) # True
print("ananas" in weights) # False

print(weights) # {'apina': 100, 'banaani': 1, 'cembalo': 500}
del weights["banaani"]
print(weights) # {'apina': 100, 'cembalo': 500}


# seen elements
items=[]
seen={}
for x in items:
    seen[x]=True

#Set seen
seen=set()
for x in items:
    seen.add(x)

#Counting occurance
count = {}
for x in items:
    if x not in count:
        count[x] = 0
    count[x] += 1

#position of occurance
pos = {}
for i, x in enumerate(items):
    pos[x] = i