from PIL import Image
import tkinter as tk
from tkinter import filedialog

raw = " "
root = tk.Tk()
root.title("IMAGE TO ASCII RENDERER by Shahin")
root.geometry("600x600")
root.configure(bg="black")

charsList = []

raw = filedialog.askopenfilename(title="Pick a file: ", filetypes=[(".jpg",".png")])

def render(inputPath):
      charsList.clear()
      print("beginning render")
      img = Image.open(str(inputPath))
      width, height = img.size
      x = width
      y = height

      comp_factorX = 1
      comp_factorY = 1
      gray = img.convert('L')

      
      for j in range(y):
            if j%comp_factorY== 0:
                  for i in range(x):
                        if i%comp_factorX== 0:
                              pixel_value = gray.getpixel((i, j))

                              chars = " .:-=+*#%@"
                              ascii_char = chars[pixel_value * len(chars) // 256]
                              charsList.append(ascii_char)

                  charsList.append("\n")           
      
      print("ASCII art created successfully!")

      asciiString = " ".join(charsList)
      label = tk.Label(root, padx= 20, pady=10, text = asciiString, bg="black",fg= "white", font=('Ariel',1) )
      label.pack()      
      

print("path selected")
inputPath = raw
filepathlabel = tk.Label(root,text=raw, padx = 30,height=2, font=('Ariel', 19))
filepathlabel.pack()

def getInput():
      render(inputPath)
      
convertButton = tk.Button(root, text= "CONVERT", command=lambda: getInput())
convertButton.pack()


root.mainloop()



