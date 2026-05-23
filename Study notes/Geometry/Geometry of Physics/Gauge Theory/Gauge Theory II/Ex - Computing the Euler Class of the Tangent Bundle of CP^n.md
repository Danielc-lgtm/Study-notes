---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Gauss-Bonnet-Chern Theorem"
  - "Def - The Euler Class of a Real Oriented Vector Bundle"
  - "Def - The Hopf Bundle"
tags: [geometry, gauge-theory, characteristic-classes, projective-spaces]
---

# Problem Statement

Show that
$$\int_{\mathbb{CP}^n} e(T\mathbb{CP}^n) \;=\; n + 1 \;=\; \chi(\mathbb{CP}^n),$$
where $e(T\mathbb{CP}^n)$ is the Euler class of the (real) tangent bundle of complex projective $n$-space.

Use two methods:

**(a) The CW-decomposition method.** Use the standard CW-structure on $\mathbb{CP}^n$ (one cell in each even dimension $0, 2, 4, \ldots, 2n$) to compute the Euler characteristic directly as the alternating sum of cell counts.

**(b) The Chern-class method.** Use the splitting principle / Chern-class formula
$$c(T\mathbb{CP}^n) = (1 + h)^{n+1}/(1+0) = (1+h)^{n+1},$$
where $h \in H^2(\mathbb{CP}^n; \mathbb{Z})$ is the hyperplane class (i.e., $c_1$ of the dual of the tautological line bundle $\mathcal{O}(1)$), to extract the top Chern class $c_n(T\mathbb{CP}^n) = e(T\mathbb{CP}^n)$, then integrate over $\mathbb{CP}^n$.

**Recall:**

![[Thm - Gauss-Bonnet-Chern Theorem#Statement]]

![[Def - The Euler Class of a Real Oriented Vector Bundle#The Definition]]

The complex projective space $\mathbb{CP}^n = (\mathbb{C}^{n+1}\setminus\{0\})/\mathbb{C}^*$ has $H^*(\mathbb{CP}^n; \mathbb{Z}) = \mathbb{Z}[h]/(h^{n+1})$, with $h \in H^2(\mathbb{CP}^n;\mathbb{Z})$ the **hyperplane class** ($c_1$ of $\mathcal{O}(1) = H_1$, the dual of the tautological line bundle).

The Chern classes of a holomorphic vector bundle $V$ are $c(V) = 1 + c_1(V) + c_2(V) + \cdots + c_{\mathrm{rk}}(V) \in H^*(M)$.

---

# Convergent Strategy

**Problem class:** *Compute a characteristic class on a specific manifold via two complementary methods.* The topic-page strategy uses both the topological route (CW-decomposition) and the geometric route (Chern-class formula + integration).

**Assumption pattern:** The key assumption is that $\mathbb{CP}^n$ has a *simple* cell structure (one cell per even dimension), which gives the Euler characteristic combinatorially. For (b), the assumption is the **Euler sequence** of $\mathbb{CP}^n$: $0 \to \mathcal{O} \to \mathcal{O}(1)^{\oplus (n+1)} \to T\mathbb{CP}^n \to 0$, which gives the Chern-class identity via multiplicativity of the total Chern class.

**Theorem routing:** [[Thm - Gauss-Bonnet-Chern Theorem]] guarantees $\int e(T\mathbb{CP}^n) = \chi(\mathbb{CP}^n)$. The CW-decomposition gives the LHS combinatorially; the Chern-class formula gives it via $c_n(T\mathbb{CP}^n) \in H^{2n}(\mathbb{CP}^n;\mathbb{Z}) = \mathbb{Z}$.

**Key decision point:** For (b), the non-obvious step is deriving the Chern-class formula from the Euler sequence. The whole computation relies on the multiplicative property $c(A \oplus B) = c(A) \cdot c(B)$ of the total Chern class, applied to the Euler sequence after recognizing it as a short exact sequence of vector bundles.

---

# Legal Operations Used

1. **Operation 7 from the topic page (Use Kronecker indices for Euler characteristic).** Combined with the explicit Morse function on $\mathbb{CP}^n$, gives $\chi$ as a count.

2. **Operation 4 from the topic page (Use Pfaffian / invariant polynomial of curvature).** Specialized to Chern classes via Chern-Weil; integrate $c_n(T\mathbb{CP}^n)$ over $\mathbb{CP}^n$.

3. **Operation 1 from the topic page (Pass between bundle and frame bundle).** Apply: $T\mathbb{CP}^n$ has natural complex structure, so its frame bundle is principal $\mathrm{GL}(n, \mathbb{C})$, and characteristic classes pull back from $BU(n)$.

---

# Hints

> [!note]- Hint 1
> For (a), the CW structure on $\mathbb{CP}^n$ has cells $\mathbb{CP}^0, \mathbb{CP}^1 \setminus \mathbb{CP}^0 \cong \mathbb{R}^2$, $\mathbb{CP}^2 \setminus \mathbb{CP}^1 \cong \mathbb{R}^4$, ..., $\mathbb{CP}^n \setminus \mathbb{CP}^{n-1} \cong \mathbb{R}^{2n}$ — one cell in each even dimension $0, 2, 4, \ldots, 2n$, total $n+1$ cells.

> [!note]- Hint 2
> For (b), the Euler sequence is the short exact sequence $0 \to \mathcal{O} \to \mathcal{O}(1)^{n+1} \to T\mathbb{CP}^n \to 0$ of holomorphic vector bundles. Applying the multiplicative property of Chern classes gives $c(\mathcal{O}) \cdot c(T\mathbb{CP}^n) = c(\mathcal{O}(1)^{n+1}) = (1+h)^{n+1}$, and $c(\mathcal{O}) = 1$, so $c(T\mathbb{CP}^n) = (1+h)^{n+1}$.

> [!note]- Hint 3
> The top Chern class of a rank-$n$ complex bundle is the $h^n$-coefficient of the total Chern class (since the bundle is over a $2n$-dim base, higher classes vanish). Extract from $(1+h)^{n+1}$.

> [!note]- Hint 4
> For (b), $c_n(T\mathbb{CP}^n) = \binom{n+1}{n}h^n = (n+1)h^n$. Integrate: $\int_{\mathbb{CP}^n} h^n = 1$ (the fundamental class of $\mathbb{CP}^n$ is dual to $h^n$). So $\int e = (n+1) \cdot 1 = n+1$.

---

# Solution

The proof has two methods. Method (a) uses topology: count cells. Method (b) uses geometry/algebra: Chern-class formula. Both give $\chi(\mathbb{CP}^n) = n + 1$, confirming Gauss-Bonnet-Chern. The non-obvious move in (b) is the derivation of the Chern-class formula from the Euler sequence — a beautiful application of multiplicativity.

**Method (a): CW-decomposition.**

> [!note]- Derivation
> $\mathbb{CP}^n$ has a CW-decomposition with exactly one cell in each even dimension $0, 2, 4, \ldots, 2n$:
> - The $0$-cell is a single point ($\mathbb{CP}^0 = \mathrm{pt}$).
> - The $2k$-cell is $\mathbb{CP}^k \setminus \mathbb{CP}^{k-1} \cong \mathbb{C}^k \cong \mathbb{R}^{2k}$, for $k = 1, 2, \ldots, n$.
>
> So the cell count by dimension: $1$ cell in dimension $0$, $0$ cells in dimension $1$, $1$ cell in dimension $2$, $0$ cells in dimension $3$, ..., $1$ cell in dimension $2n$. Total: $n + 1$ even-dimensional cells, $0$ odd-dimensional cells.
>
> Euler characteristic via alternating sum:
> $$\chi(\mathbb{CP}^n) = \sum_k (-1)^k (\text{number of $k$-cells}) = 1 + 0 + 1 + 0 + \cdots + 1 = n + 1.$$
>
> By [[Thm - Gauss-Bonnet-Chern Theorem]], $\int_{\mathbb{CP}^n}e(T\mathbb{CP}^n) = \chi(\mathbb{CP}^n) = n + 1$. ✓

**Method (b): Chern-class formula via the Euler sequence.**

> [!note]- Derivation: The Euler sequence
> Recall the tautological line bundle $\mathcal{O}(-1) =$ the line bundle whose fibre over $[z_0 : \ldots : z_n] \in \mathbb{CP}^n$ is the line through $(z_0, \ldots, z_n)$ in $\mathbb{C}^{n+1}$. Its dual is $\mathcal{O}(1) = \mathcal{O}(-1)^*$.
>
> The **Euler sequence** is the short exact sequence of holomorphic vector bundles on $\mathbb{CP}^n$:
> $$0 \;\to\; \mathcal{O} \;\to\; \mathcal{O}(1)^{\oplus(n+1)} \;\to\; T\mathbb{CP}^n \;\to\; 0,$$
> where $\mathcal{O} = \mathbb{CP}^n \times \mathbb{C}$ is the trivial line bundle. The first map sends $1 \in \mathcal{O}$ to the section $(z_0, z_1, \ldots, z_n) \mapsto (z_0\xi^0, z_1\xi^0, \ldots, z_n\xi^0)$ scaled by the appropriate trivializations; the second is the quotient. Geometrically, $T\mathbb{CP}^n$ is the "tangent space at $[z]$" which is identified with $T_{[z]}\mathbb{CP}^n = \{w \in \mathbb{C}^{n+1} : w \perp z\} / \mathbb{C}\cdot z = \mathrm{Hom}(\mathbb{C}\cdot z, \mathbb{C}^{n+1}/\mathbb{C}\cdot z)$ — the tangent direction to varying $[z]$ in $\mathbb{CP}^n$.

> [!note]- Derivation: Total Chern class formula
> Apply multiplicativity of the total Chern class to the Euler sequence: for an exact sequence $0 \to A \to B \to C \to 0$, $c(B) = c(A) \cdot c(C)$. Therefore
> $$c(\mathcal{O}(1)^{\oplus(n+1)}) = c(\mathcal{O}) \cdot c(T\mathbb{CP}^n).$$
> Now $c(\mathcal{O}) = 1$ (trivial bundle has trivial total Chern class), and $c(\mathcal{O}(1)) = 1 + h$ where $h = c_1(\mathcal{O}(1)) \in H^2(\mathbb{CP}^n; \mathbb{Z})$ is the hyperplane class. By multiplicativity for direct sums (or the Whitney sum formula), $c(\mathcal{O}(1)^{\oplus(n+1)}) = (1+h)^{n+1}$.
>
> Therefore $c(T\mathbb{CP}^n) = (1+h)^{n+1}$.

> [!note]- Derivation: Top Chern class
> The top Chern class is the highest-degree piece of $c(T\mathbb{CP}^n)$ that fits in $H^{2n}(\mathbb{CP}^n; \mathbb{Z}) = \mathbb{Z}\cdot h^n$:
> $$c_n(T\mathbb{CP}^n) = [\text{coefficient of $h^n$ in } (1+h)^{n+1}] \cdot h^n = \binom{n+1}{n}h^n = (n+1)h^n.$$

> [!note]- Derivation: Integration
> For a closed oriented manifold $M$ of dimension $2n$, $\int_M h^n = 1$ if $h^n$ is the generator of $H^{2n}(M; \mathbb{Z})$ matched to the fundamental class $[M]$ — and for $\mathbb{CP}^n$ this is exactly the case: $H^{2n}(\mathbb{CP}^n; \mathbb{Z}) = \mathbb{Z} \cdot h^n$ and $\int_{\mathbb{CP}^n} h^n = 1$.
>
> So
> $$\int_{\mathbb{CP}^n} e(T\mathbb{CP}^n) = \int_{\mathbb{CP}^n} c_n(T\mathbb{CP}^n) = (n+1) \int_{\mathbb{CP}^n} h^n = (n+1) \cdot 1 = n + 1. \checkmark$$

> [!note]- Complete formal solution
> **Method (a):** $\mathbb{CP}^n$ has CW-decomposition $\mathrm{pt} \subset \mathbb{CP}^1 \subset \mathbb{CP}^2 \subset \cdots \subset \mathbb{CP}^n$, with one cell in each even dimension $0, 2, \ldots, 2n$. Total: $n+1$ even-dimensional cells, $0$ odd. So $\chi(\mathbb{CP}^n) = n+1$ by the alternating-sum formula. By [[Thm - Gauss-Bonnet-Chern Theorem]], $\int e(T\mathbb{CP}^n) = n+1$.
>
> **Method (b):** The Euler sequence $0 \to \mathcal{O} \to \mathcal{O}(1)^{n+1} \to T\mathbb{CP}^n \to 0$, combined with the multiplicative property of total Chern class, gives $c(T\mathbb{CP}^n) = (1+h)^{n+1}$. The top class is $c_n = \binom{n+1}{n}h^n = (n+1)h^n$. Integration: $\int h^n = 1$, so $\int e(T\mathbb{CP}^n) = (n+1) \cdot 1 = n+1$. ∎

> [!warning] Sanity-check via independent route
> Both methods give the same answer $n+1$ — this is a non-trivial check that the Gauss-Bonnet-Chern theorem holds and that the Euler-sequence computation is correct. As a further check, for $n = 1$: $\mathbb{CP}^1 = S^2$, $\chi(S^2) = 2 = 1+1$. ✓ For $n = 2$: $\mathbb{CP}^2$ has $\chi = 3 = 2+1$. ✓

---

# Key Takeaways

**Total Chern class is multiplicative under direct sums and short exact sequences.** The formula $c(A \oplus B) = c(A) \cdot c(B)$ (and more generally $c$ is multiplicative on short exact sequences in the *Grothendieck group* $K^0(M)$) is the engine of Chern-class computations. Given a short exact sequence with two of the three bundles' Chern classes known, the third is recovered. The Euler-sequence computation here is the prototype: $c(T\mathbb{CP}^n)$ is unknown, but it appears in an exact sequence with $\mathcal{O}$ (trivial) and $\mathcal{O}(1)^{n+1}$ (Chern class $(1+h)^{n+1}$), letting us solve for it. The trigger-reaction pattern: "I need Chern classes of an unfamiliar bundle" → "find an exact sequence relating it to bundles with known Chern classes; apply multiplicativity".

**The CW structure on $\mathbb{CP}^n$ as a tower of complex projective spaces.** $\mathbb{CP}^n$ is built inductively from $\mathbb{CP}^{n-1}$ by attaching a single $2n$-cell. The cells are all even-dimensional, which makes $\mathbb{CP}^n$ very simple cohomologically: $H^*(\mathbb{CP}^n; \mathbb{Z}) = \mathbb{Z}[h]/(h^{n+1})$, generated by a single element $h$ in degree 2. The same pattern (single generator in degree 2, truncated at degree $2n$) holds for $\mathbb{CP}^n$ over various coefficient rings. This is what makes $\mathbb{CP}^n$ a fundamental example: its cohomology ring is the simplest possible nontrivial truncated polynomial algebra.

**Integer-valued Chern numbers as the pairing of Chern classes with the fundamental class.** $\int_{\mathbb{CP}^n} c_n(T\mathbb{CP}^n) = n+1$ is the "Chern number" of the tangent bundle, and the integrality is built into the cohomology. The same calculation, generalized to other manifolds, produces the **Chern numbers** that are fundamental in cobordism, in characteristic-class identities, and in physics (e.g., the integer Hall conductance in the quantum Hall effect, the magnetic monopole charge, the topological invariants of K3 surfaces and Calabi-Yau manifolds). The trigger-reaction pattern: "I need a topological invariant of a complex manifold" → "compute Chern numbers via Chern-Weil; the answer is an integer".

This exercise prefigures **Hirzebruch's Riemann-Roch theorem** (which uses the Todd class instead of the Euler class) and the **Riemann-Roch formula for $\mathbb{CP}^n$**, both of which depend on the same Chern-class computation.
