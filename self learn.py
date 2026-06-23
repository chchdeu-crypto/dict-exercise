#mission 1
# Stores key and value information using a hash function to map the key to an exact location in memory.
# And when I want to find something, I'll search by the key and it passes it through the hash function and then it knows how to find it quickly.
#misson 2
#For the mechanism to work, the key code must remain the same and cannot be changed because if it changes, I won't be able to find it.
#list
#mission 3
#When searching the list, it has to go through one by one until it finds it, and if there are 5000 entries, it will have to list them one by one, unlike a dictionary, which takes the same time whether there are 5000 entries or just one.
#Because a list has no particular order, it will have to go through it one by one, unlike a dictionary, which it searches through a hash function, so it instantly calculates the exact position.
names = {}
names.update({"chaim":21,"yossi":23,"avi":26})
print(names)
tupels=[("a",1),("b",2)]
dicts=dict(tupels)
print(dicts)
