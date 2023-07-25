import subprocess
import platform

def ping(address):
    # Vérifie l'OS pour utiliser la bonne commande de ping
    if platform.system().lower() == "windows":
        command = ["ping", "-n", "1", address]
    else: 
        command = ["ping","-c","1", address]

    try:
        # Exécute la commande de ping et récupère la sortie
        output = subprocess.check_output(command, universal_newlines=True)

        # Analyse la sortie pour vérifier l'état de la connectivité
        if "TTL=" in output:
            return f"{address} est en ligne."
        else:
            return f"{address} est hors ligne."
        
    except subprocess.CalledProcessError:
        return f"{address} est hors ligne."
    

if __name__ == "__main__":
    addresses = ["google.com", "facebook.com", "ajouter.."]

    for address in addresses:
        print(ping(address))