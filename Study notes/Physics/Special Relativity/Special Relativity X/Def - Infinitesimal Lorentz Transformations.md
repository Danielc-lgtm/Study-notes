---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Lorentz Group"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity, lie-groups]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(1,-1,-1,-1)$. A [[Def - The Lorentz Group|Lorentz transformation]] is a real $4\times 4$ matrix $\Lambda$ with $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$; its components are $\Lambda^\mu{}_\nu$. We write $\mathrm{Id}$ for the $4\times 4$ identity, $\varepsilon$ for a small real parameter, and $\omega, L$ for $4\times 4$ real matrices regarded as candidate generators. The transpose is $\omega^{\mathsf T}$, with components $(\omega^{\mathsf T})^\mu{}_\nu = \omega^\nu{}_\mu$. Lowering the first index with $\eta$ gives $\omega_{\mu\nu} = \eta_{\mu\alpha}\omega^\alpha{}_\nu$. Greek indices run $0$–$3$, Latin $1$–$3$. Full registry on [[Special Relativity X — The Lorentz Group as a Lie Group]].

> [!warning] Convention: Gourgoulhon's signature
> Gourgoulhon writes infinitesimal Lorentz transformations as $\Lambda = \mathrm{Id} + \varepsilon L$ with $L \in \mathfrak{so}(3,1)$ in the mostly-plus signature $\eta = \mathrm{diag}(-1,1,1,1)$, and obtains the condition "$\eta L$ is antisymmetric" (his Eq. 7.6). We use mostly-minus $\eta = \mathrm{diag}(1,-1,-1,-1)$; the condition is the *same equation in form*, $\omega^{\mathsf T}\eta + \eta\,\omega = 0$, because flipping the overall sign of $\eta$ flips both terms together. Only the explicit entries of $\eta$ differ.

---

# Axiom Motivation

The [[Def - The Lorentz Group|Lorentz group]] is a six-parameter continuous group, and to study it with the tools of calculus one looks first at the transformations *infinitely close to the identity* — the ones that move every event only slightly. The desideratum is a clean characterisation of these: which $4\times 4$ matrices arise as $\Lambda = \mathrm{Id} + \varepsilon\,\omega$ for a Lorentz transformation $\Lambda$, to first order in the small parameter $\varepsilon$? The answer is a linear condition on $\omega$, and that linear condition is the gateway to the Lie algebra. Everything finite about $SO^+(1,3)$ — boosts, rotations, their composition — will be reconstructed by exponentiating these infinitesimal pieces, so getting the condition exactly right is the foundation of the whole chapter.

The reason to expect a clean linear condition is that the defining equation of the group, $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$, is *quadratic* in $\Lambda$, and linearising a quadratic constraint about a solution always produces a linear constraint on the perturbation. We know $\Lambda = \mathrm{Id}$ is a solution (the identity preserves the interval), so we perturb around it: set $\Lambda = \mathrm{Id} + \varepsilon\,\omega$ and ask what $\omega$ must satisfy for $\Lambda$ to remain a Lorentz transformation through first order. Substituting,
$$
(\mathrm{Id} + \varepsilon\,\omega)^{\mathsf T}\,\eta\,(\mathrm{Id} + \varepsilon\,\omega)
= \eta + \varepsilon(\omega^{\mathsf T}\eta + \eta\,\omega) + \varepsilon^2\,\omega^{\mathsf T}\eta\,\omega,
$$
and demanding this equal $\eta$ kills the order-$\varepsilon$ term: $\omega^{\mathsf T}\eta + \eta\,\omega = 0$. The order-$\varepsilon^2$ term is dropped because we work to first order — it is precisely the piece the finite theory (the exponential map) will reinstate.

What does the condition *say*? Multiply through by recognising $\omega_{\mu\nu} := \eta_{\mu\alpha}\omega^\alpha{}_\nu$, the matrix $\omega$ with its first index lowered by the metric. The condition $\omega^{\mathsf T}\eta + \eta\,\omega = 0$ reads, in components, $\omega_{\nu\mu} + \omega_{\mu\nu} = 0$ — that is, **$\omega_{\mu\nu}$ is antisymmetric**. So the infinitesimal Lorentz generators are exactly the matrices that become antisymmetric once an index is lowered with $\eta$. This is the precise and frequently-quoted statement "$\omega$ is antisymmetric when an index is lowered", and it is the indefinite-signature analogue of the Euclidean fact that infinitesimal rotations are antisymmetric matrices.

It is worth seeing why the naive guess — that $\omega$ itself should be antisymmetric — is *wrong*, because the failure is instructive. In Euclidean signature ($\eta = \mathrm{Id}$) the condition collapses to $\omega^{\mathsf T} + \omega = 0$, genuine antisymmetry, and infinitesimal rotations are antisymmetric matrices. The Minkowski metric has a minus sign in the spatial block, and this is exactly what turns three of the six "antisymmetric" generators into *symmetric* matrices: lowering the time index with $\eta_{00} = +1$ leaves a sign alone, but the pairing of a time index with a space index (where $\eta$ contributes $+1$ on one side and $-1$ on the other) means the corresponding $\omega^\mu{}_\nu$ is symmetric while $\omega_{\mu\nu}$ is antisymmetric. The symmetric generators are the **boosts**; the antisymmetric ones are the **rotations**. If one had wrongly imposed antisymmetry on $\omega^\mu{}_\nu$ directly, one would have thrown away the boosts and kept only $\mathfrak{so}(3)$ — the rotation subalgebra — missing exactly the relativistic content. The lowered-index antisymmetry is the condition that keeps all six.

A final design point: why work to *first* order, and what is lost? Working to first order is what makes the constraint linear and hence makes the set of generators a *vector space* — closed under addition and real scaling, which is what an algebra needs. The second-order term $\varepsilon^2\,\omega^{\mathsf T}\eta\,\omega$ that we discarded does carry information, but it is information about how the group *curves* away from its tangent space, and that is recovered systematically by the exponential map and the Baker–Campbell–Hausdorff formula rather than by the linear condition. The infinitesimal transformation is the first term of a Taylor expansion of $\exp(\varepsilon\,\omega) = \mathrm{Id} + \varepsilon\,\omega + \tfrac12\varepsilon^2\omega^2 + \cdots$; the linear condition controls the first term, and the algebra's bracket controls how the higher terms assemble.

---

# The Definition

An **infinitesimal Lorentz transformation** is a transformation of the form
$$
\Lambda \;=\; \mathrm{Id} + \varepsilon\,\omega + O(\varepsilon^2),
$$
where $\varepsilon$ is a small real parameter and $\omega$ is a real $4\times 4$ matrix, required only to satisfy the defining condition of a [[Def - The Lorentz Group|Lorentz transformation]] *to first order in $\varepsilon$*. Substituting into $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ and keeping the order-$\varepsilon$ term gives the condition on $\omega$:
$$
\boxed{\;\omega^{\mathsf T}\,\eta + \eta\,\omega \;=\; 0\;}
\qquad\Longleftrightarrow\qquad
\omega_{\mu\nu} := \eta_{\mu\alpha}\,\omega^{\alpha}{}_{\nu}\ \text{ is antisymmetric},\quad \omega_{\mu\nu} = -\omega_{\nu\mu}.
$$
Such matrices $\omega$ are the **generators** of the Lorentz group; the set of all of them is the [[Def - Lie Algebra of the Lorentz Group|Lie algebra]] $\mathfrak{so}(1,3)$. Equivalently, $\eta\,\omega$ is an antisymmetric matrix, so $\omega = \eta(\eta\,\omega)$ with $\eta\,\omega \in \{$antisymmetric $4\times 4$ matrices$\}$; since there are $\binom{4}{2} = 6$ independent antisymmetric $4\times 4$ matrices, the generators form a six-dimensional real vector space.

The relation $\mathrm{Id} + \varepsilon\,\omega \in O(1,3)$ (to first order) holds **if and only if** $\omega \in \mathfrak{so}(1,3)$. Because the identity lies in the restricted (proper orthochronous) component, every infinitesimal Lorentz transformation is automatically proper and orthochronous: it deforms continuously from $\mathrm{Id}$, and $\det\Lambda = 1 + \varepsilon\,\mathrm{tr}\,\omega + O(\varepsilon^2)$ with $\mathrm{tr}\,\omega = 0$ keeps it on the $\det = +1$, $\Lambda^0{}_0 > 0$ sheet.

---

# Categorical / Structural Definition

Structurally, an infinitesimal Lorentz transformation is a **tangent vector to the Lie group $SO^+(1,3)$ at the identity**. The condition $\omega^{\mathsf T}\eta + \eta\,\omega = 0$ is precisely the statement that $\omega$ is the velocity $\dot\Lambda(0)$ of a smooth curve $\Lambda(s)$ in the group with $\Lambda(0) = \mathrm{Id}$: differentiating $\Lambda(s)^{\mathsf T}\eta\,\Lambda(s) = \eta$ at $s = 0$ and applying the product rule gives $\dot\Lambda(0)^{\mathsf T}\eta + \eta\,\dot\Lambda(0) = 0$, the boxed condition with $\omega = \dot\Lambda(0)$. This identifies the space of generators with the tangent space $T_{\mathrm{Id}}SO^+(1,3)$, which is the underlying vector space of the [[Def - The Lie Algebra of a Lie Group|Lie algebra of the group]]. The map $\omega \mapsto \eta\,\omega$ is then a linear isomorphism from $\mathfrak{so}(1,3)$ onto the space of antisymmetric $4\times 4$ matrices, the cleanest coordinatisation of the algebra.

This places the construction inside the general pattern of [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|matrix Lie theory]]: for a matrix group $G$ defined by an equation $f(\Lambda) = \text{const}$, the Lie algebra is $\ker\,df_{\mathrm{Id}}$, the kernel of the differential of the defining equation at the identity. For the orthogonal group $O(n)$ (defining equation $\Lambda^{\mathsf T}\Lambda = I$) this gives the antisymmetric matrices, $\mathfrak{so}(n)$. For the Lorentz group the same procedure with $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ gives the $\eta$-skew matrices, $\mathfrak{so}(1,3)$. The two computations are identical up to the replacement $I \to \eta$ — the single substitution that turns Euclidean geometry into Minkowski geometry — and the infinitesimal transformation is the object on which that substitution acts most transparently.

---

# Relate to Other Fields / Compression

The defining condition is the relativistic generalisation of "**infinitesimal rotations are antisymmetric matrices**", a fact the reader knows from rigid-body mechanics: an angular velocity $\boldsymbol\omega$ acts on a position vector as $\dot{\mathbf{r}} = \boldsymbol\omega \times \mathbf{r} = \Omega\,\mathbf{r}$, where $\Omega$ is the antisymmetric matrix (the hat of $\boldsymbol\omega$) generating the rotation. In the Lorentz case the generator $\omega$ is antisymmetric only *after lowering an index with $\eta$*, and the price of the indefinite metric is that three of the generators (the boosts) become *symmetric* matrices. So the slogan to carry is: rotations are antisymmetric, boosts are symmetric, and both are "$\eta$-antisymmetric" — the uniform condition that the Minkowski metric imposes.

**True name:** the generators are **"the matrices $\omega$ whose metric-lowered form $\eta\,\omega$ is antisymmetric"**. This is the form you check in practice: given a candidate $\omega$, multiply by $\eta$ and test whether the result is antisymmetric. It is also the form that makes the dimension count immediate — six independent antisymmetric $4\times 4$ matrices, hence six generators — and the form that generalises verbatim to $\mathfrak{so}(p,q)$ for any signature. The component statement $\omega_{\mu\nu} = -\omega_{\nu\mu}$ is the same fact written with both indices down, and it is the form in which the generator appears in field theory, where $\omega_{\mu\nu}$ is the antisymmetric array of six boost-and-rotation parameters multiplying the generators $\mathscr{J}^{\mu\nu}$.

---

# Examples / Corollaries

**Is an instance — an infinitesimal boost.** $\omega = \varepsilon K_1$ with $K_1$ the symmetric matrix having $1$ in the $(0,1)$ and $(1,0)$ slots gives $\Lambda = \mathrm{Id} + \varepsilon K_1$, an infinitesimal boost of rapidity $\varepsilon$ along $x$. Check: $\eta K_1$ has $\pm 1$ in the $(0,1)$ and $(1,0)$ entries with *opposite* signs (because $\eta_{00} = +1$, $\eta_{11} = -1$), hence $\eta K_1$ is antisymmetric and $K_1 \in \mathfrak{so}(1,3)$.

**Is an instance — an infinitesimal rotation.** $\omega = \varepsilon J_3$ with $J_3$ the antisymmetric matrix rotating the $x$–$y$ block gives an infinitesimal rotation by angle $\varepsilon$ about the $z$-axis. Check: $\eta J_3 = -J_3$ on the spatial block (since $\eta_{ii} = -1$ there), and $-J_3$ is antisymmetric, so $J_3 \in \mathfrak{so}(1,3)$.

**Is NOT an instance — an infinitesimal dilation.** $\omega = \varepsilon\,\mathrm{Id}$ gives $\Lambda = (1+\varepsilon)\mathrm{Id}$, a uniform rescaling. Its $\eta\,\omega = \varepsilon\,\eta$ is *symmetric*, not antisymmetric, so $\mathrm{Id} \notin \mathfrak{so}(1,3)$. Dilations preserve the light cone but not the interval, and this is the infinitesimal reason: the identity matrix is not $\eta$-antisymmetric.

**Is NOT an instance — a generic antisymmetric matrix in the wrong sense.** A matrix that is antisymmetric *before* lowering an index, such as the one with $+1$ in $(0,1)$ and $-1$ in $(1,0)$, has $\eta\,\omega$ *symmetric* and so is not a Lorentz generator. The correct boost generator $K_1$ is *symmetric* before lowering. This non-example is the trap the lowered-index condition exists to catch: it is $\omega_{\mu\nu}$, not $\omega^\mu{}_\nu$, that must be antisymmetric.

**Corollary — the commutator of an infinitesimal pair.** Two infinitesimal transformations $\Lambda_1 = \mathrm{Id} + \varepsilon L_1$, $\Lambda_2 = \mathrm{Id} + \varepsilon L_2$ have group commutator $\Lambda_1\Lambda_2\Lambda_1^{-1}\Lambda_2^{-1} = \mathrm{Id} + \varepsilon^2[L_1, L_2] + O(\varepsilon^3)$. The leading discrepancy from the identity is the *Lie bracket* $[L_1,L_2]$ — the infinitesimal record of the group's non-commutativity, and the reason the bracket is the natural operation on generators.

**Corollary — generators have zero trace.** Antisymmetry of $\eta\,\omega$ forces $\mathrm{tr}\,\omega = \mathrm{tr}(\eta\cdot\eta\,\omega) = 0$ on the basis (each $K_i$ and $J_i$ has zero diagonal). Hence $\det(\mathrm{Id} + \varepsilon\,\omega) = 1 + \varepsilon\,\mathrm{tr}\,\omega + O(\varepsilon^2) = 1 + O(\varepsilon^2)$ — every infinitesimal Lorentz transformation is proper.

**Calibration check.** You should be able to: (1) substitute $\Lambda = \mathrm{Id} + \varepsilon\,\omega$ into $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ and read off $\omega^{\mathsf T}\eta + \eta\,\omega = 0$; (2) explain in one sentence why this condition makes the boost generators symmetric but the rotation generators antisymmetric; (3) verify $\mathrm{tr}\,\omega = 0$ for any $\eta$-skew $\omega$.

---

# Unlocked by This

> [!tip] The Lie Algebra so(1,3) *(from §10.2)*
> The set of all generators $\omega$, with the matrix commutator as bracket, is the [[Def - Lie Algebra of the Lorentz Group|Lie algebra]] $\mathfrak{so}(1,3)$ — a six-dimensional real Lie algebra with basis the three boost generators $K_i$ and three rotation generators $J_i$, whose commutators encode the Thomas rotation and the entire local structure of $SO^+(1,3)$.

> [!tip] The Exponential Map *(from §10.3)*
> Iterating an infinitesimal transformation $N$ times and letting $N \to \infty$ produces the **exponential** $\exp(\omega) = \lim_{N\to\infty}(\mathrm{Id} + \omega/N)^N$, a *finite* Lorentz transformation. This is how $\mathrm{Id} + \varepsilon\,\omega$ grows into a full boost or rotation; see [[Thm - The Exponential Map Generates the Restricted Lorentz Group]].

> [!tip] The Field-Theory Form ω_μν 𝒥^μν *(from Quantum Field Theory)*
> In field theory the six independent components of the antisymmetric $\omega_{\mu\nu}$ are the parameters of an infinitesimal Lorentz transformation, contracted against the six generators $\mathscr{J}^{\mu\nu}$ as $\tfrac12\omega_{\mu\nu}\mathscr{J}^{\mu\nu}$. A relativistic field transforms by $\exp(-\tfrac{i}{2}\omega_{\mu\nu}\mathscr{J}^{\mu\nu})$ in whichever representation it carries, and this is the practical interface between the abstract algebra and **spinor and tensor fields**.
