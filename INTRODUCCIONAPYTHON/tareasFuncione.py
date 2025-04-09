# funciones de area y volumen, Tarea

# Area y volumen de un cono truncado
def areaconotruncado(radio1, radio2, altura):
    pi = 3.1416
    area = pi * (radio1 + radio2) * ((radio1 - radio2) ** 2 + altura ** 2) ** 0.5
    return area
def volumencotruncado(radio1, radio2, altura):
    pi = 3.1416
    volumen = (1 / 3) * pi * altura * (radio1 ** 2 + radio1 * radio2 + radio2 ** 2)
    return volumen
# Area y volumen de una esfera
def areaesfera(radio):
    pi = 3.1416
    area = 4 * pi * radio ** 2
    return area
def volumenesfera(radio):
    pi = 3.1416
    volumen = (4 / 3) * pi * radio ** 3
    return volumen
# Area y volumen de un cilindro
def areacilindro(radio, altura):
    pi = 3.1416
    area = 2 * pi * radio * (radio + altura)
    return area
def volumencilindro(radio, altura):
    pi = 3.1416
    volumen = pi * radio ** 2 * altura
    return volumen