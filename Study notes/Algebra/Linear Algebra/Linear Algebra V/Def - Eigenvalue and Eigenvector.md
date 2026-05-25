---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Linear Map"
  - "Def - Invariant Subspace"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over a field $F$ (almost always $\mathbb{R}$ or $\mathbb{C}$), $T \in \mathcal{L}(V)$ is an operator on $V$, and $I \in \mathcal{L}(V)$ is the identity operator. Scalars $\lambda, \mu \in F$ are called **eigenvalues** when associated to nonzero invariant directions. The set of all eigenvectors of $T$ for the eigenvalue $\lambda$, together with the zero vector, forms the **eigenspace** $E(\lambda, T) = \ker(T - \lambda I)$. The full registry is on the parent page [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

This is a compound page: it defines the **eigenvalue**, the **eigenvector**, and the **eigenspace**, plus several equivalent characterizations — these are introduced together because none of them is fully usable without the others.

---

# Axiom Motivation

The motivation comes directly from the previous definition: the simplest non-trivial invariant [[Def - Subspace|subspace]] is one-dimensional, and on a one-dimensional invariant [[Def - Subspace|subspace]] $U = \operatorname{span}(v)$ with $v \neq 0$, the operator $T$ must act as a scalar (it has nowhere else to map a vector). So $Tv = \lambda v$ for some $\lambda \in F$. The scalar $\lambda$ is the **eigenvalue** and $v$ (which must be nonzero, because we want $U$ to be a one-dimensional subspace) is the **eigenvector**. The definition is the formalisation of this geometric fact.

The constraint $v \neq 0$ is not optional. Without it, every scalar $\lambda \in F$ would satisfy $T(0) = \lambda \cdot 0$, so the zero vector would be an "eigenvector" for every scalar simultaneously, and the definition would lose its discriminatory content. The nonzero condition is exactly what makes "eigenvalue" a property of $T$ rather than a property of every scalar.

Why is the eigenvalue $\lambda$ required to lie in $F$, the same field as the scalars of $V$? Because if $\lambda$ were in a larger field, the equation $Tv = \lambda v$ would not even make sense — multiplication of $v$ by $\lambda$ would require $\lambda$ to act on $V$, and $V$'s scalar action is by definition by elements of $F$. This is the source of the *field-dependence* of the eigenvalue: a real operator can have no real eigenvalues but pick up complex ones after **complexification** — extending the scalars from $\mathbb{R}$ to $\mathbb{C}$ to make the equation legal.

The four-fold characterisation of an eigenvalue — $\lambda$ is an eigenvalue $\iff$ $T - \lambda I$ has a nonzero kernel $\iff$ $T - \lambda I$ is not injective $\iff$ $T - \lambda I$ is not surjective $\iff$ $T - \lambda I$ is not invertible — is the bridge between the geometric and algebraic views. The geometric view ("there is a nonzero $v$ with $Tv = \lambda v$") gives intuition; the algebraic views ("$T - \lambda I$ fails to be invertible") give computational handles. The equivalence rests on [[Thm - Injectivity Equals Surjectivity in Finite Dimensions|injectivity = surjectivity in finite dimensions]] (a consequence of the rank-nullity theorem) — this is one place where the finite-dimensional hypothesis matters: in infinite [[Def - Dimension|dimensions]], an operator can be injective but not surjective and so have no eigenvalues even though the natural target space (the spectrum) is nontrivial.

The eigenspace $E(\lambda, T) = \ker(T - \lambda I)$ packages all eigenvectors for $\lambda$, plus the zero vector, into a single subspace. This packaging is what makes the notion algebraically useful: $E(\lambda, T)$ is a subspace (a closed object under linear operations), whereas the set of eigenvectors alone is not (it lacks zero, which we excluded by definition). The eigenspace is automatically $T$-invariant (since $T$ acts on it as the scalar $\lambda$), so the eigenspace decomposition $\bigoplus_k E(\lambda_k, T)$ — when it exists — is the canonical example of a direct-sum decomposition into invariant pieces.

A subtle distinction: an eigenvalue $\lambda$ has an associated **multiplicity**, which can be measured in two ways. The **geometric multiplicity** is $\dim E(\lambda, T)$ — how many linearly independent eigenvectors there are. The **algebraic multiplicity** (defined later, once one has the characteristic polynomial) is the multiplicity of $\lambda$ as a root of the characteristic polynomial. These are equal when $T$ is diagonalizable and differ by Jordan-block sizes when $T$ is not. In this chapter we have only the geometric multiplicity, so when we say "the eigenspace has dimension $k$" we are giving the geometric multiplicity.

Why is the existence of eigenvalues a non-trivial question? Because the equation $Tv = \lambda v$ is highly constrained: it asks for a *direction* (a one-dimensional subspace) on which $T$ behaves as a scalar. Most operators fail to have such a direction over $\mathbb{R}$ — any rotation by an angle other than $0$ or $\pi$ is a counterexample. Over $\mathbb{C}$, the [[Thm - Existence of Eigenvalues on Complex Vector Spaces|existence-of-eigenvalues theorem]] guarantees the failure cannot occur, but this is genuinely a theorem with non-trivial content (its proof requires the fundamental theorem of algebra, which is itself a theorem of complex analysis). The geometric intuition that "every operator has at least one fixed line" turns out to be true over $\mathbb{C}$ but false over $\mathbb{R}$.

---

# The Definition

Let $V$ be a vector space over $F$ and let $T \in \mathcal{L}(V)$.

**Eigenvalue.** A scalar $\lambda \in F$ is an **eigenvalue** of $T$ if there exists a nonzero vector $v \in V$ such that
$$Tv = \lambda v.$$

**Eigenvector.** A nonzero vector $v \in V$ is an **eigenvector** of $T$ corresponding to the eigenvalue $\lambda$ if $Tv = \lambda v$. (The condition $v \neq 0$ is part of the definition: zero is never an eigenvector.)

**Eigenspace.** For $\lambda \in F$, the **eigenspace** of $T$ corresponding to $\lambda$ is
$$E(\lambda, T) = \ker(T - \lambda I) = \{v \in V : Tv = \lambda v\}.$$
This is a subspace of $V$. $\lambda$ is an eigenvalue if and only if $E(\lambda, T) \neq \{0\}$. The eigenspace consists of all eigenvectors for $\lambda$ together with the zero vector.

**Equivalent characterizations (finite-dimensional case).** When $V$ is finite-dimensional, the following are equivalent:

(a) $\lambda$ is an eigenvalue of $T$;
(b) $T - \lambda I$ is not injective;
(c) $T - \lambda I$ is not surjective;
(d) $T - \lambda I$ is not invertible;
(e) $E(\lambda, T) = \ker(T - \lambda I) \neq \{0\}$.

The equivalences (b) $\iff$ (c) $\iff$ (d) follow from [[Thm - Injectivity Equals Surjectivity in Finite Dimensions]]; (a) $\iff$ (e) is just unpacking definitions; (a) $\iff$ (b) is "$Tv = \lambda v \iff (T - \lambda I)v = 0$".

---

# Categorical / Structural Definition

In the language of $F[x]$-[[Def - Module|modules]] — $V$ with $x$ acting as $T$ — an eigenvalue is a $\lambda \in F$ such that the **prime ideal** $(x - \lambda) \subseteq F[x]$ is in the **support** of the [[Def - Module|module]] $V$, equivalently such that $V \otimes_{F[x]} F[x]/(x - \lambda) \neq 0$. The eigenspace $E(\lambda, T)$ is the **[[Def - Submodule|submodule]] annihilated by $(x - \lambda)$**, equivalently the $F[x]/(x - \lambda) \cong F$-isotypic component of the socle.

This sounds elaborate, but it explains the deeper structure. An eigenvector for $\lambda$ is a nonzero element of $V$ on which $x - \lambda$ acts as $0$ — that is, an element of the simple submodule $F[x]/(x - \lambda) \cdot v \cong F$. The eigenspace $E(\lambda, T)$ is the sum of all such simple [[Def - Submodule|submodules]] sharing the eigenvalue $\lambda$.

In the [[Def - The Module of a Linear Operator|F[x]-module V_T]] viewpoint, the structure theorem decomposes $V_T$ as a sum of cyclic pieces $F[x]/(p^k)$ for $p$ irreducible. The piece $F[x]/((x - \lambda)^k)$ corresponds to a Jordan block of size $k$ for the eigenvalue $\lambda$. The eigenspace $E(\lambda, T)$ is then the sum of the **socles** $\ker(x - \lambda)$ of these Jordan-block pieces — and each Jordan block contributes exactly one dimension to the eigenspace. So the geometric multiplicity of $\lambda$ equals the number of Jordan blocks for $\lambda$, and the algebraic multiplicity (to be defined later via the characteristic polynomial) equals the sum of the Jordan block sizes.

The categorical view also explains why eigenvalues lie in $F$ (the field of scalars) and not in some extension: the prime [[Def - Ideal|ideals]] of $F[x]$ of the form $(x - \lambda)$ are exactly those with [[Def - Residue|residue]] field $F$. Other prime [[Def - Ideal|ideals]] of $F[x]$ — say $(x^2 + 1) \subseteq \mathbb{R}[x]$ — have larger [[Def - Residue|residue]] fields ($\mathbb{C}$ in this case) and correspond to "Galois-conjugate pairs of eigenvalues" that an operator can have over the algebraic closure but not over $F$.

---

# Relate to Other Fields / Compression

**True name.** An eigenvector is **a nonzero vector whose span is a one-dimensional $T$-invariant subspace**. The eigenvalue is the scalar by which $T$ acts on that line. This is the operational characterisation that makes most problems tractable: when looking for an eigenvector, look for a structurally distinguished line in $V$ that $T$ preserves (a fixed axis, a privileged direction, a structural line); when computing eigenvalues, use the kernel characterisation $\ker(T - \lambda I) \neq 0$ to convert the search into a linear-algebra calculation.

In **physics and quantum mechanics**, eigenvalues are the **observable values** of a self-adjoint operator (the Hamiltonian, position, momentum, angular momentum), and eigenvectors are the **stationary states** in which that observable has a definite value. The spectral theorem decomposes any self-adjoint operator into its eigenspaces; the eigenvalues are real (this is the [[Ex - Self-adjoint operators have real eigenvalues|standard exercise]]), and the eigenvectors of distinct eigenvalues are orthogonal. The whole framework of quantum measurement is the linear-algebraic study of eigenvalues and eigenspaces, with the additional structure of an inner product. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]].

In **dynamical systems**, eigenvalues of a linear map $T$ govern the **long-term behaviour** of iteration. If $T : \mathbb{R}^n \to \mathbb{R}^n$ has all eigenvalues of absolute value less than $1$, every trajectory contracts to $0$; if any eigenvalue has absolute value greater than $1$, generic trajectories explode along the corresponding eigenvector direction. The "spectral radius" $\max |\lambda|$ controls the asymptotic growth rate, and is the source of the entire theory of stability. The same idea, applied to the [[Def - The Total Derivative and Differentiability|Jacobian]] of a nonlinear map at a fixed point, gives the **Hartman-Grobman theorem**: near a hyperbolic fixed point, the nonlinear dynamics is topologically conjugate to the linearisation.

In **statistics and data analysis**, eigenvalues of a **covariance matrix** measure the variance along the corresponding eigenvector directions. **Principal component analysis** (PCA) is the diagonalisation of the covariance matrix; the principal components are eigenvectors, the explained variances are eigenvalues. The whole subject of high-dimensional data analysis takes eigenvalues as central invariants.

In **graph theory**, eigenvalues of the **adjacency matrix** of a graph encode structural properties — connectivity, expansion, the chromatic number, the number of spanning trees. Spectral graph theory is built on the observation that the eigenvalues of these natural matrices are highly informative about combinatorial structure.

---

# Examples / Corollaries

**The identity operator: every nonzero vector is an eigenvector for $1$.** $I : V \to V$ satisfies $Iv = 1 \cdot v$ for every $v$, so every nonzero vector is an eigenvector with eigenvalue $1$. The eigenspace $E(1, I) = V$ is the whole space. This is the extreme of "many eigenvectors": the operator has only one eigenvalue, but its eigenspace fills everything.

**The zero operator: every nonzero vector is an eigenvector for $0$.** $0 : V \to V$ has $E(0, 0) = V$. So every nonzero vector is a $0$-eigenvector.

**A scalar operator: same as identity, scaled.** $\lambda I$ has $E(\lambda, \lambda I) = V$ and no other eigenvalues. *(Calibration check.)*

**Rotation on $\mathbb{R}^2$ by $90°$: no real eigenvalues.** Let $T(x, y) = (-y, x)$. The equation $T(x, y) = \lambda(x, y)$ becomes $-y = \lambda x$ and $x = \lambda y$, so $x = -\lambda^2 x$, hence $(1 + \lambda^2) x = 0$. Over $\mathbb{R}$, $1 + \lambda^2 = 0$ has no solution, so $x = 0$ and then $y = 0$ — no nonzero $v$ exists. Over $\mathbb{C}$, $\lambda^2 = -1$ gives $\lambda = \pm i$, and the eigenvectors are $(1, -i)$ for $i$ and $(1, i)$ for $-i$. The example shows the field-dependence of eigenvalues sharply.

**Differentiation on $\mathcal{P}(\mathbb{R})$: only $0$ is an eigenvalue.** $D : \mathcal{P}(\mathbb{R}) \to \mathcal{P}(\mathbb{R})$, $Dp = p'$, has $Dp = \lambda p$ exactly when $p$ is a non-constant polynomial that equals $\lambda$ times its derivative — but $\deg p' = \deg p - 1$ for nonzero non-constant $p$, so $\deg p = \deg p' = \deg p - 1$, contradiction unless $\lambda = 0$ and $p$ is constant. So $E(0, D) =$ constants, and there are no other eigenvalues. See [[Ex - The differentiation operator on polynomials has eigenvalue zero only]].

**Projection: eigenvalues $0$ and $1$.** Let $V = U \oplus W$ and $P(u + w) = u$ the projection onto $U$ along $W$. Then $P u = u$ for $u \in U$ (eigenvalue $1$) and $Pw = 0$ for $w \in W$ (eigenvalue $0$). So $E(1, P) = U$, $E(0, P) = W$, and $V = E(1, P) \oplus E(0, P)$ — $P$ is diagonalizable with eigenvalues $0$ and $1$. *(Calibration check.)*

**Non-example: the right-shift on $F^\infty$ has no eigenvalues.** Let $V = F^\infty$ (sequences) and $T(z_1, z_2, \ldots) = (0, z_1, z_2, \ldots)$. The equation $Tz = \lambda z$ says $(0, z_1, z_2, \ldots) = (\lambda z_1, \lambda z_2, \ldots)$, so $\lambda z_1 = 0$ and $z_k = \lambda z_{k+1}$ for $k \geq 1$. If $\lambda \neq 0$, the first equation gives $z_1 = 0$ and the recurrence then forces every $z_k = 0$. If $\lambda = 0$, again $z_k = 0$ for all $k$. So the only $z$ satisfying the eigenvalue equation is $z = 0$, and $T$ has no eigenvalues. This shows that the existence-of-eigenvalues theorem is genuinely a finite-dimensional statement; in infinite [[Def - Dimension|dimensions]], even on a complex vector space, operators can have no eigenvalues at all. The right-shift has spectrum equal to the closed unit disk, but no point spectrum — the spectrum is "purely continuous" in functional-analysis language.

**Eigenvectors for distinct eigenvalues are linearly independent.** If $Tv = \lambda v$ and $Tw = \mu w$ with $v, w \neq 0$ and $\lambda \neq \mu$, then $v$ and $w$ are linearly independent. The reason is one of the cleanest one-step arguments in linear algebra: if $av + bw = 0$ with $a, b$ not both zero, apply $T - \mu I$ to get $a(\lambda - \mu)v = 0$; since $\lambda \neq \mu$ and $v \neq 0$, $a = 0$, hence $b = 0$. See [[Thm - Eigenvectors with Distinct Eigenvalues are Linearly Independent]].

**Bound: at most $\dim V$ distinct eigenvalues.** The previous fact, combined with the dimension count, gives: $T \in \mathcal{L}(V)$ has at most $\dim V$ distinct eigenvalues in $F$. So eigenvalues form a finite list; over $\mathbb{C}$, this list is non-empty when $V \neq 0$.

**Calibration check.** If you have absorbed the definition: (a) you can verify quickly that $E(\lambda, T) = \ker(T - \lambda I)$ is a subspace for any $\lambda$, not just for the actual eigenvalues, but is non-trivial exactly when $\lambda$ is an eigenvalue; (b) you can see why $Tv = \lambda v$ and $v \neq 0$ together imply $T$ acts as $\lambda I$ on the line $\operatorname{span}(v)$; (c) you can interpret the eigenvalue equation for the differentiation operator on the finite-dimensional space $\mathcal{P}_n(\mathbb{R})$ (polynomials of degree at most $n$) and see that there is still only the eigenvalue $0$ — eigenvalues do not multiply by restricting to a finite-dimensional invariant subspace.

---

# Unlocked by This

> [!tip] Diagonalizable Operator *(from Linear Algebra V, §5D)*
> An operator is [[Def - Diagonalizable Operator|diagonalizable]] if $V$ has a basis of eigenvectors of $T$ — equivalently, $V = \bigoplus_k E(\lambda_k, T)$ for the distinct eigenvalues. This is the cleanest possible structure for an operator and is the prototype of the spectral theorem.

> [!tip] Generalized Eigenspace *(from Linear Algebra VIII)*
> Over $\mathbb{C}$, even non-diagonalizable operators admit a direct-sum decomposition by **generalized eigenspaces** $G(\lambda, T) = \ker(T - \lambda I)^{\dim V}$. These contain the ordinary eigenspaces and capture the "Jordan structure" missed by the eigenspaces alone. See [[Thm - Generalized Eigenspace Decomposition]].

> [!tip] The Spectrum of a Bounded Operator *(from Functional Analysis)*
> The right generalisation of "set of eigenvalues" to infinite-dimensional Banach or Hilbert spaces is the **spectrum** $\sigma(T) = \{\lambda \in \mathbb{C} : T - \lambda I \text{ is not invertible}\}$. In finite dimensions the spectrum equals the set of eigenvalues. In infinite dimensions, the equivalences (a)–(e) above break down: an operator can fail to be invertible without having an eigenvector at all, splitting the spectrum into point spectrum (eigenvalues), continuous spectrum, and residual spectrum. The right-shift on $\ell^2$ is the standard example of an operator with empty point spectrum but unit-disk spectrum.

> [!tip] Stability of Equilibria in Dynamical Systems *(from Dynamical Systems)*
> Near a fixed point $x_*$ of a smooth dynamical system $\dot x = f(x)$, the linearisation $Df_{x_*}$ — see [[Def - The Total Derivative and Differentiability|the total derivative]] — has eigenvalues that determine local stability: eigenvalues with negative real part contribute decaying modes, those with positive real part contribute growing modes, those on the imaginary axis are marginal. The **Hartman-Grobman theorem** says that at a hyperbolic fixed point (no imaginary eigenvalues), the nonlinear dynamics is topologically conjugate to the linearisation, so the eigenvalues capture the *qualitative* local behaviour completely. The whole subject of bifurcation theory is the study of what happens when eigenvalues cross the imaginary axis as a parameter is varied.

> [!tip] Principal Component Analysis *(from Statistics, Machine Learning)*
> Eigenvalues of a covariance matrix in statistics measure the variance along their eigenvectors. **PCA** diagonalises the covariance matrix; the largest eigenvalues correspond to directions of maximum variance, and projecting data onto the top $k$ eigenvectors gives the optimal rank-$k$ approximation in the least-squares sense. The whole subject of high-dimensional data analysis takes eigenvalue decompositions of natural matrices as central invariants.
