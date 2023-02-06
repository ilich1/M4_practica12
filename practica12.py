import json
def practica12B():
    datas = """
    {
    "book": [
    {"titel":"la vida es una",
     "cover": "dura",
    "year": "1990",
    "pages": "100"
    }
    {"titel":"mar,tierra y aire",
    "cover":"blanda",
    "year":"1989",
    "pages":"1000",
    }                           #parte del json que nos pide el ejercicio
    {"titel":"crepusculo",
    "cover":"dura",
    "year":"200",
    "pages":"400"
    }
    {"titel":"el anochecer",
    "cover":"blanda",
    "year":"2001",
    "pages":"300",
    }
    ]


}
"""
    with open("datas",'w')as file:
        json.dump(datas,file)   #codigo para crear el archivo json

    with open("datas", 'r') as file:
        result = json.load(file)   #codigo para imprimir el archivo json
        print(result)
practica12B()