from itertools import permutations

def calculate_total_distance(permutation, distance_matrix):
    total_distance = 0
    for i in range(len(permutation) - 1):
        total_distance += distance_matrix[permutation[i]][permutation[i + 1]]
    total_distance += distance_matrix[permutation[-1]][permutation[0]]
    return total_distance

def traveling_salesman_brute_force(distance_matrix):
    num_cities = len(distance_matrix)
    all_permutations = permutations(range(num_cities))
    min_distance = float('inf')
    best_permutation = None

    for perm in all_permutations:
        current_distance = calculate_total_distance(perm, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_permutation = perm

    return best_permutation, min_distance

# Example usage
if __name__ == "__main__":
    distance_matrix = [
        [0, 29, 20, 21],
        [29, 0, 15, 17],
        [20, 15, 0, 28],
        [21, 17, 28, 0]
    ]

    best_route, min_distance = traveling_salesman_brute_force(distance_matrix)
    print("Best route:", best_route)
    print("Minimum distance:", min_distance)
