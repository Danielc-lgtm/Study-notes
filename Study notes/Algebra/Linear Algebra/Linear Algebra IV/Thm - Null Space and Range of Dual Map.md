---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Dual Map"
  - "Def - Annihilator"
  - "Def - Null Space and Range"
  - "Thm - Fundamental Theorem of Linear Maps"
  - "Thm - Dimension of Dual Space"
tags: [algebra, linear-algebra]
---

# Notation

$V$ and $W$ are finite-dimensional vector spaces over $\mathbb{F}$, $T \in \mathcal{L}(V, W)$ is a linear map, and $T' \in \mathcal{L}(W', V')$ is its [[Def - Dual Map|dual map]] defined by $T'(\varphi) = \varphi \circ T$. The [[Def - Annihilator (Dual Space)|annihilator]] of $U \subseteq V$ is $U^0 \subseteq V'$. Full registry on [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

---

# Statement

> **Theorem ([[Def - Null Space and Range|Null Space and Range]] of the [[Def - Dual Map|Dual Map]]).** Suppose $V$ and $W$ are finite-dimensional and $T \in \mathcal{L}(V, W)$. Then:
> $$
> \operatorname{null} T' = (\operatorname{range} T)^0, \qquad \operatorname{range} T' = (\operatorname{null} T)^0.
> $$
> Consequently:
> - $T$ is surjective $\iff$ $T'$ is injective.
> - $T$ is injective $\iff$ $T'$ is surjective.
> - $\dim \operatorname{range} T' = \dim \operatorname{range} T$ (the *rank of the dual equals the rank*).

The first equality, $\operatorname{null} T' = (\operatorname{range} T)^0$, actually holds without finite-dimensionality of $V$ — only of $W$, or even neither, in suitable form. The other identities and corollaries use the dimension formulas.

---

# Motivation

The dual map $T'$ reverses the direction of $T$, and the natural question is what it does to [[Def - Subspace|subspaces]]. The null space and range of $T'$ ought to be related to the null space and range of $T$ — but through what relation?

The answer is *annihilation*: the null space of $T'$ is the annihilator of the range of $T$, and the range of $T'$ is the annihilator of the null space of $T$. The relation is *covariant* (no extra reversal beyond the one already in the dual map) and reads as a four-corner diagram:
$$
\begin{array}{|c|c|}
\hline
\operatorname{null} T \subseteq V & \operatorname{range} T \subseteq W \\
\hline
\downarrow \text{annihilate} & \downarrow \text{annihilate} \\
\hline
(\operatorname{null} T)^0 \subseteq V' & (\operatorname{range} T)^0 \subseteq W' \\
\| & \| \\
\operatorname{range} T' \subseteq V' & \operatorname{null} T' \subseteq W' \\
\hline
\end{array}
$$

(With the rows of the lower half flipped to match the *direction* of $T'$, which goes from $W'$ to $V'$.)

This four-fold identity has spectacular consequences for problem-solving. To prove "$T$ is surjective", you can equivalently prove "$T'$ is injective" — and often $T'$ is easier to analyse. Similarly, "$T$ is injective" is equivalent to "$T'$ is surjective". And the *rank* of $T'$ equals the rank of $T$, which is the structural source of "row rank equals column rank" (see [[Ex - Row rank equals column rank]]).

The theorem is one of those identities that looks like four separate statements but is essentially one structural fact: *dualization converts null spaces to [[Def - Annihilator|annihilators]] of ranges, and vice versa*. Once you see the symmetry the four-corner picture exposes, the consequences fall out automatically.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is finite-dimensionality. The disguised sources are setups where the dual map is used implicitly.

The first disguised source is **a problem about surjectivity of $T$** where direct analysis is hard. Convert to injectivity of $T'$: $T$ surjective $\iff$ $\operatorname{range} T = W$ $\iff$ $(\operatorname{range} T)^0 = \{0\}$ in $W'$ $\iff$ $\operatorname{null} T' = \{0\}$ $\iff$ $T'$ is injective. Each step is a one-line equivalence; the productive ones are the ones converting "fill up $W$" (a high-dimensional property to check) into "trivial null space" (a low-dimensional condition). *Example problem:* given $T : V \to W$ with $V$ large but $W$ small, show $T$ is surjective by showing every nonzero functional $\varphi \in W'$ has $T'(\varphi) \neq 0$.

The second disguised source is **a problem about injectivity of $T$**. Convert to surjectivity of $T'$: $T$ injective $\iff$ $\operatorname{null} T = \{0\}$ $\iff$ $(\operatorname{null} T)^0 = V'$ $\iff$ $\operatorname{range} T' = V'$ $\iff$ $T'$ surjective.

The third disguised source is **a problem about ranks**. The identity $\dim \operatorname{range} T' = \dim \operatorname{range} T$ converts "compute rank of $T$" into "compute rank of $T'$"; whichever is easier wins. *Example problem:* row rank equals column rank — apply this identity with $T$ being multiplication by the matrix and $T'$ being its dual, in standard bases.

**Targets (Output Amplification)**

Combine with **dimension counting**. The conclusion of the theorem, combined with dimension formulas, gives:
$$\dim \operatorname{null} T' = \dim W - \dim \operatorname{range} T = \dim W - (\dim V - \dim \operatorname{null} T) = \dim \operatorname{null} T + \dim W - \dim V.$$
This is a *useful* formula in its own right, especially when $\dim W \neq \dim V$: it lets you compute the null space of the dual without computing the dual explicitly.

Combine with **the matrix-transpose interpretation**. Using [[Thm - Matrix of Dual Map is Transpose]], the rank equality $\dim \operatorname{range} T' = \dim \operatorname{range} T$ becomes "column rank of $A^t$ equals column rank of $A$", which is "row rank of $A$ equals column rank of $A$". The classical identity is a direct corollary of the present theorem.

Combine with **the annihilator dimension formula**. The identity $\dim U^0 = \dim V - \dim U$ (Exercise [[Ex - Annihilator of a subspace has complementary dimension]]) combined with the present theorem gives $\dim \operatorname{range} T' = \dim V - \dim \operatorname{null} T = \dim \operatorname{range} T$, recovering the rank equality.

---

# Why Is It True

The four-corner identity has *one* underlying reason: **a functional $\varphi$ on $W$ vanishes on the range of $T$ if and only if the pulled-back functional $\varphi \circ T = T'(\varphi)$ is the zero functional on $V$.**

Unpack this:
- $\varphi$ vanishes on $\operatorname{range} T$ means $\varphi(Tv) = 0$ for every $v \in V$.
- $\varphi \circ T$ being zero on $V$ means $(\varphi \circ T)(v) = \varphi(Tv) = 0$ for every $v \in V$.

These are word-for-word the same condition. So $\varphi \in (\operatorname{range} T)^0$ if and only if $T'(\varphi) = 0$, that is, if and only if $\varphi \in \operatorname{null} T'$. This is the first equality.

The second equality, $\operatorname{range} T' = (\operatorname{null} T)^0$, is one direction by direct verification (if $\varphi \in \operatorname{range} T'$, then $\varphi = T'(\psi) = \psi \circ T$ for some $\psi$; for $v \in \operatorname{null} T$, $\varphi(v) = \psi(Tv) = \psi(0) = 0$, so $\varphi \in (\operatorname{null} T)^0$) and the other direction by dimension counting using the first equality and the annihilator dimension formula.

> **The whole intuition in one sentence: $\varphi$ pulls back to zero through $T$ if and only if $\varphi$ already vanishes on what $T$ hits.**

The surjectivity/injectivity duality is then immediate: $T$ is surjective iff $\operatorname{range} T = W$ iff $(\operatorname{range} T)^0 = W^0 = \{0\}$, and this is exactly $\operatorname{null} T' = \{0\}$, i.e. $T'$ injective. The mechanism is annihilator-of-the-whole-space-is-zero.

---

# What Makes This Hard

The trap is in the *direction of the implication* and in *not confusing dual with adjoint*. The first equality $\operatorname{null} T' = (\operatorname{range} T)^0$ is direct and short; the second $\operatorname{range} T' = (\operatorname{null} T)^0$ is harder because the easy direction gives only $\operatorname{range} T' \subseteq (\operatorname{null} T)^0$, and the reverse inclusion needs dimension counting (in finite [[Def - Dimension|dimensions]]) or an extension argument. The standard proof uses the dimension shortcut: both sides have the same dimension, and one is contained in the other, so they are equal.

The other slip is conflating the dual $T'$ with the adjoint $T^*$ from [[Linear Algebra VII — §7 Operators on Inner Product Spaces|Chapter 7]]. The adjoint is a map $W \to V$ (not $W' \to V'$), it requires an inner product, and the formulas $\operatorname{null} T^* = (\operatorname{range} T)^\perp$, $\operatorname{range} T^* = (\operatorname{null} T)^\perp$ use orthogonal complements (not [[Def - Annihilator|annihilators]]). The structural pattern is *the same*, and the inner product is what bridges dual and adjoint via Riesz representation, but the two are formally distinct.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove the two annihilator identities, then derive the four corollaries by routine equivalences. The first identity is direct; the second uses dimension counting.

**Subgoal decomposition:**

1. **First identity: $\operatorname{null} T' = (\operatorname{range} T)^0$.**
   - *Hint:* $T'(\varphi) = 0 \iff \varphi \circ T = 0$ on $V$ $\iff \varphi$ vanishes on the range of $T$.
   - *Why needed:* This is the core identity.

2. **Second identity (easy direction): $\operatorname{range} T' \subseteq (\operatorname{null} T)^0$.**
   - *Hint:* If $\varphi = T'(\psi) = \psi \circ T$, then for $v \in \operatorname{null} T$, $\varphi(v) = \psi(Tv) = \psi(0) = 0$.
   - *Why needed:* The easy half of the second identity.

3. **Second identity ([[Def - Dimension|dimensions]] agree): $\dim \operatorname{range} T' = \dim (\operatorname{null} T)^0$.**
   - *Hint:* Compute $\dim \operatorname{range} T'$ via rank-nullity on $T'$ and the first identity. Compute $\dim (\operatorname{null} T)^0 = \dim V - \dim \operatorname{null} T = \dim \operatorname{range} T$ via the [[Ex - Annihilator of a subspace has complementary dimension|annihilator formula]] and rank-nullity on $T$. Both equal $\dim \operatorname{range} T$.
   - *Why needed:* Containment plus dimension equality gives equality of [[Def - Subspace|subspaces]].

4. **Rank equality: $\dim \operatorname{range} T' = \dim \operatorname{range} T$.**
   - *Hint:* Falls out of the computation in step 3.
   - *Why needed:* This is one of the corollaries.

5. **Surjectivity/injectivity equivalences.**
   - *Hint:* $T$ surjective $\iff \operatorname{range} T = W \iff (\operatorname{range} T)^0 = W^0 = \{0\} \iff \operatorname{null} T' = \{0\} \iff T'$ injective. Symmetric argument for the other equivalence using the second annihilator identity.
   - *Why needed:* The four corollaries are the most useful form of the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: First annihilator identity $\operatorname{null} T' = (\operatorname{range} T)^0$
> **Statement:** For $T \in \mathcal{L}(V, W)$ (no finite-dimensionality needed), $\operatorname{null} T' = (\operatorname{range} T)^0$ as subspaces of $W'$.
>
> **Hint:** Unwind both sides using the definitions of $T'$ and $(\operatorname{range} T)^0$ — they reduce to the same condition.
>
> **Why needed:** This is the core identity. Both directions are direct.
>
> > [!note]- Full proof
> > Let $\varphi \in W'$.
> >
> > ($\Rightarrow$) Suppose $\varphi \in \operatorname{null} T'$, i.e. $T'(\varphi) = 0$. By definition $T'(\varphi) = \varphi \circ T$, and "$\varphi \circ T = 0$" means $\varphi(Tv) = 0$ for every $v \in V$. So $\varphi$ vanishes on every element of $\operatorname{range} T$, i.e. $\varphi \in (\operatorname{range} T)^0$.
> >
> > ($\Leftarrow$) Suppose $\varphi \in (\operatorname{range} T)^0$, i.e. $\varphi(Tv) = 0$ for every $v$. Then $(\varphi \circ T)(v) = \varphi(Tv) = 0$ for every $v$, so $\varphi \circ T = 0$ as a map $V \to \mathbb{F}$, i.e. $T'(\varphi) = 0$. So $\varphi \in \operatorname{null} T'$.

> [!note]- Lemma 2: Inclusion direction of the second identity
> **Statement:** For $T \in \mathcal{L}(V, W)$, $\operatorname{range} T' \subseteq (\operatorname{null} T)^0$ as subspaces of $V'$.
>
> **Hint:** Take $\varphi \in \operatorname{range} T'$, so $\varphi = T'(\psi) = \psi \circ T$ for some $\psi \in W'$. For $v \in \operatorname{null} T$, $\varphi(v) = \psi(Tv) = \psi(0) = 0$.
>
> **Why needed:** The easy half of the second identity. The reverse inclusion needs dimension.
>
> > [!note]- Full proof
> > Let $\varphi \in \operatorname{range} T'$. Then there exists $\psi \in W'$ with $\varphi = T'(\psi) = \psi \circ T$. For any $v \in \operatorname{null} T$:
> > $$\varphi(v) = (\psi \circ T)(v) = \psi(Tv) = \psi(0) = 0,$$
> > using linearity of $\psi$. So $\varphi$ vanishes on $\operatorname{null} T$, i.e. $\varphi \in (\operatorname{null} T)^0$.

> [!note]- Lemma 3: Dimension count $\dim \operatorname{range} T' = \dim \operatorname{range} T$
> **Statement:** Suppose $V, W$ finite-dimensional and $T \in \mathcal{L}(V, W)$. Then $\dim \operatorname{range} T' = \dim \operatorname{range} T$.
>
> **Hint:** Chain dimension formulas: $\dim \operatorname{range} T' = \dim W' - \dim \operatorname{null} T'$ (rank-nullity on $T'$) $= \dim W - \dim(\operatorname{range} T)^0$ (dual dimension and Lemma 1) $= \dim \operatorname{range} T$ (annihilator dimension formula).
>
> **Why needed:** This is one corollary, and is also the input for closing the second annihilator identity.
>
> > [!note]- Full proof
> > Apply [[Thm - Fundamental Theorem of Linear Maps|rank-nullity]] to $T' : W' \to V'$:
> > $$\dim \operatorname{range} T' = \dim W' - \dim \operatorname{null} T'.$$
> > Use [[Thm - Dimension of Dual Space|$\dim W' = \dim W$]] and Lemma 1 ($\operatorname{null} T' = (\operatorname{range} T)^0$):
> > $$= \dim W - \dim (\operatorname{range} T)^0.$$
> > Use the annihilator dimension formula $\dim U^0 = \dim W - \dim U$ applied to $U = \operatorname{range} T \leq W$:
> > $$\dim (\operatorname{range} T)^0 = \dim W - \dim \operatorname{range} T.$$
> > Substituting:
> > $$\dim \operatorname{range} T' = \dim W - (\dim W - \dim \operatorname{range} T) = \dim \operatorname{range} T. \qquad \blacksquare$$

---

# Formal Proof

> [!note]- Complete formal proof
> Throughout, $T \in \mathcal{L}(V, W)$ with $V, W$ finite-dimensional.
>
> **Step 1 — first identity $\operatorname{null} T' = (\operatorname{range} T)^0$:** by Lemma 1.
>
> **Step 2 — second identity $\operatorname{range} T' = (\operatorname{null} T)^0$:**
> By Lemma 2, $\operatorname{range} T' \subseteq (\operatorname{null} T)^0$. By Lemma 3,
> $$\dim \operatorname{range} T' = \dim \operatorname{range} T.$$
> By [[Thm - Fundamental Theorem of Linear Maps|rank-nullity]] applied to $T$, $\dim \operatorname{range} T = \dim V - \dim \operatorname{null} T$. By the annihilator dimension formula (applied to $\operatorname{null} T \leq V$),
> $$\dim (\operatorname{null} T)^0 = \dim V - \dim \operatorname{null} T.$$
> So $\dim \operatorname{range} T' = \dim (\operatorname{null} T)^0$. Since $\operatorname{range} T'$ is a subspace of $(\operatorname{null} T)^0$ with the same dimension, they are equal.
>
> **Step 3 — rank equality:** by Lemma 3, $\dim \operatorname{range} T' = \dim \operatorname{range} T$.
>
> **Step 4 — surjectivity/injectivity duality:**
> *($T$ surjective $\iff$ $T'$ injective):*
> $$T \text{ surjective} \iff \operatorname{range} T = W \iff (\operatorname{range} T)^0 = W^0 = \{0\} \iff \operatorname{null} T' = \{0\} \iff T' \text{ injective},$$
> using the first annihilator identity in the third step and $W^0 = \{0\}$ in $W'$ in the second.
>
> *($T$ injective $\iff$ $T'$ surjective):*
> $$T \text{ injective} \iff \operatorname{null} T = \{0\} \iff (\operatorname{null} T)^0 = \{0\}^0 = V' \iff \operatorname{range} T' = V' \iff T' \text{ surjective},$$
> using the second annihilator identity in the third step and $\{0\}^0 = V'$ in $V'$ in the second. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Row rank equals column rank.** Let $A \in \mathbb{F}^{m, n}$. View $A$ as the matrix of $T : \mathbb{F}^{n,1} \to \mathbb{F}^{m,1}$, $Tx = Ax$, in standard bases. The column rank of $A$ is $\dim \operatorname{range} T$; the column rank of $A^t$ is $\dim \operatorname{range} T'$ (using that $\mathcal{M}(T') = A^t$ in dual bases, see [[Thm - Matrix of Dual Map is Transpose]]); and the column rank of $A^t$ is the row rank of $A$. By the present theorem $\dim \operatorname{range} T = \dim \operatorname{range} T'$, hence row rank equals column rank. This is the cleanest conceptual proof of one of the most famous identities in linear algebra. See [[Ex - Row rank equals column rank]].

**Surjectivity via dual injectivity.** Given a linear map $T : V \to W$ with $V$ very large but $W$ small (say $\dim W = 2$), proving surjectivity of $T$ directly may require constructing preimages for a basis of $W$ — hard to do explicitly. Instead, show $T'$ is injective: $T'$ goes from $W'$ (a 2-dimensional space) to $V'$, and injectivity is equivalent to showing $\operatorname{null} T'$ is trivial, which is a tiny check.

**Range of a derivative operator.** Let $D : \mathcal{P}_n(\mathbb{R}) \to \mathcal{P}_{n-1}(\mathbb{R})$ be the differentiation map. Compute $\operatorname{range} D$ by dualization: $D' : \mathcal{P}_{n-1}(\mathbb{R})' \to \mathcal{P}_n(\mathbb{R})'$ sends $\varphi$ to $\varphi \circ D$. The dual map is essentially "evaluate at one degree higher", and reading off $\operatorname{range} D'$ gives the range of $D$ via the annihilator. Useful as a calibration exercise.

---

# Bridges

- **[[Thm - Fundamental Theorem of Linear Maps]]** — the dimension formulas in the proof use rank-nullity on both $T$ and $T'$. The present theorem is in some sense "rank-nullity applied dually".

- **[[Def - Annihilator (Dual Space)]]** — the structural identities are statements about annihilators. The annihilator construction is the bridge that makes the dual map's null space and range readable in terms of $T$'s data.

- **[[Thm - Matrix of Dual Map is Transpose]]** — the matrix-level shadow of the present theorem. The rank equality $\dim \operatorname{range} T' = \dim \operatorname{range} T$ becomes "column rank of $A^t$ equals column rank of $A$" which equals "row rank of $A$ equals column rank of $A$".

- **Spectral Theorem on inner product spaces** ([[Linear Algebra VII — §7 Operators on Inner Product Spaces|Chapter 7]]) — for the adjoint $T^*$ (not the dual $T'$), the analogous formulas use *orthogonal complements*: $\operatorname{null} T^* = (\operatorname{range} T)^\perp$, $\operatorname{range} T^* = (\operatorname{null} T)^\perp$. The structural pattern is identical; the inner product converts annihilators to orthogonal complements via Riesz representation.

- **Fredholm Alternative** (Functional Analysis) — in infinite dimensions, the four equivalences become the *Fredholm alternative*: for a compact perturbation of the identity, "$T$ surjective $\iff$ $T'$ injective". This is the infinite-dimensional version of the present theorem, requiring careful analysis to manage the closure of ranges.

---

# Unlocked by This

> [!tip] Row Rank Equals Column Rank *(from this topic)*
> The rank equality $\dim \operatorname{range} T' = \dim \operatorname{range} T$ combined with [[Thm - Matrix of Dual Map is Transpose]] gives the foundational fact that **row rank of $A$ = column rank of $A$**. See [[Ex - Row rank equals column rank]].

> [!tip] Fredholm Alternative *(from Functional Analysis)*
> The bi-implications "$T$ surjective $\iff$ $T'$ injective" generalise to the **Fredholm alternative** for compact operators on Banach spaces. This is the substantive theorem that makes integral equations solvable.

> [!tip] Solvability of Linear Systems *(from Linear Algebra)*
> The system $Ax = b$ is solvable iff $b \perp$ every functional vanishing on the columns of $A$ — that is, iff $b \in \operatorname{range} A$. The dual version: the system is solvable for *all* $b$ iff the dual map $A^t$ has trivial null space, which (over a square matrix) is invertibility of $A^t$, which is invertibility of $A$. This is the conceptual structure behind the surjectivity-injectivity duality on square matrices.
