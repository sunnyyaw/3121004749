// 软工作业.h : Include file for standard system include files,
// or project specific include files.

#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
class WordsCounter
{
private:
	std::map<std::vector<char>, std::pair<int, int>> words;
	double replication;
public:
	int countOne(char c) {
		int n = 0;
		while (n < 8 && (((c << n) & 0x80) == 0x80))n++;
		if (n == 0)n++;
		return n;
	}
	void readFile(std::string filepath1, std::string filepath2) {
		std::ifstream fin1;
		std::ifstream fin2;
		fin1.open(filepath1, std::ios::in);
		fin2.open(filepath2, std::ios::in);
		if (!fin1.is_open() || !fin2.is_open())return;
		while (!fin1.eof()) {
			std::vector<char> word;
			word.push_back(fin1.get());
			int n = countOne(word.back());
			for (int i = 0; i < n-1; i++)
				word.push_back(fin1.get());
			std::map<std::vector<char>, std::pair<int, int>>::iterator it = words.find(word);
			if (it == words.end())
				words.insert({ word,{1,0} });
			else
				it->second.first++;
		}
		while (!fin2.eof()) {
			std::vector<char> word;
			word.push_back(fin2.get());
			int n = countOne(word.back());
			for (int i = 0; i < n - 1; i++)
				word.push_back(fin2.get());
			std::map<std::vector<char>, std::pair<int, int>>::iterator it = words.find(word);
			if (it == words.end())
				words.insert({ word,{0,1} });
			else
				it->second.second++;
		}
		fin1.close();
		fin2.close();
	}
	double computeReplication() {
		double innerProduct = 0;
		double modular1 = 0;
		double modular2 = 0;
		for (std::pair<std::vector<char>, std::pair<int, int>> word : words) {
			innerProduct += word.second.first * word.second.second;
			modular1 += word.second.first * word.second.first;
			modular2 += word.second.second * word.second.second;
		}
		replication = innerProduct / (sqrt(modular1) * sqrt(modular2));
		return replication;
	}
	void storeReplication(std::string filepath) {
		std::ofstream fout;
		fout.open(filepath, std::ios::out);
		fout << replication<<std::endl;
		fout.close();
	}
};
// TODO: Reference additional headers your program requires here.
