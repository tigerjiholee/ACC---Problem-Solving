# [Gold V] Milk Exchange - 31649 

[문제 링크](https://www.acmicpc.net/problem/31649) 

### 성능 요약

메모리: 58016 KB, 시간: 208 ms

### 분류

구현, 애드 혹, 시뮬레이션

### 제출 일자

2025년 11월 2일 10:50:34

### 문제 설명

<p>Farmer John's $N$ $(1 \leq N \leq 2 \cdot 10^5)$ cows are lined up in a circle such that for each $i$ in $1,2,\dots,N-1$, the cow to the right of cow $i$ is cow $i+1$, and the cow to the right of cow $N$ is cow $1$. The $i$th cow has a bucket with integer capacity $a_i$ $(1 \leq a_i \leq 10^9)$ liters. All buckets are initially full.</p>

<p>Every minute, the cows exchange milk according to a string $s_1s_2\dots s_N$ consisting solely of the characters $\text{‘L’}$ and $\text{‘R’}$. if the $i$th cow has at least $1$ liter of milk, she will pass $1$ liter of milk to the cow to her left if $s_i=\text{‘L’}$, or to the right if $s_i=\text{‘R’}$. All exchanges happen simultaneously (i.e., if a cow has a full bucket but gives away a liter of milk but also receives a liter, her milk is preserved). If a cow's total milk ever ends up exceeding $a_i$, then the excess milk will be lost.</p>

<p>FJ wants to know: after $M$ minutes $(1 \leq M \leq 10^9$), what is the total amount of milk left among all cows?</p>

### 입력 

 <p>The first line contains $N$ and $M$.</p>

<p>The second line contains a string $s_1s_2\dots s_N$ consisting solely of the characters $\text{‘L’}$ or $\text{‘R’}$, denoting the direction each cow will pass their milk in.</p>

<p>The third line contains integers $a_1, a_2, \dots, a_N$, the capacities of each bucket.</p>

### 출력 

 <p>Output an integer, the sum of milk among all cows after $M$ minutes.</p>

<p><strong>Note that the large size of integers involved in this problem may require the use of 64-bit integer data types (e.g., a "long long" in C/C++).</strong></p>

