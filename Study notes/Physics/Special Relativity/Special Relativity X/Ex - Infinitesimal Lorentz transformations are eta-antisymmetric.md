---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Infinitesimal Lorentz Transformations"
  - "Def - The Lorentz Group"
  - "Def - Lie Algebra of the Lorentz Group"
tags: [physics, special-relativity, lie-groups]
---

# Problem Statement

Let $\Lambda = \mathrm{Id} + \varepsilon\,\omega + O(\varepsilon^2)$ be an infinitesimal Lorentz transformation, with $\eta = \mathrm{diag}(1,-1,-1,-1)$ and $\varepsilon$ a small real parameter.

1. By substituting into the defining equation $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ and keeping the first-order term, derive the condition on the generator $\omega$.
2. Show this condition is equivalent to the statement that the index-lowered matrix $\omega_{\mu\nu} := \eta_{\mu\alpha}\omega^\alpha{}_\nu$ is **antisymmetric**, $\omega_{\mu\nu} = -\omega_{\nu\mu}$.
3. Deduce that the boost generators are *symmetric* matrices while the rotation generators are *antisymmetric*, and count the dimension of the space of generators.
4. Verify explicitly that the boost generator $K_1$ (with $1$ in the $(0,1)$ and $(1,0)$ entries) and the rotation generator $J_3$ (rotating the $x$–$y$ block) satisfy the condition.

**Recall:**

![[Def - Infinitesimal Lorentz Transformations#The Definition]]

A [[Def - The Lorentz Group|Lorentz transformation]] is a real $4\times 4$ matrix $\Lambda$ obeying $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$; the index-lowering convention is $\omega_{\mu\nu} = \eta_{\mu\alpha}\omega^\alpha{}_\nu$, which multiplies the rows of $\omega$ by the diagonal entries of $\eta$. A matrix $M$ is symmetric if $M^{\mathsf T} = M$ and antisymmetric if $M^{\mathsf T} = -M$.

---

# Convergent Strategy

**Problem class.** A *compute-the-Lie-algebra* problem: extract the linear constraint defining $\mathfrak{so}(1,3)$ by linearising the group's defining equation. The [[Special Relativity X — The Lorentz Group as a Lie Group#Problem-Solving Strategy|topic strategy]] says the decisive first move for any Lie-algebra question is the generator condition, obtained by expanding $\Lambda = \mathrm{Id} + \varepsilon\,\omega$ to first order.

**Assumption pattern.** The transformation is given *near the identity*, which is the signpost to linearise. The quadratic constraint $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ is the only input; perturbing a quadratic constraint about a solution yields a linear constraint on the perturbation, and that linear constraint is the algebra.

**Theorem routing.** The route is: (1) substitute $\Lambda = \mathrm{Id} + \varepsilon\,\omega$ into $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$; (2) expand, the order-$1$ term is $\eta$ (automatic), the order-$\varepsilon$ term must vanish, giving $\omega^{\mathsf T}\eta + \eta\,\omega = 0$ ([[Def - Infinitesimal Lorentz Transformations]]); (3) rewrite in components by lowering an index to read off antisymmetry of $\omega_{\mu\nu}$; (4) split the antisymmetric $4\times 4$ matrices into the time-space block (boosts) and the space-space block (rotations).

**Key decision point.** The non-obvious move is recognising that the condition is antisymmetry of $\omega_{\mu\nu}$ — the matrix with *both* indices down — not of $\omega^\mu{}_\nu$. Because $\eta$ has a minus sign in the spatial block, lowering an index flips the symmetry type of the time-space entries, so the boost generators (whose nonzero entries straddle the time index) come out *symmetric* as $\omega^\mu{}_\nu$ even though $\omega_{\mu\nu}$ is antisymmetric. Missing this leads to keeping only the rotation generators.

---

# Legal Operations Used

1. **Linearise the defining equation to find generators (operation 1 from the topic page).** Substitute $\Lambda = \mathrm{Id} + \varepsilon\,\omega$ into $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ and collect the order-$\varepsilon$ term. This is the entire content of parts 1–2: the first-order term is $\varepsilon(\omega^{\mathsf T}\eta + \eta\,\omega)$, which must vanish.

2. **Check the generator condition by lowering an index (operation 2 from the topic page).** Used in parts 2 and 4: multiply $\omega$ by $\eta$ and test antisymmetry of the result. For $K_1$ and $J_3$ this is a direct $4\times 4$ multiplication.

---

# Hints

> [!note]- Hint 1
> Write $\Lambda = \mathrm{Id} + \varepsilon\,\omega$ and $\Lambda^{\mathsf T} = \mathrm{Id} + \varepsilon\,\omega^{\mathsf T}$. Compute $\Lambda^{\mathsf T}\eta\,\Lambda$ and discard the $\varepsilon^2$ term. Three terms survive at orders $\varepsilon^0$ and $\varepsilon^1$.

> [!note]- Hint 2
> The order-$\varepsilon^0$ term is $\eta$ (it cancels the $\eta$ on the right). The order-$\varepsilon^1$ term is $\omega^{\mathsf T}\eta + \eta\,\omega$, and for the equation to hold to first order this must be zero.

> [!note]- Hint 3
> To get the component form, note $(\eta\,\omega)_{\mu\nu} = \eta_{\mu\alpha}\omega^\alpha{}_\nu = \omega_{\mu\nu}$ and $(\omega^{\mathsf T}\eta)_{\mu\nu} = \omega^\alpha{}_\mu\eta_{\alpha\nu} = \omega_{\nu\mu}$. So the condition $\omega^{\mathsf T}\eta + \eta\,\omega = 0$ reads $\omega_{\nu\mu} + \omega_{\mu\nu} = 0$.

> [!note]- Hint 4
> For $K_1$: it is symmetric ($K_1^{\mathsf T} = K_1$), and $\eta K_1$ multiplies row $0$ by $+1$ and rows $1,2,3$ by $-1$. The result has $+1$ in the $(0,1)$ slot and $-1$ in the $(1,0)$ slot — antisymmetric. For $J_3$: it is already antisymmetric, and $\eta J_3 = -J_3$ on the spatial block, still antisymmetric.

---

# Solution

The proof is the linearisation of the group equation. Substituting $\Lambda = \mathrm{Id} + \varepsilon\,\omega$ and keeping first order gives $\omega^{\mathsf T}\eta + \eta\,\omega = 0$; lowering an index turns this into antisymmetry of $\omega_{\mu\nu}$; the antisymmetric $4\times 4$ matrices split into three boost (time-space) and three rotation (space-space) generators, totalling six.

**Step 1: Linearise to get $\omega^{\mathsf T}\eta + \eta\,\omega = 0$.**

> [!note]- Derivation
> Write $\Lambda = \mathrm{Id} + \varepsilon\,\omega$, so $\Lambda^{\mathsf T} = \mathrm{Id} + \varepsilon\,\omega^{\mathsf T}$. Then
> $$\Lambda^{\mathsf T}\eta\,\Lambda = (\mathrm{Id} + \varepsilon\,\omega^{\mathsf T})\,\eta\,(\mathrm{Id} + \varepsilon\,\omega) = \eta + \varepsilon\big(\omega^{\mathsf T}\eta + \eta\,\omega\big) + \varepsilon^2\,\omega^{\mathsf T}\eta\,\omega.$$
> The defining equation $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ requires the right-hand side to equal $\eta$. The order-$\varepsilon^0$ term already matches. Dropping the order-$\varepsilon^2$ term (we work to first order), the order-$\varepsilon^1$ term must vanish:
> $$\boxed{\;\omega^{\mathsf T}\eta + \eta\,\omega = 0\;.}$$
> This is the condition that $\omega$ be a [[Def - Lie Algebra of the Lorentz Group|Lorentz generator]].

**Step 2: This says $\omega_{\mu\nu}$ is antisymmetric.**

> [!note]- Derivation
> Lower the first index of $\omega$ with $\eta$: $\omega_{\mu\nu} := \eta_{\mu\alpha}\omega^\alpha{}_\nu$, so $\eta\,\omega$ has components $(\eta\,\omega)_{\mu\nu} = \omega_{\mu\nu}$. The transpose term has components $(\omega^{\mathsf T}\eta)_{\mu\nu} = (\omega^{\mathsf T})_{\mu}{}^{\alpha}\eta_{\alpha\nu} = \omega^\alpha{}_\mu\,\eta_{\alpha\nu} = \eta_{\nu\alpha}\omega^\alpha{}_\mu = \omega_{\nu\mu}$. So the condition $\omega^{\mathsf T}\eta + \eta\,\omega = 0$ reads, component by component,
> $$\omega_{\nu\mu} + \omega_{\mu\nu} = 0 \qquad\Longleftrightarrow\qquad \omega_{\mu\nu} = -\omega_{\nu\mu},$$
> i.e. the index-lowered matrix $\omega_{\mu\nu}$ is **antisymmetric**. Equivalently, $\eta\,\omega$ is an antisymmetric matrix.

**Step 3: Boosts are symmetric, rotations antisymmetric; dimension six.**

> [!note]- Derivation
> An antisymmetric $4\times 4$ matrix $\omega_{\mu\nu}$ has $\binom{4}{2} = 6$ independent entries (those above the diagonal). Split them by index type. The **time-space** entries $\omega_{0i}$ ($i = 1,2,3$) give three independent parameters: these are the *boost* generators. The **space-space** entries $\omega_{ij}$ ($1 \le i < j \le 3$) give three more: these are the *rotation* generators.
>
> Now raise the first index back: $\omega^\mu{}_\nu = \eta^{\mu\alpha}\omega_{\alpha\nu}$. For a time-space entry, $\omega^0{}_i = \eta^{00}\omega_{0i} = +\omega_{0i}$ and $\omega^i{}_0 = \eta^{ii}\omega_{i0} = -\omega_{i0} = +\omega_{0i}$ (using antisymmetry $\omega_{i0} = -\omega_{0i}$). So $\omega^0{}_i = \omega^i{}_0$: the boost block of $\omega^\mu{}_\nu$ is **symmetric**. For a space-space entry, $\omega^i{}_j = \eta^{ii}\omega_{ij} = -\omega_{ij}$ and $\omega^j{}_i = -\omega_{ji} = +\omega_{ij}$, so $\omega^i{}_j = -\omega^j{}_i$: the rotation block of $\omega^\mu{}_\nu$ is **antisymmetric**. Hence as matrices $\omega^\mu{}_\nu$, boosts are symmetric and rotations antisymmetric, and there are $3 + 3 = 6$ generators, so $\dim\mathfrak{so}(1,3) = 6$.

**Step 4: Verify $K_1$ and $J_3$.**

> [!note]- Derivation
> $K_1$ has $1$ in the $(0,1)$ and $(1,0)$ positions and zeros elsewhere; it is symmetric, $K_1^{\mathsf T} = K_1$. Compute $\eta K_1$: multiplying $K_1$ on the left by $\eta = \mathrm{diag}(1,-1,-1,-1)$ scales row $0$ by $+1$ and row $1$ by $-1$, giving
> $$\eta K_1 = \begin{pmatrix} 0&1&0&0\\ -1&0&0&0\\ 0&0&0&0\\ 0&0&0&0 \end{pmatrix},$$
> which is antisymmetric. So $K_1$ satisfies the generator condition, confirming $K_1 \in \mathfrak{so}(1,3)$.
>
> $J_3$ has $-1$ in $(1,2)$ and $+1$ in $(2,1)$ (rotating $x$ into $y$); it is antisymmetric, $J_3^{\mathsf T} = -J_3$. Compute $\eta J_3$: scaling rows $1$ and $2$ by $-1$ gives
> $$\eta J_3 = \begin{pmatrix} 0&0&0&0\\ 0&0&1&0\\ 0&-1&0&0\\ 0&0&0&0 \end{pmatrix},$$
> still antisymmetric. So $J_3 \in \mathfrak{so}(1,3)$. Note the contrast: $K_1$ is symmetric, $J_3$ antisymmetric, yet *both* have $\eta\,\omega$ antisymmetric — exactly the content of Step 3.

> [!note]- Complete formal solution
> Substituting $\Lambda = \mathrm{Id} + \varepsilon\,\omega$ into $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ gives $\eta + \varepsilon(\omega^{\mathsf T}\eta + \eta\,\omega) + O(\varepsilon^2) = \eta$, so to first order $\omega^{\mathsf T}\eta + \eta\,\omega = 0$. In components, $(\eta\,\omega)_{\mu\nu} = \omega_{\mu\nu}$ and $(\omega^{\mathsf T}\eta)_{\mu\nu} = \omega_{\nu\mu}$, so the condition is $\omega_{\mu\nu} + \omega_{\nu\mu} = 0$ — the index-lowered $\omega_{\mu\nu}$ is antisymmetric. Such a matrix has six independent entries: three time-space ($\omega_{0i}$, the boosts) and three space-space ($\omega_{ij}$, the rotations). Raising the index back, $\omega^0{}_i = \omega^i{}_0$ (boosts symmetric) and $\omega^i{}_j = -\omega^j{}_i$ (rotations antisymmetric), with $\dim\mathfrak{so}(1,3) = 6$. Direct check: $\eta K_1$ and $\eta J_3$ are both antisymmetric, so $K_1$ (symmetric) and $J_3$ (antisymmetric) are both generators. $\blacksquare$

---

# Key Takeaways

**Linearising a defining equation is the universal recipe for a matrix Lie algebra, and the metric rides along.** The whole derivation is "substitute $\mathrm{Id} + \varepsilon\,\omega$, keep first order, set it to zero", and it computes the Lie algebra of *any* matrix group from its defining equation — the kernel of the differential of the constraint at the identity. For the orthogonal group $\Lambda^{\mathsf T}\Lambda = I$ it gives antisymmetry $\omega^{\mathsf T} + \omega = 0$; for the unitary group $\Lambda^\dagger\Lambda = I$ it gives skew-Hermiticity; for the Lorentz group the metric $\eta$ rides along and gives $\omega^{\mathsf T}\eta + \eta\,\omega = 0$. The trigger is any constraint of the form $f(\Lambda) = \text{const}$ evaluated near a known solution; the pattern is always to differentiate the constraint once. The Lorentz case differs from the orthogonal case by exactly the insertion of $\eta$, which is the single algebraic difference between Euclidean and Minkowski geometry.

**The antisymmetry is of $\omega_{\mu\nu}$ with both indices down, and this is why boosts are symmetric matrices.** The most common error in this computation is to conclude that $\omega$ itself is antisymmetric, by false analogy with the Euclidean case. The correct statement is that $\omega_{\mu\nu}$ — the matrix with its first index *lowered* by $\eta$ — is antisymmetric, and because $\eta$ flips the sign of spatial rows, the time-space entries of $\omega^\mu{}_\nu$ come out *symmetric*. So the boost generators are symmetric matrices and the rotation generators antisymmetric, even though both are "$\eta$-antisymmetric". The diagnostic to carry: whenever a metric appears in a group's defining equation, the algebra condition is antisymmetry (or skewness) *after the metric acts*, not before — and the symmetry type of the generators as plain matrices depends on where the metric's minus signs fall. This is why the membership test is "is $\eta\,\omega$ antisymmetric?", not "is $\omega$ antisymmetric?".

**The dimension count is the infinitesimal shadow of the group's parameter count.** The six independent entries of an antisymmetric $4\times 4$ matrix give $\dim\mathfrak{so}(1,3) = 6$, exactly matching $\dim SO^+(1,3) = 6$ from the group-level count $16 - 10 = 6$ (sixteen matrix entries minus ten conditions from the symmetric matrix equation $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$). This is no coincidence: the dimension of a Lie group as a manifold equals the dimension of its Lie algebra as a vector space, because the algebra *is* the tangent space. The split into three boosts and three rotations is the infinitesimal version of "three rapidities and three angles", and the general principle — count the constraints at the identity to get the dimension — is the fastest route to the dimension of any matrix group. For $\mathfrak{so}(p,q)$ in $n = p+q$ dimensions the same count gives $\binom{n}{2}$, the number of independent rotation planes.
