---
type: definition
subject: spinors
prereqs:
  - "Def - Dirac Gamma Matrices"
  - "Def - The Dirac Equation"
  - "Def - Pin and Spin Groups"
tags: [geometry, spinors, quantum-mechanics, particle-physics]
---

# Notation

A **Weyl spinor** is a two-component complex vector $\psi \in \mathbb{C}^2$ transforming under one of the two inequivalent irreducible representations of $\mathrm{SL}(2, \mathbb{C}) = \mathrm{Spin}^+(1, 3)$. The two types are denoted $\psi_L$ (left-handed, transforming under $A$) and $\psi_R$ (right-handed, transforming under $(A^\dagger)^{-1}$). The corresponding representations are $D^{(1/2, 0)}$ and $D^{(0, 1/2)}$ in physics notation. The **chirality matrix** $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ satisfies $(\gamma^5)^2 = I$, $\{\gamma^5, \gamma^\mu\} = 0$. The **chiral projectors** are $P_L = \tfrac{1}{2}(I - \gamma^5)$ and $P_R = \tfrac{1}{2}(I + \gamma^5)$, satisfying $P_L^2 = P_L$, $P_R^2 = P_R$, $P_L P_R = 0 = P_R P_L$, $P_L + P_R = I$. The Pauli matrices $\sigma_k$ enter via the relativistic forms $\sigma^\mu = (I, \vec\sigma)$ and $\bar\sigma^\mu = (I, -\vec\sigma)$.

---

# Axiom Motivation

The Weyl spinors are forced on us by the **reducibility of the Dirac spinor representation under chirality**. The full Dirac representation $\rho: \mathrm{SL}(2, \mathbb{C}) \to GL(4, \mathbb{C})$, given by $\rho(A) = \mathrm{diag}(A, (A^\dagger)^{-1})$ in the Weyl basis, is *block-diagonal* — and therefore *reducible*: it decomposes into the direct sum of two two-dimensional representations, $\rho = D^{(1/2, 0)} \oplus D^{(0, 1/2)}$. The two summands are the **Weyl spinor representations**, and the four-component Dirac spinor decomposes correspondingly as $\psi = \psi_L \oplus \psi_R$.

The desiderata are:

1. We want a representation of $\mathrm{SL}(2, \mathbb{C})$ that is **irreducible** (cannot be decomposed further) and has the smallest possible complex dimension. The Dirac representation $\rho$ is reducible, so we look at its irreducible summands.

2. We want a notion of **chirality** — a way of distinguishing two types of spinors that are mapped into each other by parity (spatial reflection) but not by rotations and boosts alone.

3. We want the two types to capture the **left-handed vs right-handed** distinction of particles in the Standard Model, which is intrinsically chiral: the weak interaction couples only to left-handed leptons.

The decomposition is captured by the **chirality matrix** $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$. This is the unique (up to scalar) Hermitian element of the Clifford algebra anticommuting with all four $\gamma^\mu$, and it satisfies $(\gamma^5)^2 = I$, so its eigenvalues are $\pm 1$. The eigenspaces of $\gamma^5$ are the **chiral subspaces**: in the Weyl basis $\gamma^5 = \mathrm{diag}(-I_2, I_2)$, so the $-1$-eigenspace is the upper $\mathbb{C}^2$ (left-handed spinors $\psi_L$) and the $+1$-eigenspace is the lower $\mathbb{C}^2$ (right-handed spinors $\psi_R$).

Why is the decomposition $\mathbb{C}^4 = \mathbb{C}^2_L \oplus \mathbb{C}^2_R$ preserved by $\mathrm{SL}(2, \mathbb{C})$ but not by parity? The spin representation $\rho(A) = \mathrm{diag}(A, (A^\dagger)^{-1})$ acts independently on $\psi_L$ and $\psi_R$ — they don't mix under proper Lorentz transformations. But parity (spatial reflection $\vec x \to -\vec x$, time unchanged) corresponds to a Lorentz transformation outside the connected component $L_0$, and its action on spinors interchanges $\psi_L \leftrightarrow \psi_R$ (this is the *parity operator* $\gamma^0$ in the Dirac basis). So Weyl spinors are well-defined under the *proper-orthochronous* Lorentz group but get mixed by parity.

What about the mass term $m\bar\psi\psi = m(\bar\psi_L\psi_R + \bar\psi_R\psi_L)$? This term *couples* left- and right-handed spinors: a massive Dirac fermion is "left-handed and right-handed in equal measure", oscillating between the two as it propagates. **Massless** fermions have decoupled equations: a massless left-handed Weyl fermion stays left-handed forever, with no right-handed partner. This is the structure of the **Weyl equation** $\sigma^\mu \partial_\mu \psi_L = 0$ (for left-handed) or $\bar\sigma^\mu\partial_\mu\psi_R = 0$ (for right-handed), each independent.

Why is the Weyl decomposition important in physics? Because the Standard Model is **chiral**: the weak interaction couples only to $\psi_L$ (the V-A theory), and neutrinos in the original Standard Model were assumed to be purely left-handed (massless Weyl fermions, before neutrino mass was discovered). Chirality is the geometric source of *parity violation* in weak interactions and is one of the most counterintuitive features of fundamental physics.

What if we dropped the four-component structure entirely and worked with Weyl spinors from the start? In the massless case this works fine — the **Weyl equation** is the cleanest relativistic equation for a chiral fermion. In the massive case the two-component formalism becomes unwieldy: the mass term is a *coupling* between $\psi_L$ and $\psi_R$, so one cannot describe a massive fermion with a single Weyl spinor unless additional structure (a *Majorana mass*) is invoked.

What is a **Majorana spinor**? It is a Dirac spinor satisfying the *reality condition* $\psi = C\bar\psi^T$ where $C$ is the charge-conjugation matrix. Majorana spinors are intrinsically real (in a suitable basis) and have only two independent real degrees of freedom — they are equivalent to *self-conjugate* Weyl spinors (a Weyl spinor with its complex conjugate identified). A **Majorana–Weyl spinor** is both Majorana and Weyl — only possible in spacetime dimensions $D \equiv 2 \pmod 8$ (so $D = 2, 10, \ldots$).

---

# The Definition

A **(two-component) Weyl spinor** is an element $\psi \in \mathbb{C}^2$ transforming under one of the two inequivalent irreducible representations of the spin group $\mathrm{Spin}^+(1, 3) = \mathrm{SL}(2, \mathbb{C})$:

- **Left-handed Weyl spinor** $\psi_L \in \mathbb{C}^2_L$: transforms under $A \in \mathrm{SL}(2, \mathbb{C})$ as $\psi_L \mapsto A\psi_L$. This is the representation $D^{(1/2, 0)}$.

- **Right-handed Weyl spinor** $\psi_R \in \mathbb{C}^2_R$: transforms as $\psi_R \mapsto (A^\dagger)^{-1}\psi_R$. This is the representation $D^{(0, 1/2)}$.

The two are **inequivalent** as representations of $\mathrm{SL}(2, \mathbb{C})$: there is no linear isomorphism $\mathbb{C}^2_L \to \mathbb{C}^2_R$ intertwining the two actions (since $A$ and $(A^\dagger)^{-1}$ are not similar for general $A$ — though they coincide when $A \in SU(2)$, the rotation subgroup).

**Chiral decomposition of a Dirac spinor.** In the Weyl basis, a Dirac spinor decomposes as
$$\psi = \begin{pmatrix}\psi_L \\ \psi_R\end{pmatrix} \in \mathbb{C}^2_L \oplus \mathbb{C}^2_R = \mathbb{C}^4.$$
The chiral projectors $P_L = \tfrac{1}{2}(I - \gamma^5)$ and $P_R = \tfrac{1}{2}(I + \gamma^5)$ extract the components:
$$\psi_L = P_L\psi = \begin{pmatrix}\psi_L \\ 0\end{pmatrix}, \quad \psi_R = P_R\psi = \begin{pmatrix}0 \\ \psi_R\end{pmatrix}.$$

**Weyl equations (massless case).** For $m = 0$, the Dirac equation decouples into independent equations for $\psi_L$ and $\psi_R$:
$$\sigma^\mu \partial_\mu \psi_L = 0, \qquad \bar\sigma^\mu\partial_\mu\psi_R = 0,$$
where $\sigma^\mu = (I, \vec\sigma)$ and $\bar\sigma^\mu = (I, -\vec\sigma)$ (using Frankel's sign convention). Equivalently:
$$(\partial_t + \vec\sigma\cdot\vec\nabla)\psi_L = 0, \qquad (\partial_t - \vec\sigma\cdot\vec\nabla)\psi_R = 0.$$

**Mass term as chirality coupling.** For $m \neq 0$, the Dirac equation couples chiralities:
$$\bar\sigma^\mu \partial_\mu \psi_R = m\psi_L, \qquad \sigma^\mu\partial_\mu\psi_L = m\psi_R.$$
The mass term $m\bar\psi\psi = m(\bar\psi_L \psi_R + \bar\psi_R\psi_L)$ explicitly mixes the chiralities.

---

# Categorical / Structural Definition

The Weyl spinors are the two **fundamental representations** of $\mathrm{SL}(2, \mathbb{C})$, which is the universal cover of the proper-orthochronous Lorentz group $L_0$. They are related by **complex conjugation**: $D^{(0, 1/2)}$ is the complex-conjugate representation of $D^{(1/2, 0)}$, i.e., $(A^\dagger)^{-1} = (\bar A^{-1})^T = (A^{-1})^*$ for $A \in \mathrm{SL}(2, \mathbb{C})$.

The general irreducible representation of $\mathrm{SL}(2, \mathbb{C})$ is labelled by a pair $(j_L, j_R)$ with $j_L, j_R \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$, and is the tensor product $D^{(j_L, 0)} \otimes D^{(0, j_R)} = \mathrm{Sym}^{2j_L}(\mathbb{C}^2_L) \otimes \mathrm{Sym}^{2j_R}(\mathbb{C}^2_R)$. So:
- $(0, 0) = D^{(0, 0)}$ — scalar (1-dim);
- $(\tfrac{1}{2}, 0) = D^{(1/2, 0)}$ — left-handed Weyl (2-dim);
- $(0, \tfrac{1}{2}) = D^{(0, 1/2)}$ — right-handed Weyl (2-dim);
- $(\tfrac{1}{2}, \tfrac{1}{2}) = D^{(1/2, 1/2)}$ — Lorentz vector $\mathbb{C}^4$ (4-dim);
- $(1, 0) \oplus (0, 1) = D^{(1, 0)} \oplus D^{(0, 1)}$ — self-dual + anti-self-dual 2-form (3 + 3 = 6-dim, the bivector $F^{\mu\nu}$);
- $(j_L, j_R)$ with $j_L + j_R = \tfrac{3}{2}$: spin-$\tfrac{3}{2}$ Rarita–Schwinger fields.

The Dirac spinor is the *reducible* representation $D^{(1/2, 0)} \oplus D^{(0, 1/2)}$, and Weyl spinors are its irreducible building blocks. The chirality matrix $\gamma^5$ is the projector onto these blocks: an element of the *center* of $\mathrm{Cl}^0(1, 3) \otimes \mathbb{C}$.

Categorically, **chirality is the $\mathbb{Z}/2$-grading of the spinor module $\mathbb{C}^4 = \mathbb{C}^2_L \oplus \mathbb{C}^2_R$** induced by $\gamma^5$. The Dirac spinor module is a $\mathbb{Z}/2$-graded $\mathrm{Cl}(1, 3) \otimes \mathbb{C}$-module, with the grading inherited from the even-odd decomposition of the Clifford algebra. This grading is the algebraic origin of every chirality-related phenomenon in physics: parity violation, the chiral anomaly, the Witten index, the Dirac operator's index theorem.

---

# Relate to Other Fields / Compression

**True name:** A Weyl spinor is *the smallest irreducible representation of the universal cover of the Lorentz group*, equivalently *an eigenspace of the chirality matrix $\gamma^5$ in the Dirac spinor module*. The two flavors (left- and right-handed) correspond to the two inequivalent fundamental representations of $\mathrm{SL}(2, \mathbb{C})$, which are complex-conjugates of each other. The physical interpretation as "chirality" reflects the geometric fact that parity (spatial reflection) maps left to right but proper Lorentz transformations cannot.

Connections to other areas:

- **Lie group representation theory:** the classification of $\mathrm{SL}(2, \mathbb{C})$-representations by pairs $(j_L, j_R)$ generalizes to all semisimple complex Lie groups via the **Weyl character formula**; Weyl spinors are the simplest non-trivial example.
- **Higher dimensions:** in spacetime dimension $D = 2k$, the Dirac spinor module $\mathbb{C}^{2^k}$ splits as $\mathbb{C}^{2^{k-1}}_L \oplus \mathbb{C}^{2^{k-1}}_R$ under chirality (the splitting exists in *all* even dimensions, with the projectors $P_{L,R} = \tfrac{1}{2}(I \mp \gamma^{2k+1})$). In odd dimensions, the Dirac spinor module is irreducible and chirality is absent.
- **Twistor theory:** Penrose's twistor formalism encodes the spinorial structure of $L_0$ directly, with $\mathrm{SL}(2, \mathbb{C})$ acting on 4-component twistors $Z^\alpha = (\omega^A, \pi_{A'})^T$ that combine a left-handed and a right-handed Weyl spinor — generalizing the spinor-helicity formalism of particle physics.
- **Conformal field theory:** in 2-dimensional CFT, left-movers and right-movers of a chiral conformal field theory are naturally Weyl-like — the chiral fermion is the prototype.

---

# Examples / Corollaries

**Example 1: Massless neutrino (early Standard Model).** Before neutrino oscillation experiments (1998+), neutrinos were assumed to be massless left-handed Weyl fermions described by the Weyl equation $\sigma^\mu \partial_\mu \nu_L = 0$. The right-handed neutrino was absent from the theory entirely. Parity violation in weak interactions follows directly: left-handed neutrinos can interact via the weak force, but there are no right-handed neutrinos at all to mirror them.

**Example 2: Photon as $(1, 0) \oplus (0, 1)$.** The electromagnetic field strength $F_{\mu\nu}$ is a Lorentz $2$-form, which under $\mathrm{SL}(2, \mathbb{C})$ decomposes as $(1, 0) \oplus (0, 1)$ — the self-dual and anti-self-dual parts. The self-dual part is $F^+_{\mu\nu} = \tfrac{1}{2}(F_{\mu\nu} + i\tilde F_{\mu\nu})$ (with $\tilde F$ the Hodge dual), and the photon's two helicity states correspond to these two irreducible pieces.

**Example 3: Helicity of massless particles.** The **helicity** of a massless particle is the projection of its spin along its direction of motion, and for Weyl fermions it equals the chirality: $h = \pm\tfrac{1}{2}$ for $\psi_L, \psi_R$ respectively. The helicity is Lorentz-invariant for massless particles (since one cannot boost past them) but frame-dependent for massive particles, which can be "overtaken" by a boost.

**Example 4: Majorana spinor as a Weyl spinor with reality condition.** A Majorana spinor $\psi = (\psi_L, \psi_R)^T$ satisfies $\psi_R = i\sigma^2 \psi_L^*$ — i.e., the right-handed component is determined by the left-handed via charge conjugation. Equivalently, a Majorana spinor has half as many independent components as a Dirac spinor (4 real instead of 4 complex). The neutrino, *if* it is its own antiparticle (currently unknown), would be a Majorana spinor.

**Non-example: a 2-component spinor under $SO(3)$.** $SO(3)$-representations are labelled by integer spin $0, 1, 2, \ldots$; there are *no* 2-component irreducible $SO(3)$-representations. So an "ordinary" 2-component object under $\mathbb{R}^3$-rotations doesn't exist — the 2-component object $\psi \in \mathbb{C}^2$ requires the $SU(2)$ structure (the cover) to make sense as a spinor. The Weyl spinor is the relativistic analogue, requiring $\mathrm{SL}(2, \mathbb{C})$.

**Non-example: a "left-and-right" spinor as a *single* representation.** In odd dimensions (e.g., $D = 3, 5$), the Dirac spinor is irreducible and *cannot* be split into left- and right-handed parts — chirality is a phenomenon of even spacetime dimensions only. This is reflected in the fact that $\gamma^5 = \gamma^0\gamma^1\cdots\gamma^{D-1}$ has $(\gamma^5)^2 = (-1)^{D(D-1)/2}\eta^{00}\cdots\eta^{D-1,D-1}$, which is $\pm 1$ depending on dimension and signature; in odd dimensions it commutes with all $\gamma^\mu$, so it is a scalar multiple of the identity by Schur's lemma — not a useful chirality operator.

**Calibration check.** A reader should verify: (i) the projectors $P_L$ and $P_R$ are orthogonal idempotents summing to $I$; (ii) the chirality matrix $\gamma^5$ anticommutes with each $\gamma^\mu$ and commutes with each $\sigma^{\mu\nu} = \tfrac{i}{2}[\gamma^\mu, \gamma^\nu]$; (iii) under a boost in the $z$-direction with rapidity $\xi$, the Weyl spinors transform as $\psi_L \mapsto e^{-\xi\sigma_3/2}\psi_L$ and $\psi_R \mapsto e^{+\xi\sigma_3/2}\psi_R$ — opposite signs, reflecting the inequivalence of the two representations.

---

# Unlocked by This

> [!tip] Chiral Anomaly and the Adler–Bell–Jackiw Theorem
> The **chiral anomaly** is the phenomenon that the classically-conserved axial current $j_5^\mu = \bar\psi\gamma^\mu\gamma^5\psi$ acquires an anomaly at the quantum level: $\partial_\mu j_5^\mu = \tfrac{e^2}{16\pi^2}\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ in QED. This *anomaly* — a quantum-mechanical breaking of a classical symmetry — was discovered by Adler, Bell, and Jackiw in 1969 and explains the observed decay rate $\pi^0 \to \gamma\gamma$. Mathematically, the anomaly is the *index of the Dirac operator* on the spacetime manifold, and the Atiyah–Singer index theorem provides the precise coefficient. The chiral anomaly is the central example showing that classical chirality structures (left- vs right-handed Weyl spinors) are quantum-mechanically constrained — and is the foundation of all anomaly-related phenomena in modern physics.

> [!tip] Standard Model Chirality and the Weak Force
> The weak interaction in the Standard Model is **chiral**: the $W$ and $Z$ bosons couple only to left-handed fermions (and right-handed anti-fermions). This is parameterized by the **V-A** ("vector-minus-axial") current $\bar\psi\gamma^\mu(I - \gamma^5)\psi = 2\bar\psi_L\gamma^\mu\psi_L$. The right-handed components do not participate in weak interactions at all (except via the Higgs mechanism, which couples them to give mass). This explains **parity violation** in weak decays — a phenomenon that has no analog in the strong and electromagnetic forces and was one of the great surprises of 20th-century physics (Lee–Yang 1956, Wu 1957).

> [!tip] Spinor Helicity Formalism *(from QFT Computations)*
> Modern computations of scattering amplitudes in QFT use the **spinor helicity formalism**, which expresses external particle momenta as products of Weyl spinors. A massless 4-momentum factorizes as $p_{a\dot a} = \lambda_a \tilde\lambda_{\dot a}$ where $\lambda$ is a left-handed Weyl spinor and $\tilde\lambda$ is a right-handed Weyl spinor. This decomposition makes the BCFW (Britto–Cachazo–Feng–Witten) recursion relations possible, dramatically simplifying perturbative calculations and revealing surprising structures (the **CSW** rules, twistor amplitudes, the **amplituhedron** of Arkani-Hamed). The spinor helicity formalism is the practical face of Weyl spinors in 21st-century QFT.
