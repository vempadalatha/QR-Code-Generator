import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
qr=qrcode.make("https://www.linkedin.com/in/vempada-latha-859658303/")
qr.save("qr.png",scale=8)
b=decode(Image.open("qr.png"))
print(b[0].data.decode("ascii"))