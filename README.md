# Nmap Script
Aldo Alcantara Martinez 

#Descripción
Este es un script en Python que utiliza la biblioteca `python-nmap` para realizar escaneos de red utilizando `nmap`. El usuario puede especificar los hosts, puertos, argumentos adicionales y si desea ejecutar el comando como superusuario.

#Requisitos
- Python 3.x
- `python-nmap`

#Instalación
Para instalar las dependencias necesarias, ejecuta los siguientes comandos:
pip install python-nmap

#Ejecución
Para ejecutar el script, guarda el código .py y ejecuta el siguiente comando en tu terminal:
python "Nombre".py

El script te pedirá ingresar la siguiente información:
Hosts: Las direcciones IP o rangos de IPs que deseas escanear (e.g., 192.168.1.1 o 192.168.1.1/24).
Puertos: Los puertos que deseas escanear (e.g., 22,80,443 o 1-1024).
Argumentos adicionales: Cualquier argumento adicional de nmap que desees incluir (e.g., -sS -O).
Superusuario: Si deseas ejecutar el comando como superusuario (e.g., s para sí, n para no).

El script ejecutará el escaneo y mostrará los resultados.
