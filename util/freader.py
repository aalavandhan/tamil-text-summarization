class FileReader:
  def __init__(self, filePath):
    self.inputFile = open(filePath, 'r')

  def read(self, fileParser):
    for line in self.inputFile:
      fileParser(line.decode('utf-8').strip('\n'))
    self.stop()

  def stop(self):
    self.inputFile.close()
