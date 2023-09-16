import pytest
from main import WordsCounter

def test_a():
    with pytest.raises(Exception):
        wordsCounter = WordsCounter()
    wordsCounter = WordsCounter("a","b","c")
    with pytest.raises(Exception):
        wordsCounter.countWords()
def test_b():
    wordsCounter = WordsCounter("orig.txt","orig_0.8_add.txt","result.txt")
    wordsCounter.countWords()
    wordsCounter.calculateReduplication()
    wordsCounter.outReduplication()
    assert wordsCounter.reduplication>0
def test_c():
    wordsCounter = WordsCounter("orig.txt","orig_0.8_del.txt","result.txt")
    wordsCounter.countWords()
    wordsCounter.calculateReduplication()
    wordsCounter.outReduplication()
    assert wordsCounter.reduplication>0
def test_d():
    wordsCounter = WordsCounter("orig.txt","orig_0.8_dis_1.txt","result.txt")
    wordsCounter.countWords()
    wordsCounter.calculateReduplication()
    wordsCounter.outReduplication()
    assert wordsCounter.reduplication>0
def test_e():
    wordsCounter = WordsCounter("orig.txt","orig_0.8_dis_10.txt","result.txt")
    wordsCounter.countWords()
    wordsCounter.calculateReduplication()
    wordsCounter.outReduplication()
    assert wordsCounter.reduplication>0
def test_f():
    wordsCounter = WordsCounter("orig.txt","orig_0.8_dis_15.txt","result.txt")
    wordsCounter.countWords()
    wordsCounter.calculateReduplication()
    wordsCounter.outReduplication()
    assert wordsCounter.reduplication>0

