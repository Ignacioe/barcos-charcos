def inicializarMapa(n):
    elem = ["_"]
    fila = elem * n
    tablero = [fila] * n
    return tablero

def imprimirMapa(tablero,n):
    k=0
    cadena="\t "
    while(k<n):
        cadena+="  "+str(k+1)+"   "
        k+=1
    print("\n"+ cadena )
    print ("\t"+"_"*n*6 + "_")
    i=0
    while (i<n):
        fila = tablero[i]

        print ("\t|"+"     |"*n)
        j=0
        cadena=str(i+1)+"\t|"
        while(j<n):
            cadena+= "  "+str(fila[j])+"  |"
            j+=1
        print(cadena)
        print ("\t|"+"_____|"*n)
        i+=1

def juego(tablero1, tablero2, turno, tamano):
    return 0

def ingresar(tamano):
    direccion = ""
    band1=False
    band2=False
    while (direccion != "v" and direccion != "h"):
        direccion=(input("Ingrese 'v' para colocar el barco vertical, o 'h' para colocarlo horizontal: ")).lower()
    while (band1==False):
        posx=input("Ingrese la fila: ")
        if(posx.isnumeric()):
            posx=int(posx)-1
            if(posx<=tamano):
                band1=True
    while (band2==False):
        posy=input("Ingrese la columna: ")
        if(posy.isnumeric()):
            posy=int(posy)-1
            if(posy<=tamano):
                band2=True
    if(direccion=="v"):
        direccion=True
    else:
        direccion=False
    return(direccion, posx, posy)

def ponerBarcos(tamano, barcos, tablero):
    largoBarco=1
    for largo in barcos:
        while largo > 0:
            imprimirMapa(tablero,tamano)
            ingreso=ingresar(tamano)
            tablero=ponerBarco(tablero, tamano, largoBarco, ingreso)
            largo -= 1
        largoBarco+=1
    return tablero  

def chequeoV(tablero, tamano, largoBarco, ingreso):
    posiciones = []
    i = ingreso[1]
    bandera = True
    while(i<largoBarco+ingreso[1] and bandera):
        if(tablero[i][ingreso[2]] == "X"):
            bandera = False
        i += 1
    return bandera

def chequeoH(tablero, tamano, largoBarco, ingreso):
    posiciones = []
    i = ingreso[2]
    bandera = True
    while(i<largoBarco+ingreso[2] and bandera):
        if(tablero[ingreso[1]][i] == "X"):
            bandera = False
        i += 1
    return bandera

def ponerBarco(tablero, tamano, largoBarco, ingreso):
    posibles=["w","a","s","d","e","c"]
    tableroTemporal = []
    for columna in tablero:
        columnaTemporal=columna[:]
        tableroTemporal+=[columnaTemporal]
    if(ingreso[0]):
        i = ingreso[1]
        if(largoBarco<=tamano-ingreso[1]):
            while (i<largoBarco+ingreso[1]):
                tableroTemporal[i][ingreso[2]] = "#"
                i+=1
            imprimirMapa(tableroTemporal, tamano)
            print("X = Barcos \t\t # = Barco Actual \t _ = Agua")
            accion = ""
            while (not (accion in posibles)):
                accion = input("WASD = Mover Barco \t C = Colocar Barco \t E = Cancelar Direccion/Posicion\n").lower()
            if(accion=="e"):
                ingreso = ingresar(tamano)
                return ponerBarco(tablero, tamano, largoBarco, ingreso)
            elif(accion == "d"):
                if(ingreso[2] == tamano - 1):
                    return ponerBarco(tablero, tamano, largoBarco, ingreso)
                else:
                    retorno = (ingreso[0],ingreso[1],ingreso[2]+1)
                    return ponerBarco(tablero, tamano, largoBarco, retorno)
            elif(accion == "a"):
                if(ingreso[2] == 0):
                    return ponerBarco(tablero, tamano, largoBarco, ingreso)
                else:
                    retorno = (ingreso[0],ingreso[1],ingreso[2]-1)
                    return ponerBarco(tablero, tamano, largoBarco, retorno)
            elif(accion == "s"):
                if(ingreso[1] + largoBarco == tamano):
                    return ponerBarco(tablero, tamano, largoBarco, ingreso)
                else:
                    retorno = (ingreso[0],ingreso[1]+1,ingreso[2])
                    return ponerBarco(tablero, tamano, largoBarco, retorno)
            elif(accion == "w"):
                if(ingreso[1] == 0):
                    return ponerBarco(tablero, tamano, largoBarco, ingreso)
                else:
                    retorno = (ingreso[0],ingreso[1]-1,ingreso[2])
                    return ponerBarco(tablero, tamano, largoBarco, retorno)
            elif(accion == "c"):
                if(chequeoV(tablero, tamano, largoBarco, ingreso)):
                    i = ingreso[1]
                    while (i<largoBarco+ingreso[1]):
                        if(tableroTemporal[i][ingreso[2]] == "#"):
                            tableroTemporal[i][ingreso[2]] = "X"
                        i+=1
                else:
                    return ponerBarco(tablero, tamano, largoBarco, ingreso)
        else:
            retorno = (ingreso[0],ingreso[1]-1,ingreso[2])
            return ponerBarco(tablero, tamano, largoBarco, retorno)
    else:
        i = ingreso[2]
        if(largoBarco<=tamano-ingreso[2]):
            while (i<largoBarco+ingreso[2]):
                tableroTemporal[ingreso[1]][i] = "#"
                i+=1
            imprimirMapa(tableroTemporal, tamano)
            print("X = Barcos \t\t # = Barco Actual \t _ = Agua")
            accion = ""
            while (not (accion in posibles)):
                accion = input("WASD = Mover Barco \t C = Colocar Barco \t E = Cancelar Direccion/Posicion\n").lower()
            if(accion=="e"):
                ingreso = ingresar()
                return ponerBarco(tablero, tamano, largoBarco, ingreso)
            elif(accion == "d"):
                if(ingreso[2] + largoBarco == tamano):
                    return ponerBarco(tablero, tamano, largoBarco, ingreso)
                else:
                    retorno = (ingreso[0],ingreso[1],ingreso[2]+1)
                    return ponerBarco(tablero, tamano, largoBarco, retorno)
            elif(accion == "a"):
                if(ingreso[2] == 0):
                    return ponerBarco(tablero, tamano, largoBarco, ingreso)
                else:
                    retorno = (ingreso[0],ingreso[1],ingreso[2]-1)
                    return ponerBarco(tablero, tamano, largoBarco, retorno)
            elif(accion == "s"):
                if(ingreso[1] == tamano - 1):
                    return ponerBarco(tablero, tamano, largoBarco, ingreso)
                else:
                    retorno = (ingreso[0],ingreso[1]+1,ingreso[2])
                    return ponerBarco(tablero, tamano, largoBarco, retorno)
            elif(accion == "w"):
                if(ingreso[1] == 0):
                    return ponerBarco(tablero, tamano, largoBarco, ingreso)
                else:
                    retorno = (ingreso[0],ingreso[1]-1,ingreso[2])
                    return ponerBarco(tablero, tamano, largoBarco, retorno)
            elif(accion == "c"):
                if(chequeoH(tablero, tamano, largoBarco, ingreso)):
                    i = ingreso[2]
                    while (i<largoBarco+ingreso[2]):
                        if(tableroTemporal[ingreso[1]][i] == "#"):
                            tableroTemporal[ingreso[1]][i] = "X"
                        i+=1
                    bandera= False
                else:
                    return ponerBarco(tablero, tamano, largoBarco, ingreso)
        else:
            retorno = (ingreso[0],ingreso[1],ingreso[2]-1)
            return ponerBarco(tablero, tamano, largoBarco, retorno)
    return tableroTemporal

if __name__ == "__main__":
    vale = False
    while not vale:
        tamano = input("Ingrese el tamano del tablero: ")
        if(tamano.isnumeric()):
            vale = True
            tamano = int(tamano)
    barcos = []
    for largo in range(1, tamano + 1):
        barcos += [int(input("Cantidad de barcos de tamano " + str(largo) + ": "))]
    tableroPlayer1 = inicializarMapa(tamano)
    tableroPlayer2 = inicializarMapa(tamano)
    turno = False
    tableroplayer1 = ponerBarcos(tamano, barcos, tableroPlayer1)
    imprimirMapa(tableroplayer1,tamano)
    tableroplayer2 = ponerBarcos(tamano, barcos, tableroPlayer2)
    imprimirMapa(tableroplayer2,tamano)
    #juego(tableroplayer1, tableroplayer2, turno, tamano)
        
    
