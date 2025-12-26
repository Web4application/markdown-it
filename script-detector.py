import imghdr
import os

def detect_file_type(file_path):
    # Read first bytes
    with open(file_path, "rb") as f:
        header = f.read(8)

    # Check common signatures
    if header.startswith(b"PK"):
        return "ZIP archive (maybe .xlsx, .docx, .zip)"
    elif header.startswith(b"%PDF"):
        return "PDF document"
    elif header.startswith(b"\x89PNG"):
        return "PNG image"
    elif header.startswith(b"GIF89a") or header.startswith(b"GIF87a"):
        return "GIF image"
    elif header.startswith(b"{") or header.startswith(b"["):
        return "JSON text"
    elif header.startswith(b"<?xml"):
        return "XML text"
    else:
        # Check if it’s an image by imghdr
        image_type = imghdr.what(file_path)
        if image_type:
            return f"{image_type.upper()} image"
        # Fallback: check if mostly readable text
        with open(file_path, "r", errors="ignore") as f:
            sample = f.read(512)
        if all(32 <= ord(c) <= 126 or c in "\r\n\t" for c in sample):
            return "Plain text file"
        return "Unknown binary file"

# Example usage
file_path = "Workbook.clsl"
file_type = detect_file_type(file_path)
print(f"{file_path} is detected as: {file_type}")