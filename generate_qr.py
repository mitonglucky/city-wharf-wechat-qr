#!/usr/bin/env python3
"""Generate a printable QR code pointing to your City Wharf landing page."""
import argparse
import qrcode

parser = argparse.ArgumentParser(description="Generate the permanent City Wharf QR code.")
parser.add_argument("url", help="Your published GitHub Pages URL, e.g. https://USERNAME.github.io/REPOSITORY/")
parser.add_argument("-o", "--output", default="city-wharf-permanent-qr.png", help="Output PNG filename")
args = parser.parse_args()

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=16,
    border=4,
)
qr.add_data(args.url)
qr.make(fit=True)
image = qr.make_image(fill_color="black", back_color="white")
image.save(args.output)
print(f"QR code saved to: {args.output}")
print(f"Encoded URL: {args.url}")
