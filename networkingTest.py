import socket
import struct
from find_xp import find_xp

HOST: str
PORT: int

#NO_CMD Constant
NO_CMD: int = -999


if __name__ == '__main__':
    networking = find_xp()
    HOST = networking['ip']
    PORT = networking['port']

    print(networking)
    print(HOST)
    print(PORT)


