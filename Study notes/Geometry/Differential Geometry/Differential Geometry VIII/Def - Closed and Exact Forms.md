---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Differential k-Form on a Manifold"
  - "Def - Exterior Derivative on a Manifold"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold. $\Omega^k(M)$ is the space of smooth $k$-forms; $d : \Omega^k(M) \to \Omega^{k+1}(M)$ is the exterior derivative. A form $\omega \in \Omega^k(M)$ is **closed** if $d\omega = 0$, and **exact** if there exists $\eta \in \Omega^{k-1}(M)$ with $\omega = d\eta$. We write $Z^k(M) = \ker(d : \Omega^k \to \Omega^{k+1})$ for the space of closed $k$-forms and $B^k(M) = \operatorname{im}(d : \Omega^{k-1} \to \Omega^k)$ for the space of exact $k$-forms. The $k$-th **de Rham cohomology** of $M$ is $H^k_{dR}(M) = Z^k(M)/B^k(M)$. The full registry is on [[Differential Geometry VIII — Differential Forms]].

This page is a **compound page**: it defines two interlocking notions — closed and exact — because they are introduced together and neither is fully usable without the other (the central question of the chapter is the relationship between them).

---

# Axiom Motivation

The two notions are forced by the structure of the exterior derivative and by the topological question they jointly raise.

**Why "closed"?** A form $\omega$ is closed if $d\omega = 0$, i.e., the exterior derivative annihilates it. The condition is meaningful because $d$ is a well-defined, intrinsic operator on $\Omega^\bullet(M)$, and the kernel of any intrinsic operator deserves a name. Closedness is the natural test condition for any form whose primitive is sought: if a primitive $\eta$ with $\omega = d\eta$ exists, then $d\omega = d^2\eta = 0$, so closedness is *necessary* for exactness. The closedness test is therefore the mandatory first step in every exactness question.

**Why "exact"?** A form $\omega$ is exact if it has a *primitive* — a form $\eta$ one degree lower whose exterior derivative is $\omega$. The terminology is borrowed from differential equations (a $1$-form $\omega = P\,dx + Q\,dy$ is "exact" exactly when $\omega = df$ for some function $f$, in which case the ODE $P\,dx + Q\,dy = 0$ is integrable). Exactness is what we usually *want*: a primitive is what we integrate to find by anti-differentiation, what we use to evaluate integrals by Stokes, what we recognize as a potential energy in physics, and what de Rham theory then promotes to a [[Def - Homotopy|homotopy]] invariant via the quotient construction.

**The relationship $B^k \subseteq Z^k$.** Every exact form is closed: if $\omega = d\eta$, then $d\omega = d^2\eta = 0$ by [[Thm - d-Squared-is-Zero|nilpotence of d]]. The reverse inclusion — every closed form is exact — is the **central question of the chapter**, and the answer depends on the topology of $M$.

**The Poincaré lemma: locally, closed $\Rightarrow$ exact.** On a contractible manifold (e.g., $\mathbb{R}^n$, a convex set, a star-shaped set), every closed form of positive degree is exact. The proof constructs the primitive explicitly via the contracting homotopy. See [[Thm - The Poincaré Lemma]] (in MA IV, used here for $\mathbb{R}^n$). The lemma is *local*, so it always applies in a sufficiently small coordinate neighborhood — every point of every manifold has a contractible neighborhood. **Locally, every closed form has a primitive.**

**The de Rham theorem: globally, the failure of closed $\Rightarrow$ exact is topological.** On a non-contractible manifold, closed forms may fail to be exact. The quotient $H^k_{dR}(M) = Z^k(M)/B^k(M)$ — the **de Rham cohomology** — measures the failure precisely. By de Rham's theorem, $H^k_{dR}(M) \cong H^k(M; \mathbb{R})$, the singular cohomology with real coefficients — a topological invariant computable by purely combinatorial means with no calculus. So the calculus-side gap between closed and exact equals the topology-side cohomology of $M$.

**Why this matters for problem-solving.** Every problem of the form "is this form exact?" "is this field conservative?" "is this integral path-independent?" reduces to two tests: (i) is $\omega$ closed? (ii) if so, what is the topology of the domain? The angular form $\omega = (-y\,dx + x\,dy)/(x^2+y^2)$ on the punctured plane is the prototype: it is closed, but the punctured plane has $H^1_{dR} \cong \mathbb{R}$, and $\omega$ represents the nonzero generator — so $\omega$ is closed but not exact. The single number $\int_{S^1}\omega = 2\pi$ detects this.

**What breaks if we tried weaker conditions?** Replacing "closed" with "$d\omega = $ something easy" loses the connection to exactness; replacing "exact" with "$\omega = $ pullback of something" works only when the relevant map exists. The two conditions $d\omega = 0$ and $\omega = d\eta$ are the algebraically minimal conditions that interact correctly with $d$ to give a well-behaved theory.

**Why the quotient and not the kernel or image alone?** Because the closed forms $Z^k(M)$ are infinite-dimensional (they include all smooth $0$-forms whose differential is $0$, namely the locally constant functions, on a manifold with arbitrarily many components — already an infinite-dimensional space for many manifolds, and worse in higher degrees). The exact forms $B^k(M)$ are also infinite-dimensional. The *quotient* $H^k_{dR}(M)$, however, is finite-dimensional for any reasonable manifold (e.g., compact, or homotopy equivalent to a finite CW complex), and it is precisely the right finite-dimensional invariant.

---

# The Definition

Let $\omega \in \Omega^k(M)$ be a smooth differential $k$-form on a smooth manifold $M$.

- **Closed.** $\omega$ is **closed** if $d\omega = 0$ in $\Omega^{k+1}(M)$.
- **Exact.** $\omega$ is **exact** if there exists a smooth $(k-1)$-form $\eta \in \Omega^{k-1}(M)$ with $\omega = d\eta$.

By convention, every $0$-form is automatically "closed when constant" — a function $f$ has $df = 0$ iff $f$ is locally constant. There are no exact $0$-forms (no $(-1)$-forms exist), so the question of exactness is trivial in degree $0$.

The spaces of closed and exact $k$-forms are
$$Z^k(M) = \ker(d : \Omega^k(M) \to \Omega^{k+1}(M)), \qquad B^k(M) = \operatorname{im}(d : \Omega^{k-1}(M) \to \Omega^k(M)).$$

**The inclusion $B^k \subseteq Z^k$.** Every exact form is closed: $\omega = d\eta \Rightarrow d\omega = d^2\eta = 0$ by [[Thm - d-Squared-is-Zero]]. This inclusion is what makes the quotient $Z^k/B^k$ a well-defined vector space.

**de Rham cohomology.** The $k$-th **de Rham cohomology [[Def - Group|group]]** of $M$ is the quotient vector space
$$H^k_{dR}(M) = Z^k(M)/B^k(M) = \frac{\{\text{closed } k\text{-forms}\}}{\{\text{exact } k\text{-forms}\}}.$$
Elements of $H^k_{dR}(M)$ are equivalence classes of closed forms, with two closed forms equivalent if they differ by an exact form. The class of $\omega$ is denoted $[\omega] \in H^k_{dR}(M)$.

**Algebraic structure.** $\Omega^\bullet(M)$ is a graded algebra; $Z^\bullet(M) = \bigoplus_k Z^k(M)$ is a graded subalgebra (the wedge of two closed forms is closed, by graded Leibniz applied to $d(\omega \wedge \eta) = d\omega \wedge \eta \pm \omega \wedge d\eta$, both terms vanishing); $B^\bullet(M)$ is a *two-sided [[Def - Ideal|ideal]]* in $Z^\bullet(M)$ (the wedge of a closed and an exact form is exact, by Leibniz). So $H^\bullet_{dR}(M) = Z^\bullet(M)/B^\bullet(M)$ inherits an associative graded-commutative algebra structure — the **de Rham cohomology [[Def - Ring|ring]]** of $M$.

**Functoriality.** For a smooth map $F : M \to N$, the pullback $F^* : \Omega^k(N) \to \Omega^k(M)$ sends closed forms to closed forms ($F^*d\omega = dF^*\omega$, so $d\omega = 0 \Rightarrow dF^*\omega = 0$) and exact forms to exact forms ($F^*(d\eta) = d(F^*\eta)$). Therefore $F^*$ descends to a well-defined map $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$, making $H^k_{dR}$ a contravariant functor.

**The Poincaré lemma.** On a contractible open set $U \subseteq M$, every closed form of positive degree is exact: $H^k_{dR}(U) = 0$ for $k \geq 1$. The proof, available in [[Thm - The Poincaré Lemma]] in MA IV, constructs the primitive via the contracting homotopy. The lemma is *local* — every point of every manifold has a contractible neighborhood — so locally, closed always implies exact.

**Singular cohomology comparison — de Rham's theorem.** For any smooth manifold $M$ (with suitable conditions, satisfied by all reasonable manifolds),
$$H^k_{dR}(M) \cong H^k(M; \mathbb{R}),$$
where the right side is singular cohomology with real coefficients. This is **de Rham's theorem**, stated in [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]]. It is the bridge from calculus to topology: the de Rham invariant defined by smooth forms equals the topological invariant defined by simplicial methods.

---

# Categorical Definition

A pair (closed, exact) of forms makes the de Rham complex $(\Omega^\bullet(M), d)$ a **cochain complex**: a $\mathbb{Z}$-graded vector space with a degree-$+1$ linear endomorphism $d$ satisfying $d^2 = 0$. The cohomology $H^\bullet = \ker d / \operatorname{im} d$ is the universal invariant of a cochain complex.

In the language of homological algebra, the de Rham complex is the **prototype of a DG algebra (differential graded algebra)**, and its cohomology is the prototype of a graded-commutative algebra invariant of the underlying space. The whole machinery of homological algebra — spectral sequences, derived functors, Tor, Ext — was developed in part to understand cochain complexes like the de Rham complex.

**Cocycles and coboundaries.** The terminology "cocycle" and "coboundary" is the homological-algebra version of "closed" and "exact": a $k$-cocycle is a closed $k$-form (an element of $\ker d$), and a $k$-coboundary is an exact $k$-form (an element of $\operatorname{im} d$). The cohomology $H^k = (\text{cocycles}) / (\text{coboundaries})$. The dictionary between calculus (closed/exact) and homological algebra (cocycle/coboundary) is exact.

**de Rham as a contravariant functor.** The assignment $M \mapsto H^k_{dR}(M)$ is a contravariant functor from smooth manifolds to graded-commutative $\mathbb{R}$-algebras. Morphisms (smooth maps) become $F^*$ on cohomology, reversing direction. By the homotopy invariance of de Rham cohomology — which follows from the Poincaré lemma machinery in [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]] — $H^k_{dR}$ even descends to a functor on the *homotopy* category of smooth manifolds, identifying $H^k_{dR}(M) = H^k_{dR}(N)$ when $M \simeq N$.

---

# Relate to Other Fields / Compression

**The closed-versus-exact dichotomy is the calculus of holes.** This is the most important conceptual remark in this chapter, and it is worth stating directly. The identity $d^2 = 0$ guarantees exact $\Rightarrow$ closed. The Poincaré lemma guarantees the converse *locally* — every closed form is *locally* exact. The gap between local and global is the topology of the manifold, and the **periods** of a closed form (the integrals around generating loops) measure the gap precisely. A closed form on a domain with holes is exact if and only if all its periods vanish — and de Rham cohomology is the systematic packaging of this principle.

**True name:** A closed form is "a form whose local primitives may or may not patch into a global primitive." An exact form is "a form whose local primitives *do* patch."

A trigger-reaction pattern: **see "is this form exact?" → (i) compute $d\omega$; if nonzero, the answer is no. (ii) if $d\omega = 0$, ask: is the domain contractible? If yes, apply Poincaré. If no, compute the periods $\int_\gamma\omega$ around loops generating the relevant homology**. The two-step test is universal.

**Bridge to physics — conservative force fields.** In Newtonian mechanics, a force field $F$ on $\mathbb{R}^3$ is **conservative** if and only if its work $\int_\gamma F \cdot dr$ is path-independent. Equivalently, $F = -\nabla U$ for some potential $U$. In the language of forms: the work form $\omega_F = \sum F_j\,dx^j$ is exact, $\omega_F = -dU$. The question of conservativity reduces to: is $\omega_F$ closed (necessary, equivalent to $\nabla \times F = 0$)? And if so, is the domain simply connected (sufficient, by Poincaré for $1$-forms)? **Conservativity = exactness of the work form.**

**Bridge to electromagnetism — magnetic monopoles.** The magnetic field $\vec B$ on $\mathbb{R}^3$ corresponds to a $2$-form $\beta$, and Maxwell's equation $\nabla \cdot \vec B = 0$ becomes $d\beta = 0$ — $\beta$ is closed. On contractible spacetime regions $\beta = dA$ for some vector potential $1$-form $A$, by Poincaré. The question of whether the vector potential exists globally — i.e., whether magnetic monopoles can be sourced — is exactly the question of whether $\beta$ is globally exact on the relevant region. The Dirac string is the obstruction to global exactness.

**Bridge to algebraic topology — the de Rham theorem.** Singular cohomology $H^k(M; \mathbb{R})$ is built combinatorially from the simplices of $M$: it captures equivalence classes of simplicial cochains modulo coboundaries. The de Rham theorem states that this combinatorial invariant equals $H^k_{dR}(M)$, the calculus invariant. The proof, surprisingly subtle, runs via the integration pairing $\int : H^k_{dR}(M) \times H_k(M; \mathbb{R}) \to \mathbb{R}$, $([\omega], [c]) \mapsto \int_c \omega$, which is well-defined by Stokes' theorem (independence of closed-form representative and of cycle representative) and is a perfect pairing.

---

# Examples / Corollaries

**Is an instance — every constant function is closed.** A locally constant function $f$ has $df = 0$, hence $f$ is closed as a $0$-form. On a connected manifold, the closed $0$-forms are exactly the constants, and there are no exact $0$-forms (there are no $(-1)$-forms), so $H^0_{dR}(M) \cong \mathbb{R}$ for any connected $M$. In general $H^0_{dR}(M) \cong \mathbb{R}^{c}$ where $c$ is the number of connected components — the simplest topological invariant computable from forms.

**Is an instance — every $df$ for $f \in C^\infty(M)$ is exact.** Trivially: $df = d(f)$, and $f$ is a $(k-1)$-form (a $0$-form) with $d$ giving $df$. The cohomology class of $df$ in $H^1_{dR}(M)$ is zero. More generally, every $d\omega$ for a $(k-1)$-form $\omega$ is by definition exact and hence closed.

**Is an instance — the angular form on the punctured plane.** $\omega = (-y\,dx + x\,dy)/(x^2 + y^2)$ on $\mathbb{R}^2 \setminus \{0\}$ is closed ($d\omega = 0$ by computation) but not exact ($\int_{S^1}\omega = 2\pi$, while an exact form would integrate to zero around any closed loop by Stokes). The class $[\omega]$ generates $H^1_{dR}(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{R}$. See [[Ex - A Form that is Closed but Not Exact on the Punctured Plane]].

**Is an instance — the volume form on $S^2$.** The volume form $\omega_{S^2}$ on the round sphere is a top-degree form on a compact $2$-manifold; it satisfies $d\omega_{S^2} = 0$ trivially (top-degree forms on $n$-manifolds have $d = 0$ since $\Omega^{n+1} = 0$). But it is not exact: $\int_{S^2}\omega_{S^2} = 4\pi \neq 0$, while an exact form $d\eta$ would have $\int_{S^2}d\eta = \int_{\partial S^2}\eta = 0$ (since $\partial S^2 = \emptyset$). So $[\omega_{S^2}]$ generates $H^2_{dR}(S^2) \cong \mathbb{R}$.

**Is NOT an instance — $d^2\eta$ for some $\eta$, viewed as closed.** This is closed *and* exact, equal to zero. It is closed because $d(d^2\eta) = d^3\eta = 0$ trivially; it is exact because $d^2\eta = d(d\eta)$, so its primitive is $d\eta$. In fact $d^2\eta = 0$ identically by nilpotence, so the example is vacuous: there is no nontrivial form that is "$d^2\eta$".

**Is NOT an instance — a closed form is automatically exact.** False on any manifold with nontrivial $H^k_{dR}$. The standard counterexample is the angular form above. On $\mathbb{R}^n$ (or any contractible domain), by the Poincaré lemma every closed positive-degree form *is* exact, so the test is degenerate; the closed-not-exact phenomenon requires a non-contractible domain.

**Is NOT an instance — an exact form has nonzero period.** False. By Stokes, $\int_\gamma d\eta = \int_{\partial\gamma}\eta = 0$ for any closed loop $\gamma$ (whose boundary is empty), so exact forms always have zero period around any closed loop. This is the structural reason a nonzero period is a certificate of *non*-exactness.

**Corollary — vector calculus identities.** $\operatorname{curl}\operatorname{grad} = 0$: the curl of a gradient field is zero, equivalently the $2$-form $d(df) = d^2 f = 0$ — every exact $1$-form is closed. $\operatorname{div}\operatorname{curl} = 0$: the divergence of a curl is zero, equivalently $d(d\omega) = d^2\omega = 0$ for a $1$-form $\omega$, expressing that every exact $2$-form (in $\mathbb{R}^3$, identified with a vector field via the Hodge star) is closed. Both are instances of $d^2 = 0$.

**Corollary — closed-not-exact detection via integration.** If $\omega$ is closed and there exists a closed (in the topological sense) $k$-submanifold $\Sigma$ with $\int_\Sigma\omega \neq 0$, then $\omega$ is not exact. (For exact forms, Stokes gives $\int_\Sigma d\eta = \int_{\partial\Sigma}\eta = 0$ when $\partial\Sigma = \emptyset$.) This is the "period test" mentioned above and is the standard way to prove non-exactness.

**Corollary — the de Rham complex of a contractible manifold.** On $\mathbb{R}^n$ (or any contractible domain), $H^k_{dR} = 0$ for $k \geq 1$ and $H^0_{dR} \cong \mathbb{R}$. The de Rham complex is *acyclic in positive degrees*, which is the Poincaré lemma. This is the calculus-side encoding of "contractible manifolds have no holes".

**Calibration check.** Verify $d(df) = 0$ for $f = e^{xy}$ on $\mathbb{R}^2$; check that $\omega = x\,dx + y\,dy$ on $\mathbb{R}^2$ is exact (find an explicit primitive — answer: $\frac{1}{2}(x^2+y^2)$); show $\omega = y\,dx - x\,dy$ on $\mathbb{R}^2$ is *not* closed (compute $d\omega = -2\,dx \wedge dy$); state $H^k_{dR}(\mathbb{R}^n)$ for all $k$ (answer: $\mathbb{R}$ for $k = 0$, zero for $k \geq 1$, by Poincaré); explain why the period $\int_{S^1}d\theta = 2\pi$ proves $d\theta$ is not exact on $\mathbb{R}^2 \setminus \{0\}$. If you can explain why the wedge of two closed forms is closed *and* the wedge of a closed form with an exact form is exact, you have understood the algebraic structure of $H^\bullet_{dR}$.

---

# Unlocked by This

> [!tip] de Rham Cohomology *(from DG X / Algebraic Topology)*
> The quotient $H^k_{dR}(M) = Z^k(M)/B^k(M)$ is the **de Rham cohomology** — a finite-dimensional vector space (for compact $M$) that is a powerful topological invariant. By **de Rham's theorem**, $H^k_{dR}(M) \cong H^k(M; \mathbb{R})$, the singular cohomology with real coefficients. The dimension counts $k$-dimensional holes. See [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]].

> [!tip] The Poincaré Lemma *(this chapter)*
> On a contractible manifold, every closed form of positive degree is exact: $H^k_{dR}(\text{contractible}) = 0$ for $k \geq 1$. The proof constructs the primitive by integrating along the contracting homotopy. See [[Thm - The Poincaré Lemma]] (in MA IV).

> [!tip] Symplectic Form *(from Symplectic Geometry)*
> A **symplectic form** $\omega$ on a $2n$-manifold is closed ($d\omega = 0$) and nondegenerate. The closedness is what makes Cartan-formula computations of $\mathcal{L}_X\omega$ simplify, and it is what makes Hamiltonian vector fields preserve $\omega$. The class $[\omega] \in H^2_{dR}(M)$ is a topological invariant of the symplectic structure.

> [!tip] Holonomic Constraints and Frobenius *(from Mechanics / DG X)*
> A constraint $1$-form $\omega$ on configuration space is **holonomic** (integrable) if and only if $\omega \wedge d\omega = 0$ — a closedness-like condition that licenses the existence of a level-set function whose differential is proportional to $\omega$. This is the Frobenius integrability criterion in forms language. Non-holonomic constraints (like rolling without slipping) are precisely those whose constraint form fails this condition.

> [!tip] Maxwell's Equations and Gauge Symmetry *(from Electromagnetism)*
> The electromagnetic field strength $F$ is a closed $2$-form ($dF = 0$, the homogeneous Maxwell equations). On a contractible region the Poincaré lemma gives $F = dA$ for a potential $1$-form $A$ — the vector potential. The gauge freedom $A \mapsto A + d\chi$ adds an exact form and leaves $F$ unchanged because $d^2 = 0$. **Gauge symmetry is the freedom to add exact forms to a potential, with no observable consequences.** The global obstruction to a single-valued vector potential is the nontriviality of the second de Rham cohomology of the magnetic-field region.
