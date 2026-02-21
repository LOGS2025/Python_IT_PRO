
# Bloque A - Condicionales básicos (if / else)

    # 1 MAYOR DE EDAD
def ageApproval(age : int):
    return "Menor de edad" if age<18 else "Mayor de edad"

    # 2 PAR O IMPAR
def evenCheck(number : int):
    return "Par" if number//2==0 else "Impar"

    # 3 POSITIVO, NEGATIVO O CERO
def signCheck(number : float):
        # 2 OPERADORES TERNRARIOS COMBINADOS
    return "Positivo" if number>0 else "Cero" if number==0 else "Negativo"

    # 4 DISCOUNT 
def discountCheck(total : float):
    print(f"Salida : {total-total*0.1 if total>=1000.0 else total}")

# Bloque B - Decisiones múltiples (elif)

    # 5 CALIFICACION CON LETRA
def gradeABC(calificacion : int):
    if calificacion in range(6):
        print('F')
        return
    else:
        match calificacion:
            case 6:
                print('D')
            case 7:
                print('C')
            case 8:
                print('B')
            case 9 | 10:
                print('A')

    # 6 TIPO DE TRIÁNGULO
def triangleID(a : float, b : float, c : float):
    # Se aplica el teorema de inequidad 
    if a+b<c or a+c<b or b+c<a: 
        print("Triángulo imposible")
        return
    elif a == b == c :
        print("Equilátero")
        return
    elif a == b or a == c or b == c :
        print("Isósceles")
        return
    else :
        print("Escaleno")

    # 7 CAJERO SIMPLE
    # 1) Consultar saldo 2) Depositar 3) Retirar
def forceNumber(var, errString, flag, rango):
    while var is None:
        try:
            var = int(input())
        except ValueError:
            print(errString)
            var = None
        if flag!=0 and var != None and var-1 not in range(rango):           
            print(errString)
            var = None
    return var

def cashMachine(initial : float):
    print(f"\n---------------------------\n\tElija una opción:\n\n1) Consultar saldo \n2) Depositar \n3) Retirar")    
    opcion = None
    opcion = forceNumber(opcion, "Elija una de las opciones",1,3)
    match opcion :
        case 1 :
            output = print(f"Su saldo es {initial}")
        case 2 :
            output = None
            print("¿Cuánto va a depositar?")
            output = forceNumber(output,"Coloque una cifra",0,0)
        case 3 :
            output = None
            print("¿Cuánto va a retirar?")
            output = int(forceNumber(output,"Coloque una cifra",0,0))
            if output > initial:
                output = forceNumber(output,"Cifra incorrecta",1,initial)
            else:
                return

#cashMachine(1)


# Bloque C - Lógica (and/or/not) y comparaciones
    # 8 ACCESO CON DOBLE CONDICIÓN
def access():
    age = int(input("Ingrese su edad : "))
    hasID = input("¿Tiene credencial? (S/N) : ")
    
    if age>=18 and hasID.lower() == 's':
        print("Acceso permitido")
    else:
        print("Acceso denegado")

    # 9 RANGO CON COMPARACIÓN ENCADENADA
def rangeCheck(number : float):
    if number >=0:
        if number <= 100:
            print("Dentro del rango")
        else:
            print("Fuera del rango")
    else:
        print("Fuera del rango")

    # 10 USUARIO Y CONTRASEÑA
def uses_pswd():
    