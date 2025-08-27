from PIL import Image

txt_path = r"C:\Users\etern\OneDrive\Desktop\example.txt"

raw = input("Enter file path: ").strip()
# remove surrounding quotes if user pasted them
if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
    raw = raw[1:-1]

inputPath = raw.replace("\\", "/")
                              
img = Image.open(str(inputPath))


width, height = img.size
x = width
y = height

comp_factorX = 2
comp_factorY = 4

gray = img.convert('L')

with open(txt_path,'w') as text:
      for j in range(y):
            if j%comp_factorY== 0:
                  for i in range(x):
                        if i%comp_factorX== 0:
                              pixel_value = gray.getpixel((i, j))

                              chars = " .:-=+*#%@"
                              ascii_char = chars[pixel_value * len(chars) // 256]
                              text.write(ascii_char )
                              
                  text.write("\n")
                  

print("ASCII art created successfully in the text file.")
