import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

img = None
watermark_img = None
img_lb = None
mark_en = None
mark_btn = None
download_btn = None


def view_img(image):
    global img_lb
    width, height = image.size
    if width > 4000 or height > 4000:
        x, y = width//11, height//11
    elif width > 3500 or height > 3500:
        x, y = width//9, height//9
    elif width > 3000 or height > 3000:
        x, y = width//8, height//8
    elif width > 2500 or height > 2500:
        x, y = width//7, height//7
    elif width > 2000 or height > 2000:
        x, y = width//5, height//5
    elif width > 1500 or height > 1500:
        x, y = width//4, height//4
    else:
        x, y = width//3, height//3
    resized_img = ImageTk.PhotoImage(image.resize((x, y)))
    img_lb = tkinter.Label()
    img_lb.grid(row=3, column=1)
    img_lb.image = resized_img
    img_lb['image'] = resized_img


def clear_window():
    global img, img_lb, mark_en, mark_btn, download_btn
    to_destroy = [img_lb, mark_en, mark_btn, download_btn]
    for item in to_destroy:
        if item is not None:
            item.destroy()


def upload_file():
    global img, img_lb, mark_en, mark_btn, download_btn
    clear_window()
    f_types = [('Image Files', ['*.jpg', '*.jpeg', '*.png'])]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)
    mark_en = tkinter.Entry(width=40)
    mark_en.grid(row=4, column=1)
    view_img(img)
    mark_btn = tkinter.Button(text="Watermark", command=watermarking)
    mark_btn.grid(row=5, column=1)


def watermarking():
    global img, watermark_img, img_lb, mark_en, mark_btn, download_btn
    if img is not None:
        mark_sentence = mark_en.get()
        clear_window()
        watermark_img = img.copy()
        draw = ImageDraw.Draw(watermark_img)
        width, height = watermark_img.size
        font = ImageFont.truetype("arial.ttf", width//10)
        c_x = width//2 - len(mark_sentence) * width//50
        c_y = height//2 - height//10
        draw.text((c_x, c_y), mark_sentence, font=font, fill=(230, 230, 230))
        view_img(watermark_img)
        download_btn = tkinter.Button(text="Download", command=download_img)
        download_btn.grid(row=4, column=1)


def download_img():
    global watermark_img, download_btn
    if download_btn is not None:
        clear_window()
        f_type = [("Jpg Files", "*.jpg")]
        filename = filedialog.asksaveasfilename(filetypes=f_type)
        watermark_img.save(filename + ".jpg")


window = tkinter.Tk()
window.title("Watermark on Image")
window.geometry("900x1000")
window.config(padx=230, pady=50)

title_lb = tkinter.Label(text="Choose Image File", font=("Arial", 40, "bold"))
title_lb.grid(row=1, column=1)

find_btn = tkinter.Button(text="Find Image", command=upload_file)
find_btn.grid(row=2, column=1)


window.mainloop()