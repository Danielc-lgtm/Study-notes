---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Compact Weak Generator"
  - "Def - Chain Map and Chain Homotopy"
  - "Def - Module"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $R$ be a [[Def - Ring|ring]] and $D(R)$ its [[Def - Chain Map and Chain Homotopy|derived category]]. Regard $R$ as a complex concentrated in degree $0$. Show that $R$ is a [[Def - Compact Weak Generator|compact weak generator]] of $D(R)$:

(a) **Computation of the detector.** For any complex $X$, $[\Sigma^n R, X] = [R[n], X] \cong H_n(X)$, the $n$-th homology.

(b) **Generation.** If $H_n(X) = 0$ for all $n$ (i.e. $X$ is acyclic), then $X \cong 0$ in $D(R)$.

(c) **Compactness.** $[R, -] = H_0$ commutes with direct sums of complexes.

Conclude that $\mathrm{End}(R) = R$ (an ordinary ring, with no higher homotopy), so the recognition theorem returns the tautology that $D(R)$ is "modules over $R$."

**Recall:**

![[Def - Compact Weak Generator#The Definition]]

In $D(R)$, a complex $X$ is isomorphic to $0$ iff it is **acyclic** ($H_n(X) = 0$ for all $n$), because quasi-isomorphisms are inverted. The shift $R[n]$ is $R$ placed in degree $n$.

---

# Convergent Strategy

**Problem class:** This is an "identify the generator" problem, the §3 target, run in the simplest possible case ($D(R)$) where every step is explicit homology.

**Assumption pattern:** The resource is that maps out of $R[n]$ compute homology — $[R[n], X] = H_n(X)$ — so both generation and the detector computation are immediate from this single identity. Compactness rests on homology commuting with direct sums, an elementary fact.

**Theorem routing:** Compute $[R[n], X] = H_n(X)$ (maps out of the free module on one generator evaluate, and the shift selects degree $n$); generation follows because acyclic complexes are zero in $D(R)$; compactness follows because $H_0$ commutes with direct sums. The conclusion routes through Schwede–Shipley with $\mathrm{End}(R) = R$.

**Key decision point:** The non-obvious step is the homology computation $[R[n], X] \cong H_n(X)$ in the *derived* category — one must use that $R$ is projective (so chain-homotopy classes of maps out of $R[n]$ already compute homology, with no need for resolutions). Recognizing that projectivity of $R$ is what makes the computation work is the crux.

---

# Legal Operations Used

1. **Operation 7 from the topic page (test or exhibit a weak generator).** Both halves are carried out for $G = R$.

2. **Operation 4 from the topic page (suspend or desuspend).** The shifts $R[n]$ access all homological degrees, which is what generation requires.

---

# Hints

> [!note]- Hint 1
> A map of complexes out of $R$ (in degree $0$) is determined by where the generator $1 \in R$ goes, i.e. by an element of $X_0$ that is a cycle; up to chain homotopy this is exactly a homology class. So $[R, X] = H_0(X)$. Shifting, $[R[n], X] = H_n(X)$.

> [!note]- Hint 2
> $R$ is projective (it is free of rank $1$), so no projective resolution is needed: chain-homotopy classes of maps already compute the derived hom. This is why the naive computation in Hint 1 is valid in $D(R)$, not just in the homotopy category of complexes.

> [!note]- Hint 3
> For compactness, homology commutes with direct sums: $H_0(\bigoplus_i X_i) = \bigoplus_i H_0(X_i)$, because a direct sum of complexes has its homology the direct sum of the homologies (cycles and boundaries are computed degreewise, and direct sums are exact).

---

# Solution

The plan: compute the detector as homology using projectivity of $R$; generation and compactness then follow immediately; conclude with $\mathrm{End}(R) = R$.

**Step 1 (part a): $[\Sigma^n R, X] \cong H_n(X)$.**

> [!note]- Derivation
> Since $R$ is free of rank $1$ (hence projective), a chain map $R \to X$ (with $R$ in degree $0$) is determined by the image of $1 \in R$, which must be a $0$-cycle $z \in Z_0(X) = \ker(d \colon X_0 \to X_{-1})$. Two such maps are chain-homotopic iff their cycles differ by a boundary. So $[R, X]$ (chain-homotopy classes, which compute the derived hom because $R$ is projective) is $Z_0(X)/B_0(X) = H_0(X)$. Applying the shift, $[\Sigma^n R, X] = [R[n], X] = H_n(X)$.

**Step 2 (part b): Generation.**

> [!note]- Derivation
> Suppose $[\Sigma^n R, X] = 0$ for all $n$. By Step 1, $H_n(X) = 0$ for all $n$, i.e. $X$ is acyclic. In $D(R)$ a complex is isomorphic to $0$ iff it is acyclic (the map $X \to 0$ is then a quasi-isomorphism, hence an isomorphism in $D(R)$). Therefore $X \cong 0$, and $R$ is a weak generator.

**Step 3 (part c): Compactness.**

> [!note]- Derivation
> For any family $\{X_i\}$, the direct sum $\bigoplus_i X_i$ has homology $H_n(\bigoplus_i X_i) = \bigoplus_i H_n(X_i)$: cycles and boundaries are computed degreewise, and a direct sum of cycles is a cycle, a direct sum of boundaries a boundary, with no interaction across summands. By Step 1 this says $[R[n], \bigoplus_i X_i] = \bigoplus_i [R[n], X_i]$, so $[R, -]$ commutes with direct sums and $R$ is compact.

**Step 4: $\mathrm{End}(R) = R$ and the conclusion.**

> [!note]- Derivation
> The endomorphism object is $[\Sigma^n R, R] = H_n(R) = R$ if $n = 0$ and $0$ otherwise (the complex $R$ has homology $R$ in degree $0$ only). So $\mathrm{End}(R)$ is concentrated in degree $0$ with $\pi_0 = R$: it is the *ordinary ring* $R$, with **no higher homotopy** (the Eilenberg–MacLane case). The Schwede–Shipley recognition theorem then returns the tautology that $D(R) \simeq$ modules over $R$ in the classical sense. This is the degenerate pole of the recognition theorem, to be contrasted with $\mathcal{SH}$ where $\mathrm{End}(\mathbb{S}) = \mathbb{S}$ has rich higher homotopy.

> [!note]- Complete formal solution
> *Detector.* $R$ is projective, so $[R[n], X]$ (derived hom $=$ chain-homotopy classes) is $H_n(X)$: a map out of $R[n]$ is a degree-$n$ cycle up to boundary.
>
> *Generation.* If all $[R[n], X] = H_n(X)$ vanish then $X$ is acyclic, hence $\cong 0$ in $D(R)$. So $R$ generates.
>
> *Compactness.* Homology commutes with direct sums, so $[R, \bigoplus_i X_i] = H_0(\bigoplus_i X_i) = \bigoplus_i H_0(X_i) = \bigoplus_i [R, X_i]$. So $R$ is compact.
>
> *Conclusion.* $[\Sigma^n R, R] = H_n(R)$ is $R$ for $n=0$ and $0$ otherwise, so $\mathrm{End}(R) = R$ is an ordinary ring; Schwede–Shipley gives the tautology $D(R) \simeq \mathrm{Mod}_R$. $\blacksquare$

---

# Key Takeaways

**Maps out of the free module compute homology, and this is why $R$ generates its derived category.** The identity $[R[n], X] = H_n(X)$ is the derived-category version of "$\mathrm{Hom}_R(R, M) = M$," and it is the engine of the whole exercise: generation is "homology detects acyclicity," compactness is "homology commutes with sums." The trigger to remember: in any module-like setting, the free module on one generator is the natural candidate generator, and maps out of it *evaluate* — in the derived world, evaluation becomes homology. Projectivity of the generator is what lets you skip resolutions and compute the derived hom directly.

**$D(R)$ is the degenerate pole of Schwede–Shipley, where the ring spectrum is an ordinary ring.** This exercise is the calibration counterpart to the sphere-spectrum exercise: there $\mathrm{End}(\mathbb{S}) = \mathbb{S}$ had infinitely many nonzero homotopy groups; here $\mathrm{End}(R) = R$ has exactly one. The transferable diagnostic: a triangulated category is "ordinary algebra" precisely when its compact generator's endomorphism ring spectrum has no higher homotopy, and $D(R)$ is the universal such example. Recognizing when $\mathrm{End}(G)$ collapses to a ring tells you when homotopical machinery is overkill and classical homological algebra suffices.

**Compactness in $D(R)$ for the generator $R$ is elementary, but compactness for general objects is subtle and important.** While $R$ is obviously compact (homology commutes with sums), a general complex is compact in $D(R)$ iff it is a **perfect complex** (quasi-isomorphic to a bounded complex of finitely generated projectives) — a genuinely restrictive condition. The lesson to carry forward: do not over-generalize from the easy case; the generator is compact for elementary reasons, but characterizing *all* compact objects is the start of the theory of perfect complexes, dualizable objects, and the relationship between compactness and finiteness that governs duality in $D(R)$.
