def countWordsFromFile():
  filePath = input("Enter the path to your file")
  readFile = open(filePath, 'r')
  noOfWords = 0
  for line in readFile:
    words = line.split()
    noOfWords = noOfWords + len(words)
  print("Number of words: ", noOfWords)

countWordsFromFile()