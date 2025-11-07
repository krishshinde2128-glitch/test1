# 1. Read input without any prompts
m_size = int(input())
M = set(map(int, input().split()))
n_size = int(input())
N = set(map(int, input().split()))

# 2. Find the symmetric difference
sym_diff_set = M.symmetric_difference(N)

# 3. Sort the results
sorted_results = sorted(list(sym_diff_set))

# 4. Print only the numbers
for num in sorted_results:
    print(num)