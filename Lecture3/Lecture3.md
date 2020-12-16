# Lecture 3: Elimination with Matrices

This lecture is about solving systems of linear equation, while the method of solution will not be determinants (which will come later), the method here we'll use is called *Elimination*. It is a method that a lot of software packages used to solve equations.

**Example** Let's consider the following system of linear equations as an example,

<img src="https://latex.codecogs.com/svg.latex?\begin{aligned}x&space;&plus;&space;2y&space;&plus;&space;z&space;&=&space;2\\&space;3x&space;&plus;&space;8y&space;&plus;&space;z&space;&=&space;12\\&space;4y&space;&plus;&space;z&space;&=&space;12\end{aligned}" title="\begin{aligned}x + 2y + z &= 2\\ 3x + 8y + z &= 12\\ 4y + z &= 12\end{aligned}" />

We have the following coefficient matrix,

<img src="https://latex.codecogs.com/svg.latex?A&space;=&space;\begin{bmatrix}1&space;&2&space;&1\\&space;3&space;&8&space;&1\\&space;0&space;&4&space;&1\end{bmatrix}" title="A = \begin{bmatrix}1 &2 &1\\ 3 &8 &1\\ 0 &4 &1\end{bmatrix}" />

and the system of linear equations can be written in the following matrix form,

<img src="https://latex.codecogs.com/svg.latex?Ax&space;=&space;b" title="Ax = b" />

## Overview

- Elimination
  - Success
  - Failure
- Back-Substitution
- Elimination Matrices
- Matrix Multiplication

## Elimination

One intuitive idea of elimination is to knock out (multiply and subtract) the term associated with each variable one at a time, to do this, let's first pick the first "pivot" as shown in the solid box below in the matrix $A$,

<img src="https://latex.codecogs.com/svg.latex?A&space;=&space;\begin{bmatrix}\fbox{1}&space;&2&space;&1\\&space;3&space;&8&space;&1\\&space;0&space;&4&space;&1\end{bmatrix}&space;\rightarrow&space;\begin{bmatrix}\fbox{1}&space;&2&space;&1\\&space;0&space;&2&space;&-2\\&space;0&space;&4&space;&1\end{bmatrix}" title="A = \begin{bmatrix}\fbox{1} &2 &1\\ 3 &8 &1\\ 0 &4 &1\end{bmatrix} \rightarrow \begin{bmatrix}\fbox{1} &2 &1\\ 0 &2 &-2\\ 0 &4 &1\end{bmatrix}" />

Now we have the second pivot,

<img src="https://latex.codecogs.com/svg.latex?A&space;=&space;\begin{bmatrix}\fbox{1}&space;&2&space;&1\\3&space;&8&space;&1\\0&space;&4&space;&1\end{bmatrix}&space;\rightarrow&space;\begin{bmatrix}\fbox{1}&space;&2&space;&1\\0&space;&\fbox{2}&space;&-2\\0&space;&4&space;&1\end{bmatrix}&space;\rightarrow&space;\begin{bmatrix}\fbox{1}&space;&2&space;&1\\0&space;&\fbox{2}&space;&-2\\0&space;&0&space;&\fbox{5}\end{bmatrix}" title="A = \begin{bmatrix}\fbox{1} &2 &1\\3 &8 &1\\0 &4 &1\end{bmatrix} \rightarrow \begin{bmatrix}\fbox{1} &2 &1\\0 &\fbox{2} &-2\\0 &4 &1\end{bmatrix} \rightarrow \begin{bmatrix}\fbox{1} &2 &1\\0 &\fbox{2} &-2\\0 &0 &\fbox{5}\end{bmatrix}" />

**Question: How could this fail? (By failing to come up with 3 pivots)**

Pivot becomes zero,

<img src="https://latex.codecogs.com/svg.latex?A&space;=&space;\begin{bmatrix}\fbox{1}&space;&2&space;&1\\&space;3&space;&8&space;&1\\&space;0&space;&4&space;&-4\end{bmatrix}&space;\rightarrow&space;\begin{bmatrix}\fbox{1}&space;&2&space;&1\\&space;0&space;&\fbox{2}&space;&-2\\&space;0&space;&4&space;&-4\end{bmatrix}&space;\rightarrow&space;\begin{bmatrix}\fbox{1}&space;&2&space;&1\\&space;0&space;&\fbox{2}&space;&-2\\&space;0&space;&0&space;&\fbox{0}\end{bmatrix}" title="A = \begin{bmatrix}\fbox{1} &2 &1\\ 3 &8 &1\\ 0 &4 &-4\end{bmatrix} \rightarrow \begin{bmatrix}\fbox{1} &2 &1\\ 0 &\fbox{2} &-2\\ 0 &4 &-4\end{bmatrix} \rightarrow \begin{bmatrix}\fbox{1} &2 &1\\ 0 &\fbox{2} &-2\\ 0 &0 &\fbox{0}\end{bmatrix}" />

Now let's consider $Ax = b$ and we ***augment*** the matrix $A$ by an additional column representing column vector $b$.

<img src="https://latex.codecogs.com/svg.latex?[A&space;|&space;b]&space;=&space;\begin{bmatrix}\fbox{1}&space;&2&space;&1&space;&|&space;&2\\&space;3&space;&8&space;&1&space;&|&space;&12\\&space;0&space;&4&space;&1&space;&|&space;&2\end{bmatrix}&space;\rightarrow&space;\begin{bmatrix}\fbox{1}&space;&2&space;&1&space;&|&space;&2\\&space;0&space;&\fbox{2}&space;&-2&space;&|&space;&6\\&space;0&space;&4&space;&1&space;&|&space;&2\end{bmatrix}&space;\rightarrow&space;\begin{bmatrix}\fbox{1}&space;&2&space;&1&space;&|&space;&2\\&space;0&space;&\fbox{2}&space;&-2&space;&|&space;&6\\&space;0&space;&0&space;&\fbox{5}&space;&|&space;&-10\end{bmatrix}" title="[A | b] = \begin{bmatrix}\fbox{1} &2 &1 &| &2\\ 3 &8 &1 &| &12\\ 0 &4 &1 &| &2\end{bmatrix} \rightarrow \begin{bmatrix}\fbox{1} &2 &1 &| &2\\ 0 &\fbox{2} &-2 &| &6\\ 0 &4 &1 &| &2\end{bmatrix} \rightarrow \begin{bmatrix}\fbox{1} &2 &1 &| &2\\ 0 &\fbox{2} &-2 &| &6\\ 0 &0 &\fbox{5} &| &-10\end{bmatrix}" />

## Back-Substitution

Back-substitute the resulting matrices into the system of linear equations,

<img src="https://latex.codecogs.com/svg.latex?\begin{aligned}x&space;&plus;&space;2y&space;&plus;&space;z&space;&=&space;2\\&space;2y&space;-&space;2z&space;&=&space;6\\&space;5z&space;&=&space;-10\end{aligned}&space;\Rightarrow&space;\begin{cases}x&space;=&space;2\\&space;y&space;=&space;1\\&space;z&space;=&space;-2\end{cases}" title="\begin{aligned}x + 2y + z &= 2\\ 2y - 2z &= 6\\ 5z &= -10\end{aligned} \Rightarrow \begin{cases}x = 2\\ y = 1\\ z = -2\end{cases}" />

## Elimination Matrices

Let's first take the original matrix,

<img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}1&space;&2&space;&1\\3&space;&8&space;&1\\0&space;&4&space;&1\end{bmatrix}" title="\begin{bmatrix}1 &2 &1\\3 &8 &1\\0 &4 &1\end{bmatrix}" />

> The multiplication of a matrix $A$ and a column vector is the linear combination of the columns of the matrix $A$,
>
> <img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}\vline&space;&\vline&space;&\vline\\&space;col1&space;&col2&space;&col3\\&space;\vline&space;&\vline&space;&\vline\end{bmatrix}\begin{bmatrix}3\\4\\5\end{bmatrix}&space;=&space;3&space;\times&space;col1&space;&plus;&space;4&space;\times&space;col2&space;&plus;&space;5&space;\times&space;col3" title="\begin{bmatrix}\vline &\vline &\vline\\ col1 &col2 &col3\\ \vline &\vline &\vline\end{bmatrix}\begin{bmatrix}3\\4\\5\end{bmatrix} = 3 \times col1 + 4 \times col2 + 5 \times col3" />
>
> Here we have,
>
> matrix <img src="https://latex.codecogs.com/svg.latex?\times" title="\times" /> column <img src="https://latex.codecogs.com/svg.latex?=" title="=" /> column

In parallel, we have the product of a row vector and a matrix,

<img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}1&space;&2&space;&7\end{bmatrix}\begin{bmatrix}-&space;&row1&space;&-\\-&space;&row2&space;&-\\-&space;&row3&space;&-\end{bmatrix}&space;=&space;1&space;\times&space;row1&space;&plus;&space;2&space;\times&space;row2&space;&plus;&space;7&space;\times&space;row3" title="\begin{bmatrix}1 &2 &7\end{bmatrix}\begin{bmatrix}- &row1 &-\\- &row2 &-\\- &row3 &-\end{bmatrix} = 1 \times row1 + 2 \times row2 + 7 \times row3" />

> Here we have,
>
> row <img src="https://latex.codecogs.com/svg.latex?\times" title="\times" /> matrix <img src="https://latex.codecogs.com/svg.latex?=" title="=" /> row

### Reproducing Matrix Elimination

Now let's reproduce the elimination steps above in matrix forms,

**STEP 1**: subtract <img src="https://latex.codecogs.com/svg.latex?3&space;\times" title="3 \times" /> row1 from row2

<img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}1&space;&0&space;&0\\-3&space;&1&space;&0\\0&space;&0&space;&1\end{bmatrix}\begin{bmatrix}1&space;&2&space;&1\\3&space;&8&space;&1\\0&space;&4&space;&1\end{bmatrix}=&space;\begin{bmatrix}1&space;&2&space;&1\\0&space;&2&space;&-2\\0&space;&4&space;&1\end{bmatrix},&space;\text{where&space;}&space;E_{21}&space;=&space;\begin{bmatrix}1&space;&0&space;&0\\-3&space;&1&space;&0\\0&space;&0&space;&1\end{bmatrix}" title="\begin{bmatrix}1 &0 &0\\-3 &1 &0\\0 &0 &1\end{bmatrix}\begin{bmatrix}1 &2 &1\\3 &8 &1\\0 &4 &1\end{bmatrix}= \begin{bmatrix}1 &2 &1\\0 &2 &-2\\0 &4 &1\end{bmatrix}, \text{where } E_{21} = \begin{bmatrix}1 &0 &0\\-3 &1 &0\\0 &0 &1\end{bmatrix}" />

**STEP 2**: subtract <img src="https://latex.codecogs.com/svg.latex?2&space;\times" title="2 \times" /> row2 from row3

<img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}1&space;&0&space;&0\\0&space;&1&space;&0\\0&space;&-2&space;&1\end{bmatrix}\begin{bmatrix}1&space;&2&space;&1\\0&space;&2&space;&-2\\0&space;&4&space;&1\end{bmatrix}&space;=&space;\begin{bmatrix}1&space;&2&space;&1\\0&space;&2&space;&-2\\0&space;&0&space;&5\end{bmatrix}&space;=&space;\mathcal{U},&space;\text{where&space;}E_{32}&space;=&space;\begin{bmatrix}1&space;&0&space;&0\\0&space;&1&space;&0\\0&space;&-2&space;&1\end{bmatrix}" title="\begin{bmatrix}1 &0 &0\\0 &1 &0\\0 &-2 &1\end{bmatrix}\begin{bmatrix}1 &2 &1\\0 &2 &-2\\0 &4 &1\end{bmatrix} = \begin{bmatrix}1 &2 &1\\0 &2 &-2\\0 &0 &5\end{bmatrix} = \mathcal{U}, \text{where }E_{32} = \begin{bmatrix}1 &0 &0\\0 &1 &0\\0 &-2 &1\end{bmatrix}" />

To summarize, we have the elimination can be carried out using matrices as follows,

<img src="https://latex.codecogs.com/svg.latex?E_{32}E_{21}A&space;=&space;\mathcal{U}" title="E_{32}E_{21}A = \mathcal{U}" />

**How to create a matrix that does all the eliminations in one shot?**

Use the **associative** law,

<img src="https://latex.codecogs.com/svg.latex?E_{32}(E_{21}A)&space;=&space;\mathcal{U}&space;\Rightarrow&space;(E_{32}E_{21})A&space;=&space;\mathcal{U}" title="E_{32}(E_{21}A) = \mathcal{U} \Rightarrow (E_{32}E_{21})A = \mathcal{U}" />

> **NOTE**: many facts from Linear Algebra come from simply moving the parentheses.

### Permutation Matrices

1. **Row-Exchange** let's consider a matrix that exchanges row1 and row2,

   <img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}0&space;&1\\1&space;&0\end{bmatrix}\begin{bmatrix}a&space;&b\\c&space;&d\end{bmatrix}&space;=&space;\begin{bmatrix}c&space;&d\\a&space;&b\end{bmatrix},&space;\text{where&space;}P&space;=&space;\begin{bmatrix}0&space;&1\\1&space;&0\end{bmatrix}" title="\begin{bmatrix}0 &1\\1 &0\end{bmatrix}\begin{bmatrix}a &b\\c &d\end{bmatrix} = \begin{bmatrix}c &d\\a &b\end{bmatrix}, \text{where }P = \begin{bmatrix}0 &1\\1 &0\end{bmatrix}" />

   > **NOTE**: for row permutations, the permutation matrix should be multiplied from the left

2. **Column-Exchange**

   <img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}a&space;&b\\c&space;&d\end{bmatrix}\begin{bmatrix}0&space;&1\\1&space;&0\end{bmatrix}=&space;\begin{bmatrix}b&space;&a\\d&space;&c\end{bmatrix}" title="\begin{bmatrix}a &b\\c &d\end{bmatrix}\begin{bmatrix}0 &1\\1 &0\end{bmatrix}= \begin{bmatrix}b &a\\d &c\end{bmatrix}" />

   > **NOTE**: for column permutations, the permutation matrix should be multiplied from the right.

The commutative law for matrices don't work!

<img src="https://latex.codecogs.com/svg.latex?AB&space;\neq&space;BA" title="AB \neq BA" />

## Inverse Matrices

Let's consider the case where we would like to cancel out the elimination,

<img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}1&space;&0&space;&0\\3&space;&1&space;&0\\0&space;&0&space;&1\end{bmatrix}\begin{bmatrix}1&space;&0&space;&0\\-3&space;&0&space;&0\\0&space;&0&space;&1\end{bmatrix}&space;=&space;\begin{bmatrix}1&space;&0&space;&0\\0&space;&1&space;&0\\0&space;&0&space;&1\end{bmatrix}" title="\begin{bmatrix}1 &0 &0\\3 &1 &0\\0 &0 &1\end{bmatrix}\begin{bmatrix}1 &0 &0\\-3 &0 &0\\0 &0 &1\end{bmatrix} = \begin{bmatrix}1 &0 &0\\0 &1 &0\\0 &0 &1\end{bmatrix}" />

In short,

<img src="https://latex.codecogs.com/svg.latex?E^{-1}&space;E&space;=&space;I" title="E^{-1} E = I" />

## Problems

**Problem 1** Solve, using the method of elimination:

<img src="https://latex.codecogs.com/svg.latex?\begin{aligned}x&space;-&space;y&space;-&space;z&space;&plus;&space;u&space;&=&space;0\\2x&space;&plus;&space;2z&space;&=&space;8\\&space;-y&space;-2z&space;&=&space;-8\\3x&space;-&space;3y&space;-2z&space;&plus;4u&space;&=&space;7\end{aligned}" title="\begin{aligned}x - y - z + u &= 0\\2x + 2z &= 8\\ -y -2z &= -8\\3x - 3y -2z +4u &= 7\end{aligned}" />

**Solution**

Convert the system of equations (augmented) into a matrix,

<img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}\fbox{1}&space;&-1&space;&-1&space;&1&space;&\vline&space;&0&space;\\&space;2&space;&0&space;&2&space;&0&space;&\vline&space;&8\\&space;0&space;&-1&space;&-2&space;&0&space;&\vline&space;&-8\\&space;3&space;&-3&space;&-2&space;&4&space;&\vline&space;&7\end{bmatrix}&space;\rightarrow&space;\begin{bmatrix}\fbox{1}&space;&-1&space;&-1&space;&1&space;&\vline&space;&0&space;\\&space;0&space;&\fbox{2}&space;&4&space;&-2&space;&\vline&space;&8\\&space;0&space;&-1&space;&-2&space;&0&space;&\vline&space;&-8\\&space;0&space;&0&space;&1&space;&1&space;&\vline&space;&7\end{bmatrix}&space;\rightarrow&space;\begin{bmatrix}\fbox{1}&space;&-1&space;&-1&space;&1&space;&\vline&space;&0&space;\\&space;0&space;&\fbox{2}&space;&4&space;&-2&space;&\vline&space;&8\\&space;0&space;&0&space;&0&space;&-1&space;&\vline&space;&-4\\&space;0&space;&0&space;&1&space;&1&space;&\vline&space;&7\end{bmatrix}" title="\begin{bmatrix}\fbox{1} &-1 &-1 &1 &\vline &0 \\ 2 &0 &2 &0 &\vline &8\\ 0 &-1 &-2 &0 &\vline &-8\\ 3 &-3 &-2 &4 &\vline &7\end{bmatrix} \rightarrow \begin{bmatrix}\fbox{1} &-1 &-1 &1 &\vline &0 \\ 0 &\fbox{2} &4 &-2 &\vline &8\\ 0 &-1 &-2 &0 &\vline &-8\\ 0 &0 &1 &1 &\vline &7\end{bmatrix} \rightarrow \begin{bmatrix}\fbox{1} &-1 &-1 &1 &\vline &0 \\ 0 &\fbox{2} &4 &-2 &\vline &8\\ 0 &0 &0 &-1 &\vline &-4\\ 0 &0 &1 &1 &\vline &7\end{bmatrix}" />

<img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}\fbox{1}&space;&-1&space;&-1&space;&1&space;&\vline&space;&0&space;\\&space;0&space;&\fbox{2}&space;&4&space;&-2&space;&\vline&space;&8\\&space;0&space;&0&space;&\fbox{1}&space;&1&space;&\vline&space;&7\\&space;0&space;&0&space;&0&space;&\fbox{-1}&space;&\vline&space;&-4\end{bmatrix}&space;\Rightarrow&space;-u&space;=&space;-4&space;\Rightarrow&space;\begin{cases}\fbox{u&space;=&space;4}\\z&space;&plus;&space;u&space;=&space;7\\z&space;&plus;&space;4&space;=&space;7&space;\Rightarrow&space;\fbox{z&space;=&space;3}\\&space;2y&space;&plus;&space;4&space;*&space;3&space;-&space;2*4&space;=&space;8&space;\Rightarrow&space;\fbox{y&space;=&space;2}\\&space;x&space;-&space;2&space;-&space;3&space;&plus;&space;4&space;=&space;0&space;\Rightarrow&space;\fbox{x&space;=&space;1}\end{cases}" title="\begin{bmatrix}\fbox{1} &-1 &-1 &1 &\vline &0 \\ 0 &\fbox{2} &4 &-2 &\vline &8\\ 0 &0 &\fbox{1} &1 &\vline &7\\ 0 &0 &0 &\fbox{-1} &\vline &-4\end{bmatrix} \Rightarrow -u = -4 \Rightarrow \begin{cases}\fbox{u = 4}\\z + u = 7\\z + 4 = 7 \Rightarrow \fbox{z = 3}\\ 2y + 4 * 3 - 2*4 = 8 \Rightarrow \fbox{y = 2}\\ x - 2 - 3 + 4 = 0 \Rightarrow \fbox{x = 1}\end{cases}" />

**Problem 2** Find the triangular matrix <img src="https://latex.codecogs.com/svg.latex?E" title="E" /> that reduces "Pascal's matrix" to a smaller Pascal:

<img src="https://latex.codecogs.com/svg.latex?E\begin{bmatrix}1&space;&0&space;&0&space;&0\\1&space;&1&space;&0&space;&0\\1&space;&2&space;&1&space;&0\\1&space;&3&space;&3&space;&1\end{bmatrix}&space;=&space;\begin{bmatrix}1&space;&0&space;&0&space;&0\\0&space;&1&space;&0&space;&0\\&space;0&space;&1&space;&1&space;&0\\0&space;&1&space;&2&space;&1\end{bmatrix}" title="E\begin{bmatrix}1 &0 &0 &0\\1 &1 &0 &0\\1 &2 &1 &0\\1 &3 &3 &1\end{bmatrix} = \begin{bmatrix}1 &0 &0 &0\\0 &1 &0 &0\\ 0 &1 &1 &0\\0 &1 &2 &1\end{bmatrix}" />.

What matrix <img src="https://latex.codecogs.com/svg.latex?M" title="M" /> (multiplying several <img src="https://latex.codecogs.com/svg.latex?E" title="E" />'s') reduces Pascal all the way to <img src="https://latex.codecogs.com/svg.latex?I" title="I" />?

### Solution

Starting from the identity matrix,

<img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}1&space;&0&space;&0&space;&0\\0&space;&1&space;&0&space;&0\\0&space;&0&space;&1&space;&0\\0&space;&0&space;&0&space;&1\end{bmatrix}" title="\begin{bmatrix}1 &0 &0 &0\\0 &1 &0 &0\\0 &0 &1 &0\\0 &0 &0 &1\end{bmatrix}" />

We have the triangular matrix $E$ that the reduces the Pascal matrix to a smaller Pascal is,

<img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}1&space;&0&space;&0&space;&0\\-1&space;&1&space;&0&space;&0\\0&space;&-1&space;&1&space;&0\\0&space;&0&space;&-1&space;&1\end{bmatrix}" title="\begin{bmatrix}1 &0 &0 &0\\-1 &1 &0 &0\\0 &-1 &1 &0\\0 &0 &-1 &1\end{bmatrix}" />

To further convert the smaller Pascal to identity matrix, we need to left multiply another matrix,

<img src="https://latex.codecogs.com/svg.latex?\begin{bmatrix}1&space;&0&space;&0&space;&0\\0&space;&1&space;&0&space;&0\\0&space;&-1&space;&1&space;&0\\0&space;&0&space;&-2&space;&1\end{bmatrix}" title="\begin{bmatrix}1 &0 &0 &0\\0 &1 &0 &0\\0 &-1 &1 &0\\0 &0 &-2 &1\end{bmatrix}" />

Multiply the two matrices to obtain <img src="https://latex.codecogs.com/svg.latex?M" title="M" />,

<img src="https://latex.codecogs.com/svg.latex?M&space;=&space;\begin{bmatrix}1&space;&0&space;&0&space;&0\\0&space;&1&space;&0&space;&0\\0&space;&-1&space;&1&space;&0\\0&space;&0&space;&-2&space;&1\end{bmatrix}\begin{bmatrix}1&space;&0&space;&0&space;&0\\-1&space;&1&space;&0&space;&0\\0&space;&-1&space;&1&space;&0\\0&space;&0&space;&-1&space;&1\end{bmatrix}&space;=&space;\begin{bmatrix}1&space;&0&space;&0&space;&0\\-1&space;&1&space;&0&space;&0\\1&space;&-2&space;&1&space;&0\\0&space;&3&space;&-3&space;&1\end{bmatrix}" title="M = \begin{bmatrix}1 &0 &0 &0\\0 &1 &0 &0\\0 &-1 &1 &0\\0 &0 &-2 &1\end{bmatrix}\begin{bmatrix}1 &0 &0 &0\\-1 &1 &0 &0\\0 &-1 &1 &0\\0 &0 &-1 &1\end{bmatrix} = \begin{bmatrix}1 &0 &0 &0\\-1 &1 &0 &0\\1 &-2 &1 &0\\0 &3 &-3 &1\end{bmatrix}" />

Since <img src="https://latex.codecogs.com/svg.latex?M" title="M" /> reduces the Pascal matrix to <img src="https://latex.codecogs.com/svg.latex?I" title="I" />, <img src="https://latex.codecogs.com/svg.latex?M" title="M" /> is the **inverse** matrix of the original Pascal matrix.

## Implementation

### Python Version

```python
def gauss_elim(matrix):
    """MAIN PROCEDURE: perform Gaussian Elimination on the given matrix. The expected
    result of the elimination is a upper-triangular matrix U. The Main Procedure of
    this implementation contains the following steps:
    1. Sanity check, quit if the matrix is empty or contains only a row vector.
    2. Organize the matrix into a nice form where all the zeros are pushed to the
        lower left corner.
    3. Loop through the rows, find the pivot entries and perform row eliminations.py
    
    If elimination succeeds, it will print out the resulting matrix and return it.

    NOTE: here all the entries of the matrix will be converted to float-point
    numbers automatically for the sake of computation.

    Args:
        matrix ([[], [], ...]): nested list representing the target matrix to perform the elimination

    Returns:
        [[], [], ...]: nested list representing the resulting upper-triangular matrix after elimination.
    """
    print("Performing Gaussian Elimination ===>\n")
    if matrix is None or len(matrix) == 0:
        print("Matrix is empty! Bail...")
        return
    if len(matrix) == 1:
        print("No need for elimination for a row vector!")
        return matrix
    
    # Get the matrix dimension.
    nrows = len(matrix)
    ncols = len(matrix[0])

    # Reorganize the matrix to move the zeroes to lower-left corner.
    matrix = organize(matrix)

    # Loop through the rows and perform the row eliminations.
    for i in range(1, nrows):
        row = matrix[i]
        for j in range(i):
            if row[j] != 0:
                row_elim(row, matrix[j], ncols, j + 1)
            
    print("Elimination succeeded:)\n")

    # TODO: deal with the cases where the elimination fails.

    print_matrix(matrix)

    return matrix
```
