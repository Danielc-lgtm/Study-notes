---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Krull Dimension and Height"
  - "Def - Noetherian Ring"
  - "Thm - Noether Normalization"
  - "Def - Algebraic Independence and Transcendence Degree"
  - "Thm - Integral Extensions Preserve Dimension"
  - "Thm - Krull's Height Theorem (Principal Ideal Theorem)"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. For a ring $R$, $R[T]$ is the [[Def - Polynomial Ring|polynomial ring]] in one indeterminate and $R[T_1,\dots,T_n]$ the polynomial ring in $n$ indeterminates; $\dim R$ is the [[Def - Krull Dimension and Height|Krull dimension]] and $\operatorname{ht}\mathfrak p$ the height of a prime $\mathfrak p$. For a field $k$ and a $k$-algebra $A$ that is a [[Def - Integral Domain|domain]], $\operatorname{trdeg}_k A := \operatorname{trdeg}_k \operatorname{Frac}(A)$ is the [[Def - Algebraic Independence and Transcendence Degree|transcendence degree]] of its fraction field. We write $\mathbb A^n_k = \operatorname{Spec} k[T_1,\dots,T_n]$ for affine $n$-space. The full registry is on [[Commutative Algebra XII — Dimension Theory]].

---

# Statement

> **Theorem (dimension of a polynomial ring).** Let $k$ be a field. Then
> $$\dim k[T_1, \dots, T_n] = n.$$
> More precisely, for any [[Def - Noetherian Ring|Noetherian]] ring $A$ of finite dimension,
> $$\dim A[T] = 1 + \dim A, \qquad \text{hence} \qquad \dim A[T_1,\dots,T_n] = n + \dim A.$$

> **Companion (the transcendence-degree formula).** For a finitely generated algebra $A$ over a field $k$ that is an integral domain,
> $$\dim A = \operatorname{trdeg}_k \operatorname{Frac}(A),$$
> and for every prime $\mathfrak p \in \operatorname{Spec} A$ the chain-length is exact: $\operatorname{ht}\mathfrak p + \dim A/\mathfrak p = \dim A$.

The two statements are related: $k[T_1,\dots,T_n]$ is a finitely generated domain with fraction field $k(T_1,\dots,T_n)$ of transcendence degree $n$, so the companion gives $\dim k[T_1,\dots,T_n] = n$ directly; the Noetherian recursion $\dim A[T] = 1 + \dim A$ gives the same number without the domain hypothesis and is what makes the result inductive.

---

# Motivation

This is the theorem that makes "dimension" deserve its name. The whole point of [[Def - Krull Dimension and Height|Krull dimension]] was to produce an algebraic number that equals the geometric dimension of a variety, and the most basic sanity check is that affine $n$-space $\mathbb A^n_k$ — the variety with coordinate ring $k[T_1,\dots,T_n]$ — should come out $n$-dimensional. Without this theorem, Krull dimension is just a definition chasing chains of primes with no guarantee it counts anything recognisable; with it, the definition is anchored to geometry, and every other dimension computation in algebraic geometry is bootstrapped from it.

The inequality $\dim k[T_1,\dots,T_n] \geq n$ is easy and was already visible at the level of the definition: the flag of linear subspaces gives the chain of primes
$$(0) \subsetneq (T_1) \subsetneq (T_1,T_2) \subsetneq \cdots \subsetneq (T_1,\dots,T_n),$$
which is dual to the tower $\mathbb A^n \supsetneq \{T_1=0\} \supsetneq \{T_1=T_2=0\} \supsetneq \cdots \supsetneq \{0\}$ of $n$ strict steps. The entire difficulty — and the entire content — is the *reverse* inequality $\dim \leq n$: the assertion that you cannot do better, that no clever chain of primes is longer than the obvious linear one. That a polynomial ring has no "hidden" extra dimensions is exactly the kind of finiteness statement that requires real theorems, and there are two complementary routes to it. The geometric route, via [[Thm - Noether Normalization|Noether normalization]], says every finitely generated domain is a finite extension of a polynomial ring, and finite extensions do not change dimension. The recursive route, via [[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's height theorem]] and a localization argument, computes $\dim A[T]$ from $\dim A$ one variable at a time. Both are worth knowing because they generalise in different directions.

---

# Sources and Targets

**Sources (Input Broadening)**

The first disguised source is **"$A$ is a finitely generated domain over a field"**, the property $B$. The bridge to the theorem is [[Thm - Noether Normalization|Noether normalization]]: such an $A$ is a finite (hence [[Def - Integral Element and Integral Extension|integral]]) extension of a polynomial subring $k[y_1,\dots,y_d]$, and [[Thm - Integral Extensions Preserve Dimension|integral extensions preserve dimension]], so $\dim A = d = \operatorname{trdeg}_k A$. The non-obvious step is that an abstract chain-of-primes count is computed by the concrete, linear-algebra quantity $\operatorname{trdeg}$. *Example problem:* compute $\dim k[X,Y]/(Y^2 - X^3)$ — the cuspidal cubic is a domain of transcendence degree $1$, so its dimension is $1$, a curve.

The second disguised source is **"$A$ is Noetherian and I have already computed $\dim A$"**, when you meet $A[T]$. The bridge is the recursion $\dim A[T] = 1 + \dim A$: adjoining one polynomial variable raises dimension by exactly one. This is non-obvious because $A[T]$ has *many* more primes than $A$ (each prime of $A$ spreads into a whole line of primes of $A[T]$), yet the longest chain grows by only one. *Example problem:* $\dim \mathbb Z[T] = 1 + \dim \mathbb Z = 2$ — the arithmetic plane has dimension two.

The third disguised source is **"a prime $\mathfrak p$ is given by an explicit set of $r$ generators in $k[T_1,\dots,T_n]$"**. Via Krull's height theorem $\operatorname{ht}\mathfrak p \leq r$, and via the companion formula $\dim A/\mathfrak p = n - \operatorname{ht}\mathfrak p \geq n - r$: the quotient variety has dimension at least $n - r$. The non-obvious content is the lower bound on the dimension of a variety cut out by $r$ equations. *Example problem:* a single nonzero non-unit $f$ cuts out a hypersurface $V(f)$ of dimension exactly $n-1$.

**Targets (Output Amplification)**

Combine the conclusion $\dim k[T_1,\dots,T_n] = n$ with **the companion exactness $\operatorname{ht}\mathfrak p + \dim A/\mathfrak p = \dim A$**. The further result $E$ is that *every* maximal chain of primes in a finitely generated domain has the same length (the ring is **catenary**), so codimension is well defined and additive — the backbone of intersection theory. This is non-obvious because Krull dimension is a *supremum*, and a priori different maximal chains could have different lengths.

Combine the recursion with **induction on $n$** to get $\dim A[T_1,\dots,T_n] = n + \dim A$ for any finite-dimensional Noetherian $A$. The further result is the dimension of any **affine space over a base**: $\dim \mathbb A^n_A = n + \dim A$, the fact that fibre dimension and base dimension simply add for the trivial family.

Combine $\dim k[T_1,\dots,T_n] = n$ with **Krull's principal ideal theorem** to get that the zero set of a single irreducible $f$ has dimension exactly $n-1$, and inductively that a complete intersection of $r$ equations has dimension $\geq n-r$ with equality in the regular case. This is the source of the **expected dimension** heuristic in enumerative geometry.

---

# Why Is It True

The geometric mechanism is one sentence: **a finitely generated domain is a finite cover of an affine space, a finite cover preserves dimension, and an affine space has dimension equal to its number of coordinates because coordinates are exactly a transcendence basis.** Unpack the three clauses and the theorem is inevitable.

First, *why dimension should equal transcendence degree*. The transcendence degree of $\operatorname{Frac}(A)$ over $k$ is the number of algebraically independent elements — the number of "free coordinates" the variety has. A chain of irreducible subvarieties $X = X_0 \supsetneq X_1 \supsetneq \cdots \supsetneq X_d$ must drop the transcendence degree of the function field by at least one at each strict step (passing to a strictly smaller irreducible subvariety imposes a genuine algebraic relation, killing one independent coordinate). So the longest chain has at most $\operatorname{trdeg}$ steps, giving $\dim \leq \operatorname{trdeg}$; and you can always realise that many steps by cutting one coordinate at a time, giving equality. Dimension counts independent coordinates, and that count is the transcendence degree.

Second, *why Noether normalization closes the gap for the polynomial ring itself*. You could try to prove $\dim k[T_1,\dots,T_n] \leq n$ by brute force, but chains of primes are hard to bound directly. Noether normalization sidesteps this: it exhibits any finitely generated domain $A$ as module-finite over a polynomial ring $k[y_1,\dots,y_d]$ with $d = \operatorname{trdeg}_k A$, and [[Thm - Integral Extensions Preserve Dimension|going-up/lying-over/incomparability]] force the two rings to have *equal* dimension (a chain upstairs lies over a chain downstairs of the same length, and no two distinct primes of the cover lie over the same prime in a chain). So $\dim A = \dim k[y_1,\dots,y_d]$, reducing every finitely generated domain to the polynomial case — and the polynomial case is pinned by its own transcendence degree $d$.

Third, *why the recursion $\dim A[T] = 1+\dim A$ holds without the domain hypothesis*. The inequality $\geq$ is the chain $\mathfrak p_0[T] \subsetneq \cdots \subsetneq \mathfrak p_d[T] \subsetneq (\mathfrak p_d, T)$, lifting a length-$d$ chain of $A$ to a length-$(d{+}1)$ chain of $A[T]$ by appending the variable. The inequality $\leq$ is the hard half and is where Noetherianity enters: above a fixed prime $\mathfrak p$ of $A$, the primes of $A[T]$ contracting to $\mathfrak p$ correspond to primes of $\kappa(\mathfrak p)[T]$ — a PID, dimension one — so each prime of $A$ can support a chain of length at most one in the fibre direction. Krull's height theorem bounds how these fibre-chains stack, and the total comes out $1 + \dim A$.

**The one-line summary: adjoining a variable adds exactly one to the dimension because a variable is one new free coordinate — algebraically, $\operatorname{trdeg}$ goes up by one — and no chain of primes can exploit it for more than one extra step.**

---

# What Makes This Hard

The trap is to think the easy inequality $\dim \geq n$ (the linear flag of primes) is the whole story; the entire mathematical content is the *upper* bound $\dim \leq n$, the assertion that no exotic chain beats the linear one, and that bound is not elementary — it requires either Noether normalization plus dimension-invariance under integral extensions, or Krull's height theorem plus a fibre analysis. The most common error is to "prove" $\dim A[T] = 1 + \dim A$ by only exhibiting the lifted chain (which gives $\geq$) and forgetting the genuinely hard $\leq$ direction, which needs Noetherianity — and indeed $\dim A[T]$ can exceed $1 + \dim A$ for non-Noetherian $A$ (it can be as large as $1 + 2\dim A$).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove the companion $\dim A = \operatorname{trdeg}_k A$ for finitely generated domains by Noether normalization plus dimension-invariance under integral extensions; specialise to $A = k[T_1,\dots,T_n]$ to get $\dim = n$. Separately, prove the recursion $\dim A[T] = 1 + \dim A$ for Noetherian $A$ by lifting chains (for $\geq$) and a height/fibre bound (for $\leq$).

**Subgoal decomposition:**

1. **Lower bound $\dim k[T_1,\dots,T_n] \geq n$.** Exhibit the chain $(0) \subsetneq (T_1) \subsetneq \cdots \subsetneq (T_1,\dots,T_n)$.
   - *Hint:* Each $(T_1,\dots,T_i)$ is prime because the quotient $k[T_{i+1},\dots,T_n]$ is a domain.
   - *Why needed:* Half of every dimension equality; the easy half.

2. **Noether normalization.** Any finitely generated domain $A$ over $k$ is module-finite over a polynomial subring $k[y_1,\dots,y_d]$, $d = \operatorname{trdeg}_k A$.
   - *Hint:* Cite [[Thm - Noether Normalization]].
   - *Why needed:* Reduces a general $A$ to the polynomial case and identifies $d$ with $\operatorname{trdeg}$.

3. **Dimension is invariant under the integral extension $k[y_1,\dots,y_d] \subseteq A$.** Hence $\dim A = \dim k[y_1,\dots,y_d]$.
   - *Hint:* [[Thm - Integral Extensions Preserve Dimension]] — lying over and going up lift chains up, incomparability stops two primes collapsing.
   - *Why needed:* Transports the unknown $\dim A$ to the polynomial ring.

4. **$\dim k[y_1,\dots,y_d] = d$.** Combine the lower bound (subgoal 1) with the upper bound $\dim \leq \operatorname{trdeg} = d$ (each strict drop in an irreducible-subvariety chain drops transcendence degree by $\geq 1$).
   - *Hint:* A strictly smaller irreducible subvariety has a strictly smaller function-field transcendence degree.
   - *Why needed:* Closes the polynomial case, hence (via 2–3) the companion formula.

5. **Recursion $\dim A[T] = 1 + \dim A$ for Noetherian $A$.** Lift a chain of $A$ to length $d+1$ in $A[T]$ for $\geq$; for $\leq$, bound chains by analysing primes contracting to each $\mathfrak p \in \operatorname{Spec} A$ via the fibre ring $\kappa(\mathfrak p)[T]$, a one-dimensional PID, using [[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's height theorem]].
   - *Hint:* Append $(\mathfrak p_d, T)$ to a lifted chain $\mathfrak p_0[T] \subsetneq \cdots \subsetneq \mathfrak p_d[T]$.
   - *Why needed:* Gives the result for any Noetherian base, without the domain hypothesis, and by induction $\dim A[T_1,\dots,T_n] = n + \dim A$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The linear flag is a chain of primes
> **Statement:** In $k[T_1,\dots,T_n]$, each ideal $\mathfrak p_i = (T_1,\dots,T_i)$ is prime, and $\mathfrak p_0 \subsetneq \mathfrak p_1 \subsetneq \cdots \subsetneq \mathfrak p_n$ is a chain of length $n$.
>
> **Hint:** Identify the quotient ring.
>
> **Why needed:** It is the witness for $\dim k[T_1,\dots,T_n] \geq n$.
>
> > [!note]- Full proof
> > The quotient $k[T_1,\dots,T_n]/(T_1,\dots,T_i) \cong k[T_{i+1},\dots,T_n]$ via the evaluation $T_1,\dots,T_i \mapsto 0$. A polynomial ring over a field is an [[Def - Integral Domain|integral domain]] (the product of leading terms is nonzero), so the quotient is a domain, and by [[Thm - Maximal and Prime Ideals via Quotients|the quotient criterion]] $\mathfrak p_i$ is prime. The inclusions are strict because $T_{i+1} \in \mathfrak p_{i+1} \setminus \mathfrak p_i$. Hence the displayed chain has $n+1$ primes and length $n$. $\square$

> [!note]- Lemma 2: A strict drop of irreducible subvarieties drops transcendence degree
> **Statement:** If $\mathfrak p \subsetneq \mathfrak q$ are primes of a finitely generated domain $A$ over $k$, then $\operatorname{trdeg}_k A/\mathfrak q < \operatorname{trdeg}_k A/\mathfrak p$.
>
> **Hint:** $A/\mathfrak q$ is a proper quotient domain of $A/\mathfrak p$; a nonzero element of the kernel is algebraic-dependence-creating.
>
> **Why needed:** It forces $\dim A \leq \operatorname{trdeg}_k A$, the hard upper bound.
>
> > [!note]- Full proof
> > Write $B = A/\mathfrak p$, a domain, and $\bar{\mathfrak q} = \mathfrak q/\mathfrak p \neq 0$ its image, so $A/\mathfrak q \cong B/\bar{\mathfrak q}$. Let $d = \operatorname{trdeg}_k \operatorname{Frac}(B)$. Pick $0 \neq t \in \bar{\mathfrak q}$. In $B/\bar{\mathfrak q}$ the image of $t$ is $0$. Suppose for contradiction $\operatorname{trdeg}_k \operatorname{Frac}(B/\bar{\mathfrak q}) = d$ as well; choose elements $\bar b_1,\dots,\bar b_d \in B/\bar{\mathfrak q}$ algebraically independent over $k$ and lifts $b_1,\dots,b_d \in B$. These $b_i$ are then algebraically independent in $B$ too, so they form a transcendence basis of $\operatorname{Frac}(B)$, and $t$ is algebraic over $k(b_1,\dots,b_d)$: there is a polynomial relation $\sum_j c_j(b) t^j = 0$ with $c_j \in k[b_1,\dots,b_d]$ and $c_0 \neq 0$ (clear the relation of $t$ and divide out, using that $B$ is a domain, so the lowest-degree term in $t$ can be taken nonzero). Reducing mod $\bar{\mathfrak q}$ kills every term with $j \geq 1$ (as $t \mapsto 0$) and leaves $\bar c_0(\bar b) = 0$, a nontrivial algebraic relation among $\bar b_1,\dots,\bar b_d$ — contradicting their independence. Hence $\operatorname{trdeg}_k \operatorname{Frac}(B/\bar{\mathfrak q}) < d$. $\square$

> [!note]- Lemma 3: Lifting a chain through one variable
> **Statement:** If $\mathfrak p_0 \subsetneq \cdots \subsetneq \mathfrak p_d$ is a chain of primes of $A$, then $\mathfrak p_0[T] \subsetneq \cdots \subsetneq \mathfrak p_d[T] \subsetneq (\mathfrak p_d, T)$ is a chain of primes of $A[T]$ of length $d+1$.
>
> **Hint:** $\mathfrak p[T]$ is the kernel of $A[T] \to (A/\mathfrak p)[T]$; $(\mathfrak p_d, T)$ is the kernel of $A[T] \to A/\mathfrak p_d$.
>
> **Why needed:** It gives $\dim A[T] \geq 1 + \dim A$.
>
> > [!note]- Full proof
> > For a prime $\mathfrak p \trianglelefteq A$, the set $\mathfrak p[T]$ of polynomials with all coefficients in $\mathfrak p$ is the kernel of the surjection $A[T] \to (A/\mathfrak p)[T]$ reducing coefficients; since $(A/\mathfrak p)[T]$ is a domain (polynomial ring over the domain $A/\mathfrak p$), $\mathfrak p[T]$ is prime. The inclusions $\mathfrak p_i[T] \subsetneq \mathfrak p_{i+1}[T]$ are strict (a constant in $\mathfrak p_{i+1}\setminus \mathfrak p_i$ witnesses it). Finally $(\mathfrak p_d, T)$ is the kernel of $A[T] \to A/\mathfrak p_d$ (reduce coefficients mod $\mathfrak p_d$ and set $T = 0$), with quotient the domain $A/\mathfrak p_d$, so it is prime; and $\mathfrak p_d[T] \subsetneq (\mathfrak p_d, T)$ strictly because $T \in (\mathfrak p_d,T) \setminus \mathfrak p_d[T]$. The chain has length $d+1$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> **Part A — the companion formula $\dim A = \operatorname{trdeg}_k A$ for a finitely generated domain $A/k$, and $\dim k[T_1,\dots,T_n] = n$.**
>
> By [[Thm - Noether Normalization|Noether normalization]], $A$ is module-finite — hence [[Def - Integral Element and Integral Extension|integral]] — over a polynomial subring $R = k[y_1,\dots,y_d]$, where $y_1,\dots,y_d$ is a transcendence basis of $\operatorname{Frac}(A)$, so $d = \operatorname{trdeg}_k A$. By [[Thm - Integral Extensions Preserve Dimension|invariance of dimension under integral extensions]], $\dim A = \dim R = \dim k[y_1,\dots,y_d]$.
>
> It remains to show $\dim k[y_1,\dots,y_d] = d$. The bound $\geq d$ is Lemma 1. For $\leq d$: a chain of primes $\mathfrak q_0 \subsetneq \cdots \subsetneq \mathfrak q_e$ in the domain $k[y_1,\dots,y_d]$ gives quotient domains $A/\mathfrak q_0 \twoheadleftarrow \cdots$ with strictly decreasing transcendence degrees by Lemma 2, starting from $\operatorname{trdeg}_k k[y_1,\dots,y_d] = d$ at $\mathfrak q_0 = (0)$ and ending $\geq 0$, so $e \leq d$. Hence $\dim k[y_1,\dots,y_d] = d$, and $\dim A = d = \operatorname{trdeg}_k A$. Taking $A = k[T_1,\dots,T_n]$ (its fraction field $k(T_1,\dots,T_n)$ has transcendence degree $n$) gives $\dim k[T_1,\dots,T_n] = n$.
>
> The exactness $\operatorname{ht}\mathfrak p + \dim A/\mathfrak p = \dim A$ follows from the same circle of ideas (Noether normalization adapted to the quotient, together with going-down for the normal polynomial subring); see [[Ex - Height plus dimension of the quotient equals dimension]] for the chain argument.
>
> ---
> **Part B — the recursion $\dim A[T] = 1 + \dim A$ for Noetherian $A$ of finite dimension.**
>
> *Lower bound.* If $\dim A = d$, take a chain of primes of length $d$ in $A$ and apply Lemma 3 to obtain a chain of length $d+1$ in $A[T]$; hence $\dim A[T] \geq 1 + \dim A$.
>
> *Upper bound.* Let $\mathfrak P_0 \subsetneq \cdots \subsetneq \mathfrak P_m$ be a chain of primes in $A[T]$, and let $\mathfrak p_i = \mathfrak P_i \cap A$ be their contractions, a (weakly) increasing chain in $A$. Group the $\mathfrak P_i$ by their contraction. Above a *fixed* prime $\mathfrak p$ of $A$, the primes of $A[T]$ contracting to $\mathfrak p$ are in bijection with the primes of the fibre ring $(A[T])\otimes_A \kappa(\mathfrak p) = \kappa(\mathfrak p)[T]$, a polynomial ring over a field, which is a [[Def - Principal Ideal Domain|PID]] of dimension $1$. Hence among the $\mathfrak P_i$ contracting to the same $\mathfrak p$ there are at most $2$ (a chain of length $\leq 1$ in the fibre). Krull's height theorem (Noetherian hypothesis) makes this local count add up: passing from one distinct contraction to the next consumes at least one step, and at most one extra step can occur within a single fibre, so $m \leq (\text{number of distinct } \mathfrak p_i \text{ steps}) + 1 \leq \dim A + 1$. Therefore $\dim A[T] \leq 1 + \dim A$.
>
> Combining, $\dim A[T] = 1 + \dim A$, and induction on $n$ gives $\dim A[T_1,\dots,T_n] = n + \dim A$. With $A = k$ a field ($\dim k = 0$) this re-proves $\dim k[T_1,\dots,T_n] = n$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Algebraic number theory — the dimension of $\mathbb Z[T]$.** Since $\mathbb Z$ is a Noetherian ring of dimension $1$, the recursion gives $\dim \mathbb Z[T] = 2$. The "arithmetic plane" $\operatorname{Spec}\mathbb Z[T]$ has chains like $(0) \subsetneq (p) \subsetneq (p, f)$ with $f$ irreducible mod $p$. The application is nonobvious because $\mathbb Z$ is not a field, yet the same fibre analysis governs the count; it is the gateway to arithmetic geometry, where number rings and polynomial rings are treated on equal footing.

**Invariant theory — dimension of a ring of invariants.** For a finite group $G$ acting on $k[T_1,\dots,T_n]$, the invariant subring $k[T_1,\dots,T_n]^G$ is a finitely generated domain (Noether), and $k[T_1,\dots,T_n]$ is integral over it, so by dimension-invariance $\dim k[T_1,\dots,T_n]^G = n$. The application is nonobvious because the invariant ring can be far more complicated than a polynomial ring (it may need many generators with relations), yet its dimension is forced to be $n$ — the quotient $\mathbb A^n/G$ has the same dimension as $\mathbb A^n$.

**Combinatorics — Krull dimension of a Stanley–Reisner ring.** For a simplicial complex $\Delta$, the Stanley–Reisner ring $k[\Delta] = k[T_1,\dots,T_n]/I_\Delta$ (with $I_\Delta$ generated by non-face monomials) has Krull dimension equal to $1 + \dim \Delta$ (one more than the dimension of the largest face). The application uses the companion formula and the fact that the minimal primes correspond to facets; it is the bridge by which commutative-algebra dimension theory computes combinatorial invariants of complexes.

---

# Bridges

- **[[Thm - Noether Normalization|Noether Normalization]]** — the engine of the companion formula. It writes any finitely generated domain as a finite cover of an affine space, and the number of base coordinates *is* the transcendence degree; without it, computing $\dim$ would mean directly bounding chains of primes, which is intractable. The theorem here is essentially "Noether normalization plus dimension-invariance under integral extensions, read as a dimension count".

- **[[Thm - Integral Extensions Preserve Dimension|Integral Extensions Preserve Dimension]]** — the transport mechanism. Lying-over and going-up lift a chain of primes from the base to the cover; incomparability stops two distinct primes of the cover from collapsing onto one prime of a chain. Together they force a finite cover to have the *same* dimension as its base, which is what lets $\dim A$ be read off the polynomial subring.

- **[[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's Height Theorem]]** — the tool for the hard half of the recursion. Bounding $\dim A[T] \leq 1 + \dim A$ requires controlling how primes stack above a fixed prime of $A$, and the height theorem supplies exactly the local bound (the fibre is one-dimensional). The two theorems are the two faces of dimension theory: one geometric (covers), one local (heights).

- **[[Def - Algebraic Independence and Transcendence Degree|Transcendence Degree]]** — the linear-algebra shadow of dimension. $\operatorname{trdeg}$ is a "dimension" defined purely in field theory by counting independent elements; the companion formula is the statement that this field-theoretic count and the ring-theoretic chain count *agree* for finitely generated domains. This is why dimension is computable: you never chase primes, you count independent coordinates.

---

# Unlocked by This

> [!tip] The dimension of an affine variety equals $n$ for $\mathbb A^n$ *(from Algebraic Geometry)*
> This theorem is the base case of all dimension computations in algebraic geometry: $\dim \mathbb A^n = n$, and via Noether normalization every affine variety inherits its dimension as the transcendence degree of its function field. A morphism's generic fibre dimension, the dimension of a product ($\dim(X\times Y) = \dim X + \dim Y$), and the expected dimension of an intersection are all bootstrapped from $\dim k[T_1,\dots,T_n] = n$.

> [!tip] Catenary rings and the codimension formula *(from Algebraic Geometry)*
> The exactness $\operatorname{ht}\mathfrak p + \dim A/\mathfrak p = \dim A$ for finitely generated domains is the **catenary** property: all maximal chains of primes between two fixed primes have the same length. This makes **codimension** well defined and additive, underwriting intersection theory and the dimension theory of schemes of finite type over a field.
