---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Krull Dimension and Height"
  - "Thm - Noether Normalization"
  - "Thm - Integral Extensions Preserve Dimension"
  - "Thm - Dimension of a Polynomial Ring"
  - "Def - Noetherian Ring"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $k$ be a field and $A$ a finitely generated $k$-algebra that is an integral domain. Prove
$$\dim A = \operatorname{trdeg}_k A,$$
where $\operatorname{trdeg}_k A := \operatorname{trdeg}_k \operatorname{Frac}(A)$ is the transcendence degree of the fraction field over $k$.

This combines ES3 Q10 (the inequality $\dim A \leq \operatorname{trdeg}_k A$ for a finitely generated domain, by induction on transcendence degree using the localization $A_{\{x\}}$) and ES4 Q11 (the equality, and its generalization $t = \dim A$ where $t$ is the maximal cardinality of an algebraically independent subset of $A$, for a possibly non-domain finitely generated $k$-algebra). The clean route to *equality* is via [[Thm - Noether Normalization|Noether normalization]] and [[Thm - Integral Extensions Preserve Dimension|invariance of dimension under integral extensions]] (the lecture's Proposition 13.5): normalize $A$ to be finite over a polynomial ring $k[Y_1,\dots,Y_d]$ with $d = \operatorname{trdeg}_k A$, transport dimension across the integral extension, and use $\dim k[Y_1,\dots,Y_d] = d$.

**Recall:**

The objects in play are the Krull dimension, transcendence degree, Noether normalization, and integral extensions.

![[Def - Krull Dimension and Height#Krull dimension]]

The **transcendence degree** $\operatorname{trdeg}_k A$ is the common cardinality of a transcendence basis of $\operatorname{Frac}(A)$ over $k$: a maximal algebraically independent subset $\{a_1,\dots,a_d\}$ such that $\operatorname{Frac}(A)$ is algebraic over $k(a_1,\dots,a_d)$. It is additive in towers, $\operatorname{trdeg}_k E = \operatorname{trdeg}_k L + \operatorname{trdeg}_L E$, and invariant under finite (algebraic) extensions: if $A \subseteq B$ is integral with both domains, then $\operatorname{trdeg}_k A = \operatorname{trdeg}_k B$.

![[Thm - Noether Normalization#Statement]]

![[Thm - Integral Extensions Preserve Dimension#Statement]]

The key bridge — *integral extensions preserve both dimension and transcendence degree*: for $A \subseteq B$ integral with $A, B$ domains and $k$-algebras, $\dim A = \dim B$ and $\operatorname{trdeg}_k A = \operatorname{trdeg}_k B$ (Proposition 13.4).

---

# Convergent Strategy

**Problem class.** This is a *prove-an-equality-of-two-invariants* problem, of the "reduce both sides to a common model" kind. The two invariants — $\dim A$ (defined by chains of primes, combinatorial) and $\operatorname{trdeg}_k A$ (defined by algebraic independence in a field, transcendental) — live in different worlds, and the entire strategy is to find a third object, a **polynomial subring**, to which *both* invariants are visibly equal, and a structural fact — **integrality** — that transports both invariants from $A$ down to that subring without change. It is the theorem that makes "dimension of a variety" a computable and geometric notion: the dimension is just the number of independent coordinates.

**Assumption pattern.** Three hypotheses, each load-bearing. "$A$ finitely generated over $k$" is exactly the hypothesis of [[Thm - Noether Normalization|Noether normalization]] — it is what lets you write $A$ as a finite module over a polynomial subring. "$A$ is a domain" is needed so that $\operatorname{Frac}(A)$ exists, so that $\operatorname{trdeg}_k A$ is defined, and so that the integral extension $k[Y_1,\dots,Y_d] \subseteq A$ has both rings domains (allowing transcendence degree to transfer). "$k$ a field" anchors transcendence degree. The recognisable trigger for the whole approach is "finitely generated $k$-algebra domain" — the precise class on which Noether normalization plus dimension-invariance applies.

**Theorem routing.** The route is: by Noether normalization, get a finite integral injection $k[Y_1,\dots,Y_d] \hookrightarrow A$ with $d = \operatorname{trdeg}_k A$ (the normalization parameter *equals* the transcendence degree, because transcendence degree is preserved by the integral extension and $\operatorname{trdeg}_k k[Y_1,\dots,Y_d] = d$). Then [[Thm - Integral Extensions Preserve Dimension|integral invariance of dimension]] (Proposition 13.4(i), via lying-over, going-up, incomparability) gives $\dim A = \dim k[Y_1,\dots,Y_d]$. Finally $\dim k[Y_1,\dots,Y_d] = d$ (the [[Thm - Dimension of a Polynomial Ring|dimension of a polynomial ring]]). Chaining: $\dim A = d = \operatorname{trdeg}_k A$. The alternative ES3 Q10 route proves $\dim A \leq \operatorname{trdeg}_k A$ directly by induction on $\operatorname{trdeg}$ using the localization $A_{\{x\}}$, and the reverse inequality by exhibiting a chain via the normalization.

**Key decision point.** Two non-obvious moves. First, *choosing the polynomial subring as the common model* — neither $\dim$ nor $\operatorname{trdeg}$ is easy to compute on $A$ itself, but both are trivial on $k[Y_1,\dots,Y_d]$, and the genuine insight is that integrality is a strong enough relation to equate *both* invariants across the extension simultaneously. Second, *recognising that the Noether-normalization parameter $d$ is forced to be the transcendence degree*: $A$ is integral (hence algebraic) over $k[Y_1,\dots,Y_d]$, so $\operatorname{Frac}(A)$ is algebraic over $k(Y_1,\dots,Y_d)$, so they share transcendence degree $d$ — you do not get to choose $d$ independently, it is pinned by the birational geometry. Missing this, one might think dimension and transcendence degree could disagree; the point is that the *same* integer $d$ computes both.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra XII — Dimension Theory#Legal Operations|the topic page's Legal Operations]]:

1. **Noether-normalize a finitely generated $k$-algebra.** Write $A$ as a finite (integral) module over a polynomial subring $k[Y_1,\dots,Y_d] \hookrightarrow A$.

2. **Transport transcendence degree across an integral extension.** Integrality makes $\operatorname{Frac}(A)$ algebraic over $k(Y_1,\dots,Y_d)$, so $\operatorname{trdeg}_k A = \operatorname{trdeg}_k k[Y_1,\dots,Y_d] = d$.

3. **Transport Krull dimension across an integral extension (Proposition 13.4).** Lying-over, going-up and incomparability give $\dim A = \dim k[Y_1,\dots,Y_d]$.

4. **Compute the dimension of a polynomial ring.** $\dim k[Y_1,\dots,Y_d] = d$, the base computation of dimension theory.

5. **Chain equalities to identify two invariants.** $\dim A = d = \operatorname{trdeg}_k A$.

---

# Hints

> [!note]- Hint 1
> Both $\dim A$ and $\operatorname{trdeg}_k A$ are hard to read off $A$ directly. Look for a *simpler ring* to which both are equal and to which $A$ is closely related. Which structure theorem writes a finitely generated $k$-algebra as a finite module over a polynomial ring?

> [!note]- Hint 2
> [[Thm - Noether Normalization|Noether normalization]] gives a finite integral injection $k[Y_1,\dots,Y_d] \hookrightarrow A$. The polynomial ring $k[Y_1,\dots,Y_d]$ has $\dim = d$ and $\operatorname{trdeg}_k = d$ — both invariants are obvious there. Now you need: does the integral extension change either invariant?

> [!note]- Hint 3
> Integral extensions preserve *both* invariants. For dimension this is Proposition 13.4(i): lying-over and going-up lift a chain in the base to a chain upstairs, incomparability stops chains from collapsing, so $\dim A = \dim k[Y_1,\dots,Y_d]$. For transcendence degree, integrality means $\operatorname{Frac}(A)$ is algebraic over $k(Y_1,\dots,Y_d)$, so they have the same transcendence degree $d$.

> [!note]- Hint 4
> Assemble: $d = \operatorname{trdeg}_k k[Y_1,\dots,Y_d] = \operatorname{trdeg}_k A$ (integral $\Rightarrow$ same trdeg), and $d = \dim k[Y_1,\dots,Y_d] = \dim A$ (integral $\Rightarrow$ same dim). Hence $\dim A = \operatorname{trdeg}_k A$. The one subtlety: check that the Noether-normalization parameter $d$ is *forced* to equal $\operatorname{trdeg}_k A$ — it is, because the extension is integral.

---

# Solution

The proof equates two invariants by routing both through a polynomial subring. Noether normalization produces a finite integral extension $k[Y_1,\dots,Y_d] \subseteq A$; integrality preserves transcendence degree, forcing $d = \operatorname{trdeg}_k A$; integrality also preserves Krull dimension (lying-over / going-up / incomparability), giving $\dim A = \dim k[Y_1,\dots,Y_d]$; and the polynomial ring has dimension $d$. The two invariants meet at the single integer $d$.

**Step 1: Noether-normalize $A$.**

There is a polynomial subring $k[Y_1,\dots,Y_d] \subseteq A$ over which $A$ is a finite (hence integral) module.

> [!note]- Derivation
> $A$ is a finitely generated $k$-algebra, so by [[Thm - Noether Normalization|Noether's normalization theorem]] there exist $Y_1,\dots,Y_d \in A$, algebraically independent over $k$, such that $A$ is a finitely generated module over the polynomial subring $k[Y_1,\dots,Y_d]$. In particular the inclusion
> $$k[Y_1,\dots,Y_d] \hookrightarrow A$$
> is an **integral** ring extension (a finite extension is integral: every element of $A$ satisfies a monic polynomial over $k[Y_1,\dots,Y_d]$). Both rings are integral domains ($A$ by hypothesis, $k[Y_1,\dots,Y_d]$ as a polynomial ring over a field).

**Step 2: The normalization parameter equals the transcendence degree, $d = \operatorname{trdeg}_k A$.**

Integrality forces $\operatorname{Frac}(A)$ algebraic over $k(Y_1,\dots,Y_d)$, so the transcendence degrees agree.

> [!note]- Derivation
> Since $A$ is integral — hence algebraic — over $k[Y_1,\dots,Y_d]$, passing to fraction fields, $\operatorname{Frac}(A)$ is algebraic over $k(Y_1,\dots,Y_d)$. By additivity of transcendence degree in towers $k \subseteq k(Y_1,\dots,Y_d) \subseteq \operatorname{Frac}(A)$,
> $$\operatorname{trdeg}_k \operatorname{Frac}(A) = \operatorname{trdeg}_k k(Y_1,\dots,Y_d) + \underbrace{\operatorname{trdeg}_{k(Y_1,\dots,Y_d)} \operatorname{Frac}(A)}_{= 0 \text{ (algebraic)}} = d.$$
> Here $\operatorname{trdeg}_k k(Y_1,\dots,Y_d) = d$ because $Y_1,\dots,Y_d$ are algebraically independent over $k$. Thus
> $$\operatorname{trdeg}_k A = d.$$
> This is the content of Proposition 13.4(ii): integral extensions of $k$-algebra domains preserve transcendence degree.

**Step 3: Integral invariance gives $\dim A = \dim k[Y_1,\dots,Y_d]$.**

Lying-over, going-up, and incomparability make dimension invariant across the integral extension.

> [!note]- Derivation
> By [[Thm - Integral Extensions Preserve Dimension|Proposition 13.4(i)]], an integral extension $B \subseteq C$ of rings satisfies $\dim B = \dim C$. The argument: given a chain $\mathfrak{q}_0 \subsetneq \cdots \subsetneq \mathfrak{q}_d$ of primes in $B$, **lying-over** and **going-up** produce primes $\mathfrak{Q}_0 \subseteq \cdots \subseteq \mathfrak{Q}_d$ of $C$ with $\mathfrak{Q}_i \cap B = \mathfrak{q}_i$, strict because the contractions differ, so $\dim C \geq \dim B$; conversely, contracting a chain in $C$ yields a chain in $B$, strict by **incomparability** (no two primes of $C$ over the same prime of $B$ are comparable), so $\dim B \geq \dim C$. Applying this to $B = k[Y_1,\dots,Y_d] \subseteq A = C$,
> $$\dim A = \dim k[Y_1,\dots,Y_d].$$

**Step 4: The polynomial ring has dimension $d$; chain the equalities.**

Combining with $\dim k[Y_1,\dots,Y_d] = d$ and Step 2 yields the result.

> [!note]- Derivation
> By [[Thm - Dimension of a Polynomial Ring|the dimension of a polynomial ring]], $\dim k[Y_1,\dots,Y_d] = d$ (see [[Ex - The dimension of a polynomial ring is n]]). Therefore, using Steps 2–4,
> $$\dim A \;\overset{\text{Step 3}}{=}\; \dim k[Y_1,\dots,Y_d] \;=\; d \;\overset{\text{Step 2}}{=}\; \operatorname{trdeg}_k A.$$
> Hence $\dim A = \operatorname{trdeg}_k A$. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** For a finitely generated $k$-algebra domain $A$, $\dim A = \operatorname{trdeg}_k A$.
>
> By Noether normalization, there is an integral extension $k[Y_1,\dots,Y_d] \hookrightarrow A$ with $Y_1,\dots,Y_d$ algebraically independent over $k$ and $A$ finite over the subring.
>
> *Transcendence degree.* Integrality makes $\operatorname{Frac}(A)$ algebraic over $k(Y_1,\dots,Y_d)$, so by tower additivity $\operatorname{trdeg}_k A = \operatorname{trdeg}_k k(Y_1,\dots,Y_d) = d$.
>
> *Dimension.* By integral invariance of dimension (Proposition 13.4(i): lying-over, going-up, incomparability), $\dim A = \dim k[Y_1,\dots,Y_d] = d$ (the dimension of a polynomial ring).
>
> Therefore $\dim A = d = \operatorname{trdeg}_k A$. $\blacksquare$
>
> *Remark (the non-domain generalization, ES4 Q11).* If $A \neq 0$ is a finitely generated $k$-algebra, not necessarily a domain, let $t$ be the maximal cardinality of a $k$-algebraically independent subset of $A$. Then $t = \dim A$. Reduce to the domain case: $\dim A = \max_i \dim A/\mathfrak{p}_i$ over the (finitely many) minimal primes $\mathfrak{p}_i$, each $A/\mathfrak{p}_i$ a finitely generated domain with $\dim A/\mathfrak{p}_i = \operatorname{trdeg}_k A/\mathfrak{p}_i$; and $t = \max_i \operatorname{trdeg}_k A/\mathfrak{p}_i$ because a maximal algebraically independent subset of $A$ maps to one in some component.

---

# Key Takeaways

**To equate two invariants from different worlds, route both through a common model on which both are obvious.** Krull dimension is combinatorial (chains of primes); transcendence degree is transcendental (algebraic independence in a field). Neither is easy to compute on a general finitely generated algebra, and there is no direct bridge between "longest chain of primes" and "size of a transcendence basis." The strategy that wins is to interpose a *third* ring — the polynomial subring $k[Y_1,\dots,Y_d]$ from Noether normalization — on which $\dim = d$ and $\operatorname{trdeg} = d$ are both visible, and then to use a single structural relation, **integrality**, strong enough to drag *both* invariants from $A$ down to the model unchanged. This "common model" pattern is one of the most reusable in algebra: it is exactly how one proves invariance of dimension, the going-up theorems, and the well-definedness of geometric degree. The meta-lesson for spaced practice: when two invariants must be shown equal, do not look for a map between their definitions — look for a normal form that computes both.

**Noether normalization is the structural backbone of dimension theory: every affine variety is a branched cover of affine space.** The theorem $\dim A = \operatorname{trdeg}_k A$ is the cleanest expression of the geometric idea that **bold plain text — a $d$-dimensional affine variety is a finite branched cover of $\mathbb{A}^d$.** Noether normalization realizes this cover explicitly: $A$ finite over $k[Y_1,\dots,Y_d]$ means the variety $\operatorname{Spec} A$ maps to affine $d$-space with finite fibres, and the number $d$ — the dimension, the transcendence degree, the number of coordinates of the base — is one and the same. Integrality is the precise hypothesis that makes this a *finite* cover (proper, finite fibres), which is why it preserves dimension: a finite map cannot raise or lower the number of independent directions. Carrying this picture — "$d$-fold cover of $\mathbb{A}^d$" — makes the equality intuitive: a variety has as many independent coordinate-directions ($\operatorname{trdeg}$) as it has dimensions to shrink in ($\dim$), because it is *spread finitely over* a $d$-dimensional coordinate space.

**Integrality preserves everything that matters about dimension, and this is why finite morphisms are the well-behaved ones.** The deep reusable fact is that an integral (equivalently, for finitely generated algebras, finite) extension preserves Krull dimension *and* transcendence degree *and* (where defined) the field of fractions up to algebraic closure. Dimension-invariance rests on the triad **bold plain text — lying-over, going-up, incomparability**: lying-over and going-up *lift* chains upward (so dimension cannot drop), incomparability prevents distinct upstairs primes from collapsing onto one downstairs (so dimension cannot rise). These three are the algebraic skeleton of "fibres of a finite map are finite and dimension-preserving," and they recur throughout: in the proof of the [[Thm - Dimension of a Polynomial Ring|dimension of a polynomial ring]], in the theory of finite morphisms, and in the fibre-dimension theorem. Whenever you see "finite over" or "integral over," reach for these three.

**For finitely generated algebras over a field, dimension is computable, geometric, and additive — and this exercise is why.** The equality $\dim A = \operatorname{trdeg}_k A$ is not merely an identity; it is what makes dimension *usable*. It gives a finite recipe (find a transcendence basis, count it), it identifies dimension with the geometric "number of coordinates," and it powers the further identities $\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$ (see [[Ex - Height plus dimension of the quotient equals dimension]]) and $\operatorname{trdeg}_k k[T_1,\dots,T_n]/(f) = n-1$ for irreducible $f$ — both of which reduce, via this theorem, to additivity of transcendence degree in towers. The non-domain version $t = \dim A$ extends the recipe to reducible varieties by taking the max over irreducible components, matching the geometric fact that a variety's dimension is the largest dimension among its components. This is the result that lets a geometer say "the dimension of $X$" and compute it by counting independent functions — the practical heart of the whole chapter.
