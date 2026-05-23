---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Vector Field"
  - "Def - Flow of a Vector Field"
  - "Def - The Lie Bracket of Vector Fields"
  - "Def - Lie Derivative of a Vector Field"
  - "Thm - Lie Bracket Properties"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth manifold, $X, Y \in \mathfrak{X}(M)$ smooth [[Def - Smooth Vector Field|vector fields]] with flows $\phi^X, \phi^Y$. Two flows $\phi$ and $\psi$ on $M$ are said to **commute** if for every $p \in M$ and every pair of open intervals $J, K$ containing $0$ such that one of $\phi_t \psi_s(p)$ or $\psi_s \phi_t(p)$ is defined for all $(s, t) \in J \times K$, both are defined and equal. For global flows this reduces to $\phi_t \circ \psi_s = \psi_s \circ \phi_t$ for all $s, t$. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]] for the full notation registry.

---

# Statement

> **Theorem (Commuting Flows; Lee Theorems 9.42 and 9.44).** Let $X, Y \in \mathfrak{X}(M)$ be smooth vector fields with flows $\phi$ and $\psi$. The following are equivalent:
>
> (a) **Bracket vanishes.** $[X, Y] = 0$.
>
> (b) **$Y$ invariant under flow of $X$.** $d(\phi_t)_p(Y_p) = Y_{\phi_t(p)}$ for all $(t, p)$ in the flow domain of $\phi$.
>
> (c) **$X$ invariant under flow of $Y$.** $d(\psi_s)_p(X_p) = X_{\psi_s(p)}$ for all $(s, p)$ in the flow domain of $\psi$.
>
> (d) **Flows commute.** $\phi_t \circ \psi_s = \psi_s \circ \phi_t$ wherever defined (in the precise sense above).

---

# Motivation

This is the **geometric soul** of the Lie bracket. The algebraic definition $[X, Y]f = X(Yf) - Y(Xf)$ is operationally useful for computations, but it leaves the *meaning* of the bracket obscure — why should this particular commutator of derivations be the central operation on $\mathfrak{X}(M)$? The Commuting Flows Theorem answers: because **the bracket measures the failure of flows to commute**. If $[X, Y] = 0$, the flows commute exactly; if $[X, Y] \neq 0$, they fail to commute, and the failure is, to leading order, exactly $[X, Y]$.

This is the *trigger-reaction pattern* of differential geometry: **when you see "commuting flows", compute the Lie bracket — the bracket vanishes if and only if the flows commute.** And conversely, **when you see "Lie bracket is zero", flows commute**. The theorem is the bridge between algebra and geometry, and it is the source of every "involutivity implies integrability" result downstream.

The intuition is the **parallelogram**: starting at $p$, flow along $X$ for time $s$ to reach $\phi^X_s(p)$, then along $Y$ for time $t$ to reach $\phi^Y_t \phi^X_s(p)$. Now run the parallelogram from the other corner: along $Y$ for time $t$ to reach $\phi^Y_t(p)$, then along $X$ for time $s$ to reach $\phi^X_s \phi^Y_t(p)$. The two corners coincide for all $(s, t)$ if and only if the parallelogram closes, which is equivalent to $[X, Y] = 0$.

The four equivalent characterizations (a)–(d) play different roles. (a) is computational: write down the bracket and check. (b) and (c) are geometric: check whether one vector field is dragged unchanged along the flow of the other. (d) is *the* geometric content: the flows commute. The theorem says all four are equivalent, so any one of them can be checked to verify the others.

Why is this the right theorem to prove? Because it provides the structural justification for *every* multi-flow construction in differential geometry. The Straightening Theorem ([[Thm - Canonical Form for a Nonvanishing Vector Field]]) handles single nonvanishing fields; the multi-field generalization (canonical form for commuting frames) requires commuting flows; the [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|Frobenius theorem]] generalizes to non-commuting fields but still requires the bracket-closure (involutivity). All of these rest on the Commuting Flows Theorem.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$[X, Y] = 0$" (and dually). The skill is recognizing when bracket-vanishing is in disguise.

The first disguised source is **two flows known to commute geometrically.** Property $B$: a problem says "$\phi_t \circ \psi_s = \psi_s \circ \phi_t$ for all $(s, t)$" or describes a setup with this property (e.g., two commuting group actions on $M$). The bridge: $[X, Y] = 0$. Use: any subsequent bracket calculation is automatically zero; any "involutivity" check is automatically passed. This is the common case: an obvious flow-commutation gives a free bracket-vanishing.

The second disguised source is **two coordinate vector fields.** Property $B$: $X = \partial/\partial x^i$ and $Y = \partial/\partial x^j$ in some chart. The bridge: $[X, Y] = 0$ by the coordinate formula (or by equality of mixed partial derivatives). Use: the flows of two coordinate vector fields commute, and this is the source of the multi-field canonical form (commuting frames are coordinate frames).

The third disguised source is **two left-invariant vector fields on an abelian Lie group.** Property $B$: $X, Y \in \mathfrak{g}$ on a Lie group $G$ with $G$ abelian. The bridge: $[X, Y] = 0$ because the Lie algebra of an abelian Lie group is abelian (Lee 8.40 and Problem 8-25). Use: the exponential map is a homomorphism, $\exp(X + Y) = \exp(X)\exp(Y)$ — see [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

The fourth disguised source is **a vector field along its own flow.** Property $B$: $X = X$ (the trivial case). The bridge: $[X, X] = 0$ by antisymmetry. Use: every vector field is invariant under its own flow ($\phi^X_t$-related to itself for all $t$) — a special case of the theorem, often used without invocation.

**Targets (Output Amplification)**

The conclusion is "the four conditions are equivalent". Combined with one further property, the equivalence amplifies into structural results.

The first combination is **commuting flows + linear independence gives a joint canonical form.** Property $D$: $X_1, \dots, X_k$ are linearly independent commuting smooth vector fields ($[X_i, X_j] = 0$ for all $i, j$). The amplification (Lee Theorem 9.46): there are local coordinates $(s^1, \dots, s^n)$ such that $X_i = \partial/\partial s^i$ for $i = 1, \dots, k$. Single-field straightening generalises to multi-field straightening when the fields commute. This is the multi-field [[Thm - Canonical Form for a Nonvanishing Vector Field]].

The second combination is **commuting flows + group structure gives a torus action.** Property $D$: $X_1, \dots, X_k$ are complete commuting smooth vector fields with periodic flows of period $2\pi$. The amplification: the joint flow defines a smooth action of the torus $T^k = (\mathbb{R}/2\pi\mathbb{Z})^k$ on $M$ — a Hamiltonian torus action in symplectic geometry, or a torus subgroup of $\mathrm{Diff}(M)$ in general. Torus actions are the central object of equivariant topology.

The third combination is **commuting flows + Lie algebra closure gives an integrable distribution.** Property $D$: a smooth subbundle $D \subseteq TM$ such that for every pair of sections $X, Y \in \Gamma(D)$, $[X, Y] \in \Gamma(D)$ (involutivity). The amplification (the [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|Frobenius theorem]]): $D$ is integrable — tangent to a foliation. In the rank-$1$ case, this reduces to the Straightening Theorem; in the case of a commuting frame, this is the multi-field canonical form.

---

# Why Is It True

**The mechanism in one sentence: the bracket is the Lie derivative ($\mathcal{L}_X Y = [X, Y]$), so $[X, Y] = 0$ exactly when $Y$ is invariant under the flow of $X$; flow invariance of $Y$ along $\phi^X$ is equivalent to the flows commuting, because flow invariance is precisely "$Y$ is pushed to itself, so the curves of $Y$ are mapped to curves of $Y$".**

Unpack this:

**(a) ⟺ (b).** By the Lie derivative identification (Lemma 5 of [[Thm - Lie Bracket Properties]]), $[X, Y] = \mathcal{L}_X Y$. Now $\mathcal{L}_X Y = 0$ at every point if and only if $d(\phi^X_{-t})_{\phi^X_t(p)}(Y_{\phi^X_t(p)}) = Y_p$ for all $(t, p)$ — which is exactly the statement that $Y$ is invariant under the flow of $X$. So (a) and (b) are equivalent.

(For a fully geometric route without invoking the Lie derivative: Proposition 9.41 of Lee shows the derivative of the time-dependent pullback $X(t) := d(\phi_{-t})_{\phi_t(p)}(Y_{\phi_t(p)})$ at $t = t_0$ equals $d(\phi_{-t_0}) \cdot (\mathcal{L}_X Y)_{\phi_{t_0}(p)}$, so $\mathcal{L}_X Y \equiv 0$ implies $X(t)$ is constant in $t$; since $X(0) = Y_p$, this gives flow invariance.)

**(a) ⟺ (c).** By antisymmetry, $[X, Y] = 0 \iff [Y, X] = 0$; apply (a)⟺(b) with the roles of $X$ and $Y$ swapped.

**(b) ⟹ (d).** Suppose $Y$ is invariant under $\phi^X$. Fix $p \in M$. The curve $t \mapsto \phi^X_{-s} \circ \psi^Y_t \circ \phi^X_s(p)$ starts at $\phi^X_{-s}(\phi^X_s(p)) = p$ (using the group law for $\phi^X$) and its velocity at $t$ is

$$\frac{d}{dt}\left(\phi^X_{-s}(\psi^Y_t(\phi^X_s(p)))\right) = d(\phi^X_{-s})_{\psi^Y_t(\phi^X_s(p))}\left(Y_{\psi^Y_t(\phi^X_s(p))}\right) = Y_{\phi^X_{-s} \psi^Y_t \phi^X_s(p)},$$

using the invariance of $Y$ in the last step. So this curve is an integral curve of $Y$ starting at $p$, hence by uniqueness equals $\psi^Y_t(p)$. So $\phi^X_{-s} \circ \psi^Y_t \circ \phi^X_s(p) = \psi^Y_t(p)$, i.e. $\psi^Y_t \circ \phi^X_s = \phi^X_s \circ \psi^Y_t$ on the appropriate domain.

**(d) ⟹ (b).** Suppose flows commute: $\phi^X_s \circ \psi^Y_t = \psi^Y_t \circ \phi^X_s$ on appropriate domain. For small $s, t$ both sides are defined, and differentiating both sides in $t$ at $t = 0$:

$$\frac{d}{dt}\bigg|_{t=0} \phi^X_s(\psi^Y_t(p)) = d(\phi^X_s)_p(Y_p),$$

$$\frac{d}{dt}\bigg|_{t=0} \psi^Y_t(\phi^X_s(p)) = Y_{\phi^X_s(p)}.$$

So $d(\phi^X_s)_p(Y_p) = Y_{\phi^X_s(p)}$ for small $s$, i.e. $Y$ is invariant under $\phi^X$ in a neighborhood of $0$. The same argument with the roles of $s, t$ swapped extends the invariance globally.

So all four are equivalent.

---

# What Makes This Hard

Where most people get stuck is **the equivalence (b) ⟹ (d)**: it requires the careful curve-construction argument with $\phi^X_{-s} \circ \psi^Y_t \circ \phi^X_s$ and the use of flow invariance at every $t$ to identify this as an integral curve of $Y$. The most common error is to think that flow invariance "at $t = 0$" (i.e. just the bracket vanishing pointwise) is enough — but the geometric content requires invariance for *all* $t$ in the flow domain, and the Lie derivative identification is what gives the all-$t$ statement from the pointwise bracket. A second subtlety is the domain question for flows that are not global: "$\phi_t \circ \psi_s = \psi_s \circ \phi_t$" makes sense only on appropriate domains, and the precise statement of "(d) flows commute" must handle this delicately.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
The key bridge is the Lie derivative identification $\mathcal{L}_X Y = [X, Y]$. (a)⟺(b) follows from $\mathcal{L}_X Y = 0$ ⟺ $Y$ invariant under $\phi^X$. (a)⟺(c) is the dual (swap $X$ and $Y$ using antisymmetry). (b)⟹(d) constructs the curve $t \mapsto \phi^X_{-s} \psi^Y_t \phi^X_s(p)$ and shows it is the integral curve of $Y$ from $p$. (d)⟹(b) differentiates the commutation $\phi^X_s \circ \psi^Y_t = \psi^Y_t \circ \phi^X_s$ in $t$ at $t = 0$.

**Subgoal decomposition:**

1. **(a) ⟺ (b).** Use $\mathcal{L}_X Y = [X, Y]$ and the definition of $\mathcal{L}_X Y$.
   - *Hint:* $\mathcal{L}_X Y = 0$ pointwise ⟺ $d(\phi^X_{-t})_{\phi^X_t(p)}(Y_{\phi^X_t(p)}) = Y_p$ for all $(t, p)$ in flow domain ⟺ $Y$ invariant under $\phi^X$. The "for all $t$" part uses Proposition 9.41 of Lee: $\mathcal{L}_X Y = 0$ pointwise gives constancy of the pullback at every time, not just $t = 0$.
   - *Why needed:* This is the bridge between the algebraic and geometric pictures of the bracket.

2. **(a) ⟺ (c).** Use antisymmetry of the bracket.
   - *Hint:* $[X, Y] = 0 \iff [Y, X] = 0$ by antisymmetry. Apply step 1 with $X, Y$ swapped.
   - *Why needed:* Gives the dual statement and symmetry of the theorem.

3. **(b) ⟹ (d).** Construct the curve $t \mapsto \phi^X_{-s} \psi^Y_t \phi^X_s(p)$ and show it equals $\psi^Y_t(p)$.
   - *Hint:* Differentiate the curve in $t$ using flow invariance of $Y$; result is $Y$ evaluated at the curve point. So the curve is an integral curve of $Y$, hence by uniqueness equals $\psi^Y_t(p)$.
   - *Why needed:* Promotes pointwise flow invariance of $Y$ to global flow commutation.

4. **(d) ⟹ (b).** Differentiate the commutation $\phi^X_s \circ \psi^Y_t = \psi^Y_t \circ \phi^X_s$ in $t$ at $t = 0$.
   - *Hint:* Apply $\frac{d}{dt}\big|_{t=0}$ to both sides; left gives $d(\phi^X_s)_p(Y_p)$, right gives $Y_{\phi^X_s(p)}$. Hence flow invariance.
   - *Why needed:* Closes the equivalence loop.

---

# Lemma Decomposition

> [!note]- Lemma 1: Flow invariance is equivalent to bracket vanishing
> **Statement:** $Y$ is invariant under the flow of $X$ — i.e. $d(\phi^X_t)_p(Y_p) = Y_{\phi^X_t(p)}$ for all $(t, p)$ in the flow domain of $\phi^X$ — if and only if $[X, Y] = 0$.
>
> **Hint:** Use the Lie derivative identification $\mathcal{L}_X Y = [X, Y]$ and Proposition 9.41 of Lee.
>
> **Why needed:** This is the (a) ⟺ (b) part of the theorem, the central bridge between algebra and geometry.
>
> > [!note]- Full proof
> > *($\Leftarrow$)* If $Y$ is invariant under $\phi^X$, then $d(\phi^X_{-t})_{\phi^X_t(p)}(Y_{\phi^X_t(p)}) = Y_p$ for every $(t, p)$ in the flow domain (this is the equivalent form). The right-hand side is constant in $t$; differentiating at $t = 0$ gives $(\mathcal{L}_X Y)_p = 0$ for every $p$, i.e. $\mathcal{L}_X Y = 0$. By $\mathcal{L}_X Y = [X, Y]$ (Lemma 5 of [[Thm - Lie Bracket Properties]]), $[X, Y] = 0$.
> >
> > *($\Rightarrow$)* Conversely, suppose $[X, Y] = 0$, hence $\mathcal{L}_X Y = 0$. By Lee Proposition 9.41, $\frac{d}{dt} \big|_{t = t_0} d(\phi^X_{-t})_{\phi^X_t(p)}(Y_{\phi^X_t(p)}) = d(\phi^X_{-t_0})_{\phi^X_{t_0}(p)} ((\mathcal{L}_X Y)_{\phi^X_{t_0}(p)}) = 0$ for every $t_0$. So the function $t \mapsto d(\phi^X_{-t})_{\phi^X_t(p)}(Y_{\phi^X_t(p)})$ is constant in $t$, equal to its value at $t = 0$, which is $Y_p$. Hence $d(\phi^X_{-t})_{\phi^X_t(p)}(Y_{\phi^X_t(p)}) = Y_p$ for every $(t, p)$, which (applying $d(\phi^X_t)_p$ to both sides) is exactly flow invariance of $Y$.

> [!note]- Lemma 2: Flow invariance gives flow commutation
> **Statement:** If $Y$ is invariant under the flow of $X$, then the flows of $X$ and $Y$ commute (in the precise sense).
>
> **Hint:** Fix $p$, $s$. Show that $t \mapsto \phi^X_{-s}(\psi^Y_t(\phi^X_s(p)))$ is an integral curve of $Y$ starting at $p$; by uniqueness, equals $\psi^Y_t(p)$.
>
> **Why needed:** This is the (b) ⟹ (d) implication.
>
> > [!note]- Full proof
> > Let $p \in M$ and $s \in \mathcal{D}^{(p)}_{\phi^X}$ (the flow domain of $\phi^X$). Define $\sigma(t) := \phi^X_{-s}(\psi^Y_t(\phi^X_s(p)))$ on the appropriate $t$-interval. Then $\sigma(0) = \phi^X_{-s}(\phi^X_s(p)) = p$ by the group law for $\phi^X$.
> >
> > Differentiate:
> > $$\sigma'(t) = \frac{d}{dt} \phi^X_{-s}(\psi^Y_t(\phi^X_s(p))) = d(\phi^X_{-s})_{\psi^Y_t(\phi^X_s(p))}\left(\frac{d}{dt}\psi^Y_t(\phi^X_s(p))\right) = d(\phi^X_{-s})_{\psi^Y_t(\phi^X_s(p))}(Y_{\psi^Y_t(\phi^X_s(p))}),$$
> > where the last step uses that $\psi^Y_t$ is the flow of $Y$. By flow invariance of $Y$ under $\phi^X$ applied to the point $\psi^Y_t(\phi^X_s(p))$ with time $-s$:
> > $$d(\phi^X_{-s})_{\psi^Y_t(\phi^X_s(p))}(Y_{\psi^Y_t(\phi^X_s(p))}) = Y_{\phi^X_{-s}(\psi^Y_t(\phi^X_s(p)))} = Y_{\sigma(t)}.$$
> > So $\sigma'(t) = Y_{\sigma(t)}$: $\sigma$ is an integral curve of $Y$ starting at $p$. By uniqueness of integral curves ([[Thm - Existence and Uniqueness of Integral Curves]]), $\sigma(t) = \psi^Y_t(p)$, i.e. $\phi^X_{-s}(\psi^Y_t(\phi^X_s(p))) = \psi^Y_t(p)$, equivalently $\psi^Y_t(\phi^X_s(p)) = \phi^X_s(\psi^Y_t(p))$.

> [!note]- Lemma 3: Flow commutation gives flow invariance
> **Statement:** If $\phi^X_s \circ \psi^Y_t = \psi^Y_t \circ \phi^X_s$ on appropriate domain, then $Y$ is invariant under the flow of $X$.
>
> **Hint:** Differentiate the commutation in $t$ at $t = 0$.
>
> **Why needed:** This is the (d) ⟹ (b) implication, closing the equivalence loop.
>
> > [!note]- Full proof
> > Fix $p \in M$ and let $s$ be in the flow domain of $\phi^X$ from $p$. For small $|t|$, both sides $\phi^X_s(\psi^Y_t(p))$ and $\psi^Y_t(\phi^X_s(p))$ are defined and equal. Differentiate in $t$ at $t = 0$:
> > $$\frac{d}{dt}\bigg|_{t=0} \phi^X_s(\psi^Y_t(p)) = d(\phi^X_s)_{\psi^Y_0(p)}\left(\frac{d}{dt}\big|_{t=0}\psi^Y_t(p)\right) = d(\phi^X_s)_p(Y_p),$$
> > $$\frac{d}{dt}\bigg|_{t=0} \psi^Y_t(\phi^X_s(p)) = Y_{\phi^X_s(p)}.$$
> > Hence $d(\phi^X_s)_p(Y_p) = Y_{\phi^X_s(p)}$, which is flow invariance of $Y$ at $(s, p)$. Varying $p$ and $s$ over the flow domain, this holds throughout.

---

# Formal Proof

> [!note]- Complete formal proof
> By Lemma 1, (a) $[X, Y] = 0$ is equivalent to (b) $Y$ invariant under $\phi^X$. By antisymmetry $[X, Y] = -[Y, X]$, so (a) is also equivalent to $[Y, X] = 0$, which by Lemma 1 (with roles swapped) is equivalent to (c) $X$ invariant under $\psi^Y$. By Lemma 2, (b) implies (d) flows commute. By Lemma 3, (d) implies (b). So all four are equivalent. $\qquad\blacksquare$
>
> **Corollary.** Every vector field is invariant under its own flow: take $Y = X$ in the theorem; then $[X, X] = 0$ by antisymmetry, so by (b) $X$ is invariant under its own flow. (This is Lee Corollary 9.43.)

---

# Cross-Field Exercise Suggestions

**Torus action on a manifold from commuting periodic flows.** If $X_1, \dots, X_n$ are linearly independent commuting smooth complete vector fields on $M$ with periodic flows of period $2\pi$, then their joint flow defines a smooth action of the torus $T^n = (\mathbb{R}/2\pi\mathbb{Z})^n$ on $M$. The commutativity assumption is what makes the joint flow well-defined as a $T^n$-action; without it, only an $\mathbb{R}^n$-action emerges. This is the geometric source of toric symplectic geometry — see Atiyah and Guillemin–Sternberg's convexity theorems.

**Symmetries of a Hamiltonian system.** In Hamiltonian mechanics, a function $F : T^*M \to \mathbb{R}$ that Poisson-commutes with the Hamiltonian $H$ — $\{F, H\} = 0$ — gives a conserved quantity. The Hamiltonian flows of $F$ and $H$ commute (by $[X_F, X_H] = -X_{\{F, H\}} = 0$), so the flow of $F$ is a symmetry of the dynamics of $H$. The Commuting Flows Theorem is what licences this geometric interpretation of Poisson-commuting observables.

**Action-angle coordinates on a completely integrable system.** A Hamiltonian system on a $2n$-dimensional symplectic manifold is **completely integrable** if it has $n$ independent commuting conserved quantities. The Liouville–Arnold theorem says the joint level sets of these quantities are diffeomorphic to tori, and on these tori the system is conjugate to a linear flow. The Commuting Flows Theorem certifies that the joint flow is a torus action, and the existence of action-angle coordinates is the multi-field Straightening Theorem (Lee 9.46) applied to the commuting Hamiltonian flows.

**Linear flows on the torus.** On $T^n = \mathbb{R}^n / \mathbb{Z}^n$, the constant-coefficient vector fields $X_a = a^i \partial_i$ all commute pairwise. The flow of $X_a$ is the linear flow $\phi^a_t(\theta) = \theta + ta$, and these commute. The full toric symmetry $T^n \times T^n \to T^n$ is the joint flow of an abelian Lie algebra of commuting vector fields. The bracket condition is automatic from the abelian Lie algebra structure.

---

# Bridges

- **[[Thm - Lie Bracket Properties]]** — the proof of this theorem uses the Lie derivative identification $\mathcal{L}_X Y = [X, Y]$ (part (g) of the bracket properties theorem) as the central bridge. Without that identification, the algebraic condition $[X, Y] = 0$ would not connect to the geometric condition of flow invariance.

- **[[Thm - Canonical Form for a Nonvanishing Vector Field|Straightening Theorem]]** — the single-field version of "canonical form for commuting fields". The multi-field generalization (Lee Theorem 9.46) says $k$ linearly independent commuting vector fields jointly straighten to $\partial/\partial s^1, \dots, \partial/\partial s^k$. The proof uses the commutativity to compose the flows in any order, and this is the structural content of the Commuting Flows Theorem.

- **[[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|Frobenius theorem]]** — the natural generalization to non-commuting fields. A distribution $D \subseteq TM$ is **involutive** if $[X, Y] \in \Gamma(D)$ for $X, Y \in \Gamma(D)$. Frobenius says involutive distributions are integrable (tangent to a foliation), and the proof uses the multi-field straightening when commutativity is achievable by local change of basis. The single-field case of Frobenius is the Straightening Theorem; the commuting case is the multi-field Straightening; the general involutive case is Frobenius proper.

- **[[Def - Lie Derivative of a Vector Field|Lie derivative]]** — the meaning of (b) and (c). $\mathcal{L}_X Y = 0$ is exactly "$Y$ is invariant under the flow of $X$", and the Commuting Flows Theorem connects this to bracket-vanishing and to flow commutation.

- **Lie's third theorem** — a global converse of sorts. Every finite-dimensional Lie algebra integrates to a connected simply-connected Lie group. The proof requires assembling commuting flows of left-invariant vector fields into a coherent group operation; the Commuting Flows Theorem is the prerequisite that lets you make sense of "commuting flows of commuting fields" globally.

---

# Unlocked by This

> [!tip] Canonical Form for Commuting Vector Fields *(within this chapter, Lee 9.46)*
> Given $k$ linearly independent commuting smooth vector fields $V_1, \dots, V_k$ on $M$, there are local coordinates $(s^1, \dots, s^n)$ in which $V_i = \partial/\partial s^i$ for $i = 1, \dots, k$. This is the multi-field generalization of [[Thm - Canonical Form for a Nonvanishing Vector Field]]; the commutativity is what licenses the coordinate construction.

> [!tip] Frobenius Theorem *(from Distributions)*
> A smooth distribution $D \subseteq TM$ is **integrable** (tangent to a foliation) if and only if it is **involutive** ($[X, Y] \in \Gamma(D)$ for $X, Y \in \Gamma(D)$). See [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]]. The Commuting Flows Theorem is the rank-one ancestor: bracket vanishing of a single pair of fields is the bracket-closure condition on the span of those two fields, and the canonical-form coordinates are the integral leaves.

> [!tip] Hamiltonian Torus Action *(from Symplectic Geometry)*
> Commuting periodic Hamiltonian flows assemble into a smooth **torus action** $T^n \to \mathrm{Symp}(M, \omega)$ on a symplectic manifold. The Atiyah–Guillemin–Sternberg convexity theorem says the momentum map image is a convex polytope; the toric setting is when the torus has half the dimension of the manifold. The Commuting Flows Theorem certifies the underlying $T^n$-action exists.
