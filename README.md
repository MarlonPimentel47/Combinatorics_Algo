# Non-negative Integer Solutions Calculator
### Implementation of Inclusion-Exclusion Algorithm on Counting Integer Solutions

A simple Flask app that gives you the number of non-negative solutions to an equation given upper limits to the variables.

To see the building process, check out this video: <>

The algorithm that I implemented in the back-end can handle any number of variables with its restrictions on the upper limits. The lower limit is set at 0 by default. 

At the moment, there is no way to set your own lower limits, but one can handle this by subtracting the lower limits to 0 and subtracting each difference from both their upper limit and the total. From there, the lower limits of the variables are at 0 and you can just call the original algorithm. On the front-end, my interface is restricted to 3 variables as I didn't spend too much time reading on how to dynamically modify a form. Maybe I'll get to that in the future...
___

### Quick Explanation

The algorithm is based on the principle of Inclusion-Exclusion. The idea is that if we want to count the number of objects with a certain condition, 
we can count the total number of objects and then subtract the number of objects that do not have the condition.

>For example, if we had the set {1, 3, 5, 6} and we wanted the number of even numbers in the set, we first count the total number of elements
in the set, which is 4. Then, we count the number of numbers that do not have the condition of being even. In other words, the number 
of odd elements in the set, which is 3. Using the principle, we get 4 - 3 = 1, indicating that there is one even element in the set.

This is a simple case using Inclusion-Exclusion but we can use extend it to solve our original problem:

To count the # of non-neg int solutions such that properties P1, P2,...,Pk all hold,
let Ai be the set of solutions such that Pi doesn't hold.

>So if we have x1 <= 3, then |A1| is the # of non-neg solutions such that x1 <= 3 is not true (P1 here is that x1 <= 3 *is* true). Another way to say this is that |A1| is the # of non-neg solutions such that x1 >= 4.

We'd then want the size of the union of A1, A2,...,Ak and subtract that from the total # of solutions. The technique I used re-expresses the union of A1, A2,...,Ak into intersections, where to get the size of each intersection, we use
the stars and bars approach explained here: [stars_and_bars](https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)).

We calculate several different combinations (stars and bars approach) to get the sizes of all the intersections, which in turn, gets us the size of the union. We then subtract this from the total # of solutions to get our answer. 

In short, I implemented the following:

![Alt text](https://i.imgur.com/KmK4nfz.png)
![Alt text](https://i.imgur.com/Lwn0IiR.png)

Applying the above by hand is not bad at all as they're just calculations, but that can get tedious... so lets let the program do all the work. Shoutout to python *fire emoji*.

