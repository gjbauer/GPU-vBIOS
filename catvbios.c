#include <stdio.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <fcntl.h>

int main(int argc, char **argv)
{
    struct stat stats;
    int size, fd;
    stat(argv[1], &stats);

    printf("%d\n", (size=stats.st_size));
    
    fd = open(argv[1], O_RDWR, 0644);
    char *rom = mmap(0, size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    char ch;
    for (int i=0; rom[i]; i++) printf("%X", (ch=rom[i]));
    return 0;
}
