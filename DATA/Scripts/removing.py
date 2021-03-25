import json
f=open("CENTER.txt")
dt=json.loads(f.read())
f.close()
a=list(set(dt))
print(a)
fl=open("CENTER.txt","w")
kk=json.dumps(a)
fl.write(kk)