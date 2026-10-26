#El programa es un gestor de gastos entre 2 o mas personas.
 
def mostrar_menu():
    #Muestra un menu que le permite al usuario elegir una opcion.
    print("\n1. - Registrar gasto")
    print("2. - Ver balances")
    print("3. - Ver historial de gastos")
    print("4. - Salir")
    opcion = input("Ingrese una opción: ")
    return opcion
 
def calcular_monto_individual(monto_total, cantidad_de_participantes):
    #Define cuanto le corresponde pagar a cada persona.
    monto_individual = monto_total / cantidad_de_participantes
    return monto_individual
 
def calcular_balance_persona(balance_persona, monto_individual):
    #Balance de una persona que NO hizo el pago inicial.
    balance_persona = balance_persona - monto_individual
    return balance_persona
 
def calcular_balance_persona_que_pago(balance_persona, monto_total, monto_individual):
    #Balance de la persona que hizo el pago inicial, tambien le toca su parte.
    balance_persona = balance_persona + monto_total - monto_individual
    return balance_persona
 
def pedir_monto_total():
    #Pregunta por la cantidad de dinero que pagaron.
    monto_total = float(input("Ingrese el monto total del gasto: "))
    while monto_total <= 0:
        print("El monto debe ser mayor a 0")
        monto_total = float(input("Ingrese el monto total del gasto: "))
    return monto_total
 
def pedir_participantes():
    #Pregunta cuantas personas participaron y guarda sus nombres en una lista.
    cantidad_de_participantes = int(input("Ingrese la cantidad de participantes: "))
    while cantidad_de_participantes < 2:
        print("La cantidad de personas debe ser de al menos 2")
        cantidad_de_participantes = int(input("Ingrese la cantidad de participantes: "))
 
    participantes = []
    while len(participantes) < cantidad_de_participantes:
        nombre = input("Nombre del participante " + str(len(participantes) + 1) + ": ")
        if nombre == "":
            print("El nombre no puede estar vacío")
        elif nombre in participantes:
            print("Ese nombre ya fue ingresado en este gasto")
        else:
            participantes.append(nombre)
    return participantes
 
def quien_pago(participantes):
    #Pide el nombre de quien pago; debe estar dentro de la lista de participantes.
    pagador = input("Quién pagó? ")
    while pagador not in participantes:
        print("Esa persona no está entre los participantes:", participantes)
        pagador = input("Quién pagó? ")
    return pagador
 
def obtener_indice_persona(personas, nombre):
    #Busca a la persona en la lista de nombres. Si es nueva, la agrega con balance 0.
    for i in range(len(personas)):
        if personas[i][0] == nombre:
            return i
    personas.append([nombre, 0])
    return len(personas) - 1
 

 
def actualizar_balances(personas, participantes, pagador, monto_total, monto_individual):
    #Recorre a los participantes y actualiza el balance de cada uno en la lista.
    for persona in participantes:
        i = obtener_indice_persona(personas, persona)
        if persona == pagador:
            personas[i][1] = calcular_balance_persona_que_pago(personas[i][1], monto_total, monto_individual)
        else:
            personas[i][1] = calcular_balance_persona(personas[i][1], monto_individual)
 
def acumular_gastos(montos_gastos, pagadores_gastos, participantes_gastos, monto_total, pagador, participantes):
    #Guarda el gasto en las listas del historial.
    montos_gastos.append(monto_total)
    pagadores_gastos.append(pagador)
    participantes_gastos.append(participantes)
 
def redondear_a_2_decimales(valor):
    #Deja el numero con 2 decimales.
    return int(valor * 100 + 0.5) / 100
 
def mostrar_balances(personas):
    #Muestra el balance de cada persona registrada.
    if len(personas) == 0:
        print("Todavía no hay personas registradas.")
        return
    print("\n--- Balances ---")
    for nombre, balance in personas:
        if balance > 0:
            print(nombre, ": le deben $", redondear_a_2_decimales(balance))
        elif balance < 0:
            print(nombre, ": debe $", redondear_a_2_decimales(-balance))
        else:
            print(nombre, ": está a mano")
 
def mostrar_historial(montos_gastos, pagadores_gastos, participantes_gastos):
    #Muestra todos los gastos registrados.
    if len(montos_gastos) == 0:
        print("Todavía no hay gastos registrados.")
        return
    print("\n--- Historial de gastos ---")
    for i in range(len(montos_gastos)):
        print("Gasto", i + 1, "- Pagó:", pagadores_gastos[i], "- Monto: $", montos_gastos[i])
        print("Participantes: ", participantes_gastos[i])
        for persona in participantes_gastos[i]:
            print("   -", persona)
    print("Cantidad de gastos:", len(montos_gastos))
    print("Gasto total acumulado: $", sum(montos_gastos))
 
 
#Listas del programa (se mantienen "paralelas": misma posicion = misma persona / mismo gasto)
personas = []
montos_gastos = []      #monto de cada gasto registrado
pagadores_gastos = []   #quien pago cada gasto
participantes_gastos = [] #es la lista de los participantes del gasto i 
 
salir = False
 
while not salir:
    opcion = mostrar_menu()
 
    if opcion == "1":
        monto_total = pedir_monto_total()
        participantes = pedir_participantes()
        pagador = quien_pago(participantes)
        monto_individual = calcular_monto_individual(monto_total, len(participantes))
        print("El monto individual es: ", redondear_a_2_decimales(monto_individual))
        actualizar_balances(personas, participantes, pagador, monto_total, monto_individual)
        acumular_gastos(montos_gastos, pagadores_gastos,participantes_gastos, monto_total, pagador, participantes)
        print("Gasto registrado correctamente.")
 
    elif opcion == "2":
        mostrar_balances(personas)
 
    elif opcion == "3":
        mostrar_historial(montos_gastos, pagadores_gastos, participantes_gastos)
 
    elif opcion == "4":
        salir = True
        print("Saliendo del programa")
 
    else:
        print("Opcion no valida, intente de nuevo")
