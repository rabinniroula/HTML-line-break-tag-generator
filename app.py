import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()

# args.file
filename = args.file

f = open(filename, 'r', encoding="utf-8")

pre = ""
orig = f.read()

for letter in orig:
    if letter == '\n':
        pre = pre + '<br>\n'
    else:
        pre = pre + letter

print("Enter the filename to save as: ")
filename = input()

f = open(filename, 'w', encoding="utf-8")
f.write(pre)

print("done!")
