//Name:  Saar Haber
//Date:  April 19 2018
//program 56

#include <iostream>  //The built-in library for input/output
using namespace std; //The names of standard definitions

int main ()          //C++ programs all have a main() function
{
int i;
int num;
cout << "Enter a number: ";
cin >> num;

while ( num>0 ) {
  for (i=num; i>0; i--) {
    cout << "*";
  }
  cout << "\n";
  num=num-1;
}

return 0;
}
