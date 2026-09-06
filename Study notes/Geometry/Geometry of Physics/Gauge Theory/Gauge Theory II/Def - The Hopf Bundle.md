---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Ex - SU(2) is Diffeomorphic to S^3"
tags: [geometry, gauge-theory, hopf-bundle, topology]
---

# Notation

The **Hopf bundle** is the principal $U(1)$-bundle $S^1 \to S^3 \to S^2$ obtained from the action of $U(1) \subset \mathbb{C}^*$ on $S^3 \subset \mathbb{C}^2$. The total space is $S^3 = \{(z_0, z_1) \in \mathbb{C}^2 : |z_0|^2 + |z_1|^2 = 1\}$; the base is $S^2 = \mathbb{CP}^1$; the projection is $\pi(z_0, z_1) = [z_0 : z_1]$. The corresponding complex line bundle (tautological line bundle) is denoted $\mathcal{O}(-1)$ or $H_{-1}$ over $\mathbb{CP}^1$; its dual is $\mathcal{O}(1) = H_1$. Tensor powers $H_n = H_1^{\otimes n}$ (with $H_{-n} = H_{-1}^{\otimes n}$) realize all integer first Chern classes. See [[Gauge Theory II — Principal Bundles, Representations, and Bundle Classification]] for the registry.

---

# Axiom Motivation

The Hopf bundle is the **smallest nontrivial principal $U(1)$-bundle**, and it is the geometric model for the magnetic monopole of unit charge. Why is it special?

First, it is **the simplest nontrivial bundle one can construct**. The base $S^2$ has the smallest $H^2$ among connected closed surfaces ($H^2(S^2;\mathbb{Z}) = \mathbb{Z}$), and the structure group $U(1)$ is the simplest nontrivial compact connected Lie group. Principal $U(1)$-bundles over $S^2$ are classified by their first Chern class $c_1 \in H^2(S^2;\mathbb{Z}) = \mathbb{Z}$; the Hopf bundle realizes the generator $c_1 = -1$ (or $+1$ for the dual), and all higher Chern classes are realized by tensor powers. So the Hopf bundle is the *building block* for all $U(1)$-bundles over $S^2$.

Second, it has a **uniquely natural construction** from $\mathbb{C}^2$. The $U(1) = \{e^{i\theta}\}$ action on $\mathbb{C}^2$ by $(z_0, z_1) \mapsto (e^{i\theta}z_0, e^{i\theta}z_1)$ is free on $S^3 \setminus \{0\} = S^3$, and the orbit space is by definition $\mathbb{CP}^1 = S^2$. So the bundle is "automatic" — no transition functions need to be constructed by hand, just identify the action.

Third, it realizes **the smallest topologically nontrivial map between spheres of different dimensions**. The Hopf map $S^3 \to S^2$ is a generator of $\pi_3(S^2) = \mathbb{Z}$. Before its discovery (Heinz Hopf, 1931), it was widely believed that maps $S^n \to S^m$ with $n > m$ were all null-homotopic (since they cannot wrap around the codomain in any obvious way); the Hopf map was the first counterexample, showing that higher homotopy groups of spheres can be very rich. The **Hopf invariant** distinguishes the Hopf map (invariant $1$) from null-homotopic maps (invariant $0$).

Fourth, it appears in **physics** as the magnetic-monopole bundle. Dirac's quantization argument for a magnetic monopole at the origin of $\mathbb{R}^3$ requires a $U(1)$-bundle over $\mathbb{R}^3 \setminus \{0\} \simeq S^2$ with the monopole charge $g$ determining the first Chern class. The minimum (nonzero) monopole charge $g = \hbar/(2e)$ corresponds to $c_1 = \pm 1$ — exactly the Hopf bundle and its dual.

The construction has a **tautological interpretation**: a point of $\mathbb{CP}^1$ is by definition a 1-dimensional subspace of $\mathbb{C}^2$, and the fibre of the Hopf bundle over that point is *that very subspace* (restricted to the unit sphere, giving an $S^1$, or unrestricted, giving a $\mathbb{C}^*$). So the Hopf bundle is the *tautological* line bundle $\mathcal{O}(-1) \to \mathbb{CP}^1$, the universal example of a holomorphic line bundle on a projective variety.

What would go wrong if we used $\mathbb{R}^4$ instead of $\mathbb{C}^2$? Then we would need a real division algebra structure to make the action work — and there is none on $\mathbb{R}^4$ in the form needed. The use of complex structure is essential. The quaternionic analogue $S^3 \to S^4$ (with fibre $S^3$) and the octonionic $S^7 \to S^{15}$ (with fibre $S^7$) exist, giving rise to the **Hopf bundles** $S^3, S^7, S^{15}$, but these are higher-dimensional and not exhibited by the Frankel chapter.

---

# The Definition

The **Hopf bundle** is the principal $U(1)$-bundle
$$U(1) \;\to\; S^3 \;\xrightarrow{\pi}\; S^2 = \mathbb{CP}^1,$$
defined as follows.

- **Total space:** $S^3 = \{(z_0, z_1) \in \mathbb{C}^2 : |z_0|^2 + |z_1|^2 = 1\}$, the unit sphere in $\mathbb{C}^2$.
- **Base:** $S^2 \cong \mathbb{CP}^1 = (\mathbb{C}^2 \setminus \{0\})/\mathbb{C}^*$, the complex projective line. Points are equivalence classes $[z_0 : z_1]$.
- **Projection:** $\pi(z_0, z_1) = [z_0 : z_1]$. The fibre over $[z_0 : z_1]$ is the unit circle in the complex line through $(z_0, z_1)$.
- **Right $U(1)$-action:** $(z_0, z_1) \cdot e^{i\theta} = (z_0 e^{i\theta}, z_1 e^{i\theta})$, free and fibre-preserving, with orbits equal to the fibres of $\pi$.

In two charts on $S^2 = \mathbb{CP}^1$: in the chart $U = \{[z_0 : z_1] : z_0 \neq 0\}$ with coordinate $z = z_1/z_0$, a local section is
$$e_U(z) \;=\; \frac{(1, z)^T}{\sqrt{1 + |z|^2}}.$$
In the chart $V = \{[z_0 : z_1] : z_1 \neq 0\}$ with coordinate $w = z_0/z_1 = 1/z$, a local section is
$$e_V(w) \;=\; \frac{(w, 1)^T}{\sqrt{1 + |w|^2}}.$$
On the overlap $U \cap V$ (where both $z$ and $w$ are nonzero), the **transition function** is
$$c_{VU}(z) \;=\; \frac{z}{|z|} \;=\; e^{i\phi} \in U(1), \qquad z = |z|e^{i\phi}.$$

The associated **tautological complex line bundle** over $\mathbb{CP}^1$ is $H_{-1} = \mathcal{O}(-1) = S^3 \times_{U(1)} \mathbb{C}$, the line bundle whose fibre over $[z_0:z_1]$ is the complex line through $(z_0, z_1)$ in $\mathbb{C}^2$ itself. Its **first Chern class** is $c_1(H_{-1}) = -1 \in H^2(\mathbb{CP}^1; \mathbb{Z}) = \mathbb{Z}$.

The **Hopf invariant** of the Hopf map $\pi : S^3 \to S^2$ is $1$ — the smallest nontrivial value, generating $\pi_3(S^2) = \mathbb{Z}$.

---

# Relate to Other Fields / Compression

The Hopf bundle is **simultaneously several things at once**, and the equivalences are highly informative:

- The principal $U(1)$-bundle $S^3 \to S^2$ (Frankel's definition).
- The unit sphere bundle of the tautological line bundle $\mathcal{O}(-1) \to \mathbb{CP}^1$.
- The associated $U(1)$-bundle to the principal $U(2)$-bundle $U(1) \to U(2) \to S^3$ specialized via $U(2)/U(1) = S^3$. (Strictly speaking $S^3 = \mathrm{SU}(2)$, but the principal-bundle structure is the same.)
- The quotient of the special unitary group $\mathrm{SU}(2) = S^3$ by its maximal torus $U(1)$, giving $S^2 = \mathrm{SU}(2)/U(1) = \mathbb{CP}^1$.
- The minimum-charge Dirac monopole bundle.

Each viewpoint is useful in different contexts. The principal-bundle viewpoint is geometric; the tautological-line-bundle viewpoint is algebraic-geometric (and emphasizes the holomorphic structure); the $\mathrm{SU}(2)/U(1)$ viewpoint connects to Lie theory and representation theory; the monopole viewpoint is physical.

The Hopf bundle is the **unique nontrivial principal $U(1)$-bundle over $S^2$ with $|c_1| = 1$**. All other principal $U(1)$-bundles over $S^2$ are tensor powers $H_n$, with $c_1 = n$. The classification follows from $H^2(S^2; \mathbb{Z}) = \mathbb{Z}$ and the bijection between principal $U(1)$-bundles and integer cohomology classes (Chern's theorem 17.29).

**True name:** the Hopf bundle is **the tautological line bundle over $\mathbb{CP}^1$, restricted to its unit-sphere subbundle**. Operationally, you compute everything by working in $\mathbb{C}^2$ with the natural unit vectors $(1, z)/\sqrt{1+|z|^2}$ and $(w, 1)/\sqrt{1+|w|^2}$, and tracking the $U(1)$ phase factors on overlaps.

---

# Examples / Corollaries

**Is an instance: the principal $U(1)$-bundle $S^1 \to S^3 \to S^2$ itself.** The defining example.

**Is an instance: the tensor power $H_n = H_1^{\otimes n}$, the line bundle with first Chern class $n$.** All principal $U(1)$-bundles over $S^2$ are of this form for some integer $n$. The Hopf bundle corresponds to $n = -1$; the dual $H_1 = \mathcal{O}(1)$ to $n = +1$.

**Is an instance: the magnetic monopole bundle for unit charge.** $g = \hbar/(2e)$ (one Dirac unit) gives the Hopf bundle; $g = n\hbar/(2e)$ gives $H_{-n}$.

**Is an instance: the unit tangent bundle of $S^2$ as $H_{-2}$.** $TS^2$ is a complex line bundle (using the complex structure on $S^2 = \mathbb{CP}^1$) with $c_1 = \chi(S^2) = 2$; the principal $U(1)$-bundle is $H_2$, the *negative* power of the Hopf bundle.

**Is NOT an instance: the trivial bundle $S^1 \times S^2 \to S^2$.** This is principal $U(1)$ with $c_1 = 0$, hence $H_0$ — not the Hopf bundle.

**Is NOT an instance: the bundle $S^1 \to S^2$ for any base.** $S^1$ is not the base of a principal $U(1)$-bundle in any nontrivial sense; the Hopf bundle has $S^2$ as base, not $S^1$.

**Corollary (first Chern class).** $c_1(H_{-1}) = -1$, computed explicitly by integrating $i\theta/(2\pi)$ over $S^2$:
$$\frac{i}{2\pi}\int_{S^2} \theta_{H_{-1}} = -1.$$
See [[Thm - First Chern Class of the Hopf Bundle is One]] for the computation. (The sign convention: $H_{-1}$ has $c_1 = -1$, the dual $H_1$ has $c_1 = +1$.)

**Corollary (Hopf invariant).** The Hopf map $\pi : S^3 \to S^2$ has Hopf invariant $1$, the generator of $\pi_3(S^2) = \mathbb{Z}$. Geometrically, the preimages $\pi^{-1}(p)$ and $\pi^{-1}(q)$ of any two distinct points are great circles in $S^3$ that link each other with linking number $\pm 1$.

**Corollary (fibres are great circles of $S^3$).** Each fibre $\pi^{-1}([z_0:z_1])$ is a great circle of $S^3$: the unit circle in the complex line through $(z_0, z_1)$. The fibration $S^3 = \bigsqcup_{p \in S^2} \pi^{-1}(p)$ exhibits $S^3$ as a disjoint union of great circles parametrized by $S^2$ — a beautiful geometric picture due to Hopf.

**Corollary (quaternionic description: $S^3 \subset \mathbb{H}$, $\pi(q) = q\mathbf{i}q^{-1} \in S^2 \subset \mathrm{Im}\,\mathbb{H}$).** The Hopf map has a clean quaternionic formula. See [[Ex - Hopf Fibration Computed Explicitly via Quaternions]].

**Calibration check.** Verify (i) the transition function $c_{VU}(z) = z/|z|$ from the explicit local sections; (ii) the right $U(1)$-action is free (no fixed points: $(z_0, z_1) e^{i\theta} = (z_0, z_1)$ implies $e^{i\theta} = 1$ since $z_0, z_1$ are not both zero); (iii) the fibres are connected circles.

---

# Unlocked by This

> [!tip] Dirac Monopole and Charge Quantization *(from Gauge Theory)*
> A magnetic monopole at the origin of $\mathbb{R}^3$ requires a $U(1)$-bundle over $\mathbb{R}^3 \setminus \{0\} \simeq S^2$ for the gauge field of the EM connection. The first Chern class of this bundle must be an integer (Frankel Thm 17.28), and the integer equals $2eq/\hbar$ where $q$ is the monopole charge. This is **Dirac's quantization condition**: magnetic monopoles must come in integer multiples of $\hbar/(2e)$, with the Hopf bundle realizing the smallest nonzero unit. See [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

> [!tip] Hopf Invariant and $\pi_3(S^2) = \mathbb{Z}$ *(from Algebraic Topology)*
> The Hopf map is the generator of $\pi_3(S^2) = \mathbb{Z}$, the first nontrivial homotopy group of $S^2$ above $\pi_2$. The full homotopy theory of spheres is built on this discovery: $\pi_n(S^2)$ is nontrivial for many $n > 2$, and the Hopf invariant is the simplest of an infinite family of invariants of maps between spheres. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].

> [!tip] Higher Hopf Bundles $S^3 \to S^4, S^7 \to S^{15}$ *(from Topology)*
> The quaternionic Hopf bundle $S^3 \to S^7 \to S^4$ (with fibre $S^3 = \mathrm{Sp}(1)$) and the octonionic Hopf bundle $S^7 \to S^{15} \to S^8$ are the only other examples (Adams' theorem) of "Hopf fibrations" of spheres by spheres with sphere fibres. These three Hopf fibrations correspond to the three division algebras $\mathbb{C}, \mathbb{H}, \mathbb{O}$ over $\mathbb{R}$, and the impossibility of further Hopf fibrations (e.g., $S^{15} \to S^{16}$ with fibre $S^{15}$) is **Adams' Theorem on Hopf invariants**, one of the deep results of stable homotopy theory.

> [!tip] $\mathcal{O}(-1)$ as the Tautological Bundle on $\mathbb{CP}^n$ *(from Algebraic Geometry)*
> The Hopf bundle generalizes to $\mathcal{O}(-1) \to \mathbb{CP}^n$ in higher dimensions: the bundle whose fibre over $[z_0 : \ldots : z_n] \in \mathbb{CP}^n$ is the complex line through $(z_0, \ldots, z_n)$. Together with its dual $\mathcal{O}(1)$, this generates the **Picard group** of $\mathbb{CP}^n$: every holomorphic line bundle on $\mathbb{CP}^n$ is $\mathcal{O}(d)$ for some integer $d$. This is the simplest classification of line bundles in algebraic geometry and underlies the entire theory of projective embeddings via complete linear systems.
