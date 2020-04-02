import shutil

def findStart(lines):
    for i, line in enumerate(lines):
        if "song.ini" in line:
            return i + 1
    raise ValueError("No valid start line. No songs are missing .ini files.")


def findEnd(lines, start):
    blankLines = findBlanks(lines)
    for lineNo in blankLines:
        if lineNo > start:
            return lineNo
    raise ValueError("No valid end line. Perhaps there isn't a blank line at the end of the file?")


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


def createINIFile(path):
    iniFile = shutil.copy('template.ini', path + "/song.ini")
    songName = path[path.rindex("-")+2:].title()
    artist = path[path.rindex("/")+1:path.rindex("-")].title()

    # open(path + "/song.ini", "a") as ini:

    print(songName, "by", artist)
    print(iniFile)


if __name__ == "__main__":

    with open("D:/Clone Hero/badsongs.txt", "r") as badSongs:
        lines = badSongs.readlines()

    try:
        badSongINIStart = findStart(lines)
    except ValueError as err:
        print(err)
        exit(-1)

    try:
        badSongINIEnd = findEnd(lines, badSongINIStart)
    except ValueError as err:
        print(err)
        exit(-2)

    songs = stripSongs(lines, badSongINIStart, badSongINIEnd)
    createINIFile(songs[0])
    print(songs)

