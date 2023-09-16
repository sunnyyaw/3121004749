import jieba
import sys
import math
class WordsCounter:
    def __init__(self,origPath,repliPath,outPath):
        self.words = {}
        self.origPath = origPath
        self.repliPath = repliPath
        self.outPath = outPath
        self.replication = 0
    def countWords(self):
        # 清空词袋
        self.words.clear()
        # 读取文件
        try:
            f1 = open(self.origPath,'r')
            f2 = open(self.repliPath,'r')
        except Exception as e:
            print(e)
            raise
        paragraph1 = f1.read()
        paragraph2 = f2.read()
        # 用jieba库进行分词
        seg_words1 = jieba.cut(paragraph1)
        seg_words2 = jieba.cut(paragraph2)
        # 计算词频
        for word in seg_words1:
            if(word not in self.words):
                self.words[word]=[1,0]
            else:
                self.words[word][0]+=1
        for word in seg_words2:
            if(word not in self.words):
                self.words[word]=[0,1]
            else:
                self.words[word][1]+=1
        f1.close()
        f2.close()
    def calculateReplication(self):
        # 计算文章余弦相似度
        innerProduct = 0
        modular1 = 0
        modular2 = 0
        for value in self.words.values():
            innerProduct += value[0]*value[1]
            modular1 += value[0]*value[0]
            modular2 += value[1]*value[1]
        if(innerProduct!=0):
            self.replication = innerProduct/(math.sqrt(modular1)*math.sqrt(modular2))
    def outReplication(self):
        # 将相似度输出至文件
        try:
            f = open(self.outPath,"w")
        except Exception as e:
            print(e)
            raise
        f.write(str(self.replication))
        f.close()
def main():
    if(len(sys.argv)<4):
        raise Exception("参数数目不足")
    wordsCounter = WordsCounter(sys.argv[1],sys.argv[2],sys.argv[3])
    wordsCounter.countWords()
    wordsCounter.calculateReplication()
    wordsCounter.outReplication()
if __name__=='__main__':
    main()
