# Matt Bennett CS 1410 Mon-Wed-Fri 1:00pm-1:50pm

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


def candidateOverlapsTarget(target, candidate, overlap):
    if candidate[0:overlap] == target[-overlap:]:
        return True
    else:
        return False


def findLargestOverlap(target, candidate):
    if strandsAreEqualLengths(target, candidate) and strandsAreNotEmpty(target, candidate):
        length = len(target)
        largestOverlap = 0
        i = 0
        while i <= length:
            if candidateOverlapsTarget(target, candidate, i):
                largestOverlap = i
                i += 1
            else:
                i += 1
                continue
        return largestOverlap
    else:
        return -1


def findBestCandidate(target, candidates):
    largestStrand = ''
    largestOverlap = 0
    for candidate in candidates:
        overlap = findLargestOverlap(target, candidate)
        if findLargestOverlap(target, candidate) > largestOverlap:
            largestStrand = candidate
            largestOverlap = overlap
        else:
            continue
    return largestStrand, largestOverlap


def joinTwoStrands(target, candidate, overlap):
    if candidateOverlapsTarget(target, candidate, overlap):
        return target[0:len(target) - overlap] + candidate
    else:
        return target + candidate


def main():
    target = returnFirstString(fileToList(input('Target strand filename: ')))
    candidate = fileToList(input('Candidate strands filename: '))

    bestCandidate = findBestCandidate(target, candidate)
    print(joinTwoStrands(target, bestCandidate[0], bestCandidate[1]))


if __name__ == '__main__':
    main()
