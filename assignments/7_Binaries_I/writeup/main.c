/*
 * Name: Holland Emery
 * Section: 0201
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Holland Emery
 */

/* your code goes here */
int main(int num, int num2) {
printf("%d\n",num);
printf("%d\n", num2);
num = num^num2;
num2 = num^num2;
num = num^num2;
printf("%d\n", num);
printf("%d\n", num2);
}