def esSeguro(tablero,fila,columna):
        N= len(tablero)

        for i in range(columna):
            if tablero[fila][i]=="R":
                       return False
    
        for  i in range(columna,N,1):
            if tablero[fila][i]=="R":
                      return False


        for f, c in zip(range(fila, -1,-1), range(columna,-1,-1)):
            if tablero[f][c]=="R":
                     return False


        for f, c in zip(range(fila, N,1), range(columna,-1, -1)):
            if tablero[f][c]=="R":
                      return False

        for f, c in zip(range(fila, -1,-1), range(columna,N,1)):
            if tablero[f][c]=="R":
                    return False

        for f, c in zip(range(fila, N,1), range(columna,N,1)):
            if tablero[f][c]=="R":
                     return False
            return True               
     
    
def iteraFilas(tablero,columna):
    N= len(tablero)
    if columna>=N:
        return True
    
    

    if columnaOcupada(tablero,columna):
        if  iteraFilas(tablero, columna + 1) ==True:
             return True
            

    for i in range(N):
        if esSeguro(tablero,i,columna):
            tablero[i][columna]="R"
            #Usamos el llamado recursivo
            if iteraFilas(tablero,columna+1)==True:
                return True
                
                
            tablero[i][columna]=0
        tablero[i][columna]=0 
               
       
    return False


def columnaOcupada(tablero,columna):
    N=len(tablero)
    for i in range(N):
        if tablero[i][columna]=="R":
            return True
            
    return False
       


def imprimirTablero(tablero):
    N=len(tablero)
    for i in range(N):
        for j in range(N):
                print(tablero[i][j],end = " ")
        print()        
      

            
def resolverNQueen(tablero):
    if iteraFilas(tablero,0)==False:
        print("No existe la solucion");
        imprimirTablero(tablero)
        return False
        
    print("Solucion exitosa")
    imprimirTablero(tablero)   
    return True              

def cargarCeros(N):
    Lista=[]
    for i in range(N):
        Lista.append(0)
    return Lista
    
    
print("-------------------------------Problema de las reinas---------------------------")
N=int(input("Escribe el tamaño del tablero"))
f=int(input("Dame la fila en logica cero:"))
c=int(input("Dame columna en logica cero:"))
tablero=[]
for i in range(N):
     tablero.append(cargarCeros(N))


tablero[f][c]="R"
resolverNQueen(tablero) 
