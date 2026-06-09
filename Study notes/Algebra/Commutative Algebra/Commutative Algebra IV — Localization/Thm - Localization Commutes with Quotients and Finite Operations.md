---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Quotient Module"
  - "Def - Tensor Product of Modules"
  - "Def - Exact Sequence and Short Exact Sequence"
  - "Def - Multiplicative Set and Localization"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $S \subseteq R$ be a [[Def - Multiplicative Set and Localization|multiplicative subset]], $M$ an [[Def - Module|$R$-module]], and $N, P \subseteq M$ [[Def - Submodule|submodules]]. We write $N + P$ for the submodule of sums $n + p$, $N \cap P$ for the intersection, $M/N$ for the [[Def - Quotient Module|quotient]], and $\otimes_R$, $\otimes_{S^{-1}R}$ for [[Def - Tensor Product of Modules|tensor products]]. We treat $S^{-1}N$ as an $S^{-1}R$-submodule of $S^{-1}M$ (legitimate by exactness of localization, [[Thm - Localization is Exact and the Localization is Flat]]). For a prime $\mathfrak{p}$, $M_{\mathfrak{p}} = (R\setminus\mathfrak{p})^{-1}M$. The full registry is on [[Commutative Algebra IV — Localization]].

---

# Statement

> **Theorem (Localization commutes with finite operations; Becker Prop. 4.14, 4.15).** Let $N, P$ be submodules of an $R$-module $M$, and $M_1, M_2$ any $R$-modules. Then, as $S^{-1}R$-modules:
> 1. **(Sums.)** $S^{-1}(N + P) = S^{-1}N + S^{-1}P$.
> 2. **(Intersections.)** $S^{-1}(N \cap P) = S^{-1}N \cap S^{-1}P$.
> 3. **(Quotients.)** $S^{-1}M / S^{-1}N \;\xrightarrow{\ \sim\ }\; S^{-1}(M/N)$, via $\tfrac ms + S^{-1}N \mapsto \tfrac{m + N}{s}$.
> 4. **(Tensor products, Prop. 4.15.)** $S^{-1}M_1 \otimes_{S^{-1}R} S^{-1}M_2 \;\xrightarrow{\ \sim\ }\; S^{-1}(M_1 \otimes_R M_2)$, via $\tfrac{m_1}{s_1} \otimes \tfrac{m_2}{s_2} \mapsto \tfrac{m_1 \otimes m_2}{s_1 s_2}$.

> **Corollary (prime case).** For a prime $\mathfrak{p}$: $(M_1 \otimes_R M_2)_{\mathfrak{p}} \cong (M_1)_{\mathfrak{p}} \otimes_{R_{\mathfrak{p}}} (M_2)_{\mathfrak{p}}$, and $R_{\mathfrak{p}}/\mathfrak{q}R_{\mathfrak{p}} \cong (R/\mathfrak{q})_{\mathfrak{p}}$ for $\mathfrak{q} \subseteq \mathfrak{p}$; at $\mathfrak{q} = \mathfrak{p}$ this is the residue field $\kappa(\mathfrak{p})$.

---

# Motivation

This theorem is the licence to *push $S^{-1}$ through any finite module construction*. You build modules out of a small toolkit — sums, intersections, quotients, tensor products — and the natural question is whether localizing the built object equals building from the localized pieces. The answer, uniformly, is yes: localization is *transparent* to these operations. That transparency is what makes localization usable as a routine simplification rather than a delicate special case.

The reason it matters is bookkeeping at scale. Almost every computation in the chapter involves a module assembled from others — a quotient $M/N$, an intersection of two submodules, a tensor $M\otimes N$ — and you want to localize the whole thing, often at every prime, to apply a local argument. If localization did not commute with the construction, you would have to recompute the localized object from its fraction definition each time. Because it does commute, you localize the *pieces*, which are usually simpler, and reassemble. The quotient identity (part 3) is the most heavily used: it is the engine behind "localization commutes with $R/\mathfrak{q}$", which produces the residue field $\kappa(\mathfrak{p})$ and reconciles $R_{\mathfrak{p}}$ with $R/\mathfrak{p}$.

The unifying observation is that *every part of this theorem is a corollary of exactness*. Sums and quotients are right-exact constructions, intersections come from a pullback square, tensor products are right-exact and commute with base change. Since localization is an [[Thm - Localization is Exact and the Localization is Flat|exact, flat functor]], it commutes with all of them. So the theorem is not a list of independent facts to memorise but a single principle — *exactness propagates through finite constructions* — instantiated four times. The word "finite" is essential: localization commutes with *finite* sums and intersections, not infinite ones, because the clearing-denominator arguments need a common denominator, which only exists for finitely many fractions.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is *a module built by a finite operation (sum, intersection, quotient, tensor) that you want to localize*.

The first disguised source is **a quotient appears and you want to evaluate or localize it**. Property $B$: an object $M/N$ or $R/\mathfrak{q}$ is present. The bridge is part 3: localize numerator and the relation separately. The non-obvious value: it lets you compute residue fields and reduce mod a prime *after* localizing. *Example problem:* compute $\kappa(\mathfrak{p}) = R_{\mathfrak{p}}/\mathfrak{p}R_{\mathfrak{p}}$ as $(R/\mathfrak{p})_{\mathfrak{p}} = \operatorname{Frac}(R/\mathfrak{p})$ — see [[Ex - Localization commutes with quotients]].

The second disguised source is **a tensor product over $R$ that you wish to localize, or a module over a localization built from localized factors**. Property $B$: a tensor $M_1\otimes_R M_2$ or a base-changed module. The bridge is part 4: localization passes through tensor, with the denominators multiplying. The non-obvious part: this needs *flatness*, not merely right-exactness, to be a clean isomorphism. *Example problem:* showing $(M\otimes_R N)_{\mathfrak{p}} \cong M_{\mathfrak{p}}\otimes_{R_{\mathfrak{p}}} N_{\mathfrak{p}}$ to reduce a tensor computation to a local ring.

The third disguised source is **an intersection or sum of ideals/submodules**. Property $B$: $N\cap P$ or $N+P$ appears, often as ideals $\mathfrak{a}\cap\mathfrak{b}$. The bridge is parts 1–2. The non-obvious subtlety: the intersection identity requires the *finiteness* and a clearing-denominator argument (it can fail for infinite intersections). *Example problem:* localizing a primary decomposition's intersection of primary ideals one prime at a time.

**Targets (Output Amplification)**

The conclusion is *localization commutes with the finite operation*.

Combine part 3 with **a chain of primes $\mathfrak{q}\subseteq\mathfrak{p}$**. The isomorphism $R_{\mathfrak{p}}/\mathfrak{q}R_{\mathfrak{p}} \cong (R/\mathfrak{q})_{\mathfrak{p}}$ identifies "localize then quotient" with "quotient then localize". The further result $E$: the local ring of a point on a subvariety is computed either way, and at $\mathfrak{q} = \mathfrak{p}$ you get the residue field. Nonobvious because the two operations look opposite ($R_{\mathfrak{p}}$ keeps primes $\subseteq\mathfrak{p}$, $R/\mathfrak{q}$ keeps primes $\supseteq\mathfrak{q}$) yet commute.

Combine part 4 with **$\otimes$ with a residue field**. Localizing then tensoring with $\kappa(\mathfrak{p})$ computes the "fibre" $M\otimes_R\kappa(\mathfrak{p})$, the vector space of $M$ at the point $\mathfrak{p}$. The further result $E$: the function $\mathfrak{p}\mapsto \dim_{\kappa(\mathfrak{p})}(M\otimes\kappa(\mathfrak{p}))$ measures the fibre dimension of $M$ — constant for locally free $M$, the rank of a vector bundle. Nonobvious because it turns a module into a family of vector spaces over $\operatorname{Spec} R$.

Combine parts 1–2 with **the lattice of ideals**. Localization is a lattice homomorphism on the finite sublattice generated by some ideals (preserves $+$ and $\cap$). The further result $E$: ideal-theoretic identities (coprimality, primary decomposition pieces) localize term by term. Nonobvious because order-preservation is automatic but *meet*-preservation ($\cap$) is the content.

---

# Why Is It True

Each identity is "localize the relevant exact sequence". Take quotients (part 3): the defining short exact sequence is $0\to N\to M\to M/N\to 0$. Apply the [[Thm - Localization is Exact and the Localization is Flat|exact functor]] $S^{-1}(-)$ and it stays exact: $0\to S^{-1}N\to S^{-1}M\to S^{-1}(M/N)\to 0$. Exactness says $S^{-1}(M/N)$ is the cokernel of $S^{-1}N\hookrightarrow S^{-1}M$, which is by definition $S^{-1}M/S^{-1}N$. The isomorphism is automatic — *the quotient survives localization because localization preserves the exact sequence that defines the quotient*.

**One-line mechanism: every finite module construction is the (co)kernel of a map; localization is exact, so it commutes with taking (co)kernels, hence with the construction.**

Sums and intersections are fraction-level computations, and the only subtlety is the intersection. The sum is trivial: an element of $S^{-1}(N+P)$ is $\tfrac{n+p}{s}$, an element of $S^{-1}N + S^{-1}P$ is $\tfrac{n}{s_1}+\tfrac{p}{s_2}$, and these describe the same set. The intersection is where you must work: if $\tfrac{n}{s_1} = \tfrac{p}{s_2}$ lies in both $S^{-1}N$ and $S^{-1}P$, the fractions are equal in $S^{-1}M$, so some $u\in S$ gives $u(s_2 n - s_1 p) = 0$, whence $w := u s_2 n = u s_1 p$ lies in *both* $N$ and $P$ (the same element, written two ways), so $w\in N\cap P$ and the original fraction is $\tfrac{w}{us_1 s_2}\in S^{-1}(N\cap P)$. **The clearing factor $u$ is what forces the two representatives to become a single honest element of $N\cap P$** — this is why a common denominator (hence finiteness) is essential.

The tensor identity (part 4) is base-change algebra: using $S^{-1}M_i \cong S^{-1}R\otimes_R M_i$, one computes
$$(S^{-1}R\otimes_R M_1)\otimes_{S^{-1}R}(S^{-1}R\otimes_R M_2) \cong S^{-1}R\otimes_R(M_1\otimes_R M_2) \cong S^{-1}(M_1\otimes_R M_2),$$
the middle isomorphism being the standard fact that base change commutes with tensor product. So part 4 is "localization is base change, and base change is monoidal".

---

# What Makes This Hard

The only genuinely tricky part is the *intersection* (part 2): seeing that two equal fractions $\tfrac{n}{s_1} = \tfrac{p}{s_2}$ produce a *single* element $w = us_2 n = us_1 p$ lying in $N\cap P$, where the clearing factor $u$ is what merges the two representatives. People stuck here forget to use the localization equivalence relation to extract $u$. The conceptual point easily missed is *why finiteness is needed*: the arguments rely on a common denominator, which exists for two (or finitely many) submodules but not for infinitely many, so the theorem genuinely fails for infinite intersections. For part 4, the subtle ingredient is that the clean isomorphism needs *flatness*, not merely the right-exactness of tensor.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Prove quotients by localizing the defining short exact sequence and reading off the cokernel. Prove sums and intersections at the fraction level, using a clearing factor for the intersection. Prove tensors by the base-change calculation through $S^{-1}M_i \cong S^{-1}R\otimes_R M_i$.

**Subgoal decomposition:**

1. **Quotients.** Show $S^{-1}(M/N) \cong S^{-1}M/S^{-1}N$.
   - *Hint:* apply the exact functor to $0\to N\to M\to M/N\to 0$; the localized sequence's cokernel is both sides.
   - *Why needed:* the most-used identity; gives residue fields.

2. **Sums and intersections.** Show $S^{-1}(N+P) = S^{-1}N+S^{-1}P$ and $S^{-1}(N\cap P) = S^{-1}N\cap S^{-1}P$.
   - *Hint:* sums are immediate from the fraction descriptions; for $\cap$, equal fractions give a clearing factor $u$, and $w = us_2 n = us_1 p \in N\cap P$.
   - *Why needed:* makes localization a lattice map; needed for ideal computations.

3. **Tensors.** Show $S^{-1}M_1\otimes_{S^{-1}R}S^{-1}M_2 \cong S^{-1}(M_1\otimes_R M_2)$.
   - *Hint:* substitute $S^{-1}M_i = S^{-1}R\otimes_R M_i$ and use that base change commutes with tensor.
   - *Why needed:* needed to reduce tensor computations to local rings and to define fibres.

---

# Lemma Decomposition

> [!note]- Lemma 1: Quotients via the localized exact sequence
> **Statement:** $S^{-1}(M/N) \cong S^{-1}M/S^{-1}N$ as $S^{-1}R$-modules, by $\tfrac ms + S^{-1}N\mapsto\tfrac{m+N}{s}$.
>
> **Hint:** Localize $0\to N\to M\to M/N\to 0$ and identify the cokernel.
>
> **Why needed:** It is part 3 and the source of $R_{\mathfrak{p}}/\mathfrak{q}R_{\mathfrak{p}}\cong(R/\mathfrak{q})_{\mathfrak{p}}$ and the residue field.
>
> > [!note]- Full proof
> > Apply the exact functor $S^{-1}(-)$ ([[Thm - Localization is Exact and the Localization is Flat]]) to the short exact sequence $0\to N\xrightarrow{\iota} M\xrightarrow{\pi} M/N\to 0$, obtaining the exact sequence $0\to S^{-1}N\xrightarrow{S^{-1}\iota} S^{-1}M\xrightarrow{S^{-1}\pi} S^{-1}(M/N)\to 0$. Here $S^{-1}\iota$ realises $S^{-1}N$ as a submodule of $S^{-1}M$, and $S^{-1}\pi$ sends $\tfrac ms\mapsto\tfrac{m+N}{s}$. Exactness says $S^{-1}\pi$ is surjective with kernel exactly $S^{-1}N$, so by the first isomorphism theorem $S^{-1}M/S^{-1}N \cong S^{-1}(M/N)$ via $\tfrac ms + S^{-1}N\mapsto\tfrac{m+N}{s}$.

> [!note]- Lemma 2: The intersection identity via a clearing factor
> **Statement:** $S^{-1}(N\cap P) = S^{-1}N\cap S^{-1}P$.
>
> **Hint:** An element of the right side is $\tfrac{n}{s_1}=\tfrac{p}{s_2}$; the equality yields $u\in S$ with $us_2 n = us_1 p \in N\cap P$.
>
> **Why needed:** It is the one non-formal part, and shows why finiteness is essential.
>
> > [!note]- Full proof
> > The inclusion $\subseteq$ is clear ($N\cap P\subseteq N$ and $\subseteq P$). For $\supseteq$, take $x\in S^{-1}N\cap S^{-1}P$, so $x = \tfrac{n}{s_1} = \tfrac{p}{s_2}$ with $n\in N$, $p\in P$, $s_1,s_2\in S$. Since the fractions are equal in $S^{-1}M$, there is $u\in S$ with $u(s_2 n - s_1 p) = 0$, i.e.
> > $$w := u s_2 n = u s_1 p.$$
> > Now $w = us_2 n \in N$ (a multiple of $n\in N$) and $w = us_1 p \in P$ (a multiple of $p\in P$), so $w\in N\cap P$. Finally $x = \tfrac{n}{s_1} = \tfrac{w}{us_1 s_2}\in S^{-1}(N\cap P)$. Hence $\supseteq$ holds and the two sides are equal.

> [!note]- Lemma 3: The tensor identity via base change
> **Statement:** $S^{-1}M_1\otimes_{S^{-1}R}S^{-1}M_2 \cong S^{-1}(M_1\otimes_R M_2)$, by $\tfrac{m_1}{s_1}\otimes\tfrac{m_2}{s_2}\mapsto\tfrac{m_1\otimes m_2}{s_1 s_2}$.
>
> **Hint:** Replace each $S^{-1}M_i$ by $S^{-1}R\otimes_R M_i$ and apply the associativity/base-change isomorphism for tensor products.
>
> **Why needed:** It is part 4, and gives the prime-case corollary and the fibre construction.
>
> > [!note]- Full proof
> > Using the natural isomorphism $S^{-1}M_i\cong S^{-1}R\otimes_R M_i$,
> > $$S^{-1}M_1\otimes_{S^{-1}R}S^{-1}M_2 \cong (S^{-1}R\otimes_R M_1)\otimes_{S^{-1}R}(S^{-1}R\otimes_R M_2).$$
> > By the standard base-change isomorphism (the "cancellation" $(B\otimes_A M_1)\otimes_B(B\otimes_A M_2)\cong B\otimes_A(M_1\otimes_A M_2)$ with $A = R$, $B = S^{-1}R$), the right side is $S^{-1}R\otimes_R(M_1\otimes_R M_2)\cong S^{-1}(M_1\otimes_R M_2)$. Tracking $\tfrac{r_1}{s_1}\otimes m_1$ and $\tfrac{r_2}{s_2}\otimes m_2$ through these isomorphisms sends $\tfrac{m_1}{s_1}\otimes\tfrac{m_2}{s_2}\mapsto\tfrac{m_1\otimes m_2}{s_1 s_2}$ as claimed.

---

# Formal Proof

> [!note]- Complete formal proof
> **Part 1 (sums).** The left side $S^{-1}(N+P)$ consists of all $\tfrac{n+p}{s}$ with $n\in N$, $p\in P$, $s\in S$; the right side $S^{-1}N+S^{-1}P$ consists of all $\tfrac{n}{s_1}+\tfrac{p}{s_2} = \tfrac{s_2 n + s_1 p}{s_1 s_2}$. Both equal the set of fractions whose numerator is a sum of an element of $N$ and an element of $P$ (clearing to a common denominator in one direction, splitting in the other), so the two submodules of $S^{-1}M$ coincide.
>
> **Part 2 (intersections).** This is Lemma 2.
>
> **Part 3 (quotients).** This is Lemma 1.
>
> **Part 4 (tensors).** This is Lemma 3.
>
> **Corollary (prime case).** Taking $S = R\setminus\mathfrak{p}$ in Part 4 gives $(M_1\otimes_R M_2)_{\mathfrak{p}}\cong (M_1)_{\mathfrak{p}}\otimes_{R_{\mathfrak{p}}}(M_2)_{\mathfrak{p}}$. Taking $M = R$, $N = \mathfrak{q}$ in Part 3 gives $R_{\mathfrak{p}}/\mathfrak{q}R_{\mathfrak{p}} = R_{\mathfrak{p}}/S^{-1}\mathfrak{q} \cong (R/\mathfrak{q})_{\mathfrak{p}}$; at $\mathfrak{q} = \mathfrak{p}$, the right side is $(R/\mathfrak{p})_{\mathfrak{p}} = \operatorname{Frac}(R/\mathfrak{p}) = \kappa(\mathfrak{p})$ (since $R/\mathfrak{p}$ is a domain and localizing a domain at $(0) = \mathfrak{p}/\mathfrak{p}$ gives its fraction field). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Fibres of a module as a family of vector spaces.** For a finitely generated $M$ over $R$, the assignment $\mathfrak{p}\mapsto M\otimes_R\kappa(\mathfrak{p}) = M_{\mathfrak{p}}/\mathfrak{p}M_{\mathfrak{p}}$ is the fibre of $M$ at the point $\mathfrak{p}$, a vector space over the residue field, and part 4 (tensor) plus part 3 (quotient) compute it. Its dimension is the rank of $M$ at $\mathfrak{p}$; constancy of this rank is local freeness. Nonobvious because it views a single module as a varying family of vector spaces — the algebraic skeleton of a vector bundle.

**Residue fields of number rings.** For the ring of integers $\mathcal{O}_K$ of a number field and a prime $\mathfrak{p}$, the residue field $\kappa(\mathfrak{p}) = \mathcal{O}_K/\mathfrak{p}$ is a finite field (since $\mathfrak{p}$ is maximal), and part 3 lets you compute it as $(\mathcal{O}_K)_{\mathfrak{p}}/\mathfrak{p}(\mathcal{O}_K)_{\mathfrak{p}}$. The residue degree $f = [\kappa(\mathfrak{p}):\mathbb{F}_p]$ governs splitting of primes. Nonobvious because the local computation and the global quotient agree, which is what makes residue degrees well-defined.

**Stalkwise tensor in sheaf theory.** For sheaves of modules $\mathcal{F},\mathcal{G}$, the stalk of $\mathcal{F}\otimes\mathcal{G}$ at a point is the tensor of stalks: $(\mathcal{F}\otimes\mathcal{G})_x \cong \mathcal{F}_x\otimes_{\mathcal{O}_x}\mathcal{G}_x$, which is exactly part 4 for the localizations $\mathcal{F}_x = M_{\mathfrak{p}}$. This makes tensoring of sheaves computable pointwise. Nonobvious because it requires the base-change form of the tensor identity proved here.

---

# Bridges

- **[[Thm - Localization is Exact and the Localization is Flat|Exactness and flatness of localization]]** — the parent theorem. Parts 1–3 are direct consequences of exactness (localize the defining (co)kernel sequence), and part 4 is a consequence of flatness (base change commutes with tensor). This theorem is "exactness, applied to the four basic constructions".

- **[[Def - Local Ring and Residue Field|Residue field]]** — part 3 is what makes $\kappa(\mathfrak{p}) = R_{\mathfrak{p}}/\mathfrak{p}R_{\mathfrak{p}} = \operatorname{Frac}(R/\mathfrak{p})$ a *theorem* rather than two definitions: localization commuting with the quotient by $\mathfrak{p}$ reconciles "localize then quotient" with "quotient then take fractions".

- **[[Thm - Prime Ideals of a Localization|Prime ideals of a localization]]** — part 3 gives $R_{\mathfrak{p}}/\mathfrak{q}R_{\mathfrak{p}}\cong(R/\mathfrak{q})_{\mathfrak{p}}$, which shows the primes between $\mathfrak{q}$ and $\mathfrak{p}$ are tracked correctly under both operations, complementing the prime-correspondence theorem.

- **[[Thm - The Local-Global Principle|The local–global principle]]** — the quotient identity $(\ker g/\operatorname{im} f)_{\mathfrak{m}}\cong(\ker g)_{\mathfrak{m}}/(\operatorname{im} f)_{\mathfrak{m}}$ is used inside the proof that *exactness is a local property*: it lets the "homology" $\ker g/\operatorname{im} f$ be localized and tested for vanishing prime by prime.

---

# Unlocked by This

> [!tip] Fibres of a coherent sheaf and the rank of a vector bundle *(from Algebraic Geometry)*
> The fibre $M\otimes_R\kappa(\mathfrak{p})$, computable by the quotient and tensor identities here, is the value of the **coherent sheaf** $\widetilde{M}$ at the point $\mathfrak{p}$ — a vector space over the residue field. Its dimension $\dim_{\kappa(\mathfrak{p})}(M\otimes\kappa(\mathfrak{p}))$ is the rank of $M$ at $\mathfrak{p}$, upper-semicontinuous in general and *locally constant* exactly when $M$ is locally free, i.e. a vector bundle. The jump locus where the rank increases is the support of a torsion/singular part — the algebraic origin of how a sheaf degenerates, central to the theory of coherent sheaves and their stratifications.

> [!tip] Base change and the projection formula *(from Algebraic Geometry)*
> Part 4 is the affine-local case of the **base-change** isomorphism $f^*(\mathcal{F}\otimes\mathcal{G}) \cong f^*\mathcal{F}\otimes f^*\mathcal{G}$ for a morphism $f$, and feeds the **projection formula** $f_*(\mathcal{F}\otimes f^*\mathcal{G})\cong f_*\mathcal{F}\otimes\mathcal{G}$. These compatibilities of pullback and pushforward with tensor are what make the six-functor formalism and intersection theory function, and they all rest on localization commuting with tensor — the local model proved on this page.
