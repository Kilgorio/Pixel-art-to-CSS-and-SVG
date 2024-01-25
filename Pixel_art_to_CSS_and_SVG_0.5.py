<<<<<<< HEAD
from PIL import Image
import numpy as np
import os
from pathlib import Path
from tkinter import Tk, Label, Entry, Button, filedialog, PhotoImage, OptionMenu, StringVar

output_file = "pixel_art.css"

window = Tk()
window.title("Pixel Art To CSS")
window.geometry("680x400")

conversion_function = StringVar()
conversion_function.set("CSS")

round_button1 = PhotoImage(file="./img/round_button1.png")
round_button2 = PhotoImage(file="./img/round_button2.png")
round_button3 = PhotoImage(file="./img/round_button3.png")

window.config(bg="#202123")

light_shadow = "#4d4d4d"
dark_shadow = "#424549"
element_bg = "#202123"

input_label = Label(window, text="Input image path:")
input_label.grid(row=0, column=0, padx=10, pady=10)

input_label.config(bg=element_bg, fg="white", font=("Arial", 12, "bold"))
input_label.config(relief="flat", bd=0)
input_label.config(highlightbackground=light_shadow, highlightcolor=light_shadow)
input_label.config(highlightbackground=dark_shadow, highlightcolor=dark_shadow)

input_entry = Entry(window, width=40)
input_entry.grid(row=0, column=1, padx=10, pady=10)

input_entry.config(bg=element_bg, fg="white", font=("Arial", 12))
input_entry.config(relief="flat", bd=0)
input_entry.config(highlightthickness=4)
input_entry.config(highlightbackground=light_shadow, highlightcolor=light_shadow)
input_entry.config(highlightbackground=dark_shadow, highlightcolor=dark_shadow)

# function to select the input file
def select_input():
    global input_file
    input_file = filedialog.askopenfilename()
    input_entry.delete(0, "end")
    input_entry.insert(0, input_file)

input_button = Button(window, text="Select", command=select_input, image=round_button1, borderwidth=0, height=67, width=116)
input_button.grid(row=0, column=2, padx=10, pady=10)
input_button.config(highlightthickness=0)

output_label = Label(window, text="Output path:")
output_label.grid(row=1, column=0, padx=10, pady=10)

output_label.config(bg=element_bg, fg="white", font=("Arial", 12, "bold"))
output_label.config(relief="flat", bd=0)
output_label.config(highlightbackground=light_shadow, highlightcolor=light_shadow)
output_label.config(highlightbackground=dark_shadow, highlightcolor=dark_shadow)

output_entry = Entry(window, width=40)
output_entry.grid(row=1, column=1, padx=10, pady=10)

output_entry.config(bg=element_bg, fg="white", font=("Arial", 12))
output_entry.config(relief="flat", bd=0)
output_entry.config(highlightthickness=4)
output_entry.config(highlightbackground=light_shadow, highlightcolor=light_shadow)
output_entry.config(highlightbackground=dark_shadow, highlightcolor=dark_shadow)

conversion_function_menu = OptionMenu(window, conversion_function, "CSS", "SVG")
conversion_function_menu.grid(row=2, column=0, sticky='ew', padx=10, pady=10)
conversion_function_menu.config(highlightthickness=0, bg="#4d4d4d", borderwidth=0, fg="white", activebackground="#101113", activeforeground="white")
conversion_function_menu["menu"].config(bg="#4d4d4d", fg="white")

# function to select the output file
def select_output():
    global output_file
    conversion_choice = conversion_function.get()
    file_ext = ".css" if conversion_choice == "CSS" else ".svg"
    output_file = filedialog.asksaveasfilename(defaultextension=file_ext)
    output_entry.delete(0, "end")
    output_entry.insert(0, output_file)

output_button = Button(window, text="Select", command=select_output, image=round_button1, borderwidth=0, height=67, width=116)
output_button.grid(row=1, column=2, padx=10, pady=10)
output_button.config(highlightthickness=0)

def pixelart2css():
    # Load the image and convert it to RGB mode
    try:
        img = Image.open(input_file).convert("RGB")
    except ValueError:
        raise ValueError("Invalid input. Please select an image file.")

    width, height = img.size

    pixels = np.array(img)

    css = ".pixelart-to-css {\n box-shadow: "

    # Loop through each row of pixels
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[y, x]
            hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
            css += "{}px {}px 0 0 {}, ".format(x, y, hex)

    css = css[:-2] + "; \n height: 10px;\n width: 10px;\n}"

    # Write the CSS code to the output file
    with open(output_file, "w") as f:
        f.write(css)

    print("The CSS code for the pixel art image has been written to {}".format(output_file))

def pixelart2svg():
    # Load the image and convert it to RGB mode
    try:
        img = Image.open(input_file).convert("RGB")
    except ValueError:
        raise ValueError("Invalid input. Please select an image file.")

    width, height = img.size

    pixels = np.array(img)

    svg = '<?xml version="1.0" encoding="UTF-8"?>\n'
    svg += '<svg width="{}" height="{}" xmlns="http://www.w3.org/2000/svg">\n'.format(width, height)

    # Loop through each row of pixels
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[y, x]
            hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
            svg += '<rect x="{}" y="{}" width="1" height="1" fill="{}"/>\n'.format(x, y, hex)

    svg += '</svg>'

    # Write the SVG code to the output file
    with open(output_file, "w") as f:
        f.write(svg)

    print("The SVG code for the pixel art image has been written to {}".format(output_file))


generate_button = Button(window, text="Generate", command=lambda: generate_pixel_art(conversion_function.get()), image=round_button2, borderwidth=0, height=67, width=138)
generate_button.grid(row=3, column=1, padx=10, pady=10)
generate_button.config(highlightthickness=0)

def generate_pixel_art(conversion_choice):
    if conversion_choice == "CSS":
        pixelart2css()
    elif conversion_choice == "SVG":
        pixelart2svg()

def exit_program():
    window.destroy()

exit_button = Button(window, text="Exit", command=exit_program, image=round_button3, borderwidth=0, height=67, width=116)
exit_button.grid(row=4, column=1, padx=10, pady=10)
exit_button.config(highlightthickness=0)

window.mainloop()
=======
from PIL import Image
import numpy as np
import os
from pathlib import Path
from tkinter import Tk, Label, Entry, Button, filedialog, PhotoImage, OptionMenu, StringVar

output_file = "pixel_art.css"

window = Tk()
window.title("Pixel Art To CSS")
window.geometry("680x400")

conversion_function = StringVar()
conversion_function.set("CSS")

round_button1 = PhotoImage(file="./img/round_button1.png")
round_button2 = PhotoImage(file="./img/round_button2.png")
round_button3 = PhotoImage(file="./img/round_button3.png")

window.config(bg="#202123")

light_shadow = "#4d4d4d"
dark_shadow = "#424549"
element_bg = "#202123"

input_label = Label(window, text="Input image path:")
input_label.grid(row=0, column=0, padx=10, pady=10)

input_label.config(bg=element_bg, fg="white", font=("Arial", 12, "bold"))
input_label.config(relief="flat", bd=0)
input_label.config(highlightbackground=light_shadow, highlightcolor=light_shadow)
input_label.config(highlightbackground=dark_shadow, highlightcolor=dark_shadow)

input_entry = Entry(window, width=40)
input_entry.grid(row=0, column=1, padx=10, pady=10)

input_entry.config(bg=element_bg, fg="white", font=("Arial", 12))
input_entry.config(relief="flat", bd=0)
input_entry.config(highlightthickness=4)
input_entry.config(highlightbackground=light_shadow, highlightcolor=light_shadow)
input_entry.config(highlightbackground=dark_shadow, highlightcolor=dark_shadow)

# function to select the input file
def select_input():
    global input_file
    input_file = filedialog.askopenfilename()
    input_entry.delete(0, "end")
    input_entry.insert(0, input_file)

input_button = Button(window, text="Select", command=select_input, image=round_button1, borderwidth=0, height=67, width=116)
input_button.grid(row=0, column=2, padx=10, pady=10)
input_button.config(highlightthickness=0)

output_label = Label(window, text="Output path:")
output_label.grid(row=1, column=0, padx=10, pady=10)

output_label.config(bg=element_bg, fg="white", font=("Arial", 12, "bold"))
output_label.config(relief="flat", bd=0)
output_label.config(highlightbackground=light_shadow, highlightcolor=light_shadow)
output_label.config(highlightbackground=dark_shadow, highlightcolor=dark_shadow)

output_entry = Entry(window, width=40)
output_entry.grid(row=1, column=1, padx=10, pady=10)

output_entry.config(bg=element_bg, fg="white", font=("Arial", 12))
output_entry.config(relief="flat", bd=0)
output_entry.config(highlightthickness=4)
output_entry.config(highlightbackground=light_shadow, highlightcolor=light_shadow)
output_entry.config(highlightbackground=dark_shadow, highlightcolor=dark_shadow)

conversion_function_menu = OptionMenu(window, conversion_function, "CSS", "SVG")
conversion_function_menu.grid(row=2, column=0, sticky='ew', padx=10, pady=10)
conversion_function_menu.config(highlightthickness=0, bg="#4d4d4d", borderwidth=0, fg="white", activebackground="#101113", activeforeground="white")
conversion_function_menu["menu"].config(bg="#4d4d4d", fg="white")

# function to select the output file
def select_output():
    global output_file
    conversion_choice = conversion_function.get()
    file_ext = ".css" if conversion_choice == "CSS" else ".svg"
    output_file = filedialog.asksaveasfilename(defaultextension=file_ext)
    output_entry.delete(0, "end")
    output_entry.insert(0, output_file)

output_button = Button(window, text="Select", command=select_output, image=round_button1, borderwidth=0, height=67, width=116)
output_button.grid(row=1, column=2, padx=10, pady=10)
output_button.config(highlightthickness=0)

def pixelart2css():
    # Load the image and convert it to RGB mode
    try:
        img = Image.open(input_file).convert("RGB")
    except ValueError:
        raise ValueError("Invalid input. Please select an image file.")

    width, height = img.size

    pixels = np.array(img)

    css = ".pixelart-to-css {\n box-shadow: "

    # Loop through each row of pixels
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[y, x]
            hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
            css += "{}px {}px 0 0 {}, ".format(x, y, hex)

    css = css[:-2] + "; \n height: 10px;\n width: 10px;\n}"

    # Write the CSS code to the output file
    with open(output_file, "w") as f:
        f.write(css)

    print("The CSS code for the pixel art image has been written to {}".format(output_file))

def pixelart2svg():
    # Load the image and convert it to RGB mode
    try:
        img = Image.open(input_file).convert("RGB")
    except ValueError:
        raise ValueError("Invalid input. Please select an image file.")

    width, height = img.size

    pixels = np.array(img)

    svg = '<?xml version="1.0" encoding="UTF-8"?>\n'
    svg += '<svg width="{}" height="{}" xmlns="http://www.w3.org/2000/svg">\n'.format(width, height)

    # Loop through each row of pixels
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[y, x]
            hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
            svg += '<rect x="{}" y="{}" width="1" height="1" fill="{}"/>\n'.format(x, y, hex)

    svg += '</svg>'

    # Write the SVG code to the output file
    with open(output_file, "w") as f:
        f.write(svg)

    print("The SVG code for the pixel art image has been written to {}".format(output_file))


generate_button = Button(window, text="Generate", command=lambda: generate_pixel_art(conversion_function.get()), image=round_button2, borderwidth=0, height=67, width=138)
generate_button.grid(row=3, column=1, padx=10, pady=10)
generate_button.config(highlightthickness=0)

def generate_pixel_art(conversion_choice):
    if conversion_choice == "CSS":
        pixelart2css()
    elif conversion_choice == "SVG":
        pixelart2svg()

def exit_program():
    window.destroy()

exit_button = Button(window, text="Exit", command=exit_program, image=round_button3, borderwidth=0, height=67, width=116)
exit_button.grid(row=4, column=1, padx=10, pady=10)
exit_button.config(highlightthickness=0)

window.mainloop()
>>>>>>> a023e8e (Initial Upload)
