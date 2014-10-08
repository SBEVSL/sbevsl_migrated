from threading import Thread
from Queue import Queue
import sys

class Logger(Thread):
    def __init__(self, fileStr=None):
        Thread.__init__(self)
        self.setDaemon(True)
        self.queue = Queue()
        if fileStr:
            self.file = open(fileStr, 'w')
            self._write = self.writeToFile
            self.cleanup = self.closeFile
        else:
            self._write = self.writeToStdout
            self.cleanup = self.null

    def run(self):
        try:
            while 1:
                str = self.queue.get(block=True)
                if str == '_':
                    return
                self._write(str)
        finally:
            self.cleanup()

    def write(self, str):
        self.queue.put(str)

    def writeToFile(self, str):
        self.file.write(str)

    def closeFile(self):
        self.file.close()

    def addFile(self, fileStr):
        self.file = open(fileStr, 'w')

    def null(self):
        pass

    def writeToStdout(self, str):
        print str

def main():
    log = Logger('Logger_Test.txt')
    log.start()
    log.write('Logger Successful!')
    sys.exit(0)

if __name__ == '__main__':
    main()
