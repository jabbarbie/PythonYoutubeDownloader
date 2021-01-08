import sys, os, time
from warna import prCyan, prRed, prYellow

from threading import Thread
from itertools import cycle

done = False

def animasi():
    global done
    for x in cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r' + x)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

def tunggu():
    Thread(target=animasi).start()


def s(kata)->str:
    return "  %s" % (kata)

def garis()->str:
    return s("============================================") #40

def ceksize(filesize: 0) -> str:
    """ parameter : int (byte) """
    ukuran = "bit"
    if (filesize < 1000):
        ukuran = "byte"
        filesize = (filesize/1000)
    elif (filesize < 1000000):
        ukuran = "kB"
        filesize = (filesize/100000)
    elif (filesize >= 1000000):
        ukuran = "MB"
        filesize = (filesize/1000000)

    return "{0:.1f} {1}".format(filesize, ukuran)

def pilihAngka(tanya)->int:
    while True:
        try:
            pilih = int(input(tanya))
            return pilih
        except Exception:
            print(s("%s" % prRed("Bukan angka!")))
    return pilih

def cls():
    # karena di windows pakenya cls
    if sys.platform == 'win32':
        os.system("cls")
        return
    os.system("clear")

def cetakgaris(kata):
    spasi = ""
    jum = int((46 - len(kata)) / 2) - 2
    print(prCyan(garis()))
    for ispace in range( jum ):
        spasi = "{} ".format(spasi)

    print("  {0}{1}{2}{1}{0}".format(prCyan("|"), spasi , prYellow(kata)))
    print(prCyan(garis()))
    print("")
