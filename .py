recursos_ecosistema = {"agua": 1000, "alimento": 800}
    
def animal_interactua(tipo_animal, cant_alimen, cant_agua=None):
    global recursos_ecosistema
    if tipo_animal == "herbívoro":
        if recursos_ecosistema["agua"] >= cant_agua and recursos_ecosistema["alimento"] >= cant_alimen:
            recursos_ecosistema["agua"] -= cant_agua
            recursos_ecosistema["alimento"] -= cant_alimen
            print(f"Un herbívoro ha consumido {cant_agua} de agua y {cant_alimen} de alimento.")
        else:
            print("Recursos insuficientes en el ecosistema")
            return
    elif tipo_animal == "carnívoro":
        if recursos_ecosistema["alimento"] >= cant_alimen:
            recursos_ecosistema["alimento"] -= cant_alimen
            print(f"Un carnívoro ha consumido {cant_alimen} de alimento.")
        else:
            print("Recursos insuficientes en el ecosistema")
            return
        
    print(f"Estado actual del ecosistema: {recursos_ecosistema}.")


def lluvia(agua):
    global recursos_ecosistema
    recursos_ecosistema["agua"] += agua
    print(f"¡Ha llovido! Se añadieron {agua} unidades de agua al ecosistema.")
    
print("Inicio del día en el ecosistema:",recursos_ecosistema,".")
animal_interactua("herbívoro", 100, 200)
animal_interactua("carnívoro", 50)
lluvia(200)
print("Fin del día en el ecosistema: [recursos actuales].")