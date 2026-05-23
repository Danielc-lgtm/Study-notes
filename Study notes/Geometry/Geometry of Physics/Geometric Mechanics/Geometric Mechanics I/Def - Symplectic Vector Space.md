---
type: definition
subject: geometric-mechanics
prereqs:
  - "Def - Vector Space"
  - "Def - Bilinear Form"
  - "Def - Symmetric and Alternating Bilinear Form"
tags: [physics, geometric-mechanics, symplectic-geometry, linear-algebra]
---

# Notation

$V$ is a finite-dimensional real vector space, $V^*$ its dual. A **bilinear form** $\omega : V \times V \to \mathbb{R}$ is **antisymmetric** if $\omega(v, w) = -\omega(w, v)$ for all $v, w$; it is **nondegenerate** if $\omega(v, \cdot) = 0 \in V^*$ implies $v = 0$, equivalently the induced map $\omega^\flat : V \to V^*$, $v \mapsto \omega(v, \cdot)$ is an isomorphism. The standard model is $\mathbb{R}^{2n}$ with coordinates labelled $(q^1, \dots, q^n, p_1, \dots, p_n)$. The matrix of the standard antisymmetric form in this basis is $J = \begin{pmatrix} 0 & I_n \\ -I_n & 0\end{pmatrix}$, and the standard form is $\omega_0((q,p), (q',p')) = \sum_i(p_i q'^i - p'_i q^i) = (q,p)^T J (q',p')$.

---

# Axiom Motivation

The thing we are trying to axiomatize is **the algebraic structure on phase space that produces dynamics from energy**. Look at the elementary situation: a single degree of freedom, coordinates $(q, p)$ for position and momentum, Hamiltonian $H(q, p)$, and Hamilton's equations $\dot q = \partial H/\partial p$, $\dot p = -\partial H/\partial q$. The map from the function $H$ to the vector field $(\partial H/\partial p)\partial_q - (\partial H/\partial q)\partial_p$ can be written as $X_H = J^{-1}\nabla H$ where $J = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$ is the standard symplectic matrix. The asymmetric "minus sign" between $q$ and $p$ is the whole content of Hamilton's equations, and it is exactly the **antisymmetry** of $J$. We are looking for the right axiomatic abstraction of $J$.

Start with the form. We want a pairing $\omega : V \times V \to \mathbb{R}$ that takes two phase-space directions and returns a number — geometrically, the **oriented area** of the parallelogram they span in some $(q, p)$ direction. **Bilinearity** is automatic: areas scale linearly in each side. So we need a bilinear form. What about its symmetry type?

Suppose first we tried a *symmetric* form $\omega(v, w) = \omega(w, v)$. Such a form is an inner product (when also positive-definite) and gives rise to a metric structure: lengths, angles, orthogonality. The map $X \mapsto \omega(X, \cdot)$ is then the musical isomorphism of [[Def - Riemannian Metric|Riemannian geometry]]. But the dynamics produced by $X_H = \omega^{-1}(dH, \cdot)$ would be **gradient flow** $\dot x = \nabla H$, not Hamiltonian flow — and gradient flow famously *decreases* $H$ (it descends the energy landscape), violating energy conservation. The wrong sign structure gives the wrong physics. Energy is *conserved* along Hamiltonian flow, not minimized; the conservation is $X_H(H) = \omega(X_H, X_H)$ which must vanish for energy conservation. A symmetric form has $\omega(X_H, X_H) \geq 0$ generically (positive-definite case) and *cannot* vanish unless $X_H = 0$. So we cannot use a symmetric form.

Suppose instead we try an *antisymmetric* form: $\omega(v, w) = -\omega(w, v)$. Now $\omega(X, X) = 0$ for every $X$, automatically. So $X_H(H) = \omega(X_H, X_H) = 0$ — energy is automatically conserved along its own Hamiltonian flow, no extra condition needed. **Antisymmetry is the algebraic encoding of energy conservation.** This is the first axiom forced by physics.

Why **nondegeneracy**? We need the assignment $H \mapsto X_H$ to be well-defined: given any energy function $H$ (or equivalently any covector $dH$), we want a *unique* vector field whose Hamiltonian-equation relation $\iota_{X_H}\omega = dH$ singles it out. The map $X \mapsto \iota_X\omega = \omega(X, \cdot)$ goes from $V$ to $V^*$, both $n$-dimensional, so it is an isomorphism if and only if it has trivial kernel — which is exactly the **nondegeneracy** condition. Without nondegeneracy, some energy functions would have no Hamiltonian vector field at all (when $dH$ lies outside the image of $X \mapsto \iota_X\omega$), and other vector fields would be Hamiltonian for many different $H$'s (the kernel of the map gives an ambiguity). The dynamics would not be well-defined. **Nondegeneracy is what makes "$H$ generates the dynamics $X_H$" a sensible statement.**

What if we drop nondegeneracy? Then we have an antisymmetric bilinear form that may have a nontrivial radical $\text{rad}(\omega) = \{v : \omega(v, \cdot) = 0\}$. The quotient $V/\text{rad}(\omega)$ is symplectic — so degenerate antisymmetric forms reduce to symplectic forms on smaller spaces. This is the algebraic content of **symplectic reduction**: the radical is "spurious dimensions" that play no role in the dynamics, and quotienting by them gives the genuine phase space. The classification result is: every antisymmetric bilinear form on $V$ has even rank $2n$, and on the quotient by its radical it has the standard symplectic form.

One could ask whether to *strengthen* the axioms — for instance, by demanding $\omega$ be positive-definite (i.e., $\omega(v, v) > 0$ for $v \neq 0$). But for an antisymmetric form, $\omega(v, v) = 0$ identically, so positive-definiteness would force $V = 0$. There is nothing to strengthen.

In summary, the two demands — antisymmetry and nondegeneracy — are each forced by one feature of the dynamics-from-energy structure. Antisymmetry is the algebraic shadow of energy conservation. Nondegeneracy makes the energy-to-flow assignment well-defined. The crucial consequence is that the dimension is forced to be even: $\det(\omega^T) = (-1)^{\dim V}\det(\omega)$, so if $\dim V$ is odd then $\det\omega = -\det\omega = 0$, contradicting nondegeneracy. Drop either axiom, and you either lose energy conservation (drop antisymmetry) or lose the energy-to-flow bijection (drop nondegeneracy).

---

# The Definition

A **symplectic vector space** is a pair $(V, \omega)$ where $V$ is a finite-dimensional real vector space and $\omega : V \times V \to \mathbb{R}$ is a bilinear form satisfying:

1. **Antisymmetry.** $\omega(v, w) = -\omega(w, v)$ for all $v, w \in V$.
2. **Nondegeneracy.** The map $\omega^\flat : V \to V^*$, $v \mapsto \omega(v, \cdot)$ is a linear isomorphism, equivalently $\omega(v, w) = 0$ for all $w \in V$ implies $v = 0$.

A direct consequence is that $\dim V$ must be even, $\dim V = 2n$ for some $n \geq 0$.

The **standard symplectic vector space** of dimension $2n$ is $(\mathbb{R}^{2n}, \omega_0)$ with coordinates $(q^1, \dots, q^n, p_1, \dots, p_n)$ and

$$\omega_0((q, p), (q', p')) = \sum_{i=1}^n (p_i q'^i - p'_i q^i),$$

equivalently $\omega_0 = \sum_i dp_i \wedge dq^i$ as a $2$-form on $\mathbb{R}^{2n}$. By the **linear Darboux theorem** (see Examples below), every symplectic vector space is isomorphic to the standard one of the same dimension.

---

# Categorical / Structural Definition

A symplectic vector space is the **antisymmetric counterpart of an inner product space**. An inner product space is a finite-dimensional real vector space equipped with a *symmetric*, nondegenerate (and usually positive-definite) bilinear form; a symplectic vector space replaces "symmetric" with "antisymmetric". In the language of bilinear forms on $V$, the classifying object is $\mathrm{Sym}^2 V^* \oplus \Lambda^2 V^*$ — symmetric plus antisymmetric. An inner product is a positive-definite element of the first summand; a symplectic form is a nondegenerate element of the second.

In categorical language, both arise from a **nondegenerate pairing** $V \otimes V \to \mathbb{R}$, with the symmetry encoded by the action of $S_2$ on the tensor square. Symmetric forms are $S_2$-invariants (the $+1$-eigenspace); antisymmetric forms are $S_2$-anti-invariants (the $-1$-eigenspace). The categories of symmetric and symplectic vector spaces are formally dual in this $\mathbb{Z}/2$-grading.

The natural morphisms in the category of symplectic vector spaces are **symplectic linear maps**: linear maps $T : (V, \omega_V) \to (W, \omega_W)$ with $\omega_W(Tv, Tv') = \omega_V(v, v')$. The invertible symplectic linear maps from $(V, \omega)$ to itself form a Lie group, the **symplectic group** $\mathrm{Sp}(V, \omega)$, of dimension $n(2n+1)$ where $\dim V = 2n$. This is one of the four classical Lie groups (alongside $\mathrm{SO}(n)$, $\mathrm{SU}(n)$, $\mathrm{GL}(n)$) and is the linear automorphism group of the symplectic structure.

---

# Relate to Other Fields / Compression

A symplectic vector space is the **antisymmetric, real, nondegenerate version of a Hermitian inner product space**, with the imaginary part of the Hermitian form playing the role of $\omega$ and the real part producing a compatible inner product. Specifically, $(\mathbb{C}^n, h)$ with $h(z, w) = \sum_i \bar z_i w_i$ has $\mathrm{Re}(h)$ symmetric (the standard inner product on $\mathbb{R}^{2n} \cong \mathbb{C}^n$) and $\mathrm{Im}(h)$ antisymmetric (the standard symplectic form $\omega_0$). The choice of a *compatible* complex structure on $(V, \omega)$ — a linear map $J : V \to V$ with $J^2 = -I$ and $\omega(Jv, Jw) = \omega(v, w)$ and $\omega(v, Jv) > 0$ for $v \neq 0$ — recovers exactly this Hermitian structure: $g(v, w) := \omega(v, Jw)$ is an inner product, and $h := g + i\omega$ is Hermitian.

From the dynamics side, a symplectic vector space is the **infinitesimal model of phase space at a point**: at any point $p$ of a symplectic manifold $(M, \omega)$, the tangent space $(T_pM, \omega_p)$ is a symplectic vector space, and all local computations reduce to linear-algebraic questions about this tangent space.

**True name:** the true name of a symplectic vector space is **"a vector space carrying the algebraic structure that produces Hamilton's equations"** — explicitly, a vector space such that the assignment from linear functions $H : V \to \mathbb{R}$ to vector fields $X_H$ defined by $\omega(X_H, \cdot) = dH$ is a well-defined linear isomorphism $V^* \to V$. The official definition (antisymmetric + nondegenerate) is the minimal algebraic abstraction of this dynamical content.

---

# Examples / Corollaries

**Is an instance: $(\mathbb{R}^2, dp \wedge dq)$.** The simplest non-trivial case. Coordinates $(q, p)$, form $\omega_0 = dp \wedge dq$, so $\omega_0((1, 0), (0, 1)) = (dp \wedge dq)(\partial_q, \partial_p) = 1$. Geometrically $\omega_0$ measures the oriented area of parallelograms in the $(q, p)$-plane. Every Hamiltonian system with one degree of freedom lives here.

**Is an instance: $(\mathbb{R}^{2n}, \omega_0 = \sum_i dp_i \wedge dq^i)$.** The standard symplectic space of dimension $2n$. Every symplectic vector space of dimension $2n$ is isomorphic to this one — this is the **linear Darboux theorem**, proved by an inductive Gram–Schmidt-like procedure: pick a nonzero $v_1$, find $u_1$ with $\omega(v_1, u_1) = 1$ (which exists by nondegeneracy), restrict to the orthogonal complement $\{x : \omega(v_1, x) = \omega(u_1, x) = 0\}$ (which is $(2n-2)$-dimensional and still symplectic), and iterate. The resulting basis $(v_1, \dots, v_n, u_1, \dots, u_n)$ is a **symplectic basis**.

**Is an instance: $(V \oplus V^*, \omega_V)$ for any finite-dimensional $V$.** With $\omega_V((v, \alpha), (v', \alpha')) = \alpha(v') - \alpha'(v)$. This is the tangent-cotangent symplectic structure at a point and is the linearization of the canonical symplectic form on a cotangent bundle.

**Is an instance: $(\mathbb{C}^n, \mathrm{Im}(h))$.** Take $\mathbb{C}^n$ as a real vector space ($\dim_\mathbb{R} = 2n$) with the standard Hermitian form $h(z, w) = \sum_i \bar z_i w_i$. The imaginary part $\omega(z, w) = \mathrm{Im}(h(z, w)) = \sum_i(\mathrm{Re}\,\bar z_i\, \mathrm{Im}\,w_i - \mathrm{Im}\,\bar z_i\,\mathrm{Re}\,w_i)$ is a symplectic form on $\mathbb{R}^{2n} \cong \mathbb{C}^n$. Writing $z_i = q^i + ip_i$ recovers the standard form $\omega_0 = \sum dp_i \wedge dq^i$.

**Is NOT an instance: $(\mathbb{R}^3, \omega)$ for any antisymmetric $\omega$.** No nondegenerate antisymmetric form exists on an odd-dimensional vector space: the matrix $A$ of an antisymmetric form satisfies $A^T = -A$, so $\det A = \det A^T = \det(-A) = (-1)^{2n+1}\det A = -\det A$, forcing $\det A = 0$. So $\omega$ is *always* degenerate on odd-dimensional spaces, with at least a $1$-dimensional radical. The odd-dimensional analogue is the **contact structure**, which is different geometric machinery.

**Is NOT an instance: $(\mathbb{R}^4, dx^1 \wedge dx^2)$.** The form $\omega = dx^1 \wedge dx^2$ on $\mathbb{R}^4$ with coordinates $(x^1, x^2, x^3, x^4)$ is antisymmetric and a genuine $2$-form, but it is **degenerate**: $\omega(\partial_{x^3}, \cdot) = 0$ identically. The radical is $\mathrm{span}(\partial_{x^3}, \partial_{x^4})$, and the quotient is the symplectic $(\mathbb{R}^2, dx^1 \wedge dx^2)$. So even-dimensional does not suffice for symplecticness — nondegeneracy is an independent demand.

**Is NOT an instance: $(\mathbb{R}^2, dq \otimes dq)$.** A symmetric, nondegenerate bilinear form is an inner product, not a symplectic form. Antisymmetry must fail in the wrong direction for the structure to be symplectic.

**Corollary (existence of a symplectic basis).** Every symplectic vector space $(V, \omega)$ of dimension $2n$ admits a basis $(e_1, \dots, e_n, f_1, \dots, f_n)$ in which $\omega(e_i, e_j) = \omega(f_i, f_j) = 0$ and $\omega(e_i, f_j) = \delta_{ij}$ — the **standard form** of the symplectic basis. This is the linear Darboux theorem.

**Corollary (the symplectic isomorphism).** The map $\omega^\flat : V \to V^*$, $v \mapsto \omega(v, \cdot)$ is a linear isomorphism. So for any covector $\alpha \in V^*$ there is a unique vector $X_\alpha$ with $\iota_{X_\alpha}\omega = \alpha$. This is the algebraic underpinning of "$H \mapsto X_H$" on a symplectic manifold.

**Corollary (the symplectic complement and isotropic subspaces).** For any subspace $W \leq V$, the **symplectic complement** is $W^\omega = \{v \in V : \omega(v, w) = 0 \text{ for all } w \in W\}$, of dimension $2n - \dim W$. $W$ is **isotropic** if $W \leq W^\omega$ (equivalently $\omega|_{W \times W} = 0$); **coisotropic** if $W \geq W^\omega$; **Lagrangian** if $W = W^\omega$, equivalently $W$ is isotropic with $\dim W = n$. Lagrangian subspaces are the maximal isotropic subspaces.

**Calibration check.** If you can do these three things, you have understood the definition. First, verify that the form $\omega_0 = dp \wedge dq$ on $\mathbb{R}^2$ satisfies $\omega_0(\partial_q, \partial_p) = 1$ and $\omega_0(\partial_q, \partial_q) = \omega_0(\partial_p, \partial_p) = 0$. Second, prove that on a $2n$-dimensional symplectic vector space, the top wedge power $\omega^n$ is a nonzero element of $\Lambda^{2n}V^* \cong \mathbb{R}$ (a "volume" element). Third, give an example of an isotropic subspace, a coisotropic subspace, and a Lagrangian subspace of $(\mathbb{R}^4, \omega_0)$.

---

# Unlocked by This

> [!tip] Symplectic Group $\mathrm{Sp}(V, \omega)$ *(from Lie Theory)*
> The set of linear automorphisms of $(V, \omega)$ — invertible linear maps $T : V \to V$ with $T^*\omega = \omega$ — forms a Lie group $\mathrm{Sp}(V, \omega) \cong \mathrm{Sp}(2n, \mathbb{R})$, one of the four classical infinite families of simple Lie groups. Its Lie algebra $\mathfrak{sp}(2n, \mathbb{R})$ consists of linear maps $A$ with $A^TJ + JA = 0$, equivalently $JA$ symmetric. The dimension is $n(2n+1)$. The symplectic group plays the same role for symplectic geometry that the orthogonal group plays for Riemannian geometry: it is the linear isometry group of the structure.

> [!tip] Lagrangian Grassmannian and the Maslov Class *(from Symplectic Topology)*
> The set of all Lagrangian subspaces of $(\mathbb{R}^{2n}, \omega_0)$ forms a smooth manifold, the **Lagrangian Grassmannian** $\Lambda(n)$, of dimension $n(n+1)/2$. Its fundamental group is $\pi_1(\Lambda(n)) = \mathbb{Z}$ (for $n \geq 1$), and the generator of $H^1(\Lambda(n); \mathbb{Z}) = \mathbb{Z}$ is the **Maslov class** — a fundamental topological invariant of loops of Lagrangian subspaces. The Maslov class appears in the **WKB approximation** in quantum mechanics (as the phase shift through a caustic), in the **Atiyah–Patodi–Singer eta-invariant**, and in **Floer homology** as a grading on the chain complex.

> [!tip] Compatible Triples and Kähler Geometry *(from Complex Differential Geometry)*
> A symplectic vector space $(V, \omega)$ together with a compatible **complex structure** $J : V \to V$ (with $J^2 = -I$ and $\omega(J\cdot, J\cdot) = \omega(\cdot, \cdot)$ and $\omega(\cdot, J\cdot)$ positive-definite) and the resulting inner product $g(\cdot, \cdot) = \omega(\cdot, J\cdot)$ form a **compatible triple** $(\omega, J, g)$. On a manifold, the global existence of such a triple is the definition of a **Kähler manifold** — a symplectic manifold with a compatible integrable complex structure. Kähler manifolds are simultaneously symplectic, complex, and Riemannian, and they support the deepest theorems of complex algebraic geometry (Hodge theory, Calabi–Yau theorems, mirror symmetry). The standard symplectic space $(\mathbb{R}^{2n}, \omega_0)$ is just the linear model of Kähler space: complex coordinates $z_j = q^j + ip_j$, Hermitian form $h = \sum d\bar z_j \otimes dz_j$, with real part the standard inner product and imaginary part the standard symplectic form.
