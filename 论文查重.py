import jieba
import sys
import math
class WordsCounter:
    def __init__(self,origPath,repliPath,outPath):
        self.words = {}
        self.origPath = origPath
        self.repliPaht = repliPath
        self.outPath = outPath
        self.replication = 0
    def countWords(self):
        f1 = open(self.origPath,'r')
        f2 = open(self.repliPath,'r')
        paragraph1 = f1.read()
        paragraph2 = f2.read()
        seg_words1 = jieba.cut(paragraph1)
        seg_words2 = jieba.cut(paragraph2)
        for word in seg_words1:
            if(word in self.words):
                self.words[word][0]+=1
            else:
                self.words[word]=[1,0]
        for word in seg_words2:
            if(word in self.words):
                self.words[word][1]+=1
            else:
                self.words[word]=[0,1]
        f1.close()
        f2.close()
    def calculateReplication(self):
        innerProduct = 0
        modular1 = 0
        modular2 = 0
        for word in self.words:
            innerProduct += word[0]*word[1]
            modular1 += word[0]*word[0]
            modular2 += word[1]*word[1]
        self.replication = innerProduct/(math.sqrt(modular1)*math.sqrt(modular2))
    def outReplication(self):
        f = open(self.outPath,"w")
        f.write(self.replication)
        f.close()
if __name__=='__main__':
    if(len(sys.argv)!=4):
        sys.exit(1)
    wordsCounter = WordsCounter(sys.argv[1],sys.argv[1],sys.argv[1])
    wordsCounter.countWords()
    wordsCounter.calculateReplication()
    wordsCounter.outReplication()
    
