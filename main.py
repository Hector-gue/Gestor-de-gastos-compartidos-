#El programa es un gestor de gastos entre 2 o mas personas. 
def mostrar_menu():
    #Muestra un menu que le permite al usuario elegir al usuario
    print("1. - Registrar gasto") 
    print("2. - Salir") 
    opcion =(input("Ingrese una opción: "))
    return opcion

def calcular_monto_individual(monto_total, cantidad_de_participantes):
    #Define cuanto le corresponde pagar a cada persona, divide el monto total entre la cantidad de personas que hicieron el gasto.
    monto_individual = monto_total / cantidad_de_participantes
    return monto_individual

def calcular_balance_persona(balance_persona, monto_individual):
    #Es el balance que tiene una persona que no hizo el pago inicial, el balance de cada persona es 0 al iniciar.
    balance_persona = balance_persona - monto_individual
    return balance_persona

def calcular_balance_persona_que_pago(monto_total, monto_individual):
    #Es el balance que tiene la persona que hizo el gasto inicial. 
    balance_persona_que_pago = monto_total - monto_individual
    return balance_persona_que_pago

def pedir_monto_total():
    #Pregunta por la cantidad de dinero que pagaron.
    return float(input("Ingrese el monto total del gasto: "))

def pedir_participantes():
    #Pregunta por cuantas personas estuvieron involucradas en el gasto.
    return int(input("Ingrese la cantidad de participantes: "))

def quien_pago(): #Despues agregare una lista para asignar los balances a cada persona en especifico.
    #Pide que se escriba el nombre de quien pago.
    return input("Quién pago? ")

def acumular_gastos(total_gastado,cantidad_gastos,monto_total):
    #Suma los gastos y los muestra.
    total_gastado = total_gastado + monto_total
    cantidad_gastos = cantidad_gastos + 1
    return total_gastado,cantidad_gastos

salir = False
total_gastado = 0
cantidad_gastos = 0
balance_persona = 0

while not salir:
    opcion = mostrar_menu()

    if opcion == "1":
        monto_total = pedir_monto_total()
        cantidad_de_participantes = pedir_participantes()
        monto_individual = calcular_monto_individual(monto_total, cantidad_de_participantes)
        print("El monto individual es: ", monto_individual)
        balance_persona_que_pago = calcular_balance_persona_que_pago(monto_total, monto_individual)
        print("El balance de la persona que pagó es: ", balance_persona_que_pago)
        balance_persona = calcular_balance_persona(balance_persona, monto_individual)
        print("El balance de los demas es: ", balance_persona)
        total_gastado,cantidad_gastos = acumular_gastos(total_gastado,cantidad_gastos,monto_total)
        print("Gastos registrados hasta ahora: " ,cantidad_gastos)
        print("Gasto total acumulado: ",total_gastado)

    elif opcion == "2":
        salir = True
        print("Saliendo del programa")
    else:
        print("Opcion no valida, intente de nuevo")


