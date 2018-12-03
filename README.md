# Combinatorics_Algo

I've built a simple Flask app that gives you the number of non-negative solutions to an equation given upper limits to the variables.

The algorithm is based on the principle of Inclusion-Exclusion. The idea is that if we want to count the number of objects with a certain condition, 
we can count the total number of objects and then subtract the number of objects that do not have the condition.

For example, if we had the set {1, 3, 5, 6} and we wanted the number of even numbers in the set, we first count the total number of elements
in the set, which is 4. Then, we count the number of numbers that do not have the condition of being even. In other words, the number 
of odd elements in the set, which is 3. Using the principle, we get 4 - 3 = 1, indicating that there is one even element in the set.

This is a simple case using Inclusion-Exclusion but we can use extend it to solve our original problem:

  To count the # of non-neg int solutions such that properties P1, P2,...,Pk all hold,
  let Ai be the set of solutions such that Pi doesn't hold.

So if we have x1 <= 3, then A1 is the # of non-neg solutions such that x1<=3 is not true, so the # of solutions with x1 >= 4. And so on.

The technique re-expresses the union of A1, A2,...,Ak into intersections, where to get the size of the intersection, we use
the stars and bars approach explained here: [I'm an inline-style link](https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)).

We calculate these different combinations to get our union. We subtract this from the total # of solutions:

In short, I implemented the following technique:

![](file:///C:/Users/Marlon%20Pimentel/Downloads/CodeCogsEqn.svg)
