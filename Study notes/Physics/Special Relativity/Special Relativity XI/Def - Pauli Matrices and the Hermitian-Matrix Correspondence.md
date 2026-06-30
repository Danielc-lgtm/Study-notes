---
type: definition
subject: special-relativity
prereqs:
  - "Def - Minkowski Space and the Metric"
  - "Def - Four-Vector"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, so a four-vector $X$ has $X\cdot X = (x^0)^2 - (x^1)^2 - (x^2)^2 - (x^3)^2$ with $x^0 = t$. A $2\times 2$ complex matrix $H$ is **Hermitian** if $H^\dagger = H$, where $H^\dagger = \overline{H}^{\mathsf T}$ is the conjugate transpose; $\mathrm{Herm}(2,\mathbb{C})$ is the set of such matrices. $\delta_{ij}$ is the Kronecker delta and $\varepsilon_{ijk}$ the totally antisymmetric Levi-Civita symbol with $\varepsilon_{123} = +1$. Latin indices $i,j,k$ run over $1,2,3$; Greek $\mu,\nu$ over $0,1,2,3$. Full registry on [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]].

This is a compound page: it defines two interlocking notions — the **Pauli matrices** (with their multiplication law) and the **Hermitian-matrix correspondence** $\mathscr{H}$ between four-vectors and $2\times 2$ Hermitian matrices — because the correspondence is built out of the Pauli matrices and neither is usable without the other.

---

# Axiom Motivation

The chapter wants to act on spacetime with $2\times 2$ complex matrices, and for that it first needs a faithful way to *write* a spacetime event as a $2\times 2$ matrix. The design question is: what kind of $2\times 2$ matrix should encode a four-vector $(t,x,y,z)$, and which matrices should the four basis directions go to?

Begin by counting. A four-vector has four real degrees of freedom. A general $2\times 2$ complex matrix has eight (four complex entries), too many; a real symmetric one has three, too few. The class of matrices with exactly four real degrees of freedom — no more, no less — is the **Hermitian** matrices $H^\dagger = H$: the two diagonal entries are forced to be real (two real numbers), and the off-diagonal entries are conjugates of each other (one complex number, two real numbers), giving $2 + 2 = 4$. This is the unique natural class matching the dimension of $\mathbb{R}^4$, so the correspondence must land in $\mathrm{Herm}(2,\mathbb{C})$. That Hermitian matrices form a *real* vector space (closed under real but not complex scalar multiplication, since multiplying a Hermitian matrix by $i$ makes it anti-Hermitian) is exactly right: spacetime is a real vector space.

Now we need a basis of $\mathrm{Herm}(2,\mathbb{C})$ to assign to the four coordinate directions $e_0, e_1, e_2, e_3$. The choice is not free if we want the second, decisive property: that the Minkowski interval $X\cdot X$ should equal the determinant $\det\underline X$. The determinant of a Hermitian matrix $\begin{pmatrix} a & b \\ \bar b & d\end{pmatrix}$ is $ad - |b|^2$ with $a,d$ real, and we want this to come out as $(x^0)^2 - (x^1)^2 - (x^2)^2 - (x^3)^2$. Writing the matrix as $x^0\sigma_0 + x^1\sigma_1 + x^2\sigma_2 + x^3\sigma_3$ and demanding the determinant be the Minkowski quadratic form forces the diagonal direction $\sigma_0$ to be the identity (so $x^0$ sits symmetrically on the diagonal, contributing $+(x^0)^2$) and forces $\sigma_3 = \mathrm{diag}(1,-1)$ (so $x^3$ splits the diagonal, contributing $-(x^3)^2$). The two off-diagonal directions $\sigma_1, \sigma_2$ must between them produce the term $-|b|^2 = -((x^1)^2 + (x^2)^2)$, which pins them to the real and imaginary off-diagonal Hermitian matrices $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ and $\begin{pmatrix}0&-i\\i&0\end{pmatrix}$. These are the **Pauli matrices**, and they are not a convention plucked from quantum mechanics but the unique Hermitian basis making the interval a determinant.

The third property the Pauli matrices must supply, used everywhere downstream, is a clean *multiplication* law, because all the exponentials that build rotations and boosts depend on knowing $\sigma_i\sigma_j$. What breaks if the multiplication law were ugly? Nothing about the correspondence itself, but the entire exponential machinery of [[Def - Lie Algebra sl(2,C) and the Exponential Map]] would not close into $\cos/\sin$ and $\cosh/\sinh$. The miracle is that the same three matrices forced on us by the determinant requirement happen to satisfy $\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k$, so that $(\mathbf n\cdot\boldsymbol\sigma)^2 = I$ for any unit vector — exactly the condition that makes the exponential series telescope. This is not a separate axiom; it is a consequence, and its discovery is what makes the Pauli matrices worth singling out.

One could ask why not use anti-Hermitian matrices, or some other normalisation. Anti-Hermitian matrices also form a four-dimensional real space, but the determinant of an anti-Hermitian matrix is $|b|^2 - ad$ up to sign and does not as cleanly give the mostly-minus interval; more importantly, Hermitian matrices are the ones preserved by the congruence $H \mapsto AHA^\dagger$, which is the action we are about to use. The normalisation $\det\sigma_i = -1$, $\mathrm{tr}\,\sigma_i = 0$, $\sigma_i^2 = I$ is the one that makes both the interval-as-determinant and the multiplication law come out without stray factors.

---

# The Definition

The **Pauli matrices** are the four $2\times 2$ complex matrices
$$
\sigma_0 = I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad
\sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad
\sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.
$$
Each is Hermitian, $\sigma_\mu^\dagger = \sigma_\mu$; the three $\sigma_i$ ($i = 1,2,3$) are traceless with determinant $-1$ and square to the identity, $\sigma_i^2 = I$. Together $(\sigma_0,\sigma_1,\sigma_2,\sigma_3)$ form a real basis of the four-dimensional real vector space $\mathrm{Herm}(2,\mathbb{C})$.

The **multiplication law** of the three traceless Pauli matrices is
$$
\sigma_i\,\sigma_j \;=\; \delta_{ij}\,I \;+\; i\,\varepsilon_{ijk}\,\sigma_k,
$$
which packages the anticommutator $\{\sigma_i,\sigma_j\} = 2\delta_{ij}I$ and the commutator $[\sigma_i,\sigma_j] = 2i\varepsilon_{ijk}\sigma_k$ in one line. An immediate consequence is that for any Euclidean unit vector $\mathbf n = (n^1,n^2,n^3)$ with $\sum_i (n^i)^2 = 1$,
$$
(\mathbf n\cdot\boldsymbol\sigma)^2 \;=\; n^i n^j \sigma_i\sigma_j \;=\; n^i n^j \delta_{ij} I \;=\; I,
\qquad (i\,\mathbf n\cdot\boldsymbol\sigma)^2 = -I,
$$
where $\mathbf n\cdot\boldsymbol\sigma := n^i\sigma_i$ and the antisymmetric $\varepsilon_{ijk}$ term drops out against the symmetric $n^i n^j$.

The **Hermitian-matrix correspondence** is the real-linear map
$$
\mathscr{H} : \mathbb{R}^{1,3} \longrightarrow \mathrm{Herm}(2,\mathbb{C}), \qquad
X = x^\mu e_\mu \;\longmapsto\; \underline X = x^\mu\sigma_\mu
= \begin{pmatrix} x^0 + x^3 & x^1 - i x^2 \\ x^1 + i x^2 & x^0 - x^3 \end{pmatrix}.
$$
It is a linear isomorphism, with inverse given by
$$
x^0 = \tfrac12\,\mathrm{tr}\,\underline X, \qquad x^i = \tfrac12\,\mathrm{tr}\big(\sigma_i\,\underline X\big),
$$
and it carries the Minkowski interval to the determinant:
$$
\det\underline X \;=\; (x^0)^2 - (x^1)^2 - (x^2)^2 - (x^3)^2 \;=\; X\cdot X.
$$

---

# Categorical / Structural Definition

Structurally, $\mathscr{H}$ is an isomorphism of *quadratic spaces*: it identifies the real four-dimensional space $\mathbb{R}^{1,3}$ carrying the Minkowski quadratic form $Q(X) = X\cdot X$ with the real four-dimensional space $\mathrm{Herm}(2,\mathbb{C})$ carrying the determinant quadratic form $Q'(H) = \det H$. A quadratic space is a vector space with a quadratic form, and an isomorphism of quadratic spaces is a linear bijection intertwining the forms, $Q'(\mathscr{H}(X)) = Q(X)$. The determinant is genuinely a quadratic form on $\mathrm{Herm}(2,\mathbb{C})$ — it is degree two and homogeneous — and its signature, by direct computation on the basis $(\sigma_0,\sigma_1,\sigma_2,\sigma_3)$ where $\det\sigma_0 = +1$ and $\det\sigma_i = -1$, is $(1,3)$. By Sylvester's law of inertia two real quadratic spaces of the same dimension are isomorphic exactly when their forms have the same signature, so the *existence* of an isomorphism $\mathbb{R}^{1,3} \cong (\mathrm{Herm}(2,\mathbb{C}),\det)$ is guaranteed the moment one checks the signature is $(1,3)$ on both sides; the Pauli matrices provide the explicit isomorphism.

This is the conceptual reason the spinor map exists. The automorphism group of the quadratic space $(\mathbb{R}^{1,3}, X\cdot X)$ is the Lorentz group $O(1,3)$; the automorphism group of $(\mathrm{Herm}(2,\mathbb{C}),\det)$ contains every map of the form $H \mapsto AHA^\dagger$ with $\det A = 1$. The functor "automorphism group of the quadratic space" sends the isomorphism $\mathscr{H}$ to an isomorphism of groups, and tracing through it is what produces $\mathscr{S} : SL(2,\mathbb{C}) \to SO^+(1,3)$ in [[Def - The Spinor Map and SL(2,C)]]. The accident that powers all of this is dimensional: it is only in four spacetime dimensions that the orthogonal group of the interval coincides (up to cover) with a group of $2\times 2$ matrices, because it is only here that the interval is the determinant form on a $2\times 2$ Hermitian space.

---

# Relate to Other Fields / Compression

In quantum mechanics the same three matrices $\sigma_1,\sigma_2,\sigma_3$ are the **spin operators** of a spin-½ particle, normalised as $S_i = \tfrac12\sigma_i$, with the commutator $[\sigma_i,\sigma_j] = 2i\varepsilon_{ijk}\sigma_k$ becoming the angular-momentum algebra $[S_i,S_j] = i\varepsilon_{ijk}S_k$. The vault's [[Def - The Pauli Matrices|Pauli matrices]] page (in the Clifford/Dirac notes) and its [[Ex - Pauli Matrices Generate Cl(R^3)|generation of the Clifford algebra]] develop exactly this algebra; the present page is the special-relativistic face of the same object, where the *fourth* matrix $\sigma_0 = I$ is added so that the three spatial Pauli matrices and the time identity together span a Hermitian basis matching the four spacetime directions.

The multiplication law $\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k$ is precisely the statement that the Pauli matrices generate the **Clifford algebra** $\mathrm{Cl}(3)$ of Euclidean three-space: the anticommutator part $\{\sigma_i,\sigma_j\} = 2\delta_{ij}I$ is the defining Clifford relation $v w + w v = 2\langle v,w\rangle$. So this page is, compressed, "the Clifford algebra of $\mathbb{R}^3$ in its $2\times 2$ matrix realisation, plus the identity," and the interval-as-determinant is the four-dimensional Lorentzian extension of that Clifford structure.

**True name:** the operational characterisation of the correspondence is "*an event is a $2\times 2$ Hermitian matrix whose determinant is its interval*." When solving problems you never reconstruct $\mathscr{H}$ from the basis; you write $\underline X = \begin{pmatrix} t+z & x-iy \\ x+iy & t-z\end{pmatrix}$, take its determinant to get $t^2 - x^2 - y^2 - z^2$, and act by congruence. The trace formulas $x^0 = \tfrac12\mathrm{tr}\,\underline X$, $x^i = \tfrac12\mathrm{tr}(\sigma_i\underline X)$ are the operational inverse.

---

# Examples / Corollaries

**Is an instance — a generic timelike vector.** The four-velocity of a particle at rest, $U = (1,0,0,0)$, maps to $\underline U = \sigma_0 = I$, with $\det I = 1 = U\cdot U$ (the four-velocity is a unit timelike vector). A particle moving with $U = (\gamma, \gamma v, 0, 0)$ maps to $\underline U = \begin{pmatrix}\gamma & \gamma v \\ \gamma v & \gamma\end{pmatrix}$, with determinant $\gamma^2 - \gamma^2 v^2 = \gamma^2(1-v^2) = 1$, again the unit norm.

**Is an instance — a null vector.** The null vector $X = (1,0,0,1)$ (a light ray along $+z$) maps to $\underline X = \begin{pmatrix}2 & 0 \\ 0 & 0\end{pmatrix}$, with $\det\underline X = 0 = X\cdot X$. A rank-one Hermitian matrix always has zero determinant, so null vectors correspond exactly to the rank-deficient Hermitian matrices — the fact exploited in [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)]] to write $\underline X = \xi\xi^\dagger$.

**Is NOT an instance — a non-Hermitian matrix.** The matrix $\begin{pmatrix}1 & i \\ 0 & 1\end{pmatrix}$ is not Hermitian (its adjoint is $\begin{pmatrix}1 & 0 \\ -i & 1\end{pmatrix} \neq$ itself), so it does not correspond to any real four-vector under $\mathscr{H}$. Its determinant is $1$, but it has no interpretation as a spacetime event; the correspondence is with Hermitian matrices only, and a general complex matrix carries eight real parameters rather than four.

**Is NOT an instance — the wrong basis assignment.** If one (mistakenly) assigned $x^3$ to the off-diagonal real matrix and $x^1$ to $\mathrm{diag}(1,-1)$, the determinant would still be a quadratic form of signature $(1,3)$, so the *existence* of a valid correspondence would survive — but $\det\underline X$ would no longer equal the *standard* interval with $x^1$ measuring the first spatial axis. The specific Pauli assignment $\sigma_1, \sigma_2, \sigma_3 \leftrightarrow x^1, x^2, x^3$ is what makes $\det\underline X = X\cdot X$ in the usual coordinates; any permutation of the spatial labels is an orthogonal relabelling but the convention above is the standard one.

**Corollary — Hermiticity is preserved by congruence.** For any $A$ and any Hermitian $H$, the matrix $AHA^\dagger$ is Hermitian: $(AHA^\dagger)^\dagger = A H^\dagger A^\dagger = AHA^\dagger$. This is why the spinor map's action $\underline X \mapsto A\underline X A^\dagger$ stays inside $\mathrm{Herm}(2,\mathbb{C})$ and hence corresponds to a genuine four-vector transformation.

**Corollary — the trace recovers the time component frame-independently up to the action.** Since $\mathrm{tr}\,\sigma_i = 0$ and $\mathrm{tr}\,\sigma_0 = 2$, the trace formula $x^0 = \tfrac12\mathrm{tr}\,\underline X$ extracts the time component; combined with $\det\underline X = X\cdot X$ this gives a quick check on any computed $\underline X$.

**Calibration check.** If you have understood this page you should be able to: (1) write down $\underline X$ for the event $(2,1,0,-1)$ and verify $\det\underline X = 4 - 1 - 0 - 1 = 2$ equals $X\cdot X$; (2) verify $\sigma_1\sigma_2 = i\sigma_3$ directly by multiplying the matrices, confirming the multiplication law; (3) explain in one sentence why $(\mathbf n\cdot\boldsymbol\sigma)^2 = I$ but $(\mathbf n\cdot\boldsymbol\sigma)^3 = \mathbf n\cdot\boldsymbol\sigma$ for a unit $\mathbf n$.

---

# Unlocked by This

> [!tip] The Spinor Map *(from §11.1)*
> With four-vectors realised as Hermitian matrices and the interval realised as a determinant, the congruence action $\underline X \mapsto A\underline X A^\dagger$ of [[Def - The Spinor Map and SL(2,C)]] automatically preserves the interval whenever $\det A = 1$, delivering a Lorentz transformation from every $SL(2,\mathbb{C})$ matrix — the spinor map.

> [!tip] The Clifford Algebra and Gamma Matrices *(from Spin Geometry)*
> The anticommutator $\{\sigma_i,\sigma_j\} = 2\delta_{ij}I$ is the defining relation of the **Clifford algebra** $\mathrm{Cl}(3)$, and the four-dimensional Lorentzian analogue $\{\gamma_\mu,\gamma_\nu\} = 2\eta_{\mu\nu}I$ defines the **gamma matrices** of the Dirac equation. The Pauli matrices are the building blocks: in the Weyl representation the $4\times 4$ gamma matrices are assembled from $\sigma_\mu$ and $\bar\sigma_\mu = (\sigma_0, -\sigma_i)$ in off-diagonal blocks, which is the bridge from this page to [[Def - The Dirac Equation]].

> [!tip] Spin Angular Momentum *(from Quantum Mechanics)*
> Reading $S_i = \tfrac12\sigma_i$ as operators on $\mathbb{C}^2$ makes the multiplication law's commutator part $[\sigma_i,\sigma_j] = 2i\varepsilon_{ijk}\sigma_k$ into the **spin angular momentum algebra** $[S_i,S_j] = i\varepsilon_{ijk}S_k$, with $S^2 = \tfrac34 I$ the eigenvalue $s(s+1)$ for $s = \tfrac12$. The same matrices that label spacetime directions here are the observables of a spin-½ particle, the deepest reason the two subjects share a formalism.
