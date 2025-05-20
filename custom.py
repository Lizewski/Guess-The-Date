import os

def printcenter(text):
    try:
        columns = os.get_terminal_size().columns
    except:
        columns = 80

    for line in text.split('\n'):
        print(line.center(columns))