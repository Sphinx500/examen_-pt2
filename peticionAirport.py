import json
from urllib import response
import requests


class AirportRest():

    def createData():

        try: 
            archivo = "Clientes.txt"

            with open(archivo) as f:
                for x in f:
                    out = str(x).split(",")
                    data = {'firstname':out[0],'surname':out[1],'country':out[2],'language':out[3],'airport':out[4]}

        except FileNotFoundError:
                    print('¡El fichero ' + archivo + ' no existe!\n')
        except ValueError as err:
            print(err)
        finally:
            f.close()

        try:
            with open("json-test.json", "w") as j:
                json.dump(data, j, indent = 4)

        except ValueError as err:
            print(err)

    def sendData():
        api_url = "http://localhost:8080/employee/apiv1/clientes/add"
        try:
            with open("json-test.json", "w") as jsonfile:
                data = json.load(jsonfile)
            
            response = requests.post(api_url, json=data)
            response.json()

        except ValueError as err:
            print(err)
        
        except FileNotFoundError:
                    print('¡El fichero ' + jsonfile + ' no existe!\n')