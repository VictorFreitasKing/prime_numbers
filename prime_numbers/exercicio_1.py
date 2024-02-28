import time
from prime_numbers import prime_number
from multiprocessing import Pool

if __name__ == '__main__':
    max = 1000000
    num_threads = 8

    nums = []
    i=0
    if (num_threads>1):
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

        with Pool(num_threads) as p:
            before = time.time()
            results = p.map(prime_number.list_primes, indexes)
            prime_numbers_result = []

            for result in results:
                for i in result:
                    prime_numbers_result.append(i)
            after = time.time()
            runtime = (after - before)
    else:
        before = time.time()
        prime_numbers_result = prime_number.list_primes([num_threads, max])
        after = time.time()
        runtime = (after - before)

    print('Resultado:\n')
    print(f'Numero de entradas: {max}\n')
    print(f'Numero de Threads:{num_threads}\n')
    print(f'Tempo de execução: {runtime}\n')
    #print(f'{prime_numbers_result}\n')
