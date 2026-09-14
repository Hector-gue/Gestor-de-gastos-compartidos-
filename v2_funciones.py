#Los comentarios de cada version se diferencian por el "x.0", 1 es la primera, 2 la segunda,...
#1.0 Me base en el ejemplo de la clase pasada para hacer el menu.
def mostrar_menu():
    print("1. - Registrar gasto") #1.0 Aqui despues pondre el "Guardar/consultar historial" y "Salir"
    opcion =(input("Ingrese una opción: "))
    return opcion

def calcular_monto_individual(monto_total, cantidad_de_participantes):
    monto_individual = monto_total / cantidad_de_participantes
    return monto_individual

def calcular_balance_persona(balance_persona, monto_individual):
    balance_persona = balance_persona - monto_individual
    return balance_persona

def calcular_balance_persona_que_pago(monto_total, monto_individual):
    balance_persona_que_pago = monto_total - monto_individual #1.0 No lo puedo acomodar a como lo puse en el algortimo, cambie sumar el balance_persona a monto_individual.
    return balance_persona_que_pago

def pedir_monto_total():
    return float(input("Ingrese el monto total del gasto: "))

def pedir_participantes():
    return int(input("Ingrese la cantidad de participantes: "))

def quien_pago():
    return input("Quién pago? ")

def acumular_gastos(total_gastado,cantidad_gastos,monto_total): #2.0 Actualmente el gasto acumulado siempre va a ser igual al monto total, espero poder cambiar eso en un futuro. 
    total_gastado = total_gastado + monto_total
    cantidad_gastos = cantidad_gastos + 1
    return total_gastado,cantidad_gastos

opcion = mostrar_menu()
if opcion == "1":
    monto_total = pedir_monto_total()
    cantidad_de_participantes = pedir_participantes()
    monto_individual = calcular_monto_individual(monto_total, cantidad_de_participantes)
    print("El monto individual es: ", monto_individual)
    balance_persona = 0 #1.0 Cuando se inicia, tiene que ser 0 para que cuando los demas participantes paguen, el balance de la persona que pago tambien llegue a 0.
    balance_persona_que_pago = calcular_balance_persona_que_pago(monto_total, monto_individual)
    print("El balance de la persona que pagó es: ", balance_persona_que_pago)
    balance_persona = calcular_balance_persona(balance_persona, monto_individual)
    print("El balance de los demas es: ", balance_persona)
    total_gastado = 0
    cantidad_gastos = 0
    total_gastado,cantidad_gastos = acumular_gastos(total_gastado,cantidad_gastos,monto_total)
    print("Gastos registrados hasta ahora: " ,cantidad_gastos)
    print("Gasto total acumulado: ",total_gastado)
