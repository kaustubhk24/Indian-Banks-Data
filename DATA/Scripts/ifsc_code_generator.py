import json,os

bad_chars = [';', ':', '!', "*","\n",'?','.','/',"."]

def getData(bank,state,district,city,center,branch,details):
    for i in bad_chars:
        bank=bank.replace(i,'')
        state=state.replace(i,'')
        district=district.replace(i,'')
        city=city.replace(i,'')
        center=center.replace(i,'')
        branch=branch.replace(i,'')
        ifsc=details['IFSC']
        if not os.path.exists("IFSC/"+ifsc):
            os.makedirs("IFSC/"+ifsc)
            file="IFSC/"+ifsc+"/"+"index.html"
            f=open(file,"w+")
            json.dump(details,f)
            print(ifsc)

        
 



        


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



for root, dirs, files in os.walk("C:\\Users\\Kaustubh\\Downloads\\data"):
    for file in files:
        if file.endswith('.json') :
            print(file)
            start(file)

