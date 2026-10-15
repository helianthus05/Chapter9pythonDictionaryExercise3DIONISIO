filename = input("Enter file name: ")

try:
    handle = open(filename)
except FileNotFoundError:
    print(f"File {filename} could not be opened.")
    quit()

counts = dict()

for line in handle:
    if not line.startswith("From "):
        continue

    words = line.split()
    email = words[1]

    counts[email] = counts.get(email, 0) + 1

print(counts)
