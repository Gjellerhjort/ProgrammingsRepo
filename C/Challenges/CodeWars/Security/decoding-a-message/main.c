#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *alphabet = "abcdefghijklmnopqrstuvwxyz";

char *decode (char *encoded, char *decoded)
{
    *decoded = '\0'
    for (int i = 0; i<strlen(encoded);i++)
    {
        char letter = encoded[i];
        char newletter = alphabet[27-(int)(strchr(alphabet, letter) - alphabet)];
        // append letter to decoded
    }
	return decoded; // return it
}

void sample_test(char *encoded, const char *expected) 
{
    char *actual;
    decode(encoded, actual);
    printf("encoded: %s decoded: %s \n", encoded, actual);
}

int main() 
{
    sample_test("sr", "hi");
	sample_test("svool", "hello");
	sample_test("r slkv mlylwb wvxlwvh gsrh nvhhztv", "i hope nobody decodes this message");
	sample_test("qzezxirkg rh z srts ovevo wbmznrx fmgbkvw zmw rmgvikivgvw kiltiznnrmt ozmtfztv rg szh yvvm hgzmwziwravw rm gsv vxnzxirkg ozmtfztv hkvxrurxzgrlm zolmthrwv sgno zmw xhh rg rh lmv lu gsv gsivv vhhvmgrzo gvxsmloltrvh lu dliow drwv dvy xlmgvmg kilwfxgrlm gsv nzqlirgb lu dvyhrgvh vnkolb rg zmw rg rh hfkkligvw yb zoo nlwvim dvy yildhvih drgslfg koftrmh",  "javacript is a high level dynamic untyped and interpreted programming language it has been standardized in the ecmacript language specification alongside html and css it is one of the three essential technologies of world wide web content production the majority of websites employ it and it is supported by all modern web browsers without plugins"); 
	sample_test("gsv vrtsgs hbnkslmb dzh qvzm hryvorfh urmzo nzqli xlnklhrgrlmzo kilqvxg lxxfkbrmt srn rmgvinrggvmgob",  "the eighth symphony was jean sibelius final major compositional project occupying him intermittently");
	sample_test("husbands ask repeated resolved but laughter debating",  "sfhyzmwh zhp ivkvzgvw ivhloevw yfg ozftsgvi wvyzgrmt");
	sample_test("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",  "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz");
	sample_test(" ", " ");
	sample_test(" aaa ", " zzz ");
	sample_test("       ", "       ");
	sample_test("", "");
	sample_test("thelastrandomsentence",  "gsvozhgizmwlnhvmgvmxv");
}