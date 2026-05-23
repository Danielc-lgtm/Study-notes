---
type: theorem
subject: hodge-theory
prereqs:
  - "Thm - Hodge Decomposition Theorem"
  - "Def - Harmonic Form"
  - "Def - de Rham Cohomology"
  - "Def - Closed and Exact Forms"
tags: [geometry, hodge-theory, cohomology]
---

# Notation

$(M, g)$ is a closed oriented Riemannian $n$-manifold. $\mathcal{H}^k(M) = \ker(\Delta : \Omega^k \to \Omega^k)$ is the space of harmonic $k$-forms; $H^k_{dR}(M) = Z^k(M)/B^k(M)$ is de Rham cohomology, with $Z^k = \ker d$ and $B^k = \operatorname{im}\,d$. The natural map $\iota : \mathcal{H}^k(M) \to H^k_{dR}(M)$ sends $h \mapsto [h]$.

---

# Statement

> **Theorem (Hodge isomorphism).** Let $(M, g)$ be a closed oriented Riemannian $n$-manifold. The natural map
> $$\iota : \mathcal{H}^k(M) \to H^k_{dR}(M; \mathbb{R}), \qquad h \mapsto [h],$$
> sending a harmonic $k$-form to its de Rham cohomology class, is an $\mathbb{R}$-vector-space isomorphism. Equivalently:
> 1. **(Existence)** Every de Rham cohomology class $[\omega] \in H^k_{dR}(M)$ contains at least one harmonic representative.
> 2. **(Uniqueness)** Every de Rham cohomology class contains *exactly one* harmonic representative.
> 3. **(Dimension)** $\dim\mathcal{H}^k(M) = b_k(M)$, the $k$-th Betti number. In particular, $\dim\mathcal{H}^k$ is a *topological* invariant of $M$.

---

# Motivation

This is the central structural payoff of Hodge theory. The Hodge decomposition theorem (which we use as input) is an analytic statement about an orthogonal splitting of forms. This theorem packages that analytic content into a clean cohomological statement: *the harmonic forms are exactly the cohomology classes, in a canonical way*.

Three consequences make this the most-used theorem in the chapter.

**First, harmonic representatives are canonical.** A de Rham class $[\omega]$ is an equivalence class of closed forms — an infinite-dimensional affine [[Def - Subspace|subspace]], with no preferred member. After choosing a Riemannian metric, exactly one form in the class satisfies $\Delta\omega = 0$. The choice is not arbitrary: the harmonic representative is the *$L^2$-minimum* of the class, the unique form that achieves the minimum norm subject to the constraint $[\omega] = c$. It is also the unique form satisfying both $d\omega = 0$ (closed, automatic since in the class) and $\delta\omega = 0$ (coclosed, the variational equation).

**Second, the Betti numbers become PDE-theoretic.** The dimension $b_k(M) = \dim H^k_{dR}(M)$ is, by this theorem, equal to the dimension of the solution space of an elliptic PDE: $b_k = \dim\ker\Delta$. This converts a topological invariant into an analytic one. It is the foundation of **spectral geometry**: the Betti numbers are the multiplicities of the eigenvalue $0$ in the spectrum of $\Delta$, and the positive-eigenvalue part of the spectrum encodes metric information (lengths, curvatures).

**Third, the cup product becomes computable via wedge products of harmonics.** The cup product structure on $H^*(M)$ is, abstractly, a tensor structure on cohomology classes. After the Hodge isomorphism, it becomes computable: $[\alpha] \smile [\beta] = [h_\alpha \wedge h_\beta]$, and the right side can be computed using the harmonic representatives. The wedge is generally not harmonic, but its harmonic projection gives the harmonic representative of the cup product. The cup product algebra of cohomology — a far richer invariant than just the Betti numbers — becomes concretely computable.

The proof itself is short, given the Hodge decomposition theorem. The decomposition's clean orthogonality structure immediately gives both existence and uniqueness of the harmonic representative.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is a closed oriented Riemannian manifold and a de Rham cohomology class. Several non-obvious sources lead to using this theorem.

The most common source is **a closed form, abstract or explicit, whose harmonic projection is sought**. Property $B$: $\beta \in \Omega^k(M)$ with $d\beta = 0$. The bridge is that $\beta$ defines a cohomology class $[\beta]$, which by this theorem has a unique harmonic representative $h$. Construction: $h = \beta - d\delta G\beta$ (subtract off the exact part of the Hodge decomposition). On a manifold with continuous isometry group, the harmonic projection is the symmetry-average projection — a substantial computational simplification.

A second source is **a question about the dimension of cohomology, computed analytically**. Property $B$: a question about $b_k(M)$. The bridge is $b_k = \dim\mathcal{H}^k = \dim\ker\Delta$, computable via the elliptic operator $\Delta$. On a homogeneous space, the kernel can be computed from the structure of the symmetry group's representation theory; on a Lie group, from Lie algebra cohomology; on a torus, from Fourier analysis. The theorem is the bridge that lets these analytic computations replace topological ones.

A third source is **a metric-dependent statement about cohomology that needs to be shown metric-independent**. Property $B$: a statement like "harmonic $k$-forms are dimension $b_k$" — the dimension is on the right side (topological), the left side is metric-dependent. The bridge is that the theorem gives the equality, so the dimension is the same for any choice of metric. The corollary is that any Hodge-theoretic dimension formula automatically gives a topological invariant — this is what makes the theorem so useful.

**Targets (Output Amplification)**

The conclusion is the isomorphism $\mathcal{H}^k\cong H^k_{dR}$. Combined with other facts, this produces several powerful results.

The most powerful combination is **Hodge isomorphism plus Hodge star commutation gives Poincaré duality**. The Hodge star $\star : \mathcal{H}^k\to\mathcal{H}^{n-k}$ is an isomorphism (since $\Delta\star = \star\Delta$, hence $\star$ preserves the kernel). Combined with $\mathcal{H}^k\cong H^k_{dR}$ for both $k$ and $n-k$, this gives the cohomological isomorphism $H^k_{dR}\cong H^{n-k}_{dR}$ — **Poincaré duality** for closed orientable manifolds. The combination is non-obvious because it requires both the algebraic fact ($\star$ commutes with $\Delta$) and the cohomological isomorphism; together they produce a metric-dependent construction of a topological invariant.

A second combination is **Hodge isomorphism plus symmetry gives explicit cohomology computations on homogeneous spaces**. On a homogeneous space $G/K$ with $G$-invariant metric, the harmonic forms are the $G$-invariant forms, and $\dim\mathcal{H}^k = \dim$ ($G$-invariant $k$-forms) $=$ Lie algebra cohomology $H^k(\mathfrak{g}, \mathfrak{k}; \mathbb{R})$. By the Hodge isomorphism, this equals $b_k(G/K)$. The combination is non-obvious because the symmetry-invariance is a very different characterization from "minimum $L^2$ norm" — both characterize harmonic forms on symmetric spaces.

A third combination is **Hodge isomorphism plus curvature inequality gives Bochner-type theorems**. Take a harmonic $1$-form $h$; the Hodge isomorphism identifies $h$ with a cohomology class in $H^1$. The Weitzenböck formula $\Delta = \nabla^*\nabla + \operatorname{Ric}$ on $1$-forms plus positivity of $\operatorname{Ric}$ forces $h = 0$, so $\mathcal{H}^1 = 0$, so $H^1_{dR} = 0$ by the Hodge isomorphism. This is **Bochner's theorem**, deriving a topological vanishing from a curvature condition via Hodge theory.

A fourth combination is **Hodge isomorphism plus heat-kernel gives the McKean–Singer index formula**. The supertrace of the heat semigroup on forms, $\mathrm{str}(e^{-t\Delta}) = \sum_k(-1)^k\mathrm{tr}(e^{-t\Delta}|_{\Omega^k})$, is constant in $t$ (since the time derivative vanishes by a calculation). As $t\to\infty$, the heat semigroup projects onto harmonics, giving $\mathrm{str}(e^{-t\Delta})\to\sum_k(-1)^k\dim\mathcal{H}^k = \sum_k(-1)^k b_k = \chi(M)$. As $t\to 0$, the heat kernel has a local expansion in curvature invariants, giving the integrand of the Gauss–Bonnet–Chern theorem. Equating limits: $\chi(M) = \int_M e(TM)$, the topological Euler class integrated. This is the **heat-kernel proof of Gauss–Bonnet** via Hodge theory.

---

# Why Is It True

The proof is a direct application of the Hodge decomposition theorem. The intuition compresses into one picture: **a closed form is harmonic plus exact, by the Hodge decomposition; "exact" doesn't change the cohomology class, so the harmonic part is the canonical representative**.

In detail: by the Hodge decomposition, any $k$-form $\beta$ decomposes as $\beta = h + d\alpha + \delta\gamma$. If $\beta$ is closed ($d\beta = 0$), then $0 = d\beta = d^2\alpha + d\delta\gamma = d\delta\gamma$. Pairing with $\gamma$: $0 = \langle d\delta\gamma, \gamma\rangle = \langle\delta\gamma, \delta\gamma\rangle = \|\delta\gamma\|^2$ (using the adjoint identity), so $\delta\gamma = 0$. Therefore $\beta = h + d\alpha$ — closed forms split as harmonic plus exact.

In cohomology: $[\beta] = [h + d\alpha] = [h]$ (since $d\alpha$ is exact). So the harmonic part of $\beta$ has the same cohomology class as $\beta$. Existence of a harmonic representative: take $\beta =$ any closed form in the class, and its harmonic projection $h = H\beta$ is in the same class.

Uniqueness: if $h_1, h_2 \in \mathcal{H}^k$ are both in the same cohomology class, then $h_1 - h_2 \in \mathcal{H}^k$ (closed under subtraction) and $h_1 - h_2$ is exact (same class). By the Hodge decomposition, $\mathcal{H}^k \perp d\Omega^{k-1}$ orthogonally in $L^2$. So $h_1 - h_2 \in \mathcal{H}^k \cap d\Omega^{k-1} = \{0\}$, giving $h_1 = h_2$.

**The one-line mechanism summary:** **the Hodge decomposition gives every closed form as harmonic plus exact, the exact part is cohomologically trivial, so the harmonic part is the canonical cohomology representative.**

The structural insight: **the Hodge decomposition makes "is exact" a complement of "is harmonic" inside "is closed"**. The orthogonality is the analytic content; the cohomological consequence is "any closed form is harmonic + exact, and the harmonic part is uniquely determined". Cohomology classes correspond bijectively to harmonic forms.

---

# What Makes This Hard

The proof is easy once the Hodge decomposition is granted; the difficulty is in the decomposition theorem itself (see [[Thm - Hodge Decomposition Theorem]]). The most common error in *this* theorem is **conflating uniqueness with rigidity**: the harmonic representative is unique for a *given* metric, but a different metric gives a different harmonic representative (in the same cohomology class). So $\mathcal{H}^k(M; g)$ depends on $g$ as a *subspace* of $\Omega^k$, but its *dimension* depends only on the smooth structure of $M$.

A second error: confusing "harmonic" with "closed-and-coclosed" in inappropriate settings. The equivalence $\Delta\omega = 0 \iff d\omega = 0 \text{ and } \delta\omega = 0$ holds *only on closed Riemannian manifolds*. On a noncompact manifold, harmonic forms need not be closed/coclosed in the form sense, and the cohomology correspondence breaks down.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Take the Hodge decomposition of a closed form, observe that closedness forces the coexact part to vanish (via integration by parts), so the form is harmonic plus exact. The harmonic part has the same cohomology class. For uniqueness, use the orthogonality of $\mathcal{H}^k$ and $d\Omega^{k-1}$ in the Hodge decomposition.

**Subgoal decomposition:**

1. **A closed form's Hodge decomposition has trivial coexact part.** If $\beta$ is closed, then in $\beta = h + d\alpha + \delta\gamma$, we have $\delta\gamma = 0$.
   - *Hint:* Apply $d$ to both sides and use $d\delta\gamma = -\delta d\gamma + \Delta\gamma$... actually simpler: $0 = d\beta = d^2\alpha + d\delta\gamma = d\delta\gamma$, then pair with $\gamma$ and use the adjoint identity to get $\|\delta\gamma\|^2 = 0$.
   - *Why needed:* Shows closed forms split as harmonic plus exact, with no coexact contribution.

2. **The harmonic part of a closed form has the same cohomology class.** From $\beta = h + d\alpha$, $[\beta] = [h] + [d\alpha] = [h] + 0 = [h]$.
   - *Hint:* $d\alpha$ is exact, hence cohomologically trivial.
   - *Why needed:* Establishes existence: every cohomology class has a harmonic representative (the harmonic projection of any closed form in the class).

3. **Uniqueness.** Two harmonic forms in the same cohomology class differ by an exact form. But $\mathcal{H}^k \cap d\Omega^{k-1} = 0$ by the orthogonality of the Hodge decomposition.
   - *Hint:* $h_1 - h_2 = d\eta$ for some $\eta$ (same class), and $h_1 - h_2 \in \mathcal{H}^k$. So $h_1 - h_2 \in \mathcal{H}^k \cap d\Omega^{k-1}$. The intersection is $\{0\}$ because $\langle h, d\eta\rangle = \langle\delta h, \eta\rangle = 0$ for harmonic $h$ (so $h \perp d\Omega^{k-1}$).
   - *Why needed:* Establishes uniqueness: at most one harmonic representative per class.

4. **The map $\iota$ is an isomorphism.** Surjective (existence) and injective (uniqueness) on $\mathcal{H}^k$.
   - *Hint:* Linearity is immediate; bijectivity comes from steps 2 and 3.
   - *Why needed:* Concludes the isomorphism.

5. **[[Def - Dimension|Dimensions]].** $\dim\mathcal{H}^k = \dim H^k_{dR} = b_k$.
   - *Hint:* Immediate from the isomorphism, using the definition of the Betti number.
   - *Why needed:* Provides the most-used corollary: $\dim\mathcal{H}^k$ is a topological invariant.

---

# Lemma Decomposition

> [!note]- Lemma 1: Closed forms have trivial coexact part in the Hodge decomposition
> **Statement:** If $\beta \in \Omega^k(M)$ is closed ($d\beta = 0$) and $\beta = h + d\alpha + \delta\gamma$ is the Hodge decomposition, then $\delta\gamma = 0$.
>
> **Hint:** Apply $d$: $0 = d\beta = d^2\alpha + d\delta\gamma = d\delta\gamma$. Pair with $\gamma$ and use the adjoint identity.
>
> **Why needed:** Reduces the decomposition of a closed form to "harmonic plus exact", which directly identifies the harmonic representative.
>
> > [!note]- Full proof
> > $d\beta = 0$. Decomposing: $0 = d(h + d\alpha + \delta\gamma) = dh + d^2\alpha + d\delta\gamma = 0 + 0 + d\delta\gamma = d\delta\gamma$ (using $dh = 0$ since $h$ harmonic is closed, and $d^2 = 0$).
> >
> > Now $\|\delta\gamma\|^2_{L^2} = \langle\delta\gamma, \delta\gamma\rangle_{L^2} = \langle\gamma, d\delta\gamma\rangle_{L^2}$ by the adjoint identity. From $d\delta\gamma = 0$, this gives $\|\delta\gamma\|^2 = 0$, hence $\delta\gamma = 0$.

> [!note]- Lemma 2: $\mathcal{H}^k \cap d\Omega^{k-1} = \{0\}$
> **Statement:** The intersection of harmonic forms and exact forms in $\Omega^k(M)$ is trivial.
>
> **Hint:** A harmonic form orthogonal to exact forms (by Hodge decomposition); only $0$ is in both.
>
> **Why needed:** Gives uniqueness of the harmonic representative.
>
> > [!note]- Full proof
> > Suppose $h \in \mathcal{H}^k$ and $h = d\eta$ for some $\eta \in \Omega^{k-1}$. By the adjoint identity, $\|h\|^2 = \langle h, d\eta\rangle = \langle\delta h, \eta\rangle = \langle 0, \eta\rangle = 0$ (using $\delta h = 0$ for $h$ harmonic). So $h = 0$.

> [!note]- Lemma 3: Existence of harmonic representative
> **Statement:** Every de Rham cohomology class $[\omega] \in H^k_{dR}(M)$ contains a harmonic representative.
>
> **Hint:** Take any closed form $\omega_0$ in the class, decompose via Hodge: $\omega_0 = h + d\alpha + \delta\gamma$. By Lemma 1, $\delta\gamma = 0$, so $\omega_0 = h + d\alpha$. Hence $[\omega_0] = [h]$.
>
> **Why needed:** Existence half of the isomorphism.
>
> > [!note]- Full proof
> > Let $\omega_0$ be any closed representative of $[\omega]$, so $d\omega_0 = 0$ and $[\omega_0] = [\omega]$. By the Hodge decomposition, $\omega_0 = h + d\alpha + \delta\gamma$ uniquely with $h \in \mathcal{H}^k$. By Lemma 1, $\delta\gamma = 0$, so $\omega_0 = h + d\alpha$. Taking cohomology classes: $[\omega] = [\omega_0] = [h + d\alpha] = [h] + [d\alpha] = [h] + 0 = [h]$. So $h$ is a harmonic representative of $[\omega]$.

> [!note]- Lemma 4: Uniqueness of harmonic representative
> **Statement:** Any two harmonic forms in the same de Rham cohomology class are equal.
>
> **Hint:** Their difference is harmonic and exact; apply Lemma 2.
>
> **Why needed:** Uniqueness half of the isomorphism.
>
> > [!note]- Full proof
> > Suppose $h_1, h_2 \in \mathcal{H}^k$ are both in the class $[\omega] \in H^k_{dR}$. Then $[h_1 - h_2] = 0$ in cohomology, so $h_1 - h_2 = d\eta$ for some $\eta \in \Omega^{k-1}$. Now $h_1 - h_2 \in \mathcal{H}^k$ (difference of harmonics is harmonic). So $h_1 - h_2 \in \mathcal{H}^k \cap d\Omega^{k-1} = \{0\}$ by Lemma 2. Hence $h_1 = h_2$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem (Hodge isomorphism).** Let $(M, g)$ be a closed oriented Riemannian $n$-manifold. The map $\iota : \mathcal{H}^k(M) \to H^k_{dR}(M)$, $h \mapsto [h]$, is an $\mathbb{R}$-linear isomorphism.
>
> *Proof.*
>
> **Step 0 — Well-posedness.** Every harmonic form $h \in \mathcal{H}^k(M)$ is closed (since $0 = \Delta h = d\delta h + \delta d h$; pairing with $h$ gives $\|dh\|^2 + \|\delta h\|^2 = 0$, so $dh = 0$ and $\delta h = 0$). So $h \in Z^k(M)$ and $[h] \in H^k_{dR}(M)$ is well-defined. $\mathbb{R}$-linearity is clear.
>
> **Step 1 — Surjectivity (existence of harmonic representative).** Let $[\omega] \in H^k_{dR}(M)$. Take any closed representative $\omega_0 \in Z^k$. By the Hodge decomposition theorem (applied to $\omega_0$):
> $$\omega_0 = h + d\alpha + \delta\gamma$$
> uniquely with $h \in \mathcal{H}^k$, $\alpha \in \Omega^{k-1}$, $\gamma \in \Omega^{k+1}$. Applying $d$:
> $$0 = d\omega_0 = dh + d^2\alpha + d\delta\gamma = 0 + 0 + d\delta\gamma = d\delta\gamma.$$
> Pairing $d\delta\gamma = 0$ with $\gamma$ using the adjoint identity:
> $$0 = \langle d\delta\gamma, \gamma\rangle_{L^2} = \langle\delta\gamma, \delta\gamma\rangle_{L^2} = \|\delta\gamma\|^2,$$
> so $\delta\gamma = 0$. Hence $\omega_0 = h + d\alpha$, and $[\omega] = [\omega_0] = [h] + [d\alpha] = [h] + 0 = [h]$. So $h \in \iota^{-1}([\omega])$, proving surjectivity.
>
> **Step 2 — Injectivity (uniqueness of harmonic representative).** Suppose $h_1, h_2 \in \mathcal{H}^k$ with $[h_1] = [h_2]$ in $H^k_{dR}$. Then $h_1 - h_2$ is exact: $h_1 - h_2 = d\eta$ for some $\eta \in \Omega^{k-1}$. But also $h_1 - h_2 \in \mathcal{H}^k$, so $h_1 - h_2 \in \mathcal{H}^k \cap d\Omega^{k-1}$.
>
> The intersection is trivial: if $h = d\eta$ is harmonic and exact, then by the adjoint identity $\|h\|^2_{L^2} = \langle h, d\eta\rangle_{L^2} = \langle\delta h, \eta\rangle_{L^2} = \langle 0, \eta\rangle = 0$ (using $\delta h = 0$). So $h = 0$. Hence $h_1 = h_2$.
>
> **Step 3 — Conclusion.** $\iota$ is a linear bijection $\mathcal{H}^k(M) \to H^k_{dR}(M)$, hence an isomorphism. In particular, $\dim\mathcal{H}^k(M) = \dim H^k_{dR}(M) = b_k(M)$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian geometry — harmonic forms on a torus.** On the flat $n$-torus $T^n = \mathbb{R}^n/\mathbb{Z}^n$, the harmonic $k$-forms are exactly the constant-coefficient $k$-forms $\sum c_I dx^I$, with $\binom{n}{k}$ independent parameters. The Hodge isomorphism gives $b_k(T^n) = \binom{n}{k}$, matching the topological computation via the Künneth formula. The exercise is to verify directly that constant-coefficient forms are harmonic, and that no other harmonic forms exist (by Fourier analysis on the torus).

**Complex / Kähler geometry — Hodge structure on a Kähler manifold.** On a compact Kähler manifold, the harmonic decomposition refines into $\mathcal{H}^k_d = \bigoplus_{p+q=k}\mathcal{H}^{p,q}_{\bar\partial}$ via the Kähler identities ($\Delta_d = 2\Delta_{\bar\partial}$). Applying the Hodge isomorphism on each side: $H^k(M; \mathbb{C}) = \bigoplus_{p+q=k}H^{p,q}(M)$, the **Hodge decomposition** of complex cohomology. The Hodge numbers $h^{p,q}$ satisfy Hodge symmetry $h^{p,q} = h^{q,p}$ — a constraint on the Kähler cohomology. The exercise: verify that the Kähler form $\omega$ on $\mathbb{CP}^m$ is harmonic and generates $H^{1,1}(\mathbb{CP}^m)$.

**Algebraic topology — Poincaré duality from harmonic forms.** The Hodge isomorphism plus the Hodge star $\star : \mathcal{H}^k \to \mathcal{H}^{n-k}$ (an isomorphism since $\Delta\star = \star\Delta$) gives Poincaré duality $H^k_{dR}\cong H^{n-k}_{dR}$ explicitly. The exercise: show that the integration pairing $H^k\times H^{n-k}\to\mathbb{R}$ is realized as the $L^2$ inner product of harmonic representatives via $\int_M\alpha\wedge\beta = \langle h_\alpha, \star^{-1}h_\beta\rangle$.

**Mathematical physics — vacuum solutions and ground states.** In quantum field theory on a Riemannian manifold $M$ viewed as Euclidean spacetime, the path integral concentrates on extremals of an action; for free $k$-form gauge theory (e.g., abelian Yang–Mills), the action is $\frac{1}{2}\int F\wedge\star F$ where $F = dA$, and the extremals modulo gauge transformations are exactly the harmonic forms. The dimension $\dim\mathcal{H}^k = b_k$ counts the **ground states** of the theory, and the Hodge isomorphism says these are exactly cohomology classes. This is the QFT interpretation of the Hodge isomorphism.

---

# Bridges

- **[[Thm - Hodge Decomposition Theorem|Hodge decomposition theorem]]** — this theorem is the direct corollary of the Hodge decomposition applied to closed forms. The decomposition's structural orthogonality is the key: closed forms have trivial coexact part in their decomposition, leaving harmonic plus exact, with the harmonic part canonically determined.

- **[[Thm - Poincare Duality via Hodge Star|Poincaré duality]]** — the Hodge isomorphism combined with the Hodge star $\star : \mathcal{H}^k\to\mathcal{H}^{n-k}$ gives the cohomological Poincaré duality $H^k_{dR}\cong H^{n-k}_{dR}$. The harmonic side carries the duality via $\star$; the cohomological side inherits it.

- **[[Thm - Bochner's Theorem|Bochner's theorem]]** — the Hodge isomorphism is the bridge between the Bochner technique (curvature analysis of harmonic forms) and topology (Betti numbers). Bochner's theorem says: positive Ricci curvature forces harmonic $1$-forms to vanish, and by the Hodge isomorphism this means $b_1 = 0$ — a topological obstruction derived from curvature.

- **The de Rham theorem** — the de Rham theorem identifies $H^k_{dR}(M; \mathbb{R})$ with the singular cohomology $H^k(M; \mathbb{R})$. Combining with the Hodge isomorphism, harmonic forms compute singular cohomology with real coefficients. This is the analytic realization of a topological invariant.

- **Spectral geometry — the dimension of the zero eigenspace** — the spectrum of $\Delta$ on $\Omega^k$ is a discrete set $0 = \lambda_0 < \lambda_1 \leq \lambda_2 \leq \dots \to \infty$, with multiplicity of $\lambda_0 = 0$ equal to $\dim\mathcal{H}^k = b_k$. The harmonic part is the zero eigenspace; the positive part of the spectrum encodes metric information. The Hodge isomorphism makes this multiplicity a topological invariant.

---

# Unlocked by This

> [!tip] Atiyah–Singer Index Theorem and Gauss–Bonnet–Chern *(from Index Theory)*
> The Hodge isomorphism is the engine of **the heat-kernel proof of the Atiyah–Singer index theorem**. Specifically, the **McKean–Singer formula** $\chi(M) = \mathrm{str}(e^{-t\Delta})$ (supertrace of the heat semigroup on $\Omega^\bullet$, time-independent) connects the Euler characteristic $\chi(M) = \sum_k(-1)^k b_k$ — a topological invariant — to the trace of $e^{-t\Delta}$ — an analytic object computable from the geometry. As $t\to\infty$ the heat semigroup projects onto harmonics; as $t\to 0$ it has a local expansion in curvature invariants. Equating the limits gives the **Gauss–Bonnet–Chern theorem** $\chi(M) = \int_M e(TM)$, with $e(TM)$ the Euler class (a polynomial in the Riemann curvature). This is the prototype of the Atiyah–Singer index theorem.

> [!tip] Bochner Technique and Curvature-Topology Inequalities *(from Geometric Analysis)*
> The Hodge isomorphism is what makes the **Bochner technique** produce *topological* conclusions from *geometric* hypotheses. Specifically: harmonic forms are determined by curvature (via the Weitzenböck formula), so dimensions of $\mathcal{H}^k$ are constrained by curvature; by the Hodge isomorphism, these are Betti numbers. The original **Bochner's theorem** is the simplest example. Generalizations include **Lichnerowicz's theorem** for harmonic spinors (using scalar curvature), **Kodaira vanishing** for holomorphic line bundles (using Hermitian curvature), and many more — all are "curvature-positivity kills harmonic objects" via Weitzenböck-style identities, then "harmonic objects represent cohomology" via Hodge-isomorphism arguments.

> [!tip] Spectral Geometry and Isospectrality *(from Geometric Analysis)*
> The spectrum of $\Delta$ on a closed Riemannian manifold encodes the dimension of $\mathcal{H}^k$ (multiplicity of eigenvalue $0$) plus all positive eigenvalues. By the Hodge isomorphism, the eigenvalue-$0$ multiplicity is *purely topological*. The **isospectral problem** asks whether two closed Riemannian manifolds with the same spectrum of $\Delta$ must be isometric — and the answer is no, with examples by Milnor ($16$-dimensional flat tori) and Sunada (construction of non-isometric isospectral hyperbolic surfaces). But the *topological invariants* (Betti numbers, Euler characteristic) are determined by the spectrum, by the Hodge isomorphism — so even though isospectral manifolds aren't isometric, they share topological invariants.
