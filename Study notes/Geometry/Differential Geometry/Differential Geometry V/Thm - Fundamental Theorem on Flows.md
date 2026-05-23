---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Vector Field"
  - "Def - Integral Curve of a Vector Field"
  - "Def - Flow of a Vector Field"
  - "Thm - Existence and Uniqueness of Integral Curves"
  - "Thm - The Contraction Mapping Principle"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth manifold, $X \in \mathfrak{X}(M)$ a smooth [[Def - Smooth Vector Field|vector field]]. $\gamma^{(p)} : \mathcal{D}^{(p)} \to M$ is the maximal [[Def - Integral Curve of a Vector Field|integral curve]] starting at $p$, with $\mathcal{D}^{(p)} \subseteq \mathbb{R}$ the maximal open interval through $0$ on which the integral curve exists. $\mathcal{D} = \{(t, p) : t \in \mathcal{D}^{(p)}\} \subseteq \mathbb{R} \times M$. For $t \in \mathbb{R}$, $M_t = \{p : (t, p) \in \mathcal{D}\}$ is the set of points whose maximal interval contains $t$. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]] for the full notation registry.

---

# Statement

> **Theorem (Fundamental Theorem on Flows; Lee Theorem 9.12).** Let $M$ be a smooth manifold and $X \in \mathfrak{X}(M)$ a smooth vector field. There exists a unique smooth maximal flow $\phi : \mathcal{D} \to M$ whose infinitesimal generator is $X$. This flow has the following properties:
>
> (a) For each $p \in M$, the curve $\phi^{(p)} : \mathcal{D}^{(p)} \to M$ defined by $\phi^{(p)}(t) = \phi(t, p)$ is the unique maximal integral curve of $X$ starting at $p$.
>
> (b) If $s \in \mathcal{D}^{(p)}$, then $\mathcal{D}^{(\phi_s(p))} = \mathcal{D}^{(p)} - s := \{t - s : t \in \mathcal{D}^{(p)}\}$.
>
> (c) For each $t \in \mathbb{R}$, the set $M_t = \{p : (t, p) \in \mathcal{D}\}$ is open in $M$, and $\phi_t : M_t \to M_{-t}$ is a diffeomorphism with inverse $\phi_{-t}$.

---

# Motivation

This is the heavyweight theorem of the chapter. It assembles the local existence-and-uniqueness of integral curves ([[Thm - Existence and Uniqueness of Integral Curves]]) into a single global object — the **maximal flow** — and packages all the geometric content of "infinitesimal direction field $\to$ one-parameter family of diffeomorphisms" into one clean statement. Every flow argument in the rest of differential geometry traces back to this theorem.

The role it plays is two-fold. First, it certifies that the natural map $X \mapsto \phi^X$ from smooth vector fields to flows is well-defined: the flow is *the* unique maximal smooth flow generating $X$, with no choices to make. Second, it provides the central tool for *constructing diffeomorphisms*: every smooth flow at every time gives a diffeomorphism between two open subsets of $M$, so any time you want to exhibit a diffeomorphism (between collars of submanifolds, between fibers, between perturbed and unperturbed copies of a manifold) you can try to find a vector field whose flow does the job.

The questions the theorem answers: *Does every smooth vector field generate a flow?* Yes, uniquely, maximally. *Is the flow smooth?* Yes, smoothly in $(t, p)$. *Is the flow domain open?* Yes — and this is exactly the geometric content of "ODE solutions exist for an open time interval", lifted to the manifold setting. *Is each $\phi_t$ a diffeomorphism?* Yes, with smooth inverse $\phi_{-t}$ — flowing forward by $t$ and back by $-t$ returns to start, by the group law.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is just "$X$ is a smooth vector field on a smooth manifold". The skill is recognizing when this hypothesis is in play in disguise.

The first disguised source is **a smooth first-order autonomous ODE in any open set of $\mathbb{R}^n$**. The bridge: the right-hand side $f^i(x)$ is the component field of a smooth vector field on $\mathbb{R}^n$. The amplification: the ODE has *unique smooth flow* on a maximal flow domain, and each time-$t$ map is a diffeomorphism. So whenever an autonomous ODE appears — in mechanics, in numerics, in population dynamics — this theorem gives the structural conclusion "the time-evolution forms a one-parameter family of diffeomorphisms". The non-obviousness: "evolution forms a group of diffeomorphisms" is a structural statement that pure ODE theory does not emphasize but is automatic from this theorem.

The second disguised source is **a smooth one-parameter family of diffeomorphisms with $\phi_0 = \mathrm{id}$, satisfying the group law and smooth in $(t, p)$.** The bridge: this is just a global flow, hence is the flow of its infinitesimal generator $X_p = \frac{d}{dt}|_{t=0} \phi_t(p)$, which is automatically smooth. The non-obviousness: the bijection between vector fields and maximal flows is rarely stated in this direction, but it is the same theorem read the other way.

The third disguised source is **a vector field defined locally and to be extended globally.** Given a smooth $X$ on an open subset $U \subseteq M$, this theorem applied to $U$ produces a flow on $U$, but one often wants a flow on $M$. The resolution: cut off $X$ to compact support inside $U$, then the flow extends globally (the field is now zero outside $\text{supp}$, hence integral curves there are constant). So the theorem, combined with compact support, lets you "globalize" a locally defined flow. See [[Ex - Compactly Supported Vector Fields are Complete]].

The fourth disguised source is **a smooth $\mathbb{R}$-action on $M$.** A smooth left $\mathbb{R}$-action is a smooth global flow, hence is the flow of a unique smooth vector field (its infinitesimal generator). So smooth $\mathbb{R}$-actions on smooth manifolds are *the same data* as complete smooth vector fields. The non-obviousness: this is the simplest case of Lie's correspondence between Lie group actions and Lie algebra actions.

**Targets (Output Amplification)**

The conclusion is "the maximal flow exists and has properties (a)–(c)". On its own this is a structural statement; combined with one further property, it amplifies into specific geometric constructions.

The first combination is **flow + compact support gives global one-parameter group of diffeomorphisms.** Property $D$: $X$ has compact support. Then $\mathcal{D} = \mathbb{R} \times M$, every $\phi_t$ is a diffeomorphism of *all* of $M$, and $t \mapsto \phi_t$ is a smooth group homomorphism $\mathbb{R} \to \mathrm{Diff}(M)$. The amplification produces an action of $\mathbb{R}$ on $M$, which is the standard tool for proving homotopy and isotopy results. See [[Ex - Compactly Supported Vector Fields are Complete]].

The second combination is **flow + transversal submanifold gives a tubular neighbourhood.** Property $D$: a codimension-1 embedded submanifold $S \subseteq M$ with $X$ nowhere tangent to $S$. The amplification (the Flowout Theorem, Lee 9.20): the map $(t, p) \mapsto \phi_t(p)$ is a diffeomorphism from a flow domain $O_\delta \subseteq \mathbb{R} \times S$ onto an open neighbourhood of $S$ in $M$. This is the geometric tool for constructing tubular neighbourhoods, collar neighbourhoods, and the canonical form near a regular point.

The third combination is **flow + invariance under a smooth map gives flow naturality.** Property $D$: $F : M \to N$ smooth with $X \sim_F X'$. Then $F$ takes the flow of $X$ to the flow of $X'$: $F \circ \phi^X_t = \phi^{X'}_t \circ F$ on the appropriate domain. This is Lee Proposition 9.13, which is "flow uniqueness" lifted to the level of pushing flows around between manifolds.

The fourth combination is **flow + a regular point gives the Straightening Theorem.** Property $D$: $X_p \neq 0$. Then there are coordinates $(s^1, \dots, s^n)$ near $p$ in which $X = \partial/\partial s^1$ — see [[Thm - Canonical Form for a Nonvanishing Vector Field]]. The amplification is that near regular points, every vector field looks the same up to diffeomorphism.

---

# Why Is It True

**The mechanism in one sentence: in any chart Picard–Lindelöf gives existence-uniqueness-smoothness of integral curves locally with smooth dependence on the starting point, and the group law of the flow plus the openness of flow domains assembles all the local pieces into one smooth maximal flow.**

Unpack this:

The *existence* of an integral curve through each $p$ is [[Thm - Existence and Uniqueness of Integral Curves]] — Picard–Lindelöf in a chart. The *uniqueness* on overlapping domains is also that theorem. So far we have, for each $p$, a unique maximal integral curve $\phi^{(p)} : \mathcal{D}^{(p)} \to M$. Assemble these into the candidate flow $\phi(t, p) := \phi^{(p)}(t)$.

The first non-trivial part is **the group law**: $\phi_t \circ \phi_s(p) = \phi_{t+s}(p)$ wherever defined. The proof is the **translation lemma** for integral curves: if $\gamma$ is an integral curve starting at $p$ and $q = \gamma(s)$, then $t \mapsto \gamma(t + s)$ is an integral curve starting at $q$. By uniqueness, this curve *is* $\phi^{(q)}$, so $\phi^{(q)}(t) = \phi^{(p)}(t + s)$. Rewritten: $\phi_t(\phi_s(p)) = \phi_{t+s}(p)$. The geometric content is "follow $X$ for time $s$, then for time $t$" $=$ "follow $X$ for time $t + s$" — which is exactly the autonomous nature of the ODE.

The group law also gives **part (b)**: $\mathcal{D}^{(\phi_s(p))} = \mathcal{D}^{(p)} - s$, because if you start at $q = \phi_s(p)$ then the integral curve from $q$ exists for exactly as long as the integral curve from $p$ exists, shifted by $s$.

The second non-trivial part is **the openness of $\mathcal{D}$**: $\{(t, p) \in \mathbb{R} \times M : t \in \mathcal{D}^{(p)}\}$ is an open subset. This is essentially Picard–Lindelöf's smooth dependence on the initial point: if the integral curve from $p$ exists on $[0, T]$, then the integral curve from a nearby $p'$ exists on a similar interval. The argument is to extend backwards from $T$: cover the trajectory $\phi^{(p)}([0, T])$ by finitely many product neighbourhoods of the form $J \times U \subseteq \mathcal{D}$ given by Picard–Lindelöf locally, then concatenate.

The third non-trivial part is **the smoothness of $\phi$ on $\mathcal{D}$**. The smooth dependence on initial conditions in Picard–Lindelöf is local; the global smoothness is obtained by piecing together local smoothness using the group law: $\phi_t = \phi_{t - t_0} \circ \phi_{t_0}$, and each factor is smooth on a neighbourhood by local Picard–Lindelöf.

Finally, **diffeomorphism property of $\phi_t$**: $\phi_{-t} \circ \phi_t = \phi_0 = \mathrm{id}$ on $M_t$ (by the group law), and similarly $\phi_t \circ \phi_{-t} = \mathrm{id}$ on $M_{-t}$. Both $\phi_t$ and $\phi_{-t}$ are smooth (by the smoothness of $\phi$), so each is a diffeomorphism with the other as inverse.

The whole proof is therefore the **gluing** of the local Picard–Lindelöf statements into a global one, using the group law as the gluing data. Picard–Lindelöf is doing all the analytical work; the manifold theory only contributes the chart-independence and the openness arguments.

---

# What Makes This Hard

Where most people get stuck is the **openness of the flow domain $\mathcal{D}$**, specifically the proof that if the integral curve through $p$ exists on $[0, T]$ then the integral curves through nearby points exist on a similar interval. The argument requires covering the trajectory by finitely many open sets in $\mathcal{D}$ — possible because the trajectory is compact and each point has a product-neighbourhood in $\mathcal{D}$ by local Picard–Lindelöf — and then concatenating; the concatenation step is the part that requires care. The most common error is to think the flow domain is automatically open from local existence, but local existence only gives openness in a *strip* $(-\varepsilon, \varepsilon) \times U$, not in arbitrarily large $t$. A second subtle point is the smoothness of $\phi$ in $(t, p)$ *jointly*, not just separately — but the joint smoothness follows from Picard–Lindelöf's smoothness in initial data plus the chain rule.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Get integral curves through every point from [[Thm - Existence and Uniqueness of Integral Curves]]. Assemble them into the flow $\phi(t, p) = \phi^{(p)}(t)$. Verify the group law using the translation lemma. Verify openness of the flow domain using a compactness argument: any compact subtrajectory is covered by finitely many product-neighbourhoods. Verify smoothness using the smooth-dependence conclusion of Picard–Lindelöf in each product neighbourhood, glued by the group law. Each $\phi_t$ is then a diffeomorphism by the group law.

**Subgoal decomposition:**

1. **Assemble integral curves into the flow.** For each $p$, let $\phi^{(p)}$ be the unique maximal integral curve from $p$, and define $\phi(t, p) = \phi^{(p)}(t)$ on the candidate domain $\mathcal{D} = \{(t, p) : t \in \mathcal{D}^{(p)}\}$.
   - *Hint:* This is just packaging.
   - *Why needed:* Defines the object whose properties we are about to verify.

2. **Group law.** Show $\phi_t(\phi_s(p)) = \phi_{t+s}(p)$ wherever defined.
   - *Hint:* Translation lemma — $t \mapsto \phi^{(p)}(t + s)$ is an integral curve starting at $\phi_s(p)$, so by uniqueness it equals $\phi^{(\phi_s(p))}$.
   - *Why needed:* Gives the structure of a partial $\mathbb{R}$-action and the relation $\mathcal{D}^{(\phi_s(p))} = \mathcal{D}^{(p)} - s$.

3. **Openness of $\mathcal{D}$.** Show that $\mathcal{D}$ is open in $\mathbb{R} \times M$.
   - *Hint:* Given $(t_0, p_0) \in \mathcal{D}$, the trajectory $\phi^{(p_0)}([0, t_0])$ is compact; cover by finitely many product-neighbourhoods from local Picard–Lindelöf; concatenate using the group law.
   - *Why needed:* Without openness, $\phi$ is not even a well-defined smooth map on its domain.

4. **Smoothness of $\phi$.** Show that $\phi : \mathcal{D} \to M$ is smooth.
   - *Hint:* On each product-neighbourhood from local Picard–Lindelöf, smoothness is direct; the global smoothness follows by gluing using the group law: $\phi_t = \phi_{t - t_0} \circ \phi_{t_0}$ at every point.
   - *Why needed:* This is the regularity statement (c).

5. **Diffeomorphism property.** Show that $\phi_t : M_t \to M_{-t}$ is a diffeomorphism with inverse $\phi_{-t}$.
   - *Hint:* Group law: $\phi_{-t} \circ \phi_t = \phi_0 = \mathrm{id}$ on $M_t$; similarly the other direction. Smoothness from step 4.
   - *Why needed:* This is the final form of (c).

6. **Maximality and uniqueness.** Show that this $\phi$ is *the* maximal flow.
   - *Hint:* Maximality is built into the construction. Uniqueness: any other smooth maximal flow generating $X$ has the same integral curves (by uniqueness in step 1) and so equals $\phi$.
   - *Why needed:* Completes the statement.

---

# Lemma Decomposition

> [!note]- Lemma 1: The translation lemma
> **Statement:** Let $X$ be a smooth vector field on $M$, $\gamma : J \to M$ an integral curve of $X$, and $b \in \mathbb{R}$. Then $\tilde\gamma(t) = \gamma(t + b)$ defined on $\tilde J = \{t : t + b \in J\}$ is also an integral curve of $X$.
>
> **Hint:** Differentiate $\tilde\gamma(t) = \gamma(t + b)$ using the chain rule: $\tilde\gamma'(t) = \gamma'(t + b) = X_{\gamma(t + b)} = X_{\tilde\gamma(t)}$.
>
> **Why needed:** This is the autonomous nature of the ODE. It gives the group law for the flow.
>
> > [!note]- Full proof
> > $\tilde\gamma'(t) := d\tilde\gamma_t(d/dt|_t)$. By the chain rule for smooth curves, $\tilde\gamma'(t) = \frac{d}{dt} \gamma(t + b) = \gamma'(t + b)$. Since $\gamma$ is an integral curve, $\gamma'(t + b) = X_{\gamma(t+b)} = X_{\tilde\gamma(t)}$. Hence $\tilde\gamma$ is an integral curve.

> [!note]- Lemma 2: The flow domain $\mathcal{D}$ is open
> **Statement:** Let $X$ be a smooth vector field on $M$ with maximal integral curves $\phi^{(p)}$, and define $\mathcal{D} = \{(t, p) : t \in \mathcal{D}^{(p)}\}$. Then $\mathcal{D}$ is open in $\mathbb{R} \times M$.
>
> **Hint:** Given $(t_0, p_0) \in \mathcal{D}$ with $t_0 > 0$, cover the trajectory $\phi^{(p_0)}([0, t_0])$ by finitely many open product-neighbourhoods $J_i \times U_i \subseteq \mathcal{D}$ from local Picard–Lindelöf; the group law then lets you "concatenate" to produce a product-neighbourhood of $(t_0, p_0)$.
>
> **Why needed:** Without openness of $\mathcal{D}$, the flow $\phi$ is not smooth on its domain (smoothness requires an open domain).
>
> > [!note]- Full proof
> > Let $(t_0, p_0) \in \mathcal{D}$ with $t_0 \geq 0$ (the case $t_0 < 0$ is symmetric). Consider the trajectory $K = \phi^{(p_0)}([0, t_0]) \subset M$, a compact connected curve.
> >
> > Define $W \subseteq \mathcal{D}$ as the set of $(t, p) \in \mathcal{D}$ such that $\phi$ is defined and smooth on a product neighbourhood $J \times U$ of $(t, p)$ with $J$ open interval containing $0$ and $t$, and $U$ an open neighbourhood of $p$. $W$ is open by definition. We show $(t_0, p_0) \in W$.
> >
> > Let $T = \sup \{t \in [0, t_0] : (t, p_0) \in W\}$. By local Picard–Lindelöf there is a product neighbourhood $(-\varepsilon, \varepsilon) \times U_0$ of $(0, p_0)$ in $\mathcal{D}$ with $\phi$ smooth, so $T \geq \varepsilon > 0$.
> >
> > Suppose $T \leq t_0$, aiming for contradiction. Let $q = \phi^{(p_0)}(T)$. By local Picard–Lindelöf at $q$, there is $\eta > 0$ and an open $V \ni q$ with $\phi$ defined and smooth on $(-\eta, \eta) \times V$. Pick $T - \eta/2 < t_1 < T$ with $(t_1, p_0) \in W$, so $\phi$ is smooth on a product neighbourhood $J_1 \times U_1$ of $(t_1, p_0)$ contained in $\mathcal{D}$. Shrink $U_1$ so $\phi(\{t_1\} \times U_1) \subseteq V$.
> >
> > Define $\tilde \phi$ on $(t_1 - \eta/2, t_1 + \eta) \times U_1$ by $\tilde\phi(t, p) = \phi(t - t_1, \phi(t_1, p))$, the composition of smooth maps, hence smooth. By the group law, $\tilde\phi = \phi$ where both are defined, so $\phi$ extends smoothly to $(t_1 - \eta/2, t_1 + \eta) \times U_1$. This contains a product neighbourhood of $(T, p_0)$, contradicting maximality of $T$.
> >
> > Hence $T > t_0$ and $(t_0, p_0) \in W$. So $\mathcal{D} \subseteq W$, hence $\mathcal{D} = W$ is open.

> [!note]- Lemma 3: The maximal flow is unique
> **Statement:** If $\phi, \tilde\phi : \mathcal{D}, \tilde{\mathcal D} \to M$ are two smooth maximal flows with infinitesimal generator $X$, then $\mathcal{D} = \tilde{\mathcal D}$ and $\phi = \tilde\phi$.
>
> **Hint:** For each $p$, both $t \mapsto \phi(t, p)$ and $t \mapsto \tilde\phi(t, p)$ are maximal integral curves starting at $p$; by uniqueness from [[Thm - Existence and Uniqueness of Integral Curves]] they agree on $\mathcal{D}^{(p)} \cap \tilde{\mathcal D}^{(p)}$. Maximality of both forces $\mathcal{D}^{(p)} = \tilde{\mathcal D}^{(p)}$.
>
> **Why needed:** Without uniqueness, there could be inequivalent flows generating $X$, and the theorem's statement would be ill-posed.
>
> > [!note]- Full proof
> > Fix $p \in M$. Both $\phi^{(p)} := \phi(\cdot, p)$ and $\tilde\phi^{(p)} := \tilde\phi(\cdot, p)$ are integral curves of $X$ starting at $p$, defined on $\mathcal{D}^{(p)}$ and $\tilde{\mathcal D}^{(p)}$ respectively. By [[Thm - Existence and Uniqueness of Integral Curves]] uniqueness, $\phi^{(p)} = \tilde\phi^{(p)}$ on $\mathcal{D}^{(p)} \cap \tilde{\mathcal D}^{(p)}$.
> >
> > If $\mathcal{D}^{(p)} \neq \tilde{\mathcal D}^{(p)}$ — say $\mathcal{D}^{(p)} \subsetneq \tilde{\mathcal D}^{(p)}$ — then $\tilde\phi^{(p)}$ is an integral curve through $p$ on a strictly larger interval, contradicting maximality of $\phi^{(p)}$. So $\mathcal{D}^{(p)} = \tilde{\mathcal D}^{(p)}$ and $\phi^{(p)} = \tilde\phi^{(p)}$ on the common domain. Varying $p$, $\mathcal{D} = \tilde{\mathcal D}$ and $\phi = \tilde\phi$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — Maximal integral curves exist.** By [[Thm - Existence and Uniqueness of Integral Curves]], for each $p \in M$ there is a unique maximal integral curve $\phi^{(p)} : \mathcal{D}^{(p)} \to M$ of $X$ with $\phi^{(p)}(0) = p$, with $\mathcal{D}^{(p)} \subseteq \mathbb{R}$ an open interval containing $0$.
>
> **Step 1 — Definition of the flow.** Let $\mathcal{D} = \{(t, p) \in \mathbb{R} \times M : t \in \mathcal{D}^{(p)}\}$ and define $\phi : \mathcal{D} \to M$ by $\phi(t, p) := \phi^{(p)}(t)$. We write $\phi_t(p) := \phi(t, p)$. The claim is that $\phi$ is a smooth maximal flow on $M$ generating $X$.
>
> **Step 2 — Identity at zero.** $\phi(0, p) = \phi^{(p)}(0) = p$, by the starting condition of $\phi^{(p)}$.
>
> **Step 3 — Group law (proves (b)).** Suppose $s \in \mathcal{D}^{(p)}$ and let $q = \phi_s(p) = \phi^{(p)}(s)$. By Lemma 1 (translation lemma), $t \mapsto \phi^{(p)}(t + s)$ is an integral curve starting at $q$, defined for $t$ in the shifted interval $\mathcal{D}^{(p)} - s$. By uniqueness of maximal integral curves ([[Thm - Existence and Uniqueness of Integral Curves]]), this curve agrees with $\phi^{(q)}$ on $\mathcal{D}^{(p)} - s \cap \mathcal{D}^{(q)}$, and maximality of $\phi^{(q)}$ forces $\mathcal{D}^{(p)} - s \subseteq \mathcal{D}^{(q)}$. Applying the same argument with $q$ and $-s$ gives $\mathcal{D}^{(q)} + s \subseteq \mathcal{D}^{(p)}$, i.e. $\mathcal{D}^{(q)} \subseteq \mathcal{D}^{(p)} - s$. Hence $\mathcal{D}^{(q)} = \mathcal{D}^{(p)} - s$, and $\phi^{(q)}(t) = \phi^{(p)}(t + s)$, i.e. $\phi_t(\phi_s(p)) = \phi_{t+s}(p)$.
>
> **Step 4 — Openness of $\mathcal{D}$ (proves (c) part 1).** By Lemma 2, $\mathcal{D}$ is open in $\mathbb{R} \times M$.
>
> **Step 5 — Smoothness of $\phi$.** Local Picard–Lindelöf gives, around each $(t_0, p_0) \in \mathcal{D}$, a product neighbourhood $J \times U \subseteq \mathcal{D}$ on which $\phi$ is smooth (the smooth-dependence statement of [[Thm - The Contraction Mapping Principle|Picard–Lindelöf]] in $\mathbb{R}^n$, applied in a chart). The proof of openness in Lemma 2 also shows that smoothness extends globally on $\mathcal{D}$ using the group law $\phi_t = \phi_{t - t_0} \circ \phi_{t_0}$, since each factor is smooth on a small set.
>
> **Step 6 — Each $\phi_t$ is a diffeomorphism (proves (c) part 2).** For each $t \in \mathbb{R}$, $M_t = \{p : (t, p) \in \mathcal{D}\}$ is the projection of the open set $\{t\} \times M \cap \mathcal{D}$ in $\mathcal{D}$ onto $M$, hence open in $M$. From the group law, for $p \in M_t$, $\phi_{-t}(\phi_t(p)) = \phi_0(p) = p$, so $\phi_t : M_t \to M_{-t}$ has the smooth left inverse $\phi_{-t}$ on $M_{-t}$ (and the analogous right inverse). Hence $\phi_t$ is a diffeomorphism.
>
> **Step 7 — Maximality and uniqueness.** By construction, each $\phi^{(p)}$ is maximal as an integral curve, so $\phi$ is maximal as a flow. By Lemma 3, $\phi$ is the unique smooth maximal flow with infinitesimal generator $X$.
>
> **Step 8 — Infinitesimal generator is $X$.** By definition, $\frac{d}{dt}\big|_{t=0} \phi(t, p) = \phi^{(p)\prime}(0) = X_{\phi^{(p)}(0)} = X_p$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Hamiltonian dynamics on phase space.** In Hamiltonian mechanics, the Hamiltonian function $H : T^*M \to \mathbb{R}$ determines a Hamiltonian vector field $X_H$ on phase space $T^*M$, and the time-evolution is the flow of $X_H$. The Fundamental Theorem on Flows applied to $X_H$ certifies that Hamiltonian trajectories exist, are unique, and depend smoothly on initial conditions — and that the time-$t$ map is a diffeomorphism of phase space (the symplectomorphism property). Recognizing the role of this theorem in Hamiltonian mechanics is recognising that the smooth structure of phase-space dynamics is built into the geometric setup.

**Construction of tubular neighbourhoods.** For an embedded submanifold $S \subseteq M$, the **tubular neighbourhood theorem** (a standard result of differential topology) constructs an open neighbourhood of $S$ in $M$ diffeomorphic to the normal bundle $NS$. The proof exhibits a vector field transverse to $S$ and applies the Flowout Theorem — which is the Fundamental Theorem on Flows plus the transverse-submanifold hypothesis. Recognising this as a flow construction is part of the standard toolkit of differential topology.

**Heat-flow methods in geometric analysis.** Curve shortening, mean curvature flow, Ricci flow — all are flows of vector fields on infinite-dimensional spaces (spaces of curves, spaces of metrics), and the existence and short-time uniqueness of solutions is an infinite-dimensional version of the Fundamental Theorem on Flows. In the finite-dimensional version this theorem is the prototype.

**Differentiable conjugacy in dynamical systems.** Two vector fields $X, X'$ on manifolds $M, M'$ are **differentiably conjugate** if there is a diffeomorphism $F : M \to M'$ with $F_* X = X'$. Conjugate vector fields have the same flow structure: $F \circ \phi^X_t = \phi^{X'}_t \circ F$ — the Naturality of Flows (Lee 9.13), corollary of the Fundamental Theorem. So classifying vector fields up to conjugacy is classifying flows up to diffeomorphism, and the local classification (the Straightening Theorem) is the simplest non-trivial case.

---

# Bridges

- **[[Thm - Existence and Uniqueness of Integral Curves]]** — the pointwise version. The Fundamental Theorem on Flows is the global packaging of the pointwise local existence-and-uniqueness theorem: it takes the per-point integral curves and shows they assemble into a single smooth flow on an open flow domain. The uniqueness statement of the integral curve theorem is what licences the group law of the flow.

- **[[Thm - The Contraction Mapping Principle]]** — the analytical engine, two levels deeper. The integral-curve theorem is Picard–Lindelöf in a chart; the Fundamental Theorem is the global packaging of Picard–Lindelöf via the group law. The smooth dependence on the initial point — used here to prove smoothness of $\phi$ and openness of $\mathcal{D}$ — is the standard "smooth dependence on parameters" conclusion of Picard–Lindelöf, a refinement of the basic existence-uniqueness statement.

- **[[Thm - Commuting Flows Theorem]]** — uses this theorem twice. The Commuting Flows Theorem says the flows of two vector fields commute iff their Lie bracket vanishes; the "flows" in question are the maximal flows produced by the Fundamental Theorem. Without this theorem, the Commuting Flows Theorem would have no flows to compare.

- **[[Thm - Canonical Form for a Nonvanishing Vector Field]]** — direct consequence + a transverse submanifold. The Straightening Theorem says a nonvanishing vector field looks like $\partial/\partial s^1$ in suitable coordinates; the proof is the Flowout Theorem, which is the Fundamental Theorem on Flows combined with a transverse submanifold.

- **Lie group exponential map** — for left-invariant vector fields on a Lie group, the maximal flow is global by translation-equivariance, and the assignment $v \mapsto \phi^{v^L}_1(e)$ is the exponential map $\mathfrak{g} \to G$ — see [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]]. The Fundamental Theorem is what certifies the flow exists; the special features of left-invariant fields make it global.

---

# Unlocked by This

> [!tip] Exponential Map of a Lie Group *(from Lie Theory)*
> For a [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|Lie group]] $G$ with Lie algebra $\mathfrak{g} = T_e G$, every $v \in \mathfrak{g}$ extends to a *left-invariant* vector field $v^L$ on $G$, which is complete (by the homogeneity argument). The exponential map $\exp : \mathfrak{g} \to G$ is then $\exp(v) := \phi^{v^L}_1(e)$. The Fundamental Theorem on Flows is what certifies the flow exists; left-invariance makes it global; the exponential is the time-$1$ map of the flow.

> [!tip] Smooth $\mathbb{R}$-Actions ↔ Complete Vector Fields *(from Lie Theory and Dynamical Systems)*
> Complete smooth vector fields on $M$ are exactly the same data as smooth $\mathbb{R}$-actions on $M$. The bijection is: action $\mapsto$ infinitesimal generator at the identity; vector field $\mapsto$ flow. This is the simplest case of Lie's correspondence between Lie groups (here $\mathbb{R}$) and their actions, and it is the foundation of dynamical-systems theory on manifolds.

> [!tip] Tubular Neighbourhood Theorem *(from Differential Topology)*
> Combining the Fundamental Theorem on Flows with a transverse vector field along a submanifold $S \subseteq M$, the **Flowout Theorem** (Lee 9.20) produces an open neighbourhood of $S$ diffeomorphic to a flow domain in $\mathbb{R} \times S$. This is the differential-geometric way to construct **tubular neighbourhoods**, **collar neighbourhoods of boundary**, and **normal-bundle parametrizations**, which are the basic tools of differential topology and Morse theory.
