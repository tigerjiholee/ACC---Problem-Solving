# [Bronze II] Cow Routing - 10675 

[문제 링크](https://www.acmicpc.net/problem/10675) 

### 성능 요약

메모리: 36504 KB, 시간: 120 ms

### 분류

구현

### 제출 일자

2025년 8월 24일 11:24:08

### 문제 설명

<p>Tired of the cold winter weather on her farm, Bessie the cow plans to fly to a warmer destination for vacation.  Unfortunately, she discovers that only one airline, Air Bovinia, is willing to sell tickets to cows, and that these tickets are somewhat complicated in structure.</p>

<p>Air Bovinia owns N planes (1 <= N <= 500), each of which flies on a specific "route" consisting of two or more cities.  For example, one plane might fly on a route that starts at city 1, then flies to city 5, then flies to city 2, and then finally flies to city 8.  No city appears multiple times in a route.  If Bessie chooses to utilize a route, she can board at any city along the route and then disembark at any city later along the route.  She does not need to board at the first city or disembark at the last city.  Each route has a certain cost, which Bessie must pay if she uses any part of the route, irrespective of the number of cities she visits along the route.</p>

<p>Bessie would like to find the cheapest way to travel from her farm (in city A) to her tropical destination (city B). Since she does not want to be confused by a complicated itinerary, she wants to use only a single route.  Please help her decide what is the minimum cost she must pay.</p>

### 입력 

 <p>The first line of input contains A, B, and N, separated by spaces.  </p>

<p>The next 2N lines describe the available routes, in two lines per route. The first line contains the cost of using the route (an integer in the range 1..1000), and the number of cities along the route (an integer in the range 1..500).  The second line contains a list of the cities in order along the route.  Each city is identified by an integer in the range 1..10,000.</p>

### 출력 

 <p>Output the minimum cost of a single route Bessie can use to travel from city A to city B.  If there is no such route, output -1.</p>

