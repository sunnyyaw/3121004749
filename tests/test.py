import pytest
from test_main import WordsCounter

def test_a():
    with pytest.raises(Exception):
        wordsCounter = WordsCounter()
    wordsCounter = WordsCounter("a","b","c")
    with pytest.raises(Exception):
        wordsCounter.countWords()
    wordsCounter = WordsCounter("orig.txt","orig_0.8_add.txt","orig_0.8_del.txt")
    assert wordsCounter.replication == 0
    wordsCounter.countWords()
    wordsCounter.calculateReplication()
    assert wordsCounter.replication>0
