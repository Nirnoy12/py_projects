import qrcode
from PIL import Image

# 💬 Take user input
user_text = input("Enter the text to encode into QR code: ")

# 📦 Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(user_text)
qr.make(fit=True)

# 🖼️ Generate image
img = qr.make_image(fill_color="black", back_color="white")

# 💾 Save image
output_file = "./python/qr-code_generator/MY_QRCODE.png"
img.save(output_file)

print(f"✅ QR Code saved as '{output_file}' with your message.")
