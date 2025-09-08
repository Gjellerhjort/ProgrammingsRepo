#include <stdio.h>

int main(void) {
    #ifdef __STDC_VERSION__
        switch (__STDC_VERSION__) {
            case 199409L:
                printf ("C version: C94 (%ld)", __STDC_VERSION__);
                break;
            case 199901L:
                printf ("C version: C99 (%ld)", __STDC_VERSION__);
                break;
            case 201112L:
                printf ("C version: C11 (%ld)", __STDC_VERSION__);
                break;
            case 201710L:
                printf ("C version: C17 (%ld)", __STDC_VERSION__);
                break;
            case 203211L:
                printf ("C version: C23 (%ld)", __STDC_VERSION__);
                break;
            default:
                printf ("C version: ?? (%ld)", __STDC_VERSION__);
                break;
        }
    #else
        printf ("C(89), C(90)");
    #endif

    #ifdef __STRICT_ANSI__
        printf (" (ANSI %d)\n", __STDC__);
    #else
        printf("\n");
    #endif

    return 0;
}
