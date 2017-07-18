import os

os.system('cls' if os.name == 'nt' else 'clear')

oldfile = input('{*} Enter the file (with extension) you would like to strip domains from: ')
newfile = input('{*} Enter the name of the file (with extension) you would like me to save: ')

linesToRemove = ['PART NUMBER......', 'Inventory  items', 'Press any key to continue...', 'SALE 12mo.']

print("\n[*] This script will remove records that contain the following strings: \n\n", linesToRemove)

input("\n[!] Press any key to start...\n")

linecounter = 0

with open(oldfile, encoding="utf-8", errors='ignore') as oFile, open(newfile, 'w') as nFile:
    for line in oFile:
        if not any(domain in line for domain in linesToRemove):
            nFile.write(line)
            linecounter = linecounter + 1
            print('[*] - {%s} Writing verified record to %s ---{ %s' % (linecounter, newfile, line))

print('[*] === COMPLETE === [*]')
print('[*] %s was saved' %newfile)
print('[*] There are %s records in your saved file.' %linecounter)