from DATA import DATA

def run():
    nombre = "Platzi"
    filtraNombre = list(filter(lambda name: name["organization"] == nombre, DATA))
    filtraNombre = list(map(lambda name: name["name"], filtraNombre))

    filtraOrganization = [worker["name"] for worker in DATA if worker["organization"]=="Platzi"]
    print(filtraOrganization) 

if __name__ == "__main__":
    run()
#    for name in DATA:
#        nombre = name["name"]
#        print(nombre)