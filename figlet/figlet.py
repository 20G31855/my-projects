from pyfiglet import Figlet
import sys
import random


figlet = Figlet()
fonts = figlet.getFonts()
if len(sys.argv) == 3:
    input = input("Input:")
    f = Figlet(font=sys.argv[2])
    print(f.renderText(input))
elif len(sys.argv) == 1:
    font_input = input("Input:")
    fonts = figlet.getFonts()
    random = random.choice(fonts)
    f = Figlet(font=random)
    print(f.renderText(font_input))
elif len(sys.argv) > 3:
    sys.exit("too many commmand line arguments")
elif len(sys.argv) == 2:
    sys.exit("you didnt specify a font")
