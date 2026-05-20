---
type: theorem
subject: topology
prereqs:
  - "Def - Homotopy"
  - "Def - Continuous Map"
tags: [analysis, topology, homotopy, fundamental-group]
---

# Notation

$X, Y$ topological spaces. $I = [0, 1]$, $\partial I = \{0, 1\}$. $\phi_1, \phi_2 : (I, \partial I) \to (I, \partial I)$ continuous maps fixing the endpoints (i.e., $\phi_i(0) = 0, \phi_i(1) = 1$, or more generally agreeing on $\partial I$). $F : X \times I \to Y$ a homotopy. The reparametrized homotopies are $G_i(x, t) = F(x, \phi_i(t))$. The full registry is on the topic page.

---

# Motivation

When we want to do algebra with homotopies — concatenate them, take inverses, prove associativity — we need to compose them with parametrizations of the interval. For example, to concatenate two paths at the midpoint, we squeeze each into half the interval. The result depends on *which* squeezing we use: we could squash each path into $[0, 1/2]$ and $[1/2, 1]$ respectively, or into $[0, 1/3]$ and $[1/3, 1]$, or any other proportional split.

The reparametrization lemma says: as long as the parametrization $\phi$ fixes the endpoints, the resulting homotopies are themselves homotopic. In particular, different ways of "running the path at different speeds" produce homotopic, not just topologically similar, paths. This is what makes the fundamental group well-defined: the *associativity, identity, and inverse axioms* hold up to homotopy because reparametrizations are absorbed by further homotopies.

The lemma is a tool, not a result of intrinsic interest. Its power comes from the slick proof: a 2-parameter family $H(x, t, s) = F(x, s \phi_2(t) + (1-s)\phi_1(t))$ provides a single homotopy from $G_1 = F \circ \phi_1$ to $G_2 = F \circ \phi_2$, using *linear interpolation in the parameter*. The proof is purely formal: the convex combination of two interval reparametrizations is still an interval reparametrization (because $I$ is convex), and applying $F$ gives a continuous homotopy of homotopies.

---

# Statement

Let $X, Y$ be topological spaces, $F : X \times I \to Y$ a continuous map (a homotopy), and let $\phi_1, \phi_2 : I \to I$ be continuous maps with $\phi_1|_{\partial I} = \phi_2|_{\partial I}$ (i.e., $\phi_1$ and $\phi_2$ agree on the endpoints).

Define $G_i(x, t) := F(x, \phi_i(t))$ for $i = 1, 2$. Then $G_1 \simeq G_2$ **rel** $X \times \partial I$ — there is a continuous map $H : X \times I \times I \to Y$ with:

- $H(x, t, 0) = G_1(x, t)$,
- $H(x, t, 1) = G_2(x, t)$,
- $H(x, 0, s) = G_1(x, 0) = G_2(x, 0)$ for all $s$,
- $H(x, 1, s) = G_1(x, 1) = G_2(x, 1)$ for all $s$.

(So the homotopy from $G_1$ to $G_2$ keeps the endpoint values fixed.)

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition "$\phi_1, \phi_2 : I \to I$ continuous with $\phi_1|_{\partial I} = \phi_2|_{\partial I}$" is the key. Common sources where this arises:

**Concatenation of paths.** Property $B$: we have three paths $\alpha, \beta, \gamma : I \to Y$ and want to compare $(\alpha * \beta) * \gamma$ with $\alpha * (\beta * \gamma)$. The bridge: both are reparametrizations of the same underlying path (going through $\alpha, \beta, \gamma$ in sequence) — one splits the interval as $[0, 1/4] \cup [1/4, 1/2] \cup [1/2, 1]$, the other as $[0, 1/2] \cup [1/2, 3/4] \cup [3/4, 1]$. Both reparametrizations fix endpoints, so the lemma applies. *Example:* associativity of concatenation in the fundamental group ([[Thm - Concatenation of Homotopies is Associative up to Homotopy]]).

**Constant-path identity.** Property $B$: we want $\alpha * c \simeq \alpha$ where $c$ is the constant path at $\alpha(1)$. The bridge: $\alpha * c$ is a reparametrization of $\alpha$: it runs $\alpha$ on $[0, 1/2]$ and stays constant on $[1/2, 1]$. The "stay constant" portion of $\phi_2$ corresponds to $\phi_2(t) = 1$ for $t \in [1/2, 1]$, while $\phi_1(t) = t$ throughout. Both $\phi_1, \phi_2$ fix $\{0, 1\}$. The lemma gives $\alpha * c \simeq \alpha$ rel endpoints. (Proposition 14.13 in Bredon.)

**Inverse path.** Property $B$: $\alpha * \alpha^{-1} \simeq c$ where $\alpha^{-1}(t) = \alpha(1 - t)$ and $c$ is the constant path at $\alpha(0)$. The bridge: $\alpha * \alpha^{-1}$ is a reparametrization that goes from $\alpha(0)$ to $\alpha(1/2) = \alpha(1)$ and back to $\alpha(0)$. The reparametrization $\phi_1$ traces this out; $\phi_2$ is the constant function at $0$. Both fix the endpoints ($\phi_1(0) = \phi_1(1) = 0$; $\phi_2(t) = 0$ for all $t$). The lemma gives the result. (Proposition 14.15 in Bredon.)

**Targets (Output Amplification)**

The conclusion is "$G_1 \simeq G_2$ rel $X \times \partial I$", which is the technical input to several structural results.

Combine with **concatenation respects homotopy.** Property $D$: if $F_1 \simeq F_2$ rel endpoints and $G_1 \simeq G_2$ rel endpoints, then $F_1 * G_1 \simeq F_2 * G_2$ rel endpoints. The amplified result $E$: the concatenation operation is well-defined on homotopy classes, hence the fundamental groupoid is a category. This combination uses the reparametrization lemma indirectly — both as the proof of associativity and as a consequence of well-definedness.

Combine with **the constant homotopy.** Property $D$: $F * c$ where $c$ is constant. The amplified result $E$: $c$ is a two-sided identity for the concatenation product, completing the group structure of $\pi_1$. (Combined with the inverse-path identity.)

---

# Why Is It True

The proof is a single explicit homotopy: $H(x, t, s) = F(x, s \phi_2(t) + (1-s) \phi_1(t))$. At $s = 0$, $H(x, t, 0) = F(x, \phi_1(t)) = G_1(x, t)$. At $s = 1$, $H(x, t, 1) = F(x, \phi_2(t)) = G_2(x, t)$. So $H$ is a homotopy between $G_1$ and $G_2$.

The endpoint conditions: at $t = 0$, $\phi_1(0) = \phi_2(0)$, so $s \phi_2(0) + (1-s)\phi_1(0) = \phi_1(0)$ for all $s$. Hence $H(x, 0, s) = F(x, \phi_1(0)) = G_1(x, 0)$, constant in $s$. Same at $t = 1$. So the homotopy is rel $X \times \partial I$.

Continuity of $H$: $F$ is continuous, $\phi_1, \phi_2$ are continuous, scalar multiplication and addition are continuous, so the composition $H = F \circ ((x, t, s) \mapsto (x, s \phi_2(t) + (1-s)\phi_1(t)))$ is continuous.

The deep reason this works: the interval $I$ is **convex**. Any two continuous maps $\phi_1, \phi_2 : I \to I$ can be joined by a continuous family of maps via *linear interpolation in the codomain*: the map $\phi_s(t) = s \phi_2(t) + (1-s)\phi_1(t)$ is itself a continuous map $I \to I$ for each $s$, because $I = [0, 1]$ is convex (so the convex combination of two values in $I$ is again in $I$). Combined with the agreement at the endpoints, the path of reparametrizations is a homotopy of homotopies.

This is a special case of a general principle: in a *convex* target, any two maps with the same boundary values are joined by a straight-line homotopy. The lemma is just this principle applied with $I$ as the target.

---

# What Makes This Hard

The lemma is not hard — it's a 3-line proof. What's tricky is *recognizing when to apply it*. The non-obvious step in any concatenation-associativity argument is to identify the reparametrizations $\phi_1, \phi_2$ that encode the two ways of splitting the interval. The most common error is to construct the wrong $\phi_2$ — failing to track which slice of the interval each piece is mapped to.

---

# Rederivation Scaffold

**High-level strategy:**
Linear interpolation between $\phi_1$ and $\phi_2$ in the convex target $I$ gives a continuous family of reparametrizations $\phi_s$ with the same boundary values. Applying $F$ to $\phi_s$ produces the homotopy $H$.

**Subgoal decomposition:**

1. **Define the interpolation.** Set $\phi_s(t) = s \phi_2(t) + (1-s)\phi_1(t)$ for $s \in I$. Verify $\phi_s : I \to I$ (uses convexity of $I$).
   - *Hint:* Convex combination of two values in $[0, 1]$ is in $[0, 1]$.

2. **Define $H$.** Set $H(x, t, s) = F(x, \phi_s(t))$. Continuous by composition.
   - *Hint:* Multiplication and addition are continuous.

3. **Verify endpoint conditions.** $H(x, t, 0) = G_1(x, t)$, $H(x, t, 1) = G_2(x, t)$, and $H(x, 0, s), H(x, 1, s)$ are independent of $s$ (using $\phi_1, \phi_2$ agree on $\partial I$).

---

# Lemma Decomposition

> [!note]- Lemma 1: Convex combination preserves $I$
> **Statement:** For $\phi_1, \phi_2 : I \to I$ continuous and $s \in [0, 1]$, the map $\phi_s(t) := s \phi_2(t) + (1-s) \phi_1(t)$ is continuous $I \to I$.
>
> **Hint:** $I = [0, 1]$ is convex.
>
> **Why needed:** Ensures the reparametrization stays in the domain of $F$.
>
> > [!note]- Full proof
> > Continuity is immediate (composition of continuous maps). For range: since $\phi_1(t), \phi_2(t) \in [0, 1]$ and $s, 1-s \in [0, 1]$, the convex combination $s \phi_2(t) + (1-s)\phi_1(t)$ lies in $[0, 1] = I$.

---

# Formal Proof

> [!note]- Complete formal proof
> Define $H : X \times I \times I \to Y$ by
> $$H(x, t, s) := F(x, s \phi_2(t) + (1-s) \phi_1(t)).$$
>
> *Continuity:* $\phi_1, \phi_2$ are continuous, so $(t, s) \mapsto s\phi_2(t) + (1-s)\phi_1(t)$ is continuous $I \times I \to \mathbb{R}$. By Lemma 1, the range is in $I$, so this is a continuous map $I \times I \to I$. Combined with continuity of $F : X \times I \to Y$, $H$ is continuous.
>
> *Endpoint conditions:*
> - $H(x, t, 0) = F(x, 0 \cdot \phi_2(t) + 1 \cdot \phi_1(t)) = F(x, \phi_1(t)) = G_1(x, t)$.
> - $H(x, t, 1) = F(x, 1 \cdot \phi_2(t) + 0 \cdot \phi_1(t)) = F(x, \phi_2(t)) = G_2(x, t)$.
>
> *Rel $X \times \partial I$:*
> - For $t = 0$: $\phi_1(0) = \phi_2(0)$ (call this value $a$), so $H(x, 0, s) = F(x, sa + (1-s)a) = F(x, a)$, independent of $s$.
> - For $t = 1$: $\phi_1(1) = \phi_2(1)$ (call this $b$), so $H(x, 1, s) = F(x, b)$, independent of $s$.
>
> So $H$ is a homotopy from $G_1$ to $G_2$ relative to $X \times \partial I$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Homotopy rel boundary for higher-dimensional cells.** The lemma generalizes: if $\phi_1, \phi_2 : D^n \to D^n$ agree on $\partial D^n = S^{n-1}$, then for any homotopy $F : X \times D^n \to Y$, the precompositions are homotopic rel $X \times S^{n-1}$. The proof is the same — straight-line homotopy in the convex target $D^n$. This is used in defining higher homotopy groups via maps from disks.

**Path spaces and exponential law.** The reparametrization lemma is the topological content of: the space of paths $\text{Map}((I, \partial I), (Y, \partial))$ is well-behaved under reparametrization. This connects to the exponential law $\text{Map}(X \times I, Y) \cong \text{Map}(X, Y^I)$ in compactly-generated spaces.

**Reparametrization in flow theory.** A flow $\Phi : X \times \mathbb{R} \to X$ has the property that reparametrizations of $\mathbb{R}$ (orientation-preserving homeomorphisms fixing $\pm \infty$) give equivalent dynamical systems. The same convex-target trick applies, modulo working with $\mathbb{R}$ instead of $I$.

---

# Bridges

- **[[Thm - Concatenation of Homotopies is Associative up to Homotopy]]** — applies the reparametrization lemma to show that $(F * G) * H \simeq F * (G * H)$.

- **[[Def - Homotopy]]** — the lemma is a statement about reparametrizing the time parameter of a homotopy.

- **[[Def - Convex Body]]** — the proof uses convexity of $I$ in an essential way.

---

# Unlocked by This

> [!tip] Fundamental Group *(from Algebraic Topology)*
> The reparametrization lemma is the technical input to the well-definedness of the **fundamental group** $\pi_1(X, x_0)$: associativity, identity, and inverse properties of concatenation all reduce to reparametrization. Without the lemma, $\pi_1$ would only be a *quasi-group*; with it, $\pi_1$ is a genuine group.

> [!tip] Higher Homotopy Groups *(from Algebraic Topology)*
> Higher homotopy groups $\pi_n(X)$ use a higher-dimensional version of the lemma: any reparametrization of $D^n$ rel boundary gives a homotopic map, ensuring the group operation on $\pi_n$ is well-defined.

> [!tip] Fundamental Groupoid *(from Algebraic Topology)*
> The **fundamental groupoid** $\Pi_1(X)$ has points of $X$ as objects and homotopy classes of paths as morphisms. The reparametrization lemma is what makes the groupoid composition associative and unital.
