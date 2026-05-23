---
type: theorem
subject: differential-topology
prereqs:
  - "Def - Brouwer Degree of a Map"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Def - Integral of a Compactly Supported Form on a Manifold"
tags: [topology, differential-topology, degree-theory, homotopy]
---

# Notation

Let $M^n, V^n$ be closed (compact, no boundary) oriented smooth manifolds of the same dimension $n$. A **smooth homotopy** from $\phi_0$ to $\phi_1$ is a smooth map $H : M \times [0, 1] \to V$ with $H(\cdot, 0) = \phi_0$ and $H(\cdot, 1) = \phi_1$. We write $\phi_t = H(\cdot, t)$. Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

---

# Statement

> **Theorem (Brouwer Degree is a Homotopy Invariant).** Let $\phi_t : M^n \to V^n$ ($t \in [0, 1]$) be a smooth homotopy between maps of closed oriented manifolds of the same [[Def - Dimension|dimension]]. Then the [[Def - Brouwer Degree of a Map|Brouwer degree]] is constant in $t$:
> $$
> \deg(\phi_0) = \deg(\phi_1).
> $$
> Equivalently, $\deg$ descends to a function $[M, V] \to \mathbb{Z}$ on the set of smooth-homotopy classes of maps $M \to V$.

> **Corollary.** Maps with different Brouwer degrees are not homotopic. In particular: the identity $\mathrm{id}_M : M \to M$ (degree $+1$) is not homotopic to a constant map (degree $0$) for any closed oriented manifold $M$.

> **Corollary (Brouwer fixed-point theorem, smooth version).** Every smooth map $\phi : B^{n+1} \to B^{n+1}$ of the closed unit ball to itself has a fixed point.

---

# Motivation

The Brouwer degree is a count of "how many times the map wraps the source around the target" — but a priori this count could change as the map deforms continuously. The remarkable fact is that **it cannot**: the integer degree is locked under any smooth deformation, exactly because the degree is an integral of a top form whose pullback differs from itself by an exact form under homotopy, and Stokes' theorem makes that exact form integrate to zero on a closed manifold.

This homotopy invariance is what makes Brouwer degree a **topological** invariant rather than a merely geometric one. Without it, the degree would change wildly under perturbations of $\phi$ — for instance, a small bump on the source could create new preimage points, and the count would jump. Homotopy invariance says: any new preimage points created by a deformation must come in **cancelling pairs** (one positive, one negative), keeping the algebraic count fixed.

The theorem is the technical engine behind every application of degree theory: the fundamental theorem of algebra (degree is continuous in the polynomial's coefficients, hence locally constant, hence equal to $n$ since the limit $z^n$ map has degree $n$); the Brouwer fixed-point theorem (a self-map without fixed point produces a retraction $B \to S^n$, contradicting degree-of-the-identity = $1$); the Borsuk–Ulam theorem; the existence of zeros of vector fields on closed manifolds via Poincaré–Hopf — all flow from the fact that degree is homotopy-invariant.

---

# Sources and Targets

**Sources (Input Broadening).**

*Source 1: A continuous family of maps $\phi_t$.* Any smooth homotopy — e.g., $\phi_t = (1-t)\phi_0 + t\phi_1$ for maps into a convex target, or a more general path in the space of maps — gives a hypothesis for the theorem. **Why $B \Rightarrow A$:** Direct application — smooth homotopy is the precondition. **Example problem:** A polynomial map $P_\epsilon = z^n + \epsilon\cdot\text{(lower order)}$ is homotopic to $z^n$ via $t \mapsto z^n + t\epsilon\cdot\text{(...)}$, so $\deg(P_\epsilon) = \deg(z^n) = n$. Application: fundamental theorem of algebra.

*Source 2: Two maps $\phi_0, \phi_1$ that are continuously close (not necessarily through a given homotopy).* If $\phi_0, \phi_1 : M \to V$ are sufficiently close in the $C^0$-topology (close enough that the straight-line interpolation in $V$ stays well-defined — needs $V$ to have small enough convex normal neighbourhoods), then they are homotopic and have equal degrees. **Why $B \Rightarrow A$:** Closeness gives a canonical homotopy via straight-line interpolation in normal coordinates of $V$. **Example problem:** Smoothing a continuous map to a smooth map preserves degree (the smoothing can be done in $C^0$-small steps).

*Source 3: A degree-zero map.* If $\phi : M \to V$ has $\deg(\phi) = 0$, then $\phi$ might still be highly nontrivial (degree zero does not mean homotopic to constant in general — though for maps $S^n \to S^n$ it does, by Hopf's theorem). But: **degree-zero on $V \neq S^n$ is *not* sufficient for null-homotopy**. **Example problem:** A map $T^2 \to S^2$ can have degree zero but still wrap around topologically — degree is too coarse for the target $S^2$ when the source is not $S^n$.

**Targets (Output Amplification).**

*Target 1: Distinguishing homotopy classes.* For any two maps $\phi_0, \phi_1 : M \to V$ with $\deg(\phi_0) \neq \deg(\phi_1)$, the theorem says they are *not* homotopic. So degree separates homotopy classes — though not always finely enough (for maps $T^2 \to S^2$ it does not, but for maps $S^n \to S^n$ Hopf's theorem says it is a *complete* invariant). **Application:** Concrete obstructions to homotopy.

*Target 2: Continuity of degree under perturbation.* Degree is locally constant in the space of maps — once you compute $\deg(\phi)$ for one $\phi$, all maps in a small neighbourhood of $\phi$ in $C^\infty(M, V)$ have the same degree. **Application:** Stability of degree-theoretic counts under errors / approximations. The **fundamental theorem of algebra** uses this: any small perturbation of $z^n$ still has degree $n$ as a map of the Riemann sphere.

*Target 3: Fixed-point theorems via topological obstructions.* If $\phi : M \to M$ has a "wrong" degree (e.g., for an orientable closed manifold, $\deg \neq 1$), then certain geometric properties are forced. The cleanest application is the Brouwer fixed-point theorem: a fixed-point-free self-map of $B^{n+1}$ would produce a retraction $B^{n+1} \to S^n$, but a retraction would force $\deg(\mathrm{id}_{S^n}) = 1$ to factor through a contractible space, contradiction.

---

# Why Is It True

The proof is essentially **Stokes' theorem on a closed manifold**: an exact form on a closed manifold integrates to zero. The homotopy $H : M \times [0, 1] \to V$ gives a pullback form $H^*\omega \in \Omega^n(M \times [0, 1])$, and $\int_{M \times \{1\}}H^*\omega - \int_{M \times \{0\}}H^*\omega = \int_{M \times [0, 1]}d(H^*\omega) = \int_{M \times [0, 1]}H^*d\omega = 0$, where the first equality is Stokes (the boundary of $M \times [0, 1]$ is $M \times \{1\} - M \times \{0\}$), and the last equality is $d\omega = 0$ (top-degree forms on $V$ are automatically closed since $\Omega^{n+1}(V) = 0$ when $\dim V = n$).

**The bolded one-liner:** **degree is a homotopy invariant because the pullback of a top-degree form on a homotopy-cylinder is closed (since the target has no $(n+1)$-forms), so its integral over the cylinder vanishes by Stokes, forcing the boundary integrals to agree.**

A purely topological way to see it: in singular homology, the induced map $H_*$ on top-degree homology is, for an oriented closed $n$-manifold, multiplication by $\deg$. Homotopic maps induce the *same* map on homology (this is the basic homotopy-invariance of singular homology). So homotopic maps have the same degree. This is the homology-theoretic version; the de Rham-Stokes argument above is its smooth-de-Rham analogue, and the two agree via the de Rham theorem.

A picture: imagine $\phi_t$ continuously deforming. Preimages $\phi_t^{-1}(y)$ for a regular value $y$ can be created or destroyed only in **pairs**: as $\phi_t$ deforms, two preimage points can merge and disappear (one with sign $+1$, the other with sign $-1$, since they must approach the boundary of the regular-value set with opposite Jacobian signs), or a pair can appear (similarly with opposite signs). The signed count is unchanged. This is the geometric mechanism behind homotopy invariance: deformations preserve the *algebraic* count even though they can change the *absolute* count $|\phi^{-1}(y)|$.

---

# What Makes This Hard

The technical hard part is establishing **independence of the regular value** in the preimage-counting formula, which is what makes the homotopy invariance proof work cleanly. If two regular values $y_0, y_1$ give different preimage counts, then degree-as-signed-count would not be well-defined; one needs to know that as $y$ varies along a path of regular values, the signed count is constant. The argument uses the fact that the set of regular values is open and dense (Sard's theorem), and that crossing the critical-value set involves pairs of preimages appearing or disappearing in cancelling ways.

A second technical subtlety: the homotopy $H$ needs to be smooth, not just continuous. For continuous maps, one approximates by smooth maps (which is possible by partition-of-unity arguments) and notes that the smooth approximation preserves degree (it is a small homotopy). So the *smooth* homotopy invariance extends to the continuous case via approximation — but the formal statement and proof are cleanest in the smooth category.

A common confusion: students sometimes think the theorem says "smooth [[Def - Homotopy|homotopies]] preserve the preimage count $|\phi^{-1}(y)|$". This is **false** — the count can change (and typically does) as the homotopy deforms $\phi$ to pass through critical values. What is preserved is the *signed* count, the algebraic sum $\sum_x \mathrm{sign}\,\phi(x)$. Pairs can be created or destroyed, but with cancelling signs.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Let $H : M \times [0, 1] \to V$ be the smooth homotopy. Apply Stokes' theorem to $H^*\omega$ on the manifold $M \times [0, 1]$ (with boundary $M \times \{0\} \sqcup M \times \{1\}$ oriented as $M \times \{1\} - M \times \{0\}$). Since $\omega$ is top-degree on $V$, $d\omega = 0$, hence $H^*\omega$ is closed on $M \times [0, 1]$. The difference $\int_{M \times \{1\}}H^*\omega - \int_{M \times \{0\}}H^*\omega = \int_{M \times [0, 1]}dH^*\omega = 0$.

**Subgoal decomposition:**

1. **Set up the homotopy and the boundary identification.** The product $M \times [0, 1]$ is an $(n+1)$-manifold with boundary $M \times \{0\} \sqcup M \times \{1\}$. Orient the product as $M \times [0, 1]$ (the standard product orientation), and the boundary inherits the orientation $M \times \{1\}$ outward, $M \times \{0\}$ inward.
   - *Hint:* Just verify the orientation convention; the boundary of $M \times [0, 1]$ as an oriented manifold is $M \times \{1\} - M \times \{0\}$.
   - *Why needed:* Stokes' theorem requires a precise boundary orientation.

2. **Note that $H^*\omega$ is closed on $M \times [0, 1]$.** Since $\omega \in \Omega^n(V)$ and $\dim V = n$, $\Omega^{n+1}(V) = 0$, so $d\omega = 0$. Hence $d(H^*\omega) = H^*(d\omega) = 0$.
   - *Hint:* Use the naturality of $d$ with respect to pullback.
   - *Why needed:* This is what makes Stokes' theorem yield zero on the cylinder.

3. **Apply Stokes' theorem.** $\int_{\partial(M \times [0, 1])}H^*\omega = \int_{M \times [0, 1]}d(H^*\omega) = 0$. The left side equals $\int_{M \times \{1\}}H^*\omega - \int_{M \times \{0\}}H^*\omega$ by the boundary orientation.
   - *Hint:* Standard Stokes' theorem applied to $M \times [0, 1]$ with boundary.
   - *Why needed:* This gives the boundary integral identity.

4. **Identify the boundary integrals as $\deg(\phi_1)$ and $\deg(\phi_0)$.** The restriction $H|_{M \times \{t\}} = \phi_t$, so $H^*\omega|_{M \times \{t\}} = \phi_t^*\omega$. Hence $\int_{M \times \{t\}}H^*\omega = \int_M\phi_t^*\omega = \deg(\phi_t)$.
   - *Hint:* Apply the definition of degree to each slice.
   - *Why needed:* Connects the cylinder calculation to the actual degrees.

Combining: $\deg(\phi_1) - \deg(\phi_0) = 0$, hence equal.

---

# Lemma Decomposition

> [!note]- Lemma 1: Top-degree forms on $V^n$ are automatically closed
> **Statement:** For any $n$-form $\omega \in \Omega^n(V)$ where $\dim V = n$, $d\omega = 0$.
>
> **Hint:** $d\omega \in \Omega^{n+1}(V)$, but $\Omega^{n+1}(V) = 0$ when $V$ has dimension $n$ (there are no $(n+1)$-forms on an $n$-manifold).
>
> **Why needed:** This is what makes Stokes' theorem on the homotopy cylinder give zero, without which the proof fails.
>
> > [!note]- Full proof
> > Trivial: $\Omega^k(V) = 0$ for $k > \dim V$ by definition (an alternating $k$-tensor on an $n$-dimensional vector space vanishes when $k > n$). So $d\omega = 0$ pointwise, hence as a form.

> [!note]- Lemma 2: Stokes' theorem on the cylinder
> **Statement:** For a smooth $n$-form $\eta$ on $M^n \times [0, 1]$, $\int_{M \times \{1\}}\eta - \int_{M \times \{0\}}\eta = \int_{M \times [0, 1]}d\eta$.
>
> **Hint:** Direct application of [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] on the oriented manifold-with-boundary $M \times [0, 1]$, whose boundary is $M \times \{1\} - M \times \{0\}$.
>
> **Why needed:** This is the technical input that connects degree-on-source to degree-on-target via the cylinder.
>
> > [!note]- Full proof
> > Stokes' theorem on an oriented compact manifold with boundary says $\int_W d\eta = \int_{\partial W}\eta$. Here $W = M \times [0, 1]$ (compact since $M$ is closed), with boundary $\partial W = M \times \{1\} - M \times \{0\}$ (the standard orientation of the cylinder gives outward-pointing normal on $M \times \{1\}$ and inward-pointing on $M \times \{0\}$, so the orientations on the boundary components differ by a sign). Substituting: $\int_{M \times [0, 1]}d\eta = \int_{M \times \{1\}}\eta - \int_{M \times \{0\}}\eta$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\omega \in \Omega^n(V)$ be a normalised top-degree form, $\int_V\omega = 1$. Let $H : M \times [0, 1] \to V$ be the smooth homotopy from $\phi_0$ to $\phi_1$. Then $H^*\omega \in \Omega^n(M \times [0, 1])$, and by Lemma 1, $d\omega = 0$, hence $d(H^*\omega) = H^*(d\omega) = 0$. By Lemma 2 (Stokes on the cylinder),
> $$
> \int_{M \times \{1\}}H^*\omega - \int_{M \times \{0\}}H^*\omega = \int_{M \times [0, 1]}d(H^*\omega) = 0.
> $$
> The restriction $H|_{M \times \{t\}}$ is naturally identified with $\phi_t : M \to V$ (via the canonical identification $M \times \{t\} \cong M$). Hence
> $$
> \int_{M \times \{t\}}H^*\omega = \int_M\phi_t^*\omega = \deg(\phi_t).
> $$
> Substituting,
> $$
> \deg(\phi_1) - \deg(\phi_0) = 0,
> $$
> proving the theorem. $\square$

---

# Cross-Field Exercise Suggestions

1. **Fundamental theorem of algebra via degree continuity.** Show that any polynomial $P(z) = z^n + a_{n-1}z^{n-1} + \cdots + a_0$, extended to a map $P : \mathbb{CP}^1 \to \mathbb{CP}^1$ (with $P(\infty) = \infty$), is homotopic to $z \mapsto z^n$ via $t \mapsto z^n + t(a_{n-1}z^{n-1} + \cdots + a_0)$. By homotopy invariance, $\deg(P) = \deg(z^n) = n$. Hence for $n \geq 1$, $P$ is surjective (degree-$n \neq 0$ map is surjective), so $P$ takes value $0$ — fundamental theorem of algebra. **Why nonobvious:** This is the cleanest proof of the FTA, requiring no analytic continuation, [[Def - Residue|residue]] calculus, or other complex-analytic machinery beyond degree theory.

2. **Borsuk–Ulam theorem.** Use homotopy invariance to prove that every continuous odd map $f : S^n \to S^n$ (i.e., $f(-x) = -f(x)$) has odd degree, in particular nonzero degree. **Application:** any continuous map $S^n \to \mathbb{R}^n$ sends some pair of antipodal points to the same value (the Borsuk–Ulam theorem) — proven by considering $g(x) = f(x) - f(-x)$ and showing it must have a zero. **Why nonobvious:** Translating "odd map" to "odd degree" uses homotopy invariance to compare $f$ with the antipodal map.

3. **Brouwer fixed-point theorem via degree.** Suppose $\phi : B^{n+1} \to B^{n+1}$ is a smooth fixed-point-free self-map. Define the **retraction** $r(x) =$ the point on $S^n = \partial B^{n+1}$ where the ray from $\phi(x)$ through $x$ exits the ball. Then $r$ is smooth and $r|_{S^n} = \mathrm{id}_{S^n}$. The map $r$ provides a smooth retraction $B^{n+1} \to S^n$. But $r|_{S^n} = \mathrm{id}_{S^n}$ has degree $1$ as a map $S^n \to S^n$, and any retraction can be deformed to a constant map (contracting $B^{n+1}$ to a point), giving degree $0$ — a contradiction with homotopy invariance. So no fixed-point-free $\phi$ exists. **Why nonobvious:** The whole argument hinges on the impossibility of a retraction $B^{n+1} \to S^n$, which is itself a consequence of degree homotopy invariance.

---

# Bridges

- **To **singular homology** and the **functoriality of $H_n$**.** The Brouwer degree is, in homological language, the integer $\deg(\phi)$ such that the induced map $\phi_* : H_n(M; \mathbb{Z}) \to H_n(V; \mathbb{Z})$ sends $[M] \mapsto \deg(\phi)\cdot[V]$ on fundamental classes. Homotopic maps induce equal maps on singular homology (a basic theorem of algebraic topology), so they have equal degrees. The de Rham–Stokes proof here is the smooth-cohomology version of this homological fact, and the two are equivalent via the de Rham theorem.

- **To the **Lefschetz fixed-point theorem** ([[Algebraic Topology I — Singular Homology and the de Rham Theorem]]).** For a self-map $\phi : M \to M$ on a closed oriented manifold, the **Lefschetz number** $L(\phi) = \sum_k(-1)^k\mathrm{tr}(\phi_* : H_k \to H_k)$ is a homotopy invariant (by the same argument as for degree). If $L(\phi) \neq 0$, then $\phi$ has a fixed point. The identity case gives $L(\mathrm{id}) = \chi(M)$, the Euler characteristic, and the resulting theorem is the **Poincaré–Hopf theorem** for gradient vector fields. The degree is the $H_n$-piece of the Lefschetz number, and degree's homotopy invariance is the simplest case of Lefschetz's.

- **To **homotopy theory** and **classifying spaces**.** The degree generalises to the **Hopf invariant** for maps $S^{2n-1} \to S^n$, the **mapping degree** for maps between general spaces, and the **homotopy classes** $[M, V] = \pi_0(\mathrm{Map}(M, V))$. For maps $S^n \to S^n$, Hopf's theorem says degree is a *complete* invariant: $\pi_0(\mathrm{Map}(S^n, S^n)) = \mathbb{Z}$ with the degree as the isomorphism. For other targets, the homotopy classification is much richer (involving the full homotopy groups of $V$), but degree is always the first piece.

- **To **Morse theory** and the **handle decomposition** of manifolds.** The homotopy invariance of degree is the technical fact behind why Morse-theoretic counts (alternating sum of critical points equals $\chi(M)$) are topological. Adding a $k$-handle changes the Morse index sums in a controlled way, and the alternating signs give a homotopy-invariant total — exactly the same mechanism as preimage cancellation in degree theory.

---

# Unlocked by This

> [!tip] Hopf's Theorem: Degree Classifies Maps $S^n \to S^n$ *(from Algebraic Topology)*
> Two maps $S^n \to S^n$ are smoothly homotopic if and only if they have the same Brouwer degree. So degree is a *complete* invariant for self-maps of spheres, and $[S^n, S^n] = \mathbb{Z}$ via the degree. The proof beyond degree-invariance is non-trivial (requires constructing a homotopy when degrees agree).

> [!tip] The Fundamental Theorem of Algebra *(from Complex Analysis)*
> Any polynomial $P$ of degree $n \geq 1$, viewed as a map $\mathbb{CP}^1 \to \mathbb{CP}^1$, is homotopic to $z \mapsto z^n$, hence has degree $n$, hence is surjective, hence takes value $0$. This is the cleanest degree-theoretic proof of the fundamental theorem of algebra.

> [!tip] The Brouwer Fixed-Point Theorem *(from Topology)*
> Every continuous self-map of $B^{n+1}$ has a fixed point. Generalisations: the Schauder fixed-point theorem (compact maps of convex subsets of Banach spaces), the Kakutani fixed-point theorem (upper-semicontinuous correspondences) used in game theory, the Markov–Kakutani theorem in topological vector spaces. All ultimately rest on degree-theoretic obstructions.

> [!tip] The Leray–Schauder Degree *(from Nonlinear Analysis)*
> The Brouwer degree generalises to infinite-dimensional Banach spaces — the **Leray–Schauder degree** for compact perturbations of the identity — by approximation from finite-dimensional subspaces. Homotopy invariance carries over. This is the foundation of **degree-theoretic methods in nonlinear PDE**: bifurcation theory, the Krasnosel'skii fixed-point theorem, continuation methods for boundary-value problems, and existence proofs for many nonlinear elliptic equations.

> [!tip] Index Theorems and Characteristic Classes *(from Algebraic Topology III)*
> The Atiyah–Singer index theorem identifies the analytical index of an elliptic operator (dim ker − dim coker) with a topological integer (an integral of characteristic classes). The analytical index is a homotopy invariant of the operator's symbol (its principal-symbol class), and the topological index is a homotopy invariant of the underlying bundle. The agreement of the two is a vast generalisation of Brouwer's degree-invariance: both sides are homotopy-invariant integers, and they happen to be equal by deep PDE arguments.
