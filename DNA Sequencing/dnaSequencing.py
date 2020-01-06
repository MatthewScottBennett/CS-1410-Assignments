import os

def fileToList(filename):
    files_lines = []
    if os.path.isfile(filename):
        file = open(filename)
        for line in file:
            files_lines.append(line.strip())
        file.close()
    return files_lines

def returnFirstString(strings):



    return 0