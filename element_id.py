import pandas as pd
import os

def element2id(element,output=False):
    data_path = os.listdir("./data/")
    villages = []
    floors = []
    types = []

    for csv in data_path:
        csv_path = os.path.join("./data/",csv)
        csv_file = pd.read_csv(csv_path)

        village_info = csv_file.loc[1:,"鄉鎮市區"]
        floor_info = csv_file.loc[1:,"總樓層數"]
        type_info = csv_file.loc[1:,"建物型態"]


        for village in village_info:
            if village not in villages:
                villages.append(village)

        for floor in floor_info:
            if floor not in floors:
                floors.append(floor)

        for typ in type_info:
            if typ not in types:
                types.append(typ)
    
    #print(villages)
    #print(floors)
    #print(types)
    #print(list(enumerate(villages,start=1)))
    if output:
        if element == "village":
            with open("./fk/village.csv",'w') as vill:
                vill.write("ID, Village\n")
                for ids, value in list(enumerate(villages,start=1)):
                    vill.write("{},{}\n".format(ids,value))
        if element == "floor":
            with open("./fk/floor.csv",'w') as f:
                f.write("ID, Floor\n")
                for ids, value in list(enumerate(floors,start=1)):
                    f.write("{},{}\n".format(ids,value))
        if element == "type":
            with open("./fk/type.csv",'w') as f:
                f.write("ID, Type\n")
                for ids, value in list(enumerate(types,start=1)):
                    f.write("{},{}\n".format(ids,value))
    else:
        if element == "village": return list(enumerate(villages,start=1))
        if element == "floor": return list(enumerate(floors,start=1))
        if element == "type": return list(enumerate(types,start=1))


if __name__ == '__main__':
    element2id("type",output=True)
