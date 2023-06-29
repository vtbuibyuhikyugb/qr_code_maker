# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 
import os
import tkinter
# String which represent the QR code 
def make_def():
    text_text=text_w.get(1.0,tkinter.END)
    if(len(text_text)!=0):
    
        # Generate QR code 
        url = pyqrcode.create(text_text) 
        print(type(url))
        # Create and save the png file naming "myqr.png" 
        url.svg("myqr.svg", scale = 8) 
        os.system("1.html")


W=tkinter.Tk()
W.title("qr_code")
text_w=tkinter.Text(W)
B=tkinter.Button(W,command=make_def)
text_w.pack()
B.pack()
W.mainloop()
