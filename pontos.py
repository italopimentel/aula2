import math

def distancia(x2,x1,y2,y1):
    math.sqrt(math.pow(x2 - x1) + math.pow(y2 - y1))

pontoA = []
pontoB = []

for i in range(0,5):
    ponto_A = input("Digite as cordenadas x e y do ponto separadas por ','").split(',')
    
