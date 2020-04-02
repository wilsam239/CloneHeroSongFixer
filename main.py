import shutil
import sys
import fileinput


def findStart(lines):
    return [i + 1 for i, line in enumerate(lines) if
            'song.ini' in line] or "Error"


def findEnd(lines):
    blankLines = findBlanks(lines)
    start = findStart(lines)
    try:
        return [lineNo for lineNo in blankLines if
                lineNo > start[0]] or "Error"
    except TypeError:
        print("No valid start line. No songs are missing .ini files.")
        exit(-1)


def findBlanks(lines):
    return [i for i, line in enumerate(lines) if line.isspace()]


def stripSongs(lines, start, end):
    try:
        return [line.replace("\\", "/").strip() for line in lines[start[0]:end[0]]]
    except TypeError:
        print("No valid end line. Perhaps there isn't a blank line at the end of the file?")
        exit(-2)


def createINIFile(path):
    iniFile = shutil.copy('template.ini', path + "/song.ini")
    songName = path[path.rindex("-") + 2:].title()
    artist = path[path.rindex("/") + 1:path.rindex("-")].title()

    for line in fileinput.input(iniFile, inplace=True):
        print(line.replace("name =", "name =" + songName).strip())
    for line in fileinput.input(iniFile, inplace=True):
        print(line.replace("artist =", "artist =" + artist).strip())

    print(songName, "by", artist)
    print(iniFile)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "D:/Clone Hero/badsongs.txt"

    print(f"Checking path: {path}")

    try:
        with open(path, "r") as badSongs:
            lines = badSongs.readlines()
    except FileNotFoundError:
        print(f"No file found at this path: {path}")
        exit(-3)

    songs = stripSongs(lines, findStart(lines), findEnd(lines))

    for song in songs:
        createINIFile(song)
    print(songs)
