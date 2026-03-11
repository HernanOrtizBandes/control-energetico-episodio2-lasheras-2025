# Diccionario de watts por electrodoméstico

WATTS = {
    "televisor": 150,
    "microondas": 1200,
    "heladera": 200,
    "ventilador": 60,
    "pc": 500,
    "lavarropas": 500,
    "aire_acondicionado" : 1000,
    "licuadora" : 500,
    "notebook" : 90,
    "cargador_celular" : 5
}

def mostrar_menu():
    print("\n Holii, bienvenido a Energy Saver")
    print("\n ¿Qué deseas hacer?")
    print("1. Cargar electrodomésticos")
    print("2. Calcular el consumo energético diario de cada electrodoméstico")
    print("3. Calcular tu consumo energetico mensual y su tarifa -de cada electrodoméstico-")
    print("4. Calcular tu consumo energético total y tu tarifa total")
    print("5. Saber si estás en riesgo energético")
    print("6. Salir del programa")
    print("\n")

def cargar_electrodomestico():
    
    electrodomesticos = []
    while True:
    
        electrodomestico = {}

        electrodomestico["marca_electrodomestico"] = input("Marca: ")
        electrodomestico["tipo_electrodomestico"] = input("Tipo (televisor/microondas/heladera/etc.): ").lower()
        while True: 
            try:
                electrodomestico["hora_uso_diario"] = float(input("Horas de uso diario: "))
                break
            except ValueError:
                print("Error: debe ingresar un número válido. Intente nuevamente")
        
        while True: 
            try:
                electrodomestico["cantidad_dias_uso_semana"] = int(input("Días de uso por semana: "))
                break
            except ValueError:
                print("Error: debe ingresar un número válido. Intente nuevamente")

        
        tipo = electrodomestico["tipo_electrodomestico"]

        # Verifica si existe en las constantes
        if tipo not in WATTS:
            print("No tengo los watts de ese electrodoméstico.")
            return electrodomestico

        watts = WATTS[tipo]   # ← AQUÍ se obtiene el watt correspondiente ✔

         # Crear nueva key dinámica
        nueva_key = f"kwh_{tipo}"

        # Cálculo en kWh
        electrodomestico[nueva_key] = (electrodomestico["hora_uso_diario"] * watts) / 1000
        
        electrodomesticos.append(electrodomestico)
        print("Electrodoméstico cargado!")

        respuesta = input("Desea seguir cargando otro electrodoméstico? (s/n): ")
        
        if respuesta != "s":
            break

    return electrodomesticos

def mostrar_consumo_kWh(lista_electrodomesticos):
    
    print("========== LISTA DE ELECTRODOMÉSTICOS ==========")
    
    for v in lista_electrodomesticos: #este bucle for recorre la lista 'lista_electrodomestico' y nos muestra los valores de lo que llamamos por key
        print(f"Marca: {v['marca_electrodomestico']}")
        print(f"Tipo: {v['tipo_electrodomestico']}")
        print(f"Horas por día: {v['hora_uso_diario']}")
        print(f"Días por semana: {v['cantidad_dias_uso_semana']}")

        # Buscar la key kWh
        for key in v: #hacemos otro bucle for va a iterar para buscar las claves del diccionario que ahora se llama 'v'
            if key.startswith("kwh_"): # usamos un if para buscar con el indice 'key' y'startswith' de strings que devuelve un True si el texto empieza con lo que vos le  digas
                print(f"KWh diarios ({key}): {v[key]}")

        print("-----------------------------------------------") 

def consumo_kwh_mensual(lista_electrodomesticos):

    print("========== CONSUMO MENSUAL ESTIMADO ==========")

    for v in lista_electrodomesticos:

        # 1. Buscar la key que empieza con "kwh_" (kWh diarios)
        kwh_diario = None
        for key in v:
            if key.startswith("kwh_"):
                kwh_diario = v[key]   # ejemplo: v["kwh_heladera"]
                break

        # Si no se encontró key kwh_, pasar al siguiente
        if kwh_diario is None:
            print("No se encontró consumo kWh diario para este electrodoméstico.")
            continue

        dias_semana = v["cantidad_dias_uso_semana"]
        
        # 2. Cálculo mensual
        TARIFA_KWH =  219.60 # Precio por kWh
        consumo_mensual = kwh_diario * dias_semana * 4
        tarifa_mensual = consumo_mensual * TARIFA_KWH

        # 3. Mostrar datos
        print(f"Electrodoméstico: {v['marca_electrodomestico']} ({v['tipo_electrodomestico']})")
        print(f" - kWh diario: {kwh_diario}")
        print(f" - Días por semana: {dias_semana}")
        print(f" - Consumo mensual: {consumo_mensual} kWh")
        print(f" - Consumo mensual: ${tarifa_mensual:.2f}")
        print("-------------------------------------") 

def consumo_total_mensual(lista_electrodomesticos):

    TARIFA_KWH = 219.60   # Precio por kWh

    total_kwh_mensual = 0
    total_pesos_mensual = 0

    print("\n===== CONSUMO MENSUAL TOTAL DE TODOS LOS ELECTRODOMÉSTICOS =====")

    for v in lista_electrodomesticos:

        # Buscar el kWh diario (key dinámica)
        kwh_diario = None
        for key in v:
            if key.startswith("kwh_"):
                kwh_diario = v[key]
                break

        if kwh_diario is None:
            continue

        dias_semana = v["cantidad_dias_uso_semana"]

        # Cálculo mensual por electrodoméstico
        consumo_mensual = kwh_diario * dias_semana * 4
        costo_mensual = consumo_mensual * TARIFA_KWH

        # Acumulamos
        total_kwh_mensual += consumo_mensual
        total_pesos_mensual += costo_mensual

    # Mostrar totales con formato
    print(f"\nTotal mensual en kWh: {total_kwh_mensual:.2f} kWh")
    print(f"Total mensual estimado en pesos: ${total_pesos_mensual:.2f}")
    print("================================================================\n")

def riesgo_energetico(lista_electrodomesticos):
    total_kwh_mensual = 0
    
    print("\n===== CONSUMO MENSUAL kWh DE TODOS LOS ELECTRODOMÉSTICOS =====")

    for v in lista_electrodomesticos:

        # Buscar el kWh diario (key dinámica)
        kwh_diario = None
        for key in v:
            if key.startswith("kwh_"):
                kwh_diario = v[key]
                break

        if kwh_diario is None:
            continue

        dias_semana = v["cantidad_dias_uso_semana"]

        # Cálculo mensual por electrodoméstico
        consumo_mensual = kwh_diario * dias_semana * 4
        

        # Acumulamos
        total_kwh_mensual += consumo_mensual
        
    if total_kwh_mensual >= 400:
        print(f"\nTotal mensual en kWh: {total_kwh_mensual:.2f}. Su casa está en riesgo energético")
        print("Se recomienda desenchufar todos los electrodomésticos que no se usan continuamente")
        print("================================================================\n")
    else:
        print(f"\nTotal mensual en kWh: {total_kwh_mensual:.2f}. Su casa no está en riesgo energético")
        print("Se recomienda desenchufar todos los electrodomésticos que no se usan continuamente")
        print("================================================================\n")
        


def consumo_energetico():
    lista_electrodomesticos= []    # es una lista -está vacia-  

    while True:

        mostrar_menu()
        opcion = input("Por favor, elija una opción: ")

        if opcion == "1":
            lista_electrodomesticos.extend(cargar_electrodomestico())
        elif opcion == "2":
            
            mostrar_consumo_kWh(lista_electrodomesticos)
        elif opcion == "3":
            
            consumo_kwh_mensual(lista_electrodomesticos)
        elif opcion == "4":
            
            consumo_total_mensual(lista_electrodomesticos)
        elif opcion == "5":
            
            riesgo_energetico(lista_electrodomesticos)
        elif opcion == "6":
            print("Saliendo de la calculadora de consumo energético ¡Hasta luego!")
            break
        else:
            print("Por favor selecciones una opción válida (del 1 al 5)")

consumo_energetico()