
# MKV Altazyı Ekleme
#### Nedir?
Video dosyasını sürükle bırak yaparak Matroska (mkv) dosyasına altyazı eklemek için yazılmış bir python scriptdir.

#### Neden?
Bazı media playerlerın video dosyasının yanındaki altyazıları görmemesinden dolayı altyazıları video dosyasına eklemek ihtiyacından yazıldı.

#### Nasıl çalışır?
[MKVToolNix – Matroska tools for Linux/Unix and Windows](https://mkvtoolnix.download) araçlarını kullanarak video dosyalarından Matroska (mkv) oluşturup altyazıyı bu dosyaya ekler. Video dosyası herhangi bir format olacağıbileceği gibi mkv dosyasıda olabilir. Sadece .ass veya .srt dosyalarını destekler. Üretilen yeni dosyanın ismi video dosyasına .tur.mkv ekelnerek yeni mkv dosyası oluşturulur.

#### Adım adım

 1. [Python yükleyin.](https://www.python.org/downloads/)
 2. [MKVToolNix](https://www.fosshub.com/MKVToolNix.html)'in mümkünse portable versiyonunu indirin.
 3. **altyazi_ekleme.py** dosyasını indirin.
 4. **C:\mkv** dizini oluşturun.
 5. MKVToolNix paketinden **mkvinfo.exe** ve **mkvmerge.exe** dosyalarını **C:\mkv** dizinine kopyalayın.
 6. Altyazı dosyasının video dosyasının aynı dizinde ve aynı isimde olduğundan emin olun.
 7. Video dosyasını **altyazi_ekleme.py** üzerine sürükleyip bırakın.
 8. ![Kullanım](http://omerhakan.net/altyazi_ekleme.gif)
