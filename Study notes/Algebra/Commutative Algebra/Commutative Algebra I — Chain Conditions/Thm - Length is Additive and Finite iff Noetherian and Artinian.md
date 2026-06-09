---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Composition Series and Length"
  - "Def - Noetherian and Artinian Module"
  - "Def - Exact Sequence and Short Exact Sequence"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$; modules are unital. Let $R$ be a ring. We write $\ell(M) = \ell_R(M)$ for the [[Def - Composition Series and Length|length]] of an $R$-module $M$ — the common length of all its composition series, $\infty$ if none exists, $\ell(0) = 0$. A module is **simple** if it is non-zero with no proper non-zero [[Def - Submodule|submodule]]; the composition factors of $M$ are the simple quotients $M_i/M_{i+1}$ of a composition series. "Noetherian"/"Artinian" are the ascending/descending [[Def - Noetherian and Artinian Module|chain conditions]]. A short exact sequence is $0 \to N \to M \to L \to 0$. The full registry is on [[Commutative Algebra I — Chain Conditions]].

---

# Statement

> **Theorem (length: finiteness criterion and additivity).** Let $R$ be a ring and $M$ an $R$-module.
>
> 1. **(Finiteness criterion.)** $\ell(M) < \infty$ if and only if $M$ is both Noetherian and Artinian.
> 2. **(Additivity.)** For any short exact sequence $0 \to N \xrightarrow{i} M \xrightarrow{p} L \to 0$ of finite-length modules,
> $$\ell(M) = \ell(N) + \ell(L).$$
> 3. **(Alternating sum.)** For any exact sequence $0 \to M_0 \to M_1 \to \cdots \to M_n \to 0$ of finite-length modules,
> $$\sum_{i=0}^{n} (-1)^i \ell(M_i) = 0.$$

> **Corollary (vector spaces).** For a $k$-vector space $V$, the conditions $\dim_k V < \infty$, $\ell(V) < \infty$, $V$ Noetherian, $V$ Artinian are all equivalent, and then $\ell(V) = \dim_k V$.

Part 3 is part 2 telescoped: splitting the long exact sequence at each spot into short exact sequences and summing with signs cancels the intermediate lengths.

---

# Motivation

Length is the invariant that completes the chapter by *unifying* its two chain conditions. The first two theorems treated Noetherian and Artinian as independent finiteness conditions; this theorem reveals that their *conjunction* has a clean numerical meaning — finite length — and that this number behaves exactly like a dimension. The finiteness criterion (part 1) is the bridge: it says "finite length" is not a third, separate condition but precisely "Noetherian and Artinian together", so the two halves of finiteness, "cannot grow forever" and "cannot shrink forever", combine into a single integer.

Additivity (part 2) is what makes length *useful* rather than merely definable. An invariant that adds along short exact sequences can be computed by decomposition: break a module into a sub and a quotient, compute each, add. This is the same principle as rank–nullity for vector spaces ($\dim V = \dim \ker f + \dim \operatorname{im} f$ is additivity of $\dim$ along $0 \to \ker f \to V \to \operatorname{im} f \to 0$), now available over any ring for finite-length modules. The alternating-sum form (part 3) is the prototype of an Euler characteristic: along a long exact sequence the lengths cancel in alternating fashion, exactly as Betti numbers do in topology.

The corollary anchors everything to the familiar case. Over a field, all the chapter's notions collapse: Noetherian, Artinian, finite length, and finite-dimensional are one condition, and $\ell = \dim$. So the entire apparatus of chain conditions and length is, over a field, just dimension theory — and the interest of the general theory is precisely the phenomena (like Noetherian $\neq$ Artinian) that *cannot* occur over a field but *do* occur over a ring. This theorem is where you see the general machinery reduce, in the field case, to something you already know completely.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition for the additivity statements is "the modules have finite length", and for the criterion "both chain conditions hold".

The first disguised source is **a module over an Artinian ring, or a finitely generated module over a ring that is both Noetherian and Artinian (e.g. $k[T]/(f)$)**. The property $B$ is "$M$ is finitely generated over an Artinian ring". Then $M$ is both Noetherian and Artinian by [[Thm - Finitely Generated Modules over a Noetherian Ring are Noetherian|the finite-generation theorem]] (applied in both chain conditions), so $\ell(M) < \infty$. The non-obvious value is that finite length comes for free from finite generation once the base is Artinian. *Example problem:* every finitely generated module over $\mathbb{Z}/n$ has finite length.

The second disguised source is **a finite-dimensional vector space, or a module annihilated by a product of maximal ideals**. The property $B$ is "$\dim_k V < \infty$" or "$\mathfrak{m}_1 \cdots \mathfrak{m}_n M = 0$". A finite-dimensional space has $\ell = \dim < \infty$ by the corollary; a module killed by a product of maximal ideals has a finite filtration with vector-space quotients, hence finite length. The non-obviousness is that an annihilator condition produces finite length via a filtration. *Example problem:* if $\mathfrak{m}_1 \cdots \mathfrak{m}_n = 0$ in $R$, then $R$ has finite length, so Noetherian $\iff$ Artinian for $R$ (ES2 Q1e).

The third disguised source is **a module sitting in a short exact sequence with finite-length ends**. The property $B$ is "$0 \to N \to M \to L \to 0$ with $\ell(N), \ell(L) < \infty$". By part 1 plus [[Thm - Chain Conditions Pass Through Short Exact Sequences|two-out-of-three]], $M$ has finite length too, and additivity computes it. The non-obviousness is that finite length is built from the ends. *Example problem:* compute $\ell(M)$ for an extension of two known finite-length modules.

**Targets (Output Amplification)**

The conclusion is a length value or a length identity.

Combine additivity with **a composition series of $M$**. Each step of a composition series is a short exact sequence $0 \to M_{i+1} \to M_i \to M_i/M_{i+1} \to 0$ with simple quotient (length $1$), so additivity gives $\ell(M) = \sum_i \ell(M_i/M_{i+1})$, the number of steps. The further result $E$ is the **Jordan–Hölder invariance** itself — additivity forces all composition series to have the same length. This is non-obvious because additivity *proves* the well-definedness that the definition of length assumed.

Combine the alternating-sum form with **a free resolution or a chain complex**. For a finite resolution $0 \to F_n \to \cdots \to F_0 \to M \to 0$ with each $F_i$ of finite length, $\ell(M) = \sum_i (-1)^i \ell(F_i)$. The further result $E$ is the **Euler characteristic** as a length-theoretic invariant — computable from any resolution, independent of which one. This is non-obvious because it makes a derived quantity computable from finite data.

Combine the criterion with **the Artinian-iff-Noetherian-plus-product-of-maximals trick**. If $R$ has $\mathfrak{m}_1 \cdots \mathfrak{m}_n = 0$, the filtration $R \supseteq \mathfrak{m}_1 \supseteq \mathfrak{m}_1\mathfrak{m}_2 \supseteq \cdots \supseteq 0$ has each quotient a vector space over a residue field, so finite length is equivalent to all quotients being finite-dimensional, equivalent to $R$ Noetherian, equivalent to $R$ Artinian. The further result $E$ is **for such rings, Noetherian $\iff$ Artinian** — the bridge to the structure theory of Artinian rings. This is non-obvious because it makes the two normally-independent conditions coincide under the product-of-maximals hypothesis.

---

# Why Is It True

The two statements have different mechanisms; take them in turn.

**Why finite length $=$ Noetherian and Artinian.** The bolded mechanism: **a composition series is a chain that both starts at the top and reaches the bottom in finitely many simple steps; Noetherian ensures you can keep refining upward without an infinite ascent, Artinian ensures the refinement reaches $0$ in an infinite descent, and only together do they force a finite maximal chain.** Concretely, if $\ell(M) < \infty$ there is a finite composition series $M = M_0 \supsetneq \cdots \supsetneq M_n = 0$; any ascending chain of submodules can be refined into a chain whose length is bounded by $n$ (each simple quotient admits at most one insertion), so it stabilises — Noetherian; and dually for descending — Artinian. Conversely, if $M$ is both Noetherian and Artinian, build a composition series greedily: by the maximal condition (Noetherian) pick a maximal proper submodule $M_1 \subsetneq M$ (so $M/M_1$ is simple), then a maximal proper submodule $M_2 \subsetneq M_1$, and so on; the descending chain $M \supsetneq M_1 \supsetneq \cdots$ must terminate at $0$ because $M$ is Artinian. The two conditions are exactly the two ways the greedy construction could fail — failing to find a maximal proper submodule (no Noetherian) or never terminating (no Artinian) — so their conjunction is exactly finite length.

**Why length is additive.** The bolded mechanism: **the composition factors of $M$ are exactly the composition factors of the submodule $N$ together with the composition factors of the quotient $L$ — splice a composition series of $N$ below a composition series of $L$ (pulled back to $M$) to get a composition series of $M$.** Given $0 \to N \to M \to L \to 0$, take a composition series $N = N_0 \supsetneq \cdots \supsetneq N_a = 0$ of $N$ (length $\ell(N)$) and a composition series $L = L_0 \supsetneq \cdots \supsetneq L_b = 0$ of $L$ (length $\ell(L)$). Pull the latter back through $p : M \to L$ to a chain $M = p^{-1}(L_0) \supsetneq p^{-1}(L_1) \supsetneq \cdots \supsetneq p^{-1}(L_b) = N$ in $M$ with simple quotients (since $p^{-1}(L_j)/p^{-1}(L_{j+1}) \cong L_j/L_{j+1}$ is simple). Concatenate with the composition series of $N$ sitting below $p^{-1}(L_b) = N$:
$$M = p^{-1}(L_0) \supsetneq \cdots \supsetneq p^{-1}(L_b) = N = N_0 \supsetneq \cdots \supsetneq N_a = 0.$$
This is a composition series of $M$ with $b + a$ simple factors, so $\ell(M) = \ell(L) + \ell(N)$. The composition factors literally partition into the $L$-factors (top) and the $N$-factors (bottom). The alternating sum is this additivity telescoped: split $0 \to M_0 \to \cdots \to M_n \to 0$ at each map into short exact sequences via the images $Z_i = \operatorname{im}(M_{i-1} \to M_i) = \ker(M_i \to M_{i+1})$, apply additivity to each $0 \to Z_i \to M_i \to Z_{i+1} \to 0$, and add with alternating signs; every $\ell(Z_i)$ appears twice with opposite signs and cancels, leaving $\sum (-1)^i \ell(M_i) = 0$.

The corollary is the special case where every simple module is $k$ (a one-dimensional space), so the number of composition factors equals the dimension; additivity of length becomes additivity of dimension, i.e. rank–nullity.

---

# What Makes This Hard

The non-obvious construction is the **splicing** in additivity: you must pull a composition series of the quotient $L$ back through $p$ to a chain in $M$ ending at $N$, then stack a composition series of $N$ below it, and verify the spliced chain still has simple quotients. The common error is to think the factors of $M$ are some mixture of those of $N$ and $L$ — they are exactly the disjoint union, but only because the pullback preserves simplicity of quotients ($p^{-1}(L_j)/p^{-1}(L_{j+1}) \cong L_j/L_{j+1}$). For the finiteness criterion, the subtle point is that you need *both* chain conditions to build the composition series: Noetherian to keep finding maximal proper submodules (simple quotients), Artinian to guarantee termination at $0$. Dropping either gives a module with no finite composition series, and the standard errors are exhibited by $\mathbb{Z}$ (Noetherian, $\ell = \infty$) and $\mathbb{Z}[\tfrac12]/\mathbb{Z}$ (Artinian, $\ell = \infty$).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** For the criterion, show a finite composition series bounds all chains (giving both conditions), and conversely build a composition series greedily using the maximal condition (Noetherian) and termination (Artinian). For additivity, splice a composition series of $N$ below the pullback of a composition series of $L$. For the alternating sum, split the long sequence into short ones and telescope.

**Subgoal decomposition:**

1. **Finite length $\Rightarrow$ Noetherian and Artinian.** Show $\ell(M) < \infty$ bounds the length of every chain.
   - *Hint:* Any chain refines to a composition series, whose length is the fixed $\ell(M)$; so chains have bounded length and stabilise.
   - *Why needed:* It is one direction of the criterion.

2. **Noetherian and Artinian $\Rightarrow$ finite length.** Build a composition series greedily.
   - *Hint:* Use the maximal condition (Noetherian) to pick a maximal proper submodule at each step (simple quotient); use Artinian to force the descending chain to reach $0$.
   - *Why needed:* It is the other direction; both conditions are essential.

3. **Additivity via splicing.** Show $\ell(M) = \ell(N) + \ell(L)$.
   - *Hint:* Pull a composition series of $L$ back through $p$ to a chain $M \supsetneq \cdots \supsetneq N$ with simple quotients, then append a composition series of $N$.
   - *Why needed:* It is the additive law that makes length computable.

4. **Alternating sum by telescoping.** Show $\sum (-1)^i \ell(M_i) = 0$.
   - *Hint:* Split at images $Z_i = \ker(M_i \to M_{i+1})$ into short exact sequences $0 \to Z_i \to M_i \to Z_{i+1} \to 0$; apply additivity and sum with signs so the $\ell(Z_i)$ cancel.
   - *Why needed:* It is the Euler-characteristic form, the basis for resolution computations.

---

# Lemma Decomposition

> [!note]- Lemma 1: A finite composition series bounds the length of every chain
> **Statement:** If $M$ has a composition series of length $n$, then every chain of submodules of $M$ has length $\leq n$, and can be refined to a composition series.
>
> **Hint:** Define $\ell(K)$ as the shortest composition-series length; show $\ell(N) < \ell(M)$ for every proper submodule $N \subsetneq M$, then induct.
>
> **Why needed:** It gives both chain conditions from finite length, and is the heart of Jordan–Hölder invariance.
>
> > [!note]- Full proof
> > Write $\ell(K)$ for the length of the shortest composition series of $K$ (when one exists). *Claim: if $N \subsetneq M$ properly, then $\ell(N) < \ell(M)$.* Given a composition series of $M$ of length $\ell(M)$, intersect it with $N$: the chain $N \cap M_i$ has successive quotients $(N \cap M_i)/(N \cap M_{i+1})$ embedding into the simple $M_i/M_{i+1}$, hence each is $0$ or simple; deleting repeats gives a composition series of $N$ of length $\leq \ell(M)$, and it is $< \ell(M)$ because $N \neq M$ forces at least one quotient to collapse to $0$. So $\ell(N) < \ell(M)$. Now any strict chain $M = K_0 \supsetneq K_1 \supsetneq \cdots \supsetneq K_r = 0$ has $\ell(M) > \ell(K_1) > \cdots > \ell(K_r) = 0$, a strictly decreasing sequence of non-negative integers of length $r$, so $r \leq \ell(M)$. Hence every chain has length $\leq n = \ell(M)$ and refines to one of length exactly $n$ (a composition series). In particular all composition series have length $n$.

> [!note]- Lemma 2: Both chain conditions yield a composition series
> **Statement:** If $M$ is both Noetherian and Artinian, then $M$ has a (finite) composition series.
>
> **Hint:** Greedily pick maximal proper submodules using the Noetherian maximal condition; the resulting descending chain terminates because $M$ is Artinian.
>
> **Why needed:** It is the "$\Leftarrow$" of the finiteness criterion.
>
> > [!note]- Full proof
> > Construct a descending chain $M = M_0 \supsetneq M_1 \supsetneq \cdots$ as follows. Given $M_i \neq 0$, the set of proper submodules of $M_i$ is non-empty (it contains $0$), so by the maximal condition (Noetherian) it has a maximal element $M_{i+1}$; then $M_i/M_{i+1}$ is simple (a maximal proper submodule has simple quotient). This produces a strictly descending chain $M_0 \supsetneq M_1 \supsetneq \cdots$ with simple quotients. Since $M$ is Artinian, the descending chain must stabilise, which (being strict) means it terminates: $M_n = 0$ for some $n$. Then $M = M_0 \supsetneq \cdots \supsetneq M_n = 0$ is a composition series.

> [!note]- Lemma 3: Splicing composition series across a short exact sequence
> **Statement:** For $0 \to N \xrightarrow{i} M \xrightarrow{p} L \to 0$ with $N, L$ of finite length, $M$ has finite length and $\ell(M) = \ell(N) + \ell(L)$.
>
> **Hint:** Pull a composition series of $L$ back through $p$ to a chain from $M$ down to $N$ (preserving simple quotients), then stack a composition series of $N$ below it.
>
> **Why needed:** It is additivity (part 2), and gives part 3 by telescoping.
>
> > [!note]- Full proof
> > Identify $N$ with $i(N) \subseteq M$, so $L = M/N$ and $p$ is the quotient map. Take a composition series $L = L_0 \supsetneq L_1 \supsetneq \cdots \supsetneq L_b = 0$ of $L$ (length $b = \ell(L)$). Its preimages $p^{-1}(L_j)$ give a chain $M = p^{-1}(L_0) \supsetneq \cdots \supsetneq p^{-1}(L_b) = N$, with quotients $p^{-1}(L_j)/p^{-1}(L_{j+1}) \cong L_j/L_{j+1}$ simple (the correspondence theorem). Append a composition series $N = N_0 \supsetneq \cdots \supsetneq N_a = 0$ of $N$ (length $a = \ell(N)$). The concatenation
> > $$M = p^{-1}(L_0) \supsetneq \cdots \supsetneq p^{-1}(L_b) = N = N_0 \supsetneq \cdots \supsetneq N_a = 0$$
> > is a composition series of $M$ with $a + b$ simple factors. Hence $\ell(M) = a + b = \ell(N) + \ell(L)$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Part 1 — finiteness criterion.**
>
> ($\Rightarrow$) Suppose $\ell(M) = n < \infty$. By Lemma 1, every chain of submodules of $M$ has length $\leq n$. In particular no infinite strictly ascending or strictly descending chain exists, so $M$ is both Noetherian and Artinian.
>
> ($\Leftarrow$) Suppose $M$ is both Noetherian and Artinian. By Lemma 2, $M$ has a finite composition series, so $\ell(M) < \infty$.
>
> ---
> **Part 2 — additivity.** This is Lemma 3: for $0 \to N \to M \to L \to 0$ with $N, L$ finite length, $\ell(M) = \ell(N) + \ell(L)$ (and $M$ has finite length).
>
> ---
> **Part 3 — alternating sum.** Let $0 \to M_0 \xrightarrow{d_0} M_1 \xrightarrow{d_1} \cdots \xrightarrow{d_{n-1}} M_n \to 0$ be exact, all $M_i$ of finite length. Set $Z_i = \operatorname{im}(d_{i-1}) = \ker(d_i) \subseteq M_i$ (with $Z_0 = 0$ and $Z_{n+1} = 0$ by exactness at the ends). Exactness gives short exact sequences
> $$0 \to Z_i \to M_i \to Z_{i+1} \to 0 \qquad (0 \leq i \leq n),$$
> since $\operatorname{im}(M_i \to M_{i+1}) = Z_{i+1}$ and $\ker(M_i \to M_{i+1}) = Z_i$. By Part 2, each $Z_i$ has finite length and $\ell(M_i) = \ell(Z_i) + \ell(Z_{i+1})$. Therefore
> $$\sum_{i=0}^n (-1)^i \ell(M_i) = \sum_{i=0}^n (-1)^i \big(\ell(Z_i) + \ell(Z_{i+1})\big).$$
> In this sum every $\ell(Z_j)$ appears once as $(-1)^j \ell(Z_j)$ (from the $i = j$ term's $\ell(Z_i)$) and once as $(-1)^{j-1} \ell(Z_j)$ (from the $i = j-1$ term's $\ell(Z_{i+1})$); these cancel. With $Z_0 = Z_{n+1} = 0$ all boundary terms vanish, so the total is $0$.
>
> ---
> **Corollary.** For a $k$-vector space $V$: a composition series is a maximal flag with one-dimensional quotients, so $\ell(V) = \dim_k V$ when finite. Then $\dim_k V < \infty \iff \ell(V) < \infty \iff V$ Noetherian and Artinian (Part 1); and an infinite-dimensional $V$ fails both chain conditions (exhibit an infinite ascending/descending flag), so each of the four conditions is equivalent. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Rank–nullity as additivity of length.** For a linear map $f : V \to W$ of finite-dimensional vector spaces, the sequence $0 \to \ker f \to V \to \operatorname{im} f \to 0$ is short exact, and additivity of length gives $\dim V = \dim \ker f + \dim \operatorname{im} f$ — rank–nullity. The application is non-obvious because the familiar dimension formula is *exactly* length-additivity specialised to the field case; recognising this places rank–nullity inside a much more general additivity.

**Euler characteristics of chain complexes.** For a bounded chain complex of finite-length modules, the alternating sum of lengths equals the alternating sum of the lengths of the homology modules — the **Euler characteristic** is computable either from the complex or from its homology. The application is non-obvious because it is the algebraic core of why topological Euler characteristics $\sum (-1)^i \dim H_i$ are homotopy invariants: the alternating sum is unchanged by passing to homology.

**Multiplicity and Bézout's theorem.** For two plane curves meeting at a point $x$, the intersection multiplicity is $\ell(\mathcal{O}_{x}/(f, g))$, and additivity of length over the points of intersection yields Bézout's count $\sum_x \ell = \deg f \cdot \deg g$. The application is non-obvious because it turns a geometric counting problem into additivity of an algebraic length invariant, the foundation of intersection theory.

---

# Bridges

- **[[Def - Composition Series and Length|Composition series and length]]** — the definition this theorem makes well-founded and useful. Length is *defined* via composition series assuming Jordan–Hölder invariance; Lemma 1 here *proves* that invariance (all composition series have the same length), and additivity (Lemma 3) gives the computational law. This theorem is what turns the definition into a working invariant.

- **[[Thm - Chain Conditions Pass Through Short Exact Sequences|Two-out-of-three for chain conditions]]** — the qualitative companion to additivity. That lemma says finite length is two-out-of-three (preserved along short exact sequences); this theorem sharpens it to the *quantitative* statement $\ell(M) = \ell(N) + \ell(L)$. The composition factors of $M$ being the disjoint union of those of $N$ and $L$ is the refinement of "finite length is conserved".

- **[[Ex - Composition length is additive on exact sequences|Additivity of any additive invariant]]** — the generalisation. The alternating-sum argument uses nothing about length except additivity on short exact sequences; the same telescoping holds for *any* additive integer-valued invariant $\lambda$, giving $\sum (-1)^i \lambda(M_i) = 0$. This is the abstract content (ES1 Q12, ES2 Q1c) and the seed of the Grothendieck group.

- **Hilbert–Samuel functions and dimension theory** — the downstream quantitative theory. For a Noetherian local ring, the lengths $\ell(R/\mathfrak{m}^n)$ are governed by a polynomial (the Hilbert–Samuel polynomial) whose degree is the Krull dimension. Length is the raw counting invariant; dimension theory ([[Commutative Algebra XII — Dimension Theory]]) is built by studying how it grows.

---

# Unlocked by This

> [!tip] The Grothendieck group $K_0$ *(from Homological Algebra and K-theory)*
> Additivity on short exact sequences is the defining relation of the **Grothendieck group** $K_0(\mathcal{A})$ of an abelian category: the universal abelian group receiving an additive invariant, $[M] = [N] + [L]$ for every short exact sequence. Length is the homomorphism $K_0(\text{finite-length modules}) \to \mathbb{Z}$ sending each simple to $1$. Every additive invariant — rank, dimension, Euler characteristic, Chern character — factors through $K_0$, which is the organising object of algebraic K-theory.

> [!tip] Euler characteristics and the Hilbert polynomial *(from Algebraic Geometry)*
> The alternating-sum identity is the algebraic prototype of the **Euler characteristic** $\chi(\mathcal{F}) = \sum (-1)^i \dim H^i(X, \mathcal{F})$ of a coherent sheaf, which is additive on short exact sequences for exactly this reason. The Hilbert polynomial of a projective variety, the Riemann–Roch theorem, and the computation of cohomology from resolutions all rest on additivity of these length-like Euler characteristics. This is developed through the dimension theory of Commutative Algebra XII.

> [!tip] Multiplicity in intersection theory *(from Algebraic Geometry)*
> Length is the local **multiplicity**: $\ell(\mathcal{O}_{X,x}/I)$ counts the order of contact at a point, and additivity of length spreads a global degree over local contributions — the mechanism of Bézout's theorem and of intersection numbers on surfaces. Intersection theory is, at its arithmetic core, additivity of length applied point by point.
