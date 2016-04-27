class FileReader:
  def __init__(self, filePath):
    self.inputFile = open(filePath, 'r')

  def read(self, fileParser):
    for line in self.inputFile:
      fileParser(line.decode('utf-8').strip('\n'))
    self.stop()

  def stop(self):
    self.inputFile.close()


def readAsString(filePath):
  return "\n".join(readAsList(filePath))

def readAsList(filePath):
  r = FileReader(filePath)
  res = [ ]
  r.read(lambda l: res.append(l))
  return res
