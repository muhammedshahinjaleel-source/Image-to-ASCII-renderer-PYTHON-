from PIL import Image
import tkinter as tk

raw = " "
root = tk.Tk()
root.geometry("600x600")
root.configure(bg="black")

charsList = []


textbox = tk.Text(root, padx = 30,height=2, font=('Ariel', 19))
textbox.pack()

def render(inputPath):
      charsList.clear()
      print("beginning render")
      img = Image.open(str(inputPath))
      width, height = img.size
      x = width
      y = height

      comp_factorX = 4
      comp_factorY = 4
      gray = img.convert('L')

      
      for j in range(y):
            if j%comp_factorY== 0:
                  for i in range(x):
                        if i%comp_factorX== 0:
                              pixel_value = gray.getpixel((i, j))

                              chars = " .:-=+*#%@"
                              ascii_char = chars[pixel_value * len(chars) // 256]
                              charsList.append(ascii_char)
                              #text.write(ascii_char )

                  charsList.append("\n")           
                  #text.write("\n")
      
      print("ASCII art created successfully!")

      asciiString = " ".join(charsList)
      label = tk.Label(root, padx= 20, pady=10, text = asciiString, bg="black",fg= "white", font=('Ariel',1) )
      label.pack()      
      


def getInput():
      raw = textbox.get("1.0",'end-1c')
      print("path selected")
      if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
            raw = raw[1:-1]
      inputPath = raw.replace("\\", "/")
      render(inputPath)
      

convertButton = tk.Button(root, text= "CONVERT", command=lambda: getInput())
convertButton.pack()


root.mainloop()



