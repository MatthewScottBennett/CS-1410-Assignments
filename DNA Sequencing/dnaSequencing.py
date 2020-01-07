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
    if strings == []:
        return ''
    else:
        return strings[0]

def strandsAreNotEmpty(strand1, strand2):
    strand1length = len(strand1)
    strand2length = len(strand2)
    if strand1length > 0 and strand2length > 0:
        return True
    else:
        return False

def strandsAreEqualLengths(strand1, strand2):
    strand1length = len(strand1)
    strand2length = len(strand2)
    if strand1length == strand2length:
        return True
    else:
        return False

def candidateOverlapsTarget(target, canadite, overlap):

    i = 0
    while i <


    return

def findLargestOverlap():
    return

def findBestCandidate():
    return

def joinTwoStrands():
    return

def main():
    return