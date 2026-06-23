#mission 1
config= {}
config.setdefault("timeout",30)
print(config)
config.setdefault("timeout",31)
print(config)
#mission 2
d1={"a":1,"b":2}
d2={"b":3,"c":4}
merged=d1 | d2
print(merged)
#mission 3
try_pop= {"name":"chaim","age":21}
print(try_pop.pop("age"))
#print(try_pop.pop("ch"))
#misson 4
nested={"server":{"host":"localhost","port":80}}
print(nested["server"]["port"])