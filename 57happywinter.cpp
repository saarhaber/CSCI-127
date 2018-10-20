//Name:  Saar Haber
//Date:  April 19 2018
//program 57

#include <iostream>  //The built-in library for input/output
using namespace std; //The names of standard definitions

int main ()          //C++ programs all have a main() function
{
int num;
cout << "Enter number of a month: ";
cin >> num;

if (num<3 or num>11) {
  cout << "Happy Winter";
}
else if (num>=3 and num<7) {
  cout << "Happy Spring";
}
else if (num>=7 and num<9) {
  cout << "Happy Summer";
}
else {
  cout << "Happy Fall";
}


return 0;
}
