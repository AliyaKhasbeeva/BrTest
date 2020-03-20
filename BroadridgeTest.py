import datetime
import os
from sys import argv


script, path = argv

dir_name = os.path.dirname(path)
file_name = os.path.basename(path)
out_file_name = os.path.splitext(file_name)[0]+".out"
output_path = os.path.join(dir_name, out_file_name)

in_file = open(path, 'r', encoding='utf8')
out_file = open(output_path, 'w', encoding='utf8')
file_rows = []
time_from = datetime.datetime.strptime("18:00:00", "%H:%M:%S")
time_to = datetime.datetime.strptime("23:59:59", "%H:%M:%S")
for row in in_file:
    parts = row.split()
    file_rows.append(parts)
for i in range(len(file_rows)):
    msg_date = datetime.datetime.strptime(file_rows[i][0], "%Y/%m/%d")
    if msg_date.weekday() != 5 and msg_date.weekday() != 6:
        msg_time = datetime.datetime.strptime(file_rows[i][1], "%H:%M:%S")
        if time_to >= msg_time >= time_from:
            print(*file_rows[i][3:], file=out_file)
in_file.close()
out_file.close()
