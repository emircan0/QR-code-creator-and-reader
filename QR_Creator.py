import pyqrcode
import png

link = "https://www.linkedin.com/in/emircanmert"
qr_code = pyqrcode.create(link)
qr_code.png("linkedin.png", scale=5)
qr_code.show(qr_code)
