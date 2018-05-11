#include "simlib.c"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ofstream file;
	file.open("LCGRAND.txt");
	for (int i = 0; i < 1000; i++)
	{
		file << lcgrand(7);
		file << "\n";
	}
	file.close();
	return 0;
}