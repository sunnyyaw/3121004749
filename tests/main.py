import jieba
import sys
import math
class WordsCounter:
    def __init__(self,origPath,repliPath,outPath):
        self.words = {}
        self.origPath = origPath
        self.repliPath = repliPath
        self.outPath = outPath
        self.reduplication = 0
    def countWords(self):
        # 清空词袋
        self.words.clear()
        # 读取文件
        try:
            with open(self.origPath,'r')as f1:
                paragraph1 = f1.read()
            with open(self.repliPath,'r')as f2:
                paragraph2 = f2.read()
        except Exception as e:
            print(e)
            raise
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
    def calculateReduplication(self):
        # 计算文章余弦相似度
        innerProduct = 0
        modular1 = 0
        modular2 = 0
        for value in self.words.values():
            innerProduct += value[0]*value[1]
            modular1 += value[0]*value[0]
            modular2 += value[1]*value[1]
        if(innerProduct!=0):
            self.reduplication = innerProduct/(math.sqrt(modular1)*math.sqrt(modular2))
    def outReduplication(self):
        # 将相似度输出至文件
        try:
            with open(self.outPath,'a')as f:
                f.write(str('%.2f'%self.reduplication)+'\n')
        except Exception as e:
            print(e)
            raise
def main():
    if(len(sys.argv)<4):
        raise Exception("参数数目不足")
    wordsCounter = WordsCounter(sys.argv[1],sys.argv[2],sys.argv[3])
    wordsCounter.countWords()
    wordsCounter.calculateReduplication()
    wordsCounter.outReduplication()
if __name__=='__main__':
    main()
