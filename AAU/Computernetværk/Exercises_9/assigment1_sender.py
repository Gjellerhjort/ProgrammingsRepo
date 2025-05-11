import socket

def main():
    # her sætter vi multicast ip og port
    MCAST_GRP = '224.1.1.1'
    MCAST_PORT = 5007
    # opretter en socket til UDP multicast hvor vi bruger ipv4
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    # sætter socket option som gør det muligt at genebruge porten så den ikke fejler hvis den er i brug da det er træls
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    # sætter socket optioner for multicast og sender en besked til multicast gruppen
    sock.sendto('Hello, World!'.encode(), (MCAST_GRP, MCAST_PORT))
    # lukker socket når vi er færdige med at sende
    sock.close()
    
if __name__ == '__main__':
    main()