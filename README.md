<!-- Upgrade Packages Linux v1.0 -->

# Upgrade Packages Linux

Este script en Python facilita la actualización de paquetes en sistemas basados en Linux. Proporciona una interfaz de línea de comandos interactiva para actualizar el sistema y los paquetes instalados.

## Información del Creador

- **Creador:** José Luis Iñigo (A.K.A. Riskoo)
- **Web Profesional:** [Diseño Web en Sevilla](https://diseñowebensevilla.org)
- **Web Curriculum:** [José Luis Iñigo - Curriculum](https://joseluisinigo.work)

## Modos de Instalación

### Clonación de Git

1. Abre la terminal en tu sistema Linux.
2. Ejecuta el siguiente comando para clonar el repositorio:

    ```bash
    git clone https://github.com/joseluisinigo/upgrade-packages-linux.git
    ```

3. Cambia al directorio recién creado:

    ```bash
    cd upgrade-packages-linux
    ```

4. Ejecuta el script Python:

    ```bash
    python3 upgrade_packages.py
    ```

## Opciones del Script

El script ofrece las siguientes opciones:

1. **Actualizar sistema:** Realiza un `sudo apt update` para actualizar la lista de paquetes disponibles.
2. **Upgradear sistema:** Ejecuta `sudo apt upgrade` para upgradear el sistema completo.
3. **Listar paquetes upgradeables:** Muestra los paquetes que pueden ser actualizados con `sudo apt list --upgradable`.
4. **Upgradear paquete:** Permite seleccionar un paquete de la lista de paquetes upgradeables y lo upgradeará.

Para salir del programa, selecciona la opción "0".

---

<!-- Upgrade Packages Linux v1.0 -->

# Upgrade Packages Linux

This Python script simplifies the package update process on Linux-based systems. It provides an interactive command-line interface for updating the system and installed packages.

## Creator Information

- **Creator:** José Luis Iñigo (A.K.A. Riskoo)
- **Professional Website:** [Web Design in Seville](https://diseñowebensevilla.org)
- **Curriculum Website:** [José Luis Iñigo - Curriculum](https://joseluisinigo.work)

## Installation Methods

### Git Clone

1. Open the terminal on your Linux system.
2. Run the following command to clone the repository:

    ```bash
    git clone https://github.com/joseluisinigo/upgrade-packages-linux.git
    ```

3. Change to the newly created directory:

    ```bash
    cd upgrade-packages-linux
    ```

4. Run the Python script:

    ```bash
    python3 upgrade_packages.py
    ```

## Script Options

The script offers the following options:

1. **Update system:** Performs `sudo apt update` to refresh the list of available packages.
2. **Upgrade system:** Executes `sudo apt upgrade` to upgrade the entire system.
3. **List upgradeable packages:** Displays packages that can be updated using `sudo apt list --upgradable`.
4. **Upgrade package:** Allows selecting a package from the list of upgradeable packages and upgrades it.

To exit the program, select option "0".
