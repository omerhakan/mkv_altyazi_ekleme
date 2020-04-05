import os
import sys
import os.path
import subprocess
import time


def altyazi_ekle(altyaziEklenecekDosyaIsmi):
    process = subprocess.Popen(
        ['C:\\mkv\\mkvinfo.exe', altyaziEklenecekDosyaIsmi], stdout=subprocess.PIPE)
    stdout = process.communicate()[0]
    b = 'STDOUT:{}'.format(stdout)

    subtitleSayisi = str(stdout).count('subtitle')
    toplamTrackSayisi = str(stdout).count('Track number:')
    silmeSonrasiTrackSayisi = toplamTrackSayisi - subtitleSayisi

    videolarinDizini = os.path.dirname(altyaziEklenecekDosyaIsmi)
    uzantisizDosyaIsmi = os.path.splitext(
        os.path.basename(altyaziEklenecekDosyaIsmi))[0]

    uretilecekDosyaIsmi = videolarinDizini + '\\' + uzantisizDosyaIsmi + '.tur.mkv'

    if os.path.isfile(videolarinDizini + '\\' + uzantisizDosyaIsmi + '.srt'):
        altyaziDosyaIsmi = videolarinDizini + '\\' + uzantisizDosyaIsmi + '.srt'

    if os.path.isfile(videolarinDizini + '\\' + uzantisizDosyaIsmi + '.ass'):
        altyaziDosyaIsmi = videolarinDizini + '\\' + uzantisizDosyaIsmi + '.ass'

    print('Toplam Track Sayisi: {}'.format(toplamTrackSayisi))
    print('Toplam Subtitle Sayisi: {}'.format(subtitleSayisi))
    print('Kalan Track Sayisi: {}'.format(silmeSonrasiTrackSayisi))

    altyaziEklemeKomut = 'C:\\mkv\\mkvmerge.exe -o ' + \
        '"' + uretilecekDosyaIsmi + '" --no-subtitles ' + \
        '"' + altyaziEklenecekDosyaIsmi + '" ' + \
        ' --language ' + str(0) + ':tur ' + \
        '"' + altyaziDosyaIsmi + '"'

    os.system(altyaziEklemeKomut)


for arg in sys.argv[1:]:
    altyazi_ekle(arg)
