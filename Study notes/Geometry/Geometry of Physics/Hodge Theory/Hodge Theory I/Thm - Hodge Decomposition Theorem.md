---
type: theorem
subject: hodge-theory
prereqs:
  - "Def - Hodge Laplacian"
  - "Def - Harmonic Form"
  - "Def - The Codifferential"
  - "Def - The L2 Inner Product on Differential Forms"
  - "Thm - Codifferential is the Adjoint of d"
  - "Def - Green Operator (Hodge)"
tags: [geometry, hodge-theory, elliptic-operators, cohomology]
---

# Notation

$(M, g)$ is a closed oriented Riemannian $n$-manifold. $\Omega^k(M)$ is the space of smooth $k$-forms; $L^2\Omega^k(M)$ its $L^2$ completion. $\mathcal{H}^k(M) = \ker(\Delta : \Omega^k \to \Omega^k)$ is the space of harmonic $k$-forms; $H : \Omega^k(M) \to \mathcal{H}^k(M)$ is the orthogonal projection; $G : \Omega^k(M) \to \Omega^k(M)$ is the [[Def - Green Operator (Hodge)|Green operator]]. The $L^2$ inner product is $\langle\cdot,\cdot\rangle_{L^2} = \int_M\langle\cdot,\cdot\rangle_g\operatorname{vol}_n$.

---

# Statement

> **Hodge Decomposition Theorem.** Let $(M, g)$ be a closed oriented Riemannian $n$-manifold. For each $k = 0, 1, \dots, n$:
> 1. The space $\mathcal{H}^k(M)$ of harmonic $k$-forms is finite-dimensional.
> 2. There is an $L^2$-orthogonal direct sum decomposition
> $$\Omega^k(M) = \mathcal{H}^k(M) \oplus d\Omega^{k-1}(M) \oplus \delta\Omega^{k+1}(M).$$
> Equivalently, every smooth $k$-form $\beta$ has a unique decomposition $\beta = h + d\alpha + \delta\gamma$ with $h \in \mathcal{H}^k(M)$, $\alpha \in \Omega^{k-1}(M)$, $\gamma \in \Omega^{k+1}(M)$, and the three summands are pairwise $L^2$-orthogonal.
> 3. The three summands $h$, $d\alpha$, $\delta\gamma$ are uniquely determined by $\beta$ (the forms $\alpha, \gamma$ themselves are not unique, but $d\alpha$ and $\delta\gamma$ are).
> 4. Poisson's equation $\Delta\beta = \rho$ has a solution iff $\rho \perp \mathcal{H}^k$, and the solution unique modulo $\mathcal{H}^k$ is given by $\beta = G\rho$.

> **Corollary (canonical harmonic representative).** Every de Rham cohomology class $[\omega] \in H^k_{dR}(M)$ contains a unique harmonic representative, namely $H\omega = \omega - d\delta G\omega$. This gives an isomorphism $\mathcal{H}^k(M) \cong H^k_{dR}(M)$.

---

# Motivation

The Hodge decomposition is the central structural theorem of the chapter. Its statement compresses a deep analytic result (the elliptic operator $\Delta$ has closed range with finite-dimensional kernel and cokernel) into a clean algebraic form: $\Omega^k$ is the orthogonal sum of three [[Def - Subspace|subspaces]] — the kernel of $\Delta$ (harmonics), and the images of $d$ and $\delta$ from neighboring degrees.

The decomposition matters because **it gives a canonical splitting of forms into algebraically meaningful pieces**. Given a general $k$-form $\beta$, we now have an unambiguous procedure: project onto $\mathcal{H}^k$ (the "cohomologically interesting" part), project onto $d\Omega^{k-1}$ (the "exact" part, with no cohomological content), project onto $\delta\Omega^{k+1}$ (the "coexact" part, also cohomologically trivial). Each summand has a clear interpretation, and the splitting is constructive via the Green operator: $\beta = H\beta + d\delta G\beta + \delta d G\beta$.

The most-used corollary is the **canonical harmonic representative**: every de Rham cohomology class has a unique form satisfying $\Delta\omega = 0$. This is the bridge between topology (cohomology, which is metric-independent) and analysis (elliptic PDEs, which are metric-dependent). The [[Def - Dimension|dimension]] $\dim\mathcal{H}^k = b_k$ is topological; the harmonic representative is metric-dependent, but for any given metric there is exactly one. This is what enables **spectral geometry** (extracting topological invariants from the spectrum of $\Delta$), **the heat-kernel approach to the Atiyah–Singer index theorem** (computing $\chi(M) = \sum_k(-1)^k\dim\mathcal{H}^k$ from heat-kernel asymptotics), and **the Bochner technique** (constraining $\dim\mathcal{H}^k$ from curvature conditions).

The deeper structural point is that **the decomposition holds because $\Delta$ is elliptic and $M$ is closed**. Both conditions are essential: the Riemannian (rather than Lorentzian) hypothesis is what makes $\Delta$ elliptic; the closed (compact, boundary-free) hypothesis is what makes the cokernel of $\Delta$ finite-dimensional. On a noncompact manifold or one with boundary, the decomposition fails (or requires modification with boundary conditions and reduced cohomology).

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is: closed oriented Riemannian manifold, and a $k$-form $\beta$. Several non-obvious sources of "I should apply the Hodge decomposition" arise in practice.

The most common source is **a general $k$-form whose harmonic / exact / coexact parts are of interest**. Property $B$: a smooth form $\beta \in \Omega^k(M)$ with no a priori special properties. The bridge is that the Hodge decomposition $\beta = h + d\alpha + \delta\gamma$ always exists and is unique — so any question about "what is the closed / exact / coclosed / coexact part of $\beta$" is answered by computing the projection. Example: in fluid dynamics on a closed Riemannian manifold, decomposing a velocity field $\vec v$ (a $1$-form) into its irrotational part ($d\phi$ for a scalar potential), divergence-free part ($\delta\vec A$ for a $2$-form potential), and harmonic part (the "topologically nontrivial" residue). This is the **Helmholtz decomposition** generalized to closed Riemannian manifolds.

A second source is **a closed form whose harmonic representative is sought**. Property $B$: $\beta \in Z^k(M)$ (closed). The bridge to the Hodge decomposition: any closed form $\beta$ decomposes as $\beta = h + d\alpha + \delta\gamma$, but closedness forces $d\delta\gamma = 0$, then pairing with $\delta\gamma$ gives $\|d\delta\gamma\|\cdot\|\delta\gamma\| \geq 0 \Rightarrow \langle\delta\gamma,\delta\gamma\rangle = \langle d\delta\gamma,\gamma\rangle = 0$, so $\delta\gamma = 0$. Hence $\beta = h + d\alpha$: the harmonic representative $h$ is uniquely identified as the harmonic projection $H\beta$.

A third source is **solving Poisson's equation $\Delta\beta = \rho$**. Property $B$: a PDE of this form with $\rho \in \Omega^k(M)$ given. The bridge is the Fredholm alternative (point 4 of the theorem): the equation has a solution iff $\rho\perp\mathcal{H}^k$, and the unique solution orthogonal to $\mathcal{H}^k$ is $\beta = G\rho$. This is the standard route for solving Laplacian-type PDEs on closed Riemannian manifolds — the obstruction is finite-dimensional (the harmonics), and the solution operator is the Green operator.

A fourth source is **a problem on the cohomology side that needs concrete forms**. Property $B$: a question about $H^k_{dR}(M)$ — its dimension, a particular cohomology class, the cup product structure. The bridge is the isomorphism $\mathcal{H}^k\cong H^k_{dR}$: cohomology classes correspond to harmonic forms, and once we are working with harmonic forms, we have *concrete* objects (forms satisfying a PDE) rather than equivalence classes. Example: computing the cup product structure of $H^*(M)$ reduces to computing wedge products of harmonic forms and projecting onto harmonics — much more tractable than working with abstract cohomology classes.

**Targets (Output Amplification)**

The conclusion is an orthogonal decomposition $\Omega^k = \mathcal{H}^k\oplus d\Omega^{k-1}\oplus\delta\Omega^{k+1}$. Combined with other facts, this produces several powerful results.

The most powerful combination is **decomposition plus $\dim\mathcal{H}^k = b_k$ gives the Hodge isomorphism**. The decomposition's harmonic summand is exactly the orthogonal complement of $d\Omega^{k-1}\oplus\delta\Omega^{k+1}$, which contains the exact forms; the quotient $Z^k(M)/B^k(M) = H^k_{dR}(M)$ then has a unique harmonic representative in each class, giving the isomorphism $\mathcal{H}^k\cong H^k_{dR}$. The combination is non-obvious because it requires both the orthogonality (analytic) and the cohomology characterization (topological); together they identify a topological invariant ($b_k$) with the dimension of a PDE-solution space.

A second combination is **decomposition plus $\star$-commutation gives Poincaré duality**. The Hodge star $\star$ commutes with $\Delta$, hence maps $\mathcal{H}^k$ bijectively to $\mathcal{H}^{n-k}$. Combined with the isomorphism $\mathcal{H}^k\cong H^k_{dR}$, this gives $H^k_{dR}\cong H^{n-k}_{dR}$ — **Poincaré duality** on a closed orientable manifold. The combination is non-obvious because $\star$ is metric-dependent but the resulting cohomological isomorphism is topologically intrinsic (the same isomorphism holds for any metric).

A third combination is **decomposition plus heat-flow gives the harmonic projection as a long-time limit**. The heat semigroup $e^{-t\Delta}$ on $L^2\Omega^k$ converges as $t\to\infty$ to the harmonic projection $H$ (in the $L^2$ sense). So the heat flow decomposes any form into its harmonic part (the equilibrium) and a transient part decaying exponentially. This is the dynamical realization of the Hodge decomposition: the harmonic summand is the *attractor* of the form-heat-equation.

A fourth combination is **decomposition plus Weitzenböck inequality gives Bochner-type vanishing theorems**. Take a harmonic $1$-form $h$, expand $\langle\Delta h, h\rangle = \|d h\|^2 + \|\delta h\|^2 = 0$ via the Hodge decomposition characterization, and combine with the Weitzenböck formula $\Delta = \nabla^*\nabla + \operatorname{Ric}$ — integrating gives $\|\nabla h\|^2 + \int\operatorname{Ric}(h,h) = 0$. Positive Ricci forces $h\equiv 0$. The combination is non-obvious because it requires both the cohomological characterization (harmonic forms represent $H^1$) and the curvature identity (Weitzenböck); together they produce a curvature-Betti inequality, **Bochner's theorem**.

---

# Why Is It True

The proof is genuinely deep — it requires the full theory of elliptic operators on closed manifolds. Three structural facts conspire.

**Fact 1: $\Delta$ is elliptic.** The [[Def - Hodge Laplacian|Hodge Laplacian]] on a Riemannian manifold has principal symbol $|\xi|_g^2\cdot\mathrm{id}_{\Lambda^k}$ at a covector $\xi$, which is invertible for $\xi \neq 0$. Ellipticity is a local condition on the symbol, but it has dramatic consequences on a closed manifold via the elliptic regularity theory.

**Fact 2: $\Delta$ has closed range with finite-dimensional kernel and cokernel (the Fredholm property on a closed manifold).** This is a deep theorem in PDE — the **Fredholm alternative for elliptic operators on closed manifolds**. The argument uses a parametrix construction (or heat-kernel methods, or the Lax–Milgram approach in Sobolev spaces) to show that the elliptic operator $\Delta$ on the Hilbert space $L^2\Omega^k(M)$ is Fredholm: its kernel is finite-dimensional, its range is closed, and its cokernel is finite-dimensional. The cokernel is canonically identified with the kernel of the adjoint $\Delta^* = \Delta$ (self-adjoint), so kernel = cokernel = $\mathcal{H}^k$.

**Fact 3: Self-adjointness gives orthogonal complement = range.** For a self-adjoint Fredholm operator $\Delta$ on a Hilbert space, $L^2\Omega^k = \ker\Delta\oplus\operatorname{ran}\Delta$ orthogonally. So $L^2\Omega^k = \mathcal{H}^k\oplus\Delta(L^2\Omega^k)$. The range $\Delta(L^2\Omega^k) = (d\delta + \delta d)(L^2\Omega^k) = d\delta(L^2\Omega^k) + \delta d(L^2\Omega^k) \subseteq dL^2\Omega^{k-1} + \delta L^2\Omega^{k+1}$. With more work (using the orthogonality and closure properties), this is shown to equal the full $L^2$-closure of $d\Omega^{k-1} + \delta\Omega^{k+1}$. Smoothness propagation via elliptic regularity then gives the smooth Hodge decomposition from the $L^2$ version.

**The one-line mechanism summary:** **the Hodge decomposition is the orthogonal complement decomposition of $L^2\Omega^k$ relative to the self-adjoint elliptic operator $\Delta$, with the kernel being the harmonics and the range being the exact-plus-coexact forms.**

The deeper structural reason: **the Hodge decomposition is an instance of the spectral theorem for compact self-adjoint operators**. The Green operator $G$ is the inverse of $\Delta$ on the orthogonal complement of $\mathcal{H}^k$ and is *compact* on $L^2\Omega^k$ (since $\Delta$ has compact resolvent on a closed manifold). The spectral theorem for compact self-adjoint operators gives an orthonormal eigenbasis with eigenvalues decreasing to $0$; the eigenvalue-$0$ eigenspace is $\mathcal{H}^k$, and the rest is the range. This is the analytic backbone.

---

# What Makes This Hard

The conceptual content is clear, but the proof requires nontrivial PDE theory. Three places trip up most students.

**The Fredholm property requires elliptic regularity.** The hardest step is showing that the range of $\Delta$ is closed in $L^2$. The naive "image of bounded operator" is not closed in general; for closed range we need the elliptic estimate $\|\omega\|_{H^2} \leq C(\|\Delta\omega\|_{L^2} + \|\omega\|_{L^2})$, which is a deep result requiring Sobolev embedding and parametrix theory. Without this estimate, the closed-range property fails, and the orthogonal direct sum decomposition has to be replaced by a non-orthogonal "$L^2$-closure" formulation.

**Smoothness propagation needs elliptic regularity.** Solving the $L^2$ Hodge decomposition gives $L^2$ summands; to recover the *smooth* Hodge decomposition we need that the harmonic part of a smooth form is smooth (which is elliptic regularity for $\Delta$: if $\Delta\omega = 0$ and $\omega \in L^2$, then $\omega \in C^\infty$). This is what makes the smooth and $L^2$ versions of the theorem agree.

**The closed-manifold hypothesis is essential.** On a noncompact manifold, $\Delta$ may not have closed range, and the simple orthogonal decomposition fails. The fix is reduced $L^2$-cohomology, where one replaces the image of $d$ with its $L^2$-closure, and computes a modified Hodge decomposition. This is the **$L^2$-Hodge theory** of Atiyah and others, used for example in **$L^2$-Betti numbers** of manifolds covered by infinite [[Def - Group|groups]].

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
The decomposition follows from the spectral theory of the self-adjoint elliptic operator $\Delta$ on a closed Riemannian manifold. The key analytic fact is that $\Delta$ is Fredholm: it has closed range with finite-dimensional kernel and cokernel. Self-adjointness identifies kernel and cokernel, giving the orthogonal direct sum $L^2\Omega^k = \ker\Delta \oplus \operatorname{ran}\Delta$. The range $\operatorname{ran}\Delta = d\delta(L^2\Omega^k) + \delta d(L^2\Omega^k) \subseteq dL^2\Omega^{k-1} + \delta L^2\Omega^{k+1}$, and orthogonality plus the smooth approximation argument upgrade this to the smooth decomposition.

**Subgoal decomposition:**

1. **$\Delta$ is elliptic and self-adjoint.** Compute the principal symbol, verify positivity; verify self-adjointness from the [[Def - The Codifferential|codifferential]] adjoint property.
   - *Hint:* The principal symbol of $\Delta = d\delta + \delta d$ at $\xi$ is the principal symbol of $\delta\circ d + d\circ\delta$, which on $\Lambda^k$ is $|\xi|^2\mathrm{id}$. Self-adjointness is from [[Thm - Codifferential is the Adjoint of d]] applied twice.
   - *Why needed:* Ellipticity gives the Fredholm property; self-adjointness gives the orthogonal complement decomposition.

2. **$\Delta$ has finite-dimensional kernel on a closed manifold.** Apply the **elliptic regularity theorem** for $\Delta$ on a closed manifold.
   - *Hint:* The kernel of an elliptic operator on a closed manifold is finite-dimensional. This is the deep PDE input.
   - *Why needed:* $\dim\mathcal{H}^k < \infty$ is what makes the harmonic projection well-defined and the cohomology computable.

3. **$\Delta$ has closed range on $L^2$.** Apply the **closed-range theorem** for elliptic operators on closed manifolds.
   - *Hint:* This is the elliptic estimate $\|\omega\|_{H^2} \leq C(\|\Delta\omega\|_{L^2} + \|\omega\|_{L^2})$, combined with the Fredholm theorem.
   - *Why needed:* Closed range is what makes the orthogonal complement of $\ker\Delta$ equal to the range, giving the direct sum decomposition.

4. **$L^2\Omega^k = \mathcal{H}^k \oplus \overline{\operatorname{ran}}\Delta$ (Hilbert space orthogonal decomposition).** By self-adjointness, the orthogonal complement of $\ker\Delta$ equals $\overline{\operatorname{ran}}\Delta$. By closed range, $\overline{\operatorname{ran}}\Delta = \operatorname{ran}\Delta$.
   - *Hint:* For a bounded self-adjoint operator $T$ on a Hilbert space, $(\ker T)^\perp = \overline{\operatorname{ran}} T$. With closed range, $\overline{\operatorname{ran}} = \operatorname{ran}$.
   - *Why needed:* Gives the $L^2$-orthogonal decomposition.

5. **Identify $\operatorname{ran}\Delta$ with $d\Omega^{k-1} + \delta\Omega^{k+1}$.** $\Delta = d\delta + \delta d$, so $\operatorname{ran}\Delta \subseteq dL^2\Omega^{k-1} + \delta L^2\Omega^{k+1}$. The other direction uses the orthogonal complement argument.
   - *Hint:* If $\omega = d\eta$ is exact (so $\eta = \delta G\zeta$ for some $\zeta$), then $\omega = d\delta G\zeta = (\Delta - \delta d)G\zeta = $ harmonic-free piece + coexact piece. With more care, $d\Omega^{k-1} + \delta\Omega^{k+1} \subseteq \operatorname{ran}\Delta$.
   - *Why needed:* Identifies the range of $\Delta$ with the exact-plus-coexact subspace, completing the algebraic identification.

6. **$d\Omega^{k-1}$ and $\delta\Omega^{k+1}$ are $L^2$-orthogonal.** Show $\langle d\alpha, \delta\gamma\rangle = 0$ for all $\alpha, \gamma$.
   - *Hint:* $\langle d\alpha, \delta\gamma\rangle = \langle d^2\alpha, \gamma\rangle = 0$ by $d^2 = 0$ and adjointness.
   - *Why needed:* Makes the direct sum *orthogonal*, not just direct.

7. **Smoothness propagation.** If $\beta$ is smooth, the summands $h$, $d\alpha$, $\delta\gamma$ are smooth.
   - *Hint:* $h = H\beta$ is harmonic, hence smooth by elliptic regularity. Then $d\alpha + \delta\gamma = \beta - h$ is smooth. The individual pieces $d\alpha$ and $\delta\gamma$ are determined by orthogonality and are smooth.
   - *Why needed:* Upgrades the $L^2$ decomposition to a smooth one.

8. **(Corollary) Canonical harmonic representative.** For a closed $\beta$, the Hodge decomposition gives $\beta = h + d\alpha + \delta\gamma$, but closedness $d\beta = 0$ forces $d\delta\gamma = 0$, then $\|\delta\gamma\|^2 = \langle d\delta\gamma,\gamma\rangle = 0$, so $\delta\gamma = 0$. Hence $\beta = h + d\alpha$, and $h$ is the unique harmonic representative of $[\beta]$.
   - *Why needed:* The most-used corollary, identifying $\mathcal{H}^k\cong H^k_{dR}$.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\Delta$ is elliptic with principal symbol $|\xi|^2\mathrm{id}$
> **Statement:** The Hodge Laplacian $\Delta : \Omega^k(M) \to \Omega^k(M)$ on a Riemannian manifold is a second-order elliptic differential operator with principal symbol $\sigma_2(\Delta)(\xi) = |\xi|_g^2\,\mathrm{id}_{\Lambda^k T_p^*M}$ at a covector $\xi \in T_p^*M$.
>
> **Hint:** The principal symbol of $\delta$ is the contraction with $\xi$ (interior product); the principal symbol of $d$ is the wedge with $\xi$ (exterior product). The composition is $\iota_\xi\circ(\xi\wedge\cdot) + (\xi\wedge\cdot)\circ\iota_\xi$, which on $\Lambda^k$ is $|\xi|^2\mathrm{id}$ by a Clifford-algebra identity.
>
> **Why needed:** Ellipticity is the local PDE condition that gives the Fredholm property on a closed manifold.
>
> > [!note]- Full proof
> > The principal symbol of $d : \Omega^k \to \Omega^{k+1}$ at $\xi$ is $\sigma_1(d)(\xi) = i\xi\wedge\cdot : \Lambda^k T_p^*M \to \Lambda^{k+1}T_p^*M$ (the imaginary unit appears in some conventions; we drop it here for clarity, working with the leading-term polynomial). The principal symbol of $\delta : \Omega^k \to \Omega^{k-1}$ at $\xi$ is $\sigma_1(\delta)(\xi) = -\iota_{\xi^\sharp}$ (where $\xi^\sharp$ is the vector dual of the covector $\xi$). Composing:
> > $\sigma_2(d\delta)(\xi) = (\xi\wedge\cdot)\circ(-\iota_{\xi^\sharp}) = -\xi\wedge\iota_{\xi^\sharp}$;
> > $\sigma_2(\delta d)(\xi) = (-\iota_{\xi^\sharp})\circ(\xi\wedge\cdot) = -\iota_{\xi^\sharp}\circ(\xi\wedge\cdot)$.
> > Their sum: $\sigma_2(\Delta)(\xi) = -(\xi\wedge\iota_{\xi^\sharp} + \iota_{\xi^\sharp}\circ\xi\wedge)$. Using the Cartan magic formula in its Clifford-algebra version (the operators $\xi\wedge$ and $\iota_{\xi^\sharp}$ generate a Clifford algebra with relation $\{a, b\} = -2g(a, b)$), the anticommutator on $\Lambda^k$ gives $|\xi|_g^2\mathrm{id}_{\Lambda^k}$ (with the appropriate sign). So $\sigma_2(\Delta)(\xi) = |\xi|_g^2\,\mathrm{id}$, invertible for $\xi \neq 0$ — $\Delta$ is elliptic.

> [!note]- Lemma 2: $\Delta$ is Fredholm on a closed manifold
> **Statement:** On a closed Riemannian manifold, $\Delta : L^2\Omega^k(M) \to L^2\Omega^k(M)$ (with appropriate domain in Sobolev spaces) is a Fredholm operator: its kernel and cokernel are both finite-dimensional, and its range is closed.
>
> **Hint:** Apply the **elliptic regularity theorem** (Atiyah, Singer; Warner Chapter 6): any elliptic operator on a closed manifold is Fredholm. The kernel and cokernel are identified via self-adjointness.
>
> **Why needed:** Provides the analytic backbone for the decomposition.
>
> > [!note]- Full proof (sketch)
> > The proof uses the **parametrix construction**: build an operator $Q : L^2 \to L^2$ that is approximately inverse to $\Delta$, with the "error terms" $\mathrm{id} - Q\Delta$ and $\mathrm{id} - \Delta Q$ being compact operators (smoothing operators of order $-\infty$ have compact restriction to $L^2$). The existence of such a $Q$ is the content of elliptic operator theory, requiring the principal symbol to be invertible (which we have by Lemma 1).
> >
> > Once $Q$ is constructed, the Fredholm property follows: $\ker\Delta \subseteq \ker(\mathrm{id} - Q\Delta) + \ker Q$… in fact more carefully, $\Delta$ being elliptic with parametrix is equivalent to $\Delta$ being Fredholm modulo compact operators, and by spectral theory of compact operators its actual kernel and cokernel are finite-dimensional, and its range is closed.

> [!note]- Lemma 3: Hilbert-space orthogonal decomposition for self-adjoint Fredholm operators
> **Statement:** For a self-adjoint Fredholm operator $T$ on a Hilbert space $\mathcal{H}$, $\mathcal{H} = \ker T \oplus \operatorname{ran} T$ as an orthogonal direct sum.
>
> **Hint:** For a bounded self-adjoint operator $T$, $(\ker T)^\perp = \overline{\operatorname{ran} T}$. The Fredholm property gives $\operatorname{ran} T$ closed, so $\overline{\operatorname{ran} T} = \operatorname{ran} T$. The two summands $\ker T$ and $\operatorname{ran} T$ are orthogonal complements, hence direct.
>
> **Why needed:** Provides the $L^2$ orthogonal direct sum $L^2\Omega^k = \mathcal{H}^k\oplus\operatorname{ran}\Delta$.
>
> > [!note]- Full proof
> > For any self-adjoint $T$ (bounded or unbounded with appropriate domain), $\ker T \perp \operatorname{ran} T$: if $v \in \ker T$ and $w = Tu \in \operatorname{ran} T$, then $\langle v, w\rangle = \langle v, Tu\rangle = \langle Tv, u\rangle = \langle 0, u\rangle = 0$. So $\ker T \subseteq (\operatorname{ran} T)^\perp$.
> >
> > For the reverse: $(\operatorname{ran} T)^\perp = \{v : \langle v, Tu\rangle = 0\, \forall u\} = \{v : \langle Tv, u\rangle = 0\, \forall u\} = \{v : Tv = 0\} = \ker T$. So $\ker T = (\operatorname{ran} T)^\perp$, equivalently $\mathcal{H} = \ker T \oplus \overline{\operatorname{ran} T}$.
> >
> > With $\operatorname{ran} T$ closed (Fredholm), $\overline{\operatorname{ran} T} = \operatorname{ran} T$, giving the orthogonal direct sum.

> [!note]- Lemma 4: $\operatorname{ran}\Delta = dL^2\Omega^{k-1} \oplus \delta L^2\Omega^{k+1}$
> **Statement:** $\operatorname{ran}(\Delta : L^2\Omega^k \to L^2\Omega^k) = dL^2\Omega^{k-1} \oplus \delta L^2\Omega^{k+1}$ as an orthogonal direct sum.
>
> **Hint:** $\Delta = d\delta + \delta d$, so $\operatorname{ran}\Delta \subseteq dL^2\Omega^{k-1} + \delta L^2\Omega^{k+1}$. For the reverse: if $\omega = d\alpha + \delta\gamma$, then $\omega = \Delta(\delta G\omega) + \Delta(d G\omega)$ when $\omega \perp \mathcal{H}^k$ (using the fundamental identity $\Delta G = \mathrm{id} - H$). Orthogonality of $d\Omega^{k-1}$ and $\delta\Omega^{k+1}$ follows from $\langle d\alpha, \delta\gamma\rangle = \langle d^2\alpha, \gamma\rangle = 0$.
>
> **Why needed:** Identifies the range of $\Delta$ with the exact-plus-coexact subspace, the structural content of the Hodge decomposition.
>
> > [!note]- Full proof
> > **One containment:** $\Delta = d\delta + \delta d$, so for any $\omega \in L^2\Omega^k$, $\Delta\omega = d(\delta\omega) + \delta(d\omega) \in dL^2\Omega^{k-1} + \delta L^2\Omega^{k+1}$. Hence $\operatorname{ran}\Delta \subseteq dL^2\Omega^{k-1} + \delta L^2\Omega^{k+1}$.
> >
> > **Reverse containment:** Take $\omega = d\alpha + \delta\gamma$. Decompose orthogonally: $\omega \perp \mathcal{H}^k$ since $\langle\omega, h\rangle = \langle d\alpha, h\rangle + \langle\delta\gamma, h\rangle = \langle\alpha, \delta h\rangle + \langle\gamma, dh\rangle = 0$ for $h$ harmonic. By the orthogonal decomposition of Lemma 3, $\omega \in \operatorname{ran}\Delta$.
> >
> > **Orthogonality:** $\langle d\alpha, \delta\gamma\rangle_{L^2} = \langle d^2\alpha, \gamma\rangle_{L^2} = \langle 0, \gamma\rangle = 0$, using $d^2 = 0$ and the adjoint identity.
> >
> > Hence $\operatorname{ran}\Delta = d\Omega^{k-1}\oplus\delta\Omega^{k+1}$ orthogonally.

> [!note]- Lemma 5: Elliptic regularity gives smoothness propagation
> **Statement:** If $\Delta\omega = \rho$ with $\rho$ smooth and $\omega \in L^2$, then $\omega$ is smooth. In particular, $\mathcal{H}^k(M) = \ker\Delta \cap L^2\Omega^k$ consists of smooth forms.
>
> **Hint:** Elliptic operators "gain regularity" — solutions have one more derivative than the right side, plus the same regularity bootstrap (Sobolev space methods).
>
> **Why needed:** Upgrades the $L^2$ Hodge decomposition to a smooth one, recovering the original smooth statement of the theorem.
>
> > [!note]- Full proof (sketch)
> > By the elliptic estimate $\|\omega\|_{H^{s+2}} \leq C(\|\Delta\omega\|_{H^s} + \|\omega\|_{L^2})$ for any $s \geq 0$, if $\Delta\omega = \rho$ with $\rho \in H^s$ then $\omega \in H^{s+2}$. Iterating, if $\rho$ is smooth ($\rho \in H^s$ for all $s$), then $\omega \in H^{s+2}$ for all $s$, hence $\omega \in C^\infty$ by Sobolev embedding ($H^s \subset C^k$ for $s > k + n/2$).
> >
> > In particular, with $\rho = 0$: harmonic $L^2$ forms are smooth.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** As stated.
>
> *Proof.* Let $(M, g)$ be a closed oriented Riemannian $n$-manifold.
>
> **Step 0 — Well-posedness.** The Hodge Laplacian $\Delta = d\delta + \delta d : \Omega^k(M) \to \Omega^k(M)$ is well-defined for any $k \in \{0, 1, \dots, n\}$, with $\delta : \Omega^0 \to \Omega^{-1} = 0$ and $d : \Omega^n \to \Omega^{n+1} = 0$ by convention. The extension to $L^2$ uses the Friedrichs extension via the closed quadratic form $\omega \mapsto \langle\Delta\omega, \omega\rangle = \|d\omega\|^2 + \|\delta\omega\|^2$ on the Sobolev space $H^2\Omega^k(M)$.
>
> **Step 1.** By Lemma 1, $\Delta$ is elliptic with principal symbol $|\xi|^2\mathrm{id}$.
>
> **Step 2.** By Lemma 2 (elliptic regularity / parametrix construction on closed manifolds), $\Delta$ is Fredholm: $\dim\ker\Delta < \infty$, $\operatorname{ran}\Delta$ is closed in $L^2$, and $\dim\mathrm{coker}\,\Delta < \infty$. Combined with self-adjointness (from [[Thm - Codifferential is the Adjoint of d]]), $\dim\ker\Delta = \dim\mathrm{coker}\,\Delta$.
>
> **Step 3.** By Lemma 3 (Hilbert-space orthogonality for self-adjoint Fredholm operators), $L^2\Omega^k(M) = \ker\Delta \oplus \operatorname{ran}\Delta$ orthogonally. The kernel is $\mathcal{H}^k(M)$, finite-dimensional.
>
> **Step 4.** By Lemma 4, $\operatorname{ran}\Delta = dL^2\Omega^{k-1}\oplus\delta L^2\Omega^{k+1}$ orthogonally. Combining with Step 3:
> $$L^2\Omega^k(M) = \mathcal{H}^k(M) \oplus dL^2\Omega^{k-1}(M) \oplus \delta L^2\Omega^{k+1}(M)$$
> orthogonally.
>
> **Step 5.** Smoothness propagation (Lemma 5): if $\beta \in \Omega^k(M)$ is smooth, then $H\beta$ is smooth (kernel elements are smooth by elliptic regularity), so $\beta - H\beta = d\alpha + \delta\gamma$ is smooth. The individual summands $d\alpha$ and $\delta\gamma$ are determined orthogonally and are smooth: $d\alpha = d(\delta G\beta) = d\delta G\beta$, $\delta\gamma = \delta(d G\beta) = \delta d G\beta$, both smooth by elliptic regularity applied to $G\beta$.
>
> **Step 6.** Restricting to smooth forms:
> $$\Omega^k(M) = \mathcal{H}^k(M) \oplus d\Omega^{k-1}(M) \oplus \delta\Omega^{k+1}(M),$$
> as an $L^2$-orthogonal direct sum of subspaces of smooth forms.
>
> **Step 7 (Uniqueness of summands).** If $h_1 + d\alpha_1 + \delta\gamma_1 = h_2 + d\alpha_2 + \delta\gamma_2$, then $(h_1 - h_2) + d(\alpha_1 - \alpha_2) + \delta(\gamma_1 - \gamma_2) = 0$. Pairing with $h_1 - h_2$ and using orthogonality: $\|h_1 - h_2\|^2 = 0$, so $h_1 = h_2$. Similarly $d(\alpha_1 - \alpha_2) = 0 = \delta(\gamma_1 - \gamma_2)$. So the summands $h$, $d\alpha$, $\delta\gamma$ are unique (the forms $\alpha, \gamma$ themselves are not — they are determined up to closed / coclosed shifts).
>
> **Step 8 (Poisson's equation).** $\Delta\beta = \rho$ has a solution iff $\rho \in \operatorname{ran}\Delta$, equivalently $\rho \perp \mathcal{H}^k$. The unique solution orthogonal to $\mathcal{H}^k$ is $\beta = G\rho$, by definition of the Green operator.
>
> **Step 9 (Canonical harmonic representative).** For $\beta$ closed (so $d\beta = 0$), the Hodge decomposition gives $\beta = h + d\alpha + \delta\gamma$. Closedness: $0 = d\beta = d^2\alpha + d\delta\gamma = d\delta\gamma$. Pairing: $0 = \langle d\delta\gamma, \gamma\rangle = \langle\delta\gamma, \delta\gamma\rangle = \|\delta\gamma\|^2$, so $\delta\gamma = 0$. Hence $\beta = h + d\alpha$ — the harmonic representative $h \in \mathcal{H}^k$ is unique. The map $\mathcal{H}^k \to H^k_{dR}$, $h \mapsto [h]$, is a bijection. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian geometry — Helmholtz decomposition on a closed surface.** On a closed orientable surface $\Sigma_g$ of genus $g$ with a Riemannian metric, decompose an arbitrary smooth vector field (= $1$-form via the musical isomorphism) into its gradient, curl, and harmonic parts. The gradient part is $d\phi$ for a scalar potential $\phi$ (unique up to constants); the curl part is $\delta(\eta\operatorname{vol}_g)$ for a $2$-form (unique up to constant multiples of $\operatorname{vol}_g$); the harmonic part is $h \in \mathcal{H}^1(\Sigma_g)$, with $\dim\mathcal{H}^1 = 2g$. The Helmholtz decomposition on a closed surface is the $n = 2$, $k = 1$ instance of Hodge.

**Complex geometry — Dolbeault Hodge decomposition.** On a compact Kähler manifold, the Dolbeault complex $\Omega^{p,q}(M)$ with $\bar\partial$ has its own Hodge decomposition: $\Omega^{p,q} = \mathcal{H}^{p,q}_{\bar\partial} \oplus \bar\partial\Omega^{p,q-1} \oplus \bar\partial^*\Omega^{p,q+1}$. The harmonic part represents the Dolbeault cohomology $H^{p,q}_{\bar\partial}(M)$. On a compact Kähler manifold, by the Kähler identities, $\Delta_d = 2\Delta_\partial = 2\Delta_{\bar\partial}$, so the de Rham Hodge decomposition refines into the Dolbeault Hodge decomposition: $\mathcal{H}^k_d = \bigoplus_{p+q=k}\mathcal{H}^{p,q}_{\bar\partial}$. This is the foundational result of complex Hodge theory.

**PDE theory — Poisson equation on a closed manifold.** Solve $\Delta f = \rho$ for a function $f$ on a closed Riemannian manifold, where $\rho$ is a given smooth function. Hodge decomposition gives: the equation has a solution iff $\int_M\rho\operatorname{vol}_g = 0$ (orthogonality to constants, the kernel of $\Delta$ on functions). The unique mean-zero solution is $f = G\rho$. The classical Euclidean version "solve $\nabla^2 u = \rho$ on a bounded domain" is the bounded-domain analog, with additional boundary conditions.

**Electromagnetism — gauge fixing.** In source-free electromagnetism on a closed Lorentzian (or Wick-rotated to Riemannian) $4$-manifold, the electromagnetic potential $A$ is a $1$-form with $F = dA$. Gauge transformations $A \to A + d\chi$ leave $F$ invariant. The **Coulomb gauge** condition $\delta A = 0$ picks out a unique representative in each gauge equivalence class (modulo harmonic $1$-forms, which are gauge-equivalent to themselves). The Hodge decomposition $A = h + d\chi + \delta\gamma$ allows the Coulomb-gauge fixing: replace $A$ by $A - d\chi = h + \delta\gamma$, which has $\delta(A - d\chi) = \delta h + \delta^2\gamma = 0$ since $\delta h = 0$ (harmonic) and $\delta^2 = 0$.

---

# Bridges

- **[[Thm - Harmonic Forms Represent de Rham Cohomology|Harmonic representatives of cohomology]]** — the corollary of the Hodge decomposition for closed forms gives the canonical harmonic representative in each de Rham class. The bridge is the orthogonality of the decomposition: a closed form's decomposition has $\delta\gamma = 0$, leaving just the harmonic part and an exact correction. The harmonic representative is the unique form in the class with minimum $L^2$ norm.

- **[[Thm - Poincare Duality via Hodge Star|Poincaré duality]]** — the Hodge star $\star : \mathcal{H}^k\to\mathcal{H}^{n-k}$ is an isomorphism (since $\star$ commutes with $\Delta$), and through the Hodge isomorphism this gives the cohomological Poincaré duality $H^k\cong H^{n-k}$. The bridge from Hodge theory to Poincaré duality is: the decomposition's harmonic summand carries the duality via $\star$, and the cohomology identification carries it forward.

- **Heat semigroup and harmonic projection** — the heat semigroup $e^{-t\Delta}$ on $L^2\Omega^k$ converges as $t\to\infty$ to the harmonic projection $H$: $\lim_{t\to\infty}\|e^{-t\Delta}\omega - H\omega\|_{L^2} = 0$ for any $\omega \in L^2$. The Green operator can be reconstructed as $G = \int_0^\infty (e^{-t\Delta} - H)dt$. This dynamical realization of the Hodge decomposition is the foundation for the **heat-kernel proof of the Atiyah–Singer index theorem**.

- **Sobolev space framework** — the smooth Hodge decomposition is recovered from the $L^2$ version via elliptic regularity: $L^2$-harmonic forms are smooth. More generally, the decomposition holds in any Sobolev space $H^s\Omega^k(M)$ with the summands being closed in the $H^s$ norm. This is the basis for **Sobolev Hodge theory** and the analytic study of gauge connections.

- **[[Def - Green Operator (Hodge)|Green operator]]** — the Green operator $G$ is the operator that *constructs* the Hodge decomposition: $\beta = H\beta + d\delta G\beta + \delta d G\beta$. The fundamental identity $\Delta G + H = \mathrm{id}$ encodes the decomposition in operator form.

---

# Unlocked by This

> [!tip] Cohomology of Symmetric Spaces *(from Lie Theory and Differential Geometry)*
> On a compact symmetric space $M = G/K$, the harmonic forms are exactly the $G$-invariant forms. By the Hodge decomposition isomorphism, $H^k(G/K; \mathbb{R}) \cong$ ($G$-invariant $k$-forms on $G/K$), computable from the Lie algebra cohomology $H^*(\mathfrak{g}, \mathfrak{k}; \mathbb{R})$ (relative Lie algebra cohomology). This gives explicit formulas for the cohomology of symmetric spaces — Grassmannians, projective spaces, classical Lie groups — that would be hard to obtain by topological methods alone.

> [!tip] Spectral Geometry: Hearing the Shape of a Drum *(from Geometric Analysis)*
> The Hodge decomposition organizes $L^2\Omega^k(M)$ by eigenspaces of $\Delta$: $L^2\Omega^k = \bigoplus_{\lambda \geq 0}E_\lambda$ with $E_0 = \mathcal{H}^k$. The spectrum $\{\lambda_n\}$ is a geometric invariant of $(M, g)$. The **isospectral problem** asks: do two metrics with the same spectrum have to be isometric? Kac's famous question "Can you hear the shape of a drum?" is the negative answer in dimension $2$ (Milnor's isospectral $16$-tori). The Hodge decomposition shows that the *kernel* of $\Delta$ — the harmonic forms — is *topological* (= Betti numbers), so part of the spectrum is automatically determined by topology, while the positive eigenvalues encode metric-geometric data.

> [!tip] $L^2$ Index Theorems on Noncompact Manifolds *(from Geometric Analysis and Geometric Group Theory)*
> On a noncompact manifold (e.g., the universal cover $\tilde M$ of a compact $M$), the Hodge decomposition fails — the image of $d$ need not be closed in $L^2$. The fix is **reduced $L^2$-cohomology**: replace $\operatorname{im}\,d$ with its $L^2$-closure $\overline{\operatorname{im}\,d}$. The resulting Hodge decomposition $L^2\Omega^k(\tilde M) = \mathcal{H}^k_{(2)} \oplus \overline{dL^2\Omega^{k-1}} \oplus \overline{\delta L^2\Omega^{k+1}}$ holds, with $\mathcal{H}^k_{(2)}$ the space of $L^2$-harmonic forms — typically infinite-dimensional. **Atiyah's $L^2$-index theorem** assigns a real-valued "$L^2$-index" to elliptic operators on $\tilde M$ via von Neumann dimension, with applications to **$L^2$-Betti numbers** of universal covers, **Lück approximation** for Betti numbers of finite covers, and **geometric group theory**.

> [!tip] Witten Deformation and Morse Theory *(from Mathematical Physics)*
> For a Morse function $f$ on a closed Riemannian manifold, the **Witten deformation** $d_t = e^{-tf}d e^{tf}$ deforms the de Rham complex. The deformed Hodge Laplacian $\Delta_t = (d_t + d_t^*)^2$ has the same kernel as $\Delta$ (the Betti numbers don't change), but its eigenforms concentrate near the critical points of $f$ as $t\to\infty$. The small-eigenvalue eigenforms become a finite-dimensional combinatorial complex generated by the critical points, with the differential counting gradient flow lines — the **Morse–Smale chain complex**. The **Morse inequalities** $b_k(M) \leq c_k(f)$ (Betti number bounded by index-$k$ critical point count) follow from the comparison: the kernel dimensions $b_k$ are bounded by the dimensions of the deformed eigenspaces near the critical points.
