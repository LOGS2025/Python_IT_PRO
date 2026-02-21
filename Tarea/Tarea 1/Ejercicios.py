
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
    user = input()
    pswd = input()
    if user == "Admin" and pswd == "1234":
        print("Acceso")
    else: 
        print("Acceso denegado")

# Bloque D - Pertenencia (in / not in)
    # 11 VOCAL O CONSONANTE
def letterCheck():
    letter = input().lower()
    if letter in ['a','e','i','o','u']:
        print("Es vocal")
    else: 
        print("Es consonante")

    # 12 LISTA DE INVITADOS
def partyGuests():
    invitados = ["ana","luis","paco"]
    name = input().lower()

    if name in invitados:
        print("Invitado")
    else : 
        print("No invitado")

# Bloque E - While (y do-while simulado)
    # 13 Contador con while
def counter():
    i = 0
    while i < 10:
        i = i+1
        print(i)

    # 14 Suma acumulada
def accSum():
    sum = 0
    while True:
        number = int(input())
        sum = sum + number
        if number == 0:
            break
    print(sum)

    # 15 Adivina el número
def guessingNumber():
    num = 7
    guess = 0
    while guess != num:
        guess = int(input())
        if abs(guess - num) < 10 and guess != num:
            print("Muy alto")
        elif abs(guess - num) < 30 and guess != num:
            print("Muy bajo")
    print("Correcto")

    # 16  Do-while simulado: menú que se repite
def menu():
    # Opciones
    print("1) Saludar\n2) Mostrar tabla del 5\n3) Salir")
    while True:
        choice = int(input())
        if choice == 3:
            break
        match choice:
            case 1:
                print("Hola")
                break
            case 2:
                for _ in range(10):
                    print("Tabla del 5 : " + str((_+1)*5))
                break
        
# Bloque F - For, range y enumerate
    # 17 Tabla de multiplicar
def multiplicationTable():
    num =int(input())
    for _ in range(10):
        print("Tabla de multiplicar : " + str((_+1)*num))

    # 18 Suma de pares
def pairSum():
    num =int(input())
    sum = 0
    for _ in range(2,num+1,2):
        sum = sum + _
        print("Suma de pares : " + str(sum))

    # 19 Enumerar caracteres
def textEnumeration():
    string = input()
    for _ in enumerate(string):
        print(_)

    # 20 Promedio de calificaciones
def avgGrades():
    iterTimes = int(input())
    grades = []
    for _ in range(iterTimes):
        grades.append(int(input()))
    sum = 0
    for _ in grades:
        sum = sum + _
    print(sum)

# Bloque G - break y continue (+ for-else)
    # 21 Contraseña con 3 intentos (while + break)
def paswdTry3():
    tries = 0
    while tries < 3:
        tries = tries +1
        paswdInput = input()
        if paswdInput == '1234':
            print("Acceso")
            return
    print("Bloqueado")
    return

    # 22 Saltar múltiplos de 3 (continue)
def skipNum():
    for _ in range(1,31,1):
        if _%3!=0:
            print( _ )
            continue
        else:
            continue


skipNum()

    # 23 Buscar elemento (for-else)
def search():
    nums = [4,8,15,16,23,42]
    lookFor=input()
    for _ in range(len(nums)):
        if lookFor==_:
            print("Encontrado")
            break
    else:
        print("No encontrado")
