import os

folder = r"D:\ComfyUI_windows_portable\ImagesKate\ComfyUI\output\CommonCoversKate_02"

files = sorted([
    f for f in os.listdir(folder)
    if os.path.isfile(os.path.join(folder, f))
])

start = 787

for i, filename in enumerate(files, start=1):
    ext = os.path.splitext(filename)[1]
    new_name = f"Cover_{start:02d}{ext}"

    src = os.path.join(folder, filename)
    dst = os.path.join(folder, new_name)

    os.rename(src, dst)
    start += 1
print("Done")