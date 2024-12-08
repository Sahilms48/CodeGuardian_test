#include <iostream>
#include <cstring>
#include <cstdlib>

void vulnerable_function(char *input) {
    char buffer[64];
    strcpy(buffer, input);
    std::cout << "Input: " << buffer << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        std::cout << "Usage: " << argv[0] << " <input>" << std::endl;
        return 1;
    }

    char *user_input = argv[1];
    vulnerable_function(user_input);

    char *memory = (char *)malloc(100);
    strcpy(memory, user_input);
    free(memory);
    std::cout << "Freed memory: " << memory << std::endl;

    return 0;
}
