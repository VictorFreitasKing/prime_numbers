from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from multiprocessing import Process
import time, pickle

max = 1000000
num_threads = 4
connections = []
count_connections = 0
result = []

def split_range(end):
    size = end / num_threads
    parts = []

    for i in range(num_threads):
        part = [
            round(1 + size * i),
            round(size * (i+1))
        ]
        parts.append(part)
    return parts

def broadcast_parts(nums):
    for i in range(0, num_threads):
        conn, addr = connections[i]
        conn.send(pickle.dumps(nums[i]))

def receive_parts():
    parcial_results = []
    for conn, addr in connections:
        part = pickle.loads(conn.recv(4096000))
        parcial_results.append(part)
    for parcial_result in parcial_results:
        result.append(parcial_result)

def start():
    global count_connections, num_threads
    server_socket = socket(AF_INET, SOCK_STREAM)
    print('Servidor iniciado!\n')

    with server_socket as ss:
        ss.bind(('localhost', 65432))
        ss.listen()
        while True:
            connection_socket, addr = ss.accept()
            connections.append((connection_socket, addr))
            count_connections += 1

            print(f'{addr} conectou-se ao servidor')
            print(f'{len(connections)} clients conectados ao servidor\n')

            if count_connections == num_threads:
                print('Iniciando programa!\n')
                broadcast_parts(split_range(max))
                receive_parts()
                break

        before = time.time()
        Process(target=broadcast_parts, args= [split_range(max)]).run()
        #
        after = time.time()
        runtime = (after - before)
    print('Resultado - Exercicio 2:\n')
    print(f'Numero de entradas: {max}\n')
    print(f'Numero de Threads:{num_threads}\n')
    print(f'Tempo de execução: {runtime}\n')
    #print(f'{result}\n')


server_thread = Thread(target=start).start()
