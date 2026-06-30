---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Levi-Civita Tensor"
  - "Def - Metric Duality and Index Manipulation"
tags: [physics, special-relativity]
---

# Problem Statement

Work in an orthonormal frame, mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, $c = 1$.

1. Establish that $\varepsilon_{0123} = +1$ in a right-handed orthonormal frame, and that this value is the same in *both* metric signatures.
2. Show that raising all four indices flips the sign: $\varepsilon^{0123} = -1$. Identify precisely where the sign comes from.
3. Prove the full-contraction identity $\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\mu\nu\rho\sigma} = -24$ by counting signed permutations.
4. Derive the once-uncontracted identity $\varepsilon^{\mu\nu\rho\alpha}\varepsilon_{\mu\nu\rho\beta} = -6\,\delta^\alpha{}_\beta$, and check consistency with part 3 by contracting $\alpha = \beta$.

**Recall:**

![[Def - The Levi-Civita Tensor#The Definition]]

The [[Def - The Levi-Civita Tensor|Levi-Civita tensor]] has components $\varepsilon_{\alpha\beta\gamma\delta} = \pm\sqrt{-\det g}\,[\alpha,\beta,\gamma,\delta]$, with the Levi-Civita *symbol* $[\alpha,\beta,\gamma,\delta] = \mathrm{sgn}$ of the permutation (or $0$ for a repeat). In an orthonormal frame $\det g = \det\eta = -1$. Raising indices uses the inverse metric $\eta^{\mu\nu}$; see [[Def - Metric Duality and Index Manipulation|metric duality]].

---

# Convergent Strategy

**Problem class.** A *structural / counting* problem establishing the [[Def - The Levi-Civita Tensor|Levi-Civita]] components and contraction identities — the algebraic engine of all Hodge computations. The [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality#Problem-Solving Strategy|topic strategy]]: work in an orthonormal frame where $\sqrt{-\det g} = 1$, and count signed permutations.

**Assumption pattern.** In an orthonormal frame, $\sqrt{-\det g} = 1$, so the tensor components equal the symbol. Raising an index multiplies by the diagonal $\eta$ entry; the four-fold raising introduces $\det\eta = -1$. The contraction identities are pure combinatorics of $\mathfrak{S}_4$ dressed with the signature sign.

**Theorem routing.** Part 1: $\det\eta = -1$ in both signatures, so $\sqrt{-\det g} = 1$ and $\varepsilon_{0123} = +1$. Part 2: $\varepsilon^{0123} = \eta^{00}\eta^{11}\eta^{22}\eta^{33}\varepsilon_{0123} = \det\eta\cdot\varepsilon_{0123} = -1$. Part 3: $\sum$ over the $4! = 24$ nonzero permutations of $\varepsilon^{\dots}\varepsilon_{\dots} = (\text{sign})^2 = +1$ each, times the overall sign from raising. Part 4: leave one index free and count the $3! = 6$ permutations of the contracted indices.

**Key decision point.** The crux is part 2's sign: $\varepsilon^{0123} = -1$ while $\varepsilon_{0123} = +1$, and the difference is the determinant of $\eta$ acquired in raising four indices. Because $\det\eta = -1$ holds in *both* signatures, this sign flip is convention-independent — the $-24, -6, \dots$ in the contraction identities are robust. Recognising that the signs trace to $\mathrm{sgn}(\det g) = -1$, not to the individual signature, is the lesson.

---

# Legal Operations Used

1. **Operation 8 from the topic page (reduce a product of two $\varepsilon$'s to Kronecker deltas).** Parts 3 and 4 establish the foundational cases of this reduction.

2. **Operation 1 from the topic page (raise/lower with the metric).** Part 2 raises all four indices of $\varepsilon$ to get the sign flip.

---

# Hints

> [!note]- Hint 1
> $\det g = \det\eta$. In mostly-minus, $\det\eta = (1)(-1)(-1)(-1) = -1$; in mostly-plus, $\det\eta = (-1)(1)(1)(1) = -1$. Either way $\det g = -1 < 0$, so $\sqrt{-\det g} = 1$ and $\varepsilon_{0123} = +1\cdot[0,1,2,3] = +1$.

> [!note]- Hint 2
> $\varepsilon^{0123} = \eta^{0\mu}\eta^{1\nu}\eta^{2\rho}\eta^{3\sigma}\varepsilon_{\mu\nu\rho\sigma}$. The diagonal $\eta$ collapses each sum: $= \eta^{00}\eta^{11}\eta^{22}\eta^{33}\varepsilon_{0123} = (1)(-1)(-1)(-1)(+1) = -1$. The product of the four diagonal entries is $\det\eta = -1$.

> [!note]- Hint 3
> $\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\mu\nu\rho\sigma} = \sum_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\mu\nu\rho\sigma}$. Only the $4! = 24$ permutations of $(0,1,2,3)$ contribute. For each, $\varepsilon^{\mu\nu\rho\sigma} = -[\mu\nu\rho\sigma]$ and $\varepsilon_{\mu\nu\rho\sigma} = +[\mu\nu\rho\sigma]$, so the product is $-[\mu\nu\rho\sigma]^2 = -1$. Summing $24$ terms of $-1$ gives $-24$.

---

# Solution

The Levi-Civita components and contraction identities are pure combinatorics in an orthonormal frame. The plan: fix $\varepsilon_{0123} = +1$ and note its signature-independence (Step 1), get the raised sign $\varepsilon^{0123} = -1$ from $\det\eta$ (Step 2), count $24$ permutations for the full contraction (Step 3), and count $6$ for the once-uncontracted identity (Step 4).

**Step 1: $\varepsilon_{0123} = +1$, the same in both signatures.**

> [!note]- Derivation
> The [[Def - The Levi-Civita Tensor|Levi-Civita]] components are $\varepsilon_{\alpha\beta\gamma\delta} = \sqrt{-\det g}\,[\alpha,\beta,\gamma,\delta]$ in a right-handed frame. Compute $\det g = \det\eta$:
> - *Mostly-minus:* $\det\eta = (+1)(-1)(-1)(-1) = -1$.
> - *Mostly-plus:* $\det\eta = (-1)(+1)(+1)(+1) = -1$.
>
> In both cases $\det g = -1 < 0$, so $\sqrt{-\det g} = \sqrt{1} = 1$, and
> $$\varepsilon_{0123} = 1\cdot[0,1,2,3] = 1\cdot(+1) = +1.$$
> The lowered top component is $+1$ regardless of signature. This is the first half of why the chapter's formulas are signature-robust: the *lowered* Levi-Civita tensor does not see the convention.

**Step 2: $\varepsilon^{0123} = -1$, from $\det\eta = -1$.**

> [!note]- Derivation
> Raise all four indices with the inverse metric $\eta^{\mu\nu}$ (diagonal, so each sum collapses):
> $$\varepsilon^{0123} = \eta^{0\mu}\eta^{1\nu}\eta^{2\rho}\eta^{3\sigma}\varepsilon_{\mu\nu\rho\sigma} = \eta^{00}\eta^{11}\eta^{22}\eta^{33}\,\varepsilon_{0123} = (1)(-1)(-1)(-1)\cdot(+1) = -1.$$
> The factor $\eta^{00}\eta^{11}\eta^{22}\eta^{33} = \det\eta = -1$ is exactly the determinant of the (inverse) metric, picked up once per raised index. Since $\det\eta = -1$ in *both* signatures, $\varepsilon^{0123} = -1$ is convention-independent. So the raised and lowered top components have *opposite* sign — a fact that must be tracked carefully in every Hodge-star computation.

**Step 3: $\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\mu\nu\rho\sigma} = -24$.**

> [!note]- Derivation
> The contraction sums over all four indices:
> $$\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\mu\nu\rho\sigma} = \sum_{\mu,\nu,\rho,\sigma = 0}^{3}\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\mu\nu\rho\sigma}.$$
> A term is nonzero only when $(\mu,\nu,\rho,\sigma)$ is a permutation of $(0,1,2,3)$ — there are $4! = 24$ such. For each permutation $\pi$, $\varepsilon_{\mu\nu\rho\sigma} = [\mu\nu\rho\sigma] = \mathrm{sgn}(\pi)$ and $\varepsilon^{\mu\nu\rho\sigma} = -[\mu\nu\rho\sigma] = -\mathrm{sgn}(\pi)$ (the raised tensor carries the extra $-1$ from Step 2). So each term is
> $$\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\mu\nu\rho\sigma} = (-\mathrm{sgn}(\pi))(\mathrm{sgn}(\pi)) = -\mathrm{sgn}(\pi)^2 = -1.$$
> Summing the $24$ nonzero terms:
> $$\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\mu\nu\rho\sigma} = 24\times(-1) = -24 = -4!.$$
> The magnitude $24 = 4!$ counts the permutations; the sign $-1$ is $\mathrm{sgn}(\det g)$, the Lorentzian fingerprint. (In a Euclidean $4$-space, $\det g = +1$, this would be $+24$.)

**Step 4: $\varepsilon^{\mu\nu\rho\alpha}\varepsilon_{\mu\nu\rho\beta} = -6\,\delta^\alpha{}_\beta$.**

> [!note]- Derivation
> Now contract only three indices, leaving $\alpha$ (up) and $\beta$ (down) free. A term is nonzero only when $\{\mu,\nu,\rho,\alpha\}$ and $\{\mu,\nu,\rho,\beta\}$ are both permutations of $\{0,1,2,3\}$. Since $\mu,\nu,\rho$ are shared, this forces $\alpha = \beta$ (both equal the one index missing from $\{\mu,\nu,\rho\}$). So the result is proportional to $\delta^\alpha{}_\beta$:
> $$\varepsilon^{\mu\nu\rho\alpha}\varepsilon_{\mu\nu\rho\beta} = c\,\delta^\alpha{}_\beta.$$
> To find $c$, fix $\alpha = \beta$ (say $\alpha = \beta = 0$) and sum: $\{\mu,\nu,\rho\}$ ranges over the $3! = 6$ permutations of $\{1,2,3\}$, and for each, $\varepsilon^{\mu\nu\rho 0}\varepsilon_{\mu\nu\rho 0} = (-\mathrm{sgn})(\mathrm{sgn}) = -1$ (as in Step 3). So $\sum = 6\times(-1) = -6$, giving $c = -6$:
> $$\varepsilon^{\mu\nu\rho\alpha}\varepsilon_{\mu\nu\rho\beta} = -6\,\delta^\alpha{}_\beta.$$
> *Consistency check.* Contract $\alpha = \beta$: $\varepsilon^{\mu\nu\rho\alpha}\varepsilon_{\mu\nu\rho\alpha} = -6\,\delta^\alpha{}_\alpha = -6\times 4 = -24$, matching Step 3. The chain continues: $\varepsilon^{\mu\nu\alpha\beta}\varepsilon_{\mu\nu\gamma\delta} = -2(\delta^\alpha{}_\gamma\delta^\beta{}_\delta - \delta^\alpha{}_\delta\delta^\beta{}_\gamma)$, and so on, each step dividing the magnitude by $(4 - p)$ and exposing more Kronecker structure.

> [!note]- Complete formal solution
> **(1)** $\det\eta = -1$ in both signatures, so $\sqrt{-\det g} = 1$ and $\varepsilon_{0123} = +1$.
> **(2)** $\varepsilon^{0123} = \eta^{00}\eta^{11}\eta^{22}\eta^{33}\varepsilon_{0123} = (\det\eta)(+1) = -1$.
> **(3)** The $4! = 24$ permutations each give $\varepsilon^{\dots}\varepsilon_{\dots} = -\mathrm{sgn}^2 = -1$, so $\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\mu\nu\rho\sigma} = -24$.
> **(4)** Three contracted indices force $\alpha = \beta$; fixing $\alpha = \beta$ and summing the $3! = 6$ permutations gives $-6$, so $\varepsilon^{\mu\nu\rho\alpha}\varepsilon_{\mu\nu\rho\beta} = -6\delta^\alpha{}_\beta$; contracting back gives $-6\cdot4 = -24$, consistent. $\blacksquare$

---

# Key Takeaways

**The lowered Levi-Civita tensor is signature-blind; only raising sees the convention.** The component $\varepsilon_{0123} = +1$ is the same in mostly-plus and mostly-minus, because $\det g = -1$ in both, so $\sqrt{-\det g} = 1$. The sign flip to $\varepsilon^{0123} = -1$ comes entirely from raising four indices, which multiplies by $\det\eta = -1$ — and that determinant is also $-1$ in both signatures. The reusable consequence is that *every* Levi-Civita contraction identity ($-24$, $-6$, $-2$, $\dots$) is convention-independent: its sign is $\mathrm{sgn}(\det g) = -1$, a property of the Lorentzian *signature* (one timelike direction), not of the sign convention. This is why one can transcribe Gourgoulhon's mostly-plus formulas to mostly-minus unchanged — the Levi-Civita machinery does not flip. The diagnostic: whenever a sign in a Hodge or $\varepsilon$ computation looks convention-dependent, check whether it traces to $\det g$; if so, it is robust, because $\det g < 0$ for any Lorentzian metric.

**Two epsilons collapse to Kronecker deltas, and the magnitude is the factorial of the contracted count.** The identity $\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\mu\nu\rho\sigma} = -24 = -4!$, and its partial contractions $-6 = -3!$ (one free pair), $-2 = -2!$ (two free pairs), encode a simple rule: contracting $k$ index pairs of two Levi-Civita tensors gives $-k!$ times the generalised Kronecker delta on the remaining indices. The minus is the Lorentzian signature; the $k!$ counts the orderings of the contracted dummy indices. This is the four-dimensional, signature-dressed version of the vector-calculus $\epsilon$–$\delta$ identity $\epsilon_{ijk}\epsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}$. The reusable move is to *never* compute with two explicit $\varepsilon$'s — replace $\varepsilon\varepsilon$ by the signed delta combination immediately, and the Kronecker deltas then contract the surrounding sums. This single substitution is what makes the proof of $\star\star = (-1)^{p+1}$, every cross-product identity, and every field-invariant computation finite.

**The consistency check — contracting a partial identity back to the full one — is the way to verify Levi-Civita gymnastics.** The relation $\varepsilon^{\mu\nu\rho\alpha}\varepsilon_{\mu\nu\rho\beta} = -6\delta^\alpha{}_\beta$, contracted on $\alpha = \beta$, must reproduce $-6\cdot4 = -24$, matching the full contraction. This self-consistency (each partial identity must reduce to the next more-contracted one) is the standard way to catch errors in the signs and factorials of $\varepsilon$ identities, and it is worth performing whenever you write one down. The general pattern: the once-uncontracted identity carries a factor $(4-p)! = 3! = 6$ for $p = 1$ free pair, and contracting the free index multiplies by $\delta^\alpha{}_\alpha = 4$ to recover the more-contracted factor. Knowing these factorials and the trace $\delta^\alpha{}_\alpha = 4$ lets you reconstruct any Levi-Civita contraction identity from scratch, and verify it by contracting back down to $-24$ — a robust check that requires no memorisation beyond "the sign is $-1$ and the magnitude is a factorial."
