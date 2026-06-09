---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Graded Ring and Graded Module"
  - "Def - Polynomial Ring"
  - "Def - The Hilbert Function and Hilbert Polynomial"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $A = k[T_1, T_2]$ over a field $k$, and define a *nonstandard* degree by
$$\deg'(T_1^{e_1} T_2^{e_2}) = e_1 + 2e_2.$$
For $n \geq 0$ let $A_n$ be the $k$-span of all monomials $m$ with $\deg'(m) = n$.

**(a)** Prove that $A = \bigoplus_{n \geq 0} A_n$ is a [[Def - Graded Ring and Graded Module|graded ring]].

**(b)** Prove that there is *no* polynomial $f$ with $f(n) = \dim_k A_n$ for all large $n$ — so this grading has no [[Def - The Hilbert Function and Hilbert Polynomial|Hilbert polynomial]] in the usual sense. (Compare to the standard grading, where one exists, and identify exactly which hypothesis of the Hilbert–Serre theorem fails.)

**(c)** Write the Poincaré series $P(t) = \sum_{n \geq 0} (\dim_k A_n)\, t^n$ as a rational function.

**Recall:**

![[Def - Graded Ring and Graded Module#The Definition]]

A grading on $A = k[T_1, T_2]$ assigns each monomial a degree; here the **weight** of $T_1^{e_1}T_2^{e_2}$ is $e_1 + 2e_2$ ($T_1$ has weight $1$, $T_2$ has weight $2$). The degree-$n$ piece $A_n$ is spanned by the monomials of weight $n$. The [[Def - The Hilbert Function and Hilbert Polynomial|Hilbert function]] is $H(n) = \dim_k A_n$, and the **Poincaré series** (Hilbert series) is its generating function $P(t) = \sum_n H(n) t^n$. For the *standard* grading, the Hilbert–Serre theorem guarantees $P(t) = \frac{Q(t)}{(1-t)^d}$ with $Q \in \mathbb{Z}[t]$, and hence $H(n)$ agrees with a polynomial for large $n$. The point of this exercise is that a nonstandard grading breaks "polynomial for large $n$" while keeping the Poincaré series rational.

---

# Convergent Strategy

**Problem class.** This is a *count-a-graded-piece-and-package-it-as-a-generating-function* problem, with a twist: it is also a *diagnose-why-the-standard-theorem-fails* problem. As the [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma#Problem-Solving Strategy|topic-page strategy]] records, Hilbert-function questions are attacked by (i) counting the dimension of each graded piece combinatorially, and (ii) recognising the count as the coefficient of a rational generating function whose denominator encodes the *weights* of the generators.

**Assumption pattern.** The decisive feature is that the grading is by *unequal weights* ($1$ and $2$). The recognisable trigger is that $\dim_k A_n$ counts *weighted* partitions: the number of $(e_1, e_2)$ with $e_1 + 2e_2 = n$. Unequal weights make this count *not* eventually a single polynomial — it depends on the parity of $n$ — which is exactly the obstruction. The standard grading (weights all $1$) avoids this because the count $\binom{n+1}{1} = n+1$ is genuinely polynomial.

**Theorem routing.** The route is: (a) check the two grading axioms (weights add under multiplication, decomposition is direct); (b) count $\dim_k A_n = \#\{(e_1, e_2) : e_1 + 2e_2 = n,\ e_i \geq 0\} = \lfloor n/2 \rfloor + 1$, observe this is *not* a polynomial in $n$ (it is a *quasi*-polynomial, differing by parity), and pin the failure on the Hilbert–Serre hypothesis "generated in degree one"; (c) recognise $P(t)$ as the product of geometric series $\frac{1}{1 - t^{w_i}}$ over the generators, with $w_i$ the weights — giving $P(t) = \frac{1}{(1-t)(1-t^2)}$.

**Key decision point.** Two non-obvious moves. First, in (b), the realisation that "$\dim_k A_n$ is eventually polynomial" *fails* not because the count is wild but because it is **quasi-polynomial** — a polynomial whose coefficients depend on $n \bmod 2$ — and the precise diagnosis is that Hilbert–Serre needs the algebra to be generated *in degree one*, which fails here since $T_2$ has degree $2$. Second, in (c), the recognition that the Poincaré series *factors over the generators*: each variable $T_i$ of weight $w_i$ contributes a factor $\frac{1}{1 - t^{w_i}}$ (the generating function for "how many times $T_i$ appears, weighted"), because a monomial basis makes $A$ a free product of the one-variable pieces. This is the structural reason the series is rational even when the Hilbert function is not polynomial.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma#Legal Operations|the topic page's Legal Operations]]:

1. **Verify a grading by checking weights add (operation 2).** For (a), confirm $\deg'(mm') = \deg'(m) + \deg'(m')$ on monomials and that the monomial basis splits $A$ as a direct sum of weight-pieces.

2. **Count a graded piece combinatorially (operation 7).** For (b), $\dim_k A_n$ is the number of lattice points $(e_1, e_2)$ on the line $e_1 + 2e_2 = n$ in the first quadrant.

3. **Diagnose Hilbert–Serre failure by the degree-one hypothesis (operation 6).** Identify that the absence of a Hilbert polynomial is the failure of "generated in degree one".

4. **Factor the Poincaré series over weighted generators (operation 8).** For (c), $P(t) = \prod_i \frac{1}{1 - t^{w_i}}$ with weights $w_1 = 1$, $w_2 = 2$.

---

# Hints

> [!note]- Hint 1
> For (a): a grading needs the decomposition $A = \bigoplus A_n$ to be direct and the multiplication to satisfy $A_m A_n \subseteq A_{m+n}$. The monomials form a $k$-basis of $A$, and each monomial has a *single* weight. What does that give you for directness? And what is $\deg'(mm')$ in terms of $\deg'(m)$, $\deg'(m')$?

> [!note]- Hint 2
> For (b): count the monomials of weight $n$. A monomial $T_1^{e_1}T_2^{e_2}$ has weight $n$ iff $e_1 + 2e_2 = n$ with $e_1, e_2 \geq 0$. For each allowed value of $e_2$, $e_1$ is determined. How many values of $e_2$ are allowed?

> [!note]- Hint 3
> For (b): the values of $e_2$ run over $0, 1, \dots, \lfloor n/2 \rfloor$, so $\dim_k A_n = \lfloor n/2\rfloor + 1$. Is $\lfloor n/2 \rfloor + 1$ a polynomial in $n$? Compute it for $n = 0, 1, 2, 3, 4, 5$: you get $1, 1, 2, 2, 3, 3$. A polynomial would not repeat values like that. Which hypothesis of Hilbert–Serre — generation in degree one — is violated, and why does the standard grading (weight $1, 1$) escape?

> [!note]- Hint 4
> For (c): in a polynomial ring with weighted variables, the Poincaré series factors as a product over the variables. The variable $T_i$ of weight $w_i$, appearing to powers $0, 1, 2, \dots$, contributes $1 + t^{w_i} + t^{2w_i} + \dots = \frac{1}{1 - t^{w_i}}$. Multiply the factors for $T_1$ (weight $1$) and $T_2$ (weight $2$).

---

# Solution

The solution is a weighted-lattice-point count packaged as a rational generating function. Part (a) checks the grading axioms via the monomial basis. Part (b) counts $\dim_k A_n = \lfloor n/2\rfloor + 1$, observes it is *quasi*-polynomial (parity-dependent) hence not polynomial, and traces the failure to the degree-one hypothesis of Hilbert–Serre. Part (c) factors the Poincaré series over the weighted generators to get $\frac{1}{(1-t)(1-t^2)}$.

**Step 1 (part a): $A = \bigoplus_n A_n$ is a graded ring.**

The monomials form a $k$-basis sorted by weight, giving the direct-sum decomposition, and weights add under multiplication, giving $A_m A_n \subseteq A_{m+n}$.

> [!note]- Derivation
> The monomials $\{T_1^{e_1}T_2^{e_2} : e_1, e_2 \geq 0\}$ form a $k$-basis of $A = k[T_1, T_2]$. Each monomial has a unique weight $\deg'(T_1^{e_1}T_2^{e_2}) = e_1 + 2e_2$, so partitioning the basis by weight gives $A = \bigoplus_{n \geq 0} A_n$ with $A_n = \operatorname{span}_k\{$monomials of weight $n\}$ — the decomposition is *direct* because each basis monomial lands in exactly one $A_n$.
>
> For the multiplicative axiom, take monomials $m = T_1^{a_1}T_2^{a_2}$ of weight $\deg'(m) = a_1 + 2a_2 = p$ and $m' = T_1^{b_1}T_2^{b_2}$ of weight $\deg'(m') = b_1 + 2b_2 = q$. Their product $mm' = T_1^{a_1+b_1}T_2^{a_2+b_2}$ has weight $(a_1+b_1) + 2(a_2+b_2) = (a_1 + 2a_2) + (b_1 + 2b_2) = p + q$. So $\deg'$ is additive on monomials, and by bilinearity $A_p A_q \subseteq A_{p+q}$. Both axioms hold, so $A = \bigoplus_n A_n$ is a graded ring. (Here $A_0 = k$, since the only weight-$0$ monomial is $1$.)

**Step 2 (part b): $\dim_k A_n = \lfloor n/2\rfloor + 1$, which is not eventually polynomial.**

Counting monomials of weight $n$ gives $\dim_k A_n = \lfloor n/2 \rfloor + 1$; this quasi-polynomial takes each value twice ($1,1,2,2,3,3,\dots$) and so cannot agree with any polynomial for large $n$.

> [!note]- Derivation
> A monomial $T_1^{e_1}T_2^{e_2}$ has weight $n$ iff $e_1 + 2e_2 = n$ with $e_1, e_2 \geq 0$. For each choice of $e_2$, the value $e_1 = n - 2e_2$ is forced and must be $\geq 0$, i.e. $e_2 \leq n/2$. So $e_2$ ranges over $0, 1, \dots, \lfloor n/2 \rfloor$, giving
> $$\dim_k A_n = \left\lfloor \frac{n}{2}\right\rfloor + 1.$$
> Explicitly: $\dim_k A_n = \tfrac{n}{2} + 1$ if $n$ is even, $\tfrac{n-1}{2} + 1 = \tfrac{n+1}{2}$ if $n$ is odd. This is a **quasi-polynomial**: a polynomial whose constant term depends on $n \bmod 2$. The values for $n = 0, 1, 2, 3, 4, 5, \dots$ are $1, 1, 2, 2, 3, 3, \dots$.
>
> No polynomial $f$ can satisfy $f(n) = \dim_k A_n$ for all large $n$. If it did, then for large even $n$, $f(n) = \tfrac n2 + 1$, and for large odd $n$, $f(n) = \tfrac{n+1}{2}$; subtracting, $f(n+1) - f(n)$ alternates between $0$ (even $\to$ odd: $\tfrac{n+1}{2} - (\tfrac n2 + 1) = -\tfrac12$, wait recompute) — directly: the consecutive differences $\dim_k A_{n+1} - \dim_k A_n$ are $0, 1, 0, 1, \dots$ (the sequence $1,1,2,2,3,3$ jumps by $0$ then $1$ alternately). A polynomial $f$ has $f(n+1) - f(n)$ itself a polynomial, hence eventually monotone or constant in sign-pattern, never eventually $0,1,0,1,\dots$. So no such $f$ exists.
>
> *Which hypothesis fails.* The Hilbert–Serre theorem guarantees $\dim_k A_n$ is eventually polynomial *when $A$ is generated in degree one over $A_0 = k$*. Here $A$ is generated by $T_1$ (degree $1$) and $T_2$ (degree $\mathbf{2}$) — it is **not generated in degree one**. The degree-$2$ generator is exactly what makes the count parity-dependent: monomials advance in weight by $1$ via $T_1$ but by $2$ via $T_2$, so the "supply" of new monomials at weight $n$ oscillates with parity. Under the standard grading (both weights $1$), the count is $\dim_k A_n = n + 1$, a genuine polynomial, and Hilbert–Serre applies with no obstruction.

**Step 3 (part c): The Poincaré series factors as $P(t) = \dfrac{1}{(1-t)(1-t^2)}$.**

Each weighted variable contributes a geometric-series factor, giving the rational function $P(t) = \frac{1}{1-t}\cdot\frac{1}{1-t^2}$.

> [!note]- Derivation
> The Poincaré series is $P(t) = \sum_{n \geq 0}(\dim_k A_n)\, t^n$. Because the monomials form a weight-graded $k$-basis, $A$ is, as a graded vector space, the "free" combination of the powers of $T_1$ and the powers of $T_2$: every monomial is $T_1^{e_1}T_2^{e_2}$ for a unique $(e_1, e_2)$, contributing $t^{e_1 \cdot 1 + e_2 \cdot 2}$. Hence
> $$P(t) = \sum_{e_1 \geq 0}\sum_{e_2 \geq 0} t^{e_1 + 2e_2} = \left(\sum_{e_1 \geq 0} t^{e_1}\right)\left(\sum_{e_2 \geq 0} t^{2e_2}\right) = \frac{1}{1 - t}\cdot\frac{1}{1 - t^2}.$$
> So
> $$\boxed{\,P(t) = \frac{1}{(1-t)(1-t^2)}\,}.$$
> *Consistency check with (b).* Expanding, $\frac{1}{(1-t)(1-t^2)} = \frac{1}{(1-t)^2(1+t)}$. The factor $(1-t)^2$ in the denominator gives an order-$1$ pole at $t = 1$ of multiplicity $2$, which would normally signal "polynomial of degree $1$"; but the *extra* factor $(1 + t)$, contributing a pole at $t = -1$, is exactly the algebraic source of the parity-dependence — a pole at a root of unity other than $1$ is the generating-function signature of a quasi-polynomial. The standard grading would give $\frac{1}{(1-t)^2}$, denominator a pure power of $(1-t)$, hence a genuine Hilbert polynomial. The presence of $(1 - t^2)$ rather than $(1-t)^2$ in the denominator *is* the failure of degree-one generation, visible in the series.

> [!note]- Complete formal solution
> **(a)** The monomials $T_1^{e_1}T_2^{e_2}$ form a $k$-basis, each of a single weight $e_1 + 2e_2$, so $A = \bigoplus_n A_n$ is direct with $A_n = \operatorname{span}_k\{$weight-$n$ monomials$\}$. Weights add: $\deg'(mm') = \deg'(m) + \deg'(m')$, so $A_p A_q \subseteq A_{p+q}$. Hence $A$ is a graded ring with $A_0 = k$.
>
> **(b)** Monomials of weight $n$ are $T_1^{n - 2e_2}T_2^{e_2}$ for $0 \leq e_2 \leq \lfloor n/2\rfloor$, so $\dim_k A_n = \lfloor n/2\rfloor + 1$, with values $1,1,2,2,3,3,\dots$. The consecutive differences are $0,1,0,1,\dots$, which no polynomial's differences can match (a polynomial's first difference is itself a polynomial, never eventually $0,1,0,1,\dots$). So no polynomial $f$ has $f(n) = \dim_k A_n$ for large $n$. The reason: Hilbert–Serre requires generation in degree one, but $A$ is generated by $T_1$ (degree $1$) and $T_2$ (degree $2$); the degree-$2$ generator makes the count quasi-polynomial. The standard grading gives $\dim_k A_n = n+1$, polynomial.
>
> **(c)** $P(t) = \sum_{e_1, e_2 \geq 0} t^{e_1 + 2e_2} = \frac{1}{1-t}\cdot\frac{1}{1-t^2} = \dfrac{1}{(1-t)(1-t^2)}$. The factor $(1 - t^2)$ (a non-$(1-t)$ denominator) is the analytic signature of the failure of degree-one generation. $\blacksquare$

---

# Key Takeaways

**Unequal weights produce quasi-polynomial Hilbert functions; the Poincaré series stays rational but its denominator is not a pure power of $(1-t)$.** The central lesson is the precise dichotomy. For a graded ring generated in degree one, Hilbert–Serre gives $P(t) = Q(t)/(1-t)^d$ and $\dim_k A_n$ is eventually a *polynomial* of degree $d - 1$. The moment a generator carries weight $> 1$, the denominator acquires factors $(1 - t^{w})$ with $w > 1$, which factor as $(1-t)\cdot(1 + t + \dots + t^{w-1})$ and contribute poles at *roots of unity other than $1$*; those poles are exactly what turn the Hilbert function into a quasi-polynomial — a polynomial whose coefficients cycle with period equal to the least common multiple of the weights. The trigger to expect this: any time you grade by unequal weights (weighted projective space, a Veronese with skipped degrees, an invariant ring with generators of mixed degree), do *not* expect a Hilbert polynomial; expect a Hilbert quasi-polynomial, and read its period off the weights.

**The Poincaré series of a (weighted) polynomial ring factors over its generators, one geometric-series factor per variable.** This is the most reusable computational fact: $P(t) = \prod_i \frac{1}{1 - t^{w_i}}$ where $w_i = \deg(T_i)$, because a monomial basis makes the graded vector space a tensor product of the one-variable strands, and generating functions multiply over tensor products. The diagnostic value is that you can *read the generators and their degrees off the denominator* of a Hilbert series: a denominator $(1-t)^a(1-t^2)^b(1-t^3)^c$ signals $a$ generators of degree $1$, $b$ of degree $2$, $c$ of degree $3$ (in the polynomial case). This is how one guesses presentations from Hilbert series, and why the Hilbert series is the first invariant computed for any graded ring. When there are relations, the numerator $Q(t)$ records them — each relation of degree $e$ contributes a factor $(1 - t^e)$ upstairs.

**The "failure" of a theorem is most instructive when you locate the exact hypothesis that breaks.** This exercise is a model of diagnostic reasoning: the Hilbert polynomial fails to exist, and the disciplined move is not to shrug but to ask *which hypothesis of Hilbert–Serre is violated* — and the answer, "generated in degree one", is precisely the structural defect. The transferable habit: when a standard theorem does not apply, run down its hypotheses one at a time against your example, and the one that fails will both *explain* the anomaly and *tell you what the corrected theorem looks like* (here, the quasi-polynomial version of Hilbert–Serre for non-degree-one gradings). The same discipline recovers, in the smooth-vs-singular contrast of [[Ex - The associated graded ring of a polynomial ring]], that singularity is the failure of "$\operatorname{gr}_{\mathfrak{m}}(R)$ is a polynomial ring"; and it connects forward to [[Def - The Hilbert Function and Hilbert Polynomial|dimension theory]], where the order of the pole at $t = 1$ — not the spurious poles at other roots of unity — is what computes the Krull dimension.
