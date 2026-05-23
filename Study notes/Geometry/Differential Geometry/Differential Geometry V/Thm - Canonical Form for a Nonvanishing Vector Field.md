---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Vector Field"
  - "Def - Flow of a Vector Field"
  - "Thm - Fundamental Theorem on Flows"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold, $X \in \mathfrak{X}(M)$ a smooth [[Def - Smooth Vector Field|vector field]]. A point $p \in M$ is **regular** for $X$ if $X_p \neq 0$, and **singular** if $X_p = 0$. $\phi^X$ is the flow of $X$. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]] for the full notation registry.

---

# Statement

> **Theorem (Canonical Form / Straightening Theorem; Lee Theorem 9.22).** Let $X$ be a smooth vector field on a smooth manifold $M$, and let $p \in M$ be a regular point of $X$ ($X_p \neq 0$). Then there exist smooth coordinates $(s^1, \dots, s^n)$ on some open neighbourhood of $p$ in which $X$ has the coordinate representation
> $$X = \frac{\partial}{\partial s^1}.$$
>
> Moreover, if $S \subseteq M$ is any embedded hypersurface (codimension-1 submanifold) through $p$ with $X_p \notin T_p S$, the coordinates can be chosen so that the slice $\{s^1 = 0\}$ is exactly $S$ in a neighborhood of $p$ (i.e. $s^1$ is a local defining function for $S$).

---

# Motivation

The Straightening Theorem is the deepest **rigidity** result in the chapter, and it makes the chapter feel surprisingly small. The lesson: *all nonvanishing smooth vector fields look the same locally*. The infinite variety of vector fields you can write down — $r \partial_r$, $\sin(x)\partial_x$, the Hamiltonian field of some complicated function — all are, up to a diffeomorphism, the constant horizontal flow $\partial/\partial s^1$ near any point where they do not vanish. There is no local invariant.

This explains why the chapter has the flavour it does. Every question about a single nonvanishing vector field has the *same answer*, because you can always straighten the field to $\partial/\partial s^1$ and reduce to an elementary computation in $\mathbb{R}^n$. The substance of differential geometry is therefore concentrated entirely in (i) what happens at *singular* points of vector fields, where straightening fails — phase portraits, hyperbolic equilibria, the entire qualitative theory of dynamical systems — and (ii) the interaction between *multiple* vector fields, where commutators measure obstructions to joint straightening.

Why does this work? Geometrically: a regular vector field defines, in a small enough neighbourhood, a local "fibration by integral curves" — the manifold near $p$ is foliated by the orbits of $X$. Pick a codimension-1 transversal $S$ through $p$; parametrize $S$ by $(s^2, \dots, s^n)$; let $s^1$ be the time spent flowing from $S$ to reach the current point. Then $(s^1, s^2, \dots, s^n)$ are coordinates, and $X = \partial/\partial s^1$ because flowing in the $s^1$ direction is exactly flowing by $X$.

The construction is the **flowout** from a transversal: every nonvanishing vector field generates a flow, and the flow projects the neighbourhood of $p$ onto a product $(-\delta, \delta) \times S$ where $S$ is any transverse hypersurface. This is the Flowout Theorem (Lee Theorem 9.20), of which the Straightening Theorem is a corollary.

The theorem's role in the chapter: it is the local canonical form against which all other local results are calibrated. It is also the foundation for the multi-field generalization (Lee Theorem 9.46, "canonical form for commuting vector fields"), which says $k$ linearly independent commuting smooth vector fields are jointly straightened to $\partial/\partial s^1, \dots, \partial/\partial s^k$. And it is the rank-1 case of the [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|Frobenius theorem]], which handles non-commuting fields via the involutivity condition.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$X_p \neq 0$" — $X$ is regular at $p$. The skill is recognizing when straightening is the right move.

The first disguised source is **a single nonvanishing vector field with complicated coordinate expression.** Property $B$: you are asked to verify a local statement about $X$ — flow domain, function-of-flow, invariant submanifold — and the explicit form of $X$ is unwieldy. The bridge: straighten. Use: in the straightened coordinates the statement becomes elementary, so reduce to that case.

The second disguised source is **a problem involving "all vector fields locally look alike" at regular points.** Property $B$: a statement about *every* vector field at regular points, e.g. "the flow is locally injective", "an integral curve is locally an embedded submanifold", "the orbit of $p$ under $\phi^X$ is locally one-dimensional". The bridge: in straightened coordinates the statement reduces to a check on $\partial/\partial s^1$. Use: the universality of the local model means you only have to verify the claim once.

The third disguised source is **a problem requiring a tubular neighbourhood or collar.** Property $B$: a submanifold $S \subseteq M$ and a nearby region you want to parametrize. The bridge: if $X$ is transverse to $S$, then the Flowout Theorem gives a tubular-neighbourhood parametrization $S \times (-\delta, \delta) \to M$ via the flow. The Straightening Theorem is the codimension-1 case. Use: collar neighbourhoods of boundary, tubular neighbourhoods of submanifolds, Morse-theoretic level sets — all built from this construction.

**Targets (Output Amplification)**

The conclusion is "coordinates exist in which $X = \partial/\partial s^1$". Combined with one further property, this amplifies.

The first combination is **straightening + smooth function gives invariant function detection.** Property $D$: a smooth function $f$ on $M$. The amplification: $\mathcal{L}_X f = Xf = \partial f / \partial s^1$ in straightened coordinates, so $f$ is conserved along the flow ($Xf \equiv 0$) iff $f$ depends only on $s^2, \dots, s^n$ in the straightened coordinates. This is the *local* statement of conservation laws.

The second combination is **straightening + commuting field gives joint canonical form.** Property $D$: $Y$ is another smooth vector field with $[X, Y] = 0$ and $Y_p \notin \mathrm{span}(X_p)$. The amplification: in straightened coordinates, $Y$ has the form $Y = Y^i \partial_i$ with the components depending only on $s^2, \dots, s^n$ (not on $s^1$) — by the commuting flows theorem, $\mathcal{L}_X Y = 0$ implies $\partial Y^i / \partial s^1 = 0$. This is the inductive step in Lee Theorem 9.46.

The third combination is **straightening + a transverse submanifold gives the Flowout Theorem.** Property $D$: an embedded submanifold $S$ of any dimension with $V$ nowhere tangent to $S$. The amplification (Lee 9.20): there is a flow domain $O \subseteq \mathbb{R} \times S$ such that the flow restricts to an immersion $O \to M$, and the image is a tubular-like neighbourhood of $S$.

---

# Why Is It True

**The mechanism in one sentence: pick a transverse hypersurface $S$ through $p$, parametrize $S$ by $(s^2, \dots, s^n)$, and define $s^1$ as the flow time from $S$ — the resulting coordinates straighten $X$ because flowing in the $s^1$ direction is flowing by $X$.**

Unpack this:

Choose smooth coordinates $(x^i)$ near $p$ with $x(p) = 0$ and with one of the components $X^j(0)$ nonzero — say $j = 1$. Let $S$ be the hypersurface $\{x^1 = 0\}$ near $p$. Since $X^1(p) \neq 0$, $X$ is transverse to $S$ at $p$, and (shrinking $S$) transverse on a neighbourhood of $p$ in $S$.

Parametrize $S$ by $\psi(a^2, \dots, a^n) = (0, a^2, \dots, a^n)$ — these are coordinates on $S$. Define the map $\Phi : (-\varepsilon, \varepsilon) \times W \to M$, where $W$ is a small neighbourhood of $0$ in $\mathbb{R}^{n-1}$, by

$$\Phi(t, a^2, \dots, a^n) := \phi^X_t(\psi(a^2, \dots, a^n)) = \phi^X_t(0, a^2, \dots, a^n),$$

i.e. start on $S$ at $\psi(a^2, \dots, a^n)$ and flow by $X$ for time $t$.

**Claim:** $\Phi$ is a diffeomorphism from a neighborhood of $(0, 0)$ onto a neighborhood of $p$. The differential of $\Phi$ at $(0, 0)$ sends:

- $\partial/\partial t$ to $X_{\psi(0)} = X_p$ (the time derivative of the flow at $t = 0$ is the vector field).
- $\partial/\partial a^i$ (for $i \geq 2$) to $\partial/\partial a^i \big|_{\psi(0)}$, which is tangent to $S$ at $p$.

The tuple $(X_p, \partial/\partial a^2|_p, \dots, \partial/\partial a^n|_p)$ is a basis of $T_p M$ because $X_p$ is transverse to $T_p S = \mathrm{span}(\partial/\partial a^2|_p, \dots, \partial/\partial a^n|_p)$. By the inverse function theorem, $\Phi$ is a local diffeomorphism.

Now declare $(s^1, s^2, \dots, s^n) := \Phi^{-1}$, so $s^1$ is the "flow time from $S$" and $s^i$ for $i \geq 2$ parametrize the starting point on $S$.

**Why is $X = \partial/\partial s^1$ in these coordinates?** Because the flow of $X$ in these coordinates is $\phi^X_t(s^1, s^2, \dots, s^n) = (s^1 + t, s^2, \dots, s^n)$ (by the very construction — flowing for time $t$ means advancing $s^1$ by $t$), so $X_p = \frac{d}{dt}\big|_{t=0} \phi^X_t(p)$ has coordinate $\partial/\partial s^1$.

The "hypersurface $S$" version of the theorem (with $s^1 = 0$ defining a specified hypersurface) follows by choosing the hypersurface $S$ to be the given one — the construction works for any $S$ transverse to $X$ at $p$.

The whole proof is the **transverse flow construction**, made possible by the Fundamental Theorem on Flows (which gives the flow) and the inverse function theorem (which certifies $\Phi$ is a local diffeomorphism). No additional machinery is needed.

---

# What Makes This Hard

The conceptual difficulty is recognizing that **the substance of the proof is in choosing the transverse hypersurface and parametrizing it**: once you set up $\Phi(t, a) = \phi^X_t(\psi(a))$, the rest is automatic from the Fundamental Theorem on Flows and the inverse function theorem. The most common error is to try to construct straightened coordinates *directly* from the components $X^i$ — a calculation that gets bogged down in ODE solutions. The transverse-flow viewpoint is the clean one.

A second subtle point: the theorem requires the point to be **regular** ($X_p \neq 0$). At singular points the theorem fails — and not because the proof breaks down for a fixable reason, but because the local structure of $X$ near a zero is genuinely much richer than the constant flow. The hyperbolic-saddle, the centre, the node, the focus — these are *all* possible local pictures at a zero, and no diffeomorphism converts one into another.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
At a regular point $p$, $X$ is transverse to some hypersurface $S$ through $p$. Parametrize a neighbourhood of $p$ via "flow time from $S$" + "starting point on $S$": the map $\Phi(t, a) = \phi^X_t(\psi(a))$, where $\psi$ parametrizes $S$. Show that $\Phi$ is a local diffeomorphism using the inverse function theorem; the inverse $\Phi^{-1}$ gives the straightened coordinates, in which $X = \partial/\partial s^1$ because flowing by $X$ for time $t$ advances $s^1$ by $t$.

**Subgoal decomposition:**

1. **Choose a transverse hypersurface.** Pick coordinates $(x^i)$ around $p$ with one component $X^j(p) \neq 0$; let $S = \{x^j = 0\}$.
   - *Hint:* The existence of such a component follows from $X_p \neq 0$. If the given hypersurface $S$ is provided, use it instead (the regularity check is that $X_p \notin T_p S$).
   - *Why needed:* Transversality is the geometric ingredient.

2. **Parametrize $S$.** Choose a smooth local parametrization $\psi : W \to S$ with $W \subseteq \mathbb{R}^{n-1}$.
   - *Hint:* In the simplest case, $\psi(a^2, \dots, a^n) = (0, a^2, \dots, a^n)$ in the chosen coordinates.
   - *Why needed:* Provides the "starting point on $S$" coordinate.

3. **Define the flow-from-$S$ map.** $\Phi : (-\varepsilon, \varepsilon) \times W \to M$, $\Phi(t, a) = \phi^X_t(\psi(a))$.
   - *Hint:* Smoothness comes from the Fundamental Theorem on Flows.
   - *Why needed:* This is the candidate coordinate chart.

4. **Verify $\Phi$ is a local diffeomorphism.** Compute $d\Phi_{(0, 0)}$ and show it is invertible.
   - *Hint:* $d\Phi_{(0,0)}(\partial/\partial t) = X_p$ (by definition of flow at $t=0$); $d\Phi_{(0,0)}(\partial/\partial a^i) = d\psi_0(\partial/\partial a^i) \in T_p S$ (tangent to $S$). The collection is a basis because $X_p$ is transverse to $T_p S$.
   - *Why needed:* Inverse function theorem gives the local diffeomorphism.

5. **Define the straightened coordinates.** $(s^1, \dots, s^n) := \Phi^{-1}$.
   - *Hint:* In these coordinates, $\phi^X_t$ shifts the first coordinate by $t$.
   - *Why needed:* This is the conclusion.

6. **Verify $X = \partial/\partial s^1$.** The flow in $s$-coordinates is $\phi^X_t(s) = (s^1 + t, s^2, \dots, s^n)$.
   - *Hint:* Differentiate at $t = 0$.
   - *Why needed:* This is the precise form of the canonical-form statement.

---

# Lemma Decomposition

> [!note]- Lemma 1: Transversality of $X$ to a hypersurface
> **Statement:** If $X_p \neq 0$, then there exists an embedded hypersurface $S$ through $p$ to which $X$ is transverse at $p$ (i.e. $X_p \notin T_p S$).
>
> **Hint:** In any chart with $X^j(p) \neq 0$, take $S = \{x^j = 0\}$.
>
> **Why needed:** Transversality is the geometric input to the flowout construction.
>
> > [!note]- Full proof
> > Pick a chart $(U, (x^i))$ centred at $p$ with $X_p \neq 0$. Since $X_p = X^i(p) \partial_i$ is nonzero, some component $X^j(p) \neq 0$. Take $S = \{q \in U : x^j(q) = 0\}$; this is an embedded hypersurface through $p$. Its tangent space at $p$ is the kernel of $dx^j_p$, which is $\{v \in T_p M : v^j = 0\}$. Since $X^j(p) \neq 0$, $X_p \notin T_p S$.

> [!note]- Lemma 2: The flow-from-transversal map is a local diffeomorphism
> **Statement:** Let $S \subseteq M$ be an embedded hypersurface through $p$ with $X_p \notin T_p S$. Choose a smooth local parametrization $\psi : W \to S$ with $\psi(0) = p$, $W$ open neighbourhood of $0$ in $\mathbb{R}^{n-1}$. Then the map $\Phi : (-\varepsilon, \varepsilon) \times W \to M$, $\Phi(t, a) = \phi^X_t(\psi(a))$, is a local diffeomorphism near $(0, 0)$ for $\varepsilon > 0$ small enough.
>
> **Hint:** Compute $d\Phi_{(0, 0)}$ and apply the inverse function theorem.
>
> **Why needed:** Provides the chart in which $X$ will be $\partial/\partial s^1$.
>
> > [!note]- Full proof
> > $\Phi$ is smooth: $\phi^X$ is smooth by the [[Thm - Fundamental Theorem on Flows]], $\psi$ is smooth by assumption, and composition of smooth maps is smooth.
> >
> > Compute $d\Phi_{(0, 0)} : T_{(0, 0)}((-\varepsilon, \varepsilon) \times W) \cong \mathbb{R}^n \to T_p M$:
> > - $d\Phi_{(0,0)}(\partial/\partial t) = \frac{d}{dt}\big|_{t=0} \Phi(t, 0) = \frac{d}{dt}\big|_{t=0} \phi^X_t(\psi(0)) = X_{\psi(0)} = X_p$.
> > - $d\Phi_{(0,0)}(\partial/\partial a^i) = \frac{d}{da^i}\big|_{a=0} \Phi(0, a) = \frac{d}{da^i}\big|_{a=0} \psi(a) = d\psi_0(\partial/\partial a^i)$ — tangent to $S$ at $p$.
> >
> > Since $X_p \notin T_p S$ and $(d\psi_0(\partial/\partial a^i))$ is a basis of $T_p S$ (because $\psi$ is a local parametrization), $\{X_p\} \cup (d\psi_0(\partial/\partial a^i))_{i = 2, \dots, n}$ is a basis of $T_p M$. Hence $d\Phi_{(0,0)}$ is invertible, and by the inverse function theorem $\Phi$ is a local diffeomorphism near $(0, 0)$.

> [!note]- Lemma 3: Straightened coordinates produce $X = \partial/\partial s^1$
> **Statement:** Let $(s^1, \dots, s^n) := \Phi^{-1}$ where $\Phi$ is from Lemma 2. Then $X = \partial/\partial s^1$ in these coordinates.
>
> **Hint:** In $s$-coordinates the flow is $\phi^X_t(s^1, \dots, s^n) = (s^1 + t, s^2, \dots, s^n)$. Differentiate.
>
> **Why needed:** Completes the verification that the constructed coordinates are straightening coordinates.
>
> > [!note]- Full proof
> > In $s$-coordinates, $\Phi(t, a) = (t, a^2, \dots, a^n)$ — that is, $s^1(\Phi(t, a)) = t$ and $s^i(\Phi(t, a)) = a^i$ for $i \geq 2$. So the flow of $X$ acts as $\phi^X_t : (s^1, s^2, \dots, s^n) \mapsto (s^1 + t, s^2, \dots, s^n)$ in these coordinates.
> >
> > By definition of the infinitesimal generator, $X_q = \frac{d}{dt}\big|_{t=0} \phi^X_t(q)$. In $s$-coordinates: $\frac{d}{dt}\big|_{t=0} (s^1 + t, s^2, \dots, s^n) = (1, 0, \dots, 0) = \partial/\partial s^1$. Hence $X = \partial/\partial s^1$ everywhere in the straightened chart.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — Transverse hypersurface.** Let $X_p \neq 0$. By Lemma 1, there is an embedded hypersurface $S \subseteq M$ through $p$ with $X_p \notin T_p S$. If the theorem's optional hypothesis "a hypersurface $S$ through $p$ with $X_p \notin T_p S$ is given" is in force, use that $S$ instead.
>
> **Step 1 — Parametrize $S$.** Choose a smooth local parametrization $\psi : W \to S$ with $\psi(0) = p$, $W \subseteq \mathbb{R}^{n-1}$ open.
>
> **Step 2 — Construct the flow-from-$S$ map.** By the [[Thm - Fundamental Theorem on Flows]], the flow $\phi^X$ is defined and smooth on an open subset of $\mathbb{R} \times M$ containing $\{0\} \times M$. Choose $\varepsilon > 0$ small enough that $(-\varepsilon, \varepsilon) \times \psi(W) \subseteq \mathcal{D}_{\phi^X}$ (the flow domain). Define $\Phi : (-\varepsilon, \varepsilon) \times W \to M$, $\Phi(t, a) := \phi^X_t(\psi(a))$.
>
> **Step 3 — $\Phi$ is a local diffeomorphism.** By Lemma 2, $\Phi$ is a local diffeomorphism near $(0, 0)$. Shrink $W$ and $\varepsilon$ as needed so $\Phi$ is a diffeomorphism onto its image (an open subset $V \subseteq M$ containing $p$).
>
> **Step 4 — Define straightened coordinates.** Let $(s^1, s^2, \dots, s^n) := \Phi^{-1} : V \to (-\varepsilon, \varepsilon) \times W$. By construction, the slice $\{s^1 = 0\}$ is exactly $\psi(W) \subseteq S$.
>
> **Step 5 — Verify $X = \partial/\partial s^1$.** By Lemma 3, in these coordinates the flow of $X$ is $\phi^X_t(s^1, \dots, s^n) = (s^1 + t, s^2, \dots, s^n)$, and differentiating at $t = 0$ gives $X = \partial/\partial s^1$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Local form of geodesics on a Riemannian manifold.** The geodesic spray on $TM$ is a vector field on the tangent bundle; near any point $(p, v) \in TM$ with $v \neq 0$, the geodesic spray is straightening-equivalent to $\partial/\partial s^1$. The geodesic-completeness question becomes whether the flow of the spray is global, which the Straightening Theorem reduces to questions about behaviour as one approaches the boundary of $TM$.

**Reduction of an autonomous ODE to a quadrature.** If $X$ is a nonvanishing autonomous vector field on $\mathbb{R}^n$, the Straightening Theorem locally reduces the ODE $\dot x = X(x)$ to the trivial ODE $\dot s^1 = 1$, $\dot s^i = 0$. The "quadrature" — finding the integral curve by integration — is exactly the inverse of the straightening map. In dynamical systems this is the local rectifiability theorem.

**The Frobenius theorem as a multi-field straightening.** The [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|Frobenius theorem]] is the multi-field generalization: a smooth involutive subbundle $D \subseteq TM$ of rank $k$ is locally tangent to coordinate slices $\{s^{k+1} = c^{k+1}, \dots, s^n = c^n\}$ in suitable coordinates. The rank-1 case is the Straightening Theorem. The proof in the general case uses the bracket-closure to commute the flows of a chosen basis of $D$ until they jointly straighten.

**Existence of action-angle coordinates in integrable systems.** A completely integrable Hamiltonian system has $n$ commuting Hamiltonian flows on a $2n$-dimensional symplectic manifold. By the multi-field straightening theorem (Lee 9.46), in a neighborhood of a regular orbit there are coordinates in which each of these flows becomes $\partial/\partial s^i$ — these are the **angle coordinates**. The action coordinates are the conserved Hamiltonians, complementing the angles. The Liouville–Arnold theorem upgrades this local statement to a global one.

---

# Bridges

- **[[Thm - Fundamental Theorem on Flows]]** — the prerequisite. The flow $\phi^X$ used in the flowout construction is provided by the Fundamental Theorem; the smoothness of $\phi^X$ is what makes the map $\Phi(t, a) = \phi^X_t(\psi(a))$ smooth, and the inverse function theorem then certifies it is a local diffeomorphism.

- **Inverse function theorem** — the technical tool. The proof that $\Phi$ is a local diffeomorphism uses the inverse function theorem applied to a smooth map between equal-dimensional manifolds with invertible differential at a point. This is the typical pattern for "construct a local diffeomorphism" arguments in differential geometry.

- **[[Thm - Commuting Flows Theorem]] + the Straightening Theorem combine to the multi-field canonical form.** Lee Theorem 9.46 says $k$ linearly independent commuting smooth vector fields $V_1, \dots, V_k$ on $M$ jointly straighten to $V_i = \partial/\partial s^i$ in suitable coordinates. The proof iteratively applies the single-field straightening: straighten $V_1$ first; the commutativity ensures the components of the other $V_j$ in straightened coordinates do not depend on $s^1$; iterate.

- **[[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|Frobenius theorem]]** — the non-commuting generalization. For a distribution $D \subseteq TM$ that is involutive (closed under bracket), there are coordinates in which $D$ is spanned by $\partial/\partial s^1, \dots, \partial/\partial s^k$. The single-field case ($\dim D = 1$) is *automatic* — every rank-1 distribution is involutive (the bracket of a section with itself is zero), so the rank-1 Frobenius theorem reduces to the Straightening Theorem. The proof in general builds on the Straightening Theorem plus a non-trivial argument to "commute" the basis vectors via local change.

- **Flowout Theorem (Lee 9.20)** — the codimension-$k$ generalization of the Straightening Theorem. Flowing a $k$-dimensional submanifold $S$ along a transverse vector field produces a tubular-like neighbourhood. The Straightening Theorem is the codimension-1 transversal version, where the submanifold $S$ is the hypersurface $\{s^1 = 0\}$ in the straightened chart.

---

# Unlocked by This

> [!tip] Canonical Form for Commuting Vector Fields *(Lee 9.46)*
> Multi-field generalization: $k$ linearly independent commuting smooth vector fields jointly straighten to $\partial/\partial s^1, \dots, \partial/\partial s^k$. This combines the single-field Straightening Theorem with the [[Thm - Commuting Flows Theorem]]. It is the rank-$k$ version of "all such things look the same locally".

> [!tip] Frobenius Theorem *(from Distribution Theory)*
> Generalization to non-commuting fields: any *involutive* smooth distribution $D \subseteq TM$ (closed under bracket) is locally tangent to coordinate slices. See [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]]. The Straightening Theorem is the rank-1 case where involutivity is automatic. The non-commuting case requires a deeper argument: even if the bracket of two sections is not zero, as long as it lies in the distribution, the distribution can still be integrated.

> [!tip] Tubular Neighborhood Theorem *(from Differential Topology)*
> Every embedded submanifold $S \subseteq M$ has an open neighborhood diffeomorphic to the **normal bundle** $NS$. The proof exhibits a tubular structure by flowing transverse vector fields out of $S$; the Straightening Theorem is the codimension-1 special case. Tubular neighbourhoods are the basic tool of differential topology, used in everything from Morse theory to the Thom transversality theorem.

> [!tip] Phase Portrait at Equilibria *(from Dynamical Systems)*
> The Straightening Theorem fails at singular points ($X_p = 0$), and the local structure of $X$ near a zero is the entire qualitative theory of **phase portraits**: hyperbolic equilibria (saddle, source, sink, focus), bifurcations, stable and unstable manifolds. The Hartman–Grobman theorem says the local phase portrait near a hyperbolic equilibrium is topologically conjugate to the linearization of $X$ — the analogue of the Straightening Theorem at zeros, but only up to topological conjugacy, not diffeomorphism.
