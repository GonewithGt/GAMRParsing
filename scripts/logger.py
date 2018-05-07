import sys
import datetime

level = 1
file = sys.stderr

def writeln(s=""):
    s = s.encode(encoding='utf-8')
    file.write("%s\r\n" % s)
    file.flush()

def write(s):
    file.write(s)
    file.flush()
