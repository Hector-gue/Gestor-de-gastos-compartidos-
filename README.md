# Gestor-de-gastos-compartidos
Compartir gastos entre varias personas es bastante común, pagar una suscripción, una salida o un viaje entre familia o amigos y en muchas ocasiones algunas personas pagan diferentes cantidades en momentos diferentes. 
Este programa permite registrar los gastos de cada integrante, indicando quien y cuanto ha pagado y entre cuantos se divide, calcula cuanto le corresponde a cada persona y determina los balances. Al final, el usuario puede guardar el resumen de gastos y balances en un archivo de texto o desplegar todos los resultados guardados previamente.

#Algoritmo

Entradas
personas - cadena
gasto - numero_decimal
opción - numero_entero

Proceso
1.	INICIO
2.	DEFINIR gastos 
3.	PEDIR personas al usuario
4.	DEFINIR balances
4.1.	PARA CADA persona 
4.2.	balance = 0 
5.	MOSTRAR menú (1. Registrar gasto 2. Guardar/consultar historial 3. Salir)
6.	PEDIR opción
7.	MIENTRAS opción != 3
7.1.	SI opción = 1
7.1.1.	PEDIR quien_pagó, monto_total, participantes
7.1.2.	Dividir monto_total / cantidad_de_participantes
7.1.3.	GUARDAR en monto_individual
7.1.4.	PARA CADA persona 
7.1.4.1.	RESTAR balance(persona) - monto_individual
7.1.4.2.	GUARDAR en balance(persona)
7.1.5.	SUMAR balance(quien_pagó) + monto_total
7.1.6.	GUARDAR en balance(quien_pagó)
7.1.7.	AGREGAR gasto a gastos
7.2.	SI opción = 2
7.2.1.	MOSTRAR gastos
7.2.2.	GUARDAR o LEER gastos en archivo de texto
7.3.	MOSTRAR menú 
7.4.	PEDIR opción
8.	FIN

Salidas
balance – numero_decimal
archivo de texto

