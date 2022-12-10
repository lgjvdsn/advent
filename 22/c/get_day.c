#include <stdio.h>

int get_day();
void download_file(int day);

int main(void) {
	printf("Day returned: %d\n", get_day());
}

int get_day() {
	int day = 0;
	printf("Which day?\n");
	scanf("%d", &day);
	printf("Getting day %d\n", day);
	return day;
}

void download_file(int day) {

}
