import socket

#Constantes para la conexion
HOST = "irc.twitch.tv"
PORT = 6667
NICK = "bunno6661"
PASS = 'oauth:' #Sacar la PASS de https://twitchapps.com/tmi/

#Conexion a twitch
s = socket.socket()
s.connect((HOST, PORT))
#Los datos se envian a traves de bytes
s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
s.send(bytes("JOIN #" + NICK + " \r\n", "UTF-8"))

def send_message(message):
    s.send(bytes("PRIVMSG #" + NICK + " :" + message + "\r\n", "UTF-8"))

#Limpiar la basura del principio
while True:
    line = str(s.recv(1024))
    if "End of /NAMES list" in line:
        break

while True:
    #Leemos cada linea recibida
    for line in str(s.recv(1024)).split('\\r\\n'):
        parts = line.split(':')
        #Si la traza tiene menos de 3 elementos nos la quitamos del medio
        if len(parts) < 3:
            continue

        #print(parts)
        #Si no contiene ninguna de estas palabras en la primera posicion guardamos el mensaje
        #EJEMPLO DE LA TRAZA
        # ["b'", 'bunno6661!bunno6661@bunno6661.tmi.twitch.tv PRIVMSG #bunno6661 ', 'Hola']
        if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
            message = parts[2][:len(parts[2])]

        print(message)

        if message == "Hola":
            send_message("Acabas de decir hola")