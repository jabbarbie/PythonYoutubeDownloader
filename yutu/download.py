import sys
from warna import prCyan, prYellow, prLightGray, prRed, prGreen
from helpers import cls, s, cetakgaris, garis, done

# Cek Paket PYTube
try:
    from pytube import Stream, YouTube
except ImportError:
    print(s(prRed("Pytube tidak ditemukan")))
    print(s("Install terlebih dahulu untuk melanjutkan"))
    print(s(prGreen("pkg install pytube")))
    sys.exit(1)

from ffmpeg import RewriteFunction
from urllib.parse import urlparse, parse_qs

from helpers import ceksize, pilihAngka, tunggu
from logs import Logs
import time
from banner import Banner
import sys
from cli import on_progress

class DownloadYT(RewriteFunction):
    def __init__(self, isDebug=False, link = None):
        """ Constructor 
        :param boolean debug:
            untuk mengecek dalam mode pengembang atau tidak
            jika true, skip semua banner / animasi
        """

        self._isDebug: bool = isDebug
        self._link = None
        self._isPlaylist: bool = False
        self._YT = YouTube
        self._savePath = 'D:/b'

        if not link == None:
            self._link = link
        
    @property
    def isDebug(self):
        """Get Mode"""
        return self._isDebug

    @property
    def link(self):
        """Link Video yang akan didownload"""
        return self._link

    """
    @link.setter
    def link(self, link):
        self._link = link;
    """

    @link.setter
    def YT(self, YT):
        self._YT = YT
        
    def tanyaLink(self):
        """ Cek apakah link valid atau tidak """
        try:
            if self._isDebug:
                self._link = 'https://www.youtube.com/watch?v=8uy7G2JXVSA'
                return

            tanya = input((s("Paste Link Youtube: ")))
            link = urlparse(tanya)
            
            if not link.scheme :
                raise ValueError("Link Tidak Valid")
            if not link.netloc in ['www.youtube.com', 'youtube.com','m.youtube.com', 'youtu.be','m.youtu.be']:                     
                raise ValueError("Bukan Link Youtube")

            self._link = tanya

        except ValueError as pesan:
            print(s(pesan))
            self.tanyaLink()

    @isDebug.setter
    def isDebug(self, isDebug):
        self._isDebug = isDebug
        
    
    def infoVideo(self):
        """Menampilkan Informasi Video"""
        
        print(s("{0:8}: {1}".format('Judul', prCyan(self._YT.title[0:30])) ))
        print(s("{0:8}: {1}".format('Chanel', self._YT.author)))
        print("")
        print(s("{0:8}: {1}".format('Views', self._YT.views)))
        print(s("{0:8}: {1}".format('Rating', self._YT.rating)))
        print(s("{0:8}: {1}".format('Publish', self._YT.publish_date)))
        print(s("{0:8}: {1:.1f} Menit".format('Durasi', self._YT.length / 60)))

    

    def resolusi(self):
        yts = self._YT.streams
        yt_video = yts.filter(type='video')
        yt_audio = yts.get_audio_only()
        jumlahpilihan = len(yt_video) + 1
        
        print(s("{0:3} {1:15} {2}".format('No', 'Resolusi', 'Size')))
        print(garis())

        for i,data in enumerate(yt_video, start=1):
            resolusi = data.resolution
            print(s("{0:3} {1:15} {2}".format(i, resolusi, ceksize(data.filesize + yt_audio.filesize) )) )

        print(s("{0:3} {1:15} {2}".format(len(yt_video)+1,"Audio MP3", ceksize(yt_audio.filesize))))
        print(garis())
        strpilih = (s(prYellow("Pilih Nomor 1 sampai {0} : ".format(str(jumlahpilihan) ))))

        pilih = pilihAngka(strpilih)
        
        if ((pilih) > jumlahpilihan):
            print(s("Pilihan Tidak Valid"))
            self.resolusi()

        self._Audio = yt_audio
        
        
        if ( (pilih) == jumlahpilihan):
            return "audio"

        self._Video = yt_video[pilih-1]
        return "video"

    def run(self):
        """ Fungsi awal saat program dijalankan """

        if(self._isDebug):
            print(s("Mode Debug Active"))
        
        if self._link is None:
            self.tanyaLink()
        
        cls()
        B = Banner()
        B.cetakbanner()
        cetakgaris("Pilih Resolusi Video")

        # tunggu()
        self._YT = YouTube(self._link, on_progress_callback=on_progress)
        done = True

        self._YT.check_availability


        self.infoVideo()
        print("")
        time.sleep(3)
        pilihan = self.resolusi()
        
        cek = Logs()
        if (not cek.cek()):
            print(s("%s" % prRed("Lokasi penyimpanan belum diset ") ))
            cek.gantiPath()


        self._savePath = cek._path

        cls()
        B.cetakbanner()
        cetakgaris("Please Wait.. Downloading")
        
        try:
            if pilihan == 'video':
                super(DownloadYT, self).Downloaderffmpeg(self._Audio, self._Video, self._savePath)
            elif (pilihan == 'audio'):
                super(DownloadYT, self).DownloadMP3(self._Audio, self._savePath)
            else:
                raise ValueError("Error")
        except Exception as Pesan:
            print(s("Terjadi kesalahan! %s" % Pesan))
            return

        print("")    
        sys.exit(s(prCyan("Terima kasih! ;) ")))
        
        
        