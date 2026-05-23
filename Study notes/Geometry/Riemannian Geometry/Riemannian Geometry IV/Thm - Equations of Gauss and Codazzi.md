---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - First Fundamental Form"
  - "Def - Second Fundamental Form"
  - "Def - Shape Operator (Weingarten Map)"
tags: [geometry, riemannian-geometry, surfaces, integrability]
---

# Notation

Let $M \subset \mathbb{R}^3$ be an oriented regular surface, with first fundamental form $g_{\alpha\beta}$, second fundamental form $b_{\alpha\beta}$, Christoffel symbols $\Gamma^\gamma_{\alpha\beta}$ of $g$, and Riemann curvature components $R^\tau_{\;\alpha\gamma\beta}$ of $g$. We write $b^\alpha_{\;\beta} = g^{\alpha\gamma}b_{\gamma\beta}$ for the shape operator's matrix and $b_{\alpha\beta;\gamma}$ for the covariant derivative $\partial_\gamma b_{\alpha\beta} - \Gamma^\sigma_{\alpha\gamma}b_{\sigma\beta} - \Gamma^\sigma_{\beta\gamma}b_{\alpha\sigma}$ of the second fundamental form. Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

---

# Statement

> **Theorem (Gauss and Codazzi–Mainardi–Peterson Equations).** For a smooth regular surface $M \subset \mathbb{R}^3$ with first fundamental form $g_{\alpha\beta}$ and second fundamental form $b_{\alpha\beta}$:
>
> **(Gauss equations.)** The Riemann curvature tensor of the induced metric satisfies
> $$
> R^\tau_{\;\alpha\gamma\beta} = b^\tau_{\;\gamma}b_{\alpha\beta} - b^\tau_{\;\beta}b_{\alpha\gamma}.
> $$
>
> **(Codazzi equations.)** The covariant derivatives of $b_{\alpha\beta}$ are symmetric in the last two indices:
> $$
> b_{\alpha\beta;\gamma} = b_{\alpha\gamma;\beta},
> $$
> equivalently
> $$
> \partial_\gamma b_{\alpha\beta} - \Gamma^\sigma_{\alpha\gamma}b_{\sigma\beta} - \Gamma^\sigma_{\beta\gamma}b_{\alpha\sigma} = \partial_\beta b_{\alpha\gamma} - \Gamma^\sigma_{\alpha\beta}b_{\sigma\gamma} - \Gamma^\sigma_{\gamma\beta}b_{\alpha\sigma}.
> $$

> **Corollary (Bonnet's Fundamental Theorem of Surface Theory).** Given smooth symmetric matrix-valued functions $g_{\alpha\beta}(u, v)$ (positive-definite) and $b_{\alpha\beta}(u, v)$ on an open simply-connected $U \subset \mathbb{R}^2$ that satisfy the Gauss and Codazzi equations, there exists a smooth surface $\mathbf{x} : U \to \mathbb{R}^3$ with $g_{\alpha\beta}$ and $b_{\alpha\beta}$ as its first and second fundamental forms. The surface is unique up to rigid motion.

---

# Motivation

These equations are the **integrability conditions** for the pair $(g_{\alpha\beta}, b_{\alpha\beta})$ to come from an actual surface in $\mathbb{R}^3$. Not every pair of symmetric matrices is realisable: most pairs would fail to satisfy $\mathbf{x}_{\alpha\beta\gamma} = \mathbf{x}_{\alpha\gamma\beta}$ (commutativity of mixed partials), and the Gauss + Codazzi equations are exactly the algebraic conditions that capture this commutativity. Bonnet's converse — that the conditions are also sufficient — says nothing more is needed: any pair satisfying both equations determines a unique surface up to rigid motion.

The Gauss equation is the heart of [[Thm - Theorema Egregium of Gauss|Theorema Egregium]]: it expresses the intrinsic Riemann curvature in terms of the extrinsic shape operator, with the consequence that one specific combination (the $(1,2,1,2)$ component, hence $K$) is intrinsic. The Codazzi equation is the second integrability condition, which constrains how $b_{\alpha\beta}$ varies from point to point and is used in many rigidity theorems (e.g., constant-mean-curvature surfaces, the Hilbert–Liebmann theorem on umbilic surfaces).

In modern language, the Gauss + Codazzi equations are the **structure equations of the embedding**, exactly analogous to **Cartan's structural equations** for a connection on a vector bundle. The Gauss equation says: "the curvature of the induced connection on $TM$ equals the quadratic combination of the second fundamental form". The Codazzi equation says: "the second fundamental form is a closed normal-valued tensor under the natural connection on the normal bundle". Both have natural higher-dimensional analogues in submanifold geometry.

---

# Sources and Targets

**Sources (Input Broadening).**

*Source 1: An ansatz for $g_{\alpha\beta}$ and $b_{\alpha\beta}$ on a surface to be constructed.* When trying to construct a surface with specified fundamental forms (e.g., a surface with prescribed Gauss curvature, or one whose principal curvatures satisfy a given relation), one assembles candidates $g_{\alpha\beta}$ and $b_{\alpha\beta}$ and must check the Gauss + Codazzi equations to verify realisability. **Why $B \Rightarrow A$:** Bonnet's converse says: if the equations are satisfied, a surface exists. **Example problem:** Construct a surface with $K = -1$ and given $H$ — set up an ansatz, check the equations, conclude existence.

*Source 2: A surface known by an explicit parametrisation, where one wants to derive intrinsic identities.* The Gauss equation in particular is the tool for proving Theorema Egregium and for computing the Riemann curvature of an induced metric efficiently. **Why $B \Rightarrow A$:** The Gauss equation gives a direct extrinsic-to-intrinsic translation. **Example problem:** For the sphere of radius $a$, compute $R_{1212}$ directly from the metric Christoffel symbols, verify $R_{1212} = a^2$ (= $\det b_{\alpha\beta}$), confirm $K = R_{1212}/\det g = 1/a^2$.

*Source 3: A constant-mean-curvature condition $H = c$.* The Codazzi equations, combined with $H = \text{const}$, lead to powerful rigidity results — for instance Hopf's theorem that the only CMC sphere in $\mathbb{R}^3$ is the round sphere. **Why $B \Rightarrow A$:** Codazzi expresses how $b$ changes from point to point; constraining $H = \text{const}$ then forces algebraic constraints on the variation of $b$. **Example problem:** A closed CMC surface in $\mathbb{R}^3$ topologically $S^2$ must be the round sphere — Codazzi + max principle force umbilicity, then Hilbert–Liebmann gives the sphere.

**Targets (Output Amplification).**

*Target 1: Theorema Egregium and its corollaries.* The Gauss equation directly proves $K = R_{1212}/\det g$ is intrinsic. **Why nonobvious:** Without Gauss equations, one would not see why the extrinsic-looking ratio $\det b/\det g$ should depend only on $g$. **Application:** Cartography (no flat map of the sphere is distortion-free), uniformisation, intrinsic Riemannian geometry.

*Target 2: Bonnet's existence and uniqueness theorem.* The Gauss and Codazzi equations together are necessary *and* sufficient for the realisability of a pair $(g_{\alpha\beta}, b_{\alpha\beta})$ as the fundamental forms of a surface, unique up to rigid motion. **Why nonobvious:** Necessity is straightforward (just commutativity of partials); sufficiency is a substantial PDE argument (the Frobenius-style integrability for an overdetermined first-order PDE system on $\mathbf{x}$, $N$, and the moving frame). **Application:** This is what makes the *moduli problem* of surfaces well-posed: surfaces are parametrised by pairs $(g, b)$ satisfying Gauss + Codazzi, modulo rigid motion.

*Target 3: Rigidity theorems via Codazzi.* Conditions like "all points are umbilic" or "$H$ is constant" combine with Codazzi to force strong rigidity. **Hilbert–Liebmann theorem:** the only closed surface in $\mathbb{R}^3$ with all points umbilic is the sphere. **Hopf's theorem:** the only immersed CMC sphere in $\mathbb{R}^3$ is the round sphere. **Why nonobvious:** Codazzi forces the umbilic / CMC conditions to propagate from a single point to the whole surface in a very controlled way.

---

# Why Is It True

The Gauss + Codazzi equations are the consequence of a single fundamental fact: **mixed partial derivatives of $\mathbf{x}$ commute**, $\mathbf{x}_{\alpha\beta\gamma} = \mathbf{x}_{\alpha\gamma\beta}$. This is Clairaut's theorem for smooth functions, and it forces algebraic constraints on the surface equations whenever those equations involve any second-derivative structure.

The mechanism: the surface equations $\mathbf{x}_{\alpha\beta} = \Gamma^\gamma_{\alpha\beta}\mathbf{x}_\gamma + b_{\alpha\beta}N$ encode all second derivatives of $\mathbf{x}$ in terms of intrinsic ($\Gamma$) and extrinsic ($b$) coefficients. Taking *another* derivative gives third derivatives in two equivalent ways — $\partial_\gamma\mathbf{x}_{\alpha\beta}$ and $\partial_\beta\mathbf{x}_{\alpha\gamma}$. Equating them and matching coefficients of $\mathbf{x}_\delta$ and $N$ separately gives two sets of equations: the tangential-coefficient equation is the **Gauss equation**, the normal-coefficient equation is the **Codazzi equation**.

**The bolded one-liner:** **the Gauss equation says "intrinsic Riemann curvature equals a quadratic combination of extrinsic data" (the tangential part of $\mathbf{x}_{\alpha\beta\gamma} - \mathbf{x}_{\alpha\gamma\beta} = 0$), and the Codazzi equation says "extrinsic data is covariantly closed" (the normal part).**

The geometric content of Gauss: $K$ measures how parallel transport fails to be commutative around an infinitesimal loop in $M$, and this failure is exactly the wedge product of the second fundamental form's eigenstructure (the principal curvatures $\kappa_1\kappa_2$). The Codazzi equation, geometrically, says that the second fundamental form is "covariantly closed" in the normal direction — a kind of integrability condition saying that "the principal curvature data is consistent as one moves on $M$".

In the bundle-theoretic language: the Gauss + Codazzi equations together state that the connection on $TM \oplus \nu M = T\mathbb{R}^3|_M$ (the trivial $\mathbb{R}^3$ bundle restricted to $M$) splits into the Levi-Civita connection on $TM$ + the trivial connection on $\nu M$, with $b$ being the "off-diagonal" piece (the second fundamental form as a normal-vector-valued $1$-form on $TM$). The Gauss equation is the curvature of the diagonal Levi-Civita connection; Codazzi is the closedness of the off-diagonal piece. This formulation generalises directly to submanifolds of arbitrary Riemannian manifolds.

---

# What Makes This Hard

The hard part is the **bookkeeping**: differentiating $\mathbf{x}_{\alpha\beta} = \Gamma^\gamma_{\alpha\beta}\mathbf{x}_\gamma + b_{\alpha\beta}N$ with respect to $u^\gamma$, applying $\mathbf{x}_{\delta\gamma}$ via the same Gauss formula recursively, applying the Weingarten equation $N_\gamma = -b^\sigma_{\;\gamma}\mathbf{x}_\sigma$, then symmetrising $\beta \leftrightarrow \gamma$ and matching tangential vs normal coefficients separately. Each step is mechanical, but the combined computation is tedious and error-prone. The result has 4-index tensors, mixed-position covariant/contravariant indices, and Christoffel-symbol products — easy to make sign and index errors.

The conceptual difficulty: separating the tangential and normal components correctly requires keeping track that the right-hand side of $\mathbf{x}_{\alpha\beta\gamma} = \mathbf{x}_{\alpha\gamma\beta}$ has tangent-plus-normal decomposition, and that the antisymmetrisation in $\beta \leftrightarrow \gamma$ acts on each piece separately. Skipping this separation leads to a single complicated equation rather than two clean ones (Gauss + Codazzi).

The proof of **Bonnet's converse** (the *sufficient* direction) is genuinely harder than the necessary direction proved here: it is a Frobenius-style integrability argument for an overdetermined first-order PDE system on $(\mathbf{x}, \mathbf{x}_1, \mathbf{x}_2, N)$, where the Gauss + Codazzi equations serve as the integrability conditions. We sketch this in Lemma 3 below.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Differentiate the surface equation $\mathbf{x}_{\alpha\beta} = \Gamma^\gamma_{\alpha\beta}\mathbf{x}_\gamma + b_{\alpha\beta}N$ once more with respect to $u^\gamma$, applying the Gauss equation and the Weingarten equation $N_\gamma = -b^\sigma_{\;\gamma}\mathbf{x}_\sigma$ to expand $\mathbf{x}_{\delta\gamma}$ and $N_\gamma$. Symmetrise $\beta \leftrightarrow \gamma$ and use $\mathbf{x}_{\alpha\beta\gamma} = \mathbf{x}_{\alpha\gamma\beta}$. Match coefficients of $\mathbf{x}_\delta$ (giving Gauss) and $N$ (giving Codazzi) separately.

**Subgoal decomposition:**

1. **Compute $\mathbf{x}_{\alpha\beta\gamma}$ via differentiation.** Take $\partial_\gamma$ of $\mathbf{x}_{\alpha\beta} = \Gamma^\delta_{\alpha\beta}\mathbf{x}_\delta + b_{\alpha\beta}N$, expand $\mathbf{x}_{\delta\gamma}$ and $N_\gamma$ via the Gauss and Weingarten equations.
   - *Hint:* Use the product rule on each term; the Gauss equation $\mathbf{x}_{\delta\gamma} = \Gamma^\sigma_{\delta\gamma}\mathbf{x}_\sigma + b_{\delta\gamma}N$ and Weingarten $N_\gamma = -b^\sigma_{\;\gamma}\mathbf{x}_\sigma$.
   - *Why needed:* This yields a closed-form expression for $\mathbf{x}_{\alpha\beta\gamma}$ as a linear combination of $\mathbf{x}_\sigma$ and $N$.

2. **Symmetrise in $\beta \leftrightarrow \gamma$ and use $\mathbf{x}_{\alpha\beta\gamma} = \mathbf{x}_{\alpha\gamma\beta}$.** The difference must be zero. Match coefficients of $\mathbf{x}_\delta$ (tangential) and $N$ (normal) separately.
   - *Hint:* The tangential part will involve Christoffel-derivative combinations and $b\cdot b$ products; the normal part will involve $\Gamma\cdot b$ products and $b$-derivatives.
   - *Why needed:* The tangential equation is Gauss; the normal equation is Codazzi.

3. **Identify the Riemann tensor.** The tangential equation's left side $\partial_\gamma\Gamma^\delta_{\alpha\beta} - \partial_\beta\Gamma^\delta_{\alpha\gamma} + \Gamma^\sigma_{\alpha\beta}\Gamma^\delta_{\sigma\gamma} - \Gamma^\sigma_{\alpha\gamma}\Gamma^\delta_{\sigma\beta}$ is exactly $R^\delta_{\;\alpha\gamma\beta}$, by definition of the Riemann tensor in terms of Christoffel symbols.
   - *Hint:* Look up the definition of $R^\delta_{\;\alpha\gamma\beta}$ in terms of $\Gamma$ and match term by term.
   - *Why needed:* This identifies the tangential equation as $R^\delta_{\;\alpha\gamma\beta} = b^\delta_{\;\gamma}b_{\alpha\beta} - b^\delta_{\;\beta}b_{\alpha\gamma}$, the Gauss equation.

4. **Conclude.** Tangential gives Gauss; normal gives Codazzi.

---

# Lemma Decomposition

> [!note]- Lemma 1: Third partial derivative via Gauss + Weingarten
> **Statement:** Starting from $\mathbf{x}_{\alpha\beta} = \Gamma^\delta_{\alpha\beta}\mathbf{x}_\delta + b_{\alpha\beta}N$ and applying $\partial_\gamma$,
> $$
> \mathbf{x}_{\alpha\beta\gamma} = \big[\partial_\gamma\Gamma^\delta_{\alpha\beta} + \Gamma^\sigma_{\alpha\beta}\Gamma^\delta_{\sigma\gamma} - b_{\alpha\beta}b^\delta_{\;\gamma}\big]\mathbf{x}_\delta + \big[\Gamma^\sigma_{\alpha\beta}b_{\sigma\gamma} + \partial_\gamma b_{\alpha\beta}\big]N.
> $$
>
> **Hint:** Use the product rule on $\Gamma^\delta_{\alpha\beta}\mathbf{x}_\delta + b_{\alpha\beta}N$; expand $\mathbf{x}_{\delta\gamma}$ and $N_\gamma$ via the Gauss equation and Weingarten equation respectively.
>
> **Why needed:** This is the explicit formula for $\mathbf{x}_{\alpha\beta\gamma}$ as a linear combination of $\mathbf{x}_\delta$ and $N$, in terms of $\Gamma, b$ and their derivatives. The symmetrisation in step 2 is on this expression.
>
> > [!note]- Full proof
> > Direct expansion:
> > $$
> > \mathbf{x}_{\alpha\beta\gamma} = \partial_\gamma(\Gamma^\delta_{\alpha\beta}\mathbf{x}_\delta + b_{\alpha\beta}N) = (\partial_\gamma\Gamma^\delta_{\alpha\beta})\mathbf{x}_\delta + \Gamma^\delta_{\alpha\beta}\mathbf{x}_{\delta\gamma} + (\partial_\gamma b_{\alpha\beta})N + b_{\alpha\beta}N_\gamma.
> > $$
> > Substitute $\mathbf{x}_{\delta\gamma} = \Gamma^\sigma_{\delta\gamma}\mathbf{x}_\sigma + b_{\delta\gamma}N$ and $N_\gamma = -b^\sigma_{\;\gamma}\mathbf{x}_\sigma$:
> > $$
> > \mathbf{x}_{\alpha\beta\gamma} = (\partial_\gamma\Gamma^\delta_{\alpha\beta})\mathbf{x}_\delta + \Gamma^\delta_{\alpha\beta}(\Gamma^\sigma_{\delta\gamma}\mathbf{x}_\sigma + b_{\delta\gamma}N) + (\partial_\gamma b_{\alpha\beta})N - b_{\alpha\beta}b^\sigma_{\;\gamma}\mathbf{x}_\sigma.
> > $$
> > Rearranging into tangential ($\mathbf{x}$) and normal ($N$) pieces, and relabelling dummy indices ($\sigma \to \delta$ where convenient), gives the stated formula.

> [!note]- Lemma 2: Symmetrisation gives Gauss + Codazzi
> **Statement:** Setting $\mathbf{x}_{\alpha\beta\gamma} - \mathbf{x}_{\alpha\gamma\beta} = 0$ and matching tangential and normal coefficients:
>
> *Tangential ($\mathbf{x}_\delta$ coefficient):*
> $$
> \partial_\gamma\Gamma^\delta_{\alpha\beta} - \partial_\beta\Gamma^\delta_{\alpha\gamma} + \Gamma^\sigma_{\alpha\beta}\Gamma^\delta_{\sigma\gamma} - \Gamma^\sigma_{\alpha\gamma}\Gamma^\delta_{\sigma\beta} = b_{\alpha\beta}b^\delta_{\;\gamma} - b_{\alpha\gamma}b^\delta_{\;\beta},
> $$
> which is the **Gauss equation** $R^\delta_{\;\alpha\gamma\beta} = b^\delta_{\;\gamma}b_{\alpha\beta} - b^\delta_{\;\beta}b_{\alpha\gamma}$ (with sign convention).
>
> *Normal ($N$ coefficient):*
> $$
> \Gamma^\sigma_{\alpha\beta}b_{\sigma\gamma} + \partial_\gamma b_{\alpha\beta} = \Gamma^\sigma_{\alpha\gamma}b_{\sigma\beta} + \partial_\beta b_{\alpha\gamma},
> $$
> the **Codazzi equation** $b_{\alpha\beta;\gamma} = b_{\alpha\gamma;\beta}$.
>
> **Hint:** Take the formula from Lemma 1, swap $\beta \leftrightarrow \gamma$ to get $\mathbf{x}_{\alpha\gamma\beta}$, subtract, and equate coefficients of $\mathbf{x}_\delta$ and $N$ to zero separately (since $\{\mathbf{x}_\delta, N\}$ is a basis of $\mathbb{R}^3$ along $M$).
>
> **Why needed:** This is where the integrability condition $\mathbf{x}_{\alpha\beta\gamma} = \mathbf{x}_{\alpha\gamma\beta}$ is converted into algebraic identities on $(\Gamma, b)$.
>
> > [!note]- Full proof
> > From Lemma 1,
> > $$
> > \mathbf{x}_{\alpha\beta\gamma} - \mathbf{x}_{\alpha\gamma\beta} = \big[\big(\partial_\gamma\Gamma^\delta_{\alpha\beta} - \partial_\beta\Gamma^\delta_{\alpha\gamma}\big) + \big(\Gamma^\sigma_{\alpha\beta}\Gamma^\delta_{\sigma\gamma} - \Gamma^\sigma_{\alpha\gamma}\Gamma^\delta_{\sigma\beta}\big) - \big(b_{\alpha\beta}b^\delta_{\;\gamma} - b_{\alpha\gamma}b^\delta_{\;\beta}\big)\big]\mathbf{x}_\delta + \big[\big(\Gamma^\sigma_{\alpha\beta}b_{\sigma\gamma} - \Gamma^\sigma_{\alpha\gamma}b_{\sigma\beta}\big) + \big(\partial_\gamma b_{\alpha\beta} - \partial_\beta b_{\alpha\gamma}\big)\big]N.
> > $$
> > Setting this equal to zero and using linear independence of $\{\mathbf{x}_\delta, N\}$, both bracketed coefficients vanish, yielding the Gauss and Codazzi equations.

> [!note]- Lemma 3: Bonnet's existence and uniqueness (sketch of the converse direction)
> **Statement:** Given smooth $g_{\alpha\beta}(u, v)$ (symmetric positive-definite) and $b_{\alpha\beta}(u, v)$ (symmetric) on a simply-connected $U \subset \mathbb{R}^2$ satisfying the Gauss and Codazzi equations, there exists a smooth $\mathbf{x} : U \to \mathbb{R}^3$ with first and second fundamental forms exactly $g_{\alpha\beta}$ and $b_{\alpha\beta}$. The surface is unique up to rigid motion.
>
> **Hint:** Set up the first-order PDE system: at each $(u, v)$, the data $(\mathbf{x}, \mathbf{x}_1, \mathbf{x}_2, N) \in \mathbb{R}^{12}$ satisfies $\partial_\alpha(\mathbf{x}_1, \mathbf{x}_2, N) = \Gamma\cdot(\mathbf{x}_1, \mathbf{x}_2) + b\cdot N$ via Gauss + Weingarten. The Frobenius integrability conditions for this overdetermined system are exactly the Gauss + Codazzi equations. Simple-connectedness of $U$ ensures global integrability.
>
> **Why needed:** This is what makes the Gauss + Codazzi equations *sufficient* (not just necessary) for a surface to exist with prescribed fundamental forms. Without this, the equations would only be a partial check.
>
> > [!note]- Full proof (sketch)
> > Define the system: at each $(u, v) \in U$, we want $(\mathbf{x}, \mathbf{x}_1, \mathbf{x}_2, N) \in \mathbb{R}^3 \times (\mathbb{R}^3)^3$ to satisfy
> > $$
> > \partial_\alpha \mathbf{x} = \mathbf{x}_\alpha, \quad \partial_\alpha \mathbf{x}_\beta = \Gamma^\gamma_{\alpha\beta}\mathbf{x}_\gamma + b_{\alpha\beta}N, \quad \partial_\alpha N = -b^\sigma_{\;\alpha}\mathbf{x}_\sigma,
> > $$
> > plus the algebraic constraints $\langle\mathbf{x}_\alpha, \mathbf{x}_\beta\rangle = g_{\alpha\beta}$ and $|N| = 1$, $\langle\mathbf{x}_\alpha, N\rangle = 0$. This is a first-order PDE system on the $12$-dimensional space of $(\mathbf{x}, \mathbf{x}_1, \mathbf{x}_2, N)$. The Frobenius theorem says: a first-order overdetermined PDE system $\partial_\alpha\mathbf{y} = F_\alpha(\mathbf{y})$ has a solution iff the integrability conditions $\partial_\beta F_\alpha = \partial_\alpha F_\beta$ hold (after substituting the PDE itself for $\partial_\beta\mathbf{y}$). Direct computation shows that these integrability conditions for our system are exactly the Gauss + Codazzi equations together with the metric-compatibility identities $\partial_\alpha\langle\mathbf{x}_\beta, \mathbf{x}_\gamma\rangle = \langle\partial_\alpha\mathbf{x}_\beta, \mathbf{x}_\gamma\rangle + \langle\mathbf{x}_\beta, \partial_\alpha\mathbf{x}_\gamma\rangle$, which are consistent when $\Gamma$ is the Christoffel symbol of $g$. Since $U$ is simply connected, the local Frobenius solutions glue into a unique global solution up to the initial data $(\mathbf{x}(u_0, v_0), \mathbf{x}_1(u_0, v_0), \mathbf{x}_2(u_0, v_0), N(u_0, v_0))$, which is determined up to a rigid motion of $\mathbb{R}^3$.

---

# Formal Proof

> [!note]- Complete formal proof (necessity)
> Apply Lemmas 1 and 2 directly. Differentiating the surface equation $\mathbf{x}_{\alpha\beta} = \Gamma^\delta_{\alpha\beta}\mathbf{x}_\delta + b_{\alpha\beta}N$ once with respect to $u^\gamma$, expanding $\mathbf{x}_{\delta\gamma}$ via the Gauss equation and $N_\gamma$ via the Weingarten equation, then symmetrising over $\beta \leftrightarrow \gamma$ and using $\mathbf{x}_{\alpha\beta\gamma} = \mathbf{x}_{\alpha\gamma\beta}$, gives two equations: the tangential equation $R^\delta_{\;\alpha\gamma\beta} = b^\delta_{\;\gamma}b_{\alpha\beta} - b^\delta_{\;\beta}b_{\alpha\gamma}$ (the **Gauss equation**) and the normal equation $b_{\alpha\beta;\gamma} = b_{\alpha\gamma;\beta}$ (the **Codazzi equation**). For sufficiency (Bonnet's converse), see Lemma 3.

---

# Cross-Field Exercise Suggestions

1. **Constant Gauss curvature surfaces (Gauss equation as ODE).** For a surface of revolution $\mathbf{x}(u, v) = (r(u)\cos v, r(u)\sin v, z(u))$ with arc-length meridian parametrisation ($r'^2 + z'^2 = 1$), the Gauss equation gives $K = -r''/r$ via Theorema Egregium. Setting $K = K_0$ constant and solving the ODE $r'' = -K_0 r$ gives $r(u) = A\sin(\sqrt{K_0}\, u)$ for $K_0 > 0$ (the sphere), $r(u) = A u + B$ for $K_0 = 0$ (the cone or cylinder), $r(u) = Ae^{\sqrt{-K_0}\, u} + Be^{-\sqrt{-K_0}\, u}$ for $K_0 < 0$ (a pseudosphere variant). The Codazzi equation imposes additional constraints on $b$ that need to be checked. **Why nonobvious:** The interplay of the two equations is what determines whether a candidate $(g, b)$ comes from a surface.

2. **Hopf's theorem: the only CMC sphere in $\mathbb{R}^3$ is the round sphere.** Consider a closed immersed $S^2$ in $\mathbb{R}^3$ with constant mean curvature $H = \text{const}$. Use the Codazzi equations and the holomorphic structure on $S^2$ (a complex line bundle on a sphere has a section that vanishes — Liouville) to show the traceless part of $b$, viewed as a section of a complex line bundle on $S^2$, must vanish — so the surface is totally umbilic, hence (Hilbert–Liebmann) the round sphere. **Why nonobvious:** This combines Codazzi, complex analysis (Hopf differential), and topological rigidity (a holomorphic section of a negative-degree line bundle on $S^2$ is zero).

3. **Gauss equation in arbitrary codimension.** For a submanifold $M^k \subset \mathbb{R}^n$ of any codimension, the Gauss equation becomes $R^\tau_{\;\alpha\gamma\beta}(M) = \langle\mathrm{II}(e_\tau, e_\gamma), \mathrm{II}(e_\alpha, e_\beta)\rangle - \langle\mathrm{II}(e_\tau, e_\beta), \mathrm{II}(e_\alpha, e_\gamma)\rangle$, with the second fundamental form $\mathrm{II}$ now vector-valued in the normal bundle. This formula governs the intrinsic curvature of submanifolds of Euclidean space — and more generally, of Riemannian manifolds. **Why nonobvious:** The codimension-$1$ case Frankel discusses generalises smoothly to arbitrary codimension, with the inner product on the normal bundle replacing the scalar product of $b$'s.

---

# Bridges

- **To the [[Thm - Theorema Egregium of Gauss|Theorema Egregium]].** The Gauss equation specialised to the $(1, 2, 1, 2)$ index on a $2$-surface gives $R_{1212} = \det b_{\alpha\beta}$, hence $K = R_{1212}/\det g$. This is the entire content of the Egregium — the Gauss equation is *the* technical input that makes Egregium possible. Without the Gauss equation, $K = \det b/\det g$ would appear extrinsic.

- **To the **Maurer–Cartan equations** of Lie groups ([[Riemannian Geometry I — Connections and Covariant Differentiation]]).** The Gauss + Codazzi equations are integrability conditions for an overdetermined PDE system, structurally similar to the Maurer–Cartan equations $d\theta + \tfrac{1}{2}[\theta, \theta] = 0$ for the canonical $1$-form on a Lie group. Both arise as "the structural equations whose solution gives a uniqueness theorem (Lie's first theorem; Bonnet's theorem)". The bridge is precise: Bonnet's theorem can be reformulated as a Frobenius-style integrability for a connection on the principal $\mathrm{SO}(3)$-bundle of orthonormal frames adapted to $M$.

- **To **Cartan's structural equations** ([[Riemannian Geometry I — Connections and Covariant Differentiation]]).** Choosing an adapted orthonormal frame $(e_1, e_2, N)$ along $M$, with dual coframe $(\theta^1, \theta^2, \theta^3)$ and connection $1$-forms $\omega^a_{\;b}$, Cartan's structural equations $d\theta^a + \omega^a_{\;b}\wedge\theta^b = 0$ (first structural) and $\Omega^a_{\;b} = d\omega^a_{\;b} + \omega^a_{\;c}\wedge\omega^c_{\;b}$ (second structural) become, when restricted to the tangent piece, the Gauss equation $\Omega^1_{\;2} = K\theta^1\wedge\theta^2$; when restricted to the off-diagonal piece, they become the Codazzi equation. This is the modern frame-theoretic reformulation and is the most efficient computational approach.

- **To **higher-codimension submanifold theory** and the **Ricci** + **normal** equations.** For $M^k \subset N^n$ (Riemannian, $k < n - 1$), the Gauss equation $R^M = R^N|_M + \mathrm{II}\wedge\mathrm{II}$ (schematically) is supplemented by the **Codazzi equation** for the normal-bundle connection of $\mathrm{II}$ and the **Ricci equation** for the curvature of the normal bundle. These three equations together — Gauss, Codazzi, Ricci — are the complete integrability conditions for a submanifold of any codimension in a Riemannian ambient. The codimension-$1$ case in $\mathbb{R}^3$ (Frankel's setting) has the Ricci equation collapse trivially because the normal bundle is a real line bundle with trivial curvature.

- **To **Einstein's equations** ([[General Relativity I — Einstein's Equations and Schwarzschild]]).** Einstein's equations in the ADM ($3+1$) formulation use the Gauss + Codazzi equations of a spacelike slice $\Sigma \subset M^4$ in spacetime. The **Hamiltonian constraint** $R(\Sigma) + (\mathrm{tr}\, K)^2 - |K|^2 = 16\pi T_{nn}$ (where $K$ is the extrinsic curvature of $\Sigma$) is the Gauss equation. The **momentum constraint** $\nabla_i(K^{ij} - g^{ij}\mathrm{tr}\, K) = 8\pi T_{nj}$ is the Codazzi equation. So Einstein's equations in canonical form are *exactly* the surface-theoretic Gauss + Codazzi equations applied to the spacetime slice.

---

# Unlocked by This

> [!tip] Bonnet's Fundamental Theorem of Surface Theory *(from §4.3)*
> The Gauss + Codazzi equations are not just necessary but also sufficient: any pair $(g_{\alpha\beta}, b_{\alpha\beta})$ satisfying them arises (locally, on simply connected domains, uniquely up to rigid motion) from an actual surface in $\mathbb{R}^3$. This makes the *moduli space of surfaces in $\mathbb{R}^3$* the space of solutions of the Gauss + Codazzi equations modulo rigid motion.

> [!tip] Hilbert's Theorem (No Complete $K = -1$ Surface in $\mathbb{R}^3$) *(from Surface Theory)*
> The Gauss + Codazzi equations imply that no *complete* surface in $\mathbb{R}^3$ can have $K \equiv -1$ everywhere. The proof uses asymptotic line coordinates and a careful PDE analysis. This is in stark contrast with the *abstract* hyperbolic plane $(\mathbb{H}^2, g_{\text{hyp}})$, which is a perfectly well-defined Riemannian manifold of constant curvature $-1$ but has no isometric embedding in $\mathbb{R}^3$. The pseudosphere ([[Ex - Gauss Curvature of the Pseudosphere is -1]]) is the largest piece that fits.

> [!tip] The ADM Formulation of General Relativity *(from General Relativity I)*
> The Gauss + Codazzi equations applied to a spacelike slice $\Sigma$ in a Lorentzian $4$-spacetime $M$ give the **constraint equations** of general relativity: the Hamiltonian constraint is the Gauss equation, the momentum constraint is the Codazzi equation. Combined with the evolution equations (the time-evolution of $g_{ij}$ and $K_{ij}$), they constitute the full ADM Hamiltonian formulation of Einstein's equations.

> [!tip] Higher-Codimension Gauss–Codazzi–Ricci Equations *(from Submanifold Theory)*
> For submanifolds of arbitrary codimension, the Gauss + Codazzi equations generalise to the **Gauss–Codazzi–Ricci** trio: Gauss for intrinsic curvature, Codazzi for the second fundamental form's covariant derivative, Ricci for the normal-bundle curvature. The full system constitutes the integrability conditions for an isometric immersion into any Riemannian ambient.
