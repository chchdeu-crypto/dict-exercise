#nission 1
agent= {"name":"alpha","level":3,"active":True}
print(agent)
#mission 2
print(agent["name"])
#mission 3
print(agent.get("level"))
print(agent.get("la"))
#mission 4
agent["score"]=95
print(agent)
#mission 5
agent["level"]=5
print(agent)