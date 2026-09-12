---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Sard's Theorem for Smooth Maps"
  - "Thm - Taylor's Theorem in Several Variables"
  - "Def - Regular and Critical Points"
  - "Def - Set of Measure Zero on a Manifold"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

This exercise isolates and proves, with explicit constants, the last and quantitatively decisive step in the proof of [[Thm - Sard's Theorem for Smooth Maps|Sard's theorem]] — the estimate on the image of the *deeply critical set*, where enough derivatives vanish that Taylor's theorem crushes the map.

Let $f:U\to\mathbb{R}^n$ be smooth on an open set $U\subseteq\mathbb{R}^m$. For an integer $k\ge0$ define the **$k$-th deeply critical set**
$$
C_k=
\begin{cases}
U, & k=0,\\[4pt]
\{x\in U:\ \partial^\alpha f_i(x)=0\ \text{for all }1\le|\alpha|\le k\ \text{and all }1\le i\le n\}, & k\ge1,
\end{cases}
$$
where $\alpha\in\mathbb{N}^m$ is a multi-index, $|\alpha|=\alpha_1+\cdots+\alpha_m$, and $\partial^\alpha f_i=\partial_1^{\alpha_1}\cdots\partial_m^{\alpha_m}f_i$ is the corresponding partial derivative of the $i$-th component $f_i$ of $f$. In words: for $k\ge1$, a point lies in $C_k$ when *every* partial derivative of *every* component of $f$, of order between $1$ and $k$, vanishes there; and $C_0$ is the whole domain, imposing no condition (there are no derivatives of order between $1$ and $0$).

**Part (a) — the estimate.** Let $\bar B\subset U$ be a closed ball. Prove that if
$$(k+1)\,n>m,$$
then $f(C_k\cap\bar B)$ has Lebesgue measure zero in $\mathbb{R}^n$. Extract explicit constants from [[Thm - Taylor's Theorem in Several Variables|Taylor's theorem]]: exhibit a constant $c$, depending only on $m$, $k$, and a bound on the order-$(k+1)$ derivatives of $f$ over a cube containing $\bar B$, such that a cube of side $\delta$ meeting $C_k$ maps into a set of diameter at most $c\,\delta^{k+1}$, and run the subdivision argument to make the total image volume tend to zero.

**Part (b) — a smooth curve cannot fill the plane.** Deduce that a smooth map $f:\mathbb{R}\to\mathbb{R}^2$ cannot be surjective. (This is Part (a) with $m=1$, $n=2$, $k=0$, exhausting $\mathbb{R}$ by closed intervals.)

**Part (c) — but a continuous one can.** By contrast, there exists a *continuous* surjection $\mathbb{R}\to\mathbb{R}^2$ — the **Peano space-filling curve** extends a continuous surjection $[0,1]\to[0,1]^2$. State this contrast precisely and identify exactly which hypothesis of Part (a) fails for the Peano curve, so that smoothness (in fact a local Lipschitz bound) is seen to be the load-bearing assumption.

**Recall:**

The tools are Taylor's theorem with its integral remainder, the definition of a Lebesgue-null set through coverings by boxes, and the notion of a critical point.

![[Thm - Taylor's Theorem in Several Variables#Statement]]

To restate the exact form we use: for $f\in C^{k+1}$ on a convex open set containing the segment from $x$ to $x+h$,
$$f_i(x+h)=\sum_{|\alpha|\le k}\frac{\partial^\alpha f_i(x)}{\alpha!}\,h^\alpha+R_i(x,h),\qquad R_i(x,h)=\int_0^1(k+1)(1-t)^k\!\!\sum_{|\alpha|=k+1}\frac{\partial^\alpha f_i(x+th)}{\alpha!}\,h^\alpha\,dt,$$
with $h^\alpha=\prod_j h_j^{\alpha_j}$ and $\alpha!=\prod_j\alpha_j!$. When $x\in C_k$ (for $k\ge1$) all the polynomial terms of orders $1$ through $k$ vanish, leaving only $f_i(x+h)=f_i(x)+R_i(x,h)$; when $k=0$ the sum $\sum_{|\alpha|\le0}$ is just $f_i(x)$ and the same identity holds with no condition on $x$.

![[Def - Regular and Critical Points#The Definition]]

A point $x\in U$ is a [[Def - Regular and Critical Points|critical point]] of $f$ if the differential $d_xf:\mathbb{R}^m\to\mathbb{R}^n$ is not surjective; equivalently $\operatorname{rank}Df(x)<n$.

![[Def - Set of Measure Zero on a Manifold#The Definition]]

$S\subseteq\mathbb{R}^n$ is **Lebesgue-null** if for every $\varepsilon>0$ there are countably many boxes $Q_i$ with $S\subseteq\bigcup_iQ_i$ and $\sum_i\operatorname{vol}(Q_i)<\varepsilon$ (see [[Def - Lebesgue Measure]]). We use: any set contained, for arbitrarily small $\varepsilon$, in *finitely* many boxes of total volume $<\varepsilon$ is null; and a countable union of null sets is null.

Two elementary combinatorial identities enter the constants. First, the number of multi-indices $\alpha\in\mathbb{N}^m$ of a fixed order $|\alpha|=d$ is finite. Second, the multinomial theorem $\big(\sum_{j=1}^m1\big)^d=\sum_{|\alpha|=d}\frac{d!}{\alpha!}$ gives $\sum_{|\alpha|=d}\frac{1}{\alpha!}=\frac{m^d}{d!}$, which is the sum we shall meet when bounding the remainder.

---

# Convergent Strategy

**Problem class.** This is a *quantitative covering* problem: the goal is a measure-zero statement, and the only way to reach it is to produce, for each $\varepsilon>0$, an explicit finite cover of $f(C_k\cap\bar B)$ of total volume below $\varepsilon$. The signature is the phrase "has measure zero" attached to the image of a set on which a map degenerates; the reaction is to control *how much a small cube can grow* under $f$, and then to add up the volumes of the images of many small cubes.

**Assumption pattern.** The hypothesis "$x\in C_k$" is used in exactly one way: it kills the low-order Taylor terms, so that the displacement $f(x+h)-f(x)$ is governed entirely by the order-$(k+1)$ remainder, which is $O(|h|^{k+1})$. The hypothesis "$(k+1)n>m$" is used in exactly one way: it makes the exponent $m-(k+1)n$ in the final volume bound *negative*, so that the bound $\to0$ as the subdivision is refined. Neither hypothesis does anything else, and recognising this tells you where each must appear in the proof.

**Theorem routing.** The route is: (i) fix a cube $Q_0\supset\bar B$ and let $K$ bound the order-$(k+1)$ derivatives of every component over $Q_0$; (ii) apply [[Thm - Taylor's Theorem in Several Variables|Taylor's theorem]] at a point $x\in C_k$ to bound $|f(x+h)-f(x)|\le c\,|h|_\infty^{k+1}$ with $c$ explicit in $K,m,k$; (iii) subdivide $Q_0$ into $r^m$ subcubes of side $\delta=L/r$; each subcube meeting $C_k$ maps into a set of diameter $\le c'\delta^{k+1}$, hence into a box of volume $\le(c'\delta^{k+1})^n$; (iv) sum over the at most $r^m$ relevant subcubes to get total image volume $\le c'^n L^{(k+1)n}\,r^{m-(k+1)n}\to0$. Then Part (b) is the case $m=1,n=2,k=0$, and Part (c) contrasts it with the Peano curve, which is only continuous and satisfies *no* Lipschitz bound, so step (ii) has no analogue.

**Key decision point.** The decisive move is to measure displacements in the **maximum norm** $|h|_\infty=\max_j|h_j|$ rather than the Euclidean norm. This is not cosmetic: a cube of side $\delta$ is exactly a max-norm ball of radius $\delta/2$, so "points in a common subcube differ by at most $\delta$ in $|\cdot|_\infty$" is exact, and the image, lying within diameter $c'\delta^{k+1}$, is contained in a *cube* whose $n$-volume we can write down. Matching the norm to the geometry of the subdivision is what keeps every constant explicit. The second decision is the unified treatment of $k=0$ by declaring $C_0=U$: with no vanishing hypothesis the same Taylor identity (order-$0$ polynomial plus first-order remainder) gives the plain Lipschitz bound, and Part (b) drops out as a special case rather than as a separate argument.

---

# Legal Operations Used

The moves below are the §10.2 operations for the measure-theoretic core of Sard's theorem; they will be renumbered against [[Gauge Theory X — Fredholm Maps, Transversality, and Degree#Legal Operations|the topic page's Legal Operations]] once it is assembled.

1. **Localise to a cube and bound the top-order derivatives there.** Replace the open $U$ by a compact cube $Q_0\supseteq\bar B$; on it, continuity of the derivatives gives a finite bound $K$ on all order-$(k+1)$ partials, uniform over $Q_0$. Compactness is what converts "smooth" into a usable numerical constant.

2. **Kill the low-order Taylor terms using membership in $C_k$.** At a deeply critical point $x\in C_k$, every polynomial term of orders $1,\dots,k$ in Taylor's expansion vanishes, so $f(x+h)-f(x)$ equals the order-$(k+1)$ remainder.

3. **Bound the remainder by an explicit power of the displacement.** Estimate the integral remainder using $|h^\alpha|\le|h|_\infty^{k+1}$, the derivative bound $K$, and the multinomial identity $\sum_{|\alpha|=k+1}1/\alpha!=m^{k+1}/(k+1)!$, to get $|f(x+h)-f(x)|_\infty\le c\,|h|_\infty^{k+1}$ with $c=Km^{k+1}/(k+1)!$.

4. **Convert a diameter bound into a volume bound.** A subset of $\mathbb{R}^n$ of $|\cdot|_\infty$-diameter $D$ sits inside a cube of side $D$, of volume $D^n$; apply this with $D\le c'\delta^{k+1}$.

5. **Subdivide and sum.** Cut $Q_0$ (side $L$) into $r^m$ subcubes of side $\delta=L/r$; sum the image-volumes of the subcubes meeting $C_k$ to get a total bounded by $c'^nL^{(k+1)n}r^{m-(k+1)n}$.

6. **Send the mesh to infinity in the good exponent regime.** When $(k+1)n>m$ the exponent $m-(k+1)n<0$, so the total volume $\to0$ as $r\to\infty$; this certifies the null-set conclusion.

7. **Exhaust an unbounded domain by a countable union of balls.** For $U=\mathbb{R}^m$ apply the local statement to each ball $\bar B_j$ of a countable exhaustion and use that a countable union of null sets is null.

---

# Hints

> [!note]- Hint 1
> Write $y=f(x+h)$ for $x\in C_k$ and $x+h$ in the same small cube. You want to show $y$ cannot move far from $f(x)$. Which theorem expresses $f(x+h)-f(x)$ in terms of derivatives of $f$ at $x$, and what happens to that expression when all derivatives of orders $1$ through $k$ vanish at $x$?

> [!note]- Hint 2
> Apply Taylor's theorem to order $k$. Because $x\in C_k$, the polynomial part collapses to $f(x)$, leaving $f(x+h)-f(x)=R(x,h)$, the order-$(k+1)$ remainder. Bound $|R(x,h)|$: over a fixed compact cube the $(k+1)$-st derivatives are bounded by some $K$; use $|h^\alpha|\le|h|_\infty^{k+1}$ and the identity $\sum_{|\alpha|=k+1}1/\alpha!=m^{k+1}/(k+1)!$.

> [!note]- Hint 3
> You now have $|f(x+h)-f(x)|_\infty\le c\,|h|_\infty^{k+1}$ on each small cube meeting $C_k$. Cut the big cube $Q_0$ of side $L$ into $r^m$ subcubes of side $\delta=L/r$. Each subcube that meets $C_k$ has its image contained in a cube of side $\le 2c\,\delta^{k+1}$ (why $2c$?), of $n$-volume $\le(2c)^n\delta^{(k+1)n}$. There are at most $r^m$ such subcubes. Add up.

> [!note]- Hint 4
> The total is $\le r^m\cdot(2c)^n(L/r)^{(k+1)n}=(2c)^nL^{(k+1)n}\,r^{\,m-(k+1)n}$. When is the exponent of $r$ negative, so this tends to $0$? That is exactly the hypothesis $(k+1)n>m$. For Part (b) take $m=1,n=2,k=0$: every interval $[-j,j]$ maps to a null set, so $\mathbb{R}$ maps to a countable union of null sets. For Part (c), ask which line of the argument the Peano curve violates.

---

# Solution

The heart of the matter is a single inequality: on a deeply critical set, a smooth map contracts distances to the power $k+1$, because Taylor's theorem says the first surviving term is of order $k+1$. Once a small cube of side $\delta$ maps into a region of size $\delta^{k+1}$, a volume count over $r^m$ subcubes gives total image volume $\sim r^{m-(k+1)n}$, which collapses precisely when $(k+1)n>m$. Part (b) is the smallest instance, and Part (c) shows that without the derivative bound — with mere continuity — the collapse fails and the plane can be filled.

**Step 0: Fix the geometry and the derivative bound.**

Enclose $\bar B$ in a closed cube $Q_0\subseteq U$ of side length $L$, and let $K<\infty$ bound every order-$(k+1)$ partial of every component of $f$ over $Q_0$.

> [!note]- Derivation
> Since $\bar B\subset U$ is compact and $U$ open, choose a closed axis-aligned cube $Q_0$ with $\bar B\subseteq Q_0\subseteq U$; write $L$ for its side length (operation 1). The cube $Q_0$ is compact and convex — convexity matters because Taylor's theorem needs the segment from $x$ to $x+h$ to lie in the domain, and any segment between two points of a cube stays in the cube.
> For each component $f_i$ ($1\le i\le n$) and each multi-index $\alpha$ with $|\alpha|=k+1$, the partial $\partial^\alpha f_i$ is continuous (as $f$ is smooth), hence bounded on the compact set $Q_0$. As there are finitely many such $(i,\alpha)$, we may set
> $$K:=\max_{1\le i\le n}\ \max_{|\alpha|=k+1}\ \sup_{\xi\in Q_0}\bigl|\partial^\alpha f_i(\xi)\bigr|\ <\ \infty\qquad\text{(finite max of continuous functions on a compact set).}$$
> This single number $K$ is the only quantitative input from $f$; everything downstream is combinatorics and geometry.

**Step 1: On a subcube meeting $C_k$, the map contracts to order $k+1$.**

If $x\in C_k$ and $x+h\in Q_0$, then $|f(x+h)-f(x)|_\infty\le c\,|h|_\infty^{k+1}$ with $c=\dfrac{K\,m^{k+1}}{(k+1)!}$.

> [!note]- Derivation
> Fix $x\in C_k\cap Q_0$ and $h$ with $x+h\in Q_0$; the segment $[x,x+h]\subseteq Q_0\subseteq U$ by convexity. Apply [[Thm - Taylor's Theorem in Several Variables|Taylor's theorem]] to the component $f_i$ at $x$ with increment $h$, to order $k$ (legitimate since $f_i\in C^{k+1}$ on the convex set $Q_0$):
> $$f_i(x+h)=\sum_{|\alpha|\le k}\frac{\partial^\alpha f_i(x)}{\alpha!}\,h^\alpha+R_i(x,h),\qquad R_i(x,h)=\int_0^1(k+1)(1-t)^k\!\!\sum_{|\alpha|=k+1}\frac{\partial^\alpha f_i(x+th)}{\alpha!}\,h^\alpha\,dt.$$
> **Kill the low-order terms (operation 2).** For $k\ge1$, membership $x\in C_k$ means $\partial^\alpha f_i(x)=0$ for all $1\le|\alpha|\le k$; the only surviving polynomial term is the one with $\alpha=0$, namely $f_i(x)$. For $k=0$ the sum $\sum_{|\alpha|\le0}$ is by definition the single term $f_i(x)$, and $C_0=U$ imposes nothing. Either way,
> $$f_i(x+h)-f_i(x)=R_i(x,h)\qquad\text{(vanishing of }\partial^\alpha f_i(x)\text{ for }1\le|\alpha|\le k\text{, resp. emptiness of that range when }k=0\text{).}$$
> **Bound the remainder (operation 3).** In each subcube we measure with the maximum norm; write $|h|_\infty=\max_j|h_j|$. Then $|h^\alpha|=\prod_j|h_j|^{\alpha_j}\le\prod_j|h|_\infty^{\alpha_j}=|h|_\infty^{|\alpha|}=|h|_\infty^{k+1}$ for $|\alpha|=k+1$ (since each $|h_j|\le|h|_\infty$). For $t\in[0,1]$ the point $x+th\in[x,x+h]\subseteq Q_0$, so $|\partial^\alpha f_i(x+th)|\le K$ by Step 0. Taking absolute values inside the integral (the triangle inequality for integrals is licensed because the integrand is continuous in $t$, hence Riemann-integrable on $[0,1]$),
> $$|R_i(x,h)|\le\int_0^1(k+1)(1-t)^k\!\!\sum_{|\alpha|=k+1}\frac{|\partial^\alpha f_i(x+th)|}{\alpha!}\,|h^\alpha|\,dt\le(k+1)\Bigl(\int_0^1(1-t)^k\,dt\Bigr)K\,|h|_\infty^{k+1}\!\!\sum_{|\alpha|=k+1}\frac{1}{\alpha!}.$$
> Now $\int_0^1(1-t)^k\,dt=\tfrac{1}{k+1}$ (elementary integration), and $\sum_{|\alpha|=k+1}\tfrac{1}{\alpha!}=\tfrac{m^{k+1}}{(k+1)!}$ (the multinomial identity recalled above). Substituting, the two factors $(k+1)$ and $\tfrac{1}{k+1}$ cancel:
> $$|R_i(x,h)|\le(k+1)\cdot\frac{1}{k+1}\cdot K\cdot|h|_\infty^{k+1}\cdot\frac{m^{k+1}}{(k+1)!}=\frac{K\,m^{k+1}}{(k+1)!}\,|h|_\infty^{k+1}=c\,|h|_\infty^{k+1}.$$
> This bound holds for each component $i$, so taking the maximum over $i$,
> $$|f(x+h)-f(x)|_\infty=\max_{1\le i\le n}|f_i(x+h)-f_i(x)|=\max_i|R_i(x,h)|\le c\,|h|_\infty^{k+1},\qquad c=\frac{K\,m^{k+1}}{(k+1)!}.$$
> The constant $c$ depends only on $K$ (hence on $f$ and $Q_0$), on the domain dimension $m$, and on $k$, as required.

**Step 2: Subdivide the cube; each relevant subcube has a small image.**

Cutting $Q_0$ into $r^m$ subcubes of side $\delta=L/r$, every subcube that meets $C_k$ maps into a set of $|\cdot|_\infty$-diameter at most $c'\delta^{k+1}$ with $c'=2c$, hence into an $n$-cube of volume at most $(c')^n\delta^{(k+1)n}$.

> [!note]- Derivation
> Partition $Q_0$ into $r^m$ congruent closed subcubes of side $\delta=L/r$ by cutting each edge into $r$ equal pieces (operation 5). Consider a subcube $Q$ that meets $C_k$, and pick a point $x\in C_k\cap Q$. Any two points of $Q$ differ by at most $\delta$ in each coordinate, so for every $y\in Q$ we have $|y-x|_\infty\le\delta$; and $Q\subseteq Q_0$, so $y=x+(y-x)\in Q_0$. By Step 1 applied with $h=y-x$,
> $$|f(y)-f(x)|_\infty\le c\,|y-x|_\infty^{k+1}\le c\,\delta^{k+1}\qquad\text{(Step 1, then }|y-x|_\infty\le\delta\text{).}$$
> Thus every image point $f(y)$ lies within $|\cdot|_\infty$-distance $c\,\delta^{k+1}$ of the fixed point $f(x)$, so $f(Q)$ has $|\cdot|_\infty$-diameter at most $2c\,\delta^{k+1}=c'\delta^{k+1}$ (two points of $f(Q)$ are each within $c\delta^{k+1}$ of $f(x)$, so within $2c\delta^{k+1}$ of each other; hence the factor $c'=2c$). A set of $|\cdot|_\infty$-diameter $D$ is contained in a closed cube of side $D$ centred at any of its points (operation 4), so $f(Q)$ lies in a cube of side $c'\delta^{k+1}$, whose $n$-dimensional volume is
> $$\operatorname{vol}\bigl(\text{enclosing cube of }f(Q)\bigr)\le\bigl(c'\delta^{k+1}\bigr)^n=(c')^n\,\delta^{(k+1)n}\qquad\text{(volume of an }n\text{-cube of side }c'\delta^{k+1}\text{).}$$

**Step 3: Sum the volumes and send the mesh to infinity.**

Summing over the at most $r^m$ subcubes meeting $C_k$ gives total image volume $\le(c')^nL^{(k+1)n}\,r^{\,m-(k+1)n}$, which tends to $0$ as $r\to\infty$ exactly because $(k+1)n>m$; hence $f(C_k\cap\bar B)$ is Lebesgue-null.

> [!note]- Derivation
> The subcubes meeting $C_k$ number at most $r^m$ (the total number of subcubes). Their images cover $f(C_k\cap Q_0)\supseteq f(C_k\cap\bar B)$, since every point of $C_k\cap Q_0$ lies in some subcube. Adding the volume bound of Step 2 over these subcubes (subadditivity of outer measure; operation 5), with $\delta=L/r$,
> $$
> \sum_{Q\cap C_k\ne\varnothing}\operatorname{vol}\bigl(\text{enclosing cube of }f(Q)\bigr)
> \le r^m\cdot(c')^n\Bigl(\tfrac{L}{r}\Bigr)^{(k+1)n}
> =(c')^n L^{(k+1)n}\,r^{\,m-(k+1)n}\qquad\text{(there are }\le r^m\text{ terms, each }\le(c')^n(L/r)^{(k+1)n}\text{).}
> $$
> **Use the exponent hypothesis (operation 6).** By assumption $(k+1)n>m$, so the exponent $m-(k+1)n$ is strictly negative; therefore $r^{\,m-(k+1)n}\to0$ as $r\to\infty$, and with it the whole bound:
> $$\lim_{r\to\infty}(c')^nL^{(k+1)n}\,r^{\,m-(k+1)n}=0\qquad\text{(a negative power of }r\text{ tends to }0\text{).}$$
> Hence for every $\varepsilon>0$ there is an $r$ for which $f(C_k\cap\bar B)$ is covered by finitely many boxes (the enclosing cubes) of total volume $<\varepsilon$. By the definition of a Lebesgue-null set recalled above, $f(C_k\cap\bar B)$ has measure zero in $\mathbb{R}^n$. This proves Part (a).

**Step 4: Part (b) — a smooth curve $\mathbb{R}\to\mathbb{R}^2$ is not surjective.**

With $m=1$, $n=2$, $k=0$ the hypothesis reads $(0+1)\cdot2=2>1=m$; so $f([-j,j])=f(C_0\cap[-j,j])$ is null for each $j$, and $f(\mathbb{R})=\bigcup_j f([-j,j])$ is a countable union of null sets, hence null, hence a proper subset of $\mathbb{R}^2$.

> [!note]- Derivation
> Let $f:\mathbb{R}\to\mathbb{R}^2$ be smooth. Take $k=0$, so $C_0=\mathbb{R}$ (the whole domain), and note $(k+1)n=2>1=m$. For each $j\in\mathbb{N}$ apply Part (a) to the closed interval $\bar B_j=[-j,j]\subset\mathbb{R}$ (a closed ball of the line): since $C_0\cap\bar B_j=\bar B_j$,
> $$f(\bar B_j)=f(C_0\cap\bar B_j)\ \text{is Lebesgue-null in }\mathbb{R}^2\qquad\text{(Part (a) with }m=1,n=2,k=0\text{).}$$
> Here Step 1 with $k=0$ is exactly the Lipschitz bound: $|f(x+h)-f(x)|_\infty\le c\,|h|_\infty$ with $c=K m^{1}/1!=K=\sup_{[-j,j]}\max(|f_1'|,|f_2'|)$, and no derivative of $f$ needs to vanish — the "deeply critical set" $C_0$ is everything. Now exhaust the line (operation 7):
> $$f(\mathbb{R})=f\Bigl(\bigcup_{j\in\mathbb{N}}[-j,j]\Bigr)=\bigcup_{j\in\mathbb{N}}f([-j,j])\qquad\text{(}f\text{ of a union is the union of images).}$$
> A countable union of Lebesgue-null sets is Lebesgue-null (split $\varepsilon$ as $\sum_j\varepsilon/2^{j+1}$ over the covers), so $f(\mathbb{R})$ is null in $\mathbb{R}^2$. Since $\mathbb{R}^2$ itself is not null (the unit square has area $1$), $f(\mathbb{R})\ne\mathbb{R}^2$: the map is not surjective.
> This also recovers, and now proves in full, the assertion of the companion drill [[Ex - Sard's Theorem for Polynomial Maps|Ex - Sard's Theorem for Polynomial Maps]] Part (c), where every point of $\mathbb{R}$ was seen to be critical for $f:\mathbb{R}\to\mathbb{R}^2$.

**Step 5: Part (c) — a continuous surjection exists, and which hypothesis it breaks.**

There is a continuous surjection $P:[0,1]\to[0,1]^2$ (the Peano curve), which extends to a continuous surjection $\mathbb{R}\to\mathbb{R}^2$; it violates precisely Step 1 — it satisfies no bound $|P(x+h)-P(x)|\le c|h|$ — so the whole argument of Part (a) has no purchase on it, and continuity alone does not forbid filling the plane.

> [!note]- Derivation
> The Peano curve is the uniform limit of piecewise-linear maps $P_r:[0,1]\to[0,1]^2$ whose images are polygonal paths visiting all $4^r$ subsquares of a dyadic subdivision of $[0,1]^2$; the limit $P=\lim_rP_r$ exists and is continuous (uniform Cauchy sequence) and surjective (its image is closed and dense in $[0,1]^2$, hence all of it). Extending $P$ periodically and rescaling gives a continuous surjection $\mathbb{R}\to\mathbb{R}^2$. We do not reprove this classical construction here; we only need its existence and the qualitative fact that it fills area.
> The point is *which* step of Part (a) fails for $P$. Step 1 produced the estimate $|f(x+h)-f(x)|_\infty\le c\,|h|_\infty^{k+1}$ from a bound $K$ on derivatives. A space-filling curve cannot obey even the weakest such bound, $|P(x+h)-P(x)|\le c|h|$ (the $k=0$ Lipschitz case): if it did, then by the very argument of Steps 2–3 its image $P([0,1])$ would be null, contradicting surjectivity onto $[0,1]^2$, which has positive area. So $P$ is nowhere differentiable in any direction with a bounded difference quotient — its coordinate functions are continuous but not Lipschitz, and not $C^1$. Concretely, over a subinterval of length $\delta$ the curve $P$ traverses a whole subsquare of side $\sim\delta^{1/2}$, so $|P(x+h)-P(x)|$ is of order $|h|^{1/2}$, not $|h|$: the exponent $\tfrac12<1$ is exactly the failure of the Lipschitz bound, and it is enough to defeat the volume count. Thus the load-bearing hypothesis in Sard's Step 5 is not continuity but the *Lipschitz-to-power-$(k+1)$ contraction* that smoothness supplies through Taylor's theorem.

> [!note]- Complete formal solution
> **Claim.** Let $f:U\to\mathbb{R}^n$ be smooth, $U\subseteq\mathbb{R}^m$ open, $\bar B\subset U$ a closed ball, and $(k+1)n>m$. Then $f(C_k\cap\bar B)$ is Lebesgue-null. Consequently a smooth $f:\mathbb{R}\to\mathbb{R}^2$ is not surjective, though a continuous one can be.
>
> Fix a closed cube $Q_0$ with $\bar B\subseteq Q_0\subseteq U$, side $L$, and set $K=\max_{i}\max_{|\alpha|=k+1}\sup_{Q_0}|\partial^\alpha f_i|<\infty$ (continuous partials on a compact set).
>
> *Estimate.* Let $x\in C_k\cap Q_0$ and $x+h\in Q_0$; the segment lies in $Q_0$. By [[Thm - Taylor's Theorem in Several Variables|Taylor's theorem]] to order $k$, and since all partials of orders $1,\dots,k$ of each $f_i$ vanish at $x$ (vacuously when $k=0$),
> $$f_i(x+h)-f_i(x)=\int_0^1(k+1)(1-t)^k\!\!\sum_{|\alpha|=k+1}\frac{\partial^\alpha f_i(x+th)}{\alpha!}h^\alpha\,dt.$$
> Using $|h^\alpha|\le|h|_\infty^{k+1}$, $|\partial^\alpha f_i|\le K$ on $Q_0$, $\int_0^1(1-t)^k dt=\tfrac1{k+1}$, and $\sum_{|\alpha|=k+1}\tfrac1{\alpha!}=\tfrac{m^{k+1}}{(k+1)!}$, we get $|f(x+h)-f(x)|_\infty\le c|h|_\infty^{k+1}$ with $c=\tfrac{Km^{k+1}}{(k+1)!}$.
>
> *Covering.* Cut $Q_0$ into $r^m$ subcubes of side $\delta=L/r$. A subcube $Q$ meeting $C_k$ at $x$ has, for every $y\in Q$, $|y-x|_\infty\le\delta$, so $|f(y)-f(x)|_\infty\le c\delta^{k+1}$; thus $f(Q)$ lies in a cube of side $2c\delta^{k+1}$, of volume $\le(2c)^n\delta^{(k+1)n}$. Summing over the $\le r^m$ such subcubes, the image is covered by boxes of total volume
> $$\le r^m(2c)^n(L/r)^{(k+1)n}=(2c)^nL^{(k+1)n}\,r^{\,m-(k+1)n}\xrightarrow[r\to\infty]{}0,$$
> because $m-(k+1)n<0$. Hence $f(C_k\cap\bar B)$ is null.
>
> *Part (b).* For smooth $f:\mathbb{R}\to\mathbb{R}^2$ take $m=1,n=2,k=0$, so $C_0=\mathbb{R}$ and $(k+1)n=2>1$; each $f([-j,j])$ is null, so $f(\mathbb{R})=\bigcup_j f([-j,j])$ is a countable union of null sets, null, hence $\ne\mathbb{R}^2$: not surjective.
>
> *Part (c).* The Peano curve is a continuous surjection $[0,1]\to[0,1]^2$, extending to $\mathbb{R}\to\mathbb{R}^2$. It cannot satisfy any Lipschitz bound $|P(x+h)-P(x)|\le c|h|$, for that bound would (by the covering argument with $k=0$) force $P([0,1])$ to be null, contradicting that it is all of $[0,1]^2$. The failed hypothesis is the derivative bound $K$ of the estimate: continuity alone yields no contraction, so the volume count collapses. $\blacksquare$

> [!warning] Illegal but tempting: measuring displacement in the Euclidean norm inside a cube
> It is tempting to run the estimate with the Euclidean norm $|h|_2$ throughout. This is not wrong, but it forces a stray dimensional constant: two points of a subcube of side $\delta$ differ by at most $\sqrt{m}\,\delta$ in $|\cdot|_2$, and a Euclidean ball of radius $D$ sits in a cube of side $2D$, so the clean identities "subcube diameter $=\delta$" and "diameter-$D$ set $\subseteq$ cube of side $D$" both acquire factors of $\sqrt m$ and $2$. The argument still works — those constants are harmless since only the *power* of $r$ decides convergence — but the bookkeeping is needlessly heavier. The extra condition that makes the Euclidean route as clean as the max-norm route is simply to track the constants $\sqrt m$ and $2^n$ explicitly; matching the norm to the cube geometry avoids them from the start.

---

# Key Takeaways

**Vanishing derivatives buy a higher power in Taylor's remainder, and that power is the whole game.** The reusable principle is that if all derivatives of orders $1$ through $k$ vanish at a point, then near that point a smooth map moves by only $O(|h|^{k+1})$, because Taylor's theorem makes the first surviving term the order-$(k+1)$ remainder. This converts *analytic* information (derivatives vanish) into *metric* information (small cubes have small images), and the metric statement is what a measure argument can consume. The trigger to reach for this is any situation where you must bound the *size of an image* of a set on which a map degenerates — critical sets in Sard's theorem, but also the estimation of oscillation for maps with vanishing jets, and the Morse-theoretic control of level sets near degenerate critical points. The transferable diagnostic: whenever you can name how many derivatives vanish, you know the contraction exponent, and the covering count $r^{m-(k+1)n}$ tells you immediately whether the image is null.

**A measure-zero conclusion is always a race between how many cubes you use and how small their images are.** The subdivision argument is a template worth internalising: cut the domain into $r^m$ pieces, bound each image volume by $(\text{side})^n$ where the side shrinks like $\delta^{k+1}=(L/r)^{k+1}$, and let the total $r^m\cdot(L/r)^{(k+1)n}=L^{(k+1)n}r^{m-(k+1)n}$ decide the outcome by the sign of the exponent. Nullity holds exactly when the shrinking of images outpaces the proliferation of pieces, i.e. when $(k+1)n>m$. This exponent-counting is the same bookkeeping that governs Hausdorff-dimension estimates, the box-counting dimension of self-similar sets, and the Minkowski content of graphs; recognising it lets you predict the answer before writing a single constant, and the explicit constants ($c=Km^{k+1}/(k+1)!$, side factor $2c$) matter only for the finitely-many-boxes certificate, never for the convergence itself.

**Smoothness, not continuity, is the hypothesis that forbids space-filling — and the Peano curve marks the exact boundary.** The contrast between Parts (b) and (c) is the conceptual payoff: a smooth (even merely $C^1$, even merely Lipschitz) curve in the plane has null image and cannot be surjective, whereas a continuous curve can fill the plane completely. The dividing line is the contraction estimate of Step 1; a Lipschitz map obeys $|f(x+h)-f(x)|\le c|h|$, and that single inequality already forces null image, while the Peano curve fails it with the tell-tale Hölder exponent $\tfrac12$ ("length-$\delta$ input covers a $\sqrt\delta$-sized square"). The lesson for the whole of transversality theory is that the measure-theoretic smallness underlying Sard's theorem — and hence the genericity of regular values that powers the [[Thm - Sard-Smale Theorem|Sard–Smale theorem]] and degree theory — rests entirely on differentiability, which is why the infinite-dimensional generalisation must be built on smooth (Fredholm) maps and never on merely continuous ones. When you meet a claim that "generic behaviour is regular", trace it back and you will find a Taylor estimate of exactly this shape doing the work. The companion pages [[Ex - Sard's Theorem for Polynomial Maps]] and [[Thm - Sard's Theorem for Smooth Maps]] place this estimate in the full proof of Sard's theorem.
