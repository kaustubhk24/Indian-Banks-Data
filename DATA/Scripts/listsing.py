import os,json
states=[]
districts=[]
citys=[]
centers=[]
branchs=[]

states=os.listdir()
f=open("index.html","w+")
json.dump(states,f)

for state in states:
    if os.path.isdir(state):
        districts=os.listdir(state)
        fd=open(state+"/"+"index.html","w+")
        json.dump(districts,fd)


        for district in districts:
            if os.path.isdir(state+"/"+district):
                citys=os.listdir(state+"/"+district)
                fc=open(state+"/"+district+"/"+"index.html","w+")
                json.dump(citys,fc)
                
                
                for city in citys:
                    if os.path.isdir(state+"/"+district+"/"+city):
                        centers=os.listdir(state+"/"+district+"/"+city)
                        fce=open(state+"/"+district+"/"+city+"/"+"index.html","w+")
                        json.dump(centers,fce)


                        for center in centers:
                            if os.path.isdir(state+"/"+district+"/"+city+"/"+center):
                                branchs=os.listdir(state+"/"+district+"/"+city+"/"+center)
                                fceb=open(state+"/"+district+"/"+city+"/"+center+"/"+"index.html","w+")
                                json.dump(branchs,fceb)
