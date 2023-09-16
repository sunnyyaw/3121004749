| 这个作业属于哪个课程 | [计科21级12班 软件工程](https://edu.cnblogs.com/campus/gdgy/CSGrade21-12) |
| ----------------- |--------------- |
| 这个作业要求在哪里| [作业链接](https://edu.cnblogs.com/campus/gdgy/CSGrade21-12/homework/13015) |
| 这个作业的目标 | 个人项目 |

[github链接](https://github.com/sunnyyaw/3121004749)

| PSP2.1 Personal Software Process Stages | |预估耗时（分钟）| 实际耗时（分钟）|
| ----------------- |--------------- | ----------------- |--------------- |
| Planning | 计划 | 30 |60 |
| Estimate | 估计这个任务需要多少时间 | 30 | 60 |
| Development| 开发 | 720 | 900 |
| Analysis| 需求分析 (包括学习新技术) | 90 | 120 |
| Design Spec | 生成设计文档 | 30 | 60 |
| Design Review | 设计复审 |30 |30 |
| Coding Standard | 代码规范 (为目前的开发制定合适的规范) | 10 | 10 |
| Design | 具体设计 | 30 | 30 |
| Coding | 具体编码 | 360 | 420 |
| Code Review | 代码复审 | 30 | 30 |
| Test | 测试（自我测试，修改代码，提交修改）| 140 | 200 |
| Reporting | 报告 | 90 | 120 |
| Test Report | 测试报告 | 50 | 80 |
| Size Measurement | 计算工作量 | 20 | 20 |
| Postmortem & Process Improvement Plan | 事后总结, 并提出过程改进计划 | 20 | 20 |
|  | 合计 | 840 | 1080 |

接口的设计与实现：
---
- 总共设计了一个类和三个类成员函数。
- 类的构造函数将接收三个文件路径参数。
- countWords()接口首先从两个文件路径读取文件,然后用jieba库进行中文分词,然后遍历词列表计算词频。
- calculateReduplication()接口计算两个文件词频向量的余弦相似度
- outReduplication()接口将相似度输出至目标文件，写入模式为追加。

性能改进:
---
- 可以看出程序的主要耗时集中在读写文件函数
-     372605 function calls in 0.777 seconds

-     Ordered by: internal time

-     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
-         1    0.636    0.636    0.636    0.636 {built-in method marshal.load}
-      2090    0.023    0.000    0.049    0.000 D:\python3.7\lib\site-packages\jieba\finalseg\__init__.py:37(viterbi)
-      1858    0.019    0.000    0.660    0.000 D:\python3.7\lib\site-packages\jieba\__init__.py:180(get_DAG)
-     43187    0.012    0.000    0.016    0.000 D:\python3.7\lib\site-packages\jieba\__init__.py:177(<genexpr>)
-     101349    0.011    0.000    0.011    0.000 {method 'get' of 'dict' objects}
-     22140    0.011    0.000    0.013    0.000 D:\python3.7\lib\site-packages\jieba\finalseg\__init__.py:49(<listcomp>)
-     42965    0.010    0.000    0.028    0.000 {built-in method builtins.max}

单元测试:
---
- 用于测试程序应对文件不能打开的情况
def test_a():
    with pytest.raises(Exception):
        wordsCounter = WordsCounter()
    wordsCounter = WordsCounter("a","b","c")
    with pytest.raises(Exception):
        wordsCounter.countWords()
- 用于测试程序能否输出重复率
def test_b():
    wordsCounter = WordsCounter("orig.txt","orig_0.8_add.txt","result.txt")
    wordsCounter.countWords()
    wordsCounter.calculateReduplication()
    wordsCounter.outReduplication()
    assert wordsCounter.reduplication>0
- 测试用例结果
1.00
0.79
0.80
0.85
0.90


异常处理说明:
---
- 处理传入参数错误的问题
if(len(sys.argv)<4):
    raise Exception("参数数目不足")
- 处理文件无法打开的问题
try:
   with open(self.origPath,'r')as f1:
        paragraph1 = f1.read()
   with open(self.repliPath,'r')as f2:
        paragraph2 = f2.read()
   except Exception as e:
        print(e)
        raise
