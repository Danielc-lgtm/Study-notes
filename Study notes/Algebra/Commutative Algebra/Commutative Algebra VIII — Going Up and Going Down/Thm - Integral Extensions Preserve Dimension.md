---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Integral Element and Integral Extension"
  - "Def - Krull Dimension and Height"
  - "Def - The Induced Map on Spectra"
  - "Thm - Lying Over"
  - "Thm - Going Up"
  - "Thm - Incomparability"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $A \subseteq B$ be an [[Def - Integral Element and Integral Extension|integral extension]]. [[Def - Krull Dimension and Height|dim R]] is the Krull dimension, the supremum of $n$ over strict chains $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_n$ in $\operatorname{Spec} R$; $\operatorname{ht}\mathfrak{p}$ is the height of $\mathfrak{p}$, $= \dim A_{\mathfrak{p}}$. [[Def - The Induced Map on Spectra|ι*]] is the contraction $\mathfrak{q} \mapsto \mathfrak{q} \cap A$. The full registry is on [[Commutative Algebra VIII — Going Up and Going Down]].

---

# Statement

> **Theorem (Dimension is preserved under integral extension).** Let $A \subseteq B$ be an integral extension of rings. Then
> $$\dim A = \dim B.$$

> **Corollary (Noether normalization computes dimension).** If $A$ is a finitely generated algebra over a field $k$ that is module-finite over a polynomial subring $k[X_1,\dots,X_d]$ (which exists by Noether normalization when $A$ is a domain), then $\dim A = d$. In particular $\dim k[X_1,\dots,X_n] = n$.

> **Remark (no normality needed).** The proof uses only [[Thm - Lying Over|lying over]], [[Thm - Going Up|going up]], and [[Thm - Incomparability|incomparability]] — *not* [[Thm - Going Down for Integrally Closed Domains|going down]]. So dimension equality holds for *every* integral extension, normal or not.

---

# Motivation

This is the headline corollary of the chapter: **a finite map of spaces does not change dimension.** Integrality is the algebra of a finite map, and a finite map covers its target with finite fibres, so it stretches neither dimension up nor down — $\operatorname{Spec} B$ and $\operatorname{Spec} A$ have the same Krull dimension. Every other theorem of the chapter exists, in part, to make this one true: lying over and going up push chains *up* to give $\dim A \leq \dim B$, incomparability pulls chains *down* (contracting without collapse) to give $\dim B \leq \dim A$, and the two inequalities meet.

The practical force is that dimension becomes *computable*. Krull dimension is defined as a supremum over all chains of primes — a quantity one cannot evaluate directly for a complicated ring. But if a ring is integral over a *simple* ring of known dimension, this theorem hands you its dimension for free. The decisive instance is [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz|Noether normalization]]: every finitely generated $k$-domain $A$ is module-finite over a polynomial subring $k[X_1,\dots,X_d]$, where $d$ is the transcendence degree of $\operatorname{Frac} A$ over $k$. Since the extension is integral, $\dim A = \dim k[X_1,\dots,X_d]$, and the latter is $d$ (the chain $(0) \subsetneq (X_1) \subsetneq (X_1,X_2) \subsetneq \cdots \subsetneq (X_1,\dots,X_d)$ realises it, and nothing longer exists). So **the dimension of an affine variety equals the transcendence degree of its function field** — the single most useful computation of dimension, and it runs entirely through this theorem.

It is worth emphasising what this theorem does *not* need. One might expect that preserving dimension requires lifting chains in *both* directions, hence going down, hence normality. It does not. The upper bound $\dim B \leq \dim A$ is pure incomparability (contracting a chain in $B$ gives a chain in $A$ of the same length), and the lower bound $\dim A \leq \dim B$ is lying over plus going up (lifting a chain in $A$ to one in $B$). Neither uses going down. So dimension equality is robust — it holds across the non-normal counterexamples where going down fails. What *does* need going down is the finer, *catenary* statement $\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$, which concerns the position of an intermediate prime, not the gross dimension.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$A \subseteq B$ is integral".

The first disguised source is **a module-finite extension**: $B$ a finitely generated $A$-module $\Rightarrow$ $B$ integral over $A$. So any finite extension preserves dimension, even when "integral" is never spoken. *Example problem:* $\dim \mathcal{O}_K = \dim \mathbb{Z} = 1$ because $\mathcal{O}_K$ is a finite $\mathbb{Z}$-module — every number ring is one-dimensional.

The second disguised source is **a Noether normalization**: a finitely generated $k$-domain is module-finite over a polynomial subring. This is the standard *manufactured* integral extension, produced specifically so this theorem can transfer the dimension of the polynomial ring. *Example problem:* $\dim A = \operatorname{trdeg}_k \operatorname{Frac} A$ for a finitely generated $k$-domain.

The third disguised source is **a quotient by a nilpotent ideal, or passage to the reduced ring**: $A \to A_{\mathrm{red}} = A/\operatorname{nil}A$ has the same spectrum, and more generally an integral surjection preserves dimension on the relevant closed subset. *Example problem:* dimension is unchanged by killing nilpotents, because $\operatorname{Spec}$ does not see them.

**Targets (Output Amplification)**

The conclusion is $\dim A = \dim B$.

Combine with **Noether normalization** to compute $\dim k[X_1,\dots,X_n] = n$ and $\dim A = \operatorname{trdeg}_k \operatorname{Frac} A$. The result $E$ is the foundational dimension computation for affine varieties.

Combine with **[[Thm - Going Down for Integrally Closed Domains|going down]] (when $A$ is normal)** to upgrade dimension equality to the *catenary* formula $\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$. The result $E$ controls the dimension of every subvariety, not just the whole space — the dimension theory of varieties.

Combine with **height** $\operatorname{ht}\mathfrak{q} = \dim B_{\mathfrak{q}}$: localizing the integral extension at $\mathfrak{q}$ and its contraction gives $\dim B_{\mathfrak{q}} = \dim A_{\mathfrak{q}\cap A}$ when normality permits going down, i.e. $\operatorname{ht}\mathfrak{q} = \operatorname{ht}(\mathfrak{q}\cap A)$. The result $E$: height is an integral-extension invariant under contraction, used in computing codimensions.

---

# Why Is It True

The theorem is the marriage of two one-directional chain arguments, and the cleanest way to hold it is as a *symmetry*: chains pass between $\operatorname{Spec} A$ and $\operatorname{Spec} B$ in both directions, preserving length.

**Direction $\dim A \leq \dim B$ (lift a chain).** Take a strict chain $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_n$ in $A$. [[Thm - Lying Over|Lying over]] plants a prime $\mathfrak{q}_0$ over $\mathfrak{p}_0$; [[Thm - Going Up|going up]], applied $n$ times, extends it to $\mathfrak{q}_0 \subseteq \mathfrak{q}_1 \subseteq \cdots \subseteq \mathfrak{q}_n$ with $\mathfrak{q}_i$ over $\mathfrak{p}_i$. Each inclusion $\mathfrak{q}_i \subseteq \mathfrak{q}_{i+1}$ is *strict*: their contractions $\mathfrak{p}_i \neq \mathfrak{p}_{i+1}$ differ, so the primes differ. Hence $B$ has a strict chain of length $n$, and $\dim B \geq n$. Sup over chains in $A$: $\dim B \geq \dim A$.

**Direction $\dim B \leq \dim A$ (contract a chain).** Take a strict chain $\mathfrak{q}_0 \subsetneq \cdots \subsetneq \mathfrak{q}_n$ in $B$. Contraction gives $\mathfrak{q}_0\cap A \subseteq \cdots \subseteq \mathfrak{q}_n\cap A$ in $A$. By [[Thm - Incomparability|incomparability]], consecutive contractions cannot be equal — $\mathfrak{q}_i \subsetneq \mathfrak{q}_{i+1}$ with the same contraction would force $\mathfrak{q}_i = \mathfrak{q}_{i+1}$ — so the contracted chain is strict of length $n$, and $\dim A \geq n$. Sup over chains in $B$: $\dim A \geq \dim B$.

**The mechanism in one line: lying-over-plus-going-up carries chains upstairs without shortening, incomparability carries them downstairs without collapsing, and the two together force the chain-length suprema to agree.** The crucial point — easy to miss — is that *strictness is preserved in both directions because contractions of comparable distinct primes are distinct*, which is incomparability. That single fact does double duty: it keeps the lifted chain strict (different $\mathfrak{p}_i$ force different $\mathfrak{q}_i$) and keeps the contracted chain strict (different $\mathfrak{q}_i$, being comparable, force different $\mathfrak{p}_i$).

---

# What Makes This Hard

The proof is not hard once organised; the difficulty is *bookkeeping the strictness*, and the trap is forgetting that contracting a chain could a priori collapse it. The non-obvious realisation is that the *same* theorem — incomparability — guarantees strictness in *both* directions of the argument, so it is invoked twice for two different-looking purposes. The most common error is to think dimension preservation needs going down (and hence normality); it does not, and seeing why requires noticing that neither inequality lifts a chain *downward* — the upward lift (going up) and the contraction (incomparability) suffice.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove two inequalities. Up: lift a chain of $A$ to a chain of $B$ via lying over (anchor) and going up (extend), with strictness from incomparability, giving $\dim A \leq \dim B$. Down: contract a chain of $B$ to a chain of $A$, with strictness from incomparability, giving $\dim B \leq \dim A$.

**Subgoal decomposition:**

1. **$\dim A \leq \dim B$: lift an arbitrary strict chain of $A$.**
   - *Hint:* Lying over over the bottom, then going up at each step; strictness because $\mathfrak{p}_i \neq \mathfrak{p}_{i+1}$ forces $\mathfrak{q}_i \neq \mathfrak{q}_{i+1}$.
   - *Why needed:* It is the lower bound.

2. **$\dim B \leq \dim A$: contract an arbitrary strict chain of $B$.**
   - *Hint:* Contraction preserves $\subseteq$; incomparability forbids consecutive equal contractions, so strictness survives.
   - *Why needed:* It is the upper bound; together with (1) it gives equality.

3. **(Corollary) Apply to a Noether normalization to compute $\dim A$.**
   - *Hint:* $A$ module-finite over $k[X_1,\dots,X_d]$ is integral; $\dim k[X_1,\dots,X_d] = d$ via the standard chain.
   - *Why needed:* It is the headline application.

---

# Lemma Decomposition

> [!note]- Lemma 1: Lifting a chain (lower bound)
> **Statement:** Every strict chain $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_n$ in $\operatorname{Spec} A$ lifts to a strict chain $\mathfrak{q}_0 \subsetneq \cdots \subsetneq \mathfrak{q}_n$ in $\operatorname{Spec} B$ with $\mathfrak{q}_i \cap A = \mathfrak{p}_i$. Hence $\dim B \geq \dim A$.
>
> **Hint:** Lying over anchors $\mathfrak{q}_0$; going up extends; incomparability gives strictness.
>
> **Why needed:** It is the $\leq$ half of the dimension equality.
>
> > [!note]- Full proof
> > By [[Thm - Lying Over|lying over]] there is $\mathfrak{q}_0 \in \operatorname{Spec} B$ with $\mathfrak{q}_0 \cap A = \mathfrak{p}_0$. Inductively, given $\mathfrak{q}_i$ over $\mathfrak{p}_i$, apply [[Thm - Going Up|going up]] to $\mathfrak{p}_i \subsetneq \mathfrak{p}_{i+1}$ and $\mathfrak{q}_i$ to get $\mathfrak{q}_{i+1} \supseteq \mathfrak{q}_i$ over $\mathfrak{p}_{i+1}$. Each step is strict: if $\mathfrak{q}_i = \mathfrak{q}_{i+1}$ then $\mathfrak{p}_i = \mathfrak{q}_i \cap A = \mathfrak{q}_{i+1}\cap A = \mathfrak{p}_{i+1}$, contradicting $\mathfrak{p}_i \subsetneq \mathfrak{p}_{i+1}$. So $\mathfrak{q}_0 \subsetneq \cdots \subsetneq \mathfrak{q}_n$ is a strict chain of length $n$ in $B$, whence $\dim B \geq n$. Taking the supremum over chains in $A$ gives $\dim B \geq \dim A$.

> [!note]- Lemma 2: Contracting a chain (upper bound)
> **Statement:** Every strict chain $\mathfrak{q}_0 \subsetneq \cdots \subsetneq \mathfrak{q}_n$ in $\operatorname{Spec} B$ contracts to a strict chain $\mathfrak{q}_0\cap A \subsetneq \cdots \subsetneq \mathfrak{q}_n \cap A$ in $\operatorname{Spec} A$. Hence $\dim A \geq \dim B$.
>
> **Hint:** Contraction preserves inclusions; incomparability forbids a collapse $\mathfrak{q}_i \cap A = \mathfrak{q}_{i+1}\cap A$.
>
> **Why needed:** It is the $\geq$ half of the dimension equality.
>
> > [!note]- Full proof
> > Contraction is order-preserving, so $\mathfrak{q}_0\cap A \subseteq \cdots \subseteq \mathfrak{q}_n\cap A$. Suppose $\mathfrak{q}_i \cap A = \mathfrak{q}_{i+1}\cap A$ for some $i$. Then $\mathfrak{q}_i \subsetneq \mathfrak{q}_{i+1}$ are comparable primes of $B$ with the same contraction, so by [[Thm - Incomparability|incomparability]] $\mathfrak{q}_i = \mathfrak{q}_{i+1}$ — contradicting strictness. Hence all consecutive contractions are distinct, and $\mathfrak{q}_0\cap A \subsetneq \cdots \subsetneq \mathfrak{q}_n\cap A$ is strict of length $n$, giving $\dim A \geq n$. Supremum over chains in $B$: $\dim A \geq \dim B$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $A \subseteq B$ be an integral extension.
>
> **Step 1 — $\dim A \leq \dim B$.** By Lemma 1, every strict chain of primes of $A$ of length $n$ lifts to a strict chain of $B$ of length $n$ (lying over to anchor, going up to extend, incomparability for strictness). Hence $\dim B \geq \dim A$.
>
> **Step 2 — $\dim B \leq \dim A$.** By Lemma 2, every strict chain of primes of $B$ of length $n$ contracts to a strict chain of $A$ of length $n$ (incomparability prevents collapse). Hence $\dim A \geq \dim B$.
>
> Combining, $\dim A = \dim B$. $\blacksquare$
>
> ---
> **Corollary (computation of $\dim k[X_1,\dots,X_n]$).** First, $\dim k[X_1,\dots,X_n] \geq n$ via the strict chain $(0) \subsetneq (X_1) \subsetneq (X_1,X_2) \subsetneq \cdots \subsetneq (X_1,\dots,X_n)$ of primes (each $k[X_1,\dots,X_n]/(X_1,\dots,X_i) \cong k[X_{i+1},\dots,X_n]$ is a domain, so each $(X_1,\dots,X_i)$ is prime). The reverse inequality $\dim k[X_1,\dots,X_n] \leq n$ is proved in [[Commutative Algebra XII — Dimension Theory|the dimension chapter]] (e.g. via transcendence degree). For a finitely generated $k$-domain $A$, [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz|Noether normalization]] gives a polynomial subring $k[X_1,\dots,X_d] \subseteq A$ over which $A$ is module-finite, hence integral; by the theorem $\dim A = \dim k[X_1,\dots,X_d] = d = \operatorname{trdeg}_k\operatorname{Frac} A$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Number rings are one-dimensional.** For a number field $K$, $\mathcal{O}_K$ is a finite (hence integral) $\mathbb{Z}$-module, so $\dim \mathcal{O}_K = \dim \mathbb{Z} = 1$. This one line is why every ring of integers is a one-dimensional ring — a [[Commutative Algebra XIII — Dedekind Domains and DVRs|Dedekind domain]] — without any computation specific to $K$. The application is non-obvious because one expects the arithmetic of $K$ to matter; dimension preservation says it does not.

**The dimension of a hypersurface is $n-1$.** For an irreducible polynomial $f \in k[X_1,\dots,X_n]$, the coordinate ring $k[X_1,\dots,X_n]/(f)$ of the hypersurface $V(f)$ has transcendence degree $n-1$ (one relation among $n$ coordinates), and after Noether normalization is integral over $k[Y_1,\dots,Y_{n-1}]$, so its dimension is $n-1$ by this theorem. The application is non-obvious because it converts "one equation drops dimension by one" into a transcendence-degree count routed through an integral extension — the prototype of [[Commutative Algebra XII — Dimension Theory|Krull's height theorem]].

**Invariant rings of finite groups have the same dimension.** If a finite group $G$ acts on $B = k[X_1,\dots,X_n]$, the invariant subring $A = B^G$ has $B$ integral over it (each $b$ satisfies $\prod_{g\in G}(T - g\cdot b) = 0$, a monic relation with $G$-invariant coefficients). So $\dim B^G = \dim B = n$: the quotient variety $\operatorname{Spec} B^G = \mathbb{A}^n/G$ has the same dimension as $\mathbb{A}^n$. The application is non-obvious because the invariant ring can be far more complicated than $B$, yet its dimension is forced by integrality alone.

---

# Bridges

- **[[Thm - Lying Over|Lying Over]]** and **[[Thm - Going Up|Going Up]]** — together they give the lower bound $\dim A \leq \dim B$ by lifting a chain (lying over anchors it, going up extends it). They are the "upward girder" of the dimension bridge, and neither alone suffices: you need the anchor *and* the extension.

- **[[Thm - Incomparability|Incomparability]]** — the upper bound $\dim B \leq \dim A$ is pure incomparability (contract a chain without collapse), and incomparability *also* supplies the strictness in the lower-bound lift. It is the one theorem invoked on both sides, doing the load-bearing work of keeping chains strict in either direction.

- **[[Thm - Going Down for Integrally Closed Domains|Going Down]]** — notably *not* used here: dimension equality needs only three theorems. Going down enters one level up, in the *catenary* refinement $\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$, which controls where an intermediate prime sits in a chain. Dimension equality is the gross statement; the catenary formula is the fine one, and only the fine one costs normality.

- **[[Commutative Algebra VII — Noether Normalization and the Nullstellensatz|Noether Normalization]]** — this theorem is the *reason Noether normalization computes dimension*: normalization manufactures an integral extension over a polynomial ring, and dimension preservation transports the polynomial ring's known dimension to $A$. The pairing "Noether normalize, then preserve dimension" is the standard route to $\dim A = \operatorname{trdeg}_k \operatorname{Frac} A$.

---

# Unlocked by This

> [!tip] The dimension of an affine variety is its transcendence degree *(from Algebraic Geometry)*
> Combined with **Noether normalization**, this theorem yields the foundational fact $\dim A = \operatorname{trdeg}_k \operatorname{Frac} A$ for a finitely generated $k$-domain — the dimension of an **affine variety** equals the transcendence degree of its function field, and $\dim \mathbb{A}^n = n$. This is the entry point to the entire dimension theory of varieties and **schemes**: codimension, the [[Commutative Algebra XII — Dimension Theory|Krull height theorem]] ("a hypersurface drops dimension by one"), and the dimension formula $\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$ all build on it.
