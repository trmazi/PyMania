import sys
import struct
import os

if len(sys.argv) != 2:
    print(f"dump_sound <sound.bin>")
    sys.exit(0)

inputfile = sys.argv[1]

with open(inputfile, "rb") as snd:
    magic = snd.read(5)
    if magic != b'BESND':
        print("invalid magic")
        sys.exit(0)

    files = struct.unpack('i', snd.read(4))[0]
    print(f"files: {files}")

    for file in range(files):
        filename = snd.read(132).decode("utf-8").rstrip("\x00").strip("\\").strip(".\\")
        snd.read(4)
        size = struct.unpack('i', snd.read(4))[0]
        snd.read(4)
        data = snd.read(size)
        outputfile = os.path.join(f"{inputfile}-extract", (filename + ".wav"))

        try:
            os.makedirs(os.path.dirname(outputfile))
        except:
            pass
        print(outputfile)

        with open(outputfile, "wb") as output:
            output.write(data)
