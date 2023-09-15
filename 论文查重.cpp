// 软工作业.cpp : Defines the entry point for the application.
//

#include "Header1.h"

using namespace std;

int main(int argc, char* argv[])
{
	if (argc < 4)return 0;
	WordsCounter wordsCounter;
	wordsCounter.readFile(argv[1], argv[2]);
	wordsCounter.computeReplication();
	wordsCounter.storeReplication(argv[3]);
	return 0;
}
