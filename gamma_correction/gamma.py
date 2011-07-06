import cv
import sys

if __name__ == "__main__":
    if len(sys.argv)<2: 
        print "panggil dengan:\n python gamma.py <namafile-gambar> [nilai koreksi]"
        sys.exit(1)
    
    #nilai koreksi gamma
    #nilai < 1.0 akan membuat citra lebih terang
    #nilai > 1.0 akan membuat citra lebih gelap
    correction_value = 0.2
    if len(sys.argv)>2:
        correction_value = float(sys.argv[2])
    
    #buka citra
    im = cv.LoadImage(sys.argv[1])
    
    #buat citra hasil sementara
    gf = cv.CreateImage(cv.GetSize(im), cv.IPL_DEPTH_32F, 3)

    #citra dengan representasi piksel floating point berada dalam rentang nilai [0.0, 1.0]
    cv.ConvertScale(im, gf, 1.0/255, 0)
    
    #operasi koreksi gamma
    cv.Pow(gf, gf, correction_value)

    #tampilkan gambar
    cv.ShowImage("original", im)
    cv.ShowImage("gammacorrected", gf)

    #tunggu sampai tombol keyboard ditekan
    cv.WaitKey(0)
