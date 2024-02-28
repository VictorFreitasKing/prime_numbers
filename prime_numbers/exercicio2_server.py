from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time, pickle

max = 1000000,
num_threads = 4
connections = []
count_connections = 0

result = []


def split_range(start, end):
    size = (end - start) / num_threads
    var = start + size
    parts = []

    for i in range(num_threads):
        part = [
            int(var * i),
            int(var + size * (i + 1))
        ]
        parts.append(part)
        print(part)

    return parts

def broadcast_parts(nums):
    for i in range(0, num_threads):
        conn, addr = connections[i]
        conn.send(pickle.dumps(nums[i]))
        parcial_results = pickle.loads(conn.recv(4096))

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
                print('Conexões  atingidas!\n')

                before = time.time()
                broadcast_parts(split_range(1, max))
                after = time.time()
                runtime = (after - before)
                print('Resultado - Exercicio 2:\n')
                print(f'Numero de entradas: {max}\n')
                print(f'Numero de Threads:{num_threads}\n')
                print(f'Tempo de execução: {runtime}\n')
                break




server_thread = Thread(target=start)
server_thread.start()
