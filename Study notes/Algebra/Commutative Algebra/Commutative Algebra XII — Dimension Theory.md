---
type: topic
subject: commutative-algebra
chapter: "13"
title: "Commutative Algebra XII — Dimension Theory"
tags: [algebra, commutative-algebra]
---

# Notation Registry

**Standing convention.** Throughout these commutative algebra notes, *ring* means a commutative ring with $1$. The central achievement of this chapter is the **Dimension Theorem**, which proves that three a-priori-different numbers attached to a [[Def - Noetherian Ring|Noetherian]] local ring all coincide; the slogan, restated in Motivation, is **dimension counts the same thing whether you count chains of primes, the growth rate of the ring, or the number of equations needed to cut down to a point.**

- $R, A$ — commutative rings with $1$; $(A,\mathfrak m)$ — a Noetherian local ring with maximal ideal $\mathfrak m$ and residue field $k = A/\mathfrak m$
- $\dim R$ — the [[Def - Krull Dimension and Height|Krull dimension]]; $\operatorname{ht}\mathfrak p$ — the **height** of a prime $\mathfrak p$
- $\mathfrak p, \mathfrak q$ — prime ideals; $\mathfrak m, \mathfrak n$ — maximal ideals; $\operatorname{Spec} R$, $\operatorname{mSpec} R$ — the prime and maximal spectra
- $\ell(M)$ — the [[Def - Composition Series and Length|length]] of a module $M$ of finite length
- $A = \bigoplus_{n\geq 0} A_n$ — a graded ring; $H(M, n) = \dim_k M_n$ or $\ell(M_n)$ — the **Hilbert function** of a graded module $M$
- $P_M(T) = \sum_n H(M,n) T^n$ — the **Poincaré (Hilbert) series**; $P_M(n)$ — the **Hilbert polynomial** (agrees with $H(M,n)$ for large $n$)
- $\chi_{\mathfrak q}^M(n) = \ell(M/\mathfrak q^{n+1} M)$ — the **Hilbert–Samuel function** of an $\mathfrak m$-primary ideal $\mathfrak q$ acting on a finite module $M$
- $d(A)$ — the degree of the Hilbert–Samuel polynomial of $(A,\mathfrak m)$
- $\delta(A)$ — the least number of elements generating an $\mathfrak m$-primary ideal (the size of a **system of parameters**)
- $\operatorname{gr}_{\mathfrak q}(A) = \bigoplus_n \mathfrak q^n/\mathfrak q^{n+1}$ — the [[Def - The Associated Graded Ring and the Rees Algebra|associated graded ring]]
- $\operatorname{trdeg}_k A$ — the [[Def - Algebraic Independence and Transcendence Degree|transcendence degree]] of $\operatorname{Frac}(A)$ over $k$, for $A$ a domain

---

# Motivation

Here is the entire chapter in one sentence: **the dimension of a ring can be measured in three completely different ways — by counting chains of prime ideals, by measuring how fast the ring grows, and by counting how many equations it takes to cut the ring down to a fat point — and the Dimension Theorem is the astonishing fact that all three give the same number.** Each measurement is natural on its own terms, each is useful for different problems, and none is obviously equal to the others. That they coincide is what makes "dimension" a robust, computable invariant rather than three unrelated definitions wearing the same name.

The first measurement is the geometric one, the [[Def - Krull Dimension and Height|Krull dimension]] $\dim A$: the length of the longest chain of prime ideals $\mathfrak p_0 \subsetneq \cdots \subsetneq \mathfrak p_d$. This is the *right* definition — it manifestly gives $n$ for $\mathbb A^n$ and the geometric dimension for any variety — but it is almost useless for computation, because chains of primes are hard to enumerate and harder to bound from above. The second measurement is the *analytic* one. Attach to a Noetherian local ring $(A,\mathfrak m)$ the sequence of lengths $\ell(A/\mathfrak m^{n+1})$, counting how much of the ring is visible "to order $n$" near the point; for large $n$ this length is a polynomial in $n$ — the **Hilbert–Samuel polynomial** — and its degree $d(A)$ measures the *growth rate* of the ring. A point grows like a constant (degree $0$), a curve like $n$ (degree $1$), a surface like $n^2$ (degree $2$): the degree of growth is the dimension. The third measurement is the most operational. Define $\delta(A)$ to be the minimum number of elements $x_1,\dots,x_r$ you need so that $(x_1,\dots,x_r)$ contains a power of $\mathfrak m$ — equivalently, so that $A/(x_1,\dots,x_r)$ is Artinian, a "fat point". This is the number of equations needed to cut $A$ down to dimension zero, a **system of parameters**.

The chapter's structural backbone is the chain of equalities the Dimension Theorem proves:

$$\dim A \;=\; d(\operatorname{gr}_{\mathfrak m} A) \;=\; \delta(A),$$

for any Noetherian local ring $(A,\mathfrak m)$. The proof is a cycle of three inequalities — $\delta(A) \geq d(A) \geq \dim A \geq \delta(A)$ — each proved by a different technique: $\delta \geq d$ by feeding a system of parameters into the Hilbert function, $d \geq \dim$ by an induction on the degree using that cutting by a non-zero-divisor drops the Hilbert polynomial's degree, and $\dim \geq \delta$ by inductively building a system of parameters that avoids the minimal primes. Each inequality is where one of the three viewpoints pays for itself, and the [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma|graded-ring machinery]] (Hilbert–Serre, the associated graded ring) is the connective tissue.

Two great consequences fall out. **Krull's height theorem**, $\operatorname{ht}(x_1,\dots,x_r) \leq r$: an ideal generated by $r$ elements cannot cut codimension more than $r$ — geometrically, one equation drops dimension by at most one. And **$\dim k[T_1,\dots,T_n] = n$** together with $\dim A = \operatorname{trdeg}_k A$ for finitely generated domains: the algebraic dimension equals the number of free coordinates, anchoring the whole theory to geometry.

This chapter is the capstone of the course and leans on most of what came before. You should be fluent with [[Def - Krull Dimension and Height|Krull dimension and height]], with [[Def - Noetherian Ring|Noetherian rings]] and [[Def - Local Ring and Residue Field|local rings]] from [[Commutative Algebra IV — Localization|Localization]], with the [[Def - Graded Ring and Graded Module|graded-ring]] and [[Thm - The Artin-Rees Lemma|Artin–Rees]] material of [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma|Chapter XI]], with [[Thm - Noether Normalization|Noether normalization]] and [[Def - Algebraic Independence and Transcendence Degree|transcendence degree]] from [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz|Chapter VII]], with [[Thm - Integral Extensions Preserve Dimension|dimension-invariance under integral extensions]] from [[Commutative Algebra VIII — Going Up and Going Down|Chapter VIII]], and with the [[Thm - Cayley-Hamilton for Modules (Determinant Trick)|determinant trick]] from [[Commutative Algebra V — Nakayama's Lemma|Nakayama]].

---

# Concept Map

## §13.1 Hilbert Functions and the Dimension Theorem

- **[[Def - The Hilbert Function and Hilbert Polynomial]]**
	- For a finitely generated graded module $M = \bigoplus_n M_n$ over a graded ring finitely generated in degree one over an Artinian $A_0$, the **Hilbert function** $H(M,n) = \ell(M_n)$ records the length of each graded piece. For large $n$ it agrees with a polynomial in $n$, the **Hilbert polynomial**, whose degree measures the growth rate of $M$ and whose leading coefficient encodes the degree of the corresponding projective variety. The case $A = k[T_0,\dots,T_n]$ gives $H(n) = \binom{n+d}{d}$ for the degree-$d$ piece, a polynomial of degree equal to the dimension.

- **[[Thm - Hilbert-Serre and Rationality of the Poincare Series|Hilbert–Serre and Rationality of the Poincaré Series]]**
	- The Poincaré series $P_M(T) = \sum_n \ell(M_n) T^n$ of a finitely generated graded module is a *rational function* of the form $f(T)/\prod_i (1 - T^{k_i})$, with $f \in \mathbb Z[T]$, where the $k_i$ are the degrees of algebra generators. The pole at $T = 1$ has order equal to the dimension, so rationality of the generating function is what *forces* the Hilbert function to be eventually polynomial. The proof is induction on the number of generators, using the [[Def - Exact Sequence and Short Exact Sequence|exact sequence]] given by multiplication by a generator.

- **[[Thm - The Hilbert Polynomial]]**
	- When the graded ring is generated in degree one (the $k_i = 1$ case), the Hilbert function $H(M,n)$ equals a numerical polynomial $P_M(n)$ for all large $n$, of degree $d - 1$ where $d$ is the order of the pole at $T=1$. This is the precise sense in which "the ring grows polynomially", and the degree of $P_M$ is the dimension of $\operatorname{Proj}$ of the ring. It is the graded prototype of the Hilbert–Samuel polynomial used in the local dimension theory.

- **[[Def - System of Parameters]]**
	- A **system of parameters** for a Noetherian local ring $(A,\mathfrak m)$ of dimension $d$ is a set of $d$ elements $x_1,\dots,x_d \in \mathfrak m$ generating an $\mathfrak m$-primary ideal — equivalently, $A/(x_1,\dots,x_d)$ is Artinian. It is the algebraic notion of **local coordinates** at a point: the minimum number of functions whose common zero locus is just the point (to within nilpotents). The number $\delta(A)$ of elements in a smallest such system is one of the three quantities the Dimension Theorem equates to $\dim A$; a regular system of parameters (when $\delta(A) = \dim_k \mathfrak m/\mathfrak m^2$) marks a smooth point.

- **[[Thm - The Dimension Theorem for Noetherian Local Rings]]**
	- For a Noetherian local ring $(A,\mathfrak m)$, the three numbers coincide: $\dim A = d(A) = \delta(A)$, where $\dim A$ is the Krull dimension (longest chain of primes), $d(A)$ is the degree of the Hilbert–Samuel polynomial $n \mapsto \ell(A/\mathfrak m^{n+1})$, and $\delta(A)$ is the least number of generators of an $\mathfrak m$-primary ideal. The proof is the cycle $\delta(A) \geq d(A) \geq \dim A \geq \delta(A)$, each step a different technique. This is the theorem that makes dimension computable and finite, and from which Krull's height theorem follows immediately.

> [!tip] Unlocked: Degree and the Hilbert polynomial of a projective variety *(from Algebraic Geometry)*
> For a projective variety $X \subseteq \mathbb P^n$ with homogeneous coordinate ring $S$, the **Hilbert polynomial** $P_X(n) = \dim_k S_n$ (for large $n$) has degree $\dim X$ and leading coefficient $(\deg X)/(\dim X)!$ — so a single polynomial simultaneously encodes the **dimension** and the **degree** of $X$, and its constant term is the **arithmetic genus**. This is the bridge by which the abstract Hilbert function becomes the central numerical invariant of projective geometry, and the foundation of Hilbert schemes (moduli of subvarieties with fixed Hilbert polynomial).

- **[[Ex - The Hilbert polynomial of projective space]]** (⭐⭐)
	- Compute the Hilbert function of $k[T_0,\dots,T_n]$ as $\binom{n+d}{d}$ and read off that its degree is $n = \dim \mathbb P^n$, with the leading coefficient giving the degree — the prototype linking Hilbert polynomials to projective dimension and degree.

- **[[Ex - Dimension equals transcendence degree for a finitely generated domain]]** (⭐⭐⭐)
	- Prove $\dim A = \operatorname{trdeg}_k \operatorname{Frac}(A)$ for a finitely generated domain over a field, via Noether normalization and dimension-invariance under integral extensions — the theorem that makes dimension computable as a count of free coordinates.

> [!note] Exercise Index — §13.1
> [[Exercise Index - §13.1 Hilbert Functions and the Dimension Theorem]]

## §13.2 Krull Dimension and Height

- **[[Def - Krull Dimension and Height]]**
	- The **Krull dimension** $\dim R$ is the supremum of lengths $d$ of chains of primes $\mathfrak p_0 \subsetneq \cdots \subsetneq \mathfrak p_d$; the **height** $\operatorname{ht}\mathfrak p$ counts chains ending at $\mathfrak p$, and equals $\dim R_{\mathfrak p}$. Geometrically a chain of primes is a tower of irreducible subvarieties, so $\dim$ is the geometric dimension and $\operatorname{ht}\mathfrak p$ is the codimension of $V(\mathfrak p)$. A field has dimension $0$, $\mathbb Z$ and every PID (not a field) have dimension $1$, and the local invariant $\operatorname{ht}\mathfrak p = \dim R_{\mathfrak p}$ reduces global dimension to local dimension.

- **[[Thm - Krull's Height Theorem (Principal Ideal Theorem)]]**
	- An ideal generated by $r$ elements in a Noetherian ring has height at most $r$: $\operatorname{ht}(x_1,\dots,x_r) \leq r$; in particular (the **principal ideal theorem**) a minimal prime over a single non-unit non-zero-divisor has height exactly one. Geometrically, **$r$ equations cut codimension at most $r$, and one equation cuts exactly one** — a hypersurface in $\mathbb A^n$ has dimension $n-1$. It is an immediate corollary of the Dimension Theorem ($\operatorname{ht}\mathfrak p = \dim A_{\mathfrak p} = \delta(A_{\mathfrak p}) \leq r$), and its converse builds a system of parameters realising any given height.

- **[[Thm - Dimension of a Polynomial Ring]]**
	- $\dim k[T_1,\dots,T_n] = n$ for a field $k$, and $\dim A[T] = 1 + \dim A$ for any Noetherian $A$ of finite dimension; for a finitely generated domain $A$ over $k$, $\dim A = \operatorname{trdeg}_k \operatorname{Frac}(A)$. The hard direction is the upper bound — that no chain of primes beats the obvious linear flag — proved via [[Thm - Noether Normalization|Noether normalization]] plus [[Thm - Integral Extensions Preserve Dimension|dimension-invariance under integral extensions]], or via the recursion using Krull's height theorem. This is what anchors dimension to geometry: $\dim \mathbb A^n = n$.

> [!tip] Unlocked: Codimension, divisors, and the principal ideal theorem *(from Algebraic Geometry)*
> Krull's height theorem is the algebraic statement that **a hypersurface has codimension one**: the zero locus of a single equation $f$ drops the dimension by exactly one (when $f$ is a non-zero-divisor non-unit). Iterated, it gives the **expected dimension** $n - r$ of a variety cut by $r$ equations, with equality for complete intersections. Height-one primes are the **prime divisors**, generating the group of Weil divisors — the start of intersection theory and the theory of line bundles, tying back to the [[Commutative Algebra XIII — Dedekind Domains and DVRs|class group]] of a Dedekind domain.

- **[[Ex - The dimension of a polynomial ring is n]]** (⭐⭐)
	- Show $\dim k[T_1,\dots,T_n] = n$ by exhibiting the linear flag of primes and bounding above by transcendence degree — the base case anchoring algebraic dimension to $\dim \mathbb A^n = n$.

- **[[Ex - Krull's principal ideal theorem and hypersurfaces]]** (⭐⭐)
	- Prove that a minimal prime over a single non-zero-divisor has height exactly one, so a hypersurface has codimension one — one equation drops dimension by exactly one.

- **[[Ex - Height plus dimension of the quotient equals dimension]]** (⭐⭐)
	- Establish the catenary identity $\operatorname{ht}\mathfrak p + \dim A/\mathfrak p = \dim A$ for a finitely generated domain, the exactness that makes codimension well defined and additive.

- **[[Ex - A Noetherian ring of infinite dimension]]** (⭐⭐⭐)
	- Construct Nagata's example: a Noetherian ring with primes of unbounded height, so $\dim R = \infty$ even though every individual height is finite — Noetherianity bounds heights pointwise but not their supremum.

> [!note] Exercise Index — §13.2
> [[Exercise Index - §13.2 Krull Dimension and Height]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

Five goals recur. The first is **computing the dimension of a specific ring** — a quotient $k[T_1,\dots,T_n]/I$, a localization, an invariant ring — almost always by routing to one of the three computable forms: transcendence degree (for finitely generated domains), the degree of a Hilbert polynomial (for graded rings), or a system of parameters (for local rings). The second is **bounding the codimension of a subvariety**, i.e. the height of a prime, where [[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's height theorem]] turns "cut out by $r$ equations" into "$\operatorname{ht} \leq r$". The third is **establishing the dimension equalities themselves** — that $\dim = d = \delta$, or that $\dim A = \operatorname{trdeg}$, or $\dim A[T] = 1 + \dim A$ — the structural theorems. The fourth is **proving exactness of the chain count** — catenary-type results like $\operatorname{ht}\mathfrak p + \dim A/\mathfrak p = \dim A$, which guarantee codimension is well behaved. The fifth is **detecting regularity / singularity** — comparing $\dim A$ with $\dim_k \mathfrak m/\mathfrak m^2$ (the [[Commutative Algebra V — Nakayama's Lemma|embedding dimension]]) to decide whether a point is smooth. These are the natural targets because dimension is the first and coarsest invariant of a ring or variety, and almost every finer question (smoothness, intersection multiplicity, degree) is phrased relative to it.

**Sources — what assumptions do we usually leverage?**

The hypotheses are stereotyped. **"$A$ is a finitely generated algebra over a field"** switches on Noether normalization and the transcendence-degree formula, the fastest route to a dimension. **"$A$ is Noetherian local $(A,\mathfrak m)$"** switches on the full Dimension Theorem, systems of parameters, and the Hilbert–Samuel polynomial — and is the form *everything* reduces to by localizing at a prime ($\operatorname{ht}\mathfrak p = \dim A_{\mathfrak p}$). **"$A$ is graded, finitely generated in degree one over an Artinian $A_0$"** switches on Hilbert–Serre and the Hilbert polynomial. **"An ideal is given by $r$ generators"** routes to Krull's height theorem for an upper bound on codimension. **"$A$ is an integral domain"** makes $(0)$ prime and lets transcendence degree and going-down be used. The discipline is to localize-and-reduce: a global dimension question becomes a local one at a maximal ideal, a local one is attacked by a system of parameters or a Hilbert polynomial, and a finitely-generated-domain question is closed by transcendence degree. The [[Commutative Algebra XII — Dimension Theory#Problem-Solving Strategy|Problem-Solving Strategy]] makes these routes explicit.

---

# Legal Operations

These are the moves nearly every dimension problem is assembled from. When stuck, scan the list.

1. **Reduce dimension to the local case.** Since $\operatorname{ht}\mathfrak p = \dim A_{\mathfrak p}$ and $\dim A = \sup_{\mathfrak m} \dim A_{\mathfrak m}$, replace a global dimension/height question by a question about a Noetherian *local* ring, where the Dimension Theorem and systems of parameters are available. *Trigger:* any height computation, or a dimension that is "local at a point". *Pattern:* "localize at $\mathfrak p$; now $\operatorname{ht}\mathfrak p = \dim A_{\mathfrak p}$ and I may use a system of parameters."

2. **Compute dimension as transcendence degree.** For a finitely generated domain $A$ over a field $k$, $\dim A = \operatorname{trdeg}_k \operatorname{Frac}(A)$ — count algebraically independent elements instead of chasing primes. *Trigger:* $A$ is an explicit quotient of a polynomial ring and a domain. *Pattern:* "find a transcendence basis of the fraction field; its size is the dimension."

3. **Cut by a system of parameters.** To bring a $d$-dimensional local ring down to dimension zero, choose $x_1,\dots,x_d$ generating an $\mathfrak m$-primary ideal; each $x_i$ drops the dimension by exactly one if it avoids the minimal primes. *Trigger:* an induction on dimension, or "make the ring Artinian". *Pattern:* "pick $x_1$ outside every minimal prime; $\dim A/(x_1) = \dim A - 1$."

4. **Read dimension off a Hilbert polynomial.** For a graded ring, the dimension is the degree of the Hilbert polynomial $+1$ (the order of the pole of the Poincaré series at $T=1$); for a local ring, it is the degree of the Hilbert–Samuel polynomial $\ell(A/\mathfrak m^{n+1})$. *Trigger:* a graded ring, or a local ring where you can compute lengths $\ell(A/\mathfrak m^n)$. *Pattern:* "compute the Poincaré series, find the pole order at $T=1$."

5. **Bound codimension by the number of generators.** By [[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's height theorem]], an ideal with $r$ generators has height $\leq r$; a single non-zero-divisor non-unit gives height exactly $1$. *Trigger:* "show this subvariety has codimension $\leq r$", or "a hypersurface drops dimension by one". *Pattern:* "$\mathfrak p$ is minimal over $(x_1,\dots,x_r)$, so $\operatorname{ht}\mathfrak p \leq r$."

6. **Pass dimension through an integral extension.** An integral extension $A \subseteq B$ has $\dim A = \dim B$, via lying-over, going-up, and incomparability. *Trigger:* $B$ is module-finite over $A$ (e.g. Noether normalization, or an integral closure). *Pattern:* "$B$ is integral over the polynomial ring $A$, so $\dim B = \dim A =$ number of variables."

7. **Add one for a polynomial variable.** $\dim A[T] = 1 + \dim A$ for Noetherian $A$; inductively $\dim A[T_1,\dots,T_n] = n + \dim A$. *Trigger:* a polynomial extension of a ring of known dimension. *Pattern:* "adjoining one variable adds exactly one to the dimension."

8. **Compare with the embedding dimension to test smoothness.** Always $\dim A \leq \dim_k \mathfrak m/\mathfrak m^2$ for a Noetherian local ring; equality defines a **regular** (smooth) point. *Trigger:* a smoothness/singularity question. *Pattern:* "compute $\dim_k \mathfrak m/\mathfrak m^2$ ([[Commutative Algebra V — Nakayama's Lemma|minimal generators of \mathfrak m]]) and compare with $\dim A$."

9. **Use catenary exactness.** For a finitely generated domain over a field, $\operatorname{ht}\mathfrak p + \dim A/\mathfrak p = \dim A$. *Trigger:* you know two of {height, quotient dimension, total dimension} and want the third. *Pattern:* "$\dim A/\mathfrak p = \dim A - \operatorname{ht}\mathfrak p$."

**Illegal but tempting operations:**

> [!warning] 1. Reading height off the number of generators of a prime
> Krull's height theorem gives $\operatorname{ht}\mathfrak p \leq \mu(\mathfrak p)$, so it is tempting to read height off the number of generators. The inequality can be *strict*: the prime $\mathfrak p$ of the twisted cubic in $k[X,Y,Z]$ has height $2$ (it is a curve in $3$-space, codimension $2$) but needs $3$ generators $(XZ - Y^2,\, YZ - X^2 Z,\dots)$ — it is not a [[Def - Principal Ideal Domain|complete intersection]]. Height is a *lower* invariant than generator count; equality (a complete intersection) is special. The repair: height equals the *minimum* over chains, and only for a system of parameters cutting an $\mathfrak m$-primary ideal does the count match the dimension.

> [!warning] 2. Assuming $\dim A[T] = 1 + \dim A$ for every ring
> The recursion is true for **Noetherian** $A$, and the easy lifted chain only proves $\dim A[T] \geq 1 + \dim A$. For non-Noetherian $A$ the dimension can jump: there are rings with $\dim A[T] = 1 + 2\dim A$. The reason is that a single prime of $A$ can support a chain of length up to $2$ — not $1$ — in the fibre when Noetherianity fails to bound the heights. The repair condition is exactly Noetherianity, which forces each fibre $\kappa(\mathfrak p)[T]$ to contribute at most one extra step.

> [!warning] 3. Believing $\dim A = \dim_k \mathfrak m/\mathfrak m^2$ always
> Since both measure "size at a point", it is tempting to equate the Krull dimension with the embedding dimension $\dim_k \mathfrak m/\mathfrak m^2$. The correct relation is only the inequality $\dim A \leq \dim_k \mathfrak m/\mathfrak m^2$; it is *strict* exactly at singular points. The node $k[X,Y]/(XY)$ localized at the origin has $\dim = 1$ but $\dim_k \mathfrak m/\mathfrak m^2 = 2$ (the maximal ideal $(x,y)$ needs two generators), reflecting the two branches crossing. Equality is the *definition* of a regular point, not a theorem; assuming it assumes smoothness.

> [!warning] 4. Confusing the degree of the Hilbert polynomial with its leading coefficient
> The Hilbert polynomial $P_X(n)$ carries two invariants and they are easy to conflate: its **degree** is the dimension, its (normalised) **leading coefficient** is the degree of the variety. The conic and the line in $\mathbb P^2$ both have one-dimensional Hilbert polynomials (degree $1$), but the conic's leading coefficient is twice the line's — same dimension, different degree. Reading dimension off the leading coefficient, or degree off the polynomial degree, conflates the two. The repair: degree-of-polynomial $=$ dimension; leading-coefficient-times-(dim)! $=$ degree.

---

# Problem-Solving Strategy

The first decision in any dimension problem is *which of the three faces of dimension* to compute with, because the Krull definition — the one you usually want to prove something about — is almost never the one you compute with directly.

If the ring is **a finitely generated domain over a field**, the strategy is immediate and almost mechanical: compute the [[Def - Algebraic Independence and Transcendence Degree|transcendence degree]] of its fraction field. By the [[Thm - Dimension of a Polynomial Ring|companion formula]] $\dim A = \operatorname{trdeg}_k \operatorname{Frac}(A)$, and transcendence degree is a linear-algebra-flavoured count of independent elements you can read off generators and relations. To find $\dim k[X,Y,Z]/(F)$ for an irreducible $F$, note the quotient is a domain of transcendence degree $2$ (two of the three coordinates are independent, the third algebraic over them via $F$), so the dimension is $2$ — a surface. This route, justified by Noether normalization, is the workhorse for explicit varieties and should be tried first whenever the ring is a concrete finitely generated domain.

If the question is **local — a height, or the dimension of a local ring, or a smoothness test** — reduce to a Noetherian local ring and deploy the [[Thm - The Dimension Theorem for Noetherian Local Rings|Dimension Theorem]]. Localizing at $\mathfrak p$ converts $\operatorname{ht}\mathfrak p$ into $\dim A_{\mathfrak p}$, and then you choose the most convenient of the three equal quantities: a **system of parameters** if you can guess $d$ elements cutting out the maximal ideal up to radical (best for upper bounds and inductions), or the **Hilbert–Samuel polynomial** $\ell(A/\mathfrak m^{n+1})$ if you can compute lengths (best when the associated graded ring is understood). The inductive engine is "cut by one parameter, drop the dimension by one": to prove a statement for $d$-dimensional local rings, pick $x \in \mathfrak m$ outside every minimal prime, pass to $A/(x)$ of dimension $d-1$, and induct.

If the ring is **graded**, compute the [[Thm - Hilbert-Serre and Rationality of the Poincare Series|Poincaré series]] and read the dimension as the order of its pole at $T = 1$ (equivalently, one plus the degree of the Hilbert polynomial). This is the cleanest route for projective varieties and for rings presented by monomial ideals, where the Poincaré series is a manifest rational function.

If the question is about **codimension or the effect of equations**, reach for [[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's height theorem]]: $r$ generators bound the height by $r$, and a single non-zero-divisor cuts codimension exactly one. To show a variety cut by $r$ equations has dimension $\geq n - r$, this is the only tool; to show equality, you additionally need the equations to form a regular sequence (a complete intersection), which is a smoothness-flavoured condition.

The meta-strategy that unifies all of this: **never compute Krull dimension by chasing chains of primes — translate it.** The entire architecture of the chapter exists to give you computable surrogates: transcendence degree for domains, Hilbert-polynomial degree for graded rings, system-of-parameter count for local rings. Decide which surrogate your ring supports, compute *that*, and the Dimension Theorem guarantees you have computed the Krull dimension. The single question behind every problem is "how many independent directions does this ring have?", and the three measurements are three ways of counting them.

---

# Most Reusable Properties

- **[[Thm - The Dimension Theorem for Noetherian Local Rings|The Dimension Theorem]]** ($\dim = d = \delta$): the hub from which everything radiates. Its reusability is that it lets you *switch measurement at will* — prove an inequality about chains of primes by computing a Hilbert polynomial, or bound a Hilbert polynomial by exhibiting a system of parameters. Every other theorem in the chapter (Krull's height theorem, the polynomial-ring dimension, catenary exactness) is a corollary obtained by applying the equality after localizing. When any dimension question resists the chain definition, this is the licence to change to a computable face.

- **[[Thm - Dimension of a Polynomial Ring|dim A = \operatorname{trdeg} and dim k[T₁,…,Tₙ] = n]]**: the anchor to geometry and the most-used *computation*. For any concrete finitely generated domain it reduces dimension to counting independent coordinates, and $\dim \mathbb A^n = n$ is the base case for the dimension of products, fibres, and intersections. Reach for it whenever the ring is an explicit quotient of a polynomial ring.

- **[[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's height theorem]]** ($\operatorname{ht}(x_1,\dots,x_r) \leq r$): the codimension tool. Its reusability is that it converts a *counting* fact (number of equations) into a *geometric* bound (codimension), and its principal-ideal special case — one equation, codimension one — is the algebraic heart of intersection theory and of the theory of divisors. Use it for every "how many equations does this take" question.

- **The reduction $\operatorname{ht}\mathfrak p = \dim A_{\mathfrak p}$**: the localization principle for dimension. It is reused silently in nearly every proof, because it lets a height — a global chain count below $\mathfrak p$ — be computed in the local ring $A_{\mathfrak p}$ where the Dimension Theorem applies. The trigger is any height computation; the move is "localize at $\mathfrak p$".

- **Cutting by a parameter drops dimension by one**: the inductive backbone. Whenever a statement is to be proved for all Noetherian local rings, the standard induction picks an $x \in \mathfrak m$ avoiding the minimal primes, passes to $A/(x)$ of dimension one less, and applies the inductive hypothesis. This is how the Dimension Theorem itself is proved and how most of its consequences are established.

---

# Bridges

1. **Algebraic geometry — Krull dimension is geometric dimension, height is codimension.** The dimension of an affine variety $X = V(I)$ is *defined* as the Krull dimension of its coordinate ring $A = k[T_1,\dots,T_n]/I(X)$, and this chapter proves it equals the intuitive dimension: $\dim \mathbb A^n = n$, $\dim(\text{curve}) = 1$, $\dim(\text{surface}) = 2$. A chain of primes is a tower of irreducible subvarieties, so $\dim$ is the longest such tower, and the height of a prime is the codimension of $V(\mathfrak p)$. [[Thm - Krull's Height Theorem (Principal Ideal Theorem)|Krull's principal ideal theorem]] is the geometric law that a hypersurface has codimension one — that one equation drops dimension by exactly one — which makes the **expected dimension** $n - r$ of a variety cut by $r$ equations a theorem rather than a hope. The catenary identity $\operatorname{ht}\mathfrak p + \dim A/\mathfrak p = \dim A$ is what makes codimension additive and well defined, underwriting intersection theory.

2. **Projective geometry and Hilbert schemes — the Hilbert polynomial encodes dimension, degree, and genus.** For a projective variety $X \subseteq \mathbb P^n$ with homogeneous coordinate ring $S$, the Hilbert function $n \mapsto \dim_k S_n$ becomes, for large $n$, the **Hilbert polynomial** $P_X$, whose *degree* is $\dim X$, whose *leading coefficient* (times $(\dim X)!$) is the *degree* of $X$, and whose value pattern encodes the **arithmetic genus**. So a single numerical polynomial packages the basic discrete invariants of a projective variety, and the [[Thm - Hilbert-Serre and Rationality of the Poincare Series|Hilbert–Serre theorem]] is what guarantees it exists. Fixing $P_X$ and parametrising all subschemes with that Hilbert polynomial gives the **Hilbert scheme**, the foundational moduli space of algebraic geometry — its very definition rests on this chapter's eventual-polynomiality of the Hilbert function.

3. **Singularity theory — the gap $\dim_k \mathfrak m/\mathfrak m^2 - \dim A$ measures singularity.** The [[Commutative Algebra V — Nakayama's Lemma|embedding dimension]] $\dim_k \mathfrak m/\mathfrak m^2$ is the dimension of the [[Def - Minimal Generating Set and the Cotangent Space|Zariski tangent space]], the number of coordinates needed to embed a neighbourhood of the point; the Dimension Theorem gives $\dim A \leq \dim_k \mathfrak m/\mathfrak m^2$ always, and equality *defines* a **regular** (smooth) point. The node $k[X,Y]/(XY)$ at the origin has $\dim = 1$ but tangent dimension $2$ — the excess $1$ is the singularity of the crossing. Thus dimension theory is the prerequisite for the entire local theory of smoothness, regular sequences, and resolution of singularities: you cannot say what "smooth" means without first having the two dimensions to compare.

4. **Number theory — arithmetic schemes have dimension one more than their fibres.** Because $\dim \mathbb Z = 1$ and $\dim A[T] = 1 + \dim A$, the ring $\mathbb Z[T_1,\dots,T_n]$ has dimension $n + 1$: an "arithmetic variety" over $\operatorname{Spec}\mathbb Z$ carries one extra dimension from the base, the arithmetic direction. A ring of integers $\mathcal O_K$ is one-dimensional (a [[Commutative Algebra XIII — Dedekind Domains and DVRs|Dedekind domain]]), the arithmetic analogue of a smooth curve, and $\mathcal O_K[T]$ is a two-dimensional arithmetic surface. This dimension bookkeeping — counting the arithmetic base as a genuine dimension — is what lets the geometric machinery of this chapter be imported wholesale into arithmetic geometry, where theorems about surfaces are applied to $\mathcal O_K[T]$.

---

# Insights

**The unifying frame: dimension is a growth rate, and the three definitions are three ways to measure the same growth.** The deepest way to read this chapter is that "dimension" is fundamentally an *asymptotic* notion — it measures how fast something accumulates. The Hilbert–Samuel viewpoint makes this literal: $\ell(A/\mathfrak m^{n+1})$ counts the ring "to order $n$ near the point", and its growth is polynomial of degree exactly the dimension — constant for a point, linear for a curve, quadratic for a surface. The Krull viewpoint repackages the same growth as the length of the longest nested sequence of irreducible pieces, and the system-of-parameters viewpoint repackages it as the number of independent functions needed to pin the point down. The miracle the Dimension Theorem records is that *a combinatorial count (chains), an asymptotic count (growth of lengths), and an algebraic count (generators of a parameter ideal) all return the same integer.* Once you internalise that dimension is "how fast the ring grows near a point", the equality of the three definitions stops being a coincidence and becomes three thermometers reading the same temperature — and the practical lesson is that you should always reach for whichever thermometer is easiest to read for the ring in front of you.

**The true name of dimension is "transcendence degree", and chains of primes are its shadow.** For the rings that actually arise in geometry — finitely generated algebras over a field — the operationally correct definition of dimension is not the chain-of-primes supremum (impossible to compute directly) but the [[Def - Algebraic Independence and Transcendence Degree|transcendence degree]] of the function field, the number of genuinely free coordinates. This is what you compute with, and the chain definition is the *characterisation that makes dimension intrinsic and local* but is the wrong thing to picture. The bridge between them — [[Thm - Noether Normalization|Noether normalization]] writing every variety as a finite cover of affine space, plus the invariance of dimension under finite covers — is the single most important structural fact, because it says every variety has the same dimension as the affine space it finitely covers, and an affine space's dimension is visibly its number of coordinates. So whenever you see "dimension", translate to "number of free coordinates", compute the transcendence degree, and trust the Dimension Theorem to certify that you have computed the chain count.

**A trigger-reaction pattern: "drop the dimension by one" is the universal induction.** Across the whole chapter, the move that proves the hard theorems is *cut by one well-chosen element and induct*. To prove the Dimension Theorem, to prove $\dim A[T] = 1 + \dim A$, to prove Krull's height theorem, to compute a Hilbert–Samuel polynomial — each time the reaction to "$\dim A = d$" is "choose $x \in \mathfrak m$ avoiding the minimal primes; then $\dim A/(x) = d - 1$, and the inductive hypothesis applies". The element $x$ is a single equation, and its effect is to slice off one dimension — geometrically a hyperplane section, algebraically a non-zero-divisor mod the minimal primes. Recognising this pattern turns the chapter's proofs from a list of separate arguments into one repeated manoeuvre, and it is the same slicing that, in [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma|the graded setting]], lowers the degree of a Hilbert polynomial by one. When you return to dimension theory after months, the reconstruction of almost any proof starts with "what do I cut by, and why does it drop the dimension exactly one?".
