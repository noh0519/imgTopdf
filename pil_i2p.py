import sys
from PIL import Image

def convert_jpgs_to_pdf(jpg_files, output_pdf="output.pdf"):
    images = []

    # sort file list by filename assuming they are named like '1.jpg', '2.jpg', etc.
    jpg_files.sort(key=lambda x: int(x.split('/')[-1].split('.')[0]))

    for file in jpg_files:
        try:
            img = Image.open(file).convert("RGB")
            images.append(img)
        except Exception as e:
            print(f"Error loading {file}: {e}")

    if images:
        first_image = images[0]
        rest_images = images[1:]
        first_image.save(output_pdf, save_all=True, append_images=rest_images)
        print(f"Saved PDF as {output_pdf}")
    else:
        print("No valid images to convert.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pil_j2p.py image1.jpg image2.jpg ...")
    else:
        convert_jpgs_to_pdf(sys.argv[1:])