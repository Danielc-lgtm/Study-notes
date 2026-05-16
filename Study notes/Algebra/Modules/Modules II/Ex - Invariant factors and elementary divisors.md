---
type: exercise
subject: module-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Classification of Finitely Generated Abelian Groups"
  - "Thm - Chinese Remainder Theorem for Modules"
  - "Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain"
tags: [algebra, module-theory]
---

# Problem Statement

A finite abelian group can be written in two canonical ways:

- **Invariant-factor form:** $A\cong C_{d_1}\times C_{d_2}\times\cdots\times C_{d_s}$ with the divisibility chain $d_1\mid d_2\mid\cdots\mid d_s$ (each $d_i>1$).
- **Elementary-divisor form:** $A\cong C_{q_1}\times C_{q_2}\times\cdots\times C_{q_t}$, where each $q_j$ is a power of a prime.

1. Start from a group given by its **elementary divisors**: the multiset
$$\{2,\ 2,\ 4,\ 3,\ 9,\ 5\},$$
so $A\cong C_2\times C_2\times C_4\times C_3\times C_9\times C_5$. Convert $A$ to **invariant-factor form** $C_{d_1}\times\cdots\times C_{d_s}$ with $d_1\mid\cdots\mid d_s$.
2. Conversely, take a group given in invariant-factor form, say $B\cong C_6\times C_{60}$ (note $6\mid 60$), and convert it to **elementary-divisor form** — a product of cyclic groups of prime-power order.
3. State precisely the algorithm for each direction, and explain why both forms describe *the same* group, i.e. why the conversion is an isomorphism.

The point is to become fluent with the two canonical decompositions and the bookkeeping — a grid of prime-power exponents — that translates between them.

**Recall:**

The engine of both forms is the structure theorem.

![[Thm - Classification of Finitely Generated Abelian Groups#Formal Statement]]

That statement *is* the invariant-factor form: a finite abelian group is uniquely $C_{d_1}\times\cdots\times C_{d_s}$ with $d_1\mid\cdots\mid d_s$. The elementary-divisor form is obtained from it by splitting each cyclic factor along its prime factorisation, using the Chinese remainder theorem for modules.

![[Thm - Chinese Remainder Theorem for Modules#Formal Statement]]

Concretely, for $R=\mathbb{Z}$: if $n=p_1^{a_1}\cdots p_k^{a_k}$ with the $p_i$ distinct primes, then since the prime powers $p_i^{a_i}$ are pairwise coprime,
$$C_n\cong C_{p_1^{a_1}}\times\cdots\times C_{p_k^{a_k}}.$$
This both *splits* a cyclic group into prime-power pieces (forward direction) and *merges* coprime cyclic groups back into one (reverse direction). A prime power $p^a$ appearing as one of the factors is an **elementary divisor** of the group; the divisor $d_i$ in the chain $d_1\mid\cdots\mid d_s$ is an **invariant factor**. Both lists are uniquely determined by $A$.

---

# Convergent Strategy

**Problem class.** This is a *canonical-form conversion* problem. There is no theorem to "discover" — the group is already classified — only an algorithm to execute reliably. The skill being drilled is the bookkeeping that moves between the two normal forms guaranteed by [[Thm - Classification of Finitely Generated Abelian Groups]].

**Assumption pattern.** The input is a finite abelian group presented in *one* of the two canonical forms. The recognisable feature deciding the direction: if the cyclic orders are prime powers with no divisibility chain imposed, you are in elementary-divisor form and must *merge*; if the orders satisfy $d_1\mid d_2\mid\cdots$, you are in invariant-factor form and must *split*.

**Theorem routing.** [[Thm - Chinese Remainder Theorem for Modules]] is the only tool, used in two directions. Splitting $C_n$ into $\prod C_{p^a}$ uses it forwards (a cyclic group of composite order is a product of coprime cyclic pieces). Merging $\prod C_{p^a}$ into a single $C_n$ uses it backwards (a product of cyclic groups of *pairwise coprime* orders is cyclic). The structure theorem ([[Thm - Classification of Finitely Generated Abelian Groups]]) guarantees both target forms exist and are unique.

**Key decision point.** The whole computation is organised by a single device: a **grid of prime-power exponents**. List the primes dividing $|A|$ as rows; for each prime $p$, the elementary divisors that are powers of $p$ are entries in that row. The non-obvious insight is *how to read the grid in each direction*. To get elementary divisors, just read off every cell. To get invariant factors, you must align the prime-power factors by *largest-in-each-prime first*: $d_s$ takes the largest power of each prime, $d_{s-1}$ the next largest, and so on — padding with $1$ when a prime runs out. Reading the columns in the wrong order produces orders that violate the divisibility chain. That alignment rule is the one thing to get right.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Modules II — §3.3–3.4#Legal Operations|the topic page's Legal Operations]]:

1. **Split a cyclic group by the Chinese remainder theorem.** Factor the order $n=\prod p_i^{a_i}$; since the prime powers are pairwise coprime, $C_n\cong\prod_i C_{p_i^{a_i}}$. This breaks an invariant-factor cyclic group into elementary-divisor pieces.

2. **Merge coprime cyclic groups by the Chinese remainder theorem.** A product $\prod_j C_{q_j}$ of cyclic groups whose orders $q_j$ are *pairwise coprime* is itself cyclic, of order $\prod_j q_j$. This is the reverse use, assembling invariant factors from elementary divisors.

3. **Build the prime-power exponent grid.** Tabulate, for each prime $p\mid|A|$, the sorted list of exponents $a$ such that $p^a$ is an elementary divisor. This is the common data structure for both directions.

4. **Align by largest-first to produce the invariant-factor chain.** Form $d_s$ from the largest prime power in each row, $d_{s-1}$ from the next, etc., padding short rows with the empty product $1$. The resulting $d_1\mid\cdots\mid d_s$ automatically satisfies the divisibility chain.

5. **Verify by order.** Check $\prod d_i=\prod q_j=|A|$; the product of all cyclic orders is invariant, so a mismatch flags an arithmetic slip.

---

# Hints

> [!note]- Hint 1
> Both directions are governed by one fact: $C_{mn}\cong C_m\times C_n$ **whenever $\gcd(m,n)=1$** — the Chinese remainder theorem. It splits a cyclic group of composite order into coprime pieces, and (read backwards) merges coprime cyclic groups into one. The caution: $C_m\times C_n$ is cyclic *only* when $m,n$ are coprime — e.g. $C_2\times C_2\ne C_4$.

> [!note]- Hint 2
> Organise everything in a grid. One row per prime dividing $|A|$; in each row, list (sorted ascending) the exponents $a$ for which $p^a$ is an elementary divisor. For $\{2,2,4,3,9,5\}$: the prime $2$ row holds $2^1,2^1,2^2$; the prime $3$ row holds $3^1,3^2$; the prime $5$ row holds $5^1$.

> [!note]- Hint 3
> To read invariant factors from the grid: the *largest* invariant factor $d_s$ collects the largest prime power from every row; $d_{s-1}$ collects the next-largest from each row; continue, and when a prime's row is exhausted, contribute a factor of $1$ (i.e. nothing). The number of invariant factors equals the length of the *longest* row. Right-align the rows — think of padding the short rows with $1$'s on the *left*.

> [!note]- Hint 4
> For part 1: longest row is the prime-$2$ row, length $3$, so there are $3$ invariant factors. Column-by-column from the right: $d_3$ gets $(2^2,3^2,5^1)$, $d_2$ gets $(2^1,3^1,1)$, $d_1$ gets $(2^1,1,1)$. Multiply within each column. For part 2: factor $6=2\cdot 3$ and $60=2^2\cdot 3\cdot 5$, then split each of $C_6,C_{60}$ into prime-power cyclic factors.

---

# Solution

The unifying device is the prime-power exponent grid. Reading the grid cell-by-cell gives elementary divisors; reading it by right-aligned columns gives invariant factors.

## Part 1 — elementary divisors $\{2,2,4,3,9,5\}$ to invariant-factor form

**Step 1: Build the prime-power exponent grid.**

Group the elementary divisors by their underlying prime. The prime $2$ contributes $\{2,2,4\}=\{2^1,2^1,2^2\}$; the prime $3$ contributes $\{3,9\}=\{3^1,3^2\}$; the prime $5$ contributes $\{5\}=\{5^1\}$.

> [!note]- Derivation
> The given group is $A\cong C_2\times C_2\times C_4\times C_3\times C_9\times C_5$, an external direct product of six cyclic groups, each of prime-power order. Sort the factors by the prime they belong to:
>
> | prime $p$ | elementary divisors (powers of $p$), ascending |
> |---|---|
> | $2$ | $2^1,\ 2^1,\ 2^2$ |
> | $3$ | $3^1,\ 3^2$ |
> | $5$ | $5^1$ |
>
> The order of $A$ is the product of all of them: $|A|=2\cdot 2\cdot 4\cdot 3\cdot 9\cdot 5=2^4\cdot 3^3\cdot 5=16\cdot 27\cdot 5=2160$. We will use this at the end as a check.
>
> The longest row is the prime-$2$ row, with $3$ entries. This number, $3$, will be the number of invariant factors $s$, because each invariant factor draws *at most one* prime power from each row, and the prime needing the most factors dictates the count.

**Step 2: Read invariant factors by right-aligned columns.**

Right-align the three rows and read columns from the right. The largest invariant factor $d_3=2^2\cdot 3^2\cdot 5=180$; the middle $d_2=2^1\cdot 3^1=6$; the smallest $d_1=2^1=2$. The divisibility chain $2\mid 6\mid 180$ holds.

> [!note]- Derivation
> Right-align the rows, padding shorter rows on the *left* with $1$'s (the empty product), so that every row has length $s=3$:
>
> | prime $p$ | $d_1$ column | $d_2$ column | $d_3$ column |
> |---|---|---|---|
> | $2$ | $2^1$ | $2^1$ | $2^2$ |
> | $3$ | $1$ | $3^1$ | $3^2$ |
> | $5$ | $1$ | $1$ | $5^1$ |
>
> Each invariant factor is the product down its column:
> $$d_1=2^1\cdot 1\cdot 1=2,$$
> $$d_2=2^1\cdot 3^1\cdot 1=6,$$
> $$d_3=2^2\cdot 3^2\cdot 5^1=4\cdot 9\cdot 5=180.$$
> **Why right-alignment gives the divisibility chain.** Within each prime row, the entries are sorted ascending, so reading left-to-right the exponent of $p$ never decreases. Right-alignment makes column $d_{i}$ hold, for each prime, an exponent $\le$ the exponent in column $d_{i+1}$. Hence $d_i\mid d_{i+1}$ for every $i$, prime by prime — that is exactly the divisibility chain. Indeed $2\mid 6$ and $6\mid 180$. ✓
>
> **Check by order.** $d_1 d_2 d_3=2\cdot 6\cdot 180=2160=|A|$. ✓
>
> So in invariant-factor form,
> $$A\cong C_2\times C_6\times C_{180},\qquad 2\mid 6\mid 180.$$

**Step 3: Confirm this is the same group via the Chinese remainder theorem.**

Splitting each invariant factor by CRT returns the original elementary-divisor list, so $C_2\times C_6\times C_{180}\cong C_2\times C_2\times C_4\times C_3\times C_9\times C_5$.

> [!note]- Derivation
> By [[Thm - Chinese Remainder Theorem for Modules|the Chinese remainder theorem]], $C_n\cong\prod_i C_{p_i^{a_i}}$ when $n=\prod p_i^{a_i}$. Split each invariant factor:
> - $C_2$: already a prime power, $C_2$.
> - $C_6$ with $6=2\cdot 3$: $C_6\cong C_2\times C_3$.
> - $C_{180}$ with $180=2^2\cdot 3^2\cdot 5$: $C_{180}\cong C_4\times C_9\times C_5$.
>
> Collecting all the prime-power factors:
> $$C_2\times C_6\times C_{180}\cong C_2\ \times\ (C_2\times C_3)\ \times\ (C_4\times C_9\times C_5),$$
> whose multiset of orders is $\{2,2,3,4,9,5\}=\{2,2,4,3,9,5\}$ — exactly the elementary divisors we started with. The two presentations are therefore isomorphic; they are two readings of the same grid.

## Part 2 — invariant-factor form $C_6\times C_{60}$ to elementary-divisor form

**Step 4: Split each invariant factor into prime powers.**

Factor $6=2\cdot 3$ and $60=2^2\cdot 3\cdot 5$; the Chinese remainder theorem gives $C_6\cong C_2\times C_3$ and $C_{60}\cong C_4\times C_3\times C_5$. Hence the elementary divisors of $B$ are $\{2,4,3,3,5\}$.

> [!note]- Derivation
> The group $B\cong C_6\times C_{60}$ is in invariant-factor form, since $6\mid 60$. Apply [[Thm - Chinese Remainder Theorem for Modules|CRT]] to each factor.
>
> - $6=2^1\cdot 3^1$, coprime prime powers $2$ and $3$, so $C_6\cong C_2\times C_3$.
> - $60=2^2\cdot 3^1\cdot 5^1$, pairwise coprime prime powers $4,3,5$, so $C_{60}\cong C_4\times C_3\times C_5$.
>
> Therefore
> $$B\cong C_6\times C_{60}\cong(C_2\times C_3)\times(C_4\times C_3\times C_5)=C_2\times C_4\times C_3\times C_3\times C_5.$$
> The elementary divisors of $B$ are the multiset of these prime-power orders:
> $$\{2,\ 4,\ 3,\ 3,\ 5\}.$$
> Note $C_3$ occurs with multiplicity two — both invariant factors $6$ and $60$ are divisible by $3$ to the first power, so the prime-$3$ row of the grid is $3^1,3^1$. Multiplicities are genuine data; $C_3\times C_3$ is not $C_9$.
>
> **Sanity grid for $B$** (rows = primes, entries = exponents ascending):
>
> | prime $p$ | elementary divisors |
> |---|---|
> | $2$ | $2^1,\ 2^2$ |
> | $3$ | $3^1,\ 3^1$ |
> | $5$ | $5^1$ |
>
> Reading this grid back by right-aligned columns: $d_2=2^2\cdot 3^1\cdot 5^1=60$ and $d_1=2^1\cdot 3^1\cdot 1=6$ — recovering $C_6\times C_{60}$, confirming the round trip. **Check by order:** $|B|=6\cdot 60=360$ and $2\cdot 4\cdot 3\cdot 3\cdot 5=360$. ✓

**Step 5: State the two algorithms.**

The two directions are inverse readings of the prime-power grid: split-by-CRT to get elementary divisors, right-align-and-multiply to get invariant factors.

> [!note]- Derivation
> **Invariant factors $\to$ elementary divisors.** Given $C_{d_1}\times\cdots\times C_{d_s}$ with $d_1\mid\cdots\mid d_s$: factor each $d_i=\prod_p p^{a_{i,p}}$ into prime powers and replace $C_{d_i}$ by $\prod_p C_{p^{a_{i,p}}}$ (dropping any $p^0=1$ factor), justified by [[Thm - Chinese Remainder Theorem for Modules|CRT]] since distinct prime powers are coprime. The collected prime-power orders are the elementary divisors.
>
> **Elementary divisors $\to$ invariant factors.** Given a multiset of prime powers: build the grid with one row per prime $p$, listing the $p$-power exponents in ascending order. Let $s$ be the length of the longest row. Right-align all rows (pad short rows on the left with $1$). The $i$-th invariant factor $d_i$ is the product down the $i$-th column. Then $d_1\mid d_2\mid\cdots\mid d_s$ holds automatically, because within each row exponents increase left-to-right, so after right-alignment each column's $p$-exponent is $\le$ the next column's.
>
> **Why they are mutually inverse, and why each output is the unique canonical form.** Splitting then re-merging returns the original group: by [[Thm - Chinese Remainder Theorem for Modules|CRT]], $C_{d_i}\cong\prod_p C_{p^{a_{i,p}}}$, an *isomorphism*, so no information is lost — the group is literally unchanged, only re-bracketed. The structure theorem [[Thm - Classification of Finitely Generated Abelian Groups]] guarantees the invariant-factor list is *unique*, and the prime-power decomposition of each (uniquely determined) $d_i$ is unique by unique factorisation in $\mathbb{Z}$; hence the elementary-divisor multiset is unique too. Both lists are isomorphism invariants of $A$, and the grid is the bijection between them.

> [!note]- Complete formal solution
> **Part 1.** $A\cong C_2\times C_2\times C_4\times C_3\times C_9\times C_5$. Grid of $p$-power exponents, ascending: prime $2$: $(1,1,2)$; prime $3$: $(1,2)$; prime $5$: $(1)$. Longest row length $3$, so $3$ invariant factors. Right-align (pad left with $1$) and multiply columns: $d_1=2\cdot 1\cdot 1=2$, $d_2=2\cdot 3\cdot 1=6$, $d_3=4\cdot 9\cdot 5=180$. The chain $2\mid 6\mid 180$ holds and $2\cdot 6\cdot 180=2160=|A|$. So $A\cong C_2\times C_6\times C_{180}$. By [[Thm - Chinese Remainder Theorem for Modules|CRT]], splitting $C_6\cong C_2\times C_3$ and $C_{180}\cong C_4\times C_9\times C_5$ recovers the original factors, confirming the isomorphism.
>
> **Part 2.** $B\cong C_6\times C_{60}$ with $6\mid 60$. Factor $6=2\cdot 3$, $60=2^2\cdot 3\cdot 5$. By [[Thm - Chinese Remainder Theorem for Modules|CRT]], $C_6\cong C_2\times C_3$ and $C_{60}\cong C_4\times C_3\times C_5$, so $B\cong C_2\times C_4\times C_3\times C_3\times C_5$. The elementary divisors are the multiset $\{2,4,3,3,5\}$; $|B|=2\cdot4\cdot3\cdot3\cdot5=360=6\cdot 60$.
>
> Both conversions are inverse readings of the prime-power exponent grid: split-by-CRT reads off elementary divisors; right-align-and-multiply reads off invariant factors. Each output is unique by [[Thm - Classification of Finitely Generated Abelian Groups]] and unique factorisation in $\mathbb{Z}$. $\blacksquare$

---

# Key Takeaways

**One group, two canonical lists, one grid relating them.** A finite abelian group carries two equally canonical fingerprints: the invariant factors $d_1\mid\cdots\mid d_s$ and the elementary divisors (a multiset of prime powers). They are not rival descriptions but two readings of a single object — the grid of prime-power exponents, rows indexed by primes. Reading the grid *cell by cell* lists the elementary divisors; reading it by *right-aligned columns* lists the invariant factors. Internalising this picture means you never memorise two separate algorithms: you memorise the grid and how to read it both ways. The general lesson for canonical-form problems: when an object has two normal forms, look for the shared underlying data structure of which each form is a projection.

**The Chinese remainder theorem is a two-way valve, and coprimality is the gate.** $C_{mn}\cong C_m\times C_n$ holds *exactly* when $\gcd(m,n)=1$. Forwards, it splits a cyclic group of composite order into its prime-power constituents; backwards, it fuses cyclic groups of pairwise coprime orders into one. Every conversion in this exercise is one of these two moves. The single error to guard against is applying the merge to *non-coprime* orders: $C_2\times C_2$ is emphatically *not* $C_4$ — the former has every non-identity element of order $2$, the latter has an element of order $4$. So when merging, first verify pairwise coprimality; that is the entire content of "why $C_2\times C_3=C_6$ but $C_2\times C_2\ne C_4$". This same valve, [[Thm - Chinese Remainder Theorem for Modules]], is what powers the primary (prime-power) decomposition in the structure theory of modules over any Euclidean domain.

**Right-alignment, largest-first, is what manufactures the divisibility chain.** The defining constraint of invariant-factor form is $d_1\mid d_2\mid\cdots\mid d_s$. This is not automatic — it is *engineered* by the alignment rule. Within each prime's row the exponents are sorted ascending; right-aligning the rows and multiplying down columns guarantees that, prime by prime, the exponent in $d_i$ never exceeds the exponent in $d_{i+1}$, which is precisely $d_i\mid d_{i+1}$. The largest invariant factor $d_s$ is the *exponent* (least common multiple of all element orders) of the group, since it absorbs the top power of every prime. If you instead align *left* (smallest-first), you get a valid product of cyclic groups with the same order, but the divisibility chain fails and it is not the canonical form. The trigger "I need invariant factors" should fire "build the grid, right-align, read columns" — and the trigger "I need elementary divisors" should fire "factor each $d_i$, list the prime powers".

**Multiplicity is real data: $C_p\times C_p$ is not $C_{p^2}$.** In Part 2 the prime $3$ produced *two* copies of $C_3$, because both invariant factors $6$ and $60$ carried exactly one factor of $3$. These two $C_3$'s cannot be merged — their orders are not coprime — and they are not the same as a single $C_9$. The number of times a fixed prime power $p^a$ appears among the elementary divisors is an isomorphism invariant, counting independent cyclic summands of that exact order. This is why the elementary-divisor *multiset* (not just its underlying set) is the invariant, and why, when you classify all abelian groups of a given order, you are counting *partitions* of each prime's exponent — the theme of [[Ex - Classifying abelian groups of a given order]]. Whenever you decompose, track multiplicities; collapsing $C_p\times C_p$ to $C_{p^2}$ silently changes the group.
