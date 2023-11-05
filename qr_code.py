import qrcode 

link = input('Digite o link para qrcodar:\n-> ')

img = qrcode.make(link)
type(img)
img.save(f'arquivo_qrcode.png')