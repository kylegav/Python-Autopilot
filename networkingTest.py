import socket
import struct
from find_xp import find_xp

HOST: str = '192.168.0.1'
PORT: int = 49004

#NO_CMD Constant
NO_CMD: int = -999


if __name__ == '__main__':
    networking = find_xp()
    print(networking)


