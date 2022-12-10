#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

FILE *getFile();
int isEmptyLine(char *line);

int main()
{
	FILE* main_fp = getFile();
	char c;
	char *line = NULL;
	size_t len = 0;
	ssize_t read;
	int counter, max = 0;
	
	c = fgetc(main_fp);
	while ((read = getline(&line, &len, main_fp)) != -1) {
		if (isEmptyLine(line)){
			printf("Empty!\n");
			if(counter > max) {
				max = counter;
				counter = 0;
			}
		} else {
			char *ptr;
			printf("%s", line);
			counter += strtol(line, &ptr, 10);
		}
	}
	fclose(main_fp);
	printf("max is %d", max);
	return 0;
}

FILE *getFile() {
	FILE *fp = NULL;
	char *filename = "01.txt";
	fp = fopen("01.txt", "r");
	return fp;
}

int isEmptyLine(char *line) {
	char * ch;
	int isBlank = -1;
	for (ch = line; *ch != '\0'; ++ch) {
    	if (!isspace(*ch)){
    		isBlank = 0;
     		break;
		}
	}
	return isBlank;
}
