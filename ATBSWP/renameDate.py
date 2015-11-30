# renameDate.py - rename file name with american MM-DD_YYYY format to European date format DD-MM-YYYY

import shutil, os, re

date_pattern = re.compile(r'''^(.*?)              # All text before the date
                         ((0|1)?\d)-              # 1 or 2 digit for months
                         ((0|1|2|3)?\d)-          # 1 or 2 digit for date
                         ((19|20)?\d\d)           # four digit for year
                         (.*?)$                   # All text after the date.
                         ''', re.VERBOSE)

# TODO : Loop over the file in working directory

for americanFileName in os.listdir('.'):
    mo = date_pattern.search(americanFileName)

    # TODO : Skip files without a date.
    if mo is None:
        continue
    # TODO : Get different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    datePart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # TODO : Form the European style filename.
    euroFileName = beforePart + datePart + '-' + monthPart + '-' + yearPart + afterPart

    # TODO : Get the full absolute path.
    getAbsolutePath = os.path.abspath('.')
    americanFileName = os.path.join(getAbsolutePath, americanFileName)
    euroFileName = os.path.join(getAbsolutePath, euroFileName)

    # TODO : Rename the files.
    print('renaming the file from %s to %s' % (americanFileName, euroFileName))
    shutil.move(americanFileName, euroFileName)
