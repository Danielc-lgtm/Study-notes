---
type: exercise
subject: ring-theory
difficulty: "⭐"
prereqs:
  - "Def - Euclidean Domain"
  - "Def - Greatest Common Divisor and Least Common Multiple"
  - "Def - Irreducible and Prime Elements"
  - "Def - Unit and Field"
tags: [algebra, ring-theory]
---

# Problem Statement

Work in the **Gaussian integers** $\mathbb{Z}[i]=\{a+bi:a,b\in\mathbb{Z}\}$, which form a Euclidean domain under the norm $\varphi(z)=N(z)=|z|^2$ (see [[Ex - The Gaussian integers form a Euclidean domain]]).

Use the **Euclidean algorithm** to compute a greatest common divisor of
$$11+7i\qquad\text{and}\qquad 18-i.$$
At each step, divide the larger element by the smaller, choosing the quotient $q$ by computing the exact complex ratio and **rounding each coordinate to the nearest integer** — so the remainder $r$ satisfies $\varphi(r)<\varphi(\text{divisor})$. Iterate until the remainder is $0$; the last non-zero remainder is a gcd.

Note that, unlike in $\mathbb{Z}$, the gcd is only defined **up to multiplication by a unit** ($\pm 1,\pm i$), so the answer is an associate class, not a single element.

**Recall:**

The objects in play are the Euclidean domain $\mathbb{Z}[i]$, division-with-remainder via nearest-Gaussian-integer rounding, the definition of a gcd, and the units of $\mathbb{Z}[i]$.

![[Def - Euclidean Domain#The Definition]]

In a [[Def - Euclidean Domain|Euclidean domain]] $(R,\varphi)$, for any $a,b$ with $b\neq 0$ there exist $q,r$ with $a=bq+r$ and $r=0$ or $\varphi(r)<\varphi(b)$. For $\mathbb{Z}[i]$ with $\varphi(z)=|z|^2$, the quotient $q$ is obtained by rounding the complex number $a/b$ to a nearest Gaussian integer; the resulting remainder $r=a-bq$ has $\varphi(r)\leq\tfrac12\varphi(b)<\varphi(b)$.

![[Def - Greatest Common Divisor and Least Common Multiple#The Definition]]

A **greatest common divisor** of $a$ and $b$ is an element $d$ with $d\mid a$, $d\mid b$, and such that any common divisor $d'$ (i.e. $d'\mid a$ and $d'\mid b$) also satisfies $d'\mid d$. Here $d\mid a$ means $a=dc$ for some $c\in R$. In a Euclidean domain a gcd always exists and is **unique up to associates**: if $d$ and $d'$ are both gcds then each divides the other, so $d'=ud$ for a unit $u$.

![[Def - Unit and Field#The Definition]]

The **units** of $\mathbb{Z}[i]$ are exactly the four norm-$1$ elements $\{1,-1,i,-i\}$: a unit $u$ satisfies $N(u)N(u^{-1})=1$, so $N(u)=1$, and $a^2+b^2=1$ has solutions $(\pm1,0),(0,\pm1)$.

The **norm is multiplicative**, $N(zw)=N(z)N(w)$, and this gives the useful divisibility obstruction: $d\mid z$ in $\mathbb{Z}[i]$ forces $N(d)\mid N(z)$ in $\mathbb{Z}$.

---

# Convergent Strategy

**Problem class.** This is a *computation* problem: execute a known algorithm on concrete inputs. As the [[Rings II — §2.3–2.4]] strategy records, "find a gcd in a Euclidean domain" is solved by running the Euclidean algorithm — the same loop as in $\mathbb{Z}$ — with the ring's division-with-remainder in place of integer division.

**Assumption pattern.** The ring is presented as a Euclidean domain, so the recognisable feature is that division-with-remainder is *available* and the size function $\varphi$ *strictly decreases* on remainders. A strictly decreasing sequence of non-negative integers must terminate; that is why the algorithm halts.

**Theorem routing.** The route is: repeatedly apply the [[Def - Euclidean Domain|Euclidean division]] step. Two facts make the last non-zero remainder a gcd. First, the equation $a=bq+r$ shows that *common divisors of $\{a,b\}$ and of $\{b,r\}$ are the same* (anything dividing two of $a,b,r$ divides the third). So the pair's set of common divisors is invariant down the chain. Second, the chain terminates at remainder $0$, at which point the last divisor divides the previous remainder exactly and hence — walking back up — divides everything, while being divisible by every common divisor. So it is a gcd.

**Key decision point.** The only subtle move is the *rounding* of the complex ratio $a/b$. Integer division has an unambiguous quotient; Gaussian division does not — the exact ratio $a/b$ is a point in $\mathbb{C}$, and one selects the nearest *lattice* point. When a coordinate of $a/b$ lands exactly on a half-integer, *either* of the two nearest integers works (both give a valid remainder of norm $<\varphi(b)$); the gcd is unaffected because it is only defined up to a unit anyway. Recognising that the *output is an associate class*, not a number, is the conceptual content of the exercise.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Rings II — §2.3–2.4#Legal Operations|the topic page's Legal Operations]]:

1. **Order the pair by norm.** Compare $\varphi(11+7i)$ and $\varphi(18-i)$ to decide which element to divide by which; divide the larger-norm element by the smaller.

2. **Divide with remainder by rounding the field-quotient.** Compute the exact complex number $a/b=a\bar b/N(b)$, round each coordinate to a nearest integer to get $q\in\mathbb{Z}[i]$, and set $r=a-bq$.

3. **Iterate the Euclidean step.** Replace the pair $(a,b)$ by $(b,r)$ and repeat; the norm of the remainder strictly decreases, so the process terminates.

4. **Read off the gcd as the last non-zero remainder.** When a remainder is $0$, the previous remainder is a gcd.

5. **Interpret the answer up to associates.** Since gcds in a Euclidean domain are unique only up to a unit, present the result as an associate class; a gcd of norm $1$ certifies the inputs are coprime.

---

# Hints

> [!note]- Hint 1
> This is the *same* Euclidean algorithm you run in $\mathbb{Z}$ — repeatedly replace the pair $(a,b)$ by $(b,r)$ where $r$ is the remainder of $a$ divided by $b$ — only the division step is different. Start by computing the norms $N(11+7i)$ and $N(18-i)$ to decide which element to divide by which.

> [!note]- Hint 2
> To divide $a$ by $b$ in $\mathbb{Z}[i]$: compute the genuine complex number $a/b$. The clean way is $a/b=a\bar b/(b\bar b)=a\bar b/N(b)$, which has rational real and imaginary parts. Then round *each* part to the nearest integer to obtain the quotient $q\in\mathbb{Z}[i]$, and set $r=a-bq$.

> [!note]- Hint 3
> First division: $\dfrac{18-i}{11+7i}=\dfrac{(18-i)(11-7i)}{170}=\dfrac{191-137i}{170}\approx 1.12-0.81i$. Round to $q=1-i$. Compute $r=(18-i)-(11+7i)(1-i)$. You should find a remainder of small norm. Now repeat with the pair $(11+7i,\;r)$.

> [!note]- Hint 4
> Keep iterating; the remainder norms strictly decrease, so you reach remainder $0$ quickly. The last *non-zero* remainder is a gcd. If that remainder turns out to be a unit (norm $1$, e.g. $\pm1$ or $\pm i$), then $11+7i$ and $18-i$ are *coprime*. Watch for a step where the exact ratio has a coordinate at exactly $1.5$: either rounding choice is fine.

---

# Solution

The Euclidean algorithm in $\mathbb{Z}[i]$ is the integer algorithm with one substitution: integer division becomes "divide in $\mathbb{C}$, round to the nearest Gaussian integer." Running the loop on $11+7i$ and $18-i$ terminates in four steps at a gcd of norm $1$ — so the two inputs are coprime.

**Step 0: Order the pair by norm.**

$N(18-i)=325>170=N(11+7i)$, so the first division is $18-i$ by $11+7i$.

> [!note]- Derivation
> $N(11+7i)=11^2+7^2=121+49=170$ and $N(18-i)=18^2+(-1)^2=324+1=325$. The Euclidean algorithm divides the larger by the smaller, so we begin by dividing $18-i$ (the dividend) by $11+7i$ (the divisor).
>
> As a sanity check on what to expect: $170=2\cdot5\cdot17$ and $325=5^2\cdot13$, so $\gcd(170,325)=5$ in $\mathbb{Z}$. Since $d\mid z$ forces $N(d)\mid N(z)$, any common divisor $d$ of $11+7i$ and $18-i$ has $N(d)\mid\gcd(170,325)=5$, hence $N(d)\in\{1,5\}$. So the algorithm will return either a unit (norm $1$ — inputs coprime) or an element of norm $5$.

**Step 1: Divide $18-i$ by $11+7i$.**

$$18-i=(11+7i)(1-i)+3i,\qquad N(3i)=9<170.$$

> [!note]- Derivation
> Compute the exact ratio, clearing the denominator with the conjugate:
> $$\frac{18-i}{11+7i}=\frac{(18-i)(11-7i)}{(11+7i)(11-7i)}=\frac{(18-i)(11-7i)}{170}.$$
> The numerator is $(18-i)(11-7i)=198-126i-11i+7i^2=198-7-137i=191-137i$. So
> $$\frac{18-i}{11+7i}=\frac{191-137i}{170}\approx 1.1235-0.8059\,i.$$
> Round each coordinate to a nearest integer: $1.1235\mapsto 1$, $-0.8059\mapsto -1$, giving the quotient $q=1-i$. The remainder is
> $$r=(18-i)-(11+7i)(1-i).$$
> Now $(11+7i)(1-i)=11-11i+7i-7i^2=11+7+(-11+7)i=18-4i$, so
> $$r=(18-i)-(18-4i)=3i.$$
> Check: $N(r)=N(3i)=9$, and $9<170=N(11+7i)$, so the Euclidean division is valid.

**Step 2: Divide $11+7i$ by $3i$.**

$$11+7i=(3i)(2-4i)+(-1+i),\qquad N(-1+i)=2<9.$$

> [!note]- Derivation
> Exact ratio:
> $$\frac{11+7i}{3i}=\frac{(11+7i)(-3i)}{(3i)(-3i)}=\frac{-33i-21i^2}{9}=\frac{21-33i}{9}=\frac{7-11i}{3}\approx 2.333-3.667\,i.$$
> Round: $2.333\mapsto 2$, $-3.667\mapsto -4$, so $q=2-4i$. The remainder is
> $$r=(11+7i)-(3i)(2-4i).$$
> Here $(3i)(2-4i)=6i-12i^2=12+6i$, so
> $$r=(11+7i)-(12+6i)=-1+i.$$
> Check: $N(r)=N(-1+i)=1+1=2$, and $2<9=N(3i)$. Valid.

**Step 3: Divide $3i$ by $-1+i$.**

$$3i=(-1+i)(2-i)+1,\qquad N(1)=1<2.$$

> [!note]- Derivation
> Exact ratio:
> $$\frac{3i}{-1+i}=\frac{3i(-1-i)}{(-1+i)(-1-i)}=\frac{-3i-3i^2}{2}=\frac{3-3i}{2}=1.5-1.5\,i.$$
> *Both* coordinates land exactly on half-integers — the rounding is genuinely ambiguous, and this is fine: either nearest integer yields a valid remainder. Take $q=2-i$ (rounding $1.5\mapsto 2$ and $-1.5\mapsto -1$). The remainder is
> $$r=3i-(-1+i)(2-i).$$
> Here $(-1+i)(2-i)=-2+i+2i-i^2=-2+1+3i=-1+3i$, so
> $$r=3i-(-1+3i)=1.$$
> Check: $N(r)=N(1)=1<2=N(-1+i)$. Valid. (Had we chosen $q=1-i$ instead, the remainder would be $r=3i-(-1+i)(1-i)=3i-2i=i$ — an associate of $1$, norm still $1$. The two choices differ by a unit and lead to the same gcd class.)

**Step 4: Divide $-1+i$ by $1$ — exact, remainder $0$.**

$$-1+i=1\cdot(-1+i)+0.$$

> [!note]- Derivation
> Dividing by the unit $1$ is exact: $(-1+i)/1=-1+i\in\mathbb{Z}[i]$, so $q=-1+i$ and $r=0$. The algorithm terminates: the last non-zero remainder was $1$ (from Step 3).

**Step 5: Read off the gcd.**

The last non-zero remainder is $1$, so $\gcd(11+7i,\,18-i)=1$ — up to units, $\{1,-1,i,-i\}$. The two Gaussian integers are **coprime**.

> [!note]- Derivation
> The Euclidean algorithm produced the chain of remainders
> $$18-i,\quad 11+7i,\quad 3i,\quad -1+i,\quad 1,\quad 0,$$
> and the last non-zero entry is $1$. This is a gcd of the original pair. The justification is the standard one: from each line $a=bq+r$, an element divides *two* of $a,b,r$ if and only if it divides the third, so the set of common divisors is identical for $(a,b)$ and for $(b,r)$ all the way down the chain; at the bottom, $1$ divides the previous remainder exactly, and walking the divisibilities back up shows $1$ divides both $11+7i$ and $18-i$, while every common divisor divides $1$.
>
> Since gcds in a Euclidean domain are unique only **up to associates**, the gcd is the associate class of $1$, namely the unit group $\{1,-1,i,-i\}$. A gcd that is a unit means the only common divisors of $11+7i$ and $18-i$ are units: the two elements are **coprime**. This is consistent with Step 0, where the norm obstruction allowed only $N(d)\in\{1,5\}$ for a common divisor — the algorithm has resolved the ambiguity in favour of $N(d)=1$. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** $\gcd(11+7i,\,18-i)=1$ in $\mathbb{Z}[i]$ (up to units); the two elements are coprime.
>
> $N(11+7i)=170$, $N(18-i)=325$; divide larger by smaller.
>
> Step 1. $\dfrac{18-i}{11+7i}=\dfrac{191-137i}{170}\approx1.12-0.81i\rightsquigarrow q=1-i$. Then $(11+7i)(1-i)=18-4i$ and $r=(18-i)-(18-4i)=3i$, $N(r)=9$.
>
> Step 2. $\dfrac{11+7i}{3i}=\dfrac{7-11i}{3}\approx2.33-3.67i\rightsquigarrow q=2-4i$. Then $(3i)(2-4i)=12+6i$ and $r=(11+7i)-(12+6i)=-1+i$, $N(r)=2$.
>
> Step 3. $\dfrac{3i}{-1+i}=\dfrac{3-3i}{2}=1.5-1.5i\rightsquigarrow q=2-i$ (half-integer case; either choice works). Then $(-1+i)(2-i)=-1+3i$ and $r=3i-(-1+3i)=1$, $N(r)=1$.
>
> Step 4. $-1+i=1\cdot(-1+i)+0$; remainder $0$, algorithm terminates.
>
> Last non-zero remainder: $1$. Hence a gcd is $1$, i.e. the associate class $\{1,-1,i,-i\}$. The inputs $11+7i$ and $18-i$ are coprime. $\blacksquare$

---

# Key Takeaways

**The Euclidean algorithm is ring-agnostic: it is the same loop in every Euclidean domain, with only the division step swapped.** The structure "replace $(a,b)$ by $(b,r)$, repeat until $r=0$, return the last non-zero remainder" is *identical* in $\mathbb{Z}$, in $F[X]$, and in $\mathbb{Z}[i]$. What changes is the local division-with-remainder routine and the size function $\varphi$ that guarantees termination. The single fact making the loop correct in any of these rings is that $a=bq+r$ implies $\{a,b\}$ and $\{b,r\}$ have *the same set of common divisors* — because anything dividing two of $a,b,r$ divides the third. So the gcd of the pair is an invariant of the loop, preserved at every step, and read off at the bottom. When you meet a gcd computation in any Euclidean domain, do not reinvent it: identify $\varphi$, identify how to divide-with-remainder, and run the standard loop.

**Division in $\mathbb{Z}[i]$ means dividing in $\mathbb{C}$ and snapping to the lattice — and the practical recipe is "multiply by the conjugate over the norm."** The quotient is *not* found inside $\mathbb{Z}[i]$; it is found in the field $\mathbb{C}$ and then rounded. The computational trick that makes this painless is $a/b=a\bar b/(b\bar b)=a\bar b/N(b)$: clearing the denominator with the conjugate turns the ratio into "a Gaussian integer divided by an ordinary positive integer", whose real and imaginary parts are visibly rational and easy to round. This is the same conjugate-rationalisation move used to divide complex numbers in elementary algebra; here it is the engine of every step. The general pattern — *to divide in a lattice ring, rationalise into the ambient field then round* — is exactly the mechanism proven to work in [[Ex - The Gaussian integers form a Euclidean domain]], and it is worth internalising as the default computational stance for $\mathbb{Z}[i]$, $\mathbb{Z}[\omega]$, and similar rings.

**A gcd is an associate class, not an element — and a gcd that is a unit means "coprime."** In $\mathbb{Z}$ one fixes the gcd to be positive and forgets that $\gcd$ is really only defined up to sign. In a general Euclidean domain there is no canonical sign, and the ambiguity is the full unit group: $\mathbb{Z}[i]$ has units $\{1,-1,i,-i\}$, so a "gcd" is one of four associates and there is no preferred representative. This shows up concretely in the half-integer rounding at Step 3: the two legitimate quotient choices produced remainders $1$ and $i$ — different elements, but associates, hence the *same* gcd class. The reader should expect, and not be alarmed by, such branch-dependence; the algorithm computes a well-defined associate class even though intermediate elements are not unique. And the special case is worth flagging as a recognised outcome: when the gcd class contains a *unit*, the inputs share no non-trivial common factor — they are coprime — which is precisely the situation that, in a PID, lets you write a Bézout identity $1=r\,a+s\,b$ and run the "irreducibles are prime" argument of [[Ex - In a principal ideal domain irreducibles are prime]].

**The norm pre-screens the answer: a common divisor's norm must divide the gcd of the norms.** Before running a single division, the multiplicative norm already constrains the outcome. Since $d\mid 11+7i$ and $d\mid 18-i$ force $N(d)\mid N(11+7i)$ and $N(d)\mid N(18-i)$, any common divisor has $N(d)\mid\gcd(170,325)=5$, so $N(d)\in\{1,5\}$. This narrows the gcd to two possibilities — a unit or a norm-$5$ element — *before* any computation, and it is a useful consistency check on the final answer. The general technique: when computing or estimating a gcd in a normed ring, first compute the gcd of the *norms* in $\mathbb{Z}$; it bounds what the true gcd can be, catches arithmetic slips, and sometimes (when $\gcd$ of the norms is $1$) settles coprimality outright with no algorithm at all.
