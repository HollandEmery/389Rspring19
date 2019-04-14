# Writeup 7 - Binaries I

Name: Holland Emery
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Holland Emery

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
int main(int num, int num2) {
printf(num);
printf(num2);
num = num^num2;
num2 = num^num2;
num = num^num2;
printf(num);
printf(num2);
}
```

### Part 2 (10 Pts)

The goal of the code is to switch the values of 2 numbers without using an extra variable, switching 2 values in place.
