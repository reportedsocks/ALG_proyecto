import numpy as np
import math

def levenshtein_matriz(x, y, threshold=None):
    # esta versión no utiliza threshold, se pone porque se puede
    # invocar con él, en cuyo caso se ignora
    lenX, lenY = len(x), len(y)
    D = np.zeros((lenX + 1, lenY + 1), dtype=np.int)
    for i in range(1, lenX + 1):
        D[i][0] = D[i - 1][0] + 1
    for j in range(1, lenY + 1):
        D[0][j] = D[0][j - 1] + 1
        for i in range(1, lenX + 1):
            D[i][j] = min(
                D[i - 1][j] + 1,
                D[i][j - 1] + 1,
                D[i - 1][j - 1] + (x[i - 1] != y[j - 1]),
            )
    return D[lenX, lenY]

def levenshtein_edicion(x, y, threshold=None):
    # a partir de la versión levenshtein_matriz
    lenX, lenY = len(x), len(y)
    D = np.zeros((lenX + 1, lenY + 1), dtype=np.int)
    for i in range(1, lenX + 1):
        D[i][0] = D[i - 1][0] + 1
    for j in range(1, lenY + 1):
        D[0][j] = D[0][j - 1] + 1
        for i in range(1, lenX + 1):
            D[i][j] = min(
                D[i - 1][j] + 1,
                D[i][j - 1] + 1,
                D[i - 1][j - 1] + (x[i - 1] != y[j - 1]),
            )
    camino = []
    indX = lenX
    indY = lenY

    while indX>0 or indY >0:
        
        xi = indX -1
        yi = indY
        c = D[xi,yi]
        op = (x[xi], "")

        if D[indX, indY -1] <= c:
            xi = indX
            yi = indY-1
            c = D[xi,yi]
            op = ("", y[yi])

        if D[indX-1, indY-1] <= c:
            xi = indX-1
            yi = indY-1
            c = D[xi,yi]
            op = (x[xi], y[yi])    

        camino.append(op)
        indX = xi
        indY = yi      

    camino.reverse()

    return D[lenX, lenY], camino


def levenshtein_reduccion(x, y, threshold=None):
    # completar versión con reducción coste espacial
    # COMPLETAR
    #----------------------------------------
    #     REVISAR ESTA PARTE
    # ---------------------------------------
    lenX, lenY = len(x), len(y)
    vcurrent = np.zeros(lenX + 1, lenY + 1)
    vnext = np.zeros(lenX + 1, lenY + 1)
    for i in range(1, lenX + 1):
        vcurrent[0] = 0
    for j in range(1, lenY + 1):
        vcurrent[j] = vprev[j]
        for i in range(1, lenX + 1):
            vcurrent[i] = max(vprev[i], vprev[i])
        vprev, vcurrent = vcurrent, vprev
    return vprev[lenX, lenY] 

def levenshtein(x, y, threshold):
    # completar versión reducción coste espacial y parada por threshold
     # COMPLETAR
    lenX, lenY = len(x), len(y)
    D = np.ones((lenX + 1, lenY + 1)) * np.inf #infinito positivo
    for i in range(0, lenX + 1):
        D[i, 0] = i
    for j in range(0, lenY + 1):
        D[0, j] = j
    d = lenX / lenY
    for i in range(1, lenX + 1):
        colMin = np.inf
        for j in range(max(math.floor(d*i-threshold), 1), min(math.ceil(d*i+threshold), lenY + 1)):
            if x[i - 1] == y[j - 1]:
                D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i-1][j-1])
            else:
                D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i-1][j-1] + 1)
            if colMin > D[i,j]:
                colMin = D[i,j]
        if colMin > threshold:
            return threshold+1
            #return None
    return D[lenX, lenY]

def levenshtein_cota_optimista(x, y, threshold):
    return 0 # COMPLETAR Y REEMPLAZAR ESTA PARTE

def damerau_restricted_matriz(x, y, threshold=None):
    # completar versión Damerau-Levenstein restringida con matriz
    # COMPLETAR
    #----------------------------------------
    #     REVISAR ESTA PARTE
    # ---------------------------------------
    lenX, lenY = len(x), len(y)
    D = np.zeros((lenX + 1, lenY + 1))
    for i in range(1, lenX + 1):
        D[i, 0] = i
    for j in range(1, lenY + 1):
        D[0, j] = j
    for i in range(1, lenX + 1):
        for j in range(1, lenY + 1):
            if i > 1 and j > 1 and x[i - 2] == y[j - 1] and x[i - 1] == y[j - 2]:
                if x[i - 1] == y[j - 1]:
                    D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i-1][j-1], D[i-2][j-2] + 1)
                else:
                    D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i-1][j-1] + 1, D[i-2][j-2] + 1)
            else:
                if x[i - 1] == y[j - 1]:
                    D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i-1][j-1])
                else:
                    D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i-1][j-1] + 1)
    return D[lenX, lenY]
    


def damerau_restricted_edicion(x, y, threshold=None):
    # partiendo de damerau_restricted_matriz añadir recuperar
    # secuencia de operaciones de edición
    return 0,[] # COMPLETAR Y REEMPLAZAR ESTA PARTE

def damerau_restricted(x, y, threshold):
    # versión con reducción coste espacial y parada por threshold
     # COMPLETAR Y REEMPLAZAR ESTA PARTE
     #----------------------------------------
    #     REVISAR ESTA PARTE
    # ---------------------------------------
    lenX, lenY = len(x), len(y)
    D = np.ones((lenX + 1, lenY + 1))*np.inf
    for i in range(0, lenX + 1):
        D[i, 0] = i
    for j in range(0, len(y) + 1):
        D[0, j] = j
    d = lenX/lenY
    for i in range(1, lenX + 1):
        colMin = np.inf
        for j in range(max(math.floor(d*i-threshold), 1), min(math.ceil(d*i+threshold), lenY + 1)):
            if i > 1 and j > 1 and x[i - 2] == y[j - 1] and x[i - 1] == y[j - 2]:
                if x[i - 1] == y[j - 1]:
                    D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i-1][j-1], D[i-2][j-2] + 1)
                else:
                    D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i-1][j-1] + 1, D[i-2][j-2] + 1)
            else:
                if x[i - 1] == y[j - 1]:
                    D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i-1][j-1])
                else:
                    D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i-1][j-1] + 1)
            if colMin > D[i,j]:
                colMin = D[i,j]
        if colMin > threshold:
            return None
    return D[lenX, lenY]


def damerau_intermediate_matriz(x, y, threshold=None):
    # completar versión Damerau-Levenstein intermedia con matriz
    return D[lenX, lenY]

def damerau_intermediate_edicion(x, y, threshold=None):
    # partiendo de matrix_intermediate_damerau añadir recuperar
    # secuencia de operaciones de edición
    # completar versión Damerau-Levenstein intermedia con matriz
    return 0,[] # COMPLETAR Y REEMPLAZAR ESTA PARTE
    
def damerau_intermediate(x, y, threshold=None):
    # versión con reducción coste espacial y parada por threshold
    return min(0,threshold+1) # COMPLETAR Y REEMPLAZAR ESTA PARTE

opcionesSpell = {
    'levenshtein_m': levenshtein_matriz,
    'levenshtein_r': levenshtein_reduccion,
    'levenshtein':   levenshtein,
    'levenshtein_o': levenshtein_cota_optimista,
    'damerau_rm':    damerau_restricted_matriz,
    'damerau_r':     damerau_restricted,
    'damerau_im':    damerau_intermediate_matriz,
    'damerau_i':     damerau_intermediate
}

opcionesEdicion = {
    'levenshtein': levenshtein_edicion,
    'damerau_r':   damerau_restricted_edicion,
    'damerau_i':   damerau_intermediate_edicion
}

