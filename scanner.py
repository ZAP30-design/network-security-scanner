import socket
import sys
from datetime import datetime

# Funkcja skanująca pojedynczy port
def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) # Czekamy pół sekundy
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return True
        else:
            return False
    except socket.gaierror:
        print(f"Nie mogę znaleźć hosta: {host}")
        return False
    except Exception as e:
        return False

# Główna funkcja zarządzająca skanowaniem
def scan_network(host):
    # Lista najważniejszych portów do sprawdzenia
    # 22=SSH, 80=Web, 443=SecureWeb, 3306=MySQL, 8080=AltWeb
    ports = [22, 23, 80, 443, 445, 3306, 8080]
    
    print("-" * 50)
    print(f"Skanowanie celu: {host}")
    print(f"Czas rozpoczęcia: {datetime.now()}")
    print("-" * 50)
    
    open_ports = []
    
    for port in ports:
        # Informacja dla użytkownika, że coś się dzieje
        print(f"Sprawdzam port {port}...") 
        
        if scan_port(host, port):
            print(f">>> PORT {port}: OTWARTY! <<<")
            open_ports.append(port)
        else:
            # Możesz odkomentować linię niżej, jeśli chcesz widzieć zamknięte
            # print(f"Port {port}: zamknięty")
            pass

    print("-" * 50)
    print(f"Znalezione otwarte porty: {open_ports}")
    print(f"Czas zakończenia: {datetime.now()}")
    print("-" * 50)

if __name__ == "__main__":
    # Sprawdzamy, czy użytkownik podał cel w terminalu
    if len(sys.argv) > 1:
        target_host = sys.argv[1]
        scan_network(target_host)
    else:
        print("BŁĄD: Nie podałeś celu!")
        print("Użycie: python3 scaner.py <adres_strony>")
        print("Przykład: python3 scaner.py google.com")
