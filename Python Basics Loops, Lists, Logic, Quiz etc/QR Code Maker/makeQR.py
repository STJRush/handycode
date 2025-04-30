import qrcode

url = "https://youtu.be/epPbr8r963I?si=7gcWeiRz5NSwan2x"
img = qrcode.make(url)
img.save("youtube_qr.png")

#https://www.qr-code-generator.com/