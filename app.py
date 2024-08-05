import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
import io

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        
        # URL Input
        self.url_label = tk.Label(root, text="Omer's App")
        self.url_label.pack(pady=10)
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=5)
        
        # Generate Button
        self.generate_button = tk.Button(root, text="Generate QR Code", command=self.generate_qr)
        self.generate_button.pack(pady=20)
        
        # QR Code Display
        self.qr_label = tk.Label(root)
        self.qr_label.pack(pady=10)
    
    def generate_qr(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a URL.")
            return
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert the image to a format Tkinter can display
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        img = Image.open(img_byte_arr)
        img = img.resize((200, 200), Image.LANCZOS)
        self.qr_image = ImageTk.PhotoImage(img)
        self.qr_label.config(image=self.qr_image)
        
        # Save the QR code as an image file
        img.save('qrcode.png')

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop()
