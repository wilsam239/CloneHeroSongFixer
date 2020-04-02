def findStart(lines):
    for i,line in enumerate(lines):
        if "song.ini" in line:
            return i + 1
    return -1


def findEnd(lines, start):
    blankLines = findBlanks(lines)
    for lineNo in blankLines:
        if lineNo > start:
            return lineNo
    return -1


def findBlanks(lines):
    blankLines = []
    for i, line in enumerate(lines):
        if line == '\r' or line == '\n':
            blankLines.append(i)
    return blankLines


def stripSongs(lines, start, end):
    songs = []
    for line in lines[start:end:]:
        l = line.replace("\\", "/")
        songs.append(l.rstrip("\n"))
    return songs


if __name__ == "__main__":

    with open("D:/Clone Hero/badsongs.txt", "r") as badSongs:
        lines = badSongs.readlines()
        badSongINIStart = findStart(lines)
        badSongINIEnd = findEnd(lines, badSongINIStart)

    songs = stripSongs(lines, badSongINIStart, badSongINIEnd)
    print(songs)

