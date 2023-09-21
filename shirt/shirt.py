from PIL import Image, ImageOps
import sys


def main():
    copy_and_paste_images()


def copy_and_paste_images():
    extensions_list = []
    try:
        for file_names in sys.argv:
            string_file_names = str(file_names)
            name, extensions = string_file_names.split(".")
            extensions_list.append(extensions)
    except(ValueError):
        sys.exit(f'"{sys.argv[1]}" or "{sys.argv[2]}" is not an image file')
    if len(sys.argv) > 3:
        sys.exit("too many command line arguments")
    if len(sys.argv) < 3:
        sys.exit("too few command line arguments")
    if extensions_list[1] != extensions_list[2]:
        sys.exit("input and output have different extensions")
    else:
        Imagefile = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        size = shirt.size
        muppet = ImageOps.fit(Imagefile, size)
        muppet.paste(shirt, shirt)
        muppet.save(sys.argv[2])


if __name__ == "__main__":
    main()