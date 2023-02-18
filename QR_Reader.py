import cv2
from pyzbar import pyzbar


def okuyucu(cerceve):
    #QR kod bilgisinin şifresini çözüyor
    qrKodlar = pyzbar.decode(cerceve)           
    for qrKod in qrKodlar:
        x, y , w, h = qrKod.rect
        bilgi = qrKod.data.decode('utf-8')

        #QR kod etrafına dikdörtgen çiziyor
        cv2.rectangle(cerceve, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        # Dikdörtgenin üzerine metin ekliyoruz
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(cerceve, bilgi, (15,25), font, 0.75, (255, 255, 255), 2)
        #Bilgileri bir metin belgesine aktarıyoruz.
        with open("QRKod.txt", mode ='w') as dosya:
            dosya.write("Tannan Barkod:" + bilgi)
    return cerceve

    
def main():
    camera = cv2.VideoCapture(0)
    ret, cerceve = camera.read()
    while ret:
        ret, cerceve = camera.read()
        cerceve = okuyucu(cerceve)
        cv2.imshow('QR Kod Okuyucu', cerceve)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    camera.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':  
    main()