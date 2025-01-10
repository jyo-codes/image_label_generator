
import tkinter as tk
from PIL import Image, ImageTk
import json
import os

def display_image_with_labels(image_path, labels_file):
    """
    Display an image with labels in a GUI window.

    Parameters:
    image_path (str): Path to the image file.
    labels_file (str): Path to the JSON file containing labels.

    Returns:
    None
    """
    window = tk.Tk()
    window.title("Image Labels")

    img = Image.open(image_path)
    img = img.resize((600, 400))
    photo = ImageTk.PhotoImage(img)

    canvas = tk.Canvas(window, width=600, height=400)
    canvas.pack()
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    with open(labels_file, 'r') as f:
        labels = json.load(f)
        y_offset = 20
        for label in labels['labels']:
            text = f"{label['Name']} ({label['Confidence']:.2f}%)"
            canvas.create_text(10, y_offset, anchor=tk.W, text=text, fill="red")
            y_offset += 20

    window.mainloop()
