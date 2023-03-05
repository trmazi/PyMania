import sys
import struct
import os

if len(sys.argv) != 3:
    print(f"make_sound <output path> <input path>")
    sys.exit(0)

inputdir = sys.argv[2]
outputpath = sys.argv[1]

print(f"Creating sound.bin file named from input directory {inputdir}!")

snd = open(f"{outputpath}\\sound.bin", "wb")
snd.write(b'BESND')

files_cnt = 0
for subdir, dirs, files in os.walk(inputdir):
    for filename in files:
        if not filename.endswith('.wav'):
            continue
        files_cnt += 1

snd.write(struct.pack('i', files_cnt))
print(f"Number of files: {files_cnt}")

# get the files and paths
for subdir, dirs, files in os.walk(inputdir):
    for filename in files:
        fullfilepath = subdir + os.sep + filename
        if not filename.endswith('.wav'):
            continue

        # filename needs to be padded to 132 chars
        properpath = filename.replace('.wav', '').ljust(132, '\x00')
        print(filename)
        snd.write(bytes(properpath, encoding="utf-8"))
        
        snd.write(b'\xFF\xFF\xFF\xFF')
        
        # insert size
        file_size = (os.path.getsize(fullfilepath))
        snd.write(struct.pack('i', file_size))

        snd.write(b'\x00\x00\x00\x00')

        # insert data
        data = open(fullfilepath, "rb")
        data_hex = data.read()
        snd.write(data_hex)
        data.close()

snd.close()