#Me base en el ejemplo de la clase pasada para hacer el menu.
def mostrar_menu():
    print("1. - Registrar gasto") #Aqui despues pondre el "Guardar/consultar historial" y "Salir"
    opcion =(input("Ingrese una opción: "))
    return opcion

def calcular_monto_individual(monto_total, cantidad_de_participantes):
    monto_individual = monto_total / cantidad_de_participantes
    return monto_individual

def calcular_balance_persona(balance_persona, monto_individual):
    balance_persona = balance_persona - monto_individual
    return balance_persona
def calcular_balance_persona_que_pago(monto_total, monto_individual):
    balance_persona_que_pago = monto_total - monto_individual #No lo puedo acomodar a como lo puse en el algortimo, cambie sumar el balance_persona a monto_individual.
    return balance_persona_que_pago

opcion = mostrar_menu()
if opcion == "1":
    monto_total = float(input("Ingrese el monto total del gasto: "))
    cantidad_de_participantes = int(input("Ingrese la cantidad de participantes: "))
    monto_individual = calcular_monto_individual(monto_total, cantidad_de_participantes)
    print("El monto individual es: ", monto_individual)
    balance_persona = 0 #Cuando se inicia, tiene que ser 0 para que cuando los demas participantes paguen, el balance de la persona que pago tambien llegue a 0.
    balance_persona_que_pago = calcular_balance_persona_que_pago(monto_total, monto_individual)
    print("El balance de la persona que pagó es: ", balance_persona_que_pago)
    balance_persona = calcular_balance_persona(balance_persona, monto_individual)
    print("El balance de los demas es: ", balance_persona)


