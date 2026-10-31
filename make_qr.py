"""Make a QR code PNG from a URL.
Usage: python3 make_qr.py https://USERNAME.github.io/learnops-trail/ qr_game.png
Needs: pip install qrcode[pil] opencv-python-headless
"""
import sys, qrcode, cv2
url = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else "qr_game.png"
img = qrcode.make(url, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=12, border=4)
img.save(out)
got, _, _ = cv2.QRCodeDetector().detectAndDecode(cv2.imread(out))
print("saved", out, "| decodes to:", got)
if got != url:
    sys.exit("QR does not decode back to the URL. Do not use it.")
