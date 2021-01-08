
import sys
import time
from urllib.parse import urlparse, parse_qs

from helpers import pilihAngka, cls, cetakgaris, s
from warna import prRed, prCyan, prYellow, prGreen
from logs import Logs
from banner import Banner
from version import __constributor__

# untuk keperluan animasi loading


def main(bukaBanner = True, debug = False):
    B = Banner(True)
    # Banner
    if bukaBanner:
        cls()    
        B.cetakbanner()
    
    B.menu()

    try:
        pilihmenu = (pilihAngka("  Pilih Menu : "))        
        if (pilihmenu > 4):
            raise Exception("Menu yang dipilih tidak ada! ")


        # switch case ribet di python.. if aja :D
        if (pilihmenu == 1):
            from download import DownloadYT
            # download
            cls()
            B.cetakbanner()

            cetakgaris("Download Youtube")
            DLYt = DownloadYT(False)
            DLYt.run()
            time.sleep(5)

        elif (pilihmenu == 2):
            # ganti save path
            cls()
            B.cetakbanner()
            cetakgaris("Ubah Penyimpanan Video")
            
            cek = Logs(True)
            cek.cek()
            cek.run()
        elif pilihmenu == 3:
            # about
            cls()
            B.cetakbanner()
            cetakgaris("Team Programmer & Contributor ")
            
            print("")
            for nama in __constributor__:
                print(s("- {}".format(prGreen(nama))))

            print("")
            print(s("%s" % prCyan("Aplikasi ini dapat di peroleh di :")))
            print("")
            print(s("- %s" % prGreen("https://github.com/M24-XT/yutub")))
            print(s("- %s" % prGreen("https://github.com/jabbarbie/PythonYoutubeDownloader")))
            
        else:
            # exit
            sys.exit(r(prCyan("Terima kasih! ;) ")))
           
    except Exception as Pesan:
        print(s("Main Error %s" % prRed(Pesan)))
    

    cls
    main(False)


main(debug = True)

        