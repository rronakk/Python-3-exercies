# Create a multiClipBoard, where it saves each piece of clipboard text into a keyword.
# Usage : py.exe mcb.pyw save <keyword> - saves keyword to the clipboard.
#         py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#         py.exe list - loads all keyword to clipboard.
#         py.exe del - delete a keyword from the list


import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# save keyword to the clipboard

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # list all keyword & load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':                             # To delete all keyword
        for key in list(mcbShelf.keys()):
            del mcbShelf[key]

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':          # delete a keyword from the list
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
mcbShelf.close()
