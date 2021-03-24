import json,os

bad_chars = [';', ':', '!', "*","\n",'?','.','/']

def getData(bank,state,district,city,center,branch,details):
    for i in bad_chars:
        bank=bank.replace(i,'')
        state=state.replace(i,'')
        district=district.replace(i,'')
        city=city.replace(i,'')
        center=center.replace(i,'')
        branch=branch.replace(i,'')

    if not os.path.exists(state):
        os.makedirs(state)
    if not os.path.exists(state+"/"+district):
        os.makedirs(state+"/"+district)
    if not os.path.exists(state+"/"+district+"/"+city):
        os.makedirs(state+"/"+district+"/"+city)
    if not os.path.exists(state+"/"+district+"/"+city+"/"+center):
        os.makedirs(state+"/"+district+"/"+city+"/"+center)
    try:
        fb=open(state+"/"+district+"/"+city+"/"+center+"/"+branch+".json","w+")
        json.dump(details,fb)
    except :
        print("Error at : "+state+"/"+district+"/"+city+"/"+center+"/"+bank+"-"+branch+".json")

        


def start(file_name):
    file=open(file_name)
    data = json.load(file) 
    for i in range(0,len(data)):
        bank=data[i]['BANK'].strip()
        state=data[i]['STATE'].strip()
        district=data[i]['DISTRICT'].strip()
        city=data[i]['CITY'].strip()
        center=data[i]['CENTRE'].strip()
        branch=data[i]['BRANCH'].strip().replace('/',' ')
        details=data[i]
        getData(bank,state,district,city,center,branch,details)



for root, dirs, files in os.walk("C:\\Users\\Kaustubh\\Downloads\\JSON"):
    for file in files:
        if file.endswith('.json') :
            print(file)
            start(file)