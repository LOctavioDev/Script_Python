import qrcode

def generar_codigo_qr(enlace, nombre_archivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(enlace)
    qr.make(fit=True)

    imagen_qr = qr.make_image(fill_color="black", back_color="white")
    imagen_qr.save(nombre_archivo)

if __name__ == "__main__":
    enlace = "https://github.com/LOctavioDev"
    nombre_archivo = "codigo_qr.png"
    generar_codigo_qr(enlace, nombre_archivo)
    print(f"El código QR ha sido generado y guardado en {nombre_archivo}.")
