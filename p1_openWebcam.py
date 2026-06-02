import qrcode
img = qrcode.make("cafecode-mashhad.ir")
img.save("qr.png")