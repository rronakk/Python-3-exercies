"""Program which allows user to add bullet point in front of each line"""
import pyperclip

text = pyperclip.paste()

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = "* " + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
