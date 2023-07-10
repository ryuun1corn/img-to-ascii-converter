from configparser import ConfigParser
import cv2 as cv

config = ConfigParser()
config.read("converter_config.ini")
config_data =config["DEFAULT"]

def ascii_converter(intensity):
    ascii="@%#*+=-."
    return ascii[int(intensity/256*8)]
    # return(str(intensity))

path = str(input("Insert the name of file (with extension): "))
img =cv.imread(path, cv.IMREAD_GRAYSCALE)
new_width=int(img.shape[1]*0.5)
new_height=int(img.shape[0]*0.5*float(config_data["width_to_height_ratio"]))
min_width=int(config_data["image_width"]) # Variable for the desired image width
min_height=int(min_width*new_height/new_width)
smaller = cv.resize(img, (min_width,min_height))
for i in range(min_height):
    ascii_string=""
    for j in range(min_width):
        ascii_string+=ascii_converter(smaller[i][j])
    print(ascii_string)