import random
import time

def selection_sort(alist: list) -> int:
    comparsions: int = 0
    for i in range(len(alist)):
        min_pos = i
        for j in range(i + 1, len(alist)):
            comparsions += 1
            if alist[j] < alist[min_pos]:
                min_pos = j
        alist[i], alist[min_pos] = alist[min_pos], alist[i]
    return comparsions


def insertion_sort(alist: list) -> int:
    comparsions: int = 0
    for i in range(1, len(alist)):
        key = alist[i]
        j = i - 1
        comparsions += 1
        already_comped = True
        while j >= 0 and key < alist[j]:
            alist[j + 1] = alist[j]
            j -= 1
            if already_comped:
                already_comped = False
                continue
            comparsions += 1
        if j >= 0 and alist[j + 1] != key:  
            # didnt reach front of list and key wasnt less than item to left
            comparsions += 1  
        alist[j + 1] = key
    return comparsions


def main():

    # for num in [1000, 2000, 4000, 8000, 16000, 32000]:
    for num in [100_000]:  # for testing purposes
        random.seed(1234)
        randoms = random.sample(range(1000000), num)  # Generate num random numbers from 0 to 999,999
        start_time = time.time()
        comps = selection_sort(randoms)
        stop_time = time.time()
        print("n:", num, "- comps:", comps, "- time:", stop_time - start_time)

if __name__ == '__main__': 
    main()

