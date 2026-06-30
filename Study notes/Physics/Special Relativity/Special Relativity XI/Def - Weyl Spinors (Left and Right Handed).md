---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Spinor Map and SL(2,C)"
  - "Def - Pauli Matrices and the Hermitian-Matrix Correspondence"
  - "Def - Lie Algebra of the Lorentz Group"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus $\eta = \mathrm{diag}(1,-1,-1,-1)$. $A \in SL(2,\mathbb{C})$ is a Lorentz transformation in its $2\times 2$ form, acting on spacetime by the [[Def - The Spinor Map and SL(2,C)|spinor map]] $\underline X \mapsto A\underline X A^\dagger$. We write $A^\dagger$ for the conjugate transpose, $\overline A$ for entrywise conjugation, $A^{-\dagger} := (A^\dagger)^{-1}$, and $\boldsymbol\sigma = (\sigma_1,\sigma_2,\sigma_3)$ for the [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|Pauli matrices]]. A pair $(A,B)$ of non-negative half-integers labels a representation of the Lorentz group, as in [[Special Relativity X — The Lorentz Group as a Lie Group|the previous chapter]]'s $\mathfrak{so}(1,3)_{\mathbb C}\cong\mathfrak{su}(2)\oplus\mathfrak{su}(2)$. Full registry on [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]].

This is a compound page: it defines two interlocking notions — the **left-handed Weyl spinor** $(\tfrac12,0)$ and the **right-handed Weyl spinor** $(0,\tfrac12)$ — together with how complex conjugation swaps them and how their sum makes a Dirac spinor, because the two handedness types are only meaningful in contrast to each other.

---

# Axiom Motivation

The spinor map gives the Lorentz group two natural actions on $\mathbb{C}^2$ for free, and a spinor is, by definition, a vector carrying one of them. The motivation is to identify *what objects exist* once Lorentz transformations are $2\times 2$ matrices, and to see that the four-vector — the object of the whole sequence so far — is not the most fundamental.

The four-vector lives in the representation where $A$ acts by $\underline X \mapsto A\underline X A^\dagger$: two factors of $A$, one barred (in the dagger). This is a representation on the four real dimensions of $\mathrm{Herm}(2,\mathbb{C})$. But $A$ also acts, more simply, on $\mathbb{C}^2$ itself by $\xi \mapsto A\xi$ — one factor of $A$, no dagger. This is the **defining** or **fundamental** representation, and a vector carrying it is a **left-handed Weyl spinor**. It is "smaller" than the four-vector: two complex dimensions versus four real. The question that forces the *right-handed* spinor into existence is: is $\xi \mapsto A\xi$ the *only* two-dimensional representation, or are there inequivalent ones?

There are. The complex conjugate $\xi \mapsto \overline A\,\xi$ is also a representation of $SL(2,\mathbb{C})$ on $\mathbb{C}^2$, and it is *not* equivalent to the first. The inequivalence is the heart of the matter. For the rotation subgroup $SU(2)$ the two would be equivalent (every $SU(2)$ representation is equivalent to its conjugate, because $SU(2)$ is "self-conjugate"), and this is why non-relativistic quantum mechanics has only one kind of spinor. But the *boosts* break the equivalence: for a Hermitian boost matrix $A = \cosh\tfrac\psi2 I + \sinh\tfrac\psi2\,\mathbf n\cdot\boldsymbol\sigma$, the conjugate $\overline A$ differs from $A$ (because $\sigma_2$ is imaginary), and no fixed similarity transformation relates the two for all boosts. So relativity, by adding boosts, splits the single non-relativistic spinor into two inequivalent halves — left and right.

Why call the conjugate representation "$(A^\dagger)^{-1}$" rather than "$\overline A$"? Because the two are equivalent: for $A \in SL(2,\mathbb{C})$ one has $(A^\dagger)^{-1} = \varepsilon\,\overline A\,\varepsilon^{-1}$ with $\varepsilon = \begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix}$ (the antisymmetric "spinor metric," using $\det A = 1$). So $\xi \mapsto \overline A\xi$ and $\chi \mapsto (A^\dagger)^{-1}\chi$ are the same representation in different bases, and the latter form is the one that pairs naturally with the left spinor to build a four-vector. The choice is conventional; what is not conventional is that this conjugate representation is genuinely different from the defining one.

What goes wrong if we ignore the distinction and use only left spinors? Then we cannot build a Lorentz-invariant from a single spinor and its conjugate in the way the four-vector requires, and — physically — we cannot write a mass term or a parity-symmetric theory. A mass couples a left spinor to a right spinor; a theory of left spinors alone (a single Weyl fermion) is necessarily massless and parity-violating, which is exactly the structure of the neutrino in the Standard Model. The existence of *two* handedness types is therefore not bookkeeping; it is the origin of the distinction between massive (Dirac) and massless (Weyl) fermions, and of parity violation.

Finally, why is the four-vector the *combination* $(\tfrac12,\tfrac12)$? Because $\underline X = A\underline X A^\dagger$ carries one undaggered factor (a left index) and one daggered factor (a right index): a four-vector is a left spinor index times a right spinor index, $\underline X_{a\dot b}$, which is precisely the representation $(\tfrac12,0)\otimes(0,\tfrac12) = (\tfrac12,\tfrac12)$. The spinor is the square root of the vector.

---

# The Definition

Let $A \in SL(2,\mathbb{C})$ implement a restricted Lorentz transformation via the [[Def - The Spinor Map and SL(2,C)|spinor map]].

A **left-handed Weyl spinor** is a vector $\xi \in \mathbb{C}^2$ transforming under the Lorentz transformation by
$$
\xi \;\longmapsto\; A\,\xi,
$$
the defining (fundamental) representation, denoted $(\tfrac12, 0)$.

A **right-handed Weyl spinor** is a vector $\chi \in \mathbb{C}^2$ transforming by the conjugate representation
$$
\chi \;\longmapsto\; (A^\dagger)^{-1}\chi \;=\; A^{-\dagger}\chi,
$$
equivalent to $\chi \mapsto \overline A\,\chi$ via the spinor metric $\varepsilon = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$, and denoted $(0,\tfrac12)$. Equivalently, the right-handed representation is obtained from the left by sending rapidity $\psi \mapsto -\psi$ in the boost matrices while keeping the rotations unchanged: rotations act identically on both ($A \in SU(2)$ has $A^{-\dagger} = A$), boosts act oppositely.

The two are exchanged by **complex conjugation**: if $\xi$ is a left spinor then $\overline\xi$ transforms as a right spinor, and vice versa. There is no $SL(2,\mathbb{C})$-invariant way to turn a left spinor into a right one without conjugating, which is the precise statement that the two representations are inequivalent.

A **Dirac spinor** is the four-component object
$$
\Psi = \begin{pmatrix} \xi \\ \chi \end{pmatrix} \in \mathbb{C}^4
$$
formed from a left and a right Weyl spinor, carrying the reducible representation $(\tfrac12,0)\oplus(0,\tfrac12)$; **parity** (spatial reflection) exchanges the two blocks $\xi \leftrightarrow \chi$.

Under a rotation by angle $\theta$ about $\mathbf n$, both spinor types transform by $\exp(-\tfrac{i\theta}{2}\mathbf n\cdot\boldsymbol\sigma)$, so a rotation by $2\pi$ sends every spinor to its negative,
$$
\xi \;\longmapsto\; \exp(-i\pi\,\mathbf n\cdot\boldsymbol\sigma)\,\xi = -\xi,
$$
and a rotation by $4\pi$ returns it to itself.

---

# Categorical / Structural Definition

The structural statement is that the finite-dimensional representations of the (complexified) Lorentz group are classified by pairs $(A,B)$ with $A, B \in \{0, \tfrac12, 1, \tfrac32, \dots\}$, where $A$ is the spin under the "left" $\mathfrak{su}(2)$ and $B$ the spin under the "right" $\mathfrak{su}(2)$ in the decomposition $\mathfrak{so}(1,3)_{\mathbb C} \cong \mathfrak{su}(2)\oplus\mathfrak{su}(2)$ of [[Special Relativity X — The Lorentz Group as a Lie Group|the previous chapter]]. The dimension of $(A,B)$ is $(2A+1)(2B+1)$. The Weyl spinors are the two smallest nontrivial cases:
$$
(\tfrac12, 0)\ \text{= left Weyl}, \qquad (0, \tfrac12)\ \text{= right Weyl}, \qquad (\tfrac12,\tfrac12)\ \text{= four-vector}.
$$
The construction is the standard "highest-weight" classification of representations of a semisimple Lie algebra applied to $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$: irreducibles of a direct sum are external tensor products of irreducibles of the factors, and the irreducibles of $\mathfrak{su}(2)$ are the spin-$j$ representations, recovering the pair-of-spins label.

Two subtleties make this *only* a classification of the *complexified* algebra, and the real Lorentz group requires care. First, the two $\mathfrak{su}(2)$'s are not independent real subalgebras of $\mathfrak{so}(1,3)$ — they are complex-conjugate combinations $J_i \pm iK_i$ of the real rotation and boost generators — so a representation $(A,B)$ of the real Lorentz group must satisfy a reality condition relating $A$ and $B$ under conjugation, which is exactly why complex conjugation swaps $(\tfrac12,0)$ and $(0,\tfrac12)$. Second, the half-integer cases $(A,B)$ with $A + B$ half-integer are representations of the *cover* $SL(2,\mathbb{C})$ and not of $SO^+(1,3)$ itself — they are double-valued on the base — which is the representation-theoretic statement of "half-integer spin lives on the cover."

---

# Relate to Other Fields / Compression

The vault's [[Def - Weyl Spinor|Weyl spinor]] page (in the Clifford/Dirac notes) defines exactly this object from the spin-bundle perspective; the present page is its special-relativistic introduction, where the emphasis is on *why* there are two inequivalent handedness types (the boosts break the self-conjugacy that $SU(2)$ enjoys). The [[Def - The Dirac Equation|Dirac equation]] is the first-order wave equation that couples a left and a right Weyl spinor through a mass term, and its gamma matrices in the Weyl representation are block-off-diagonal precisely because they intertwine $(\tfrac12,0)$ and $(0,\tfrac12)$.

In quantum mechanics a single two-component spinor under the rotation subgroup is the **spin-½ wavefunction**, and the [[Def - SU(2) Action on Spinors|SU(2) action on spinors]] there is the restriction of the left (or right — they agree on $SU(2)$) Weyl representation to rotations. Relativity's contribution is the boosts, which split the one non-relativistic spinor into two.

**True name:** a Weyl spinor is "*the square root of a null vector*" — operationally, $\xi$ is the two-component object with $\underline X = \xi\xi^\dagger$ for a null $X$ (a left spinor) — and the handedness is "*which of the two factors of $A$ in $A\underline X A^\dagger$ acts on it*": the undaggered factor for left, the daggered factor for right. This is the form used on the [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)|celestial sphere]], where a null direction *is* a left Weyl spinor up to scale.

---

# Examples / Corollaries

**Is an instance — a momentum spinor.** For a massless particle with null four-momentum $P$, the Hermitian matrix $\underline P = \xi\xi^\dagger$ factors and $\xi$ (defined up to phase) is a left Weyl spinor, the "momentum spinor" of the particle. Under a Lorentz boost $A$, $\underline P \mapsto A\underline P A^\dagger$ corresponds to $\xi \mapsto A\xi$ — the spinor transforms by one factor of $A$, the momentum by two.

**Is an instance — a spin-½ state under rotation.** Restricting to rotations, a left Weyl spinor is a spin-½ wavefunction: $\xi = \begin{pmatrix}1\\0\end{pmatrix}$ is "spin up along $z$," and under a rotation by $\theta$ about $z$ it becomes $e^{-i\theta/2}\begin{pmatrix}1\\0\end{pmatrix}$, acquiring the half-angle phase.

**Is NOT an instance — a four-vector.** A four-vector $X$ is *not* a Weyl spinor: it transforms by $A\,(\cdot)\,A^\dagger$ (two factors), lives in $(\tfrac12,\tfrac12)$, and is unchanged by a $2\pi$ rotation. Confusing the two — applying $\xi \mapsto A\xi$ to a four-vector — is the error warned against on the topic page. A four-vector is a *pair* of spinor indices, one left and one right, not a single spinor.

**Is NOT an instance — a left spinor treated as a right spinor.** The vector $\xi = \begin{pmatrix}1\\0\end{pmatrix}$ transforms differently depending on whether it is declared left or right: under a $z$-boost $A = \mathrm{diag}(e^{\psi/2},e^{-\psi/2})$, a left spinor becomes $\begin{pmatrix}e^{\psi/2}\\0\end{pmatrix}$ (grows), while a right spinor becomes $A^{-\dagger}\begin{pmatrix}1\\0\end{pmatrix} = \mathrm{diag}(e^{-\psi/2},e^{\psi/2})\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}e^{-\psi/2}\\0\end{pmatrix}$ (shrinks). The same components carry opposite physics; the handedness label is essential.

**Corollary — a single Weyl fermion is massless.** A mass term couples $\xi$ to $\chi$ (it must, to be Lorentz invariant, since $\xi^\dagger\chi$ is a scalar but $\xi^\dagger\xi$ is not). With only a left spinor and no right partner, no Lorentz-invariant mass can be written, so a lone Weyl fermion is necessarily massless — the structure of the neutrino.

**Corollary — the $4\pi$ return.** Since a $2\pi$ rotation gives $\xi \mapsto -\xi$, two full turns give $\xi \mapsto (-1)^2\xi = \xi$. An object built from spinors returns to itself only after $720^\circ$, an experimentally confirmed fact (neutron interferometry) and a direct consequence of $\exp(-i\pi\,\mathbf n\cdot\boldsymbol\sigma) = -I$.

**Calibration check.** If you have understood this page you should be able to: (1) state the transformation law of a left and a right Weyl spinor under a general $A \in SL(2,\mathbb{C})$, and explain why they agree under rotations but differ under boosts; (2) explain why a four-vector is unchanged by a $2\pi$ rotation but a Weyl spinor is not; (3) say in one sentence why a single Weyl spinor cannot have a mass.

---

# Unlocked by This

> [!tip] The Dirac Equation and Antimatter *(from Relativistic Quantum Mechanics)*
> Coupling a left and a right Weyl spinor through the mass and the momentum gives the **Dirac equation** $(i\gamma^\mu\partial_\mu - m)\Psi = 0$ for the four-component $\Psi = (\xi,\chi)$; see [[Def - The Dirac Equation]]. The doubling of components that the two handedness types force is what predicts the existence of **antimatter** — the negative-energy solutions reinterpreted as positrons — and the gamma matrices' block structure is the off-diagonal coupling $(\tfrac12,0)\leftrightarrow(0,\tfrac12)$.

> [!tip] Parity Violation and the Neutrino *(from Particle Physics)*
> Because left and right Weyl spinors are genuinely inequivalent, a theory can treat them asymmetrically — coupling only the left-handed components to the weak force. This **parity violation** is built into the Standard Model, and a particle with only a left-handed component (no right partner) is necessarily massless, the original model of the **neutrino**. The inequivalence derived on this page is the structural reason parity is not a symmetry of the weak interaction.

> [!tip] Field Representations and Wigner's Classification *(from Quantum Field Theory)*
> The pair-of-spins label $(A,B)$ extends beyond spinors: $(0,0)$ is a scalar field, $(\tfrac12,\tfrac12)$ a vector, $(1,0)\oplus(0,1)$ the electromagnetic field strength. Combined with the mass and spin **Casimirs of the Poincaré group** ([[Def - Casimir Invariants of the Poincaré Group]]), this classifies every relativistic field and particle; the Weyl spinors are the irreducible building blocks, and the half-integer cases are exactly those that live on the cover $SL(2,\mathbb{C})$. See [[Special Relativity XII — Inertial Observers and the Poincaré Group]].
