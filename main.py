import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
parser.add_argument("-t", "--convert", choices=['json', 'text'], help="Convert file into JSON and TEXT")

args = parser.parse_args(sys.argv[1:])

if args.convert:
    if args.convert == "json":
        print(args.file.readlines())
        print("Masuk Json")
    else:
        print(args.file.readlines())
        print("Masuk Text")
else:
    print(args.file.readlines())
    print("Masuke ke text")
    