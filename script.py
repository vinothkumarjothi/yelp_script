import json
import csv

sourceJsonPath = "D:\pythonws\yelp_script\yelp_source.json"
decPath = "D:\pythonws\yelp_script\organised.json"
csvpath = "D:\pythonws\yelp_script\organised_file.csv"


def readSourceInput():
    with open(sourceJsonPath) as f:
      return json.load(f)

def convertIntoCSV():
    with open(decPath,'r') as dec_json_file:
        organised_data = json.load(dec_json_file)
    
    data_file = open(csvpath, 'w')
    csv_writer = csv.writer(data_file)
    
    count = 0
    for data in organised_data:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())
    
    data_file.close()

def asign_default(x):
    data = {
        "alias":x["alias"],
        "title":x["title"],
        "parents":"",
        "country_whitelist":"",
        "country_blacklist":""
    }
    return data 

def writeAsJson(data):
    with open(decPath, 'w') as json_file:
        json.dump(data, json_file)

def prepareInduvialItem(source):
    datas = []
    for x in source:
        data = asign_default(x)
        havingSub = False
        if 'parents' in x:
            for p in x['parents']:
                data = asign_default(x)
                data["parents"] = p
                datas.append(data)
                havingSub = True

        if 'country_whitelist' in x:
            for c_w in x['country_whitelist']:
                data = asign_default(x)
                data["country_whitelist"] = c_w
                datas.append(data)
                havingSub = True

        if 'country_blacklist' in x:
            for c_b in x['country_blacklist']:
                data = asign_default(x)
                data["country_blacklist"] = c_b
                datas.append(data)
                havingSub = True

        if havingSub == False:
            datas.append(data)
    return datas

sourceData = readSourceInput()

writeAsJson(prepareInduvialItem(sourceData))

convertIntoCSV()
