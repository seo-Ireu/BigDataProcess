import sys
from collections import defaultdict

input_file = sys.argv[1]
output_file = sys.argv[2]

result = defaultdict(int)

with open(input_file,"rt") as file:
    while True:
        row = file.readline()

        if not row: break

        info = row.split("::")
        genres = info[2].strip().split("|")

        for g in genres:
            result[g] +=1

with open(output_file,"at") as file:
    for genre, cnt in result.items():
        file.write(f"{genre} {cnt}\n")



