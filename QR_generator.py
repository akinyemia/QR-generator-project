#QR generator 
#pip install segno
#to install dependency 

import segno

qrcode_msg = input('QR code display:')
qrcode = segno.make_qr(qrcode_msg)
qrcode.save('QR_test.png', scale=10)
qrcode.show()