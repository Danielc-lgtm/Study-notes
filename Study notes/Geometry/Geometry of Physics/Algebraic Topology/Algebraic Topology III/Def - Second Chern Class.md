---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Chern Forms of a U(n) Bundle"
  - "Def - First Chern Class"
  - "Def - Vector Bundle"
tags: [geometry, algebraic-topology, characteristic-classes, gauge-theory, yang-mills]
---

# Notation

$E \to M$ is a complex vector bundle of rank $n \geq 2$, typically with structure group $SU(n)$ for physical applications. $\theta$ is the curvature 2-form. $\mathrm{Tr}(\theta \wedge \theta)$ is the matrix trace of the wedge product: $\mathrm{Tr}(\theta \wedge \theta) = \theta^a_b \wedge \theta^b_a$ summed over indices. $[c_2(E)] \in H^4(M; \mathbb{Z})$ is the second Chern class. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]] for the full notation registry.

---

# Axiom Motivation

The second Chern class is the *second simplest* characteristic class, and it is the one most relevant to **four-dimensional gauge theory**. For an $SU(n)$ bundle (the structure group of non-Abelian Yang–Mills theory), the first Chern class vanishes, so $c_2$ is the *first* nontrivial invariant. Its integer values on closed oriented 4-manifolds label the topological sectors of $SU(n)$ gauge theory — most famously, the **instanton number** of Yang–Mills configurations on $\mathbb{R}^4$.

The motivating question is: *what is the simplest topological invariant of a rank-$n$ complex bundle for $n \geq 2$ when the first Chern class is zero?* By the [[Def - Total Chern Class|total Chern class]] expansion,

$$c(E) = 1 + c_1(E) + c_2(E) + \cdots,$$

so if $c_1 = 0$, the leading nontrivial term is $c_2$. For an $SU(n)$ bundle, $c_1 = 0$ automatically (because $\mathrm{Tr}(\theta) = 0$ for $\mathfrak{su}(n)$-valued $\theta$), and $c_2$ becomes the central invariant. For $SU(2)$ bundles in particular — the structure group of "weak isospin" in physics — $c_2$ is the only invariant, and it labels all topologically distinct configurations.

The formula for $c_2$ comes from expanding the determinant $\det(I + i\theta/2\pi)$:

$$\det(I + A) = 1 + \mathrm{Tr}(A) + \tfrac{1}{2}[(\mathrm{Tr}\,A)^2 - \mathrm{Tr}(A^2)] + \cdots.$$

With $A = i\theta/2\pi$:

$$c_2(E) = -\frac{1}{8\pi^2}[(\mathrm{Tr}\,\theta) \wedge (\mathrm{Tr}\,\theta) - \mathrm{Tr}(\theta \wedge \theta)] = \frac{1}{8\pi^2}[\mathrm{Tr}(\theta \wedge \theta) - (\mathrm{Tr}\,\theta) \wedge (\mathrm{Tr}\,\theta)].$$

For an $SU(n)$ bundle this simplifies to

$$c_2(E) = -\frac{1}{8\pi^2} \mathrm{Tr}(\theta \wedge \theta) = -\frac{1}{8\pi^2} \mathrm{Tr}(F \wedge F),$$

where $F = \theta$ is the curvature (called "field strength" in physics).

Why is $\mathrm{Tr}(\theta \wedge \theta)$ the natural invariant? Because:
- It is the only quadratic-in-$\theta$ invariant polynomial on $\mathfrak{su}(n)$ (up to scalar multiples), as a consequence of the irreducibility of $\mathfrak{su}(n)$ under the adjoint action.
- It is a real form: $\mathrm{Tr}(\theta \wedge \theta) = \overline{\mathrm{Tr}(\theta \wedge \theta)}$ since $\theta$ is anti-Hermitian and $\theta \wedge \theta$ involves an even number of $i$ factors.
- It is closed: $d\mathrm{Tr}(\theta \wedge \theta) = 0$ by the Bianchi identity.

The factor $1/(8\pi^2)$ normalises the periods to integers, similarly to the $1/(2\pi)$ in $c_1$. The combinatorial origin: on a 4-sphere bounded by $S^3$, the integer $\int_{S^4} c_2$ equals (up to sign) the degree of the gauge-transformation map $g : S^3 \to SU(n)$, and the degree formula in terms of $g^{-1}dg$ acquires precisely the $24\pi^2$ normalisation in Frankel (22.3). The relation $\int_{\mathbb{R}^4} c_2 = -\int_{\partial}/(24\pi^2)$ between the bulk integral and the boundary winding gives the $8\pi^2$ factor in $c_2 = -(1/8\pi^2)\mathrm{Tr}(\theta\wedge\theta)$, since the homotopy-extension argument relates $1/(24\pi^2)$ on $S^3$ with $-1/(8\pi^2)$ on $\mathbb{R}^4$.

The deepest motivation is **physical**: in Yang–Mills theory, the action is

$$S_{\mathrm{YM}} = -\frac{1}{2}\int_{M^4} \mathrm{Tr}(F \wedge \star F),$$

and the **topological term** is

$$S_{\mathrm{top}} = -\frac{1}{2}\int_{M^4} \mathrm{Tr}(F \wedge F) = 4\pi^2 \int_{M^4} c_2.$$

The difference $S_{\mathrm{YM}} - |S_{\mathrm{top}}| \geq 0$ leads to the **Bogomolnyi bound** $S_{\mathrm{YM}} \geq 4\pi^2 |\int c_2|$, with equality for **self-dual** or **anti-self-dual** connections ($\star F = \pm F$). The minimisers — **instantons** — have action equal to $4\pi^2 |c_2|$ times the instanton number, and they extremise the Yang–Mills functional in each topological sector. The instanton number is precisely $\int c_2$, and its integrality (forced by the Chern–Weil theorem) labels distinct vacuum sectors of the gauge theory.

---

# The Definition

Let $E \to M$ be a complex rank-$n$ vector bundle with $U(n)$ structure group and a chosen $U(n)$ connection with curvature 2-form $\theta$ (an $n \times n$ matrix of $\mathfrak{u}(n)$-valued 2-forms). The **second Chern form** is

$$c_2(E) := \frac{1}{8\pi^2}\big[\mathrm{Tr}(\theta \wedge \theta) - \mathrm{Tr}(\theta) \wedge \mathrm{Tr}(\theta)\big],$$

a real closed 4-form on $M$.

**For an $SU(n)$ bundle** (or any bundle with $\mathrm{Tr}(\theta) = 0$), the formula simplifies:

$$c_2(E) = -\frac{1}{8\pi^2} \mathrm{Tr}(\theta \wedge \theta).$$

The **second Chern class** is the de Rham cohomology class:

$$c_2(E) := [c_2(\theta)] \in H^4_{\mathrm{dR}}(M; \mathbb{R}),$$

with integer lift in $H^4(M; \mathbb{Z})$.

**The second Chern number** of $E$ on a closed oriented 4-manifold $M^4$ is

$$\int_{M^4} c_2(E) \in \mathbb{Z}.$$

For an **$SU(n)$ instanton** — an $SU(n)$ Yang–Mills connection on $\mathbb{R}^4$ with curvature falling off at infinity — the second Chern number is the **instanton number** $k$, and the action satisfies $S = 8\pi^2 |k|$ for self-dual or anti-self-dual configurations.

**Fundamental properties:**

1. **Naturality:** $c_2(f^* E) = f^* c_2(E)$.
2. **Whitney sum:** $c_2(E \oplus F) = c_2(E) + c_1(E) c_1(F) + c_2(F)$.
3. **Real bundles:** for the complexification of a real bundle $E_{\mathbb{R}}$, $c_2(E_{\mathbb{R}} \otimes \mathbb{C}) = -p_1(E_{\mathbb{R}})$, the **first Pontryagin class**.

---

# Categorical / Structural Definition

The second Chern class is the second generator of the polynomial ring $H^*(BU(n); \mathbb{Z}) = \mathbb{Z}[c_1, c_2, \ldots, c_n]$. For an $SU(n)$ bundle, $H^*(BSU(n); \mathbb{Z}) = \mathbb{Z}[c_2, c_3, \ldots, c_n]$, and $c_2$ is the first generator — the lowest-degree non-trivial invariant.

In K-theory, the **Chern character** decomposition $\mathrm{ch}(E) = n + c_1(E) + \tfrac{1}{2}(c_1^2 - 2c_2) + \cdots$ identifies $c_2$ as appearing in the degree-4 component of the Chern character. The Chern character is the rational-cohomology image of the K-theory class $[E]$.

In **Yang–Mills theory**, $c_2$ has a clean interpretation via the [[Thm - Chern-Weil Theorem (Statement)|Chern–Weil construction]] applied to the invariant polynomial $P(A) = -\tfrac{1}{8\pi^2}\mathrm{Tr}(A^2)$ on $\mathfrak{su}(n)$. The Chern–Weil image is the cohomology class $[c_2(E)] \in H^4(M; \mathbb{R})$ — an integer-valued topological invariant.

A more refined definition uses the **Chern–Simons form** $\mathrm{CS}_3 = \mathrm{Tr}(\omega \wedge d\omega + \tfrac{2}{3} \omega \wedge \omega \wedge \omega)$, which satisfies $d\mathrm{CS}_3 = \mathrm{Tr}(\theta \wedge \theta)$ (Frankel's (22.4)). This identifies $c_2$ as the *image of the Chern–Simons form under exterior derivative*: $c_2 = -(1/8\pi^2) d\mathrm{CS}_3$. The Chern–Simons form is not globally defined on bundles with $c_2 \neq 0$ (it depends on the trivialisation), but its exterior derivative is the globally defined $c_2$.

---

# Relate to Other Fields / Compression

**True name:** $c_2$ is **the integer that counts the homotopy class in $\pi_3(SU(n)) = \mathbb{Z}$ of the gauge transformation at infinity for an instanton**. The operational picture: an $SU(n)$ Yang–Mills field on $\mathbb{R}^4$ with finite action decays at infinity to a pure-gauge configuration $g(\infty)^{-1} dg(\infty)$ for some $g : S^3_\infty \to SU(n)$; the integer $\int_{\mathbb{R}^4} c_2$ equals the degree of $g$, which is a homotopy class in $\pi_3(SU(n)) = \mathbb{Z}$. This is the **instanton number**.

In **Yang–Mills theory**, $c_2$ is the topological charge that labels distinct vacuum sectors of non-Abelian gauge theory. Yang–Mills configurations in different sectors cannot be continuously deformed into each other; tunnelling between sectors is mediated by instantons. The QCD vacuum has a $\theta$-angle multiplying $\int c_2$ in the action, leading to **CP violation** in the strong interaction (the **strong CP problem**).

In **Donaldson theory**, the moduli space of $SU(2)$ instantons of charge $k$ on a closed simply connected 4-manifold $M$ has dimension $8k - 3 - b_2^+$, where $b_2^+$ is the dimension of the positive-definite part of the intersection form. These moduli spaces are used to construct **Donaldson invariants** — diffeomorphism invariants of smooth 4-manifolds that distinguish smooth structures undetectable by classical topology.

In **algebraic geometry**, $c_2(E)$ for a rank-$n$ holomorphic vector bundle on a surface is an intersection number — it equals the number of zeros (with multiplicity) of a generic pair of holomorphic sections, providing the algebraic-geometric interpretation of "obstruction to two sections being linearly independent everywhere".

In **string theory**, $c_2$ of the spacetime tangent bundle appears in the **anomaly cancellation** conditions: the Green–Schwarz mechanism requires specific Chern classes of bundle data to cancel quantum anomalies. The **second Chern class of the tangent bundle of a Calabi–Yau** is one of the inputs to the Hirzebruch–Riemann–Roch computation of dimensions of moduli spaces.

---

# Examples / Corollaries

**Example: BPST instanton.** The BPST instanton is the $SU(2)$ self-dual connection $A_\mu = -i(x_\nu/(|x|^2 + \rho^2))\sigma_{\mu\nu}$ on $\mathbb{R}^4$, with one positive scale $\rho > 0$. Its second Chern number is $\int_{\mathbb{R}^4} c_2 = 1$ (or $-1$, depending on orientation). The action is $S = 8\pi^2$ for unit charge. See [[Ex - Winding Number of the BPST Instanton is 1]].

**Example: trivial bundle.** $c_2(M \times \mathbb{C}^n) = 0$ for any $n$, since the curvature vanishes.

**Example: $T\mathbb{CP}^2$.** From the Euler-sequence calculation $c(T\mathbb{CP}^n) = (1+h)^{n+1}$, the second Chern class of $T\mathbb{CP}^2$ is $c_2 = \binom{3}{2} h^2 = 3 h^2$, and $\int_{\mathbb{CP}^2} c_2 = 3 = \chi(\mathbb{CP}^2)$. So the second Chern number of the tangent bundle of $\mathbb{CP}^2$ is its Euler characteristic — confirming the special case of $c_n = $ Euler class for complex manifolds.

**Example: $S^4$ as $SU(2)$ instanton base.** Every $SU(2)$ principal bundle on $S^4$ is classified by $c_2 \in H^4(S^4; \mathbb{Z}) = \mathbb{Z}$. The bundle of instanton number $k$ has $\int_{S^4} c_2 = k$. The space of $SU(2)$ bundles on $S^4$ is in bijection with $\mathbb{Z}$, recovering the classification by gauge transformations at infinity (since $S^4 = \mathbb{R}^4 \cup \{\infty\}$).

**Example: complex tangent bundle on $K3$.** The K3 surface is a simply connected complex 2-manifold with $c_1 = 0$ and $\int_{K3} c_2 = 24$ — a celebrated fact called the "24" for K3, equal to the topological Euler characteristic of K3. By Hirzebruch–Riemann–Roch, the holomorphic Euler characteristic is $\chi(K3, \mathcal{O}) = \int_{K3} \mathrm{td}(K3) = (1/24)\int c_2 + \cdots = 2$.

**Example: real Pontryagin class.** For a real oriented rank-$2k$ bundle $E_{\mathbb{R}}$, the first Pontryagin class is $p_1(E_{\mathbb{R}}) = -c_2(E_{\mathbb{R}} \otimes \mathbb{C})$. The **signature theorem** for a closed oriented 4-manifold is $\sigma(M^4) = (1/3) \int_M p_1(TM) = -(1/3) \int_M c_2(TM \otimes \mathbb{C})$. So the signature of a 4-manifold is computable from the second Chern class of its complexified tangent bundle.

**Is NOT an instance: pure gauge.** If $A = g^{-1}dg$ for some globally defined $g : M \to SU(n)$, then $F = dA + A \wedge A = 0$, so all Chern forms vanish. Pure gauge configurations have trivial topology — instantons are essential because they are *not* pure gauge globally, only asymptotically.

**Corollary: real signature theorem.** $\sigma(M^4) = -\tfrac{1}{3}\int_{M^4} c_2(TM \otimes \mathbb{C})$ for a closed oriented 4-manifold. So the signature of a 4-manifold is determined by the second Chern class of its complexified tangent bundle.

**Corollary: action bound (Bogomolnyi).** For an $SU(n)$ connection $A$ on $M^4$ with curvature $F$,

$$S_{\mathrm{YM}}[A] = -\tfrac{1}{2}\int \mathrm{Tr}(F \wedge \star F) \geq |4\pi^2 \int c_2| = 8\pi^2 |c_2 \text{ number}|,$$

with equality if and only if $\star F = \pm F$ (self-dual or anti-self-dual). The minimisers are instantons.

**Corollary: charge conservation.** The instanton number is conserved by continuous deformations of the connection: it is a topological invariant. Tunnelling between sectors of different $c_2$ requires instanton processes, which contribute non-perturbatively to the path integral.

**Calibration check.** If you understand the definition you should be able to: (i) verify that for $SU(n)$, $c_2 = -(1/8\pi^2)\mathrm{Tr}(\theta \wedge \theta)$; (ii) compute $\int_{S^4} c_2$ for the BPST instanton (up to algebraic details); (iii) explain why $c_2$ is integer-valued; (iv) state the Whitney sum formula for $c_2$.

---

# Unlocked by This

> [!tip] Donaldson Theory and Smooth 4-Manifolds *(from Differential Topology)*
> The moduli space of $SU(2)$ self-dual instantons of charge $k$ on a closed simply-connected 4-manifold $M$ has dimension $8k - 3 - b_2^+(M)$. **Donaldson invariants** are integers obtained by integrating cohomology classes over these moduli spaces. They are diffeomorphism invariants of smooth 4-manifolds that distinguish exotic smooth structures — for instance, $\mathbb{R}^4$ admits uncountably many distinct smooth structures, all homeomorphic to standard $\mathbb{R}^4$, distinguished by Donaldson-theoretic methods. This is the most spectacular application of $c_2$-theory in differential topology.

> [!tip] Seiberg–Witten Theory *(from Gauge Theory)*
> **Seiberg–Witten invariants** are 4-manifold invariants obtained from a simpler abelian gauge theory ($U(1)$ coupled to a spinor) that compute the same information as Donaldson invariants (and more). The moduli spaces are typically finite-dimensional, and the invariants are far easier to compute. The Seiberg–Witten equations replace the full Yang–Mills equations with a coupled system whose moduli space has explicit dimension formula involving $c_1$ of the line bundle and the Pontryagin classes of $M$. This is the modern computational tool for 4-manifold topology.

> [!tip] Strong CP Problem *(from Particle Physics)*
> The QCD Lagrangian has a topological term $\theta \int c_2$ that contributes to the action and induces CP violation in strong interactions. Experimental constraints force $\theta \lesssim 10^{-10}$, yet no symmetry of the Standard Model explains why $\theta$ should be so small — the **strong CP problem**. Proposed resolutions include the **axion** (a dynamical field that relaxes to $\theta = 0$) or new physics at the Peccei–Quinn scale. The topological origin of $\theta$ in $\int c_2$ is what makes the problem unavoidable: it is a free parameter of the theory, not a quantity computable from first principles.
