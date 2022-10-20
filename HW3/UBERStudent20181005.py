import sys, calendar
from collections import defaultdict

result = defaultdict(dict)

weeks = ['MON','TUE','WED','THU','FRI','SAT','SUN']

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "rt") as file:
    while True:
        row = file.readline()

        if not row: break

        info = row.strip().split(",")

        region = info[0]
        m,d,y = map(int,info[1].split("/"))
        day = weeks[calendar.weekday(y,m,d)]
        vihicle = info[2]
        trip = info[3]

        if day not in result[region]:
            result[region][day] = {}
            result[region][day]['vehicle'] = vihicle
            result[region][day]['trip'] = trip
        else:
            result[region][day]['vehicle'] +=vihicle
            result[region][day]['trip'] += trip

with open(output_file,"at") as file:
    for r in result.keys():
        for d in result[r].keys():
            file.write(f"{r},{d} {result[r][d]['vehicle']},{result[r][d]['trip']}\n")
