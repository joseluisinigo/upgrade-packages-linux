# upgrade-packages-linux
script para de forma interactiva actualizar los paquetes que queramos

Este script realiza las siguientes acciones:

Actualiza el sistema mediante sudo apt update.
Muestra los paquetes upgradeables mediante sudo apt list --upgradable.
Permite al usuario seleccionar un paquete por su número de posición en el listado y lo upgradeará.
Vuelve a mostrar la lista de paquetes upgradeables y la opción "0" para salir del menú.
