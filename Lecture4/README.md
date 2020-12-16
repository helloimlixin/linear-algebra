# Lecture 4: Multiplication and Inverse Matrices

## Overview

- Matrix Multiplication
- Inverse of <img src="https://latex.codecogs.com/svg.latex?A,&space;AB,&space;A^T" title="A, AB, A^T" />
- Gauss-Jordan Method to Find <img src="https://latex.codecogs.com/svg.latex?A^{-1}" title="A^{-1}" />

## Matrix Multiplication

<img src="https://latex.codecogs.com/svg.latex?A&space;\cdot&space;B&space;=&space;C" title="A \cdot B = C" />

**First Way**

Let's take an element in the resulting matrix <img src="https://latex.codecogs.com/svg.latex?C" title="C" /> for instance, say, <img src="https://latex.codecogs.com/svg.latex?C_{34}" title="C_{34}" />, we have it's a result of the dot product of the row-3 vector in matrix <img src="https://latex.codecogs.com/svg.latex?A" title="A" /> and the column-4 vector in matrix <img src="https://latex.codecogs.com/svg.latex?B" title="B" />,

<img src="https://latex.codecogs.com/svg.latex?\begin{aligned}C_{34}&space;&=&space;(\text{row-3&space;of&space;A})&space;\cdot&space;(\text{column-4&space;of&space;B})\\&space;&=&space;a_{31}&space;\times&space;b_{14}&space;&plus;&space;a_{32}&space;\times&space;b_{24}&space;&plus;&space;\cdots\\&space;&=&space;\sum_{k&space;=&space;1}^n&space;a_{3k}b_{k4}\end{aligned}" title="\begin{aligned}C_{34} &= (\text{row-3 of A}) \cdot (\text{column-4 of B})\\ &= a_{31} \times b_{14} + a_{32} \times b_{24} + \cdots\\ &= \sum_{k = 1}^n a_{3k}b_{k4}\end{aligned}" />

**Dimensions**

**Second Way**

<img src="https://latex.codecogs.com/svg.latex?A:&space;m&space;\times&space;n,&space;B:&space;n&space;\times&space;p,&space;C&space;=&space;AB:&space;m&space;\times&space;p" title="A: m \times n, B: n \times p, C = AB: m \times p" />

Columns of <img src="https://latex.codecogs.com/svg.latex?C" title="C" /> are combinations of columns of <img src="https://latex.codecogs.com/svg.latex?A" title="A" />, resulting from the operation where matrix $A$ times a column vector in matrix <img src="https://latex.codecogs.com/svg.latex?B" title="B" />.

**Third Way**

Another way to look at this matrix multiplication is to take a row vector from matrix $A$ and multiply it with all the rows in matrix $B$, which will produce a corresponding row in the resulting matrix $C$. Hence, the rows of $C$ are combinations of rows of $B$.

Let's take a look at the following operation,

$\text{column of } A \times \text{row of } B = \text{a matrix}$

For example,

$\begin{bmatrix}2 \\ 3 \\ 4\end{bmatrix}\begin{bmatrix}1 & 6\end{bmatrix} = \begin{bmatrix}2 & 12\\ 3 & 18\\ 4 & 24\end{bmatrix}$.

**Fourth Way (BEAUTIFUL)**

$AB = \text{sum of } [(\text{columns of }A) \times (\text{rows of }B)]$

For example,

$\begin{bmatrix}2 & 7\\ 3 & 8\\ 4 & 9\end{bmatrix}\begin{bmatrix}1 & 6\\ 0 & 0\end{bmatrix} = \begin{bmatrix}2\\ 3\\ 4\end{bmatrix}\begin{bmatrix}1 & 6\end{bmatrix}+ \begin{bmatrix}7\\ 8\\ 9\end{bmatrix}\begin{bmatrix}0 & 0\end{bmatrix}$

## Block Multiplication

$\begin{bmatrix}A_1 & A_2\\ A_3 & A_4\end{bmatrix}\begin{bmatrix}B_1 & B_2\\ B_3 & B_4\end{bmatrix} = \begin{bmatrix}C_1 & C_2\\ C_3 & C_4\end{bmatrix}$

$C_1 = A_1 B_1 + A_2 B_3$

## Matrix Inverses

### Square Matrices

NOT ALL MATRICES HAVE INVERSES

If $A$ is invertible / nonsingular,

$A^{-1} A = I = AA^{-1}$

**Singular Case**: no inverse

$A = \begin{bmatrix}1 & 3\\ 2 & 6\end{bmatrix}$

Can find a vector $X \neq 0$ such that $Ax = \mathbf{0}$.

$Ax = \begin{bmatrix}1 & 3\\ 2 & 6\end{bmatrix}\begin{bmatrix}3\\ -1\end{bmatrix} = \begin{bmatrix} 0\\0 \end{bmatrix}$

**Conclusion**: if $Ax = \mathbf{0}$, you can never escape 0 even if you have $A^{-1}A = I$, hence the inverse does not exist.

Example:

$\begin{bmatrix}1 & 3\\ 2 & 7\end{bmatrix}\begin{bmatrix}A^{-1}\end{bmatrix} = I$

$\Rightarrow \begin{bmatrix}1 & 3\\2 & 7\end{bmatrix}\begin{bmatrix}a & c\\ b & d\end{bmatrix} = \begin{bmatrix}1 & 0\\0 & 1\end{bmatrix}$

$A \times \text{column j of } A^{-1} = \text{column j of I}$

## Gauss-Jordan Method (Solve two equations at once)

$\begin{aligned}\begin{bmatrix}1 & 3\\ 2 & 7\end{bmatrix}\begin{bmatrix}a \\ b\end{bmatrix} &= \begin{bmatrix}1 \\ 0\end{bmatrix}\\\begin{bmatrix}1 & 3\\ 2 & 7\end{bmatrix}\begin{bmatrix}c \\ d\end{bmatrix} &= \begin{bmatrix}0 \\ 1\end{bmatrix}\end{aligned}$

Augmented Matrix

<img src="https://latex.codecogs.com/svg.latex?[A&space;\vline&space;I]&space;=&space;\begin{bmatrix}1&space;&&space;2&space;&\vline&space;&1&space;&&space;0\\3&space;&&space;7&space;&\vline&space;&0&space;&&space;1\end{bmatrix}\rightarrow&space;\begin{bmatrix}1&space;&3&space;&1&space;&0\\0&space;&1&space;&-2&space;&1\end{bmatrix}\rightarrow&space;\begin{bmatrix}1&space;&0&space;&7&space;&-3\\0&space;&1&space;&-2&space;&1\end{bmatrix}&space;=&space;[I&space;\vline&space;A^{-1}]" title="[A \vline I] = \begin{bmatrix}1 & 2 &\vline &1 & 0\\3 & 7 &\vline &0 & 1\end{bmatrix}\rightarrow \begin{bmatrix}1 &3 &1 &0\\0 &1 &-2 &1\end{bmatrix}\rightarrow \begin{bmatrix}1 &0 &7 &-3\\0 &1 &-2 &1\end{bmatrix} = [I \vline A^{-1}]" />

It's very simple to prove, suppose we have an elimination matrix such that,

$E [A \vline I] = [I \vline E]$

Since we have $EA = I$, therefore $E = A^{-1}$.

