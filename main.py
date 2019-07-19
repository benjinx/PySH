#!/usr/bin/env python3
import os
import re

builtin = { }
cwd = "./"

def cmdExit(args):
    exit()

builtin['exit'] = cmdExit

def cmdEcho(args):
    print(" ".join(args))

builtin['echo'] = cmdEcho

def cmdEnv(args):
    for k, v in os.environ.items():
        print("{}={}".format(k, v))

builtin['env'] = cmdEnv

def process(line):
    def repl(m):
        return os.getenv(m.group(1))
    return re.sub(r'\$([a-zA-Z_][a-zA-Z0-9_]*)', repl, line)

def main():
    global builtin
    while True:
        line = input("$ ")
        args = process(line).split(" ")

        if len(args) == 0:
            continue

        if args[0] in builtin:
            builtin[args[0]](args[1:])
        else:
            print("Command '{}' not found".format(args[0]))
        
if __name__ == "__main__":
    main()
