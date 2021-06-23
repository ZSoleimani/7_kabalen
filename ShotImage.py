import qrcode
fileExtension = ".png"

cards = ["h", "d", "s", "c"]
images = ["J", "Q", "K", "A"]
for x in range(len(cards)):
    for j in range(9):
        data = (str(j+2)) + cards[x]
        qr = qrcode.make(data)
        qr.save(data + fileExtension)
    for k in range(len(images)):
        data = images[k] + cards[x]
        qr = qrcode.make(data)
        qr.save(data + fileExtension)