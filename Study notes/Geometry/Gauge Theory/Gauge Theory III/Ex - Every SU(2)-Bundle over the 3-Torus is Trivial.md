---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds"
  - "Thm - Generic Sections are Transverse to the Zero Section"
  - "Thm - Sections of a Principal Bundle and Triviality"
  - "Def - Associated Bundle"
  - "Def - Principal G-Bundle"
  - "Def - Complex Vector Bundle and Hermitian Structure"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $T^3 = \mathbb{R}^3 / \mathbb{Z}^3$ be the three-dimensional torus, with the standard coordinates $(x_1, x_2, x_3) \bmod 1$, and let $\pi\colon P \to T^3$ be a principal $SU(2)$-bundle. Prove that $P$ is trivial, that is, $P \cong T^3 \times SU(2)$ as principal $SU(2)$-bundles.

Two things are asked, and the exercise is to see that they are the same argument seen from two sides.

1. **Run the generic-section argument concretely on $T^3$.** Form the associated complex rank-two bundle $E = P \times_{SU(2)} \mathbb{C}^2$, regard it as a real vector bundle of rank $4$ over the compact three-manifold $T^3$, and show that because the rank strictly exceeds the base dimension a generic section is nowhere vanishing.

2. **Give the cocycle-free identification $P \cong S(E)$.** Show that $P$ is isomorphic, as a principal $SU(2)$-bundle, to the unit sphere bundle $S(E) \subset E$ — without ever choosing a trivialising cover or transition functions — by using that $SU(2)$ acts simply transitively on the unit sphere of $\mathbb{C}^2$. A nowhere-vanishing section of $E$, normalised, is then a global section of $P$, and a principal bundle with a global section is trivial.

The dimension inequality $\operatorname{rank}_{\mathbb{R}} E = 4 > 3 = \dim T^3$ is the whole of the topological content; everything else is bookkeeping that turns "$E$ has a unit section" into "$P$ is trivial".

**Recall:**

The objects in play are a principal $SU(2)$-bundle, its associated $\mathbb{C}^2$-bundle, the unit sphere bundle of a Hermitian bundle, the generic-section transversality theorem, and the section–triviality dictionary for principal bundles.

![[Def - Principal G-Bundle#The Definition]]

A **principal $G$-bundle** $\pi\colon P \to M$ is a fibre bundle carrying a smooth free right $G$-action that preserves the fibres and is transitive on each of them, together with $G$-equivariant local trivialisations $\psi_U\colon \pi^{-1}(U) \to U \times G$ satisfying $\psi_U(p \cdot g) = \psi_U(p)\cdot g$. Here $G = SU(2) = \{A \in \mathrm{GL}_2(\mathbb{C}) : A^* A = 1,\ \det A = 1\}$, and the action is written $R_g(p) = p \cdot g$ on the right, following the series convention.

![[Def - Associated Bundle#The Definition]]

Given $P$ and a representation $\rho\colon G \to \mathrm{GL}(V)$, the **associated bundle** is the quotient
$$E = P \times_\rho V := (P \times V)/G, \qquad (p, v) \cdot g = (p\cdot g,\ \rho(g)^{-1} v),$$
whose class of $(p, v)$ is written $[p, v]$, so that $[p \cdot g,\ v] = [p,\ \rho(g)\, v]$ for all $g \in G$. It is a vector bundle over $M$ with fibre $V$; a local section $s$ of $P$ over $U$ gives the trivialisation $U \times V \to E|_U$, $(m, v) \mapsto [s(m), v]$. For the present problem $V = \mathbb{C}^2$ and $\rho$ is the **defining representation** $\rho(A) v = A v$ (matrix times column vector), which is unitary because $SU(2) \subset U(2)$.

![[Def - Complex Vector Bundle and Hermitian Structure#The Definition]]

A **Hermitian structure** on a complex vector bundle $E$ is a smooth field of Hermitian inner products $\langle\cdot,\cdot\rangle_m$ on the fibres $E_m$; it gives each fibre a norm $|v| = \langle v, v\rangle^{1/2}$ and hence a **unit sphere bundle** $S(E) = \{ e \in E : |e| = 1\}$, a fibre bundle over $M$ with fibre the unit sphere $S^{2\,\mathrm{rk}_{\mathbb{C}} E - 1}$. On $E = P \times_\rho \mathbb{C}^2$ the standard Hermitian product of $\mathbb{C}^2$ descends, $\langle [p, v], [p, w]\rangle := \langle v, w\rangle_{\mathbb{C}^2}$, and this is well defined precisely because $\rho$ is unitary: replacing the representative $(p, v)$ by $(p\cdot g,\ \rho(g)^{-1} v)$ leaves $\langle \rho(g)^{-1} v,\ \rho(g)^{-1} w\rangle_{\mathbb{C}^2} = \langle v, w\rangle_{\mathbb{C}^2}$ unchanged.

![[Thm - Generic Sections are Transverse to the Zero Section#Statement]]

The **generic-section theorem** states: for a real vector bundle $E \to M$ of rank $r$ over a compact manifold $M$ of dimension $m$, there exist finitely many sections $s_1, \dots, s_N$ spanning every fibre, and for almost every $a = (a_1, \dots, a_N) \in \mathbb{R}^N$ the section $s_a = \sum_i a_i s_i$ is transverse to the zero section (its vertical derivative $D_x s_a\colon T_x M \to E_x$ is surjective at every zero $x$); consequently, **if $r > m$ then $E$ admits a nowhere-vanishing section**.

![[Thm - Sections of a Principal Bundle and Triviality#Statement]]

The **section–triviality theorem** states: a principal $G$-bundle $P \to M$ is trivial if and only if it admits a global smooth section $\sigma\colon M \to P$; explicitly, a section $\sigma$ gives the equivariant trivialisation $P \to M \times G$, $p \mapsto (\pi(p),\ g(p))$ where $g(p)$ is the unique group element with $p = \sigma(\pi(p))\cdot g(p)$.

![[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds#Statement]]

This exercise is exactly part (A) of the classification theorem, [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds]] — *every principal $SU(2)$-bundle over a compact manifold of dimension at most $3$ is trivial* — carried out in full for the concrete base $M = T^3$, together with the sphere-bundle lemma that its proof of (A) uses.

---

# Convergent Strategy

**Problem class.** This is a *triviality* problem: show that a bundle carrying no visible extra data is isomorphic to the product bundle. The universal move for a principal bundle is to produce a *global section*, because for principal bundles "trivial" and "sectioned" are literally the same statement ([[Thm - Sections of a Principal Bundle and Triviality|the section–triviality theorem]]). The whole difficulty is therefore displaced onto: *where does a global section of $P$ come from?* A principal $SU(2)$-bundle over a manifold that is not a Lie group has no algebraically obvious section, so the section must be manufactured, and it is manufactured out of a section of an associated *vector* bundle, where sections are cheap (they form a vector space and can be perturbed).

**Assumption pattern.** The one hypothesis that does all the work is the numerical one: $\dim T^3 = 3$ is strictly less than $\operatorname{rank}_{\mathbb{R}}\big(P \times_{SU(2)} \mathbb{C}^2\big) = 4$. The recognisable trigger is "*I want a nowhere-vanishing section of a vector bundle, and the rank exceeds the base dimension*". Whenever that inequality holds over a compact base, the generic-section theorem converts it into an actual nowhere-vanishing section: a transverse section can only vanish on a set of dimension $\dim M - \operatorname{rank} E < 0$, i.e. nowhere. The complementary fact, that over a *four*-manifold the same construction produces isolated signed zeros counted by the Chern number $k(P)$, is precisely why the classification is nontrivial in dimension $4$ and trivial below it.

**Theorem routing.** The route is a short chain. Form $E = P \times_{\rho} \mathbb{C}^2$ with $\rho$ the defining representation ([[Def - Associated Bundle|associated bundle]]); equip it with the descended Hermitian structure. Apply [[Thm - Generic Sections are Transverse to the Zero Section|the generic-section theorem]] with $r = 4 > 3 = m$ to get a nowhere-vanishing section $s$; normalise to a unit section $u = s/|s| \in \Gamma(S(E))$. Identify $S(E) \cong P$ as principal $SU(2)$-bundles ([[Def - Free, Transitive, Effective, and Proper Group Actions|simple transitivity]] of $SU(2)$ on $S^3 \subset \mathbb{C}^2$). Read $u$ as a global section of $P$ and invoke [[Thm - Sections of a Principal Bundle and Triviality|the section–triviality theorem]] to conclude $P$ is trivial.

**Key decision point.** The single non-obvious step is *passing from $P$ to $E$ and back*. There is no canonical section of $P$ to perturb — perturbing sections requires a linear (or at least affine) structure on the space of sections, which the fibres $SU(2)$ of $P$ do not have, but which the fibres $\mathbb{C}^2$ of $E$ do. So one leaves the principal bundle for its associated vector bundle, does the genuinely topological work there (transversality), and returns via the identification $P \cong S(E)$. Recognising that this identification is available *for free* — that $SU(2)$ acting on the unit sphere of its defining representation is a copy of $SU(2)$ acting on itself by right translation — is what makes the return trip legitimate and coordinate-free. Miss it, and one is tempted to trivialise $E$ instead and then argue about reductions of the structure group, a longer and error-prone route.

---

# Legal Operations Used

These are the operations of [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles#Legal Operations|the chapter's Legal Operations]] as they apply here (referred to descriptively, since the topic page's numbering is fixed when it is assembled).

1. **Pass to an associated vector bundle to gain a linear structure.** Replace the principal bundle $P$, whose fibres $SU(2)$ carry no vector-space structure, by $E = P \times_{\rho}\mathbb{C}^2$, whose fibres are $\mathbb{C}^2$; sections of $E$ can now be added and scaled, which is what genericity arguments need.

2. **Descend a fibre inner product through a unitary representation.** Because $\rho$ is unitary, the standard Hermitian product of $\mathbb{C}^2$ is $G$-invariant and descends to a Hermitian structure on $E$, giving a well-defined unit sphere bundle $S(E)$ and a normalisation $s \mapsto s/|s|$.

3. **Count dimensions to force a section to be nowhere-vanishing.** Apply the generic-section theorem with $\operatorname{rank}_{\mathbb{R}} E = 4 > 3 = \dim T^3$; a transverse section has zero set of expected dimension $3 - 4 < 0$, hence empty.

4. **Identify a principal bundle with the unit sphere bundle of its defining associated bundle.** Use that $SU(2)$ acts simply transitively on $S^3 = \{v \in \mathbb{C}^2 : |v| = 1\}$ to build a $G$-equivariant fibrewise diffeomorphism $\Phi\colon P \to S(E)$, $p \mapsto [p, e_1]$, with no reference to trivialising charts.

5. **Convert a nowhere-vanishing vector-bundle section into a global principal-bundle section.** Transport the unit section $u \in \Gamma(S(E))$ across $\Phi^{-1}$ to a global section $\sigma$ of $P$.

6. **Read off triviality from a global section.** Invoke the section–triviality theorem: a principal $G$-bundle with a global section is isomorphic to the product bundle.

---

# Hints

> [!note]- Hint 1
> A principal $SU(2)$-bundle is trivial as soon as it has a *global section* — this is the section–triviality theorem, and it is the only thing you ultimately have to produce. But the fibres of $P$ are copies of $SU(2)$, which you cannot add or average. Is there a bundle associated to $P$ whose fibres you *can* add in, where sections are plentiful?

> [!note]- Hint 2
> Form $E = P \times_{SU(2)} \mathbb{C}^2$ using the defining representation. As a *real* vector bundle it has rank $4$. The base $T^3$ has dimension $3$. When the rank of a real vector bundle over a compact manifold exceeds the dimension of the base, a *generic* section misses the zero section entirely — recall why, in terms of the expected dimension of the zero set.

> [!note]- Hint 3
> You now have a nowhere-vanishing section $s$ of $E$; normalise it with the Hermitian structure to $u = s/|s|$, a section of the unit sphere bundle $S(E)$. The last move is to recognise $S(E)$ as $P$ in disguise. Consider the map $p \mapsto [p, e_1]$ from $P$ to $S(E)$, where $e_1 = (1, 0)^{\top} \in \mathbb{C}^2$. Why is it a bijection on each fibre? What does $SU(2)$ do to the unit vector $e_1$?

> [!note]- Hint 4
> Check that $A \mapsto A e_1$ is a bijection from $SU(2)$ onto $S^3 \subset \mathbb{C}^2$: surjectivity because any unit vector can be completed to a unitary basis with determinant $1$, injectivity because a matrix in $SU(2)$ fixing $e_1$ must be the identity. This makes $\Phi(p) = [p, e_1]$ a $G$-equivariant fibre diffeomorphism $P \to S(E)$; carry $u$ back through $\Phi^{-1}$ to a global section of $P$, and finish with the section–triviality theorem.

---

# Solution

The plan is a round trip. We leave the principal bundle $P$ for the associated complex plane bundle $E = P\times_{SU(2)}\mathbb C^2$, because $E$'s fibres are linear and sections of $E$ can be perturbed; there the dimension inequality $\operatorname{rank}_{\mathbb R}E = 4 > 3 = \dim T^3$ produces, via genericity, a nowhere-vanishing section. We normalise it to a unit section, and we return to $P$ through the coordinate-free identification $P\cong S(E)$ that comes from $SU(2)$ acting simply transitively on the unit sphere of $\mathbb C^2$. A global section of $P$ then forces $P$ to be trivial.

**Step 1: Build the associated bundle $E$ and its Hermitian structure.**

We attach to $P$ the associated bundle $E = P \times_\rho \mathbb{C}^2$ of the defining representation, and give it the Hermitian structure descended from $\mathbb{C}^2$. As a real vector bundle $E$ has rank $4$.

> [!note]- Derivation
> Let $\rho\colon SU(2) \to \mathrm{GL}(\mathbb{C}^2)$ be the defining representation $\rho(A) v = A v$. Because $SU(2) \subset U(2)$, every $\rho(A)$ is a unitary matrix: $\langle A v, A w\rangle_{\mathbb{C}^2} = v^* A^* A w = v^* w = \langle v, w\rangle_{\mathbb{C}^2}$ (using $A^* A = 1$, the defining relation of $SU(2)$). Form
> $$E = P \times_\rho \mathbb{C}^2 = (P \times \mathbb{C}^2)/SU(2), \qquad [p\cdot g,\ v] = [p,\ \rho(g)\, v],$$
> which by the [[Def - Associated Bundle|associated-bundle construction]] is a complex vector bundle of rank $2$ over $T^3$, hence a **real** vector bundle of rank $\operatorname{rank}_{\mathbb{R}} E = 2 \cdot 2 = 4$.
>
> Define $\langle [p, v],\ [p, w]\rangle_E := \langle v, w\rangle_{\mathbb{C}^2}$. This is independent of the representative: any other representative of the same two classes over the same point has the form $([p\cdot g, \rho(g)^{-1} v], [p \cdot g, \rho(g)^{-1} w])$ for a single $g$ (the fibre of $P$ over a point is a single $SU(2)$-orbit, so the $P$-entries of the two classes may be aligned by the same $g$), and
> $$\langle \rho(g)^{-1} v,\ \rho(g)^{-1} w\rangle_{\mathbb{C}^2} = \langle v, w\rangle_{\mathbb{C}^2} \qquad (\text{since } \rho(g)^{-1} \text{ is unitary}).$$
> Smoothness in the base point follows by evaluating in a local trivialisation $(m, v) \mapsto [s(m), v]$ coming from a local section $s$ of $P$, where $\langle\cdot,\cdot\rangle_E$ becomes the constant standard product. Thus $E$ is a Hermitian bundle, and its **unit sphere bundle** is
> $$S(E) = \{ e \in E : |e|_E = 1\}, \qquad |e|_E = \langle e, e\rangle_E^{1/2},$$
> a fibre bundle over $T^3$ with fibre the unit sphere $S^3 \subset \mathbb{C}^2$.

**Step 2: A generic section of $E$ is nowhere vanishing.**

Because $T^3$ is compact and $\operatorname{rank}_{\mathbb{R}} E = 4$ exceeds $\dim T^3 = 3$, the generic-section theorem produces a section $s \in \Gamma(E)$ with $s(m) \neq 0$ for every $m \in T^3$.

> [!note]- Derivation
> Apply [[Thm - Generic Sections are Transverse to the Zero Section|the generic-section theorem]] to the real vector bundle $E \to T^3$, with $m = \dim T^3 = 3$ and $r = \operatorname{rank}_{\mathbb{R}} E = 4$. Its hypothesis — a compact base — holds because $T^3 = \mathbb{R}^3/\mathbb{Z}^3$ is compact.
>
> Concretely, the theorem first supplies finitely many sections $s_1, \dots, s_N \in \Gamma(E)$ that span each fibre $E_m$: choose a finite atlas $\{U_\alpha\}$ of $T^3$ over which $E$ is trivial (possible since $T^3$ is compact), a local frame $e^\alpha_1, \dots, e^\alpha_4$ of $E$ on each $U_\alpha$, and a partition of unity $\{\chi_\alpha\}$ subordinate to $\{U_\alpha\}$; the products $\chi_\alpha e^\alpha_i$, extended by zero, are global sections whose values span $E_m$ at each $m$ (some $\chi_\alpha(m) > 0$, and there the four sections $\chi_\alpha e^\alpha_i$ are a basis). Relabel these finitely many sections $s_1, \dots, s_N$.
>
> For $a = (a_1, \dots, a_N) \in \mathbb{R}^N$ put $s_a = \sum_{i=1}^N a_i s_i$. The theorem asserts that for almost every $a$ the section $s_a$ is **transverse to the zero section**: at every zero $x$ of $s_a$ the vertical derivative $D_x s_a\colon T_x T^3 \to E_x$ is surjective. But
> $$\dim T_x T^3 = 3 < 4 = \dim_{\mathbb{R}} E_x,$$
> so no linear map $T_x T^3 \to E_x$ can be surjective. Hence transversality is vacuously possible only when there are **no zeros at all**: for a generic $a$, the transverse section $s_a$ has empty zero set. Equivalently, by the regular-value theorem the zero set of a transverse section is a submanifold of dimension $m - r = 3 - 4 = -1$, i.e. empty. Fix one such $a$ and set $s := s_a \in \Gamma(E)$; then $s(m) \neq 0$ for all $m \in T^3$.

**Step 3: Normalise to a section of the unit sphere bundle.**

Dividing $s$ by its norm gives a smooth unit section $u = s/|s|_E \in \Gamma(S(E))$.

> [!note]- Derivation
> Since $s(m) \neq 0$ everywhere (Step 2) and $|s|_E\colon T^3 \to \mathbb{R}$ is smooth and strictly positive (the Hermitian norm of Step 1 is smooth and vanishes only at the zero vector), the section
> $$u(m) := \frac{s(m)}{|s(m)|_E} \in E_m$$
> is smooth and satisfies $|u(m)|_E = 1$ for all $m$. Thus $u$ is a global smooth section of the unit sphere bundle $S(E)$.

**Step 4: Identify $P$ with $S(E)$ as principal $SU(2)$-bundles, without cocycles.**

The map $\Phi\colon P \to S(E)$, $\Phi(p) = [p,\, e_1]$ with $e_1 = (1,0)^{\top}$, is a $G$-equivariant diffeomorphism of principal $SU(2)$-bundles, because $SU(2)$ acts simply transitively on the unit sphere $S^3 \subset \mathbb{C}^2$.

> [!note]- Derivation
> **Simple transitivity of $SU(2)$ on $S^3$.** Consider the orbit map of the unit vector $e_1 = (1,0)^{\top}$,
> $$\mu\colon SU(2) \to \mathbb{C}^2, \qquad \mu(A) = A\, e_1 = \text{(first column of } A).$$
> Its image lies in $S^3 = \{v : |v| = 1\}$ because $A$ is unitary, so $|A e_1| = |e_1| = 1$.
> - *Surjectivity onto $S^3$.* Let $v \in \mathbb{C}^2$ with $|v| = 1$. Write $v = (v_1, v_2)^{\top}$ and set $w = (-\overline{v_2},\ \overline{v_1})^{\top}$. Then $|w|^2 = |v_2|^2 + |v_1|^2 = 1$, and with the convention $\langle a, b\rangle_{\mathbb{C}^2} = \sum_i \overline{a_i} b_i$,
> $$\langle w, v\rangle_{\mathbb{C}^2} = \overline{(-\overline{v_2})}\,v_1 + \overline{(\overline{v_1})}\,v_2 = -v_2 v_1 + v_1 v_2 = 0,$$
> so $(v, w)$ is an orthonormal basis. The matrix $A = [\,v \ \ w\,]$ (columns $v$ and $w$) is unitary, and $\det A = v_1 \overline{v_1} + v_2 \overline{v_2} = |v_1|^2 + |v_2|^2 = 1$, so $A \in SU(2)$ and $A e_1 = v$.
> - *Injectivity, i.e. trivial stabiliser.* Suppose $A \in SU(2)$ fixes $e_1$: $A e_1 = e_1$. Then the first column of $A$ is $e_1$, so $A = \begin{pmatrix} 1 & b \\ 0 & d\end{pmatrix}$ for some $b, d \in \mathbb{C}$. Unitarity of the columns forces the second column $(b, d)^{\top}$ to be orthogonal to the first column $(1,0)^{\top}$, giving $b = \overline{1}\,b + \overline{0}\,d = \langle e_1, (b,d)^{\top}\rangle = 0$; and to have unit norm, $|d| = 1$; and $\det A = d = 1$. Hence $A = 1$. Therefore two elements of $SU(2)$ with the same value on $e_1$ differ by an element fixing $e_1$, which is the identity: $\mu$ is injective.
>
> Thus $\mu\colon SU(2) \to S^3$ is a smooth bijection; it is a diffeomorphism because it is the orbit map of a smooth transitive action of a compact Lie group on a manifold of the same dimension $3$, so it is an immersion (trivial stabiliser makes $d_e\mu$ injective, hence bijective by dimension) and a bijective immersion from a compact source is a diffeomorphism. In particular $SU(2)$ acts **simply transitively** on $S^3$.
>
> **The map $\Phi$ and its equivariance.** Define $\Phi\colon P \to S(E)$ by $\Phi(p) = [p, e_1]$. It is smooth (composite of $p \mapsto (p, e_1)$ with the quotient map $P \times \mathbb{C}^2 \to E$) and lands in $S(E)$ since $|[p, e_1]|_E = |e_1|_{\mathbb{C}^2} = 1$. It covers the identity of $T^3$: $\Phi(p)$ lies in the fibre $E_{\pi(p)}$.
>
> *Fibrewise bijectivity.* Fix $m \in T^3$ and any $p_0 \in P_m$. Every $p \in P_m$ is $p = p_0 \cdot g$ for a unique $g \in SU(2)$ (the fibre is a single free transitive orbit), and
> $$\Phi(p_0 \cdot g) = [p_0 \cdot g,\ e_1] = [p_0,\ \rho(g)\, e_1] = [p_0,\ g\, e_1] \qquad (\text{associated-bundle relation, } \rho = \text{defining}).$$
> As $g$ ranges over $SU(2)$, $g\, e_1 = \mu(g)$ ranges bijectively over $S^3$ (simple transitivity), and $v \mapsto [p_0, v]$ is a bijection $S^3 \to S(E)_m$ (the map $v \mapsto [p_0, v]$ identifies $\mathbb{C}^2 \xrightarrow{\sim} E_m$ and restricts to unit spheres). Hence $\Phi$ maps $P_m$ bijectively onto $S(E)_m$.
>
> *Principal structure on $S(E)$ and equivariance.* Give $S(E)$ the right $SU(2)$-action that makes $\Phi$ equivariant: for $q = [p_0, g\,e_1] \in S(E)_m$ and $h \in SU(2)$, set $q \cdot h := [p_0,\ (gh)\, e_1]$. This is well defined (independent of the choice of $p_0$ and of the representative $g$, by the same orbit computation) and is free and transitive on each fibre because right multiplication is free and transitive on $SU(2)$. With this action $\Phi(p \cdot h) = [p\cdot h, e_1] = [p, \rho(h) e_1] = [p, h e_1]$, and writing $p = p_0 g$ this is $[p_0, (gh)e_1] = \Phi(p_0 g)\cdot h = \Phi(p)\cdot h$. So $\Phi$ is $G$-equivariant, fibrewise bijective, smooth, and covers the identity; a $G$-equivariant smooth bundle map that is a fibrewise bijection between principal $G$-bundles is an isomorphism (its inverse is smooth by equivariance and the local trivialisations). Therefore $P \cong S(E)$ as principal $SU(2)$-bundles.

**Step 5: Conclude that $P$ is trivial.**

The unit section $u \in \Gamma(S(E))$ transports across $\Phi^{-1}$ to a global section of $P$; by the section–triviality theorem, $P$ is trivial.

> [!note]- Derivation
> By Step 4, $\Phi\colon P \to S(E)$ is an isomorphism of principal bundles, so $\sigma := \Phi^{-1} \circ u\colon T^3 \to P$ is a smooth global section: indeed $u\colon T^3 \to S(E)$ is a section (Step 3) and $\Phi^{-1}$ is a bundle isomorphism over the identity, so $\pi \circ \sigma = \pi_{S(E)} \circ u = \mathrm{id}_{T^3}$.
>
> Now invoke [[Thm - Sections of a Principal Bundle and Triviality|the section–triviality theorem]]: a principal $G$-bundle that admits a global section is trivial. Explicitly, $\sigma$ gives the trivialisation
> $$P \to T^3 \times SU(2), \qquad p \mapsto \big(\pi(p),\ g(p)\big),$$
> where $g(p) \in SU(2)$ is the unique element with $p = \sigma(\pi(p)) \cdot g(p)$ (existence and uniqueness by freeness and transitivity of the action on each fibre; smoothness of $g$ from the local trivialisations). Hence $P \cong T^3 \times SU(2)$.

> [!note]- Complete formal solution
> **Claim.** Every principal $SU(2)$-bundle $\pi\colon P \to T^3$ over the three-torus is trivial.
>
> Let $\rho\colon SU(2) \to \mathrm{GL}(\mathbb{C}^2)$ be the defining representation and $E = P \times_\rho \mathbb{C}^2$ the associated bundle, a complex rank-two, hence real rank-four, vector bundle over $T^3$. Since $SU(2) \subset U(2)$, $\rho$ is unitary, so the standard Hermitian product of $\mathbb{C}^2$ descends to a Hermitian structure $\langle[p,v],[p,w]\rangle_E = \langle v, w\rangle_{\mathbb{C}^2}$ on $E$, with unit sphere bundle $S(E)$ (fibre $S^3 \subset \mathbb{C}^2$).
>
> $T^3$ is compact and $\operatorname{rank}_{\mathbb{R}} E = 4 > 3 = \dim T^3$. By the generic-section theorem there are finitely many sections spanning every fibre, and for almost every real combination $s_a$ the section is transverse to the zero section; at any zero the vertical derivative $D_x s_a\colon T_x T^3 \to E_x$ would have to be surjective, impossible since $3 < 4$. Hence a generic $s := s_a$ has no zeros, and $u := s/|s|_E \in \Gamma(S(E))$ is a global unit section.
>
> The orbit map $\mu(A) = A e_1$ ($e_1 = (1,0)^{\top}$) is a bijection $SU(2) \to S^3$: given a unit vector $v = (v_1,v_2)^{\top}$, the matrix with columns $v$ and $(-\overline{v_2}, \overline{v_1})^{\top}$ is in $SU(2)$ and sends $e_1$ to $v$ (surjectivity); a matrix in $SU(2)$ fixing $e_1$ has first column $e_1$, and unitarity with $\det = 1$ force it to be the identity (injectivity). Being the orbit map of a transitive smooth action of a compact Lie group with trivial stabiliser, between $3$-manifolds, $\mu$ is a diffeomorphism; so $SU(2)$ acts simply transitively on $S^3$. Consequently $\Phi\colon P \to S(E)$, $\Phi(p) = [p, e_1]$, is a $G$-equivariant fibrewise bijection: for $p = p_0 g$, $\Phi(p) = [p_0, g e_1]$, and $g \mapsto g e_1$ is a fibrewise bijection while $v \mapsto [p_0, v]$ identifies unit spheres; with the induced right action $[p_0, g e_1]\cdot h = [p_0, (gh) e_1]$ on $S(E)$, $\Phi$ is equivariant. A smooth equivariant fibrewise-bijective bundle map of principal bundles over the identity is an isomorphism, so $P \cong S(E)$.
>
> Therefore $\sigma := \Phi^{-1} \circ u$ is a global section of $P$, and by the section–triviality theorem $P \cong T^3 \times SU(2)$. $\blacksquare$

> [!warning] Illegal but tempting route: "$H^4(T^3;\mathbb{Z}) = 0$, so $c_2(P) = 0$, so $P$ is trivial."
> One is tempted to argue that an $SU(2)$-bundle is classified by its second Chern class $c_2(P) \in H^4(\text{base};\mathbb{Z})$, and since $T^3$ is a three-manifold with $H^4(T^3;\mathbb{Z}) = 0$ there is no room for an obstruction. This conclusion is *correct in outcome but not a proof here*, for two reasons. First, over a manifold of dimension $\le 3$ there is no clutching construction and no four-dimensional invariant to speak of — the Chern *number* $k(P) = \int c_2$ is a device special to closed four-manifolds, not something one can attach to $T^3$. Second, even over a four-manifold the statement "$c_2$ is a *complete* invariant" (bundles with equal Chern number are isomorphic) requires $\pi_3(S^3) \cong \mathbb{Z}$, the Hopf degree theorem in dimension three, which the series records as a scope remark and does not prove; vanishing of $c_2$ is only known to control triviality once completeness is granted. The honest argument does not invoke a complete invariant at all: it produces a section by transversality. What *would* rescue the cohomological heuristic is the completeness statement together with a genuine cohomological classification of $SU(2)$-bundles, neither of which is available in this chapter — so the dimension count of Step 2 is doing the real work.

> [!note]- Independent sanity check: why the argument stops at dimension $3$
> Run the same construction over a *four*-manifold $X$ and watch it fail exactly where it should. Now $\operatorname{rank}_{\mathbb{R}} E = 4 = \dim X$, so a transverse section $s_a$ has zero set of expected dimension $4 - 4 = 0$: a *finite set of isolated nondegenerate zeros*, each carrying a sign $\varepsilon(x) = \operatorname{sign}\det D_x s_a$. Their signed count is not forced to vanish; it equals the Chern number $k(P) = \int_X c_2(P)$. So over $X^4$ one obtains a section of $P$ only away from finitely many points — precisely the clutching picture behind [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds|the four-manifold classification]], where $SU(2)$-bundles are genuinely distinguished by $k(P)$. The triviality we proved is thus sharply a below-the-critical-dimension phenomenon: it holds because $3 < 4$ and would be false at $4 = 4$.

---

# Key Takeaways

**To trivialise a principal bundle, manufacture a global section; to manufacture a section, pass to an associated vector bundle where sections are linear.** The section–triviality theorem collapses "is $P$ trivial?" into "does $P$ have a global section?", but the fibres of a principal bundle carry no linear structure, so there is nothing to perturb and no partition-of-unity averaging available directly on $P$. The universal fix is to associate a vector bundle $E = P \times_\rho V$: its sections form a $C^\infty(M)$-module, can be built locally and glued with a partition of unity, and can be perturbed to generic position. One does the topology on $E$ and transports the conclusion back to $P$. The trigger for this move is any triviality-or-section question about a principal bundle whose group has a faithful (here defining) representation; the associated bundle is the vehicle that turns representation-theoretic freedom into geometric sections. This is the same reflex that identifies gauge fields with connections on associated bundles and gauge transformations with sections of $\operatorname{Ad} P$ later in the series.

**When the real rank of a vector bundle exceeds the base dimension, a generic section is nowhere vanishing — and the strict inequality is the entire content.** The expected dimension of the zero set of a transverse section of a rank-$r$ bundle over an $m$-manifold is $m - r$; when $m - r < 0$ the transverse zero set is empty, so a generic section is a nowhere-vanishing section. This is the diagnostic to reach for whenever a problem asks for a non-vanishing section, a frame, a reduction of the structure group, or a splitting: compare $r$ with $m$. Here $r = 4$ (real rank of a $\mathbb{C}^2$-bundle) against $m = 3$ (the torus), and the single inequality $4 > 3$ decides the whole classification below dimension four. The complementary regime $r = m$ produces isolated signed zeros whose count is a characteristic number, and $r < m$ produces genuine higher-dimensional zero loci; recognising which regime one is in tells you immediately whether to expect triviality, an integer invariant, or a submanifold of zeros. The lesson transfers verbatim to the hairy-ball theorem ($r = m$ on $TS^{2n}$, forced nonzero count $\chi = 2$) and to the degree of a line bundle over a surface ($r = 2 = m$, signed zeros summing to the degree).

**A group acting simply transitively on a fibre lets you identify an associated fibre bundle with the principal bundle itself, cocycle-free.** The cleanest structural fact used here is that $SU(2)$ acting on the unit sphere $S^3$ of its defining representation is *isomorphic to $SU(2)$ acting on itself by right translation*, via the orbit map $A \mapsto A e_1$ with trivial stabiliser. Whenever the structure group $G$ acts simply transitively on the typical fibre $F$ of an associated bundle $P \times_G F$, the choice of a base point $f_0 \in F$ with trivial stabiliser gives a canonical isomorphism $P \cong P \times_G F$ as $G$-spaces, with no transition functions to check — the identification is intrinsic. This is why "$P \cong S(E)$" is available *for free* for $SU(2)$ and its $\mathbb{C}^2$: the unit sphere of the defining representation is a $G$-torsor. The same phenomenon underlies "a $G$-torsor is a principal bundle", the identification of the frame bundle of a trivialised bundle with $M \times G$, and, one dimension of generality up, the description of homogeneous principal bundles $G \to G/H$. The recognition pattern is: *a fibre on which $G$ acts freely and transitively is $G$ in disguise* — and disguised copies of $G$ carry sections exactly when the geometry provides one, as the normalised generic section did here.
