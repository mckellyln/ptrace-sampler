#!/usr/bin/python

import sys

from sample_reader import parseFile


outFd = None

def handleEvent (e):
    #print e

    for f in e[1]:
        if f[3] is not None:
            outFd.write("fl=%s\n" % f[3])
            outFd.write("fn=%s\n" % f[2])
            outFd.write("%d %d 0\n" % (f[4], 1))
            break

    for f in e[1]:
        if f[3] is not None:
            outFd.write("fl=%s\n" % f[3])
            outFd.write("fn=%s\n" % f[2])
            outFd.write("%d 0 %d\n" % (f[4], 1))

    #sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: %s <sample data file>" % sys.argv[0]
        sys.exit(1)

    sampleFile = sys.argv[1]

    outFd = open("calltree.%s" % sampleFile, "w")

    outFd.write("# callgrind output file, generated by '%s'\n" % sys.argv)
    outFd.write("events: NumSamples NumIncSamples\n")

    parseFile(sampleFile, handleEvent)

