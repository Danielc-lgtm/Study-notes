---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - The I-adic Completion"
  - "Def - Noetherian Ring"
  - "Def - Polynomial Ring"
  - "Def - Ideal"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a [[Def - Noetherian Ring|Noetherian]] ring. We write $R[T_1,\dots,T_n]$ for the [[Def - Polynomial Ring|polynomial ring]] and $R[[T_1,\dots,T_n]]$ for the **formal power series ring** — the set of formal sums $\sum_{\alpha}c_\alpha T^\alpha$ over all multi-indices $\alpha=(\alpha_1,\dots,\alpha_n)\in\mathbb{N}^n$, with $c_\alpha\in R$ and $T^\alpha=T_1^{\alpha_1}\cdots T_n^{\alpha_n}$, under the usual (Cauchy-product) addition and multiplication. We write $\mathfrak{m}=(T_1,\dots,T_n)$ for the ideal of power series with zero constant term, $\widehat{R}^{\,\mathfrak{m}}$ for the [[Def - The I-adic Completion|\mathfrak{m}-adic completion]]. The full registry is on [[Commutative Algebra X — Completions and Limits]].

---

# Statement

> **Theorem (Noetherianity of formal power series).** If $R$ is a Noetherian ring, then the formal power series ring $R[[T_1,\dots,T_n]]$ is Noetherian. In particular, for a field $k$, the ring $k[[T_1,\dots,T_n]]$ is Noetherian.

> **Corollary.** Every complete local ring of the form $k[[T_1,\dots,T_n]]/I$ is Noetherian, and so is the [[Def - The I-adic Completion|complete local ring]] $\widehat{\mathcal{O}_{X,x}}$ of any variety at any point.

This is the formal-power-series analogue of [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]] ($R$ Noetherian $\Rightarrow R[T_1,\dots,T_n]$ Noetherian), and it cannot be deduced from Hilbert directly: $R[[T_1,\dots,T_n]]$ is *not* finitely generated as an $R$-algebra.

---

# Motivation

Hilbert's basis theorem made polynomial rings safe: over a Noetherian base, adjoining finitely many variables keeps the ring Noetherian, so every affine variety has a Noetherian coordinate ring and finiteness pervades algebraic geometry. But the local-analytic study of a variety lives not in polynomials but in *power series* — the functions on the formal disk are Taylor series, not truncated ones — and one needs the same guarantee there. This theorem provides it: formal power series over a Noetherian ring are again Noetherian, so the formal disk is as finitely-controlled as the variety it sits inside. Without it, $k[[T_1,\dots,T_n]]$ might have ideals with no finite generating set, and the entire local theory — the structure of singularities, the dimension of complete local rings, the convergence of formal solutions — would collapse.

The striking feature is *how* the theorem is true: it is not proved from scratch but as a one-line consequence of the completion theorem. The power series ring is the completion of the polynomial ring at the ideal of the origin, $R[[T_1,\dots,T_n]]=\widehat{R[T_1,\dots,T_n]}^{\,(T_1,\dots,T_n)}$, and completion preserves Noetherianity. So the deep content sits in the completion theorem, and this corollary is the cashing-out of that content into the single most-used Noetherian ring of local algebra. The reason it cannot be done by Hilbert alone is worth holding onto: a power series uses *infinitely many* coefficients, so $R[[T]]$ is not a finitely generated $R$-algebra, and the inductive "adjoin one variable" argument of Hilbert has no foothold. Completion is the only bridge.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is "$R$ is Noetherian". The disguised sources are the same as for the completion theorem, since this is its corollary.

The first disguised source is **"$R$ is a field, or $\mathbb{Z}$, or any PID"**. The property $B$ is "Noetherian base of arithmetic interest". The bridge is immediate — fields and PIDs are Noetherian — and the conclusion is that $k[[T_1,\dots,T_n]]$, $\mathbb{Z}[[T]]$, $\mathbb{Z}_p[[T]]$ are all Noetherian. The non-obviousness is that the *iterated* construction stays Noetherian. *Example problem:* the Iwasawa algebra $\mathbb{Z}_p[[T]]$ is Noetherian.

The second disguised source is **"$R$ is itself a power series ring or complete local ring"**. The property $B$ is "$R=k[[S_1,\dots,S_m]]$". The bridge is this theorem applied once: $R$ is Noetherian, so $R[[T_1,\dots,T_n]]=k[[S_1,\dots,S_m,T_1,\dots,T_n]]$ is Noetherian. The non-obviousness is that mixing more variables in does not break finiteness. *Example problem:* $k[[x,y,z]]$ is Noetherian (apply twice from $k$).

The third disguised source is **"$R$ is a finitely generated algebra over a field"**. The property $B$ is "coordinate ring of an affine variety". The bridge is Hilbert (making $R$ Noetherian) followed by this theorem. The result is that the formal completion of any affine coordinate ring is Noetherian. *Example problem:* the complete local ring at a singular point of a plane curve, $k[[x,y]]/(f)$, is Noetherian.

**Targets (Output Amplification)**

The conclusion is "$R[[T_1,\dots,T_n]]$ is Noetherian".

Combine with **the maximal ideal $\mathfrak{m}=(T_1,\dots,T_n)$** to conclude $k[[T_1,\dots,T_n]]$ is a Noetherian *local* ring. The additional fact $D$ is that a power series is a unit iff its constant term is a unit, so the non-units form the single maximal ideal $\mathfrak{m}$. The result $E$ is that $k[[T_1,\dots,T_n]]$ is a regular local ring of dimension $n$ — the basic model of a smooth point's formal disk. Nonobvious because locality plus Noetherianity plus the dimension count together identify it as regular.

Combine with **a quotient by an ideal $I$** to get Noetherianity of $k[[T_1,\dots,T_n]]/I$. The additional data $D$ is any ideal $I$. The result $E$ is that *every* complete local ring arising as such a quotient — i.e., by Cohen's theorem, every complete Noetherian local ring containing a field — is Noetherian. Nonobvious because it makes the entire class of complete local rings tractable.

Combine with **flatness of the inclusion $R[T_1,\dots,T_n]\hookrightarrow R[[T_1,\dots,T_n]]$** to transport module-theoretic facts. The additional structure $D$ is the completion map's flatness. The result $E$ is that exactness of sequences of finitely generated polynomial-ring modules is preserved on completing to power series, so one may compute syzygies formally. Nonobvious because it lets local computations be done with power series and descended to polynomials.

---

# Why Is It True

The whole proof is the observation that **a formal power series is a compatible thread of polynomial truncations**, so the power series ring is literally a completion. Fix $\mathfrak{m}=(T_1,\dots,T_n)$ in $A=R[T_1,\dots,T_n]$. The quotient $A/\mathfrak{m}^N$ keeps only the monomials of total degree $<N$ — it is the ring of polynomials truncated at degree $N-1$. A compatible thread $(p_N)_N$ with $p_N\in A/\mathfrak{m}^N$ refining $p_{N-1}$ is exactly a choice of coefficient for every monomial, consistent across truncations — which is precisely a formal power series. Hence
$$\widehat{A}^{\,\mathfrak{m}}=\varprojlim_N A/\mathfrak{m}^N=R[[T_1,\dots,T_n]].$$

**A power series is the $\mathfrak{m}$-adic completion of a polynomial, so $R[[T_1,\dots,T_n]]=\widehat{R[T_1,\dots,T_n]}$ — and completion preserves Noetherian.**

Now [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]] makes $A=R[T_1,\dots,T_n]$ Noetherian, and [[Thm - The Completion of a Noetherian Ring is Noetherian|the completion theorem]] makes $\widehat{A}=R[[T_1,\dots,T_n]]$ Noetherian. That is the entire argument: the content is borrowed, and the only insight is the *identification* of the power series ring as a completion. The reason this is not circular — the reason it does not just re-prove Hilbert — is that the completion theorem's proof of Noetherianity goes through the associated graded ring, where Hilbert *does* apply (the graded ring is a polynomial ring quotient), and lifts to the completion by completeness; it does not assume the power series ring finitely generated.

---

# What Makes This Hard

The only real conceptual hurdle is resisting the temptation to prove it like Hilbert's theorem — by induction on the number of variables, taking leading coefficients of an ideal. That route *fails* for power series because there is no "leading coefficient": a non-zero power series has a lowest-degree term, not a highest one, and the ascending-chain argument that works for polynomials does not transfer. The correct move is to recognise the power series ring as a *completion* and import the completion theorem; the difficulty is purely in seeing that identification, after which the proof is a single sentence. The common error is to attempt a direct ideal-theoretic proof and get stuck on the absence of a top degree.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Identify $R[[T_1,\dots,T_n]]$ as the $\mathfrak{m}$-adic completion of $R[T_1,\dots,T_n]$ with $\mathfrak{m}=(T_1,\dots,T_n)$, then quote Hilbert (polynomial ring Noetherian) and the completion theorem (completion of Noetherian is Noetherian).

**Subgoal decomposition:**

1. **Truncation = degree truncation.** Show $R[T_1,\dots,T_n]/\mathfrak{m}^N$ is the ring of polynomials of degree $<N$.
   - *Hint:* $\mathfrak{m}^N$ is spanned by monomials of total degree $\geq N$.
   - *Why needed:* It identifies the truncation tower whose limit is the power series ring.

2. **Power series = completion.** Conclude $R[[T_1,\dots,T_n]]=\varprojlim_N R[T_1,\dots,T_n]/\mathfrak{m}^N$.
   - *Hint:* A compatible thread of truncations is a consistent choice of all coefficients, i.e. a power series.
   - *Why needed:* It is the identification that lets the completion theorem apply.

3. **Quote the two theorems.** $R$ Noetherian $\Rightarrow R[T_1,\dots,T_n]$ Noetherian (Hilbert) $\Rightarrow$ its completion $R[[T_1,\dots,T_n]]$ Noetherian (completion theorem).
   - *Hint:* Both are black boxes; chain them.
   - *Why needed:* It is the conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: The $\mathfrak{m}$-adic truncation of the polynomial ring is degree truncation
> **Statement:** For $A=R[T_1,\dots,T_n]$ and $\mathfrak{m}=(T_1,\dots,T_n)$, $\mathfrak{m}^N$ is the ideal generated by all monomials of total degree $N$, and $A/\mathfrak{m}^N$ is the free $R$-module on monomials of total degree $<N$.
>
> **Hint:** A product of $N$ generators $T_i$ has total degree $N$.
>
> **Why needed:** It identifies the truncation tower as the degree filtration, whose inverse limit is the power series ring.
>
> > [!note]- Full proof
> > The ideal $\mathfrak{m}=(T_1,\dots,T_n)$ consists of polynomials with zero constant term. A product of $N$ elements of $\mathfrak{m}$ is an $R$-combination of products $T_{i_1}\cdots T_{i_N}$, each of total degree $\geq N$; conversely every monomial of total degree $\geq N$ is such a product. Hence $\mathfrak{m}^N$ is spanned over $R$ by monomials of total degree $\geq N$. Therefore $A/\mathfrak{m}^N$ has as $R$-basis the monomials of total degree $<N$, i.e. it is the ring of polynomials truncated at degree $N-1$.

> [!note]- Lemma 2: The inverse limit of degree truncations is the power series ring
> **Statement:** $\varprojlim_N A/\mathfrak{m}^N\cong R[[T_1,\dots,T_n]]$.
>
> **Hint:** A thread assigns, compatibly, a coefficient to every monomial.
>
> **Why needed:** It realises $R[[T_1,\dots,T_n]]$ as a completion, so the completion theorem applies.
>
> > [!note]- Full proof
> > By Lemma 1, an element of $\varprojlim_N A/\mathfrak{m}^N$ is a compatible family $(p_N)_N$ where $p_N$ is a polynomial of degree $<N$ and $p_{N+1}\equiv p_N\pmod{\mathfrak{m}^N}$ (i.e. $p_{N+1}$ and $p_N$ agree on monomials of degree $<N$). Such a family is exactly a single assignment $\alpha\mapsto c_\alpha\in R$ of a coefficient to each monomial $T^\alpha$, with $p_N=\sum_{|\alpha|<N}c_\alpha T^\alpha$. This data is a formal power series $\sum_\alpha c_\alpha T^\alpha$. The bijection respects addition and multiplication (the Cauchy product computes each coefficient using only finitely many lower ones, compatibly with truncation), so $\varprojlim_N A/\mathfrak{m}^N\cong R[[T_1,\dots,T_n]]$ as rings.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be Noetherian, $A=R[T_1,\dots,T_n]$, $\mathfrak{m}=(T_1,\dots,T_n)\trianglelefteq A$.
>
> By Lemma 1, $A/\mathfrak{m}^N$ is the ring of polynomials of degree $<N$, and the transition maps $A/\mathfrak{m}^{N+1}\to A/\mathfrak{m}^N$ are degree truncation. By Lemma 2,
> $$\widehat{A}^{\,\mathfrak{m}}=\varprojlim_N A/\mathfrak{m}^N\cong R[[T_1,\dots,T_n]].$$
> Now $R$ is Noetherian, so by [[Thm - Hilbert's Basis Theorem|Hilbert's basis theorem]] the polynomial ring $A=R[T_1,\dots,T_n]$ is Noetherian. By [[Thm - The Completion of a Noetherian Ring is Noetherian|the completion theorem]] (part 1), the $\mathfrak{m}$-adic completion $\widehat{A}^{\,\mathfrak{m}}$ of the Noetherian ring $A$ is Noetherian. Therefore $R[[T_1,\dots,T_n]]\cong\widehat{A}^{\,\mathfrak{m}}$ is Noetherian.
>
> In particular, taking $R=k$ a field, $k[[T_1,\dots,T_n]]$ is Noetherian; and any quotient $k[[T_1,\dots,T_n]]/I$ is Noetherian as a quotient of a Noetherian ring. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Weierstrass preparation and division.** In $k[[T_1,\dots,T_n]]$ the Weierstrass preparation theorem writes a power series (regular in $T_n$) as a unit times a *distinguished polynomial* in $T_n$ over $k[[T_1,\dots,T_{n-1}]]$; this gives a *second*, self-contained proof that the power series ring is Noetherian, by induction on $n$ via the preparation theorem rather than via completion. Comparing the two proofs is the bridge; nonobvious because preparation is "analytic" while completion is "limit-theoretic", yet they prove the same finiteness.

**Generating functions and the recursion algebra.** A combinatorial generating function $\sum a_n T^n$ lives in $\mathbb{Q}[[T]]$, and the fact that a sequence satisfying a linear recursion with constant coefficients has a *rational* generating function is the statement that its series lies in the localization of $\mathbb{Q}[T]$ inside the Noetherian ring $\mathbb{Q}[[T]]$. The Noetherianity guarantees the algebra of such generating functions is finitely controlled. The application is nonobvious because "finiteness of recursions" is the ideal-theoretic finiteness of this theorem.

**Formal groups and $\mathbb{Z}_p[[T]]$ in arithmetic.** A one-dimensional formal group law is a power series $F(X,Y)\in R[[X,Y]]$ over a ring $R$, and the deformation theory of formal groups is module theory over $R[[T]]$; this theorem's guarantee that $\mathbb{Z}_p[[T]]$ is Noetherian is what makes the classifying objects (Lubin–Tate, Iwasawa modules) finitely generated. The application is nonobvious because the arithmetic of formal groups rests silently on Noetherianity of the completed coefficient ring.

---

# Bridges

- **[[Thm - The Completion of a Noetherian Ring is Noetherian|Completion of a Noetherian Ring is Noetherian]]** — the parent theorem, of which this is the corollary. The power series ring is the $\mathfrak{m}$-adic completion of the polynomial ring, and the parent theorem supplies the Noetherianity. All the depth — the associated-graded-ring argument — lives in the parent; this page is the identification "power series = completion" plus a citation.

- **[[Thm - Hilbert's Basis Theorem|Hilbert's Basis Theorem]]** — the polynomial-ring twin. Hilbert handles the *finitely generated* algebras $R[T_1,\dots,T_n]$; this theorem handles the *not* finitely generated power-series rings $R[[T_1,\dots,T_n]]$. The two together cover every standard ring of commutative algebra. The proof here *uses* Hilbert (to make the polynomial ring Noetherian before completing), so this theorem is genuinely downstream of it.

- **[[Def - The I-adic Completion|the \mathfrak{a}-adic completion]]** — the construction that makes the identification work. Recognising $R[[T_1,\dots,T_n]]$ as $\varprojlim R[T]/\mathfrak{m}^N$ is an instance of "a completion is a ring of compatible truncation-threads", with the truncations being polynomial degree-truncations and the threads being power series.

- **Cohen structure theorem and the local classification** — the downstream application. Because $k[[T_1,\dots,T_n]]$ is Noetherian, Cohen's theorem can present every equicharacteristic complete Noetherian local ring as a quotient $k[[T_1,\dots,T_n]]/I$, making power series the universal local model. This theorem is the finiteness input that Cohen's presentation requires.

---

# Unlocked by This

> [!tip] Regular local rings and smooth points *(from Algebraic Geometry)*
> The ring $k[[T_1,\dots,T_n]]$, now known to be Noetherian and local, is the prototypical **regular local ring** of dimension $n$ — its maximal ideal $(T_1,\dots,T_n)$ is generated by exactly $\dim=n$ elements. A point of a variety is **smooth** precisely when its complete local ring is such a power series ring, so this theorem provides the standard against which smoothness is measured: $\widehat{\mathcal{O}_{X,x}}\cong k[[T_1,\dots,T_d]]$ iff $x$ is a smooth $d$-dimensional point. Singular points are detected by their complete local rings *failing* to be power-series rings, e.g. the node $k[[x,y]]/(xy)$.

> [!tip] The Iwasawa algebra and $p$-adic $L$-functions *(from Number Theory)*
> Iterating this theorem gives that the **Iwasawa algebra** $\Lambda=\mathbb{Z}_p[[T]]$ is a Noetherian (in fact regular local) ring of dimension $2$; its finitely generated modules are classified up to pseudo-isomorphism, and this classification controls the growth of $p$-parts of class groups along $\mathbb{Z}_p$-extensions. The $p$-adic $L$-functions are elements of $\Lambda$, and the main conjecture of Iwasawa theory is an equality of ideals in $\Lambda$ — all resting on the Noetherianity this theorem provides.
