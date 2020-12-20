# Lecture 5: Factorization into LU

This lecture starts with a deeper dive into the materials left in the last lecture, including the inverse of a matrix product, the net result of today's lecture is a great way to look at the Gaussian Elimination, which is the LU factorization.

## Overview

- Inverse of a product <img src="https://latex.codecogs.com/svg.latex?AB" title="AB" />, <img src="https://latex.codecogs.com/svg.latex?A^T" title="A^T" />

- Product of elimination matrices:

  <img src="https://latex.codecogs.com/svg.latex?A&space;=&space;\mathcal{L}\mathcal{U}&space;\textit{&space;(no&space;row&space;exchanges)}" title="A = \mathcal{L}\mathcal{U} \textit{ (no row exchanges)}" />

## An Easy Example

Suppose <img src="https://latex.codecogs.com/svg.latex?A" title="A" /> is invertible, we have,

<img src="https://latex.codecogs.com/svg.latex?AA^{-1}&space;=&space;I&space;=&space;A^{-1}A" title="AA^{-1} = I = A^{-1}A" />

Then what matrix will give us the inverse of the product <img src="https://latex.codecogs.com/svg.latex?AB" title="AB" />? It can be easily seen that we can just multiply the inverse matrices in the reverse order.

<img src="https://latex.codecogs.com/svg.latex?ABB^{-1}A^{-1}&space;=&space;I" title="ABB^{-1}A^{-1} = I" />

For the left multiplication,

<img src="https://latex.codecogs.com/svg.latex?B^{-1}A^{-1}AB&space;=&space;I" title="B^{-1}A^{-1}AB = I" />

### What about the transposition?

Starting from the basics,

<img src="https://latex.codecogs.com/svg.latex?AA^{-1}&space;=&space;I" title="AA^{-1} = I" />

Note the transpose of an identity matrix is still an identity matrix (it's diagonal and symmetric). Hence, we transpose both sides of the equation, yielding,

<img src="https://latex.codecogs.com/svg.latex?(A^{-1})^TA^T&space;=&space;I" title="(A^{-1})^TA^T = I" />

We can see that <img src="https://latex.codecogs.com/svg.latex?24" title="24" /> is the inverse of <img src="https://latex.codecogs.com/svg.latex?A^T" title="A^T" />, which is <img src="https://latex.codecogs.com/svg.latex?(A^T)^{-1}" title="(A^T)^{-1}" />!

> <img src="https://latex.codecogs.com/svg.latex?A&space;=&space;\mathcal{LU}" title="A = \mathcal{LU}" /> is the most basic factorization of a matrix.

### Into a decent form (matrices)

Connection between <img src="https://latex.codecogs.com/svg.latex?A" title="A" /> and <img src="https://latex.codecogs.com/svg.latex?U" title="U" />

Let's first try a <img src="https://latex.codecogs.com/svg.latex?2&space;\times&space;2" title="2 \times 2" /> elimination,

<img src="https://latex.codecogs.com/svg.latex?A&space;=&space;\begin{bmatrix}2&space;&1\\&space;8&space;&7\end{bmatrix}" title="A = \begin{bmatrix}2 &1\\ 8 &7\end{bmatrix}" />

The elementary matrix should produce <img src="https://latex.codecogs.com/svg.latex?\mathcal{U}" title="\mathcal{U}" /> by left multiplying <img src="https://latex.codecogs.com/svg.latex?A" title="A" />,

<img src="https://latex.codecogs.com/svg.latex?E_{21}A&space;=&space;\mathcal{U}&space;\Rightarrow" title="E_{21}A = \mathcal{U} \Rightarrow" />

<img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}1&space;&0\\-4&space;&1\end{bmatrix}\begin{bmatrix}2&space;&1\\8&space;&7\end{bmatrix}&space;=&space;\begin{bmatrix}2&space;&1\\0&space;&3\end{bmatrix}" title="\begin{bmatrix}1 &0\\-4 &1\end{bmatrix}\begin{bmatrix}2 &1\\8 &7\end{bmatrix} = \begin{bmatrix}2 &1\\0 &3\end{bmatrix}" />

Therefore,

<img src="https://latex.codecogs.com/svg.latex?A&space;=&space;\mathcal{LU}&space;\Rightarrow&space;\begin{bmatrix}2&space;&1\\8&space;&7\end{bmatrix}&space;=&space;\begin{bmatrix}1&space;&0\\4&space;&1\end{bmatrix}\begin{bmatrix}2&space;&1\\0&space;&3\end{bmatrix}" title="A = \mathcal{LU} \Rightarrow \begin{bmatrix}2 &1\\8 &7\end{bmatrix} = \begin{bmatrix}1 &0\\4 &1\end{bmatrix}\begin{bmatrix}2 &1\\0 &3\end{bmatrix}" />

Moreover, if you want it more balanced, i.e., with a diagonal factor matrix in the middle,

<img src="https://latex.codecogs.com/svg.latex?A&space;=&space;\mathcal{LU}&space;\Rightarrow&space;\begin{bmatrix}2&space;&1\\8&space;&7\end{bmatrix}&space;=&space;\begin{bmatrix}1&space;&0\\4&space;&1\end{bmatrix}\begin{bmatrix}2&space;&1\\0&space;&3\end{bmatrix}" title="A = \mathcal{LU} \Rightarrow \begin{bmatrix}2 &1\\8 &7\end{bmatrix} = \begin{bmatrix}1 &0\\4 &1\end{bmatrix}\begin{bmatrix}2 &1\\0 &3\end{bmatrix}" />

Now let's try <img src="https://latex.codecogs.com/svg.latex?3&space;\times&space;3" title="3 \times 3" />,

<img src="https://latex.codecogs.com/svg.latex?E_{32}E_{31}E_{21}A&space;=&space;\mathcal{U}&space;\textit{&space;(no&space;row&space;exchange)}" title="E_{32}E_{31}E_{21}A = \mathcal{U} \textit{ (no row exchange)}" />

<img src="https://latex.codecogs.com/svg.latex?A&space;=&space;E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}\mathcal{U}&space;=&space;\mathcal{LU}" title="A = E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}\mathcal{U} = \mathcal{LU}" />

Why is <img src="https://latex.codecogs.com/svg.latex?LU-" title="LU-" />Decomposition better than simple elimination?

<img src="https://latex.codecogs.com/svg.latex?E_{32}E_{21}&space;=&space;\begin{bmatrix}1&space;&0&space;&0\\0&space;&1&space;&0\\0&space;&-5&space;&1\end{bmatrix}\begin{bmatrix}1&space;&0&space;&0\\-2&space;&1&space;&0\\0&space;&0&space;&1\end{bmatrix}&space;=&space;\begin{bmatrix}1&space;&0&space;&0\\-2&space;&1&space;&0\\10&space;&-5&space;&1\end{bmatrix}&space;=&space;E" title="E_{32}E_{21} = \begin{bmatrix}1 &0 &0\\0 &1 &0\\0 &-5 &1\end{bmatrix}\begin{bmatrix}1 &0 &0\\-2 &1 &0\\0 &0 &1\end{bmatrix} = \begin{bmatrix}1 &0 &0\\-2 &1 &0\\10 &-5 &1\end{bmatrix} = E" />

It's bad because row1 affects row3, producing the ugly <img src="https://latex.codecogs.com/svg.latex?10" title="10" /> in the third row. Now let's do the inverses,

<img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}1&space;&0&space;&0\\2&space;&1&space;&0\\0&space;&0&space;&1\end{bmatrix}\begin{bmatrix}1&space;&0&space;&0\\0&space;&1&space;&0\\0&space;&5&space;&1\end{bmatrix}&space;=&space;\begin{bmatrix}1&space;&0&space;&0\\2&space;&1&space;&0\\0&space;&5&space;&1\end{bmatrix}&space;=&space;\mathcal{L}" title="\begin{bmatrix}1 &0 &0\\2 &1 &0\\0 &0 &1\end{bmatrix}\begin{bmatrix}1 &0 &0\\0 &1 &0\\0 &5 &1\end{bmatrix} = \begin{bmatrix}1 &0 &0\\2 &1 &0\\0 &5 &1\end{bmatrix} = \mathcal{L}" />

We have <img src="https://latex.codecogs.com/svg.latex?EA&space;=&space;\mathcal{U},&space;A&space;=&space;\mathcal{LU}" title="EA = \mathcal{U}, A = \mathcal{LU}" />

> **NOTE**
>
> <img src="https://latex.codecogs.com/svg.latex?A&space;=&space;\mathcal{LU}" title="A = \mathcal{LU}" />
>
> If there's no row exchanges, then the multipliers go directly into <img src="https://latex.codecogs.com/svg.latex?\mathcal{L}" title="\mathcal{L}" />!

## How expensive is Elimination?

How many operations does it take to transform an <img src="https://latex.codecogs.com/svg.latex?n&space;\times&space;n" title="n \times n" /> matrix <img src="https://latex.codecogs.com/svg.latex?A" title="A" /> into <img src="https://latex.codecogs.com/svg.latex?\mathcal{U}" title="\mathcal{U}" />?

Let's say <img src="https://latex.codecogs.com/svg.latex?n&space;=&space;100" title="n = 100" />, we have the first step,

<img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}&space;a_{11}&space;&\cdots&space;&\cdots&space;&\cdots&space;\\&space;\cdots&space;&\cdots&space;&\cdots&space;&\cdots&space;\\&space;\vdots&space;&\vdots&space;&\vdots&space;&\vdots&space;\\&space;\cdots&space;&\cdots&space;&\cdots&space;&\cdots&space;\end{bmatrix}&space;\rightarrow&space;\begin{bmatrix}&space;a_{11}&space;&\cdots&space;&\cdots&space;&\cdots&space;\\&space;0&space;&\cdots&space;&\cdots&space;&\cdots&space;\\&space;\vdots&space;&\vdots&space;&\vdots&space;&\vdots&space;\\&space;0&space;&\cdots&space;&\cdots&space;&\cdots&space;\end{bmatrix}" title="\begin{bmatrix} a_{11} &\cdots &\cdots &\cdots \\ \cdots &\cdots &\cdots &\cdots \\ \vdots &\vdots &\vdots &\vdots \\ \cdots &\cdots &\cdots &\cdots \end{bmatrix} \rightarrow \begin{bmatrix} a_{11} &\cdots &\cdots &\cdots \\ 0 &\cdots &\cdots &\cdots \\ \vdots &\vdots &\vdots &\vdots \\ 0 &\cdots &\cdots &\cdots \end{bmatrix}" />

So it's about <img src="https://latex.codecogs.com/svg.latex?100^2" title="100^2" /> operations, subsequently, the next step takes around <img src="https://latex.codecogs.com/svg.latex?99^2" title="99^2" /> operationts, ...

Hence, the total number of operations required for eliminations can be approximated as follows,

<img src="https://latex.codecogs.com/svg.latex?n^2&space;&plus;&space;(n&space;-&space;1)^2&space;&plus;&space;\cdots&space;&plus;&space;2^2&space;&plus;&space;1^2" title="n^2 + (n - 1)^2 + \cdots + 2^2 + 1^2" />

which is,

<img src="https://latex.codecogs.com/svg.latex?\sum_{i&space;=&space;1}^n&space;i^2&space;\approx&space;\frac{1}{3}n^3" title="\sum_{i = 1}^n i^2 \approx \frac{1}{3}n^3" />

To draw an intuition, let's think about Calculus,

<img src="https://latex.codecogs.com/svg.latex?\int_1^n&space;x^2&space;dx&space;=&space;\frac{1}{3}&space;x^3" title="\int_1^n x^2 dx = \frac{1}{3} x^3" />

Now we have the operations on the left hand side, i.e., on <img src="https://latex.codecogs.com/svg.latex?A" title="A" />, while the cost of <img src="https://latex.codecogs.com/svg.latex?b" title="b" /> is <img src="https://latex.codecogs.com/svg.latex?O(n^2)" title="O(n^2)" />.

## Permutations

Starting fromt the identity matrix, we can list all the possible permutation matrices for row exchanges,

<img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}&space;1&space;&0&space;&0&space;\\&space;0&space;&1&space;&0&space;\\&space;0&space;&0&space;&1&space;\end{bmatrix},&space;\begin{bmatrix}&space;0&space;&1&space;&0&space;\\&space;1&space;&0&space;&0&space;\\&space;0&space;&0&space;&1&space;\end{bmatrix},&space;\begin{bmatrix}&space;0&space;&0&space;&1&space;\\&space;0&space;&1&space;&0&space;\\&space;1&space;&0&space;&0&space;\end{bmatrix},&space;\begin{bmatrix}&space;1&space;&0&space;&0&space;\\&space;0&space;&0&space;&1&space;\\&space;0&space;&1&space;&0&space;\end{bmatrix},&space;\begin{bmatrix}&space;0&space;&1&space;&0&space;\\&space;0&space;&0&space;&1&space;\\&space;1&space;&0&space;&0&space;\end{bmatrix},&space;\begin{bmatrix}&space;0&space;&0&space;&1&space;\\&space;1&space;&0&space;&0&space;\\&space;0&space;&1&space;&0&space;\end{bmatrix}" title="\begin{bmatrix} 1 &0 &0 \\ 0 &1 &0 \\ 0 &0 &1 \end{bmatrix}, \begin{bmatrix} 0 &1 &0 \\ 1 &0 &0 \\ 0 &0 &1 \end{bmatrix}, \begin{bmatrix} 0 &0 &1 \\ 0 &1 &0 \\ 1 &0 &0 \end{bmatrix}, \begin{bmatrix} 1 &0 &0 \\ 0 &0 &1 \\ 0 &1 &0 \end{bmatrix}, \begin{bmatrix} 0 &1 &0 \\ 0 &0 &1 \\ 1 &0 &0 \end{bmatrix}, \begin{bmatrix} 0 &0 &1 \\ 1 &0 &0 \\ 0 &1 &0 \end{bmatrix}" />

>  One interesting observation is that for the row-permutation matrices, the inverses are their transposes.

For <img src="https://latex.codecogs.com/svg.latex?4&space;\times&space;4" title="4 \times 4" />, there are <img src="https://latex.codecogs.com/svg.latex?24" title="24" /> P's.