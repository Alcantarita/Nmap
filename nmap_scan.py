import nmap

def main():
    # Crearmos un escáner nmap
    scanner = nmap.PortScanner()
    
    # Solicitar los hosts
    hosts = input("Ingrese los hosts (e.g., 192.168.1.1 o 192.168.1.1/24): ")
    
    # Solicitar los puertos
    ports = input("Ingrese los puertos (e.g., 22,80,443 o 1-1024): ")
    
    # Solicitar los argumentos
    arguments = input("Ingrese los argumentos adicionales (e.g., -sS -O): ")
    
    # Solicitar superusuario
    super_user = input("¿Desea ejecutar el comando como superusuario? (s/n): ").lower()
    
    # Ejecutar el escaneo
    print("\nEjecutando escaneo...")
    if super_user == 's':
        scanner.scan(hosts=hosts, ports=ports, arguments=f"{arguments} -p {ports}", sudo=True)
    else:
        scanner.scan(hosts=hosts, ports=ports, arguments=f"{arguments} -p {ports}")
    
    # Imprimir resultados
    for host in scanner.all_hosts():
        print(f"Host: {host} ({scanner[host].hostname()})")
        print(f"Estado: {scanner[host].state()}")
        for protocol in scanner[host].all_protocols():
            print(f"Protocolo: {protocol}")
            ports = scanner[host][protocol].keys()
            for port in ports:
                print(f"Puerto: {port}\tEstado: {scanner[host][protocol][port]['state']}")
    
if __name__ == "__main__":
    main()
