//Name:  Saar Haber
//Date:  April 19 2018
//program 59

#include <iostream>  //The built-in library for input/output
using namespace std; //The names of standard definitions

int main ()          //C++ programs all have a main() function
{
int num;
cout << "Please enter age: ";
cin >> num;

while (num<0){
cout << "\n Entered a negative number.\n";
cout << "Please enter age: ";
cin >> num;
}

cout << "You Entered your age: " << num;
return 0;
}
