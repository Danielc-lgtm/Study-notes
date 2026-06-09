---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Module"
  - "Def - Finitely Generated Module"
  - "Def - Free Module"
  - "Def - Noetherian and Artinian Module"
  - "Def - Noetherian Ring"
  - "Thm - Chain Conditions Pass Through Short Exact Sequences"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$; modules are unital. Let $R$ be a ring, regarded as a module over itself (its submodules are its [[Def - Ideal|ideals]]). We write $R^{\oplus \ell} = R \oplus \cdots \oplus R$ ($\ell$ copies) for the [[Def - Free Module|free module]] of rank $\ell$. A ring is **[[Def - Noetherian Ring|Noetherian]]** if it satisfies the ascending chain condition on ideals, equivalently if it is a [[Def - Noetherian and Artinian Module|Noetherian module]] over itself; a module is **[[Def - Finitely Generated Module|finitely generated]]** if $M = Rm_1 + \cdots + Rm_k$ for finitely many $m_i$. The full registry is on [[Commutative Algebra I — Chain Conditions]].

---

# Statement

> **Theorem.** Let $R$ be a Noetherian (resp. Artinian) ring and $M$ a finitely generated $R$-module. Then $M$ is a Noetherian (resp. Artinian) module.

> **Corollary.** A ring $R$ is Noetherian if and only if every submodule of every finitely generated $R$-module is finitely generated.

The corollary records the slogan: over a Noetherian ring, *finite generation is hereditary across all finitely generated modules*. (The "only if" is the theorem combined with [[Thm - Noetherian iff Every Submodule is Finitely Generated|Noetherian ⟺ every submodule finitely generated]]; the "if" is the special case $M = R$, where submodules are ideals.)

---

# Motivation

This theorem is the payoff of the chapter's machinery and the reason the chain condition was lifted from rings to modules in the first place. On its own, the hypothesis "$R$ is Noetherian" is a statement about ideals — submodules of $R$. The conclusion extends that finiteness to *every* finitely generated module: not just $R$, but $R^{\oplus \ell}$, every quotient of it, and every submodule of every such quotient. So a single chain condition on the ring propagates to a chain condition on the entire category of finitely generated modules.

Why is this what you want? Because almost every object of commutative algebra is a finitely generated module over a Noetherian ring — ideals, quotient rings, fractional ideals, the modules in a free resolution — and this theorem certifies *all of them* Noetherian in one stroke. The practical consequence is the corollary: over a Noetherian ring you may always assume that any submodule you encounter, of any finitely generated module, is itself finitely generated. That permission is used silently in essentially every structural argument downstream — primary decomposition, the structure theory of modules, dimension theory — all of which need to grab finite generating sets of submodules and would collapse without this guarantee.

The proof is short *because* the previous two theorems did the work. It is two moves: present $M$ as a quotient of a free module $R^{\oplus \ell}$, and observe that $R^{\oplus \ell}$ is Noetherian (finite direct sum of copies of the Noetherian module $R$) and that quotients inherit the chain condition. That both moves are available is exactly what the [[Thm - Chain Conditions Pass Through Short Exact Sequences|two-out-of-three lemma]] supplied. The theorem is best understood as the assembly of that lemma's corollary (direct sums) with its inheritance direction (quotients).

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$R$ Noetherian and $M$ finitely generated over $R$". The disguised sources are situations producing this pair.

The first is **$R$ is a quotient or localisation of a Noetherian ring, and $M$ has finitely many generators**. The property $B$ is "$R = R_0/I$ or $R = S^{-1}R_0$ with $R_0$ Noetherian". The bridge is that quotients and localisations of Noetherian rings are Noetherian, so the hypothesis on $R$ is met. The non-obvious part is that Noetherianity of the base is robust under these operations, so the theorem applies far beyond literal polynomial rings. *Example problem:* every finitely generated module over $\mathbb{Z}/n$, or over a localisation $\mathbb{Z}_{(p)}$, is Noetherian.

The second is **$R$ is a finitely generated algebra over a field or over $\mathbb{Z}$**. The property $B$ is "$R = k[T_1, \dots, T_n]/I$". By [[Thm - Hilbert's Basis Theorem (Algebra Form)|Hilbert's basis theorem]], such $R$ is Noetherian, so any finitely generated module over it is Noetherian. The non-obviousness: the coordinate rings of all affine varieties fall under this theorem. *Example problem:* every finitely generated module over the coordinate ring of an affine variety is Noetherian.

The third is **$M$ is presented by generators and relations, $M = \operatorname{coker}(R^{\oplus t} \to R^{\oplus \ell})$**. The property $B$ is "$M$ has a finite presentation". This is a fortiori finitely generated, so the theorem applies. The non-obviousness is that any module given by a finite matrix of relations is Noetherian over a Noetherian ring, so its submodules (e.g. its torsion submodule, its syzygies) are finitely generated. *Example problem:* the kernel of a map between finitely generated modules over a Noetherian ring is finitely generated.

**Targets (Output Amplification)**

The conclusion is "$M$ is a Noetherian module", hence "every submodule of $M$ is finitely generated".

Combine the conclusion with **the syzygy/kernel of a map of finitely generated modules**. If $f : M \to M'$ is $R$-linear between finitely generated modules over a Noetherian ring, then $\ker f \subseteq M$ is a submodule of a Noetherian module, hence finitely generated. The further result $E$ is that **finite presentations exist**: every finitely generated module over a Noetherian ring is finitely *presented*, since the kernel of $R^{\oplus \ell} \twoheadrightarrow M$ is finitely generated. This is non-obvious because "finitely generated" and "finitely presented" diverge over non-Noetherian rings and coincide here.

Combine the conclusion with **the existence of maximal submodules with a property**. Since $M$ is Noetherian, the maximal condition holds for its submodules, enabling Noetherian induction *inside* $M$. The further result $E$ is the family of structure theorems proved by "choose a maximal counterexample submodule" — associated primes are finite, $M$ has a filtration with quotients $R/\mathfrak{p}_i$. This is non-obvious because it transports the ring's chain condition into an induction principle on submodules of $M$.

Combine the conclusion with **the Artinian version**. If $R$ is Artinian (hence Noetherian of dimension zero) then $M$ is both, so $M$ has finite length. The further result $E$ is that **finitely generated modules over an Artinian ring have finite length**, the basis of the theory of Artinian rings as finite products of local rings. This is non-obvious because finiteness of length — a strong condition — comes for free from finite generation once the base is Artinian.

---

# Why Is It True

The intuition is inheritance: the finiteness of $M$ is *inherited* from the finiteness of the base ring $R$, transported along the surjection from a free module. $M$ is not finite by accident; it is a quotient of $R^{\oplus \ell}$, and that free module is finite (in the chain-condition sense) because $R$ is, and quotients keep the chain condition.

**The bolded mechanism: $M$ is squeezed between two things the chain condition controls — it is a quotient of the Noetherian module $R^{\oplus \ell}$ — so it inherits ACC from $R^{\oplus \ell}$, which in turn inherits it from $R$ via "finite direct sums of Noetherian modules are Noetherian".**

Trace the inheritance. The ring $R$, viewed as a module over itself, is Noetherian by hypothesis — its submodules are ideals, and ACC on ideals is the definition. The free module $R^{\oplus \ell}$ is a *finite* direct sum of copies of this Noetherian module, and the [[Thm - Chain Conditions Pass Through Short Exact Sequences|direct-sum corollary]] (itself the two-out-of-three lemma applied to $0 \to R \to R^{\oplus \ell} \to R^{\oplus(\ell-1)} \to 0$) says a finite direct sum of Noetherian modules is Noetherian. So $R^{\oplus \ell}$ is Noetherian. Finally $M$, being generated by $\ell$ elements $m_1, \dots, m_\ell$, is a *quotient* of $R^{\oplus \ell}$ via $(r_1, \dots, r_\ell) \mapsto \sum r_i m_i$; and the inheritance direction of the two-out-of-three lemma says quotients of Noetherian modules are Noetherian. Hence $M$ is Noetherian.

The deeper point is *where the finiteness lives*. It does not live in the generators of $M$ — those only say $M$ is a quotient of $R^{\oplus \ell}$, which is mere finite generation. It lives in the *ring*: ACC on $R$ is what makes $R^{\oplus \ell}$ Noetherian, and only because the rank $\ell$ is finite does the direct-sum corollary apply (an infinite direct sum of Noetherian modules need *not* be Noetherian). The two finitenesses — finite rank of the free cover and the chain condition of the base — combine through the exact sequence to give the chain condition of $M$. This is exactly why the converse-style failure happens over non-Noetherian rings: $\mathbb{Z}[T_1, T_2, \dots]$ is finitely generated as a module over itself (by $1$), but the base ring is not Noetherian, so the free cover $R^{\oplus 1} = R$ is not Noetherian, and the inheritance has nothing to inherit.

---

# What Makes This Hard

The theorem is not hard once the previous two are in hand — the difficulty is recognising that it is *purely a corollary* and resisting the urge to reprove the chain condition from scratch. The one substantive move is the presentation $M \cong R^{\oplus \ell}/K$: you must see a finitely generated module as a quotient of a free module, which is the surjection $(r_1, \dots, r_\ell) \mapsto \sum r_i m_i$ sending the standard basis to the generators. The common error is to forget that *finite* rank is essential — to apply the direct-sum corollary one needs $\ell < \infty$, and the theorem genuinely fails for non-finitely-generated modules (an infinite-rank free module over a Noetherian ring need not be Noetherian).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Present $M$ as a quotient of a finite-rank free module $R^{\oplus \ell}$. Show $R^{\oplus \ell}$ is Noetherian using that $R$ is Noetherian as a module over itself and finite direct sums preserve the chain condition. Then $M$, a quotient of a Noetherian module, is Noetherian.

**Subgoal decomposition:**

1. **Present $M$ as $R^{\oplus \ell}/K$.** Show a module generated by $\ell$ elements is a quotient of $R^{\oplus \ell}$.
   - *Hint:* The map $(r_1, \dots, r_\ell) \mapsto \sum r_i m_i$ is a surjective $R$-linear map $R^{\oplus \ell} \to M$.
   - *Why needed:* It exhibits $M$ as a quotient, the form on which inheritance acts.

2. **$R^{\oplus \ell}$ is Noetherian.** Show a finite direct sum of copies of the Noetherian module $R$ is Noetherian.
   - *Hint:* Apply the direct-sum corollary of [[Thm - Chain Conditions Pass Through Short Exact Sequences|two-out-of-three]] $\ell - 1$ times.
   - *Why needed:* It supplies a Noetherian module surjecting onto $M$.

3. **Conclude $M$ is Noetherian.** A quotient of a Noetherian module is Noetherian.
   - *Hint:* The inheritance direction of the two-out-of-three lemma, applied to $0 \to K \to R^{\oplus \ell} \to M \to 0$.
   - *Why needed:* It transfers the chain condition from the free cover to $M$.

---

# Lemma Decomposition

> [!note]- Lemma 1: A module with $\ell$ generators is a quotient of $R^{\oplus \ell}$
> **Statement:** If $M = Rm_1 + \cdots + Rm_\ell$, then the map $\pi : R^{\oplus \ell} \to M$, $\pi(r_1, \dots, r_\ell) = \sum_i r_i m_i$, is a surjective $R$-linear map, so $M \cong R^{\oplus \ell}/\ker \pi$.
>
> **Hint:** $R$-linearity is immediate from the formula; surjectivity is exactly the statement that the $m_i$ generate.
>
> **Why needed:** It is the presentation that turns finite generation into "quotient of a free module".
>
> > [!note]- Full proof
> > For $r = (r_1, \dots, r_\ell)$ and $s = (s_1, \dots, s_\ell)$ in $R^{\oplus \ell}$ and $a \in R$: $\pi(r + s) = \sum_i (r_i + s_i) m_i = \pi(r) + \pi(s)$ and $\pi(a r) = \sum_i (a r_i) m_i = a \pi(r)$, so $\pi$ is $R$-linear. Any $x \in M$ is $x = \sum_i r_i m_i$ for some $r_i \in R$ (the $m_i$ generate), so $x = \pi(r_1, \dots, r_\ell) \in \operatorname{im} \pi$; thus $\pi$ is surjective. By the [[Thm - Isomorphism Theorems for Modules|first isomorphism theorem]], $M \cong R^{\oplus \ell}/\ker \pi$.

> [!note]- Lemma 2: $R^{\oplus \ell}$ is Noetherian when $R$ is
> **Statement:** If $R$ is a Noetherian ring (Noetherian as a module over itself), then $R^{\oplus \ell}$ is a Noetherian $R$-module for every $\ell \geq 1$. Likewise for Artinian.
>
> **Hint:** Induct on $\ell$ using the split short exact sequence $0 \to R \to R^{\oplus \ell} \to R^{\oplus(\ell-1)} \to 0$.
>
> **Why needed:** It is the Noetherian free module that surjects onto $M$.
>
> > [!note]- Full proof
> > Base case $\ell = 1$: $R^{\oplus 1} = R$ is Noetherian by hypothesis. Inductive step: assume $R^{\oplus(\ell-1)}$ is Noetherian. The sequence $0 \to R \xrightarrow{r \mapsto (r, 0, \dots, 0)} R^{\oplus \ell} \xrightarrow{(r_1, \dots, r_\ell) \mapsto (r_2, \dots, r_\ell)} R^{\oplus(\ell-1)} \to 0$ is short exact. By [[Thm - Chain Conditions Pass Through Short Exact Sequences|two-out-of-three]], since both ends $R$ and $R^{\oplus(\ell-1)}$ are Noetherian, the middle $R^{\oplus \ell}$ is Noetherian. The Artinian case is identical.

> [!note]- Lemma 3: Quotients of Noetherian modules are Noetherian
> **Statement:** If $P$ is a Noetherian module and $K \subseteq P$ a submodule, then $P/K$ is Noetherian. Likewise for Artinian.
>
> **Hint:** It is the inheritance (forward) direction of the two-out-of-three lemma applied to $0 \to K \to P \to P/K \to 0$.
>
> **Why needed:** It transfers the chain condition from the free cover $R^{\oplus \ell}$ down to $M$.
>
> > [!note]- Full proof
> > Apply [[Thm - Chain Conditions Pass Through Short Exact Sequences|the theorem]] to $0 \to K \to P \to P/K \to 0$: if $P$ is Noetherian then both $K$ and $P/K$ are (the inheritance direction). In particular $P/K$ is Noetherian. The Artinian case is identical.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be Noetherian and $M$ finitely generated, say $M = Rm_1 + \cdots + Rm_\ell$. We show $M$ is a Noetherian module; the Artinian case is verbatim with "Artinian" throughout.
>
> ---
> **Step 1 — present $M$ as a quotient of a free module.** By Lemma 1, the map $\pi : R^{\oplus \ell} \to M$, $\pi(r_1, \dots, r_\ell) = \sum_i r_i m_i$, is surjective and $R$-linear, so there is a short exact sequence
> $$0 \longrightarrow K \longrightarrow R^{\oplus \ell} \xrightarrow{\;\pi\;} M \longrightarrow 0, \qquad K = \ker \pi.$$
>
> ---
> **Step 2 — the free module is Noetherian.** By Lemma 2, $R^{\oplus \ell}$ is a Noetherian $R$-module, because $R$ is Noetherian as a module over itself and finite direct sums of Noetherian modules are Noetherian.
>
> ---
> **Step 3 — the quotient inherits the chain condition.** By Lemma 3 (the inheritance direction of [[Thm - Chain Conditions Pass Through Short Exact Sequences|two-out-of-three]] applied to the sequence of Step 1), the quotient $M \cong R^{\oplus \ell}/K$ of the Noetherian module $R^{\oplus \ell}$ is Noetherian.
>
> Hence $M$ is a Noetherian module.
>
> ---
> **Corollary.** ($\Rightarrow$) If $R$ is Noetherian and $M$ is any finitely generated $R$-module, the theorem makes $M$ Noetherian, so by [[Thm - Noetherian iff Every Submodule is Finitely Generated|the finite-generation characterisation]] every submodule of $M$ is finitely generated. ($\Leftarrow$) If every submodule of every finitely generated $R$-module is finitely generated, apply this to $M = R$: every submodule of $R$ — that is, every ideal — is finitely generated, so $R$ is Noetherian. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Subgroups of finitely generated abelian groups.** Taking $R = \mathbb{Z}$ (Noetherian) and $M$ a finitely generated abelian group, the theorem makes $M$ a Noetherian $\mathbb{Z}$-module, so every subgroup is finitely generated. The application is non-obvious because this finiteness is the unstated input to the classification of finitely generated abelian groups — the relations module is automatically finitely generated.

**Finiteness of syzygies in computational algebra.** Over a polynomial ring $k[T_1, \dots, T_n]$ (Noetherian by Hilbert), the kernel of a map $R^{\oplus \ell} \to R^{\oplus m}$ — the *module of syzygies* — is a submodule of the Noetherian module $R^{\oplus \ell}$, hence finitely generated. The application underwrites the entire theory of free resolutions and Gröbner-basis syzygy computation: resolutions terminate at each stage with finitely many generators.

**Coherent sheaves on Noetherian schemes.** On $\operatorname{Spec} R$ with $R$ Noetherian, a finitely generated module corresponds to a coherent sheaf, and this theorem guarantees its subsheaves correspond to finitely generated submodules — coherence is preserved under taking subsheaves. The application is non-obvious because it is the local statement that makes the global category of coherent sheaves well-behaved (abelian, with finiteness of cohomology).

---

# Bridges

- **[[Thm - Chain Conditions Pass Through Short Exact Sequences|Two-out-of-three for chain conditions]]** — the theorem this is a corollary of. Both of its faces are used: the direct-sum corollary makes $R^{\oplus \ell}$ Noetherian, and the inheritance direction makes the quotient $M$ Noetherian. This theorem is precisely "apply two-out-of-three to the free presentation of $M$".

- **[[Thm - Hilbert's Basis Theorem (Algebra Form)|Hilbert's basis theorem]]** — the companion that supplies Noetherian base rings. Hilbert produces the Noetherian rings (polynomial rings, coordinate rings, finitely generated algebras) over which this theorem then certifies all finitely generated modules Noetherian. The two together cover essentially every ring and module of practical interest: Hilbert makes the ring Noetherian, this theorem makes its modules Noetherian.

- **[[Thm - Noetherian iff Every Submodule is Finitely Generated|Noetherian ⟺ every submodule finitely generated]]** — the characterisation that converts the conclusion into usable form. Once $M$ is known Noetherian, this theorem extracts finite generators of any submodule, which is how the conclusion is actually deployed downstream (finite presentations, finite syzygies, finite associated primes).

- **[[Def - Finitely Presented Module|Finitely presented modules]]** — the strengthening this enables. Over a Noetherian ring, "finitely generated" upgrades to "finitely presented", because the kernel $K$ in $0 \to K \to R^{\oplus \ell} \to M \to 0$ is itself finitely generated (a submodule of the Noetherian $R^{\oplus \ell}$). The distinction between generated and presented, which matters over general rings, evaporates here.

---

# Unlocked by This

> [!tip] Finitely generated equals finitely presented *(from Commutative Algebra)*
> Over a Noetherian ring, every **finitely generated** module is **finitely presented**: the kernel of any surjection $R^{\oplus \ell} \twoheadrightarrow M$ is a submodule of the Noetherian module $R^{\oplus \ell}$, hence finitely generated, so $M$ has a finite presentation $R^{\oplus t} \to R^{\oplus \ell} \to M \to 0$. This is why one rarely distinguishes the two notions in Noetherian commutative algebra, and it is the starting point of the theory of free resolutions and homological dimension.

> [!tip] Finite length over Artinian rings *(from Commutative Algebra)*
> When $R$ is Artinian (equivalently, Noetherian of Krull dimension zero), the theorem makes every finitely generated module both Noetherian and Artinian, hence of **finite length**. This is the basis for the structure theory of Artinian rings — every Artinian ring is a finite product of Artinian local rings, each module over it has a finite composition series — developed in the dimension-theory chapter (Commutative Algebra XII).
