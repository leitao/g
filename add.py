import hashlib
import os
import zlib

DEBUG = 1


# Compress the database such as the following command can decompress
# $ openssl zlib -d -in <obj>

def create_index(ci, filename, size):
    index = os.getcwd() + "/.git/index"

    fd = open(index, "w")

    buf = "10644 " + ci + " " + str(size) + "\t" + filename
    if DEBUG:
        print(buf)

    sig = [ord('D'), ord('I'), ord('R'), ord('C')]
    signature = bytearray(sig)

    ver = 0x2

    fd.write(buf)
    fd.close()

def compress(buf):
    compressed = zlib.compress(bytes(buf.encode('utf-8')))
    if 0:
        print(compressed)

    return compressed


# Create object into the database
def create_obj(ci, buf):
    head = ci[0:2]
    tail = ci[2:]

    if DEBUG:
        print(head)

    objs = os.getcwd() + "/.git/objects/" + head + "/"
    os.makedirs(objs, exist_ok=True)


    objfile = open(objs + tail, "wb")
    bytez = bytearray(compress(buf))
    objfile.write(bytez)
    objfile.close()

# Initial function to add a file into index
def add(filename):
    print("adding file", filename)
    addfile = open(filename, 'r')
    content = addfile.read() #.strip()
    size = len(content)
    buff = "blob " + str(size) + '\0' + content
    print(buff)
    sha_1 = hashlib.sha1()
    sha_1.update(buff.encode('utf-8'))

    # commmit id
    ci = sha_1.hexdigest()
    if DEBUG:
        print(ci)

    create_obj(ci, buff)
    create_index(ci, filename, size)
