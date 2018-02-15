import math
import itertools

def main():
    N = int(input())

    if N >= 9:
        return

    C = []
    for _ in range(N):
        C.append(int(input()))

    N_fact = math.factorial(N)
    total_surface = 0

    for sequence in itertools.permutations(C, N):
        is_surface = [True] * N

        for start_idx in range(N-1):
            for target_idx in range(start_idx+1, N):
                if sequence[target_idx] % sequence[start_idx] == 0:
                    is_surface[target_idx] = not is_surface[target_idx]

        for surface in is_surface:
            if surface:
                total_surface += 1

    print(total_surface / N_fact)


main()
