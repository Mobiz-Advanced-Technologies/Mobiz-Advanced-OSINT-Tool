import tkinter as tk
import ttkbootstrap as ttk
import subprocess
from tkinter import filedialog
from tkinter import messagebox

def aboutWindow():
	messagebox.showinfo("About","Mobiz-Advanced-OSINT-Tool v1.0.\n©2023 Mobiz-Advanced-Technologies")

def checkEmail():
	# Run holehe
	try:
		result = subprocess.run(['holehe', email_field.get()], stdout=subprocess.PIPE)
	except OSError as e:
		messagebox.showinfo("Error","An error occurred! Make sure you are connected to the internet and have the Holehe Python package installed.")
		return

	# Get And Cut Information
	output_lines = result.stdout.decode().split('\n')
	cut_lines = 7
	cut_end = -4
	new_output = '\n'.join(output_lines[cut_lines:cut_end])

	results_field.insert(tk.END, new_output)

def saveLog():
	# File Dialog
	file = filedialog.asksaveasfile(defaultextension = '.txt',
									filetypes = [
										("Text File", ".txt"),
										("HTML File", ".htm"),
										("All Files", ".*"),
									])

	# Check if file dialog is closed
	if file is None:
		return

	# If not then write to file
	filetext = str(results_field.get('1.0', tk.END))
	file.write(filetext)
	file.close()

# Create Window
master = ttk.Window(themename = 'solar')
master.title('Mobiz-Advanced-OSINT-Tool')
master.geometry('400x450')
master.resizable(False, False)
master.iconbitmap('logo.ico')

# Title Bar Buttons
mainmenu = ttk.Menu(master)
mainmenu.add_command(label = "Save", command = saveLog)
mainmenu.add_command(label = "About", command = aboutWindow)
master.config(menu = mainmenu)

# Create Field
frame = ttk.Frame(master = master)
email_field = ttk.Entry(master = frame, width = 48)
email_field.insert(0, 'test@example.com')
submit_button = ttk.Button(master = frame, text = 'Search', command = checkEmail)
email_field.pack(side = 'left')
submit_button.pack(side = 'left')
frame.pack(pady = 20)

# Create Results Field
results_field = ttk.Text(master = master)
results_field.pack(padx = 20, pady = (0,20))
results_field.insert(tk.END, 'Mobiz-Advanced-OSINT-Tool v1.0.\n©2023 Mobiz-Advanced-Technologies\n\n')

master.mainloop()