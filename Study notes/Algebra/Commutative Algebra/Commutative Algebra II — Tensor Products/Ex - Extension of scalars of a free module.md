---
type: exercise
subject: commutative-algebra
difficulty: "⭐"
prereqs:
  - "Def - Tensor Product of Modules"
  - "Def - Restriction and Extension of Scalars"
  - "Thm - Standard Isomorphisms of Tensor Products"
  - "Thm - Extension of Scalars and the Adjunction"
  - "Def - Free Module"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $f : R\to S$ be a ring homomorphism. Prove that [[Def - Restriction and Extension of Scalars|extension of scalars]] sends free modules to free modules of the same rank: for any (possibly infinite) index set $I$,
$$S\otimes_R R^{(I)}\ \cong\ S^{(I)}\qquad\text{as }S\text{-modules},$$
with $S$-basis $\{1\otimes e_i\}_{i\in I}$. In particular $S\otimes_R R^n\cong S^n$, and $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{R}^n\cong\mathbb{C}^n$. Show moreover that for an $R$-linear map $T : R^n\to R^m$, the extended map $\operatorname{id}_S\otimes T : S^n\to S^m$ has the **same matrix** $[T]$ as $T$, now read with entries in $S$ (via $f$).

**Recall:**

![[Def - Restriction and Extension of Scalars#The Definition]]

The extension of an $R$-module $N$ along $f : R\to S$ is the $S$-module $S\otimes_R N$, with $S$ acting on the left factor: $s(s'\otimes n) = (ss')\otimes n$.

![[Def - Free Module#The Definition]]

A [[Def - Free Module|free module]] $R^{(I)} = \bigoplus_{i\in I}R$ has basis $\{e_i\}$. The two ingredients of the proof are distributivity of $\otimes$ over [[Def - Direct Sum of Modules|direct sums]] and the identity law $S\otimes_R R\cong S$:

> [[Thm - Standard Isomorphisms of Tensor Products|Standard isomorphisms]]: $\big(\bigoplus_i M_i\big)\otimes_R P\cong\bigoplus_i(M_i\otimes_R P)$ (distributivity) and $S\otimes_R R\cong S$ via $s\otimes r\mapsto sr$ (identity).

---

# Convergent Strategy

**Problem class.** This is the simplest *compute-an-extension-of-scalars* problem, establishing the most basic and most-used fact about base change: free modules extend to free modules of the same rank, keeping their basis. As the [[Commutative Algebra II — Tensor Products#Problem-Solving Strategy|topic strategy]] records, a free $R$-module to base-change routes through distributivity plus the identity law.

**Assumption pattern.** The trigger is *a free $R$-module $R^{(I)}$* being extended. Freeness is exactly the hypothesis that lets distributivity reduce the problem to a single copy of $R$, where the identity law $S\otimes_R R\cong S$ finishes it. No relations interfere — this is why the free case is the easy case (contrast a quotient like $(\mathbb{Z}/n)\otimes\mathbb{Z}^k$, which combines this with reduction).

**Theorem routing.** The route is two isomorphisms chained: distributivity $S\otimes_R\big(\bigoplus_i R\big)\cong\bigoplus_i(S\otimes_R R)$, then the identity law $S\otimes_R R\cong S$ in each summand, giving $\bigoplus_i S = S^{(I)}$. Tracking the basis: $1\otimes e_i\mapsto e_i\in S^{(I)}$, so $\{1\otimes e_i\}$ is the $S$-basis. For the matrix claim, compute $(\operatorname{id}_S\otimes T)(1\otimes e_i) = 1\otimes Te_i = \sum_\ell[T]_{\ell i}(1\otimes f_\ell)$, reading off the same matrix.

**Key decision point.** The only subtlety is *that the $S$-module structure is respected* — distributivity and the identity law are stated for $R$-modules, and one must confirm the resulting isomorphism is $S$-linear (the $S$-action sits on the left factor throughout, and both isomorphisms move it consistently). The conceptual payoff, worth flagging, is that *the matrix is unchanged*: extension of scalars does nothing to the bookkeeping of a linear map, only to the ring its entries live in — complexifying a real matrix is "the same matrix, now complex".

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra II — Tensor Products#Legal Operations|the topic page's Legal Operations]]:

1. **Push $\otimes$ through a direct sum / use distributivity (operation 6 + standard isomorphisms).** $S\otimes_R\bigoplus_i R\cong\bigoplus_i(S\otimes_R R)$.

2. **Factor an extension of scalars (operation 8).** This is the simplest extension $S\otimes_R(-)$, the building block of the two-step factorisation.

3. **Tensor a map: apply $\operatorname{id}_S\otimes T$ (operation 7).** The extended map keeps the matrix $[T]$.

4. **Build an isomorphism by tracking generators (operation 4).** Confirm $1\otimes e_i\mapsto e_i$ to identify the $S$-basis.

---

# Hints

> [!note]- Hint 1
> $R^{(I)} = \bigoplus_{i\in I}R$. Tensor product distributes over direct sums. What does $S\otimes_R\big(\bigoplus_i R\big)$ become?

> [!note]- Hint 2
> $S\otimes_R\big(\bigoplus_i R\big)\cong\bigoplus_i(S\otimes_R R)$ by distributivity. Now use the identity law $S\otimes_R R\cong S$ in each summand to get $\bigoplus_i S = S^{(I)}$.

> [!note]- Hint 3
> Track the basis through the isomorphism: $1\otimes e_i$ on the left corresponds to the standard basis vector $e_i\in S^{(I)}$ on the right. So $\{1\otimes e_i\}$ is an $S$-basis of $S\otimes_R R^{(I)}$.

> [!note]- Hint 4
> For the matrix claim, apply $\operatorname{id}_S\otimes T$ to the basis tensor $1\otimes e_i$: it gives $1\otimes Te_i = 1\otimes\sum_\ell[T]_{\ell i}f_\ell = \sum_\ell[T]_{\ell i}(1\otimes f_\ell)$. So in the bases $\{1\otimes e_i\}, \{1\otimes f_\ell\}$, the matrix is $[T]$ — unchanged.

---

# Solution

The proof chains two standard isomorphisms and tracks the basis, then computes the extended matrix. Step 1 applies distributivity; Step 2 applies the identity law and reads off the basis; Step 3 computes $\operatorname{id}_S\otimes T$. The conceptual point is that extension keeps the basis and the matrix, changing only the scalars.

**Step 1: Distribute the extension over the direct sum.**

$S\otimes_R R^{(I)}\cong\bigoplus_{i\in I}(S\otimes_R R)$ as $S$-modules.

> [!note]- Derivation
> $R^{(I)} = \bigoplus_{i\in I}R$. By [[Thm - Standard Isomorphisms of Tensor Products|distributivity]] of $\otimes$ over [[Def - Direct Sum of Modules|direct sums]],
> $$S\otimes_R R^{(I)} = S\otimes_R\Big(\bigoplus_{i\in I}R\Big)\cong\bigoplus_{i\in I}(S\otimes_R R),$$
> with $s\otimes(r_i)_i\mapsto(s\otimes r_i)_i$. This isomorphism is $S$-linear: the $S$-action $s'\cdot(s\otimes(r_i)_i) = (s's)\otimes(r_i)_i$ maps to $(s's\otimes r_i)_i = s'\cdot(s\otimes r_i)_i$, since $S$ acts on the left factor coordinatewise.

**Step 2: Collapse each summand by the identity law and read off the basis.**

$\bigoplus_i(S\otimes_R R)\cong\bigoplus_i S = S^{(I)}$, with $S$-basis $\{1\otimes e_i\}$.

> [!note]- Derivation
> The [[Thm - Standard Isomorphisms of Tensor Products|identity law]] gives an $S$-module isomorphism $S\otimes_R R\cong S$, $s\otimes r\mapsto sr$ (it is $S$-linear: $s'(s\otimes r)\mapsto s'sr = s'(sr)$). Applying it in each summand,
> $$\bigoplus_{i\in I}(S\otimes_R R)\cong\bigoplus_{i\in I}S = S^{(I)}.$$
> Chaining with Step 1, $S\otimes_R R^{(I)}\cong S^{(I)}$ as $S$-modules. Tracking the basis tensor $1\otimes e_i$: under distributivity it goes to the element with $1\otimes 1$ in coordinate $i$ and $0$ elsewhere, then under the identity law to the standard basis vector $e_i\in S^{(I)}$. So $\{1\otimes e_i\}_{i\in I}$ is an $S$-basis of $S\otimes_R R^{(I)}$. In particular $S\otimes_R R^n\cong S^n$ and (along $\mathbb{R}\hookrightarrow\mathbb{C}$) $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{R}^n\cong\mathbb{C}^n$.

**Step 3: The extended map keeps the matrix.**

$\operatorname{id}_S\otimes T : S^n\to S^m$ has matrix $[T]$ in the bases $\{1\otimes e_i\}, \{1\otimes f_\ell\}$.

> [!note]- Derivation
> Let $T : R^n\to R^m$ have matrix $[T]$, so $Te_i = \sum_{\ell=1}^m[T]_{\ell i}f_\ell$. By [[Thm - Extension of Scalars and the Adjunction|extension on morphisms]], $\operatorname{id}_S\otimes T$ is $S$-linear, and on the basis tensor
> $$(\operatorname{id}_S\otimes T)(1\otimes e_i) = 1\otimes Te_i = 1\otimes\sum_{\ell=1}^m[T]_{\ell i}f_\ell = \sum_{\ell=1}^m[T]_{\ell i}(1\otimes f_\ell),$$
> using that $1\otimes r f_\ell = r(1\otimes f_\ell) = f(r)(1\otimes f_\ell)$ slides the scalar (image of $[T]_{\ell i}$ under $f$) onto the $S$-factor. So in the $S$-bases $\{1\otimes e_i\}$ and $\{1\otimes f_\ell\}$, the matrix of $\operatorname{id}_S\otimes T$ is $([T]_{\ell i})$ with entries interpreted in $S$ via $f$ — **the same matrix as $T$**. Complexification of a real linear map does not change its matrix, only the field its entries live in.

> [!note]- Complete formal solution
> **Claim.** $S\otimes_R R^{(I)}\cong S^{(I)}$ as $S$-modules, with basis $\{1\otimes e_i\}$, and $\operatorname{id}_S\otimes T$ has matrix $[T]$.
>
> By [[Thm - Standard Isomorphisms of Tensor Products|distributivity]] and the identity law,
> $$S\otimes_R R^{(I)} = S\otimes_R\Big(\bigoplus_{i\in I}R\Big)\cong\bigoplus_{i\in I}(S\otimes_R R)\cong\bigoplus_{i\in I}S = S^{(I)},$$
> all isomorphisms $S$-linear (the $S$-action lives on the left factor and is preserved). The basis tensor $1\otimes e_i$ maps to $e_i\in S^{(I)}$, so $\{1\otimes e_i\}$ is an $S$-basis. For $T : R^n\to R^m$, $(\operatorname{id}_S\otimes T)(1\otimes e_i) = 1\otimes Te_i = \sum_\ell[T]_{\ell i}(1\otimes f_\ell)$, so $[\operatorname{id}_S\otimes T] = [T]$ over $S$. In particular $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{R}^n\cong\mathbb{C}^n$ and complexification preserves matrices. $\blacksquare$

---

# Key Takeaways

**Extension of scalars sends free to free of the same rank, keeping the basis — base change of a free module is "rebase the scalars".** The clean lesson is that $S\otimes_R R^n\cong S^n$ with basis $\{1\otimes e_i\}$: extending a free module along $f : R\to S$ does nothing structural, it just replaces the scalar ring. The trigger for spaced recall: whenever a free module is base-changed (complexified, reduced mod $p$, localized), the answer is the free module of the same rank over the new ring, with the *same basis indices*. This is the simplest and most-used base-change fact, and it is the foundation of the two-step factorisation $M\otimes_R N\cong M\otimes_S(S\otimes_R N)$ — preparing a free $N$ by $S\otimes_R N = S^{\operatorname{rank}}$ is free.

**Matrices are base-change invariant — complexifying a linear map keeps the matrix, only the entries' home ring changes.** The matrix claim is the practically important half: $\operatorname{id}_S\otimes T$ has the *same* matrix $[T]$ as $T$, with entries reinterpreted in $S$ via $f$. So complexification of a real operator, reduction of an integer matrix mod $p$, or any base change of a linear map is computed by "read the same matrix over the new ring". The transferable diagnostic: when a problem base-changes a linear map and asks for its matrix, the answer is the original matrix with entries pushed through $f$ — no recomputation. This is why eigenvalue and rank computations transfer cleanly under base change (the matrix is unchanged), and it is the concrete content behind "complexification preserves the characteristic polynomial".

**Freeness is what makes base change easy; relations are what make it interesting.** The reason this exercise is rated ⭐ while $(\mathbb{Z}/n)\otimes\mathbb{Z}^k$ or $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ are harder is that *free modules have no relations to interfere with distributivity*. Once a module is presented with relations — as a quotient $R^m/\operatorname{im}(R^n)$ — base change must track what happens to the relations (right-exactness, the kernel may grow or shrink, flatness becomes relevant). The diagnostic for spaced practice: when base-changing, first ask "is the module free?"; if so, the answer is immediate ($S^{\operatorname{rank}}$); if not, present it by generators and relations and base-change the presentation, watching for the failure of injectivity that signals non-flatness. This is the bridge from the easy free case here to the exactness theory of [[Commutative Algebra III — Flatness and Exactness]], and to the general two-step factorisation on [[Thm - Extension of Scalars and the Adjunction]].
