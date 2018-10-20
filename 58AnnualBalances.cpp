//Name:  Saar Haber
//Date:  April 19 2018
//program 58

#include <iostream>  //The built-in library for input/output
using namespace std; //The names of standard definitions

int main ()          //C++ programs all have a main() function
{
double num;
cout << "Please enter the starting amount: ";
cin >> num;

int i;

for (i=1; i<=5; i++)
{
  num=num*1.1;
  cout << "Year " << i << " " << num << "\n";
}

return 0;
}
