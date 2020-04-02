import datetime as dt
from pathlib import Path
from sys import argv


def change_file(file_path):
    with open(file_path, 'r', encoding='utf8') as in_file:
        output_path = Path(file_path).with_suffix('.out')
        with open(output_path, 'w', encoding='utf8') as out_file:
            time_from = dt.datetime.strptime("18:00:00", "%H:%M:%S")
            for row in in_file:
                parts = row.split(" ", maxsplit=3)
                msg_date = dt.datetime.strptime(parts[0], "%Y/%m/%d")
                if msg_date.weekday() != 5 and msg_date.weekday() != 6:
                    msg_time = dt.datetime.strptime(parts[1], "%H:%M:%S")
                    if msg_time >= time_from:
                        out_file.write(*parts[3:])


script, path = argv
if __name__ == '__main__':
    change_file(path)
