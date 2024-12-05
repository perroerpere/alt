import tkinter as tk

window = tk.Tk()

window.title("GUI Elements")

label1 = tk.Label(text="Label 1")
label2 = tk.Label(text="Label 2", bg="red", fg="white")
label3 = tk.Label(text="Label 3", bg="yellow", width="10", height="5")
button = tk.Button(text="Button!", width="7", height="2")
entry = tk.Entry(width="15")
textbox = tk.Text()

label1.pack()
label2.pack()
label3.pack()
button.pack()
entry.pack()
textbox.pack()

window.mainloop()