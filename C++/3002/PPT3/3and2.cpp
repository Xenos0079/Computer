#include <iostream>
#include <cstring>
using std::cout; using std::endl;

int main() {
    char cstr[] = "hello";
    cout << cstr << endl
         << strlen(cstr) << endl
         << sizeof cstr << endl;
    strcpy(cstr, "hello world");
    cout << cstr << endl
         << strlen(cstr) << endl
         << sizeof cstr << endl;
    return 0;
}
