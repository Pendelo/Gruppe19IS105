import random

from socket import*

returnText = b" - Mottatt"
# Lager en  UDP socket
# Legger til bruken av SOCK_DGRAM for UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Tildeler IP adresse og port nummer til socket
serverSocket.bind(("", 10000))
print("Started UDP server on port 10000")
while True:     

    # Genererer et tilfeldig nummer mellom 0 og 10
    rand = random.randint(0, 9)

    # Mottar pakke fra klienten sammen med adressen den kommer fra
    message, address =serverSocket.recvfrom(1024)

    # Legger til "Mottatt" fra meldingen mottatt fra klienten
    message = message+ returnText

    # Hvis "rand" er mindre enn 4 vil vi anta at pakken er tapt og vil ikke respondere
    if rand < 4:

        continue

    # Hvis "rand" ikke er mindre enn 4 vil serveren respondere normalt
    serverSocket.sendto(message, address)