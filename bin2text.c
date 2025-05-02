// https://stackoverflow.com/questions/25965555/writing-a-binary-file-into-ascii-code-using-c/25965810#25965810

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char ** argv) {
    if ( argc != 2 ) {
        fprintf(stderr, "You need an arguments.\n");
        return EXIT_FAILURE;
    }

    FILE * infile = fopen(argv[1], "rb");
    if ( !infile ) {
        fprintf(stderr, "Couldn't open file: %s\n", argv[1]);
        return EXIT_FAILURE;
    }

    int ch;
    while ( (ch = fgetc(infile)) != EOF ) {
        printf("%c", ch);
    }
    printf("\n");

    fclose(infile);

    return EXIT_SUCCESS;
}
