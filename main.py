import qrcode
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from PIL import Image, ImageTk


# window initialization
window = Tk()
window.iconbitmap("icon.ico")
window.title('QR Code Wizard')
canvas = Canvas(window, width=500, height=500)
canvas.grid(columnspan=3, rowspan=3)

# taking user inputs


# Display the QR Code in the window upon creation
icon = Image.open('qr_code.png')
icon = ImageTk.PhotoImage(icon)
icon_label = Label(image=icon)
icon_label.image = icon
icon_label.grid(column=1, row=0)

# data = 'kelesh'
# qr = qrcode.QRCode(version=1, box_size=5, border=5)  # version is from 1 to 40;      border should be 4 or more
# qr.add_data(data)
# qr.make(fit=True)  # if version=None and fit=True, the QR Code will be in a uniform size
#
# img = qr.make_image(fill_color='black', back_color='white')
# img.save('qr_code.png')

window.mainloop()
