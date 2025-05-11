#!/usr/bin/env python

import socket
import binascii

def main():
    # her sætter vi multicast ip og port
    # til at lytte på
    MCAST_GRP = '224.1.1.1'
    MCAST_PORT = 5007
    
    # opretter en socket til UDP multicast hvor vi bruger ipv4
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    
    # sætter socket option som gør det muligt at genebruge porten så den ikke fejler hvis den er i brug
    try:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except AttributeError:
        pass
    
    # sætter socket optioner for multicast
    # sætter TTL hvor lang tid pakken skal leve i netværket og loopback til 1
    # så vi kan se vores egen pakker
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)
    
    # lytter til alle interfaces på en port
    sock.bind(('', MCAST_PORT)) 
    
    # tilføjer multicast gruppe til socket så vi kan modtage pakker
    mreq = socket.inet_aton(MCAST_GRP) + socket.inet_aton('0.0.0.0')
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    # print for at debugge og se at vi lytter på den rigtige multicast gruppe og port
    print(f"Listening for multicast packets on {MCAST_GRP}:{MCAST_PORT}...")
    
    # modtager pakker som modtages i binary format så vi dekoder dem til string så vi kan læse indholdet
    while True:
        try:
            data, addr = sock.recvfrom(1024)
        except socket.error as e:
            print(f"Exception: {e}")
        else:
            print(f"Received packet from {addr}: {data.decode()}")
    
    sock.close()
    # lukker socket når vi er færdige med at lytte
    
    
if __name__ == '__main__':
    main()