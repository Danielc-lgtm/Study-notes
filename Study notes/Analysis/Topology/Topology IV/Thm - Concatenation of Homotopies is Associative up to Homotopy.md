---
type: theorem
subject: topology
prereqs:
  - "Def - Homotopy"
  - "Thm - Reparametrization Lemma"
tags: [analysis, topology, homotopy, fundamental-group]
---

# Notation

$X, Y$ topological spaces. $F, G, H : X \times I \to Y$ homotopies with compatible endpoints: $F(x, 1) = G(x, 0)$ and $G(x, 1) = H(x, 0)$. Concatenation $F * G$ defined by running $F$ at double speed on $[0, 1/2]$ then $G$ at double speed on $[1/2, 1]$. The constant homotopy $C(x, t) = $ some constant value. Inversion $F^{-1}(x, t) = F(x, 1-t)$. The full registry is on the topic page.

---

# Motivation

To make a *group* out of the loops in a space, we need three things: associativity ($(\alpha\beta)\gamma = \alpha(\beta\gamma)$), identity ($\alpha c = c\alpha = \alpha$ for $c$ a constant loop), and inverses ($\alpha \alpha^{-1} = c$). Each of these would be true on the nose if loops formed a group in the strict sense — but they don't: the loop $(\alpha \beta) \gamma$ traverses $\alpha$ on $[0, 1/4]$, $\beta$ on $[1/4, 1/2]$, $\gamma$ on $[1/2, 1]$, while $\alpha (\beta \gamma)$ traverses $\alpha$ on $[0, 1/2]$, $\beta$ on $[1/2, 3/4]$, $\gamma$ on $[3/4, 1]$. These are different parametrizations of the same point-set path — different functions $I \to Y$. To get a group, we need to declare them equal *up to homotopy*.

This theorem establishes that. Concatenation is associative *up to homotopy rel endpoints*: there is a continuous deformation from $(F * G) * H$ to $F * (G * H)$ that fixes the start and end points. Combined with the analogous results for identity (Bredon 14.13: $F * C \simeq F$, $C * F \simeq F$) and inverses (Bredon 14.15: $F * F^{-1} \simeq C$), this turns the homotopy classes of loops into a group — the fundamental group $\pi_1$.

The proof is a direct application of the [[Thm - Reparametrization Lemma|reparametrization lemma]]: both $(F * G) * H$ and $F * (G * H)$ are reparametrizations of the same "concatenated path with three pieces", just with different splittings of the interval. The reparametrization lemma absorbs the difference.

---

# Statement

Let $F, G, H : X \times I \to Y$ be homotopies (or paths, in the case $X = *$) with compatible endpoints: $F(x, 1) = G(x, 0)$ and $G(x, 1) = H(x, 0)$ for all $x$. Then
$$(F * G) * H \simeq F * (G * H) \quad \text{rel } X \times \partial I.$$

**Companion identities** (Bredon Propositions 14.13 and 14.15):

- **Identity:** $F * C \simeq F$ and $C * F \simeq F$ rel $X \times \partial I$, where $C$ is the appropriate constant homotopy.
- **Inverse:** $F * F^{-1} \simeq C$ rel $X \times \partial I$, where $C$ is the constant homotopy at $F(\cdot, 0)$.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "three homotopies with chained endpoints". Common sources:

**Three paths in a row.** Property $B$: paths $\alpha, \beta, \gamma : I \to Y$ with $\alpha(1) = \beta(0)$, $\beta(1) = \gamma(0)$. The bridge: take $X = *$ and $F = \alpha, G = \beta, H = \gamma$. *Example:* proving associativity of the fundamental group operation; proving the fundamental groupoid is a category.

**Higher-dimensional homotopies.** Property $B$: homotopies between maps of pairs $(X, A) \to (Y, B)$, with compatible boundary behavior. The bridge: the same theorem holds in any category where reparametrization works, including the categories of based spaces, pointed pairs, etc. *Example:* associativity of concatenation for homotopy groups $\pi_n$ with $n \geq 1$ (where the concatenation is along one of the $n$ axes).

**Targets (Output Amplification)**

The conclusion "(triple concatenation is associative up to homotopy)" combines with the identity and inverse laws to produce:

Combine with **identity laws ($F * C \simeq F$).** Property $D$: $C$ acts as a two-sided identity for concatenation. The amplified result $E$: homotopy classes of loops form a *monoid* under concatenation.

Combine with **inverse laws ($F * F^{-1} \simeq C$).** Property $D$: every homotopy has a two-sided inverse up to homotopy. The amplified result $E$: the monoid is a *group* — this is the fundamental group $\pi_1(X, x_0)$.

Combine with **higher-dimensional analogues.** Property $D$: similar reparametrization arguments hold in higher dimensions. The amplified result $E$: higher homotopy groups $\pi_n(X, x_0)$ are abelian groups for $n \geq 2$ (the higher-dimensional version of the Eckmann-Hilton argument).

---

# Why Is It True

Both $(F * G) * H$ and $F * (G * H)$ are explicit piecewise-defined homotopies, each splitting $I$ into three subintervals:

- $(F * G) * H$: $F$ on $[0, 1/4]$ at $4\times$ speed, $G$ on $[1/4, 1/2]$ at $4\times$ speed, $H$ on $[1/2, 1]$ at $2\times$ speed.
- $F * (G * H)$: $F$ on $[0, 1/2]$ at $2\times$ speed, $G$ on $[1/2, 3/4]$ at $4\times$ speed, $H$ on $[3/4, 1]$ at $4\times$ speed.

Both are "do $F$, then $G$, then $H$" with different time allocations. We can write each as a reparametrization of a single underlying "concatenated path" $K(x, u)$ where $u \in [0, 3]$ runs through $F$ on $[0, 1]$, $G$ on $[1, 2]$, $H$ on $[2, 3]$. Specifically, $K(x, u) = F(x, u)$ for $u \in [0, 1]$, $K(x, u) = G(x, u - 1)$ for $u \in [1, 2]$, $K(x, u) = H(x, u - 2)$ for $u \in [2, 3]$.

The two concatenations are:

- $(F * G) * H = K \circ \phi_1$ where $\phi_1 : [0, 1] \to [0, 3]$ is the piecewise-linear map sending $[0, 1/4] \to [0, 1]$, $[1/4, 1/2] \to [1, 2]$, $[1/2, 1] \to [2, 3]$.
- $F * (G * H) = K \circ \phi_2$ where $\phi_2 : [0, 1] \to [0, 3]$ is the piecewise-linear map sending $[0, 1/2] \to [0, 1]$, $[1/2, 3/4] \to [1, 2]$, $[3/4, 1] \to [2, 3]$.

Both $\phi_1, \phi_2$ are continuous, map $0 \to 0$ and $1 \to 3$. By the [[Thm - Reparametrization Lemma|reparametrization lemma]] (applied with $K$ as the homotopy and $I$ rescaled to $[0, 3]$ — or equivalently, normalize $K$ to live on $[0, 1]$), $K \circ \phi_1 \simeq K \circ \phi_2$ rel endpoints.

This is what makes the reparametrization lemma the engine of the fundamental group: the two ways of associating three paths produce reparametrizations of the same underlying path with the same endpoints, and the lemma directly closes the gap.

---

# What Makes This Hard

The non-obvious step is *recognizing the common underlying path* $K$ and identifying the two reparametrizations $\phi_1, \phi_2$. The proof is a couple of lines once this is set up. The common error is to try to construct the associativity homotopy from scratch, writing down a complicated 2-parameter family — which is correct but unnecessary, since the reparametrization lemma already provides one.

---

# Rederivation Scaffold

**High-level strategy:**
Both sides of the desired homotopy are reparametrizations of a common "three-piece path" by different piecewise-linear functions $\phi_1, \phi_2 : I \to I$. Apply the reparametrization lemma.

**Subgoal decomposition:**

1. **Identify the common path.** Define $K : X \times [0, 3] \to Y$ by $K(x, u) = F(x, u)$ for $u \in [0, 1]$, $K(x, u) = G(x, u-1)$ for $u \in [1, 2]$, $K(x, u) = H(x, u-2)$ for $u \in [2, 3]$.
   - *Hint:* Pasting lemma ensures continuity.

2. **Identify the reparametrizations.** Let $\phi_1, \phi_2 : I \to [0, 3]$ be the piecewise-linear maps as above. Rescale to $I \to I$ by dividing by $3$.
   - *Hint:* Both fix $\{0, 1\}$ and are continuous.

3. **Apply reparametrization lemma.** [[Thm - Reparametrization Lemma]] gives $K \circ \phi_1 \simeq K \circ \phi_2$ rel $X \times \partial I$. The left side is $(F * G) * H$; the right side is $F * (G * H)$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Concatenation has a common "underlying path"
> **Statement:** Both $(F * G) * H$ and $F * (G * H)$ are reparametrizations of the common map $K : X \times [0, 3] \to Y$ defined by pasting $F, G, H$ end-to-end.
>
> **Hint:** Trace through the definitions.
>
> **Why needed:** Reduces associativity to a reparametrization question.
>
> > [!note]- Full proof
> > Direct computation. $(F * G) * H$ at $t \in [0, 1/4]$ equals $F * G$ at $2t \in [0, 1/2]$, which equals $F$ at $4t$. So $(F*G)*H$ at $t \in [0, 1/4]$ is $F(x, 4t) = K(x, 4t)$, with $4t \in [0, 1]$. Similarly for the other intervals. The reparametrization $\phi_1(t)$ sends $[0, 1/4]$ to $[0, 1]$ via $t \mapsto 4t$, etc. Match for $F*(G*H)$ analogously.

---

# Formal Proof

> [!note]- Complete formal proof
> Define the "common underlying path" $K : X \times [0, 3] \to Y$ by
> $$K(x, u) = \begin{cases} F(x, u) & u \in [0, 1] \\ G(x, u - 1) & u \in [1, 2] \\ H(x, u - 2) & u \in [2, 3] \end{cases}$$
> Continuous by the pasting lemma (consistent on overlaps: $F(x, 1) = G(x, 0)$, $G(x, 1) = H(x, 0)$).
>
> Define $\phi_1 : I \to [0, 3]$ piecewise linearly: $\phi_1(t) = 4t$ for $t \in [0, 1/4]$, $\phi_1(t) = 4t$ for $t \in [1/4, 1/2]$ (so $\phi_1(1/4) = 1, \phi_1(1/2) = 2$), $\phi_1(t) = 2t + 1$ for $t \in [1/2, 1]$ (so $\phi_1(1/2) = 2, \phi_1(1) = 3$). (Continuous, piecewise-linear, $\phi_1(0) = 0$, $\phi_1(1) = 3$.) Explicitly $\phi_1(t) = $ slope-4 on $[0, 1/2]$ and slope-2 on $[1/2, 1]$.
>
> Similarly $\phi_2 : I \to [0, 3]$: $\phi_2(t) = 2t$ for $t \in [0, 1/2]$, $\phi_2(t) = 4t - 1$ for $t \in [1/2, 3/4]$, $\phi_2(t) = 4t - 1$ for $t \in [3/4, 1]$ (matches at $t = 3/4$: $\phi_2(3/4) = 2$; $\phi_2(1) = 3$). (Continuous, $\phi_2(0) = 0$, $\phi_2(1) = 3$.)
>
> Verify: $(F * G) * H = K \circ (1_X \times \phi_1)$ and $F * (G * H) = K \circ (1_X \times \phi_2)$.
>
> Apply [[Thm - Reparametrization Lemma]] with $F$ replaced by $K$ (rescaled from $[0, 3]$ to $[0, 1]$ — equivalently, scale $\phi_1, \phi_2$ down to $\phi_i / 3 : I \to I$): since both $\phi_1, \phi_2$ agree on $\partial I = \{0, 1\}$ ($\phi_1(0) = \phi_2(0) = 0$, $\phi_1(1) = \phi_2(1) = 3$), we get
> $$K \circ \phi_1 \simeq K \circ \phi_2 \quad \text{rel } X \times \partial I.$$
> Substituting:
> $$(F * G) * H \simeq F * (G * H) \quad \text{rel } X \times \partial I. \qquad \blacksquare$$
>
> **Companion identities (Bredon 14.13).** $F * C \simeq F$ via reparametrization $\phi_1(t) = 2t$ for $t \in [0, 1/2]$, $\phi_1(t) = 1$ for $t \in [1/2, 1]$ versus $\phi_2(t) = t$. Both fix $\{0\}$ and send $1 \to 1$, so the reparametrization lemma applies.
>
> **Inverse (Bredon 14.15).** $F * F^{-1}$ is $F \circ \phi$ where $\phi(t) = 2t$ for $t \leq 1/2$, $\phi(t) = 2 - 2t$ for $t \geq 1/2$; the constant homotopy $C$ at $F(\cdot, 0)$ is $F \circ (\phi_2 \equiv 0)$. Both have $\phi(0) = \phi(1) = 0$, so the lemma applies.

---

# Cross-Field Exercise Suggestions

**Higher homotopy groups are abelian.** $\pi_n(X, x_0)$ for $n \geq 2$ is abelian. The proof uses the Eckmann-Hilton argument: in dimension $\geq 2$, one has two "independent" concatenation operations (along two different axes), and the reparametrization-style argument shows they coincide and are commutative.

**Loop spaces are H-spaces.** The loop space $\Omega X$ at a basepoint has a concatenation operation, making it an *H-space* (a space with a homotopy-associative multiplication, identity, and inverses). The associativity is exactly this theorem. The reparametrization lemma is what gives $\Omega X$ its group-up-to-homotopy structure.

**$A_\infty$ structures and operads.** In the modern formulation, the homotopy-associativity here is the first step in an infinite tower of higher coherence conditions called an **$A_\infty$ structure**, governed by Stasheff's associahedra. The reparametrization lemma provides the 2-cell associator $K_4$; higher levels involve more complex reparametrizations.

---

# Bridges

- **[[Thm - Reparametrization Lemma]]** — the engine of the proof.

- **[[Def - Homotopy]]** — concatenation $F * G$ is defined here.

- **[[Def - Topological Group]]** — analogous statement: in a topological *group*, concatenation of paths can be combined with the group operation to give an abelian structure on $\pi_1$.

---

# Unlocked by This

> [!tip] Fundamental Group *(from Algebraic Topology)*
> The fundamental group $\pi_1(X, x_0)$ is the set of homotopy classes of loops at $x_0$ under concatenation. This theorem (plus the identity and inverse laws) is precisely what makes $\pi_1$ a *group*. Without it, we'd have only a quasi-group.

> [!tip] Fundamental Groupoid *(from Algebraic Topology)*
> The fundamental groupoid $\Pi_1(X)$ has paths up to homotopy as morphisms, with associativity coming from this theorem.

> [!tip] $A_\infty$-Structure *(from Higher Category Theory)*
> The associativity-up-to-homotopy here is the first level of a hierarchy: homotopies of homotopies of homotopies satisfying coherence conditions. This is an **$A_\infty$-structure**, central in modern algebraic topology and homological algebra.
