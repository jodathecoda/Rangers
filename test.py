import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

def display_tab_content(tab_num):
    selected_value = int(selected_option[tab_num-1].get())
    image_path = image_paths[tab_num-1][selected_value-1]
    img = Image.open(image_path)
    photo = ImageTk.PhotoImage(img)
    image_labels[tab_num-1].config(image=photo)
    image_labels[tab_num-1].image = photo

def show_random_number():
    random_num = random.randint(1, 100)
    random_button.config(text=f"Rand: {random_num} %")

root = tk.Tk()
root.title("Tabs with Radio Buttons and Images Example")

# Set the size of the window
root.geometry("600x600")  # Width x Height

# Create a Notebook widget
notebook = ttk.Notebook(root)

# Create tabs
tabs = []
selected_option = []
image_paths = [
    ["image1_option1.png", "image1_option2.png", "image1_option3.png", "image1_option4.png", "image1_option5.png"],
    ["image2_option1.png", "image2_option2.png", "image2_option3.png", "image2_option4.png", "image2_option5.png"],
    ["image3_option1.png", "image3_option2.png", "image3_option3.png", "image3_option4.png", "image3_option5.png"],
    ["image4_option1.png", "image4_option2.png", "image4_option3.png", "image4_option4.png", "image4_option5.png"]
]

image_labels = []

for i in range(1, 5):
    bb = 0
    tab = ttk.Frame(notebook)
    tabs.append(tab)
    if i == 1:
        bb = 20
    elif i == 2:
        bb = 15
    elif i == 3:
        bb = 10
    else:
        bb = 7
    notebook.add(tab, text=f'{bb} BB')

    # Create radio buttons within each tab
    selected_option.append(tk.StringVar(value="0"))
    for j in range(1, 6):
        radio_button = tk.Radiobutton(tab, text=f"Option {j}", variable=selected_option[-1], value=str(j),
                                      command=lambda t=i, v=j: display_tab_content(t))
        radio_button.grid(row=j-1, column=0, pady=5, sticky="w")

    # Image label in each tab
    img = Image.open(image_paths[i-1][0])  # Display the first image initially
    photo = ImageTk.PhotoImage(img)
    image_label = tk.Label(tab, image=photo)
    image_label.image = photo
    image_label.grid(row=0, column=1, rowspan=5, padx=10)
    image_labels.append(image_label)

# Pack the Notebook widget with fill set to 'both'
notebook.pack(expand=True, fill='both', padx=10, pady=10)

# Random number button at the bottom
random_button = tk.Button(root, text="Rand: 0 %", command=show_random_number)
random_button.pack(side="bottom", pady=10)

root.mainloop()
