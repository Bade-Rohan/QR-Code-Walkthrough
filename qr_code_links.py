import qrcode
qr =qrcode.QRCode(
        version=1,#size of the png
        box_size=15,
        border=5)
link = "https://github.com/Bade-Rohan"
qr.add_data(link)
qr.make(fit= True)
image_png = qr.make_image(fill="black",back_color="white")
image_png.save("link.png")

