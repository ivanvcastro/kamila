import qrcode

# URL do link
url = "https://ivanvcastro.github.io/kamila/"

# Gerar o QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Criar a imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salvar a imagem
img.save("qrcode_kamila.png")