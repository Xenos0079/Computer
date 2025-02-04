#include <iostream>
#include <cstring>

int main() {
    char cstr[80];
    strcpy(cstr, "these ");
    strcat(cstr, "strings ");
    strcat(cstr, "are ");
    strcat(cstr, "concatenated.");
    std::cout << cstr << " length = " << strlen(cstr);
    return 0;
}
