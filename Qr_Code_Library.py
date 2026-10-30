import qrcode
Message = "www.youtube.com"
image = qrcode.make(Message)
image.save("Youtube_QR_Code.png")