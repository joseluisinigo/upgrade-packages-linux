import os

def actualizar_sistema():
    os.system("sudo apt update")

def listar_upgradeables():
    os.system("sudo apt list --upgradable")

def upgradear_paquete(paquete):
    os.system(f"sudo apt upgrade {paquete}")

def main():
    while True:
        print("\n1. Actualizar sistema")
        print("2. Listar paquetes upgradeables")
        print("3. Upgradear paquete")
        print("0. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            actualizar_sistema()
        elif opcion == "2":
            os.system("sudo apt list --upgradable")
        elif opcion == "3":
            paquetes = os.popen("apt list --upgradable").readlines()[1:]
            
            if not paquetes:
                print("No hay paquetes upgradeables.")
                continue

            print("\nPaquetes upgradeables:")
            for i, linea in enumerate(paquetes, start=1):
                print(f"{i}. {linea.strip()}")

            paquete_numero = input("\nSelecciona el número del paquete a upgradear (0 para salir): ")

            if paquete_numero == "0":
                continue

            try:
                paquete_numero = int(paquete_numero)
                paquete_seleccionado = paquetes[paquete_numero - 1].split()[0]
                upgradear_paquete(paquete_seleccionado)
                print(f"Paquete {paquete_seleccionado} upgradedo exitosamente.")
            except (ValueError, IndexError):
                print("Opción no válida. Introduce un número válido.")
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Introduce un número válido.")

if __name__ == "__main__":
    main()
