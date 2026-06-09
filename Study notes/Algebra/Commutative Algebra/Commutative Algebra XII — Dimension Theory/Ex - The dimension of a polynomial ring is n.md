---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Krull Dimension and Height"
  - "Thm - Dimension of a Polynomial Ring"
  - "Thm - Noether Normalization"
  - "Thm - Integral Extensions Preserve Dimension"
  - "Def - Noetherian Ring"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $k$ be a field. Prove that the polynomial ring in $n$ variables has Krull dimension exactly $n$:
$$\dim k[T_1, \dots, T_n] = n.$$

Concretely, this is two inequalities. The *lower* bound $\dim k[T_1,\dots,T_n] \geq n$ (this is ES2 Q15a) is exhibited by the explicit chain of primes
$$(0) \subsetneq (T_1) \subsetneq (T_1, T_2) \subsetneq \cdots \subsetneq (T_1, \dots, T_n),$$
of length $n$. The *upper* bound $\dim k[T_1,\dots,T_n] \leq n$ is the substantive half. The intended route (ES3 Q10 / the lecture proof) is via the inequality $\dim A \leq \operatorname{trdeg}_k A$ for a finitely generated $k$-algebra domain $A$, applied to $A = k[T_1,\dots,T_n]$, whose fraction field $k(T_1,\dots,T_n)$ has transcendence degree exactly $n$. Equivalently, one may invoke [[Thm - Integral Extensions Preserve Dimension|invariance of dimension under integral extensions]] together with [[Thm - Noether Normalization|Noether normalization]].

**Recall:**

The objects in play are the Krull dimension, transcendence degree, and the structure of the prime spectrum of a polynomial ring.

![[Def - Krull Dimension and Height#Krull dimension]]

The [[Def - Krull Dimension and Height|Krull dimension]] $\dim R$ is the supremum of the lengths $d$ of strictly increasing chains $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_d$ of prime ideals; a chain of $d+1$ primes has length $d$. Producing one chain of length $n$ proves $\dim \geq n$; ruling out all longer chains proves $\dim \leq n$.

The **transcendence degree** $\operatorname{trdeg}_k A$ of a $k$-algebra domain $A$ is $\operatorname{trdeg}_k \operatorname{Frac}(A)$, the common cardinality of a transcendence basis of the fraction field over $k$ — the maximal number of elements of $\operatorname{Frac}(A)$ that are algebraically independent over $k$. For $A = k[T_1,\dots,T_n]$ the variables $T_1,\dots,T_n$ are themselves a transcendence basis, so $\operatorname{trdeg}_k A = n$.

![[Thm - Dimension of a Polynomial Ring#Statement]]

The key bridge — *dimension is bounded by transcendence degree*:
$$\dim A \leq \operatorname{trdeg}_k A \quad \text{for every finitely generated } k\text{-algebra domain } A,$$
with equality when $A$ is a domain (Proposition 13.5). This is the algebraic incarnation of "a variety cannot have more independent chain-directions than it has independent coordinates."

---

# Convergent Strategy

**Problem class.** This is a *compute-an-invariant-exactly* problem, settled by a **two-sided squeeze**: a constructive lower bound (exhibit a long chain) meets a structural upper bound (no chain can be longer). It is the foundational dimension computation of the entire subject — every later statement, from [[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's height theorem]] to the dimension of an affine variety, is calibrated against the fact that affine $n$-space has dimension $n$. The lower bound is elementary bookkeeping; the difficulty, and the conceptual payload, is entirely in the upper bound, where one must convert a statement about *chains of primes* (combinatorially unbounded-looking) into a statement about *transcendence degree* (a fixed finite number).

**Assumption pattern.** The hypothesis "$k$ a field, finitely many variables" is used twice, in different guises. For the lower bound it guarantees that each $(T_1,\dots,T_i)$ is genuinely prime — the quotient $k[T_1,\dots,T_n]/(T_1,\dots,T_i) \cong k[T_{i+1},\dots,T_n]$ is a domain — so the chain is a chain of *primes*, not merely ideals. For the upper bound the recognisable trigger is "finitely generated $k$-algebra that is a domain": this is exactly the hypothesis under which $\dim A \leq \operatorname{trdeg}_k A$ holds, because it is what makes [[Thm - Noether Normalization|Noether normalization]] available — the engine that writes $A$ as a finite (integral) extension of a polynomial subring.

**Theorem routing.** The route splits. *Lower bound:* construct the chain $(0) \subsetneq (T_1) \subsetneq \cdots \subsetneq (T_1,\dots,T_n)$ and verify each link is a strict inclusion of primes; conclude $\dim \geq n$ directly from the definition. *Upper bound:* invoke $\dim A \leq \operatorname{trdeg}_k A$ (the lecture's Proposition 13.5, proved by induction on transcendence degree using the localization trick $A_{\{x\}}$ of ES2 Q15c) with $A = k[T_1,\dots,T_n]$; since $\operatorname{trdeg}_k k[T_1,\dots,T_n] = n$, this gives $\dim \leq n$. The two bounds meet at $n$. The alternative, more geometric routing for the upper bound runs through [[Thm - Integral Extensions Preserve Dimension|integral invariance]]: any finite integral extension $B \subseteq C$ has $\dim B = \dim C$, and Noether normalization realizes $k[T_1,\dots,T_n]$ as integral over itself, so its dimension is pinned to the trivially computed dimension of the parameter ring.

**Key decision point.** The single non-obvious move is *trading chains for transcendence degree*. Faced with proving $\dim \leq n$, the naive approach — directly bounding the length of every chain of primes in $k[T_1,\dots,T_n]$ — is hopeless, because chains can be long and irregular (e.g. they need not contract to a chain $(0) \subsetneq (T_1) \subsetneq \cdots$). The insight is that dimension, an invariant defined by chains, is controlled by a *birational* invariant, the transcendence degree of the fraction field, which is immune to the complexity of the prime lattice and is read off in one line. Recognising that "longest chain of primes $\leq$ number of algebraically independent coordinates" is the conceptual crux; the rest is the verification that the polynomial ring's coordinate count is $n$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra XII — Dimension Theory#Legal Operations|the topic page's Legal Operations]]:

1. **Exhibit a chain of primes to lower-bound dimension.** Producing a single strictly increasing chain of $d+1$ primes proves $\dim R \geq d$ immediately from the definition.

2. **Identify a quotient by a prefix of variables.** The isomorphism $k[T_1,\dots,T_n]/(T_1,\dots,T_i) \cong k[T_{i+1},\dots,T_n]$ shows each $(T_1,\dots,T_i)$ is prime (the quotient is a domain) and the inclusions are strict.

3. **Bound dimension by transcendence degree (Proposition 13.5).** For a finitely generated $k$-algebra domain $A$, $\dim A \leq \operatorname{trdeg}_k A$; this converts a chain-length question into a coordinate-count question.

4. **Read transcendence degree off a transcendence basis.** The variables $T_1, \dots, T_n$ are algebraically independent over $k$ and generate $\operatorname{Frac}$, so they form a transcendence basis and $\operatorname{trdeg}_k = n$.

5. **(Alternative route) Transport dimension across an integral extension.** A finite/integral extension preserves Krull dimension, so realizing the ring via [[Thm - Noether Normalization|Noether normalization]] as integral over a parameter subring pins the dimension to that of the subring.

---

# Hints

> [!note]- Hint 1
> Split the problem into $\dim \geq n$ and $\dim \leq n$. For the first, you only need to *write down one chain* of prime ideals of length $n$. The most natural one uses prefixes of the variables. Which ideals $(T_1, \dots, T_i)$ are prime, and why are the inclusions strict?

> [!note]- Hint 2
> For the chain $(0) \subsetneq (T_1) \subsetneq (T_1, T_2) \subsetneq \cdots \subsetneq (T_1, \dots, T_n)$, each ideal is prime because the quotient $k[T_1,\dots,T_n]/(T_1,\dots,T_i) \cong k[T_{i+1},\dots,T_n]$ is an integral domain. The inclusions are strict because $T_{i+1} \in (T_1,\dots,T_{i+1})$ but $T_{i+1} \notin (T_1,\dots,T_i)$. That is the entire lower bound: $\dim \geq n$.

> [!note]- Hint 3
> For the upper bound, do *not* try to bound arbitrary chains directly. Instead use the fact that for a finitely generated $k$-algebra that is a domain, $\dim A \leq \operatorname{trdeg}_k A$. Apply it to $A = k[T_1,\dots,T_n]$. What is the transcendence degree of $k(T_1,\dots,T_n)$ over $k$?

> [!note]- Hint 4
> The variables $T_1,\dots,T_n$ are algebraically independent over $k$ (no nonzero polynomial relation holds among them — that is what "polynomial ring" means) and $k(T_1,\dots,T_n)$ is generated by them, so they are a transcendence basis and $\operatorname{trdeg}_k = n$. Hence $\dim k[T_1,\dots,T_n] \leq n$. Combined with Hint 2, equality. (If you prefer the integral-extension route: Noether normalization writes the ring as a finite module over $k[T_1,\dots,T_n]$ — itself, here — and finite extensions preserve dimension; the parameter count $n$ is the answer.)

---

# Solution

The proof is a clean squeeze. The lower bound is a one-line construction: stack the prefixes of the variables into a chain of primes of length $n$. The upper bound is the only place with content: it says no chain can be longer than $n$, and it proves this *not* by examining chains but by bounding the dimension by the transcendence degree of the fraction field, which the variables compute to be $n$ in a single step. The two bounds clamp the dimension to exactly $n$.

**Step 1: The prefix chain gives $\dim k[T_1,\dots,T_n] \geq n$.**

The ideals $\mathfrak{p}_i = (T_1, \dots, T_i)$ for $0 \leq i \leq n$ form a strictly increasing chain of primes of length $n$, so the dimension is at least $n$.

> [!note]- Derivation
> Write $R = k[T_1,\dots,T_n]$ and for $0 \leq i \leq n$ set $\mathfrak{p}_i = (T_1,\dots,T_i)$ (so $\mathfrak{p}_0 = (0)$). Each $\mathfrak{p}_i$ is prime: the evaluation map $R \to k[T_{i+1},\dots,T_n]$ killing $T_1,\dots,T_i$ is a surjective ring homomorphism with kernel exactly $\mathfrak{p}_i$, so by the [[Thm - First Isomorphism Theorem for Rings|first isomorphism theorem]]
> $$R/\mathfrak{p}_i \;\cong\; k[T_{i+1},\dots,T_n],$$
> which is an integral domain. By [[Thm - Maximal and Prime Ideals via Quotients|the quotient criterion]], $\mathfrak{p}_i$ is prime.
>
> The inclusions $\mathfrak{p}_i \subseteq \mathfrak{p}_{i+1}$ are strict: $T_{i+1} \in \mathfrak{p}_{i+1}$, but $T_{i+1} \notin \mathfrak{p}_i = (T_1,\dots,T_i)$ — any element of $\mathfrak{p}_i$ has every monomial divisible by some $T_j$ with $j \leq i$, while $T_{i+1}$ is not. Hence
> $$(0) = \mathfrak{p}_0 \subsetneq \mathfrak{p}_1 \subsetneq \cdots \subsetneq \mathfrak{p}_n = (T_1,\dots,T_n)$$
> is a strictly increasing chain of $n+1$ primes, of length $n$. By the [[Def - Krull Dimension and Height|definition of Krull dimension]] as the supremum of chain lengths, $\dim R \geq n$. This is the content of ES2 Q15a.

**Step 2: The fraction field has transcendence degree $n$.**

The variables $T_1,\dots,T_n$ form a transcendence basis of $k(T_1,\dots,T_n)$ over $k$, so $\operatorname{trdeg}_k k[T_1,\dots,T_n] = n$.

> [!note]- Derivation
> By definition $\operatorname{trdeg}_k k[T_1,\dots,T_n] = \operatorname{trdeg}_k k(T_1,\dots,T_n)$, the transcendence degree of the fraction field. The set $\{T_1,\dots,T_n\}$ is **algebraically independent** over $k$: a polynomial relation $g(T_1,\dots,T_n) = 0$ with $g \in k[X_1,\dots,X_n]$ holds in $R$ only if $g = 0$, which is precisely the defining property of the polynomial ring (its elements *are* the polynomials, with no nontrivial relations). And $k(T_1,\dots,T_n)$ is algebraic over — indeed equal to — $k(T_1,\dots,T_n)$, so the field is algebraic over $k(\{T_i\})$ trivially. By the characterization of a transcendence basis (algebraically independent, and the field algebraic over its rational-function field), $\{T_1,\dots,T_n\}$ is a transcendence basis. Since all transcendence bases have the same cardinality, $\operatorname{trdeg}_k k(T_1,\dots,T_n) = n$.

**Step 3: $\dim A \leq \operatorname{trdeg}_k A$ gives the upper bound $\dim k[T_1,\dots,T_n] \leq n$.**

Applying the inequality $\dim A \leq \operatorname{trdeg}_k A$ (valid for any finitely generated $k$-algebra domain) to $A = k[T_1,\dots,T_n]$ and using Step 2 yields $\dim \leq n$.

> [!note]- Derivation
> The ring $A = k[T_1,\dots,T_n]$ is a finitely generated $k$-algebra (generated by the $T_i$) and an integral domain. The lecture's **Proposition 13.5 / ES3 Q10** gives, for every such $A$,
> $$\dim A \leq \operatorname{trdeg}_k A.$$
> The proof of this inequality is an induction on $\operatorname{trdeg}_k A$ using the localization $A_{\{x\}}$ of ES2 Q15(b)(c): the relation $\dim R \leq m \iff \dim R_{\{x\}} \leq m-1$ for all $x$ reduces the dimension bound by one each time one quotients out a transcendental direction, and the base case is a field ($\operatorname{trdeg} = 0$, $\dim = 0$). Granting it, substitute Step 2:
> $$\dim k[T_1,\dots,T_n] \leq \operatorname{trdeg}_k k[T_1,\dots,T_n] = n.$$
>
> *(Alternative, integral-extension route.)* [[Thm - Noether Normalization|Noether normalization]] produces a finite (hence integral) injection $k[Y_1,\dots,Y_d] \hookrightarrow A$ with $d = \operatorname{trdeg}_k A$. By [[Thm - Integral Extensions Preserve Dimension|invariance of dimension under integral extensions]], $\dim A = \dim k[Y_1,\dots,Y_d]$. For $A = k[T_1,\dots,T_n]$ the normalization is the identity ($d = n$), and one still needs $\dim k[Y_1,\dots,Y_n] = n$ — so this route is genuinely circular *unless* one already has the polynomial-ring dimension; it is the right route for a *general* finitely generated domain $A$, reducing $\dim A$ to the polynomial case. The transcendence-degree route above is the self-contained one.

**Step 4: Combine the bounds.**

The lower bound from Step 1 and the upper bound from Step 3 force equality.

> [!note]- Derivation
> From Step 1, $\dim k[T_1,\dots,T_n] \geq n$. From Step 3, $\dim k[T_1,\dots,T_n] \leq n$. Therefore
> $$\dim k[T_1,\dots,T_n] = n. \qquad \blacksquare$$
> Geometrically: affine $n$-space $\mathbb{A}^n_k$ has dimension $n$, as it must. The prefix chain $(0) \subsetneq (T_1) \subsetneq \cdots \subsetneq (T_1,\dots,T_n)$ is dual to the tower of linear subspaces $\mathbb{A}^n \supsetneq \{T_1=0\} \supsetneq \cdots \supsetneq \{T_1=\cdots=T_n=0\}$, space $\supsetneq$ hyperplane $\supsetneq \cdots \supsetneq$ point, of length $n$.

> [!note]- Complete formal solution
> **Claim.** For a field $k$, $\dim k[T_1,\dots,T_n] = n$.
>
> Write $R = k[T_1,\dots,T_n]$.
>
> *Lower bound.* For $0 \leq i \leq n$ let $\mathfrak{p}_i = (T_1,\dots,T_i)$. The quotient $R/\mathfrak{p}_i \cong k[T_{i+1},\dots,T_n]$ is a domain, so $\mathfrak{p}_i$ is prime; and $T_{i+1} \in \mathfrak{p}_{i+1} \setminus \mathfrak{p}_i$, so the inclusions are strict. Thus $(0) = \mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_n$ is a chain of primes of length $n$, whence $\dim R \geq n$.
>
> *Upper bound.* $R$ is a finitely generated $k$-algebra and a domain, so $\dim R \leq \operatorname{trdeg}_k R$ (Proposition 13.5, proved by induction on transcendence degree via the localization $A_{\{x\}}$). The variables $T_1,\dots,T_n$ are algebraically independent over $k$ and generate $\operatorname{Frac}(R) = k(T_1,\dots,T_n)$, so they form a transcendence basis and $\operatorname{trdeg}_k R = n$. Hence $\dim R \leq n$.
>
> Combining, $\dim R = n$. $\blacksquare$

---

# Key Takeaways

**Dimension is computed by a squeeze: a constructive lower bound meets a structural upper bound.** This is the prototype for *every* exact dimension computation in commutative algebra and algebraic geometry. The lower bound is cheap — you only need to *exhibit* one long chain of primes, and the prefix chain $(0) \subsetneq (T_1) \subsetneq \cdots$ is the obvious witness. The upper bound is where all the work is, because it is a statement about *all* chains at once. The deep move is that you never enumerate chains: you find a *different* invariant — here transcendence degree — that you can compute in one line and that provably dominates the chain length. The general lesson for spaced practice: when asked for an exact dimension, immediately split into $\geq$ (build a chain) and $\leq$ (find a dominating computable invariant), and expect the second to carry the mathematics. The same pattern recurs for $\dim A[T] = 1 + \dim A$ (lower bound: lift a chain and append $(\mathfrak{p}, T)$; upper bound: Krull's height theorem) and for the dimension of any affine variety.

**Transcendence degree is the bridge from algebra to geometry: it is the number of independent coordinates, and dimension cannot exceed it.** The inequality $\dim A \leq \operatorname{trdeg}_k A$ is the algebraic form of the geometric truism that a variety cannot have more independent directions to shrink in than it has independent functions on it. Transcendence degree is a *birational* invariant — it depends only on the fraction field — so it is blind to the complicated lattice of prime ideals and is read off instantly from a transcendence basis. That a chain-defined invariant (dimension) is controlled by a birational one (transcendence degree) is a genuine theorem, not a triviality: it is what makes "dimension of a variety" both well-defined and computable, and for finitely generated domains over a field the inequality is in fact an *equality* (Proposition 13.5), so dimension and transcendence degree are the same number wearing two hats. This is the entry point to the **dimension theory of varieties**: $\dim \mathbb{A}^n = n$, a curve has dimension $1$, a surface $2$, because each has that many independent coordinate functions.

**Noether normalization is the structural engine, and integral invariance of dimension is how it pays off.** Behind the transcendence-degree inequality sits a more geometric mechanism: **bold plain text — every affine variety is a branched cover of affine space.** [[Thm - Noether Normalization|Noether normalization]] writes any finitely generated $k$-algebra as a finite (integral) module over a polynomial subring $k[Y_1,\dots,Y_d]$, and [[Thm - Integral Extensions Preserve Dimension|integral extensions preserve Krull dimension]] (lying-over, going-up, incomparability force chains to correspond), so $\dim A = \dim k[Y_1,\dots,Y_d] = d$. For the polynomial ring itself this route is circular — its normalization is itself — which is exactly why the *self-contained* proof must instead go through transcendence degree directly. But for a general variety, normalization-plus-integral-invariance is the right tool: it reduces the dimension of *any* variety to the dimension of affine space, which this exercise pins at $n$. So this computation is the base case that makes the whole edifice stand: once $\dim \mathbb{A}^n = n$ is known, the dimension of every finitely generated $k$-algebra is computed by counting the variables in its Noether normalization.

**The lower-bound chain is the algebraic shadow of the flag of coordinate subspaces, and reading it geometrically is half the understanding.** The chain $(0) \subsetneq (T_1) \subsetneq (T_1,T_2) \subsetneq \cdots \subsetneq (T_1,\dots,T_n)$ is not an arbitrary construction; under the dictionary $\mathfrak{p} \mapsto V(\mathfrak{p})$ (inclusion-reversing) it is precisely the descending flag of linear coordinate subspaces $\mathbb{A}^n \supsetneq \{T_1 = 0\} \supsetneq \{T_1 = T_2 = 0\} \supsetneq \cdots \supsetneq \{0\}$ — space, hyperplane, codimension-two plane, ..., point. Each strict inclusion of primes adds one defining equation and drops the geometric dimension by exactly one, which is the **bold plain text — Krull's principal ideal theorem** in its tamest, linear instance. Internalizing that "a maximal chain of primes is a complete flag of subvarieties, each cut from the last by one equation" is what makes height $=$ codimension and dimension $=$ length-of-longest-flag intuitive rather than formal. When you reconstruct this proof later, the chain should come to mind not as a list of ideals but as the standard coordinate flag, and its length $n$ as the obvious number of steps from the whole space down to the origin.
