import os

PATH = os.getcwd()
print(f"This is folder location: {PATH}")

image_file = os.path.join(PATH, 'wallet-1.png')
print(image_file)