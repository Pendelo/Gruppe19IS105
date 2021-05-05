import time

from socket import *
serverName = "localhost"
serverPort = 10000
sentence = B"Ping"
counter = 0

while counter <10:

    # Increment teller
    counter += 1
    # Lager en socket og spesifiserer at den bruker IPv4 og UDP.
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1.0)
    clientSocket.sendto(sentence,(serverName, serverPort))
    t1_start = time.perf_counter()
    try:
        modifiedSentence = clientSocket.recv(1024)
        print("Fra Server:", modifiedSentence.decode(), "forespørsel:", counter)
        t1_stop = time.perf_counter()
        print("Gjennomgang tid:", "Start:", t1_start, 's', ":", "Stopp:", t1_stop, 's')
        # Omgjør resultatet fra sekunder til millisekunder
        millitid = (t1_stop-t1_start)*1000
        print (f"Det tok: {millitid}", 'ms', "for å fullføre kretsen")
        print ("----------------------------------------")

    except timeout:
        if counter<=9:
            print("Ping utgikk på forespørsel", counter)
            print("Prøver igjen på neste forespørsel", counter+1)
            print ("----------------------------------------")
        else:
            #Gjør slik at den ikke forteller at den vil prøve igjen hvis den er på siste forespørsel
            print("Ping utgikk på forespørsel", counter)
            print("----------------------------------------")



clientSocket.close()