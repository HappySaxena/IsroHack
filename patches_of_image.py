from PIL import Image
import os

# Load large image
img = Image.open("img1.png")

patch_size = 1024  # Patch size you want
overlap = 0

W, H = img.size

output_dir = "patches"
os.makedirs(output_dir, exist_ok=True)

count = 0
for top in range(0, H, patch_size - overlap):
    for left in range(0, W, patch_size - overlap):
        right = left + patch_size
        bottom = top + patch_size

        # Crop actual image area (might be smaller if beyond edges)
        crop_right = min(right, W)
        crop_bottom = min(bottom, H)

        patch = img.crop((left, top, crop_right, crop_bottom))

        # Pad if needed
        pad_width = patch_size - patch.size[0]
        pad_height = patch_size - patch.size[1]

        if pad_width > 0 or pad_height > 0:
            new_patch = Image.new("RGB", (patch_size, patch_size), (0, 0, 0))
            new_patch.paste(patch, (0, 0))
            patch = new_patch

        patch.save(f"{output_dir}/patch_{count}.png")
        count += 1

print(f"Saved {count} patches.")
