import tkinter as tk

root = tk.Tk()

root.title("Image to text")
root.geometry("500x500")
root.config(background="white")

label_file_explorer = tk.Label(root, text="File explorer", width=100, height=4, fg="blue")

def browse_files():
    filename = tk.filedialog.askopenfilename(
                    initialdir="/", 
                    title="Select an image", 
                    filetypes=(("Text files", "*.txt"), ("all files", "*.*"))
    )
    label_file_explorer.configure(text="File Opened : " + filename)

explore_button = tk.Button(root, text = "Browse Files", command = browse_files)
exit_button = tk.Button(root, text = "Exit", command = exit)

label_file_explorer.grid(column=1, row=1)
explore_button.grid(column=1, row=2)
exit_button.grid(column=1, row=3)

root.mainloop()