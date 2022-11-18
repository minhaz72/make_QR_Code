# create a QR code and decode a QR code : 
import pyqrcode 
import png 
from pyzbar.pyzbar import decode 
from PIL import Image 
def qr_code(link): 
    qr_code=pyqrcode.create(link)
    qr_code.png()
def decode_qr_code(link):  # image link 
    decodeQr=decode(Image.open(link ))
    print(decodeQr[0].data.decode('acil'))
