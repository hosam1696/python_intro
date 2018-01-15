- You have learned the basics of Python and you love the language because it's friendly and pragmatic.
Now you want to become a productive Python programmer who can develop efficient, elegant code in an efficient, agile manner.
This course is for you. My name is Michele Vallisneri and I will show you how to cut down on your development time by writing more expressive and concise Python code
and by using the most powerful features of the language. In this course I will discuss how you can select and take advantage of the strongest third party packages.
I will introduce you to object oriented and functional programming which you will need to take your coding skills to the next level.
I'll recommend the best strategies to improve the performance of your code.
We will do all of this while working through examples that highlight just how much you can achieve with a few lines of Python.
We will make 3D images and movies with photographs taken by NASA's Rover on Mars and we'll map the Rover's progress through Martial topography.
We'll implement a simple graphical programming language and we'll draw and paint beautiful fractals.
So, let's get started.

in this chapter i will give you guides to write python codes that is relief, clear beautiful and fast
*in short* this is perhabs **pyhton** secret weapon
that beauty and effecieny are united and this surely one of the python programmers report really high satisfaction
day to day work.


### **PYTHON** VS **C**


``` c
%%file pi.c

#include <math.h>
#include <stdio.h>

int main(int argc,char **argv) {
    int k;
    double acc = 0.0;

    for(k=0;k<10000;k++) {
        acc = acc + pow(-1,k)/(2*k+1);
    }

    acc = 4 * acc;

    printf("pi: %.15f\n",acc);

    return 0;
}
```

the equivelant code in `python`

``` python
acc = 0.0

for k in range(10000):
    acc = acc + pow(-1,k)/(2*k+1)

acc = 4 * acc

print("pi:",acc)
```

or event can be reduced to

``` python
print(4 * sum(pow(-1, k) / (2 * k + 1) for k in range(10000)))
```


### The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!