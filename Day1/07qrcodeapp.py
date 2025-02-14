import qrcode
name = input("Enter Your name: ")
img = qrcode.make(f"Hey {name}, how is your python programming going so far..  :) :) ")
type(img)
img.save(f"{name}.png")