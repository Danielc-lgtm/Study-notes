---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Levi-Civita Tensor"
  - "Def - Alternate Forms and the Exterior Product"
  - "Def - Metric Duality and Index Manipulation"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(1,-1,-1,-1)$. $E$ is the vector space of [[Def - Minkowski Space and the Metric|Minkowski space]], $(e_\alpha)$ a basis, $(e^\alpha)$ its [[Def - Metric Duality and Index Manipulation|dual basis]]; $g_{\alpha\beta}$ are the metric components, $g^{\alpha\beta}$ the inverse. $\mathscr{A}_p(E)$ is the space of [[Def - Alternate Forms and the Exterior Product|p-forms]] ($\dim\mathscr{A}_p = \binom{4}{p}$), and $\varepsilon$ is the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]] with components $\varepsilon_{\alpha\beta\gamma\delta}$. The Einstein convention sums an up–down pair; $p! = 1\cdot2\cdots p$. Full registry on [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality]].

> [!warning] Convention: the sign of $\star^2$ and the Lorentzian signature
> The defining feature for physics is $\star\star A = (-1)^{p+1}A$ on a $p$-form, so on $2$-forms $\star^2 = -1$. The general formula on a pseudo-Riemannian $n$-manifold is $\star\star = (-1)^{p(n-p)}\,\mathrm{sgn}(\det g)$; for $n = 4$, $p = 2$ this is $(+1)\cdot(-1) = -1$ because $\det g < 0$. Since $\det g < 0$ in **both** metric signatures, $\star^2 = -1$ on $2$-forms in any Lorentzian convention — this is a fact about the *signature being Lorentzian*, not about the sign choice. (In a Riemannian, positive-definite $4$-space one would instead get $\star^2 = +1$ on $2$-forms; the minus is the fingerprint of one timelike direction.)

---

# Axiom Motivation

The [[Def - Alternate Forms and the Exterior Product|exterior algebra]] has a striking numerical symmetry: $\dim\mathscr{A}_p(E) = \binom{4}{p} = \binom{4}{4-p} = \dim\mathscr{A}_{4-p}(E)$. A $0$-form and a $4$-form both have dimension $1$; a $1$-form and a $3$-form both have dimension $4$; and a $2$-form pairs with itself, dimension $6$. Whenever two vector spaces have the same dimension one should ask whether there is a *canonical* isomorphism between them — and the motivation for this page is that the metric plus an orientation supply exactly such an isomorphism, the **Hodge star** $\star : \mathscr{A}_p \to \mathscr{A}_{4-p}$. It is the operation that, in three dimensions, turns the plane spanned by two vectors into the perpendicular axis (the cross product), and in four dimensions turns the electric field into the magnetic field and back.

Why is a *metric* needed, when the dimension match is a pure exterior-algebra fact? Because the bare exterior algebra gives no canonical isomorphism $\mathscr{A}_p \cong \mathscr{A}_{4-p}$ — only a non-canonical one depending on a basis. The metric removes the basis-dependence. The construction is: to a $p$-form $A$, associate the $(4-p)$-form obtained by *contracting $A$ into the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]] $\varepsilon$*, using [[Def - Metric Duality and Index Manipulation|metric duality]] to raise $A$'s indices so they can be summed against $\varepsilon$'s lower indices. The metric enters twice: once through $\varepsilon$ itself (whose components carry $\sqrt{-\det g}$), and once to raise the indices of $A$. This is the unique natural way to map $p$-forms to $(4-p)$-forms that is linear, basis-independent, and built only from the geometric data $(g, \varepsilon)$. Without the metric there is no $\star$; with a *different* metric (e.g. positive-definite) the $\star$ changes, which is why its square is signature-sensitive.

The orientation is needed for the same reason it was needed for $\varepsilon$: the Hodge star inherits $\varepsilon$'s handedness. Flip the orientation and $\varepsilon \mapsto -\varepsilon$, so $\star \mapsto -\star$. The Hodge dual of a form is therefore a **pseudo**-form, well-defined only once a handedness is chosen. This is the algebraic origin of the fact that the magnetic field — which is $\star$ applied (in a sense) to the electric part of the field — is a pseudovector, flipping under a mirror reflection.

The single most consequential property, and the one this chapter is built around, is $\star\star = (-1)^{p+1}$. On $2$-forms this reads $\star^2 = -1$. The motivation to dwell on it: an operator squaring to $-1$ has no real eigenvalues, so over the reals $\star$ cannot be diagonalised on $\mathscr{A}_2(E)$ — but over the complexes it has eigenvalues $\pm i$, splitting the complexified space of $2$-forms into a **self-dual** and an **anti-self-dual** part. This is not a formal trick: it is the reason the electromagnetic field decomposes as $\mathbf E \pm i\mathbf B$, the reason the [[Def - Lie Algebra of the Lorentz Group|Lorentz Lie algebra]] complexifies into two copies of $\mathfrak{su}(2)$, and the reason a massless field of definite helicity is described by a self-dual (or anti-self-dual) field strength. The minus sign in $\star^2 = -1$ — which is there *because the signature is Lorentzian* — is the seed of the chirality of the field. Had the signature been Euclidean, $\star^2 = +1$ would give real eigenvalues $\pm 1$ and a real self-dual/anti-self-dual split (the instanton story), a genuinely different physics.

Why the factor $1/p!$ in the definition? It compensates the overcounting when summing over all $p$ index values rather than ordered ones, so that $\star$ acts cleanly on the strictly-ordered basis of $\mathscr{A}_{4-p}$. It is the same combinatorial bookkeeping as in the [[Def - Alternate Forms and the Exterior Product|wedge-basis expansion]] $A = \frac1{p!}A_{\alpha_1\dots\alpha_p}e^{\alpha_1}\wedge\cdots$, and choosing it correctly is exactly what makes $\star$ an isometry-respecting isomorphism rather than a map off by a numerical factor.

---

# The Definition

For each $p \in \{0,1,2,3,4\}$, the **Hodge star** is the linear map
$$
\star : \mathscr{A}_p(E) \longrightarrow \mathscr{A}_{4-p}(E), \qquad A \longmapsto \star A,
$$
defined on components by contracting $A$ (with raised indices) into the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]]:
$$
\boxed{\ (\star A)_{\alpha_1\dots\alpha_{4-p}} := \frac{1}{p!}\,\varepsilon_{\mu_1\dots\mu_p\,\alpha_1\dots\alpha_{4-p}}\; g^{\mu_1\nu_1}\cdots g^{\mu_p\nu_p}\; A_{\nu_1\dots\nu_p}\ }.
$$
The $(4-p)$-form $\star A$ is the **Hodge dual** of $A$. Explicitly:
$$
\begin{aligned}
p = 0: &\quad (\star A)_{\alpha\beta\gamma\delta} = A\,\varepsilon_{\alpha\beta\gamma\delta}, \\
p = 1: &\quad (\star A)_{\alpha\beta\gamma} = \varepsilon_{\mu\alpha\beta\gamma}\,g^{\mu\rho}A_\rho = A_\mu\,\varepsilon^\mu{}_{\alpha\beta\gamma}, \\
p = 2: &\quad (\star A)_{\alpha\beta} = \tfrac{1}{2}\,\varepsilon_{\mu\nu\alpha\beta}\,g^{\mu\rho}g^{\nu\sigma}A_{\rho\sigma} = \tfrac{1}{2}\,A_{\mu\nu}\,\varepsilon^{\mu\nu}{}_{\alpha\beta}, \\
p = 3: &\quad (\star A)_\alpha = \tfrac{1}{6}\,A_{\mu\nu\rho}\,\varepsilon^{\mu\nu\rho}{}_\alpha, \\
p = 4: &\quad \star A = \tfrac{1}{24}\,A_{\mu\nu\rho\sigma}\,\varepsilon^{\mu\nu\rho\sigma}.
\end{aligned}
$$
The Hodge star is an **isomorphism** of vector spaces (since $\dim\mathscr{A}_p = \dim\mathscr{A}_{4-p}$), and applying it twice gives
$$
\boxed{\ \star\star A = (-1)^{p+1}\,A \qquad \forall A \in \mathscr{A}_p(E)\ }.
$$
Hence $\star^{-1} = (-1)^{p+1}\star$. On $2$-forms, $4 - p = p = 2$, so $\star$ is an **automorphism** of the six-dimensional space $\mathscr{A}_2(E)$, with $\star^2 = -1$.

---

# Categorical / Structural Definition

The Hodge star is the composite of three canonical maps. First, raise all indices: [[Def - Metric Duality and Index Manipulation|metric duality]] gives $\sharp : \mathscr{A}_p(E) \to \Lambda^p E$ (a $p$-form with lower indices becomes a $p$-vector with upper indices). Second, contract into $\varepsilon$: the [[Def - The Levi-Civita Tensor|Levi-Civita]] form $\varepsilon \in \Lambda^4 E^*$ defines a map $\Lambda^p E \to \Lambda^{4-p}E^*$ by interior multiplication, $\xi \mapsto \iota_\xi\varepsilon$ (insert the $p$-vector into the first $p$ slots of $\varepsilon$). The Hodge star is $\star = \iota_{(\cdot)^\sharp}\varepsilon$, normalised by $1/p!$. Structurally, $\star$ is the isomorphism $\Lambda^p E^* \cong \Lambda^{4-p}E^*$ induced by the metric pairing $\Lambda^p E^* \otimes \Lambda^{4-p}E^* \to \Lambda^4 E^* \cong \mathbb{R}$ (wedge to the top, then divide by $\varepsilon$) — that is, $\star A$ is the unique $(4-p)$-form such that $B\wedge\star A = \langle B, A\rangle_g\,\varepsilon$ for every $p$-form $B$, where $\langle\cdot,\cdot\rangle_g$ is the metric-induced inner product on $\mathscr{A}_p$.

The identity $\star\star = (-1)^{p(n-p)}\mathrm{sgn}(\det g)$ is the statement that the bilinear pairing $(A,B) \mapsto B\wedge\star A$ is symmetric up to this sign; for $n = 4$ Lorentzian it is $(-1)^{p+1}$. On $\mathscr{A}_2(E)$, $\star^2 = -\mathrm{id}$ makes $(\mathscr{A}_2(E), \star)$ a **complex line's worth of structure** in disguise: $\star$ is a real linear operator with $\star^2 = -1$, i.e. a **complex structure** on the real six-dimensional space $\mathscr{A}_2(E)$, turning it into a complex three-dimensional space on which "multiplication by $i$" is "apply $\star$." This is the structural fact behind the self-dual/anti-self-dual decomposition.

This is the fibrewise version of the Hodge star on a [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition|(pseudo-)Riemannian manifold]], where $\star$ is the cornerstone of Hodge theory: the codifferential is $\delta = \pm\star d\star$, the Laplacian is $\Delta = d\delta + \delta d$, and harmonic forms represent cohomology. On a Lorentzian manifold the same $\star$ writes Maxwell's equations as $dF = 0$, $d\star F = \mu_0\star J$.

---

# Relate to Other Fields / Compression

In three dimensions the Hodge star is the operation that turns a vector into the plane perpendicular to it and vice versa: $\star$ sends a $1$-form to a $2$-form (a vector to the perpendicular oriented plane), and the **cross product** $\mathbf a\times\mathbf b$ is $\star(\mathbf a^\flat\wedge\mathbf b^\flat)$ raised back to a vector. The **curl** is $\star d$ on $1$-forms and the **divergence** is $\star d\star$ — the entire vector calculus of $\mathbb{R}^3$ is exterior derivative dressed with Hodge stars. In four-dimensional electromagnetism, $\star$ exchanges the electric and magnetic parts of the field strength, $\mathbf E \leftrightarrow \mathbf B$ (up to signs), which is the precise content of electric–magnetic duality and of the source-free symmetry of Maxwell's equations.

**True name:** $\star$ is *"contract a form into the volume form $\varepsilon$ after raising its indices with $g$" — the metric-and-orientation-induced isomorphism between the form on a subspace and the form on its orthogonal complement*. The single most useful fact to carry is $\star^2 = -1$ on $2$-forms: it says $\star$ is a complex structure, "multiplication by $i$," so the natural objects are the complex combinations $A \mp i\star A$ (self-dual / anti-self-dual). The reflex: to dualise, lower-the-degree by feeding into $\varepsilon$; to invert $\star$, apply it again and multiply by $(-1)^{p+1}$; on $2$-forms, think of $\star$ as $i$ and complexify.

---

# Examples / Corollaries

**Is an instance — the dual of a basis $2$-form.** With $\varepsilon_{0123} = 1$ in an orthonormal frame, $\star(e^0\wedge e^1) = -e^2\wedge e^3$ and $\star(e^2\wedge e^3) = e^0\wedge e^1$ (signs from the indefinite metric, computed in [[Ex - Computing the Hodge dual of a 2-form]]). Applying $\star$ twice returns $-e^0\wedge e^1$, confirming $\star^2 = -1$.

**Is an instance — the dual of the volume form.** For the $4$-form $A = \lambda\varepsilon$, $\star A = \frac{1}{24}A_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu\rho\sigma} = \frac{\lambda}{24}\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu\rho\sigma} = \frac{\lambda}{24}(-24) = -\lambda$. So $\star\varepsilon = -1$ (a $0$-form), and dually $\star 1 = \varepsilon$ — consistent with $\star\star = (-1)^{p+1}$ ($p = 0$ gives $\star\star = -1$, indeed $\star\star 1 = \star\varepsilon = -1$).

**Is an instance — the field-strength duality.** For the electromagnetic $2$-form $F$ with $(\mathbf E, \mathbf B)$, the dual $\star F$ has fields $(\mathbf E', \mathbf B') = (-\mathbf B, \mathbf E)$ (a quarter-turn in the $(\mathbf E, \mathbf B)$ plane), and the invariant $\star F^{\mu\nu}F_{\mu\nu} \propto \mathbf E\cdot\mathbf B$; see [[Special Relativity XXI — The Electromagnetic Field]].

**Is NOT an instance — a metric-free duality.** There is no Hodge star without a metric: the map "$p$-forms to $(4-p)$-forms" is not canonical in a bare vector space. The [[Def - Exterior Derivative on a Manifold|exterior derivative]] $d$ needs no metric, but $\star$ does — which is exactly why the homogeneous Maxwell equation $dF = 0$ is metric-free while the inhomogeneous $d\star F = \mu_0\star J$ uses the metric.

**Is NOT an instance — a real eigenvector of $\star$ on $2$-forms.** No nonzero *real* $2$-form satisfies $\star F = \lambda F$ for real $\lambda$, because $\star^2 = -1$ forces $\lambda^2 = -1$. Eigenforms exist only over $\mathbb{C}$, with $\lambda = \pm i$ — the self-dual and anti-self-dual forms.

**Corollary — $\star$ is invertible.** $\star^{-1} = (-1)^{p+1}\star$, so $\star$ is a bijection $\mathscr{A}_p \cong \mathscr{A}_{4-p}$; in particular it is an automorphism of $\mathscr{A}_2(E)$.

**Corollary — $\star$ defines a complex structure on $2$-forms.** Since $\star^2 = -1$ on the real six-dimensional $\mathscr{A}_2(E)$, $\star$ makes it a complex three-dimensional space, with $\star = $ "multiplication by $i$." The eigenspaces over $\mathbb{C}$ are the self-dual ($\star F = iF$) and anti-self-dual ($\star F = -iF$) subspaces, each of complex dimension $3$.

**Calibration check.** If you have understood the definition you can: (i) compute $\star(e^0\wedge e^1)$ in an orthonormal frame and verify $\star^2(e^0\wedge e^1) = -e^0\wedge e^1$; (ii) explain why $\star$ needs a metric but $d$ does not; (iii) state why $\star^2 = -1$ forces complexification and name the resulting eigenspaces.

---

# Unlocked by This

> [!tip] The Self-Dual / Anti-Self-Dual Decomposition *(from §18.3)*
> Because $\star^2 = -1$ on $2$-forms, the complexified space $\mathscr{A}_2(E)\otimes\mathbb{C}$ splits into the $\pm i$ eigenspaces of $\star$ — the **self-dual** and **anti-self-dual** $2$-forms. For the field strength this is the decomposition into $\mathbf E + i\mathbf B$ and $\mathbf E - i\mathbf B$, and it matches the $(1,0)\oplus(0,1)$ splitting of the [[Def - Lie Algebra of the Lorentz Group|Lorentz Lie algebra]]; see [[Thm - Orthogonal Decomposition of 2-Forms]].

> [!tip] Maxwell's Equations and Electric-Magnetic Duality *(from Electromagnetism)*
> The Hodge star is what makes Maxwell's equations close: $dF = 0$ (no metric) and $d\star F = \mu_0\star J$ (metric, via $\star$). The source-free equations are invariant under $F \mapsto \star F$, the **electric-magnetic duality** $\mathbf E \to \mathbf B$, $\mathbf B \to -\mathbf E$; see [[Special Relativity XXII — Maxwell's Equations]] and the energy-momentum tensor of [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

> [!tip] Hodge Theory and Harmonic Forms *(from Topology and Geometry)*
> Promoted to a field on a manifold, $\star$ defines the codifferential $\delta = -\star d\star$ (signs depending on degree and signature) and the Hodge Laplacian $\Delta = d\delta + \delta d$; the **Hodge decomposition** writes every form as exact + co-exact + harmonic, and harmonic forms represent de Rham cohomology. On a Lorentzian manifold the wave operator replaces the Laplacian; see [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].
