from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from prime_numbers import prime_number
import pickle

def broadcast_result(result, conn):
        conn.send(pickle.dumps(result))
def start():
    client_socket = socket(AF_INET, SOCK_STREAM)
    with client_socket as cs:
        cs.connect(('localhost', 65432))
        while True:
            nums = cs.recv(409600000)
            print("Calculando números primos.\n")
            break
        list_nums = pickle.loads(nums)
        print(prime_number.list_primes(list_nums))
        part = pickle.dumps(prime_number.list_primes(list_nums))
        cs.send(part)


client_thread = Thread(target=start())
client_thread.start()