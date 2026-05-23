---
type: definition
subject: geometric-mechanics
prereqs:
  - "Def - Symplectic Manifold"
  - "Def - Smooth Manifold"
  - "Def - Pullback of a Differential Form on a Manifold"
  - "Def - Closed and Exact Forms"
tags: [physics, geometric-mechanics, symplectic-geometry]
---

# Notation

$(M, \omega)$ is a symplectic manifold of dimension $2n$. $L \subset M$ is a smooth submanifold; $\iota_L : L \hookrightarrow M$ is the inclusion map; $\iota_L^*\omega$ is the pullback of $\omega$ to $L$. For a subspace $W \leq T_pM$, the **symplectic complement** is $W^\omega := \{v \in T_pM : \omega(v, w) = 0 \text{ for all } w \in W\}$, of dimension $2n - \dim W$.

---

# Axiom Motivation

Among submanifolds of a symplectic manifold, **Lagrangian submanifolds** are the most important — they are the symplectic-geometric analogue of "half-dimensional planes orthogonal to themselves", and the slogan **"everything is a Lagrangian"** is one of the central organizing principles of the subject. The motivating question is: **what is the right notion of "isotropy" for a submanifold of a symplectic manifold, and why is the half-dimensional case so special?**

Start by classifying submanifolds by how the symplectic form restricts. For a smooth submanifold $L \subset (M, \omega)$, the pullback $\iota_L^*\omega$ is a $2$-form on $L$, and there are four mutually exclusive cases at each point $p \in L$, depending on how the tangent space $T_pL$ sits inside $T_pM$:

- **Symplectic:** $\iota_L^*\omega$ is nondegenerate at $p$. Then $L$ is locally a sub-symplectic-manifold near $p$.
- **Isotropic:** $T_pL \subset (T_pL)^\omega$, i.e., $\omega|_{T_pL} = 0$. The symplectic form restricts to zero.
- **Coisotropic:** $T_pL \supset (T_pL)^\omega$. The symplectic complement of $T_pL$ is contained in $T_pL$.
- **Lagrangian:** both isotropic and coisotropic, i.e., $T_pL = (T_pL)^\omega$. The submanifold is "self-perpendicular" in the symplectic sense.

The dimensional structure tells us which cases can occur. If $\dim L = k$, then $\dim (T_pL)^\omega = 2n - k$. **Isotropic** ($T_pL \subset T_pL^\omega$) forces $k \leq 2n - k$, so $k \leq n$. **Coisotropic** ($T_pL \supset T_pL^\omega$) forces $k \geq n$. **Lagrangian** (both) forces $k = n$ — exactly half the dimension of $M$. So Lagrangian submanifolds are precisely the **half-dimensional isotropic submanifolds**, and they are *maximal* among isotropic submanifolds.

Why are Lagrangian submanifolds so important? Because of their universality: **most distinguished structures in symplectic geometry are or arise from Lagrangians**. To list a few:

1. **Configuration spaces inside cotangent bundles.** The zero section $Q \subset T^*Q$ is Lagrangian: its tangent space at $(q, 0)$ is $T_qQ \times \{0\}$, on which $\omega = dp \wedge dq$ restricts to zero (since $dp = 0$ on the zero section). Configuration space is the most basic Lagrangian, and the tautological 1-form $\theta = p\,dq$ vanishes on it.

2. **Graphs of closed 1-forms.** For a 1-form $\beta \in \Omega^1(Q)$, the graph $\{(q, \beta_q)\} \subset T^*Q$ is an $n$-dimensional submanifold. It is Lagrangian if and only if $d\beta = 0$ (closed). The proof: pull back the canonical $\omega = -d\theta$ along the section map $s_\beta : q \mapsto (q, \beta_q)$ — by the universal property of $\theta$, $s_\beta^*\theta = \beta$, so $s_\beta^*\omega = -d\beta$, and the pullback vanishes iff $d\beta = 0$.

3. **Cotangent fibres.** The fibre $T^*_qQ \subset T^*Q$ over any point $q \in Q$ is a Lagrangian submanifold. Its tangent space is the "purely momentum" direction $\{0\} \times T^*_qQ$, on which $\omega = dp \wedge dq$ restricts to zero (since $dq = 0$).

4. **Graphs of symplectomorphisms.** For a symplectomorphism $\varphi : (M_1, \omega_1) \to (M_2, \omega_2)$, the graph $\Gamma_\varphi = \{(x, \varphi(x))\} \subset M_1 \times M_2$ is a Lagrangian submanifold of $(M_1 \times M_2, \omega_2 - \omega_1)$. The proof is immediate: pull back $\omega_2 - \omega_1$ along the parametrization $x \mapsto (x, \varphi(x))$ — we get $\varphi^*\omega_2 - \omega_1 = 0$ because $\varphi^*\omega_2 = \omega_1$. **Symplectomorphisms are encoded as Lagrangian submanifolds**, and this is the basis of generating-function techniques in classical mechanics.

5. **Conormal bundles of submanifolds.** For a submanifold $S \subset Q$, the **conormal bundle** $N^*S = \{(q, \alpha) \in T^*Q : q \in S, \alpha|_{T_qS} = 0\}$ is a Lagrangian submanifold of $T^*Q$. This is the cotangent-bundle realization of "covectors that don't see the directions tangent to $S$", and it features prominently in microlocal analysis and propagation of singularities.

6. **Bohr–Sommerfeld tori in integrable systems.** For a completely integrable Hamiltonian system, the level sets of the involutive family of conserved quantities are Lagrangian tori. These are the **Arnold–Liouville tori**, and the **Bohr–Sommerfeld quantization condition** selects those whose action integrals are integer multiples of $h$.

7. **Lagrangian branes in mirror symmetry.** In string theory and mirror symmetry, Lagrangian submanifolds (with extra structure) play the role of **A-branes**, dual to the **B-branes** (coherent sheaves) on the mirror Calabi–Yau. The Fukaya category of Lagrangian submanifolds is the symplectic side of the mirror duality.

What if we *weaken* the isotropy condition, allowing $\omega|_L \neq 0$? We get symplectic submanifolds, which are sub-Hamiltonian-mechanics-arenas in their own right but are much less universal than Lagrangians. What if we *strengthen* by requiring "exact Lagrangian" (i.e., the pullback of the tautological 1-form $\theta$ is exact)? This gives a smaller class important in symplectic topology, but Lagrangian-ness alone is the structurally distinguished condition.

What if we *drop* the dimension requirement, allowing isotropic submanifolds of any dimension $\leq n$? We get **isotropic submanifolds**, which arise in degenerate or constrained problems. The Lagrangian case (dimension exactly $n$) is the maximal one and the one with the cleanest theory.

---

# The Definition

Let $(M, \omega)$ be a symplectic manifold of dimension $2n$. A submanifold $L \subset M$ is called:

- **Isotropic** if $\iota_L^*\omega = 0$, equivalently $T_pL \subset (T_pL)^\omega$ for every $p \in L$ — the symplectic form restricts to zero on $L$.
- **Coisotropic** if $T_pL \supset (T_pL)^\omega$ for every $p \in L$, equivalently the radical of $\iota_L^*\omega$ has dimension $\dim L - n$.
- **Symplectic** if $\iota_L^*\omega$ is nondegenerate (so $L$ is itself a symplectic manifold).
- **Lagrangian** if $L$ is isotropic and $\dim L = n$ — equivalently $T_pL = (T_pL)^\omega$ for every $p$ — i.e., $L$ is a **maximal isotropic submanifold**.

These conditions are at-each-point conditions; the manifold structure of $L$ ensures they extend smoothly.

A Lagrangian submanifold is automatically of dimension exactly half the dimension of $M$. **Equivalent characterizations** of Lagrangian:
- $L$ is isotropic ($\omega|_L = 0$) and $\dim L = n$;
- $L$ is coisotropic and $\dim L = n$;
- For every $p \in L$, $T_pL = (T_pL)^\omega$;
- The pullback of the form $\omega^n$ along the inclusion $\iota_L$ vanishes (in fact $\iota_L^*\omega^k = 0$ for all $k \geq 1$, since $\omega$ vanishes on $L$).

An **exact Lagrangian** in a cotangent bundle $T^*Q$ is a Lagrangian $L$ such that $\iota_L^*\theta$ is exact (rather than just closed), where $\theta = p\,dq$ is the tautological 1-form. Exact Lagrangians are an important refined class in symplectic topology.

---

# Categorical / Structural Definition

In the category of symplectic manifolds, Lagrangian submanifolds are the natural **objects of half dimension**, and a deep principle (the **symplectic creed**) holds that:

> "Every interesting symplectic-geometric structure is or arises from a Lagrangian submanifold."

This principle, due to Alan Weinstein, is operationalized by several specific constructions:

**Lagrangians as morphisms.** The graph of a symplectomorphism $\varphi : M_1 \to M_2$ is a Lagrangian in $(M_1 \times M_2, \omega_2 \ominus \omega_1)$, where $\omega_2 \ominus \omega_1 := \pi_2^*\omega_2 - \pi_1^*\omega_1$. So symplectomorphisms can be replaced by Lagrangian submanifolds of products. Composition of symplectomorphisms corresponds to a "Lagrangian composition" of graphs, defined via fibre product and projection.

**Lagrangian correspondences.** Generalizing graphs of symplectomorphisms, a **Lagrangian correspondence** from $(M_1, \omega_1)$ to $(M_2, \omega_2)$ is any Lagrangian submanifold $L \subset (M_1 \times M_2, \omega_2 \ominus \omega_1)$. These compose (with care for transversality) and form a **symplectic category** in Weinstein's sense, with objects symplectic manifolds and morphisms Lagrangian correspondences.

**Quantum states as Lagrangians (WKB).** In semiclassical quantum mechanics, a wave function $\psi(q) = a(q)e^{iS(q)/\hbar}$ in the WKB form corresponds to the Lagrangian submanifold $L_\psi = \{(q, dS(q))\} \subset T^*Q$. The Lagrangian is the geometric data; the amplitude and phase are extra data on it. This is the geometric heart of microlocal analysis.

**Moduli of Lagrangians.** The space of Lagrangian submanifolds of a fixed symplectic manifold (with appropriate equivalence relations) is itself a rich geometric object — the **Lagrangian Grassmannian** in the linear case, and various **Lagrangian moduli spaces** in the global case.

---

# Relate to Other Fields / Compression

A Lagrangian submanifold is the symplectic analogue of a **null subspace of a metric of signature $(n, n)$**: in pseudo-Riemannian geometry of signature $(n, n)$, the maximal totally isotropic subspaces have dimension $n$ and are exactly the analogues of Lagrangians (with the symmetric pairing of the metric replaced by the antisymmetric pairing of $\omega$). The two cases are dual: symmetric versus antisymmetric, real-valued isotropic versus null.

From the algebraic-geometry side, Lagrangian submanifolds of $(M, \omega)$ in the Kähler case (when $M$ has a compatible complex structure) include the **special Lagrangians** of Calabi–Yau geometry, which are calibrated submanifolds for the real-part-of-holomorphic-volume calibration. Special Lagrangians are the supersymmetric branes of string theory (A-branes), and their moduli spaces are smooth (the McLean theorem) — a key input to mirror symmetry.

**True name:** the true name of a Lagrangian submanifold is **"a generalized graph of a closed 1-form"** — operationally, in the cotangent-bundle setting, every Lagrangian close to the zero section is the graph of some closed 1-form $\beta$ (with $d\beta = 0$), and far from the zero section, more general Lagrangians arise as graphs of *multi-valued* closed 1-forms (cf. the Weinstein neighbourhood theorem, which says every Lagrangian has a tubular neighbourhood symplectomorphic to a neighbourhood of the zero section in its cotangent bundle).

---

# Examples / Corollaries

**Is an instance: the zero section $Z = \{(q, 0)\} \subset T^*Q$.** Its tangent space at $(q, 0)$ is $T_qQ$ embedded into $T_qQ \oplus T^*_qQ$ as the first factor. The symplectic form $\omega = dp \wedge dq$ restricts to zero (since $dp \equiv 0$ on $Z$), and $\dim Z = n = \dim Q$. So $Z$ is Lagrangian. The zero section is the geometric "configuration space sitting inside phase space".

**Is an instance: the graph of a closed 1-form.** For $\beta \in \Omega^1(Q)$ closed, the section $s_\beta : Q \to T^*Q$, $q \mapsto (q, \beta_q)$ embeds $Q$ as a submanifold. Its pullback of $\omega = -d\theta$ is $s_\beta^*\omega = -d(s_\beta^*\theta) = -d\beta = 0$, so the graph is Lagrangian. If $\beta = dS$ for a smooth function $S$ (exact), this is an **exact Lagrangian** representing the wavefront set of the WKB wavefunction $e^{iS/\hbar}$.

**Is an instance: cotangent fibres.** For any $q \in Q$, the fibre $T^*_qQ \subset T^*Q$ is an $n$-dimensional submanifold; its tangent space at $\alpha \in T^*_qQ$ is $\{0\} \times T_\alpha(T^*_qQ) = \{0\} \times T^*_qQ$, on which $\omega = dp\wedge dq$ vanishes (since $dq = 0$). So cotangent fibres are Lagrangian.

**Is an instance: graphs of symplectomorphisms.** For $\varphi : (M_1, \omega_1) \to (M_2, \omega_2)$ a symplectomorphism, the graph $\Gamma_\varphi = \{(x, \varphi(x))\} \subset M_1 \times M_2$ is a Lagrangian in $(M_1 \times M_2, \omega_2 - \omega_1)$. Verify: pull back $\omega_2 - \omega_1$ along the parametrization $\iota : M_1 \to M_1 \times M_2$, $x \mapsto (x, \varphi(x))$; we get $\iota^*(\omega_2 - \omega_1) = \varphi^*\omega_2 - \omega_1 = 0$. The dimension is $2n$ = half of $\dim(M_1 \times M_2) = 4n$. ✓

**Is an instance: the conormal bundle $N^*S$ of a submanifold $S \subset Q$.** Explicitly, $N^*S := \{(q, \alpha) \in T^*Q : q \in S, \alpha(v) = 0 \text{ for all } v \in T_qS\}$. Its dimension is $\dim S + (\dim Q - \dim S) = \dim Q = n$, and a computation shows $\omega|_{N^*S} = 0$. So conormal bundles are Lagrangian. Special cases: $N^*\{q_0\} = T^*_{q_0}Q$ (cotangent fibre); $N^*Q = Z$ (zero section).

**Is an instance: invariant tori of integrable systems.** For a Hamiltonian system on $(M^{2n}, \omega)$ with $n$ independent involutive integrals $f_1 = H, f_2, \dots, f_n$, the common level sets $\{f_i = c_i\}$ are $n$-dimensional submanifolds on which $\omega$ vanishes (because $X_{f_i}$ are tangent to the level set and Poisson-commute, so $\omega(X_{f_i}, X_{f_j}) = \{f_i, f_j\} = 0$). These are Lagrangian, and when compact connected they are tori (Arnold–Liouville). The dynamics on these tori is the quasi-periodic motion of [[Thm - Liouville's Theorem on Phase Space Volume|action-angle theory]].

**Is NOT an instance: a $(n-1)$-dimensional isotropic submanifold.** Such a submanifold is isotropic but not Lagrangian (it has the wrong dimension). It is **strictly isotropic**, and by Weinstein's "isotropic embedding theorem" any compact isotropic submanifold extends to a Lagrangian by adding a normal direction. Examples: a smooth curve in $(\mathbb{R}^4, \omega_0)$ on which $\omega$ restricts to zero is isotropic but not Lagrangian; it can be enlarged to a Lagrangian surface.

**Is NOT an instance: a symplectic submanifold.** $L = \{(q^1, p_1) : q^2 = p_2 = 0\} \subset (\mathbb{R}^4, \omega_0)$ is a $2$-dimensional submanifold on which $\omega = dp_1 \wedge dq^1 + dp_2 \wedge dq^2$ restricts to $dp_1 \wedge dq^1 \neq 0$. So $L$ is a *symplectic* submanifold, not Lagrangian. It is sub-Hamiltonian in its own right.

**Is NOT an instance: a non-closed graph.** If $\beta \in \Omega^1(Q)$ is a 1-form with $d\beta \neq 0$, the graph of $\beta$ in $T^*Q$ is an $n$-dimensional submanifold but $\omega$ restricts to $-d\beta \neq 0$, so it is *not* Lagrangian. The closedness of $\beta$ is exactly the Lagrangian condition.

**Corollary (Weinstein's tubular neighbourhood theorem).** Every Lagrangian submanifold $L$ of a symplectic manifold $(M, \omega)$ has a tubular neighbourhood symplectomorphic to a neighbourhood of the zero section in $T^*L$ (with its canonical symplectic structure). This is the symplectic analogue of the tubular neighbourhood theorem in differential topology, and it says **all Lagrangians look locally like a zero section in a cotangent bundle**.

**Corollary (dimension of Lagrangians).** Every Lagrangian submanifold of a $2n$-dimensional symplectic manifold has dimension exactly $n$.

**Corollary (Lagrangians are isotropic-and-coisotropic).** Lagrangian = isotropic + coisotropic. Equivalently, $T_pL = (T_pL)^\omega$ for every $p \in L$.

**Calibration check.** If you can do these three things, you have understood the definition. First, prove directly from the definition that the zero section of $T^*Q$ is Lagrangian. Second, verify that the graph of $\beta = dx + dy$ on $\mathbb{R}^2 \subset T^*\mathbb{R}^2$ is Lagrangian (it is closed), and that the graph of $\beta = x\,dy$ is *not* Lagrangian (compute $d\beta = dx \wedge dy \neq 0$). Third, show that the diagonal $\Delta \subset M \times M$ is Lagrangian for the symplectic structure $\omega_2 - \omega_1$ (where $\omega_i$ are the projections of $\omega$ to the two factors) — equivalently, the identity map is a symplectomorphism.

---

# Unlocked by This

> [!tip] Weinstein's Symplectic Creed and the Symplectic Category *(from Symplectic Geometry)*
> Alan Weinstein proposed in 1980 that the right category for symplectic geometry has **objects** symplectic manifolds and **morphisms** Lagrangian correspondences. A morphism from $(M_1, \omega_1)$ to $(M_2, \omega_2)$ is a Lagrangian submanifold $L \subset M_1 \times M_2$ for the symplectic form $\omega_2 \ominus \omega_1 = \pi_2^*\omega_2 - \pi_1^*\omega_1$. Composition is defined via fibre products. The slogan **"everything is a Lagrangian"** — symplectomorphisms become graphs, generating functions become exact Lagrangians, quantum states become Lagrangians with half-densities — organizes the entire field. The functor "quantization", in any of its forms, can be viewed as sending a Lagrangian correspondence to a quantum operator, with the obstructions captured by **Maslov classes**.

> [!tip] Fukaya Category and Mirror Symmetry *(from Symplectic Topology / String Theory)*
> The **Fukaya category** $\mathrm{Fuk}(M, \omega)$ of a symplectic manifold has objects Lagrangian submanifolds (with brane data) and morphisms the **Floer cochains** between them. It is an $A_\infty$-category, with structure constants given by counts of pseudo-holomorphic disks with boundary on the Lagrangians. **Homological mirror symmetry** (Kontsevich 1994) conjectures that for mirror pairs of Calabi–Yau manifolds $X, X^\vee$, the derived Fukaya category of $X$ is equivalent to the derived category of coherent sheaves on $X^\vee$ — a deep duality between the symplectic geometry of one space and the complex algebraic geometry of its mirror. This is one of the deepest known connections between symplectic and algebraic geometry.

> [!tip] Lagrangian Floer Homology and Intersection Numbers *(from Symplectic Topology)*
> Given two Lagrangian submanifolds $L_0, L_1$ of $(M, \omega)$, **Lagrangian Floer homology** $HF(L_0, L_1)$ is a graded vector space computed from a chain complex generated by intersection points $L_0 \cap L_1$, with differential given by counts of pseudo-holomorphic strips connecting them. When defined (the obstructions involve $\pi_2(M, L_i)$ and bubbling), $HF(L_0, L_1)$ is invariant under Hamiltonian isotopy of either Lagrangian and lower-bounds the number of intersection points $|L_0 \cap \varphi(L_1)|$ for any Hamiltonian $\varphi$. The **Arnold–Givental conjecture** specializes Arnold's conjecture to this Lagrangian setting and is proved in many cases via Lagrangian Floer theory.
