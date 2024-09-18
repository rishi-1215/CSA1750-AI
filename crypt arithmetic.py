from itertools import permutations

def solve_cryptarithmetic(puzzle):
    # Split the puzzle into left-hand side, right-hand side, and result
    parts = puzzle.split('+')
    left = parts[0].strip()
    right, result = parts[1].split('=')
    right = right.strip()
    result = result.strip()
    letters = set(left + right + result)

    # Generate all possible permutations of digits for the letters
    for perm in permutations(range(10), len(letters)):
        # Map letters to digits in the permutation
        mapping = dict(zip(letters, perm))
        
        # Check if any of the numbers start with 0
        if mapping[left[0]] == 0 or mapping[right[0]] == 0 or mapping[result[0]] == 0:
            continue

        # Convert letters to digits in left, right, and result
        left_num = int(''.join(str(mapping[char]) for char in left))
        right_num = int(''.join(str(mapping[char]) for char in right))
        result_num = int(''.join(str(mapping[char]) for char in result))

        # Check if the equation holds true
        if left_num + right_num == result_num:
            return mapping  # Return the mapping of letters to digits

    return None  # No solution found

# Example usage:
puzzle = "SCOOBY + DOOO = BLINKS"
solution = solve_cryptarithmetic(puzzle)
if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print(f"{letter}: {digit}")
else:
    print("No solution found.")
