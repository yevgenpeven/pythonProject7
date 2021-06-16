import json
import xmltodict
import sys

try:
 file = sys.argv[1]
 with open(file, 'r', encoding='UTF-8') as xml_file, open("D:\convert\datasetjson.json", 'w', encoding='UTF-8') as json_file:
    data_dict = xmltodict.parse(xml_file.read())
    json_file.write(json.dumps(data_dict, indent=4, ensure_ascii=False))

    try:
        scor = sys.argv[2]
        gend = sys.argv[3]
        with open(file, 'r', encoding='UTF-8') as xml_file:
         data_dict = xmltodict.parse(xml_file.read())
        filtered = []
        for record in data_dict['dataset']['record']:
            if str(record['score']) > scor and record['gender'] == gend:
                filtered.append(record)
        filtered_with_root = {'dataset': {'record': filtered}}
        json_data_con = json.dumps(filtered_with_root, indent=4, ensure_ascii=False)
        with open('D:\convert\dataset_filter.json', 'w', encoding='UTF-8') as json_file_con:
            json_file_con.write(json_data_con)
        try:
          unparjson=sys.argv[4]
          parserxml=sys.argv[5]
          fileptr = open(unparjson, 'r', encoding='UTF-8')
          json_data = json.load(fileptr)
          data_dict1 = xmltodict.unparse(json_data, pretty=True)
          fileptr.close()
          with open(parserxml, 'w', encoding='UTF-8') as newxml_file:
           newxml_file.write(data_dict1)
        except:
            print('If you want to convert json to xml enter path  in parametr 4 for json, in 5 parament path to xml')
    except:
        print("If you want to filter with parameters enter parameters for filter: second - it's Scor, the third -it's Gender")

except:
    print('Enter link on xml file in parametrs')