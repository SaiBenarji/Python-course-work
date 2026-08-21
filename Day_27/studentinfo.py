import json
with open('data.json','r') as file:
    data=json.load(file)
data["name"]="Sai Benarji"
data["branch"]="CSE"

with open('data.json','w') as file:
    print(data,file,'indent=4')