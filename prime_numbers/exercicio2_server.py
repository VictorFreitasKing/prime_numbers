from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time, pickle

max = 100
num_threads = 2
connections = []
count_connections = 0

result = []

def broadcast_parts(nums):
    for i in range(len(nums)):
        conn, addr = connections[i]
        conn.send(pickle.dumps(nums[i]))
        parcial_results = pickle.loads(conn.recv(4096))

        for parcial_result in parcial_results:
            result.append(parcial_result)
def start():
    global count_connections, num_threads
    server_socket = socket(AF_INET, SOCK_STREAM)

    nums = []
    i=0
    while(i<max+1):
        nums.append(int(i+1))
        i+=int(max/num_threads)
    nums[len(nums)-1]=max

    start_indexes = []
    end_indexes = []
    start_indexes.append(nums.pop(0))
    end = nums.pop()
    for num in nums:
        start_indexes.append(num)
        end_indexes.append(num)

    end_indexes.append(end)

    indexes = []
    indexes.append(start_indexes)
    indexes.append(end_indexes)

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
                broadcast_parts(indexes)
                break
        print(result)




server_thread = Thread(target=start)
server_thread.start()
