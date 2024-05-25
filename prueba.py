import re

# Read the number of test cases
T = int(input().strip())

# List to store results
results = []

# Process each test case
for _ in range(T):
    S = input().strip()
    try:
        # Try to compile the regex
        re.compile(S)
        results.append("True")
    except re.error:
        results.append("False")

# Print the results for each test case
for result in results:
    print(result)
