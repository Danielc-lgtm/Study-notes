---
type: theorem
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Continuous Map"
  - "Def - Basis and Subbasis for a Topology"
  - "Def - Neighbourhood and Neighbourhood Basis"
tags: [analysis, topology]
---

# Notation

$X, Y$ are topological spaces, $f : X \to Y$ a function. A **basis** $\mathcal{B}$ for the topology of $Y$ is a family of open sets whose unions are exactly the open sets; a **subbasis** $\mathcal{S}$ is a family whose finite intersections form a basis. A **neighbourhood basis** $\mathcal{B}_y$ at $y \in Y$ is a family of neighbourhoods of $y$ such that every neighbourhood contains some element of $\mathcal{B}_y$. The full notation registry is on [[Topology I — §1–3 Metric and Topological Spaces]].

---

# Motivation

The definition of continuity demands "$f^{-1}(U)$ open for every open $U$" — a quantification over potentially uncountably many open sets, most of which are complicated unions of basis elements. Checking this directly is rarely tractable. This theorem says we do not have to: a *much* smaller verification suffices. It is enough to check $f^{-1}(B)$ is open for $B$ in any basis (or even any subbasis) of the target topology, and the rest follows by abstract nonsense from how $f^{-1}$ interacts with unions and intersections.

The reduction is what makes practical continuity proofs short. For a map into $\mathbb{R}^n$, checking the preimage of every open set would be hopeless; checking the preimage of every open ball (the basis) is a finite-dimensional $\varepsilon$–$\delta$ exercise. For a map into a product space $\prod Y_\alpha$, checking the preimage of every open set in the product topology is impossible to even *enumerate*; checking the preimage of every set of the form $\pi_\alpha^{-1}(V)$ for $V \subseteq Y_\alpha$ open (the standard subbasis) reduces continuity to checking that every component map $f_\alpha = \pi_\alpha \circ f$ is continuous — which is the most-used corollary of the basis criterion.

The neighbourhood version is the *local* version. Where the basis version reduces continuity globally to a generating family of open sets in $Y$, the neighbourhood version reduces continuity at a single point $x$ to a generating family of neighbourhoods of $f(x)$. This is the right tool when one wants to verify continuity at one point — for example, at the "interesting" point of a piecewise definition.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition can be invoked in two forms — basis or subbasis on the target side — and the skill is recognizing which is appropriate.

The first natural source is **a metric ball basis on $Y$.** Property $B$: $Y$ is a metric space with metric $\rho$, and we have the open ball basis $\{B_\varepsilon(y) : y \in Y, \varepsilon > 0\}$. The bridge: checking $f^{-1}(B_\varepsilon(y))$ open is exactly the $\varepsilon$–$\delta$ condition translated to open-set language, so the basis criterion specializes to [[Thm - Continuity via Open Sets (Metric Spaces)]]. *Example:* showing that a function defined by a formula like $f(x) = (x, \sin x) \in \mathbb{R}^2$ is continuous by checking the preimage of each open rectangle, then of each open ball.

The second source is **a defining subbasis from a weak topology.** Property $B$: $Y$ is given the coarsest topology making a family of functions $\varphi_\alpha : Y \to Z_\alpha$ continuous (the **weak topology** induced by this family). Then $\{\varphi_\alpha^{-1}(V) : V \subseteq Z_\alpha\ \text{open}\}$ is a subbasis. The bridge: $f^{-1}(\varphi_\alpha^{-1}(V)) = (\varphi_\alpha \circ f)^{-1}(V)$, so checking $f^{-1}$ of the subbasis is equivalent to checking that each composition $\varphi_\alpha \circ f$ is continuous. *Example:* a map into a product $\prod Y_\alpha$ is continuous if and only if each component $\pi_\alpha \circ f$ is — the universal property of the product topology.

The third source is **a finite open cover with continuity on each piece.** Property $B$: $X$ is the union of finitely many closed (or open) sets, on each of which $f$ is given continuous. The bridge to a "basis-level" verification is indirect — the conclusion is continuity, but the verification path goes through the [[Thm - The Pasting Lemma|pasting lemma]] rather than directly through the basis criterion. The basis criterion remains the workhorse for the *individual pieces*.

**Targets (Output Amplification)**

The conclusion is "$f$ is continuous". The amplification game is to combine this with structural conditions on $X$ or $Y$ to obtain stronger conclusions.

Combine with **continuity into a product.** Property $D$: $Y = \prod_\alpha Y_\alpha$ has the product topology, and $f : X \to Y$ has components $f_\alpha = \pi_\alpha \circ f$. The amplified result $E$: $f$ is continuous if and only if every $f_\alpha$ is continuous (by the basis criterion applied to the standard subbasis of the product). This *decomposes* continuity verification into independent component-wise verifications, a single algebraic move.

Combine with **continuity into a quotient.** Property $D$: $Y = Z/{\sim}$ is a quotient of some space $Z$ by an equivalence relation, with the quotient topology $\tau_Y$ — the *finest* topology making the projection $q : Z \to Y$ continuous. Then for $g : Y \to W$ to be continuous, the composition $g \circ q : Z \to W$ must be continuous. The amplified result: continuity *out of* a quotient is the same as continuity of the lift, by the universal property of the quotient (dual to the present theorem).

Combine with **first countability and sequential continuity.** Property $D$: $X$ is first countable at $x$. The amplified result $E$: continuity of $f$ at $x$ is equivalent to "$x_n \to x$ implies $f(x_n) \to f(x)$" — sequential continuity. The bridge uses the countable neighbourhood basis: $f$ continuous at $x$ iff $f^{-1}(B)$ neighbourhood of $x$ for every $B$ in a basis at $f(x)$ iff (in a first-countable space, by a diagonalization) preserves sequences.

---

# Why Is It True

The basis criterion is at heart an algebraic property of $f^{-1}$: it commutes with unions and intersections. If you know the preimage of every basis element is open, then the preimage of any union of basis elements is a union of opens, hence open. Since every open in $Y$ is a union of basis elements, the conclusion follows for every open. The whole proof is *one* line: $f^{-1}(\bigcup_\alpha B_\alpha) = \bigcup_\alpha f^{-1}(B_\alpha)$, and a union of opens is open.

The subbasis version takes one more step. A subbasis $\mathcal{S}$ generates a basis by *finite intersections*: every basis element is a finite intersection $S_1 \cap \dots \cap S_n$ of subbasis elements. The preimage of a finite intersection is a finite intersection of preimages, and a finite intersection of open sets is open. So preimages of subbasis elements being open $\implies$ preimages of basis elements being open $\implies$ preimages of opens being open. Two algebraic propagation steps, both forced by the topology axioms.

The neighbourhood-basis version is the same idea localized to one point. The neighbourhood filter at $f(x)$ is generated, in the same union/intersection sense, by the neighbourhood basis at $f(x)$. So if every basis-neighbourhood pulls back to a neighbourhood of $x$ (containing some open set around $x$), every neighbourhood does too — and continuity at $x$ is by definition "preimage of every neighbourhood of $f(x)$ is a neighbourhood of $x$".

The deeper reason all of this works is that continuity, openness, and neighbourhood-membership are all *closed under unions* (and openness is closed under finite intersections). This closure structure is what lets us check a property on a *generating family* and have it propagate to the closure. The same algebraic mechanism powers the closure-of-image inclusion ($f(\overline{A}) \subseteq \overline{f(A)}$), the closure-in-subspace formula, and many other tropes in topology.

---

# What Makes This Hard

The subbasis version trips people up: it is easy to remember "checking a basis suffices" but easy to forget that *any* collection generates a topology — by taking finite intersections then arbitrary unions — and the verification on the *original* collection automatically promotes through both stages. The non-obvious move is recognizing that $f^{-1}$ commutes with both operations (commutativity with unions is automatic, commutativity with *finite* intersections requires no hypothesis), so the verification "lifts" through the basis-from-subbasis construction. A common error is to verify the condition for the subbasis but then panic about the finite-intersection step, when in fact that step is given to you for free.

---

# Rederivation Scaffold

**High-level strategy:**
Use the algebraic identities that $f^{-1}$ commutes with arbitrary unions and finite intersections. Verify the open-set condition on a generating family — basis or subbasis — and propagate to all opens. The neighbourhood version is the same argument localized to one point and one filter.

**Subgoal decomposition:**

1. **Basis version, forward:** If $f$ continuous, then $f^{-1}(B)$ open for every $B$ in any basis $\mathcal{B}$ of $Y$.
   - *Hint:* Trivial, since basis elements are open.
   - *Why needed:* Establishes one direction.

2. **Basis version, reverse:** If $f^{-1}(B)$ open for every $B \in \mathcal{B}$, then $f^{-1}(U)$ open for every open $U$.
   - *Hint:* $U = \bigcup_\alpha B_\alpha$ for some family in $\mathcal{B}$; $f^{-1}(U) = \bigcup f^{-1}(B_\alpha)$, a union of opens, hence open.
   - *Why needed:* The reverse direction is the practical content.

3. **Subbasis version:** Reduce the subbasis hypothesis to the basis hypothesis.
   - *Hint:* Finite intersections of subbasis elements have open preimage (preimage commutes with finite intersection, intersection of opens is open). So the family of basis elements (finite intersections of subbasis elements) all have open preimages, and step 2 applies.
   - *Why needed:* Extends to subbasis, the case relevant to product and weak topologies.

4. **Neighbourhood-basis version, continuity at $x$:** $f$ continuous at $x$ iff for every $B$ in a neighbourhood basis at $f(x)$, $f^{-1}(B)$ is a neighbourhood of $x$.
   - *Hint:* Every neighbourhood of $f(x)$ contains some $B$ in the basis; $f^{-1}$ preserves $\supseteq$.
   - *Why needed:* Local version, used for pointwise continuity checks.

---

# Lemma Decomposition

> [!note]- Lemma 1: Preimages commute with arbitrary unions and arbitrary intersections
> **Statement:** For $f : X \to Y$ and any family $\{V_\alpha\}$ of subsets of $Y$:
> $$f^{-1}\Big(\bigcup_\alpha V_\alpha\Big) = \bigcup_\alpha f^{-1}(V_\alpha), \qquad f^{-1}\Big(\bigcap_\alpha V_\alpha\Big) = \bigcap_\alpha f^{-1}(V_\alpha).$$
>
> **Hint:** Element-chase using "$x \in f^{-1}(V) \iff f(x) \in V$".
>
> **Why needed:** It is the algebraic backbone of every basis-criterion argument.
>
> > [!note]- Full proof
> > $x \in f^{-1}(\bigcup V_\alpha) \iff f(x) \in \bigcup V_\alpha \iff \exists \alpha,\ f(x) \in V_\alpha \iff \exists \alpha,\ x \in f^{-1}(V_\alpha) \iff x \in \bigcup f^{-1}(V_\alpha)$. Same chain for intersections with $\forall$ in place of $\exists$.

> [!note]- Lemma 2: Topology generated by a subbasis equals finite intersections then arbitrary unions
> **Statement:** Given any collection $\mathcal{S} \subseteq \mathcal{P}(Y)$, the topology $\tau$ generated by $\mathcal{S}$ consists exactly of the arbitrary unions of finite intersections of elements of $\mathcal{S}$ (including $\emptyset$ as the empty intersection and $Y$ as the intersection over the empty family).
>
> **Hint:** Show the collection described is closed under arbitrary unions and finite intersections, contains $\mathcal{S}$, and is contained in any topology containing $\mathcal{S}$.
>
> **Why needed:** It is the formal content of "subbasis generates topology" and the reason the basis criterion lifts from subbasis to all opens.
>
> > [!note]- Full proof
> > Let $\mathcal{B}$ be the family of finite intersections of elements of $\mathcal{S}$. Let $\tau$ be the family of arbitrary unions of elements of $\mathcal{B}$. We show $\tau$ is a topology.
> >
> > $\emptyset \in \tau$ (empty union); $Y \in \tau$ (Y is the empty intersection, in $\mathcal{B}$, and a union of one element). Arbitrary unions of elements of $\tau$ are unions of unions of basis elements, hence unions of basis elements, hence in $\tau$. Finite intersections: $(\bigcup_i B_i^{(1)}) \cap (\bigcup_j B_j^{(2)}) = \bigcup_{i,j}(B_i^{(1)} \cap B_j^{(2)})$, and $B_i^{(1)} \cap B_j^{(2)}$ is a finite intersection of finite intersections of $\mathcal{S}$-elements, hence in $\mathcal{B}$.
> >
> > So $\tau$ is a topology. It contains $\mathcal{S}$ (each $S \in \mathcal{S}$ is the union of the basis element $\{S\}$). Any topology $\tau'$ containing $\mathcal{S}$ must contain $\mathcal{B}$ (closed under finite intersections) and $\tau$ (closed under arbitrary unions). So $\tau$ is the smallest topology containing $\mathcal{S}$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f : X \to Y$ be a function between topological spaces.
>
> **Basis criterion ($\Rightarrow$).** Suppose $f$ is continuous. Every basis element $B \in \mathcal{B}$ is open in $Y$, so $f^{-1}(B)$ is open in $X$ by the definition of continuity.
>
> **Basis criterion ($\Leftarrow$).** Suppose $f^{-1}(B)$ is open for every $B \in \mathcal{B}$. Let $U \subseteq Y$ be open. Then $U = \bigcup_{\alpha \in I} B_\alpha$ for some family $\{B_\alpha\} \subseteq \mathcal{B}$ (definition of basis). By Lemma 1, $f^{-1}(U) = \bigcup_\alpha f^{-1}(B_\alpha)$, a union of open sets, hence open. So $f$ is continuous.
>
> **Subbasis criterion.** Suppose $f^{-1}(S)$ is open for every $S \in \mathcal{S}$, where $\mathcal{S}$ is a subbasis. Every basis element (in the basis generated by $\mathcal{S}$) is a finite intersection $S_1 \cap \dots \cap S_n$; by Lemma 1, $f^{-1}(S_1 \cap \dots \cap S_n) = f^{-1}(S_1) \cap \dots \cap f^{-1}(S_n)$, a finite intersection of opens, hence open. So the basis criterion's hypothesis is satisfied, and $f$ is continuous.
>
> **Neighbourhood-basis criterion (continuity at $x$).** Recall $f$ is continuous at $x$ if for every neighbourhood $N$ of $f(x)$ in $Y$, $f^{-1}(N)$ is a neighbourhood of $x$. ($\Rightarrow$) is trivial. ($\Leftarrow$): suppose $f^{-1}(B)$ is a neighbourhood of $x$ for every $B$ in a neighbourhood basis $\mathcal{B}_{f(x)}$. Let $N$ be any neighbourhood of $f(x)$. By the definition of neighbourhood basis, $B \subseteq N$ for some $B \in \mathcal{B}_{f(x)}$. Then $f^{-1}(B) \subseteq f^{-1}(N)$, and $f^{-1}(B)$ is a neighbourhood of $x$, so $f^{-1}(N)$ contains a neighbourhood of $x$, hence is itself a neighbourhood of $x$ (the neighbourhood filter is closed under supersets). So $f$ is continuous at $x$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Continuity of a map into a product.** A map $f : X \to \prod_{\alpha \in I} Y_\alpha$ is continuous if and only if every component $\pi_\alpha \circ f : X \to Y_\alpha$ is continuous. *Proof:* the product topology has the subbasis $\{\pi_\alpha^{-1}(V) : \alpha \in I, V \subseteq Y_\alpha\ \text{open}\}$. By the subbasis criterion, $f$ continuous iff $f^{-1}(\pi_\alpha^{-1}(V))$ open for every $\alpha, V$, iff $(\pi_\alpha \circ f)^{-1}(V)$ open for every $\alpha, V$, iff every $\pi_\alpha \circ f$ continuous. This is the **universal property of the product topology** as deduced from the subbasis criterion.

**Continuity in the weak topology on a Banach space.** A linear functional $\varphi : V \to \mathbb{R}$ on a Banach space $V$ is *automatically* continuous with respect to the weak topology on $V$ (since the weak topology is defined to be the coarsest making every continuous functional continuous). Conversely, a sequence $x_n \to x$ weakly means $\varphi(x_n) \to \varphi(x)$ for every $\varphi \in V^*$ — and the subbasis criterion is the structural reason this characterization works.

**Continuity in product measure spaces.** In probability theory, the projection maps $\pi_n : \mathbb{R}^\mathbb{N} \to \mathbb{R}$ from the product space onto the $n$-th coordinate are continuous in the product topology (by definition of the topology), and this is what makes finite-dimensional distributions well-defined. The basis criterion underlies the construction of stochastic processes via their finite-dimensional marginals — the topology on the path space is precisely the one in which the projection maps are continuous.

**Application to homotopy.** A homotopy $H : X \times I \to Y$ is continuous if and only if for every open $U \subseteq Y$, $H^{-1}(U)$ is open in $X \times I$. The basis criterion lets one verify this on the rectangle basis of $X \times I$ — a major saving in any homotopy construction (path concatenation, reparametrization).

---

# Bridges

- **[[Thm - Continuity via Open Sets (Metric Spaces)]]** — the metric special case, with $\mathcal{B}$ = open balls. The basis criterion with the metric ball basis gives the $\varepsilon$–$\delta$ formulation.

- **[[Def - Basis and Subbasis for a Topology]]** — the formal definition of the objects this theorem leverages. The theorem is what makes those definitions useful.

- **[[Def - Subspace Topology]]** — the basis for the subspace topology consists of intersections of a basis of $X$ with $Y$; the basis criterion then says continuity of a map *into* a subspace is continuity into the ambient with image in the subspace, which is the [[Def - Subspace Topology|universal property]] of the subspace topology.

- **[[Topology I — §1–3 Metric and Topological Spaces|Product topology]]** — the standard basis on a product is rectangles, the standard subbasis is the family of $\pi_\alpha^{-1}(V)$. The basis criterion applied here gives the universal property of the product.

- **[[Topology I — §1–3 Metric and Topological Spaces|Quotient topology]]** — dual to the present situation: continuity out of a quotient is verified on the source side via the projection. The same algebraic argument with the directions reversed.

---

# Unlocked by This

> [!tip] The Universal Property of the Product Topology *(in this topic)*
> A map into a product is continuous if and only if each component is. This is the most-used corollary of the basis criterion, and it is what makes the product topology workable. See the product topology construction discussed in the parent topic page.

> [!tip] The Weak Topology on a Banach Space *(from Functional Analysis)*
> The **weak topology** on a normed space $V$ is defined to be the coarsest topology making every $\varphi \in V^*$ continuous — generated by the subbasis $\{\varphi^{-1}(U) : \varphi \in V^*, U \subseteq \mathbb{R}\ \text{open}\}$. The basis criterion is what makes this construction yield a well-defined and usable topology; the **Banach–Alaoglu theorem** (compactness of the unit ball of $V^*$ in the weak-$*$ topology) depends on this setup.

> [!tip] Topology of Pointwise Convergence *(from Real Analysis)*
> On the space of functions $X \to Y$, the **topology of pointwise convergence** is the product topology under the identification "function = tuple of values at every point". Continuity of evaluation maps is built in by the subbasis. Pointwise convergence of functions is *exactly* convergence in this topology, and the basis criterion is what justifies this.
