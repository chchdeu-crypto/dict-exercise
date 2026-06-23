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
#mission 6
del agent["active"]
print(agent)
#missin 7
print(agent.keys())
print(agent.values())
print(agent.items())
#mission 8
print("score" in agent)
#mission 9
scores={"alpha":80,"bravo":95,"charlie":70}
print(max(scores))
#mission 10
new_agents=agent.copy()
new_agents["name"]="chaim"
print(agent)
print(new_agents)