---
type: exercise
subject: hodge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Harmonic Form"
  - "Def - Hodge Laplacian"
  - "Thm - Harmonic Forms Represent de Rham Cohomology"
  - "Thm - Hodge Decomposition Theorem"
tags: [geometry, hodge-theory, torus, cohomology]
---

# Problem Statement

Let $T^n = \mathbb{R}^n/\mathbb{Z}^n$ be the flat $n$-torus, with the flat Euclidean metric inherited from $\mathbb{R}^n$ and coordinates $(x^1, \dots, x^n)$ (well-defined modulo $1$).

(a) Show that every constant-coefficient $k$-form $\omega = \sum'_I c_I\,dx^I$ (with $c_I \in \mathbb{R}$ constants, $I$ ranging over increasing multi-indices of length $k$) is harmonic, i.e., $\Delta\omega = 0$.

(b) Show, conversely, that every harmonic $k$-form on $T^n$ is a constant-coefficient $k$-form. (Hint: expand in Fourier series; non-constant Fourier modes have positive Laplacian eigenvalue.)

(c) Conclude that $\dim\mathcal{H}^k(T^n) = \binom{n}{k}$, and by the Hodge isomorphism, $b_k(T^n) = \binom{n}{k}$.

(d) Verify Poincaré duality: $b_k(T^n) = b_{n-k}(T^n) = \binom{n}{k} = \binom{n}{n-k}$, consistent with the symmetric Hodge diamond.

**Recall:**

The flat $n$-torus is the quotient $T^n = \mathbb{R}^n/\mathbb{Z}^n$. Smooth functions on $T^n$ are smooth $\mathbb{Z}^n$-periodic functions on $\mathbb{R}^n$. Smooth differential forms on $T^n$ are smooth $\mathbb{Z}^n$-periodic differential forms on $\mathbb{R}^n$.

A **harmonic $k$-form** on a closed Riemannian manifold is a $k$-form $\omega$ satisfying $\Delta\omega = 0$, where $\Delta = d\delta + \delta d$ is the [[Def - Hodge Laplacian|Hodge Laplacian]].

![[Def - Harmonic Form#The Definition]]

By the [[Thm - Harmonic Forms Represent de Rham Cohomology|Hodge isomorphism]], every de Rham cohomology class has a unique harmonic representative, and $\dim\mathcal{H}^k(M) = b_k(M)$. Topologically, $b_k(T^n) = \binom{n}{k}$ (Künneth formula applied to $T^n = (S^1)^n$, or singular-homology computation).

On the flat torus with coordinates $(x^1, \dots, x^n)$, the constant-coefficient $k$-forms $\sum_I c_I\,dx^I$ (with $c_I \in \mathbb{R}$, $I$ increasing multi-indices) form a $\binom{n}{k}$-dimensional space.

---

# Convergent Strategy

**Problem class:** Computing the space of harmonic forms on a specific compact Riemannian manifold (the flat torus). The chapter's problem-solving strategy for "compute $\mathcal{H}^k(M)$ via symmetry averaging" applies, but here we use the direct Fourier-analysis approach since the flat torus is the prototype manifold where Fourier methods work cleanly.

**Assumption pattern:** Flat metric on $T^n$, with coordinates $(x^i)$. The metric is $g = \sum_i dx^i\otimes dx^i$, with $g_{ij} = \delta_{ij}$ and Christoffel symbols vanishing (flat connection). The volume form is $\operatorname{vol}_{T^n} = dx^1\wedge\cdots\wedge dx^n$ (constant coefficient $1$).

**Theorem routing:** Direct computation of $\Delta$ on constant-coefficient forms gives $0$ trivially (no derivatives = no Laplacian). For the converse, expand $\omega = \sum_I\omega_I(x)\,dx^I$ in Fourier series: $\omega_I(x) = \sum_k \hat\omega_{I,k}e^{2\pi i k\cdot x}$. The Hodge Laplacian on this is $\Delta\omega = \sum_k(2\pi)^2|k|^2\hat\omega_{I,k}e^{2\pi i k\cdot x}\,dx^I$ (componentwise, since the metric is flat). Setting $\Delta\omega = 0$ forces $\hat\omega_{I,k} = 0$ for $k \neq 0$, leaving only the constant ($k = 0$) part.

**Key decision point:** The flat metric is what makes the computation purely Fourier-theoretic — the Hodge Laplacian on a flat manifold acts componentwise on forms (no Christoffel correction). On a curved torus this would not be true; the flat metric is essential. The harmonic forms then correspond exactly to the "constant" Fourier modes.

---

# Legal Operations Used

1. **Compute $\Delta$ on constant-coefficient forms** (direct application of $\Delta = d\delta + \delta d$). With constant coefficients, $d\omega = 0$ (no derivatives to take) and $\delta\omega = 0$ (similar). So $\Delta\omega = 0$.

2. **Fourier expansion of smooth forms on $T^n$** (operation: use Fourier decomposition to convert a PDE problem on $T^n$ into an algebraic condition on Fourier coefficients). Smooth functions on $T^n$ are dense in $L^2$ Fourier modes, and the Laplacian acts diagonally on these modes.

3. **Eigenvalue analysis on Fourier modes** (operation: $\Delta(e^{2\pi i k\cdot x}) = (2\pi)^2|k|^2 e^{2\pi i k\cdot x}$ on functions, extending componentwise to forms). The kernel of $\Delta$ on Fourier modes is exactly the $k = 0$ mode (the constants).

4. **Apply the Hodge isomorphism** $\dim\mathcal{H}^k = b_k$ to convert the analytic computation into a topological result.

---

# Hints

> [!note]- Hint 1
> For part (a), check: if $\omega = c\,dx^I$ with $c$ constant, what is $d\omega$? What is $\delta\omega$? Both should be zero.

> [!note]- Hint 2
> For part (b), expand $\omega = \sum_I\omega_I(x)dx^I$ where each $\omega_I$ is a smooth periodic function. The Hodge Laplacian acts on the flat torus as $\Delta\omega = \sum_I(-\nabla^2\omega_I)dx^I$ (componentwise, since the metric is flat and Christoffel symbols vanish). So $\Delta\omega = 0 \iff \nabla^2\omega_I = 0$ for each $I$. By Fourier analysis, the only periodic harmonic functions on $T^n$ are constants.

> [!note]- Hint 3
> For part (c), the constant-coefficient $k$-forms span a $\binom{n}{k}$-dimensional vector space (one independent constant for each increasing multi-index of length $k$). Parts (a) and (b) show this is exactly the space of harmonic $k$-forms. By the Hodge isomorphism, this equals the Betti number.

---

# Solution

The proof has three parts. Part (a) shows constant-coefficient forms are harmonic by direct computation. Part (b) shows the converse via Fourier analysis: non-constant Fourier modes have positive Laplacian eigenvalue, so the kernel is just the constant part. Part (c) combines parts (a) and (b) to compute the dimension. Part (d) verifies Poincaré duality.

**Step 1: Constant-coefficient forms are harmonic (part (a)).**

> [!note]- Derivation
> Let $\omega = \sum'_I c_I\,dx^I$ with $c_I \in \mathbb{R}$ constants. Compute $d\omega$:
> $$d\omega = \sum'_I c_I\,d(dx^I) = \sum'_I c_I\cdot 0 = 0$$
> (since $d(dx^{i_1}\wedge\cdots\wedge dx^{i_k}) = 0$ by $d^2 = 0$ applied to each $dx^i$). So $\omega$ is closed.
>
> Compute $\delta\omega$:
> $$\delta\omega = (-1)^{n(k+1)+1}\star d\star\omega.$$
> $\star\omega = \sum'_I c_I\star(dx^I)$. On the flat torus with the orthonormal coframe $(dx^1, \dots, dx^n)$ (which is orthonormal since $g = \delta$), $\star(dx^I) = \pm dx^{I^c}$ — a constant-coefficient $(n-k)$-form. So $\star\omega$ is a constant-coefficient form. Then $d\star\omega = 0$ (no derivatives), so $\star d\star\omega = 0$, hence $\delta\omega = 0$.
>
> Combining: $\Delta\omega = d\delta\omega + \delta d\omega = d\cdot 0 + \delta\cdot 0 = 0$. ✓

**Step 2: Converse via Fourier analysis (part (b)).**

> [!note]- Derivation
> Let $\omega \in \Omega^k(T^n)$ be a smooth $k$-form, written in the coordinate basis as $\omega = \sum'_I\omega_I(x)\,dx^I$ with smooth periodic coefficient functions $\omega_I : T^n \to \mathbb{R}$.
>
> On the flat torus, the Hodge Laplacian acts componentwise: $\Delta\omega = \sum'_I(\Delta\omega_I)\,dx^I$, where $\Delta\omega_I = -\nabla^2\omega_I$ is the Hodge Laplacian on functions (a single component). (Verification: $d\omega = \sum'_I\sum_j\partial_j\omega_I\,dx^j\wedge dx^I$; $\delta\omega$ involves divergences of $\omega_I$; combining $\Delta = d\delta + \delta d$ and using the flat metric, one verifies that the Christoffel corrections vanish, and the result is componentwise.)
>
> So $\Delta\omega = 0 \iff \nabla^2\omega_I = 0$ for each $I$.
>
> Now expand each $\omega_I$ in Fourier series: $\omega_I(x) = \sum_{k \in \mathbb{Z}^n}\hat\omega_{I,k}\,e^{2\pi i k\cdot x}$.
>
> Apply $\nabla^2$: $\nabla^2(e^{2\pi i k\cdot x}) = -(2\pi)^2|k|^2 e^{2\pi i k\cdot x}$.
>
> So $\nabla^2\omega_I = -(2\pi)^2\sum_{k}|k|^2\hat\omega_{I,k}e^{2\pi i k\cdot x}$.
>
> For this to be zero, the Fourier coefficient $|k|^2\hat\omega_{I,k} = 0$ for every $k$. For $k \neq 0$, $|k|^2 > 0$, forcing $\hat\omega_{I,k} = 0$. So only the $k = 0$ mode survives: $\omega_I(x) = \hat\omega_{I,0}$, a constant.
>
> Hence $\omega = \sum'_I\hat\omega_{I,0}\,dx^I$ is a constant-coefficient form. ✓

**Step 3: [[Def - Dimension|Dimension]] of $\mathcal{H}^k(T^n)$ (part (c)).**

> [!note]- Derivation
> By Steps 1 and 2, $\mathcal{H}^k(T^n) = \{$ constant-coefficient $k$-forms on $T^n\} = \{\sum'_I c_I dx^I : c_I \in \mathbb{R}\}$.
>
> The vector space of constant-coefficient $k$-forms has one independent constant $c_I$ for each increasing multi-index $I$ of length $k$ in $\{1, \dots, n\}$. The number of such multi-indices is $\binom{n}{k}$.
>
> So $\dim\mathcal{H}^k(T^n) = \binom{n}{k}$.
>
> By the [[Thm - Harmonic Forms Represent de Rham Cohomology|Hodge isomorphism]], $b_k(T^n) = \dim H^k_{dR}(T^n) = \dim\mathcal{H}^k(T^n) = \binom{n}{k}$. ✓

**Step 4: Poincaré duality verification (part (d)).**

> [!note]- Derivation
> By the symmetry of binomial coefficients, $\binom{n}{k} = \binom{n}{n-k}$. So $b_k(T^n) = b_{n-k}(T^n)$, as predicted by [[Thm - Poincare Duality via Hodge Star]].
>
> The Hodge star realizes the duality explicitly: $\star : \mathcal{H}^k(T^n) \to \mathcal{H}^{n-k}(T^n)$ sends the constant-coefficient form $\sum_I c_I dx^I$ to the constant-coefficient form $\sum_I c_I\star(dx^I)$, where $\star(dx^I) = \pm dx^{I^c}$ on the orthonormal coframe of $T^n$. The map is a bijection on the bases of the two spaces: each multi-index $I$ of length $k$ corresponds to the complementary multi-index $I^c$ of length $n - k$ (with sign).
>
> Total Betti number: $\sum_{k=0}^n b_k(T^n) = \sum_k\binom{n}{k} = 2^n$.
> Euler characteristic: $\chi(T^n) = \sum_k(-1)^k\binom{n}{k} = (1 - 1)^n = 0$ (consistent with the fact that the torus admits a free $S^1$-action, and a manifold with such an action has $\chi = 0$).

> [!note]- Complete formal solution
> **Part (a):** A constant-coefficient $k$-form $\omega = \sum'_I c_I\,dx^I$ on $T^n$ satisfies $d\omega = 0$ (no coefficients to differentiate) and $\delta\omega = 0$ (similar). Hence $\Delta\omega = d\delta\omega + \delta d\omega = 0$.
>
> **Part (b):** Let $\omega \in \mathcal{H}^k(T^n)$, written as $\omega = \sum'_I\omega_I(x)\,dx^I$ with smooth periodic coefficient functions. On the flat torus, $\Delta\omega = \sum'_I(-\nabla^2\omega_I)\,dx^I$ (componentwise, since the metric is flat). So $\Delta\omega = 0 \iff \nabla^2\omega_I = 0$ for each $I$.
>
> Fourier expansion: $\omega_I(x) = \sum_{k\in\mathbb{Z}^n}\hat\omega_{I,k}e^{2\pi i k\cdot x}$. Applying $\nabla^2$: $\nabla^2\omega_I = -(2\pi)^2\sum_k|k|^2\hat\omega_{I,k}e^{2\pi i k\cdot x}$. Setting this to zero forces $|k|^2\hat\omega_{I,k} = 0$ for all $k$. For $k \neq 0$, $|k|^2 > 0$, so $\hat\omega_{I,k} = 0$. Only the $k = 0$ Fourier mode survives, so $\omega_I$ is constant.
>
> Hence $\omega = \sum'_I\hat\omega_{I,0}\,dx^I$, a constant-coefficient form.
>
> **Part (c):** Combining (a) and (b), $\mathcal{H}^k(T^n) = \{$ constant-coefficient $k$-forms $\}$, which has dimension $\binom{n}{k}$. By the Hodge isomorphism, $b_k(T^n) = \binom{n}{k}$.
>
> **Part (d):** Poincaré duality: $b_k(T^n) = \binom{n}{k} = \binom{n}{n-k} = b_{n-k}(T^n)$ by the symmetry of binomial coefficients. Hodge-star realization: $\star : \mathcal{H}^k(T^n)\to\mathcal{H}^{n-k}(T^n)$ is the obvious bijection between the bases (multi-indices and their complements). $\qquad\blacksquare$

---

# Key Takeaways

**Constant-coefficient forms on a flat compact manifold are harmonic.** The most reusable insight is that on any flat compact Riemannian manifold (torus, Klein bottle, etc.), constant-coefficient forms are automatically harmonic — they trivially satisfy both $d\omega = 0$ and $\delta\omega = 0$. The converse — that *all* harmonic forms are constant-coefficient — uses Fourier analysis and the absence of Christoffel correction in the flat metric. The trigger pattern: see "flat compact Riemannian manifold" + "compute harmonic forms" → "look at constant-coefficient forms".

**Fourier analysis diagonalizes the Hodge Laplacian on a flat torus.** The Hodge Laplacian acts componentwise on forms in flat coordinates, and on each component (a function), Fourier analysis diagonalizes it: eigenfunctions are $e^{2\pi i k\cdot x}$ with eigenvalues $(2\pi)^2|k|^2$. The kernel is the $k = 0$ [[Def - Subspace|subspace]] (constants). This pattern — Fourier diagonalization of an elliptic operator on a flat compact manifold — is the prototype for **spectral theory on compact manifolds** more generally: the Laplacian has discrete eigenvalues converging to infinity, with the kernel corresponding to topologically meaningful objects (here, cohomology classes).

**On a homogeneous manifold, harmonic forms are invariant forms.** The torus $T^n$ has a transitive $T^n$-action on itself (translation), and harmonic forms are precisely the invariant forms (constant-coefficient). This generalizes: on any homogeneous manifold $G/K$ with an invariant Riemannian metric, the harmonic forms are exactly the $G$-invariant forms, computable from the Lie algebra cohomology $H^*(\mathfrak{g}, \mathfrak{k})$. The trigger pattern: "homogeneous space with invariant metric" + "compute $\mathcal{H}^k$" → "Lie algebra cohomology computation". This is how the cohomology of spheres, projective spaces, and Lie [[Def - Group|groups]] is computed via Hodge theory.

This exercise complements [[Ex - Computing the Hodge Star on S^2]] (Hodge star on a curved $2$-manifold) and [[Ex - First Betti Number Bounds via Bochner's Theorem]] (Bochner's theorem applied to manifolds with positive Ricci). The flat torus is the boundary case of Bochner: $\operatorname{Ric} = 0$ (nonnegative but not strictly positive), and $b_1 = n$ saturates the nonnegative-Ricci bound.
