---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Chern-Weil Form of an Invariant Polynomial"
  - "Def - Ad-Invariant Polynomial"
  - "Thm - Bianchi Identity for a Principal Connection"
  - "Thm - Graded Antisymmetry and Jacobi Identity for Lie-Algebra-Valued Forms"
  - "Thm - Existence of Connections on Principal Bundles"
  - "Thm - Pull-Back of Connections and Curvature"
  - "Thm - Structure Equation for the Curvature"
  - "Thm - Homotopy Invariance of de Rham Cohomology"
tags: [geometry, gauge-theory, characteristic-classes, chern-weil]
---

# Notation

Throughout, $G$ is a Lie group with Lie algebra $\mathfrak{g} = T_eG$, and $\operatorname{Ad} : G \to GL(\mathfrak{g})$ is its [[Def - Adjoint Representation|adjoint representation]], $\operatorname{Ad}_g X = \tfrac{d}{dt}\big|_{0}\, g \exp(tX) g^{-1}$; for a matrix group $\operatorname{Ad}_g X = gXg^{-1}$ and $\operatorname{ad}_X Y = [X,Y]$. We fix a ground field $\mathbb{K} \in \{\mathbb{R}, \mathbb{C}\}$; the argument is identical for both, and we take $\mathbb{K} = \mathbb{C}$ when a choice is needed (following Haydys).

$P \xrightarrow{\ \pi\ } M$ is a principal $G$-bundle over a smooth manifold $M$; the right action is written $R_g(p) = p\cdot g$, and the [[Def - Fundamental Vector Field of a Group Action|fundamental vector field]] of $\xi \in \mathfrak{g}$ is $\xi_P(p) = \tfrac{d}{dt}\big|_0\, p\cdot\exp(t\xi)$. A [[Def - Connection on a Principal Bundle|connection]] is a form $\omega \in \Omega^1(P;\mathfrak{g})$ with $\omega(\xi_P) = \xi$ and $R_g^*\omega = \operatorname{Ad}_{g^{-1}}\omega$; its [[Def - Curvature of a Principal Connection|curvature]] is given by the [[Thm - Structure Equation for the Curvature|structure equation]]
$$\Omega \;=\; d\omega + \tfrac12[\omega\wedge\omega] \;\in\; \Omega^2(P;\mathfrak{g}),$$
which is horizontal ($\Omega(\xi_P,\cdot) = 0$) and $\operatorname{Ad}$-equivariant ($R_g^*\Omega = \operatorname{Ad}_{g^{-1}}\Omega$). The space of all connections on $P$ is written $\mathcal{A}(P)$.

For $\mathfrak{g}$-valued forms $\alpha \in \Omega^p(P;\mathfrak{g})$ and $\beta \in \Omega^q(P;\mathfrak{g})$, the [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|bracket-wedge]] $[\alpha\wedge\beta] \in \Omega^{p+q}(P;\mathfrak{g})$ combines the wedge of forms with the Lie bracket of values; on decomposables $[\,\phi\, X \wedge \psi\, Y\,] = (\phi\wedge\psi)\,[X,Y]$ for ordinary forms $\phi,\psi$ and $X,Y \in \mathfrak{g}$. We use three of its properties, all from [[Thm - Graded Antisymmetry and Jacobi Identity for Lie-Algebra-Valued Forms|graded antisymmetry and the Jacobi identity]]: graded antisymmetry $[\alpha\wedge\beta] = -(-1)^{pq}[\beta\wedge\alpha]$, the graded Leibniz rule $d[\alpha\wedge\beta] = [d\alpha\wedge\beta] + (-1)^p[\alpha\wedge d\beta]$, and the graded Jacobi identity, whose only use here is that $[[\omega\wedge\omega]\wedge\omega] = 0$ for a $1$-form $\omega$.

An $\operatorname{Ad}$-**invariant polynomial** of degree $d$ is a map $p : \mathfrak{g} \to \mathbb{K}$ that is homogeneous of degree $d$, polynomial in the coordinates of any basis, and satisfies $p(\operatorname{Ad}_g\xi) = p(\xi)$ for all $g \in G$, $\xi \in \mathfrak{g}$; the graded ring of all such is $I(G) = \bigoplus_{d\ge 0} I_d(G)$ under pointwise product. To each $p \in I_d(G)$ its [[Def - Ad-Invariant Polynomial|polarisation]] $\tilde{p} : \mathfrak{g}^{\times d} \to \mathbb{K}$ is the unique symmetric $d$-linear form with $\tilde{p}(\xi,\dots,\xi) = p(\xi)$; it is again $\operatorname{Ad}$-invariant, $\tilde{p}(\operatorname{Ad}_g\xi_1,\dots,\operatorname{Ad}_g\xi_d) = \tilde{p}(\xi_1,\dots,\xi_d)$. We use once, and prove on that page, the **infinitesimal invariance identity**
$$\sum_{j=1}^d \tilde{p}(\xi_1,\dots,\xi_{j-1},[\xi,\xi_j],\xi_{j+1},\dots,\xi_d) \;=\; 0 \qquad \text{for all } \xi,\xi_1,\dots,\xi_d \in \mathfrak{g}. \tag{$\ast$}$$

Given a basis $Y_1,\dots,Y_N$ of $\mathfrak{g}$, the polarisation extends to $\mathfrak{g}$-valued forms: for $\Phi_1,\dots,\Phi_d$ with $\Phi_i = \sum_{a} \Phi_i^a\, Y_a$ ($\Phi_i^a$ ordinary forms) we set
$$\tilde{p}(\Phi_1,\dots,\Phi_d) \;=\; \sum_{a_1,\dots,a_d=1}^N \Phi_1^{a_1}\wedge\cdots\wedge\Phi_d^{a_d}\ \tilde{p}(Y_{a_1},\dots,Y_{a_d}) \;\in\; \Omega^{\bullet}(P;\mathbb{K}),$$
independent of the basis by multilinearity. The **Chern–Weil form on the total space** is $p(\Omega) := \tilde{p}(\Omega,\dots,\Omega) \in \Omega^{2d}(P;\mathbb{K})$ (with $d$ arguments); because each $\Omega$ has even degree $2$, this equals the entrywise polynomial $p$ evaluated on the matrix of $2$-forms, and even-degree forms commute so the evaluation is unambiguous. On the [[Def - Chern-Weil Form of an Invariant Polynomial|Chern–Weil form page]] it is proved that $p(\Omega)$ is **basic** (horizontal and $G$-invariant), hence there is a unique **descended Chern–Weil form**
$$p(F_\omega) \in \Omega^{2d}(M;\mathbb{K}) \qquad\text{with}\qquad \pi^* p(F_\omega) = p(\Omega).$$

$H^k_{dR}(M) = H^k_{dR}(M;\mathbb{K})$ is the [[Def - de Rham Cohomology|de Rham cohomology]], with product $[\alpha]\smile[\beta] = [\alpha\wedge\beta]$; $H^{\mathrm{even}}_{dR}(M) = \bigoplus_j H^{2j}_{dR}(M)$ is the even subring. We write $c_p(P) := [p(F_\omega)] \in H^{2d}_{dR}(M)$ for the cohomology class the theorem shows is well defined.

> [!warning] Convention: two source formulations of $p(F_\omega)$
> Haydys (§3.1) writes the total-space curvature as $\hat{F}_A = \pi^*F_a = da + \tfrac12[a\wedge a]$ and forms $p(\hat{F}_A)$ by evaluating the polynomial on the matrix of $2$-forms; this is our $p(\Omega)$ with $\omega = a$. Bär (§2.5) works with the descended curvature $\bar\Omega \in \Omega^2(M; P\times_{\operatorname{Ad}}\mathfrak{g})$ and writes the characteristic form with an antisymmetrising normalisation, $(\lambda\circ\bar\Omega)(X_1,\dots,X_{2d}) = \tfrac{1}{d!}\sum_{\sigma\in S_{2d}}\operatorname{sign}(\sigma)\,\lambda(\bar\Omega(X_{\sigma 1},X_{\sigma 2}),\dots,\bar\Omega(X_{\sigma(2d-1)},X_{\sigma(2d)}))$, where $\lambda = \tilde{p}$. That these two forms agree, and both equal the basis formula above, is proved on the [[Def - Chern-Weil Form of an Invariant Polynomial|Chern–Weil form page]]; here we use the basis formula and its total-space avatar $p(\Omega)$.

---

# Statement

> **Theorem (Chern–Weil).** Let $P \to M$ be a principal $G$-bundle over a smooth manifold, and let $p \in I_d(G)$ be an $\operatorname{Ad}$-invariant polynomial of degree $d$. For every connection $\omega \in \mathcal{A}(P)$, with descended Chern–Weil form $p(F_\omega) \in \Omega^{2d}(M)$:
> $$\textbf{(i)}\quad d\,p(F_\omega) = 0 \qquad\text{(the Chern–Weil form is closed).}$$
> $$\textbf{(ii)}\quad \text{for any two connections } \omega_0,\omega_1 \in \mathcal{A}(P),\ \ p(F_{\omega_1}) - p(F_{\omega_0}) \text{ is exact.}$$
> Consequently the de Rham cohomology class
> $$c_p(P) := [\,p(F_\omega)\,] \in H^{2d}_{dR}(M)$$
> **does not depend on the connection** $\omega$, and:
> $$\textbf{(iii)}\quad \text{the map } I(G) \longrightarrow H^{\mathrm{even}}_{dR}(M),\quad p \longmapsto c_p(P),$$
> is a homomorphism of rings — additive, unital ($c_{\mathbf 1}(P) = 1 \in H^0_{dR}(M)$ for the constant polynomial $\mathbf 1 \in I_0(G)$), and multiplicative, $c_{pq}(P) = c_p(P)\smile c_q(P)$. This is the **Chern–Weil homomorphism** of the bundle $P$.

The class $c_p(P)$ is thus an invariant of $P$ built from the differential geometry of any single connection, yet independent of that connection. The value $\langle c_p(P), [\Sigma]\rangle = \int_\Sigma p(F_\omega)$ against a closed submanifold is a **characteristic number** of $P$.

---

# Motivation

Curvature is the local, connection-dependent measure of a bundle's twisting: a flat connection has $\Omega = 0$, and different connections on the same bundle have wildly different curvatures. The question Chern–Weil theory answers is whether curvature nonetheless contains connection-*independent* information — something intrinsic to the bundle $P$ itself, visible from any one connection but the same for all of them. The answer is yes, and the mechanism is this: certain $\operatorname{Ad}$-invariant polynomial combinations of the curvature are closed forms whose cohomology class is a topological invariant of $P$.

The point is worth stating as the contrast it resolves. The curvature $\Omega$ transforms under a change of local trivialisation by conjugation, $F' = g^{-1}Fg$; it is not a form on the base at all until one either descends it as an $\operatorname{ad}P$-valued form or feeds it to something invariant. An $\operatorname{Ad}$-invariant polynomial $p$ is exactly a gadget insensitive to conjugation, so $p(F_\omega)$ *is* an honest form on $M$. That form turns out to be closed, and — the substantial content — its cohomology class is the same for every connection. So while no single connection is canonical, the class $c_p(P)$ is canonical, and it obstructs the bundle from being trivial: a trivial bundle admits a flat connection, whose curvature vanishes, whose Chern–Weil forms vanish in positive degree, so a nonzero $c_p(P)$ certifies that $P$ is nontrivial.

This is the construction that produces every characteristic class computable from curvature: the [[Def - Chern Classes|Chern classes]] $c_j$ from the coefficients of $\det(1 + \tfrac{i}{2\pi}\xi)$, the [[Def - Pontryagin Classes|Pontryagin classes]] from $\det(1 - \tfrac{1}{2\pi}\xi)$, the [[Def - Euler Class of an Oriented Vector Bundle|Euler class]] from the [[Def - Pfaffian|Pfaffian]]. The Chern–Weil theorem is the single statement that makes all of these well defined. Downstream it is the engine behind the topological lower bound on the Yang–Mills energy, the integrality of the instanton number, and the [[Thm - Transgression Formula and the Chern-Simons Form|Chern–Simons secondary invariant]] that measures *how* two Chern–Weil forms differ within their common class.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypotheses are mild — a principal bundle, a connection, and an invariant polynomial — so the real skill is recognising when a geometric problem secretly furnishes these three ingredients, especially the invariant polynomial.

The first disguised source is **a vector bundle with a fibre metric and a compatible connection**. A rank-$r$ complex vector bundle $E \to M$ with a Hermitian metric has a principal $U(r)$-bundle of unitary frames $\operatorname{Fr}_U(E)$, and a metric-compatible connection on $E$ is a connection on $\operatorname{Fr}_U(E)$; the invariant polynomials on $\mathfrak{u}(r)$ are the symmetric functions of eigenvalues, the coefficients of $\det(\lambda\mathbf 1 + \tfrac{i}{2\pi}\xi)$. The non-obvious bridge is that a metric is not a piece of data one must be handed: every vector bundle over a paracompact base admits one (average any local metrics with a partition of unity), so *every* complex vector bundle feeds Chern–Weil theory, and the resulting classes turn out to be independent of the metric as well as the connection. *Example problem:* show the tautological line bundle $\mathcal{O}(-1)\to\mathbb{CP}^1$ is nontrivial by computing $\int_{\mathbb{CP}^1}\tfrac{i}{2\pi}F = -1$ from any unitary connection.

The second disguised source is **a Riemannian manifold and its tangent bundle**. The Levi-Civita connection is a metric connection on $TM$, whose structure group reduces to $SO(n)$; on $\mathfrak{so}(2m)$ the Pfaffian and the Pontryagin polynomials are invariant. Here the bridge is that Riemannian geometry hands you a canonical connection for free, so curvature invariants of the metric become topological invariants of the manifold. *Example problem:* recover $\int_{S^2} e(TS^2) = 2$ from the Gaussian curvature of the round sphere, the differential-geometric half of Gauss–Bonnet.

The third disguised source is **a classifying map into a Grassmannian or projective space**. If $P = f^*P_0$ for a universal bundle $P_0$ and some $f : M \to BG$, then any connection on $P_0$ pulls back to a connection on $P$, and $c_p(P) = f^* c_p(P_0)$ by naturality. The bridge is that even a bundle presented purely homotopically — by its classifying map, with no connection in sight — has Chern–Weil classes, because the universal bundle carries a connection one may pull back. *Example problem:* deduce that the class $c_p(P)$ depends only on the homotopy class of the classifying map, hence only on the isomorphism class of $P$.

**Targets (Output Amplification)**

The bare conclusion is a well-defined cohomology class $c_p(P)$. Combined with further inputs it becomes a sharp tool.

Combine $c_p(P)$ with **integration over a closed submanifold and an integrality theorem**. The pairing $\langle c_p(P),[\Sigma]\rangle = \int_\Sigma p(F_\omega)$ is a real number independent of $\omega$; when $p$ is one of the Chern or Pontryagin polynomials this number is in fact an *integer* (the [[Thm - First Chern Class of a Line Bundle from Curvature|degree of a line bundle]] over a surface, the [[Thm - Second Chern Number of an SU(2)-Bundle over a Closed Four-Manifold is the Clutching Degree|instanton number]] over a $4$-manifold). The extra ingredient is a clutching or classifying-space argument identifying the real period with a topological degree; the payoff is a integer-valued obstruction that pins down the bundle.

Combine $c_p(P)$ with **the transgression formula**. Chern–Weil (ii) says $p(F_{\omega_1}) - p(F_{\omega_0})$ is exact; the [[Thm - Transgression Formula and the Chern-Simons Form|transgression theorem]] exhibits an explicit primitive $Tp(\omega_0,\omega_1)$ with $p(F_{\omega_1}) - p(F_{\omega_0}) = d\,Tp(\omega_0,\omega_1)$. The extra ingredient is a chosen path of connections; the payoff is the Chern–Simons form, a *secondary* invariant that lives where the primary class is null and detects finer structure such as flat-connection invariants and the framing of $3$-manifolds.

Combine $c_p(P)$ with **the Yang–Mills energy and the Cauchy–Schwarz inequality**. On a closed oriented $4$-manifold the characteristic number $\tfrac{1}{8\pi^2}\int \operatorname{tr}(F\wedge F) = k(P)$ is fixed by the bundle, while the energy $\tfrac12\int|F|^2$ depends on the connection; comparing them gives the topological lower bound $\mathcal{YM}(A) \ge 8\pi^2|k(P)|$ with equality exactly at (anti-)self-dual connections. The extra ingredient is the Hodge star of chapter VII; the payoff is that instantons are the absolute minimisers of the energy in their topological sector.

---

# Why Is It True

Two facts do all the work, and they meet in one line. The first is the **Bianchi identity**: on the total space $P$, the curvature satisfies $d\Omega = [\Omega\wedge\omega]$ — its exterior derivative is a *bracket*. The second is the **invariance of $p$**: differentiating $p(\operatorname{Ad}_{\exp t\xi}\,\xi_1,\dots) = p(\xi_1,\dots)$ at $t=0$ shows that the polarisation $\tilde{p}$ annihilates any sum of "insert a bracket into one slot" terms — brackets are *invisible* to $p$. Now compute $d\,p(\Omega)$: by the Leibniz rule it is a sum of terms, each with one $d\Omega$ in a slot; replace each $d\Omega$ by the bracket $[\Omega\wedge\omega]$ using Bianchi; the result is exactly the sum of bracket-insertions that invariance kills. So $d\,p(\Omega) = 0$, and since $\pi^*$ is injective and commutes with $d$, the descended form $p(F_\omega)$ is closed.

> **Mechanism, in one sentence:** the Bianchi identity says $d$ of the curvature is a bracket, and invariance says brackets are invisible to $p$, so $d\,p(F_\omega) = 0$.

The independence of the connection is a second application of the same closedness, promoted one dimension. The space of connections $\mathcal{A}(P)$ is an **affine space**: any two connections are joined by the straight-line path $\omega_t = (1-t)\omega_0 + t\omega_1$, and every point of it is again a connection, because the two connection axioms — reproducing fundamental fields and $\operatorname{Ad}$-equivariance — are *affine* conditions preserved by convex combination. Assemble this path into a single connection $\tilde\omega$ on the bundle $\varpi^*P$ over the cylinder $M\times[0,1]$, whose two ends restrict to $\omega_0$ and $\omega_1$. Its Chern–Weil form $p(F_{\tilde\omega})$ is closed on $M\times[0,1]$ by part (i); restricting a closed form to the two ends of a cylinder gives cohomologous forms, because the two end-inclusions are homotopic. Hence $p(F_{\omega_1})$ and $p(F_{\omega_0})$ are cohomologous, that is, differ by an exact form.

> **Mechanism, in one sentence:** the space of connections is convex, so any two curvatures are the two ends of one closed form on a cylinder, and the ends of a cylinder carry the same cohomology.

The ring structure is then almost automatic: evaluating polynomials on the (commuting) even-degree matrix of curvature forms is an algebra homomorphism, so $(pq)(\Omega) = p(\Omega)\wedge q(\Omega)$, which on classes is the cup product $c_{pq}(P) = c_p(P)\smile c_q(P)$.

---

# What Makes This Hard

The subtle step in (i) is not the computation but the *transfer of the invariance identity from Lie-algebra elements to $\mathfrak{g}$-valued forms* — the passage Haydys asserts and Bär hides. The identity $(\ast)$ holds for elements $\xi_j \in \mathfrak{g}$; to use it with $\Omega$ (a $2$-form) in the slots and $\omega$ (a $1$-form) as the bracket-partner, one must track the signs incurred when an odd-degree form is commuted past the even-degree forms in front of it. The saving grace — and the thing that must be *checked*, not assumed — is that the forms being commuted past are all of even degree, so every sign is $+1$; if the polynomial had odd-degree arguments the identity would fail. The common error is to invoke $(\ast)$ verbatim without noticing that the wedge factors have been reordered.

For (ii) the pitfall is the claim, made in one clause by Haydys and needed by Bär, that the interpolating $\tilde\omega$ *is a connection* on $\varpi^*P$. It is easy to write down $(1-t)\varpi^*\omega_0 + t\varpi^*\omega_1$ and forget that $t$ is now a function on the cylinder, so that $\tilde\omega$ acquires no $dt$-component from the interpolation itself but its curvature does; one must verify the two connection axioms with $t$ varying. Bär's own proof of closedness has a third hidden step — the existence of a local section *horizontal at a prescribed point* — which we prove rather than assert.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove closedness on the total space $P$ by combining the Bianchi identity ($d\Omega$ is a bracket) with the invariance identity (brackets die under $\tilde{p}$), then descend through the injective $\pi^*$. Prove connection-independence by running closedness one dimension up, on the affine straight-line path of connections assembled into a single connection over the cylinder $M\times[0,1]$, and reading off cohomologous ends via homotopy invariance.

**Subgoal decomposition:**

1. **Invariance identity for forms.** Show $\sum_j \tilde{p}(\beta_1,\dots,[\alpha\wedge\beta_j],\dots,\beta_d) = 0$ for a $\mathfrak{g}$-valued $1$-form $\alpha$ and even-degree $\mathfrak{g}$-valued forms $\beta_j$.
   - *Hint:* Expand in a basis, pull the odd factor $\alpha^b$ to the front (no signs, since the forms it passes are even), and recognise the inner sum as $(\ast)$.
   - *Why needed:* It is the algebraic identity that makes $d\,p(\Omega) = 0$; without it closedness fails.

2. **Closedness on $P$.** Show $d\,p(\Omega) = 0$.
   - *Hint:* Leibniz gives $d\,p(\Omega) = \sum_j \tilde{p}(\Omega,\dots,d\Omega,\dots,\Omega)$; replace $d\Omega$ by $[\Omega\wedge\omega]$ (Bianchi), then apply Subgoal 1.
   - *Why needed:* This is part (i) upstairs, before descent.

3. **Descent.** Show $p(F_\omega)$ is closed on $M$.
   - *Hint:* $\pi^*$ commutes with $d$ and is injective on forms (a submersion); apply it to $d\,p(F_\omega)$.
   - *Why needed:* The theorem is about forms on $M$, not $P$.

4. **The interpolating connection.** Show $\tilde\omega = (1-t)\varpi^*\omega_0 + t\varpi^*\omega_1$ is a connection on $\varpi^*P \to M\times[0,1]$ with $\iota_j^\bullet\tilde\omega = \omega_j$ at the ends.
   - *Hint:* Check the two connection axioms; both are affine in $\omega$ and $t$ is a fibrewise-constant function.
   - *Why needed:* It packages the whole path $\omega_t$ into a single bundle-with-connection to which (i) applies.

5. **Cohomologous ends.** Show $p(F_{\omega_1}) - p(F_{\omega_0})$ is exact.
   - *Hint:* $p(F_{\tilde\omega})$ is closed (Subgoal 2–3 on the cylinder); the two end-inclusions $\iota_0,\iota_1$ are homotopic; apply homotopy invariance and the naturality $\iota_j^* p(F_{\tilde\omega}) = p(F_{\omega_j})$.
   - *Why needed:* This is part (ii).

6. **Ring homomorphism.** Show additivity, unitality, and $c_{pq}(P) = c_p(P)\smile c_q(P)$.
   - *Hint:* Polynomial evaluation on the commuting even matrix of forms is an algebra map; pass to classes.
   - *Why needed:* This is part (iii).

---

# Lemma Decomposition

> [!note]- Lemma 1: Invariance identity for $\mathfrak{g}$-valued forms
> **Statement:** Let $p \in I_d(G)$ with polarisation $\tilde{p}$. Let $\alpha \in \Omega^1(P;\mathfrak{g})$ and let $\beta_1,\dots,\beta_d \in \Omega^{\mathrm{even}}(P;\mathfrak{g})$ be $\mathfrak{g}$-valued forms of even degree. Then
> $$\sum_{j=1}^d \tilde{p}\big(\beta_1,\dots,\beta_{j-1},[\alpha\wedge\beta_j],\beta_{j+1},\dots,\beta_d\big) = 0.$$
>
> **Hint:** Expand everything in a basis of $\mathfrak{g}$; the only work is commuting the odd factor $\alpha^b$ to the front of each wedge product, which costs no sign because it passes only even-degree factors, and then recognising the coefficient as the infinitesimal invariance identity $(\ast)$.
>
> **Why needed:** It is the exact algebraic fact that turns "one $d\Omega$ per term" into zero after Bianchi. It is the step both sources leave unproved.
>
> > [!note]- Full proof
> > **Goal.** Assuming the infinitesimal invariance identity $(\ast)$ — proved on [[Def - Ad-Invariant Polynomial|the invariant-polynomial page]] and restated below — we must show the displayed sum of $\mathbb{K}$-valued forms vanishes identically.
> >
> > **Step 0 — the identity $(\ast)$ we build on.** Fix $\xi,\xi_1,\dots,\xi_d \in \mathfrak{g}$. Because $\exp(t\xi) \in G$ for all $t$, $\operatorname{Ad}$-invariance of $\tilde{p}$ gives $\tilde{p}(\operatorname{Ad}_{\exp t\xi}\xi_1,\dots,\operatorname{Ad}_{\exp t\xi}\xi_d) = \tilde{p}(\xi_1,\dots,\xi_d)$ for all $t$. Differentiating at $t=0$, using $\tfrac{d}{dt}\big|_0\operatorname{Ad}_{\exp t\xi}\xi_j = \operatorname{ad}_\xi\xi_j = [\xi,\xi_j]$ and the multilinearity of $\tilde{p}$,
> > $$\sum_{j=1}^d \tilde{p}(\xi_1,\dots,\xi_{j-1},[\xi,\xi_j],\xi_{j+1},\dots,\xi_d) = 0 \qquad (\ast)$$
> > (no connectedness of $G$ is needed, since only the one-parameter subgroups $\exp(t\xi)$ are used).
> >
> > **Step 1 — expand in a basis.** Fix a basis $Y_1,\dots,Y_N$ of $\mathfrak{g}$ and write $\alpha = \sum_{b} \alpha^b\, Y_b$ with $\alpha^b \in \Omega^1(P)$, and $\beta_i = \sum_{a} \beta_i^a\, Y_a$ with $\beta_i^a$ of even degree. By definition of the bracket-wedge on decomposables,
> > $$[\alpha\wedge\beta_j] = \sum_{b,a}\, \alpha^b\wedge\beta_j^a\ [Y_b,Y_a] \qquad \text{(bilinearity of } [\cdot\wedge\cdot] \text{ and the bracket).}$$
> > Substituting into the $j$-th term and using the basis formula for $\tilde{p}$ on $\mathfrak{g}$-valued forms,
> > $$\tilde{p}\big(\beta_1,\dots,[\alpha\wedge\beta_j],\dots,\beta_d\big) = \sum_{b}\ \sum_{a_1,\dots,a_d} \beta_1^{a_1}\wedge\cdots\wedge(\alpha^b\wedge\beta_j^{a_j})\wedge\cdots\wedge\beta_d^{a_d}\ \tilde{p}\big(Y_{a_1},\dots,[Y_b,Y_{a_j}],\dots,Y_{a_d}\big),$$
> > where $[Y_b,Y_{a_j}]$ occupies slot $j$ (the bracket's value is a Lie-algebra element, so $\tilde{p}$ receives it as an ordinary argument).
> >
> > **Step 2 — commute the odd factor to the front, tracking every sign.** In each summand the $1$-form $\alpha^b$ sits in position $j$, preceded by the factors $\beta_1^{a_1},\dots,\beta_{j-1}^{a_{j-1}}$, each of even degree. Moving $\alpha^b$ (degree $1$) leftward past a form of even degree $q$ multiplies by $(-1)^{1\cdot q} = (-1)^q = +1$ (since $q$ is even). Passing all $j-1$ even factors therefore costs the sign $\prod_{i<j}(+1) = +1$, so
> > $$\beta_1^{a_1}\wedge\cdots\wedge(\alpha^b\wedge\beta_j^{a_j})\wedge\cdots\wedge\beta_d^{a_d} = \alpha^b\wedge\big(\beta_1^{a_1}\wedge\cdots\wedge\beta_j^{a_j}\wedge\cdots\wedge\beta_d^{a_d}\big) \qquad \text{(even factors, no sign).}$$
> > This is the one place evenness of the $\beta_i$ is used; with an odd $\beta_i$ a factor of $-1$ would survive and the lemma would fail.
> >
> > **Step 3 — sum over $j$ and apply $(\ast)$.** The wedge $\alpha^b\wedge\beta_1^{a_1}\wedge\cdots\wedge\beta_d^{a_d}$ no longer depends on $j$, so summing over $j$ factors it out:
> > $$\sum_{j=1}^d \tilde{p}\big(\beta_1,\dots,[\alpha\wedge\beta_j],\dots,\beta_d\big) = \sum_{b}\ \sum_{a_1,\dots,a_d} \alpha^b\wedge\beta_1^{a_1}\wedge\cdots\wedge\beta_d^{a_d}\ \underbrace{\left(\sum_{j=1}^d \tilde{p}\big(Y_{a_1},\dots,[Y_b,Y_{a_j}],\dots,Y_{a_d}\big)\right)}_{= 0 \text{ by } (\ast)\text{ with } \xi = Y_b,\ \xi_i = Y_{a_i}}.$$
> > Every coefficient in the outer sum vanishes, so the total is $0$.
> >
> > **Conclusion.** The invariance identity transfers verbatim to even-degree $\mathfrak{g}$-valued forms with a $1$-form bracket-partner. $\blacksquare$

> [!note]- Lemma 2: The Chern–Weil form is closed on the total space
> **Statement:** With $\Omega$ the curvature of $\omega$ on $P$ and $p \in I_d(G)$, the form $p(\Omega) = \tilde{p}(\Omega,\dots,\Omega) \in \Omega^{2d}(P)$ satisfies $d\,p(\Omega) = 0$.
>
> **Hint:** Leibniz differentiates each $\Omega$ in turn (no signs, all even); Bianchi rewrites $d\Omega$ as a bracket; Lemma 1 kills the sum.
>
> **Why needed:** This is closedness upstairs — the whole of part (i) before descent.
>
> > [!note]- Full proof
> > **Goal.** Show the $(2d+1)$-form $d\,p(\Omega)$ vanishes on $P$.
> >
> > **Step 1 — differentiate by the Leibniz rule.** Since $\Omega$ has even degree $2$ and the basis coefficients $\tilde{p}(Y_{a_1},\dots,Y_{a_d})$ are constants, the graded Leibniz rule applied to $p(\Omega) = \sum \Omega^{a_1}\wedge\cdots\wedge\Omega^{a_d}\,\tilde{p}(Y_{a_1},\dots,Y_{a_d})$ produces no signs when $d$ lands on any factor:
> > $$d\,p(\Omega) = \sum_{j=1}^d \tilde{p}(\Omega,\dots,\Omega,\underset{\text{slot } j}{d\Omega},\Omega,\dots,\Omega) \qquad \text{(Leibniz; each preceding factor } \Omega^{a_i} \text{ is even, sign } +1).$$
> >
> > **Step 2 — invoke the Bianchi identity.** By the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity for a principal connection]] — for the curvature $\Omega = d\omega + \tfrac12[\omega\wedge\omega]$ of a connection $\omega$ on $P$ one has $d\Omega = [\Omega\wedge\omega]$ on $P$ — we substitute $d\Omega = [\Omega\wedge\omega]$ into every slot:
> > $$d\,p(\Omega) = \sum_{j=1}^d \tilde{p}(\Omega,\dots,\Omega,[\Omega\wedge\omega],\Omega,\dots,\Omega).$$
> >
> > **Step 3 — apply the invariance identity.** This is precisely the sum of Lemma 1 with $\alpha = \omega \in \Omega^1(P;\mathfrak{g})$ and $\beta_1 = \cdots = \beta_d = \Omega \in \Omega^2(P;\mathfrak{g})$ (all even). Hence
> > $$d\,p(\Omega) = \sum_{j=1}^d \tilde{p}(\Omega,\dots,[\Omega\wedge\omega],\dots,\Omega) = 0 \qquad \text{(by Lemma 1).}$$
> > (Lemma 1 with $\alpha = \omega$, $\beta_i = \Omega$ gives $\sum_j \tilde{p}(\Omega,\dots,[\omega\wedge\Omega],\dots,\Omega) = 0$; the bracket here is $[\Omega\wedge\omega] = -[\omega\wedge\Omega]$ by graded antisymmetry with degrees $2,1$, and the overall sign $-1$ leaves the value $0$ unchanged.)
> >
> > **Conclusion.** $d\,p(\Omega) = 0$: the Chern–Weil form is closed on the total space $P$. $\blacksquare$

> [!note]- Lemma 3: The pullback $\pi^*$ is injective and commutes with $d$; hence descent preserves closedness
> **Statement:** For the projection $\pi : P \to M$ of a fibre bundle, the pullback $\pi^* : \Omega^k(M) \to \Omega^k(P)$ is injective for every $k$, and $\pi^*d = d\,\pi^*$. Consequently, if $\gamma \in \Omega^k(M)$ satisfies $\pi^*(d\gamma) = 0$, then $d\gamma = 0$.
>
> **Hint:** $\pi$ is a surjective submersion, so its differential is surjective at every point; use that to reconstruct the value of a form on $M$ from its pullback.
>
> **Why needed:** The closedness of Lemma 2 lives on $P$; the theorem is about the descended form on $M$. Injectivity of $\pi^*$ is the bridge.
>
> > [!note]- Full proof
> > **Goal.** Show $\pi^*$ is injective and commutes with $d$, and deduce the descent statement.
> >
> > **Commuting with $d$.** Pullback of forms commutes with the exterior derivative for any smooth map, $\pi^*(d\gamma) = d(\pi^*\gamma)$; this is a standard naturality of $d$.
> >
> > **Injectivity.** Suppose $\gamma \in \Omega^k(M)$ with $\pi^*\gamma = 0$. Fix $m \in M$ and tangent vectors $v_1,\dots,v_k \in T_mM$. Since $\pi$ is a fibre-bundle projection it is a surjective submersion: there is $q \in \pi^{-1}(m)$, and $d\pi_q : T_qP \to T_mM$ is surjective, so we may choose $w_i \in T_qP$ with $d\pi_q(w_i) = v_i$. Then
> > $$\gamma_m(v_1,\dots,v_k) = \gamma_m\big(d\pi_q w_1,\dots,d\pi_q w_k\big) = (\pi^*\gamma)_q(w_1,\dots,w_k) = 0 \qquad \text{(definition of pullback; } \pi^*\gamma = 0).$$
> > As $m$ and the $v_i$ were arbitrary, $\gamma = 0$. So $\pi^*$ is injective.
> >
> > **Descent.** If $\pi^*(d\gamma) = 0$, then $d(\pi^*\gamma) = 0$; but the hypothesis is on $\pi^*(d\gamma)$, and by injectivity $\pi^*(d\gamma) = 0$ forces $d\gamma = 0$ directly. $\blacksquare$

> [!note]- Lemma 4: A local section horizontal at a point exists (Bär's route to closedness)
> **Statement:** Let $\omega$ be a connection on $P \to M$ with horizontal distribution $H = \ker\omega$, and let $b \in M$. Then there is a local section $s : U \to P$ on a neighbourhood $U \ni b$ with $ds_b(T_bM) = H_{s(b)}$; equivalently its local connection form $A := s^*\omega$ satisfies $A_b = 0$. From such a section, $d\,p(F_\omega)$ vanishes at $b$.
>
> **Hint:** Start with any section, and modify it by a gauge $g : U \to G$ with $g(b) = e$ and differential $dg_b = -A_b$; the transformation law of local connection forms cancels $A_b$.
>
> **Why needed:** It supplies Bär's alternative proof of (i) and, more importantly, fills the one gap Bär leaves — the existence of the horizontal-at-a-point section his proof assumes.
>
> > [!note]- Full proof
> > **Goal.** Construct $s$ with $A_b = 0$ and use it to prove $d\,p(F_\omega)|_b = 0$.
> >
> > **Step 0 — any section and its connection form.** Since $P$ is locally trivial, choose any local section $s_0 : U \to P$ near $b$, with local connection form $A_0 := s_0^*\omega \in \Omega^1(U;\mathfrak{g})$.
> >
> > **Step 1 — the transformation law.** For a smooth $g : U \to G$, the modified section $s := s_0\cdot g$ has connection form
> > $$A = \operatorname{Ad}_{g^{-1}}A_0 + g^*\theta,$$
> > where $\theta$ is the left [[Def - The Maurer-Cartan Form|Maurer–Cartan form]] of $G$ ($\theta_e = \operatorname{id}_{\mathfrak{g}}$, and $g^*\theta = g^{-1}dg$ for a matrix group); this is the [[Thm - Transformation of Local Connection and Curvature Forms|transformation law of local connection forms]].
> >
> > **Step 2 — choose $g$ to cancel $A_0$ at $b$.** In a chart around $b$ pick $g(x) := \exp\!\big(-A_0|_b(x - b)\big)$, so $g(b) = \exp(0) = e$ and $dg_b = -A_0|_b : T_bM \to \mathfrak{g} = T_eG$. Evaluating Step 1 at $b$, where $\operatorname{Ad}_{g(b)^{-1}} = \operatorname{Ad}_e = \operatorname{id}$ and $(g^*\theta)_b = \theta_e\circ dg_b = dg_b$,
> > $$A_b = \operatorname{Ad}_{e}(A_0|_b) + dg_b = A_0|_b - A_0|_b = 0.$$
> > Thus $A_b = s^*\omega|_b = 0$, which says $ds_b(v)$ is annihilated by $\omega$ for every $v \in T_bM$, i.e. $ds_b(T_bM) \subseteq H_{s(b)}$; equality holds by dimension count.
> >
> > **Step 3 — closedness at $b$.** Let $F_A := s^*\Omega = dA + \tfrac12[A\wedge A]$ be the local curvature. The descended form pulls back along the section as $s^* p(F_\omega) = \tilde{p}(F_A,\dots,F_A)$, and, expanding in the basis, $s^* p(F_\omega) = \sum F_A^{a_1}\wedge\cdots\wedge F_A^{a_d}\,\tilde{p}(Y_{a_1},\dots,Y_{a_d})$. Differentiating,
> > $$d\big(s^* p(F_\omega)\big) = \sum_{j=1}^d \tilde{p}(F_A,\dots,dF_A,\dots,F_A) \qquad \text{(Leibniz; even factors).}$$
> > Now $s^*(d\Omega) = d(s^*\Omega) = dF_A$; and by the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]] $d\Omega = [\Omega\wedge\omega]$ vanishes on triples of horizontal vectors. Because $ds_b(T_bM)$ is horizontal (Step 2), evaluating $dF_A|_b = s^*(d\Omega)|_b$ on any tangent vectors feeds $d\Omega$ only horizontal arguments, so $dF_A|_b = 0$. Every term of the sum contains a factor $dF_A$, hence $d(s^* p(F_\omega))|_b = 0$; as $s^* p(F_\omega) = p(F_\omega)$ on $U$ (a section splits $\pi$), $d\,p(F_\omega)|_b = 0$. Since $b$ was arbitrary, $d\,p(F_\omega) = 0$ on $M$.
> >
> > **Conclusion.** The horizontal-at-a-point section exists, and it gives a second, base-level proof that the Chern–Weil form is closed. $\blacksquare$

> [!note]- Lemma 5: The interpolating form is a connection on the cylinder bundle
> **Statement:** Let $\omega_0,\omega_1 \in \mathcal{A}(P)$, let $\varpi : M\times[0,1] \to M$ be the projection, $t$ the coordinate on $[0,1]$, and $\tilde{P} := \varpi^*P \to M\times[0,1]$ the pullback bundle. Then
> $$\tilde\omega := (1-t)\,\varpi^\bullet\omega_0 + t\,\varpi^\bullet\omega_1 \in \Omega^1(\tilde{P};\mathfrak{g})$$
> is a connection on $\tilde{P}$, where $\varpi^\bullet\omega_j$ denotes the connection on $\tilde P$ induced by $\omega_j$. Its restrictions to the ends satisfy $\iota_j^\bullet\tilde\omega = \omega_j$ for the inclusions $\iota_j : M \to M\times[0,1]$, $\iota_j(m) = (m,j)$, $j\in\{0,1\}$.
>
> **Hint:** Both connection axioms are affine in $\omega$, and $t$ is constant on the fibres of $\tilde{P}$, so it commutes with the right action and with fundamental vector fields.
>
> **Why needed:** It packages the straight-line path of connections into a single connection to which part (i) applies over the cylinder.
>
> > [!note]- Full proof
> > **Goal.** Verify the two defining properties of a connection for $\tilde\omega$, and compute its restriction to the ends.
> >
> > **Step 0 — the ingredients are connections.** By the [[Thm - Pull-Back of Connections and Curvature|pull-back theorem for connections]], each $\varpi^\bullet\omega_j := \hat\varpi^*\omega_j$ (with $\hat\varpi : \tilde{P} = \varpi^*P \to P$ the canonical equivariant map covering $\varpi$) is a connection on $\tilde{P}$. The function $t := \operatorname{pr}_{[0,1]}\circ\pi_{\tilde P}$ on $\tilde{P}$ is constant on each fibre (it is pulled back from the base $M\times[0,1]$), hence $R_g$-invariant, $R_g^*t = t$, and $t$ is annihilated by every fundamental vector field, $\xi_{\tilde P}(t) = 0$.
> >
> > **Step 1 — reproduction of fundamental fields.** For $\xi \in \mathfrak{g}$, the fundamental vector field $\xi_{\tilde P}$ has $\varpi^\bullet\omega_j(\xi_{\tilde P}) = \xi$ (each $\varpi^\bullet\omega_j$ is a connection). Since $t$ is a scalar function,
> > $$\tilde\omega(\xi_{\tilde P}) = (1-t)\,\varpi^\bullet\omega_0(\xi_{\tilde P}) + t\,\varpi^\bullet\omega_1(\xi_{\tilde P}) = (1-t)\,\xi + t\,\xi = \xi.$$
> >
> > **Step 2 — $\operatorname{Ad}$-equivariance.** For $g \in G$, using $R_g^*t = t$ (so $t$ pulls through the pullback as a scalar) and $R_g^*\varpi^\bullet\omega_j = \operatorname{Ad}_{g^{-1}}\varpi^\bullet\omega_j$,
> > $$R_g^*\tilde\omega = (1-t)\,R_g^*\varpi^\bullet\omega_0 + t\,R_g^*\varpi^\bullet\omega_1 = (1-t)\operatorname{Ad}_{g^{-1}}\varpi^\bullet\omega_0 + t\operatorname{Ad}_{g^{-1}}\varpi^\bullet\omega_1 = \operatorname{Ad}_{g^{-1}}\tilde\omega,$$
> > since $\operatorname{Ad}_{g^{-1}}$ is linear. Thus $\tilde\omega$ satisfies both axioms and is a connection on $\tilde{P}$. (Equivalently: $\varpi^\bullet\omega_1 - \varpi^\bullet\omega_0$ is basic and $\operatorname{Ad}$-equivariant, so $\tilde\omega = \varpi^\bullet\omega_0 + t\,(\varpi^\bullet\omega_1 - \varpi^\bullet\omega_0)$ adds a basic form to a connection, which is a connection by the affine structure of [[Thm - Existence of Connections on Principal Bundles|$\mathcal{A}(\tilde P)$]].)
> >
> > **Step 3 — restriction to the ends.** Because $\varpi\circ\iota_j = \operatorname{id}_M$, the bundle $\iota_j^*\tilde{P} = \iota_j^*\varpi^*P = (\varpi\circ\iota_j)^*P = P$, and under this identification $\iota_j^\bullet(\varpi^\bullet\omega_i) = (\varpi\circ\iota_j)^\bullet\omega_i = \omega_i$ (functoriality of pullback of connections). The function $t$ restricts to the constant $j$ along $\iota_j$. Hence
> > $$\iota_j^\bullet\tilde\omega = (1-j)\,\omega_0 + j\,\omega_1 = \omega_j \qquad (j = 0,1).$$
> >
> > **Conclusion.** $\tilde\omega$ is a genuine connection on the cylinder bundle whose two ends are exactly $\omega_0$ and $\omega_1$. $\blacksquare$

> [!note]- Lemma 6: Closed forms restrict to cohomologous forms at the ends of a cylinder
> **Statement:** Let $\eta \in \Omega^{k}(M\times[0,1])$ be closed, $d\eta = 0$, and let $\iota_0,\iota_1 : M \to M\times[0,1]$ be the two end-inclusions. Then $\iota_1^*\eta - \iota_0^*\eta$ is exact in $\Omega^k(M)$.
>
> **Hint:** $\iota_0$ and $\iota_1$ are smoothly homotopic, so they induce equal maps on de Rham cohomology.
>
> **Why needed:** It converts the closedness of $p(F_{\tilde\omega})$ on the cylinder into the exactness of $p(F_{\omega_1}) - p(F_{\omega_0})$ on $M$.
>
> > [!note]- Full proof
> > **Goal.** Show $[\iota_1^*\eta] = [\iota_0^*\eta]$ in $H^k_{dR}(M)$.
> >
> > **Step 1 — the end-inclusions are homotopic.** Define $H : M\times[0,1] \to M\times[0,1]$ by $H(m,\tau) = (m,\tau)$. This map is smooth, and $H(m,0) = (m,0) = \iota_0(m)$ while $H(m,1) = (m,1) = \iota_1(m)$, so $H$ is a smooth homotopy from $\iota_0$ to $\iota_1$. Thus $\iota_0 \simeq \iota_1$ as smooth maps $M \to M\times[0,1]$.
> >
> > **Step 2 — apply homotopy invariance.** By the [[Thm - Homotopy Invariance of de Rham Cohomology|homotopy invariance of de Rham cohomology]] — smoothly homotopic smooth maps $F \simeq G$ induce equal pullbacks $F^* = G^*$ on $H^\bullet_{dR}$ — we have $\iota_0^* = \iota_1^*$ as maps $H^k_{dR}(M\times[0,1]) \to H^k_{dR}(M)$. Since $\eta$ is closed it defines a class $[\eta] \in H^k_{dR}(M\times[0,1])$, and
> > $$[\iota_1^*\eta] = \iota_1^*[\eta] = \iota_0^*[\eta] = [\iota_0^*\eta] \qquad \text{(homotopy invariance).}$$
> >
> > **Step 3 — read off exactness.** Equality of classes means the representatives differ by an exact form: $\iota_1^*\eta - \iota_0^*\eta = d\zeta$ for some $\zeta \in \Omega^{k-1}(M)$.
> >
> > **Conclusion.** Restricting a closed form to the two ends of a cylinder gives cohomologous forms. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $P \to M$ be a principal $G$-bundle and $p \in I_d(G)$.
>
> **Part (i) — closedness.** Fix a connection $\omega \in \mathcal{A}(P)$ with curvature $\Omega$ and Chern–Weil forms $p(\Omega) \in \Omega^{2d}(P)$, $p(F_\omega) \in \Omega^{2d}(M)$ with $\pi^*p(F_\omega) = p(\Omega)$.
>
> By Lemma 2, $d\,p(\Omega) = 0$ on $P$. Since $\pi^*$ commutes with $d$ (Lemma 3),
> $$\pi^*\big(d\,p(F_\omega)\big) = d\big(\pi^*p(F_\omega)\big) = d\,p(\Omega) = 0 \qquad \text{(Lemma 3, definition of } p(F_\omega)\text{, Lemma 2).}$$
> By injectivity of $\pi^*$ (Lemma 3), $d\,p(F_\omega) = 0$. This proves (i). (Lemma 4 gives an independent, base-level proof via a section horizontal at each point.)
>
> **Part (ii) — independence of the connection.** Let $\omega_0,\omega_1 \in \mathcal{A}(P)$; the set $\mathcal{A}(P)$ is nonempty and affine by the [[Thm - Existence of Connections on Principal Bundles|existence and affineness of connections]], so the straight-line path is available. Form the cylinder bundle $\tilde{P} = \varpi^*P \to M\times[0,1]$ and the interpolating connection $\tilde\omega = (1-t)\varpi^\bullet\omega_0 + t\varpi^\bullet\omega_1$, which is a connection with $\iota_j^\bullet\tilde\omega = \omega_j$ by Lemma 5. Let $\eta := p(F_{\tilde\omega}) \in \Omega^{2d}(M\times[0,1])$ be its Chern–Weil form.
>
> **Step 0 — well-posedness of $\eta$.** $\tilde\omega$ is a bona fide connection on $\tilde{P}$ (Lemma 5), so its curvature and descended Chern–Weil form $\eta$ are defined exactly as on $P$.
>
> **Step 1 — $\eta$ is closed.** Applying part (i), already proved, to the bundle $\tilde{P} \to M\times[0,1]$ and the connection $\tilde\omega$ gives $d\eta = 0$.
>
> **Step 2 — restrict to the ends.** By the naturality of the Chern–Weil form under pullback: for a smooth $f : N \to M$, the [[Thm - Pull-Back of Connections and Curvature|pull-back theorem]] gives $F_{f^\bullet\omega} = f^*F_\omega$ for the curvatures, and applying the (constant-coefficient, pullback-commuting) polarisation to both sides yields $p(F_{f^\bullet\omega}) = f^*p(F_\omega)$. With $f = \iota_j$ and the interpolating connection, using $\iota_j^\bullet\tilde\omega = \omega_j$ (Lemma 5),
> $$\iota_j^*\eta = \iota_j^*p(F_{\tilde\omega}) = p\big(F_{\iota_j^\bullet\tilde\omega}\big) = p(F_{\omega_j}) \qquad (j = 0,1).$$
> (In detail: $\pi_{\tilde P}^* p(F_{\tilde\omega}) = p(\Omega_{\tilde\omega})$; pulling back along $\hat\iota_j$ and using $\hat\iota_j^*\Omega_{\tilde\omega} = \Omega_{\omega_j}$ from the pull-back theorem, then the injectivity of $\pi_P^*$ (Lemma 3), gives the identity on $M$.)
>
> **Step 3 — conclude exactness.** By Lemma 6 applied to the closed form $\eta$, the difference $\iota_1^*\eta - \iota_0^*\eta$ is exact. By Step 2 this difference is $p(F_{\omega_1}) - p(F_{\omega_0})$. Hence $p(F_{\omega_1}) - p(F_{\omega_0})$ is exact, proving (ii).
>
> **Well-definedness of $c_p(P)$.** By (i) each $p(F_\omega)$ is closed and defines a class $[p(F_\omega)] \in H^{2d}_{dR}(M)$; by (ii) any two choices of $\omega$ give cohomologous forms, so the class $c_p(P) := [p(F_\omega)]$ is independent of the connection.
>
> **Part (iii) — ring homomorphism.** Fix $P$ and a connection $\omega$ with curvature $\Omega$; write $\mathrm{ev}_\Omega : \mathbb{K}[\mathfrak{g}] \to \Omega^{\mathrm{even}}(P)$ for "evaluate a polynomial on the matrix of $2$-forms $\Omega$", equivalently $q \mapsto \tilde{q}(\Omega,\dots,\Omega)$ for homogeneous $q$.
>
> **Additivity and unitality.** For $p,p' \in I_d(G)$ of the same degree, $\mathrm{ev}_\Omega(p+p') = \mathrm{ev}_\Omega(p) + \mathrm{ev}_\Omega(p')$ by linearity of polarisation, so $c_{p+p'}(P) = c_p(P) + c_{p'}(P)$; extending additively over degrees makes $p \mapsto c_p(P)$ additive on $I(G) = \bigoplus_d I_d(G)$. The constant polynomial $\mathbf 1 \in I_0(G)$ has $\mathbf 1(\Omega) = 1 \in \Omega^0(P)$, whose descended form is $1 \in \Omega^0(M)$, so $c_{\mathbf 1}(P) = [1] = 1 \in H^0_{dR}(M)$: the map is unital.
>
> **Multiplicativity.** Let $p \in I_{d_1}(G)$, $q \in I_{d_2}(G)$, so $pq \in I_{d_1+d_2}(G)$. Because the entries of $\Omega$ are even-degree ($2$-)forms and even-degree forms commute in $\Omega^\bullet(P)$, the evaluation map $\mathrm{ev}_\Omega$ is an algebra homomorphism into the commutative ring $\Omega^{\mathrm{even}}(P)$; in particular
> $$(pq)(\Omega) = \mathrm{ev}_\Omega(pq) = \mathrm{ev}_\Omega(p)\wedge\mathrm{ev}_\Omega(q) = p(\Omega)\wedge q(\Omega).$$
> Descending (apply $\pi^*$-injectivity to $\pi^*[(pq)(F_\omega)] = (pq)(\Omega) = p(\Omega)\wedge q(\Omega) = \pi^*[p(F_\omega)\wedge q(F_\omega)]$) gives $(pq)(F_\omega) = p(F_\omega)\wedge q(F_\omega)$ on $M$. Passing to cohomology, where the cup product is represented by the wedge of representatives,
> $$c_{pq}(P) = [(pq)(F_\omega)] = [p(F_\omega)\wedge q(F_\omega)] = [p(F_\omega)]\smile[q(F_\omega)] = c_p(P)\smile c_q(P).$$
>
> **Conclusion.** The map $p \mapsto c_p(P)$ is additive, unital, and multiplicative, hence a ring homomorphism $I(G) \to H^{\mathrm{even}}_{dR}(M)$. Therefore, for every principal $G$-bundle $P \to M$, the Chern–Weil forms of any connection are closed, their cohomology classes are connection-independent invariants of $P$, and they assemble into the Chern–Weil homomorphism. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Hermitian holomorphic line bundles and the curvature of the Fubini–Study metric.** On a complex manifold, a holomorphic line bundle with a Hermitian metric $h$ carries the Chern connection, whose curvature is $F = -\partial\bar\partial\log h$ in a local holomorphic frame. Chern–Weil applies with $p = \tfrac{i}{2\pi}\operatorname{tr}$ to give $c_1 = [\tfrac{i}{2\pi}F]$. The theorem is what guarantees this class is independent of the metric $h$ — a fact not at all obvious from the formula, since $F$ depends visibly on $h$. Why it applies is subtle: the Chern connection is metric-*and*-holomorphy compatible, so it is a $U(1)$-connection to which the theorem speaks; why non-obvious: two metrics differ by a positive function, changing $F$ by $-\partial\bar\partial\log(h'/h)$, which the theorem must — and does — certify as exact.

**Flat bundles and representation varieties.** A flat connection has $\Omega = 0$, so every Chern–Weil form vanishes and $c_p(P) = 0$ for all $p$ of positive degree. Turned around, a bundle with any nonzero Chern–Weil class admits no flat connection, hence its holonomy representation cannot be rigid/trivial. This is non-obvious because flatness is a differential condition on one connection while the obstruction is a cohomological invariant of the whole bundle; the theorem is exactly the bridge, since it lets the vanishing at one flat connection propagate to the connection-independent class.

**Equivariant cohomology and moment maps.** For a Hamiltonian $G$-action with moment map $\mu$, the Cartan model computes equivariant characteristic classes by feeding the equivariant curvature $\Omega + \mu$ into invariant polynomials; the Chern–Weil theorem is the non-equivariant shadow, and the localisation formula reduces integrals of $p(F)$ to fixed-point data. The theorem applies because the equivariant curvature satisfies an equivariant Bianchi identity of the same shape; the non-obvious point is that the entire construction is the $G$-equivariant refinement of the single closedness computation proved here.

---

# Bridges

- **[[Thm - Transgression Formula and the Chern-Simons Form|Transgression and the Chern–Simons form]]** — the effective refinement of part (ii). Where Chern–Weil (ii) only asserts that $p(F_{\omega_1}) - p(F_{\omega_0})$ is exact, transgression writes down the primitive explicitly: for the path $\omega_t = \omega_0 + t(\omega_1 - \omega_0)$ one differentiates $p(F_{\omega_t})$ in $t$ using $\tfrac{d}{dt}F_{\omega_t} = d^{\omega_t}(\omega_1-\omega_0)$, the invariance identity (Lemma 1), and Bianchi, obtaining $p(F_{\omega_1}) - p(F_{\omega_0}) = d\,Tp(\omega_0,\omega_1)$. Taking $\omega_0$ the product connection on a trivial bundle produces the Chern–Simons $3$-form $\operatorname{tr}(A\wedge dA + \tfrac23 A^{\wedge 3})$, the secondary invariant that measures the interior of the class this theorem shows to be empty.

- **[[Def - Chern Classes|Chern classes]]** — the primary application. Feeding the coefficients $c_j$ of $\det(\mathbf 1 + \tfrac{i}{2\pi}\xi)$, invariant polynomials on $\mathfrak{u}(r)$, into the Chern–Weil homomorphism produces $c_j(P) = [c_j(F_\omega)] \in H^{2j}_{dR}(M)$; part (iii) is exactly what makes the total Chern class $c(P) = \sum_j c_j(P)$ multiplicative under Whitney sums (block-diagonal curvature, multiplicative determinant). The construction here replaces, with a complete proof, the statement-only page that once carried the Chern–Weil theorem elsewhere in the vault: *the Chern–Weil theorem stated there is proved here*.

- **[[Def - Euler Class of an Oriented Vector Bundle|Euler class and the Pfaffian]]** — the same theorem with $p = \operatorname{Pf}$ on $\mathfrak{so}(2m)$. The Pfaffian is $\operatorname{Ad}(SO(2m))$-invariant of degree $m$, so $e(E) = [\operatorname{Pf}(\tfrac{F}{2\pi})] \in H^{2m}_{dR}(M)$ is a well-defined class by this theorem; the Gauss–Bonnet integrand $\int_{S^2} e(TS^2) = 2$ is a characteristic number in the sense above.

- **[[Thm - Homotopy Invariance of de Rham Cohomology|Homotopy invariance of de Rham cohomology]]** — the imported engine of part (ii). The single fact used is that the two end-inclusions of a cylinder induce equal maps on cohomology; the proof there constructs the chain homotopy $h$ with $dh + hd = \iota_1^* - \iota_0^*$ by integrating along the interval, which is the "Poincaré-lemma-style" homotopy operator Haydys leaves unproved, made rigorous once on the linked page and reused here.

---

# Unlocked by This

> [!tip] The Chern–Weil homomorphism $I(G) \to H^\bullet(BG)$ *(from Algebraic Topology)*
> Running the construction on the universal bundle $EG \to BG$ gives a ring map from invariant polynomials to the cohomology of the classifying space; for compact $G$ it is an isomorphism onto $H^\bullet(BG;\mathbb{R})$, so real characteristic classes are *exactly* invariant polynomials. This is the structural reason the list of characteristic classes is the list of generators of $I(G)$.

> [!tip] Topological lower bound for Yang–Mills *(from Chapter VII)*
> Because $\tfrac{1}{8\pi^2}\int_X\operatorname{tr}(F\wedge F)$ is a connection-independent integer $k(P)$ by this theorem, the Yang–Mills energy obeys $\mathcal{YM}(A) \ge 8\pi^2|k(P)|$, with equality precisely at (anti-)self-dual connections. See **Thm - Energy Identity and the Topological Bound for Yang-Mills**.

> [!tip] Secondary and higher invariants *(from Chern–Simons theory)*
> When $c_p(P) = 0$ the primary invariant is silent, but the transgression form is then closed and defines a *secondary* class in an odd degree; iterating produces the tower of Chern–Simons and Cheeger–Simons invariants that refine flat-bundle and framing data. See [[Def - Chern-Simons Functional|the Chern–Simons functional]].
