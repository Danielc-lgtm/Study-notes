---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Cauchy's Theorem for Simply Connected Domains"
  - "Def - Simply Connected Domain in Complex Analysis"
  - "Def - Branch of the Logarithm"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}$ is open and simply connected, with $0 \notin U$. A **branch of $\log$** on $U$ is a continuous function $\ell : U \to \mathbb{C}$ with $e^{\ell(z)} = z$ for all $z \in U$. Once $\log$ exists, a branch of $z^\alpha$ is defined as $e^{\alpha \ell(z)}$ for any $\alpha \in \mathbb{C}$. Full registry on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Statement

> **Theorem (Existence of Log and Square Root on Simply Connected Domains).** Let $U \subseteq \mathbb{C}$ be open and simply connected with $0 \notin U$. Then there exists a holomorphic function $\ell : U \to \mathbb{C}$ — a **branch of the logarithm** — with
> $$e^{\ell(z)} = z \qquad\text{and}\qquad \ell'(z) = \frac{1}{z} \qquad\text{for all } z \in U.$$
> The branch $\ell$ is unique up to addition of an integer multiple of $2\pi i$. Once $\ell$ is fixed, for every $\alpha \in \mathbb{C}$ the function $z^\alpha := e^{\alpha\ell(z)}$ is a holomorphic branch of the $\alpha$-power on $U$, satisfying $(z^{1/n})^n = z$ for every positive integer $n$.
>
> More generally, if $f : U \to \mathbb{C}^\times$ is any nowhere-vanishing holomorphic function on a simply connected $U$, then there exists holomorphic $g : U \to \mathbb{C}$ with $e^{g(z)} = f(z)$.

---

# Motivation

The complex logarithm and complex powers are multi-valued: $e^{i\theta} = e^{i(\theta + 2\pi)}$, so $\log z$ has infinitely many possible values differing by $2\pi i k$. A *branch* of $\log$ is a choice of one value at each point, depending continuously on $z$. The question: on what domains does such a continuous choice exist?

The answer is exactly simply-connected domains avoiding the origin. On the punctured plane $\mathbb{C}^\times$, no continuous branch of $\log$ exists — the principal branch has a discontinuity across the negative real axis. But on any simply connected $U$ avoiding $0$, a branch exists, and it is unique up to addition of an integer multiple of $2\pi i$.

This is one of the most directly used corollaries of Cauchy's theorem in complex analysis. Many integrals, function-theoretic arguments, and conformal mapping constructions require choosing branches of $\log$ or fractional powers, and the simple-connectedness condition is the recurring justification. The Riemann mapping theorem, the existence of $z^\alpha$ on conformally-prescribed domains, the contour integrals around branch cuts of $\log$ — all rest on this theorem.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$U$ simply connected, $0 \notin U$". The sources broaden recognition of when this applies.

The first disguised source is **a slit plane.** Property $B$: $U = \mathbb{C} \setminus L$ where $L$ is a closed ray, half-line, or simple arc from $0$ to $\infty$. Bridge: removing a ray from $0$ makes the complement simply connected (no loop can wind around $0$ once $L$ is removed), and excludes $0$. Example: principal branch of $\log$ on $\mathbb{C} \setminus (-\infty, 0]$.

The second disguised source is **a half-plane or wedge avoiding $0$.** Property $B$: $U$ is a half-plane, wedge $\{r e^{i\theta} : \theta_1 < \theta < \theta_2\}$, or similar convex subset of $\mathbb{C}^\times$. Bridge: convex hence simply connected, and $0$ is excluded. Branches of $\log$ exist on every wedge of angular width less than $2\pi$.

The third disguised source is **a simply connected universal cover.** Property $B$: working on the universal cover $\tilde U$ of a (non-simply-connected) $U \subseteq \mathbb{C}^\times$. Bridge: the universal cover is simply connected by construction; $\log$ exists on $\tilde U$. This is how multi-valued functions are made single-valued in general — by going to the universal cover, equivalent to choosing a branch.

**Targets (Output Amplification)**

The conclusion is "a holomorphic branch of $\log$ exists on $U$".

Combine with **arbitrary complex powers.** Property $D$: given a branch $\ell$ of $\log$ on $U$ and any $\alpha \in \mathbb{C}$. Amplified result $E$: $z^\alpha := e^{\alpha \ell(z)}$ is a holomorphic branch of the $\alpha$-power. In particular, $z^{1/n}$ (an $n$-th root) exists for any positive integer $n$.

Combine with **a nowhere-vanishing holomorphic function.** Property $D$: $f : U \to \mathbb{C}^\times$ holomorphic and nowhere zero. Amplified result $E$: $\log f$ exists on $U$, i.e., a holomorphic $g : U \to \mathbb{C}$ with $e^g = f$. Proof: apply the log-existence theorem with $f$ in place of $z$, observing that $f'/f$ is holomorphic on simply connected $U$ and has a primitive. This handles the general case of "logarithms of holomorphic functions" beyond the specific case of $\log z$.

Combine with **Riemann mapping.** Property $D$: $U$ is a simply connected proper open subset of $\mathbb{C}$, and we want to construct a biholomorphism to $\mathbb{D}$. Amplified result $E$: branches of $\log$ and $z^\alpha$ provide building blocks for the construction.

---

# Why Is It True

The intuition: on a simply connected $U$ avoiding $0$, the function $1/z$ is holomorphic with no singularities in $U$. Cauchy's theorem says it has a primitive — call it $\ell(z)$. This primitive is the logarithm: $\ell'(z) = 1/z$, so $e^{\ell(z)}/z$ has derivative $e^{\ell}(\ell' - 1/z) \cdot (something) = 0$ (computed properly), so it is constant; adjusting $\ell$ by a constant, $e^{\ell(z)} = z$.

Why does it fail on $\mathbb{C}^\times$? Because $\mathbb{C}^\times$ is *not* simply connected: the unit circle has nonzero winding number around $0 \notin \mathbb{C}^\times$. So Cauchy's theorem does not apply, and $1/z$ has no primitive on $\mathbb{C}^\times$ — the integral $\int_{|z|=1} dz/z = 2\pi i \neq 0$ is the obstruction. The simple-connectedness condition is exactly what kills this obstruction.

The same argument generalizes: any nowhere-vanishing holomorphic $f$ on simply connected $U$ has $f'/f$ holomorphic on $U$ (no singularities, because $f$ is nowhere zero), hence has a primitive $g$. Then $e^g/f$ has derivative zero (compute), so is constant, and after adjusting $g$ by a constant, $e^g = f$. So $g$ is a holomorphic logarithm of $f$.

For powers: once $\log$ exists, $z^\alpha := e^{\alpha \log z}$ is the standard definition. Composing two holomorphic functions, this is holomorphic.

---

# What Makes This Hard

The non-obvious step is realizing that **simple-connectedness is the right hypothesis** — that $\log z$ exists exactly on simply connected $U \subseteq \mathbb{C}^\times$, not on all of $\mathbb{C}^\times$, and that the obstruction is precisely the winding number around $0$. A common confusion is to think branches exist on all of $\mathbb{C} \setminus \{0\}$ by choosing $\arg z \in [0, 2\pi)$; this gives a discontinuous function (jump across the positive real axis), not a holomorphic branch. A second slip is forgetting that the choice of branch is *not unique* — different simply connected $U$ can have different branches differing by $2\pi i k$, and the "principal branch" is just one of many.

---

# Rederivation Scaffold

**High-level strategy:**
On simply connected $U$ avoiding $0$, $1/z$ is holomorphic with no singularities, so by Cauchy's theorem it has a primitive. That primitive is the logarithm. Verify $e^{\ell(z)} = z$ by computing the derivative of $e^{\ell(z)}/z$.

**Subgoal decomposition:**

1. **$1/z$ has a primitive on $U$.** Apply Cauchy's theorem to $f(z) = 1/z$ on simply connected $U \subseteq \mathbb{C}^\times$.
   - *Hint:* Cauchy's theorem gives primitives for holomorphic functions on simply connected domains; $1/z$ is holomorphic on $\mathbb{C}^\times \supseteq U$.

2. **The primitive is a logarithm.** If $\ell'(z) = 1/z$, show $e^{\ell(z)} = c \cdot z$ for some constant $c$, hence (after adjusting $\ell$) $e^{\ell(z)} = z$.
   - *Hint:* Compute $(e^{\ell(z)}/z)' = (e^{\ell(z)} \ell'(z) z - e^{\ell(z)})/z^2 = e^{\ell(z)}(z \cdot 1/z - 1)/z^2 = 0$.
   - *Why needed:* Establishes that the primitive *is* a logarithm, not some other related function.

3. **Power functions.** Define $z^\alpha := e^{\alpha \ell(z)}$ for any $\alpha \in \mathbb{C}$. Verify this is holomorphic and behaves correctly under multiplication.

4. **Square root and $n$-th roots.** $z^{1/2} = e^{\ell(z)/2}$, $z^{1/n} = e^{\ell(z)/n}$. Verify $(z^{1/2})^2 = e^{\ell(z)} = z$.

---

# Lemma Decomposition

> [!note]- Lemma 1: A primitive of $1/z$ on simply connected $U \subseteq \mathbb{C}^\times$ is a branch of $\log$
> **Statement:** If $\ell : U \to \mathbb{C}$ is holomorphic with $\ell'(z) = 1/z$, then $e^{\ell(z)} = c z$ for some constant $c \in \mathbb{C}^\times$.
>
> **Hint:** Differentiate $e^{\ell(z)}/z$.
>
> > [!note]- Full proof
> > Compute $\frac{d}{dz}\left(\frac{e^{\ell(z)}}{z}\right) = \frac{e^{\ell(z)}\ell'(z) z - e^{\ell(z)}}{z^2} = \frac{e^{\ell(z)}(z\cdot(1/z) - 1)}{z^2} = 0$. So $e^{\ell(z)}/z$ is constant on the connected $U$. Set the constant to $c$; then $e^{\ell(z)} = cz$. Replacing $\ell$ by $\ell - \log c$ (adjusting by a constant), $e^{\ell(z)} = z$ as required.

> [!note]- Lemma 2: Logarithm of a holomorphic function
> **Statement:** If $f : U \to \mathbb{C}^\times$ is holomorphic and $U$ is simply connected, then there exists holomorphic $g : U \to \mathbb{C}$ with $e^{g(z)} = f(z)$.
>
> **Hint:** $f'/f$ is holomorphic on $U$ (no singularities since $f$ is nowhere zero); apply Cauchy's theorem.
>
> > [!note]- Full proof
> > Since $f$ is holomorphic and nowhere zero on $U$, $f'/f$ is holomorphic on $U$. By Cauchy's theorem on simply connected $U$, $f'/f$ has a primitive $g$ on $U$. Compute $(e^g/f)' = (e^g g' f - e^g f')/f^2 = e^g(g'f - f')/f^2 = e^g(f'/f \cdot f - f')/f^2 = 0$. So $e^g/f$ is constant; adjusting $g$ by a constant, $e^g = f$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $U$ be simply connected with $0 \notin U$. The function $1/z$ is holomorphic on $U$.
>
> **Step 1:** By [[Thm - Cauchy's Theorem for Simply Connected Domains|Cauchy's theorem]], $1/z$ has a primitive $\ell : U \to \mathbb{C}$ with $\ell'(z) = 1/z$.
>
> **Step 2:** By Lemma 1, $\ell$ is a branch of $\log$ on $U$, i.e., $e^{\ell(z)} = z$ after adjusting by a constant.
>
> **Step 3:** For any $\alpha \in \mathbb{C}$, $z^\alpha := e^{\alpha \ell(z)}$ is holomorphic on $U$, with $(z^\alpha)' = \alpha z^{\alpha - 1}$ (using $z^{\alpha-1} = e^{(\alpha-1)\ell(z)} = e^{\alpha\ell(z)}/e^{\ell(z)} = z^\alpha/z$). In particular, $z^{1/n}$ is an $n$-th root of $z$ ($z^{1/n})^n = e^{\ell(z)} = z$.
>
> **Uniqueness modulo $2\pi i \mathbb{Z}$.** Any two branches of $\log$ on $U$ differ by a continuous integer-valued function (times $2\pi i$), hence by a constant. So branches are unique up to addition of $2\pi i k$ for some $k \in \mathbb{Z}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Conformal mapping construction.** Many explicit conformal maps use compositions of $\log$, $z^{1/2}$, exponentials, and Möbius transformations. For instance, the map from the right half-plane to the upper half-plane is $z \mapsto z^2$ (using the branch defined on the right half-plane); composing with other Möbius maps gives biholomorphisms between many domain pairs. The existence of branches is what makes these constructions legal.

**Keyhole contour integrals.** Integrals like $\int_0^\infty x^\alpha P(x)\,dx$ for $\alpha \notin \mathbb{Z}$ are evaluated by contour integration with $z^\alpha$ — but $z^\alpha$ is multi-valued, so the contour must avoid the positive real axis (where the branches of $z^\alpha$ are discontinuous), giving a *keyhole contour*. The integrals on the upper and lower edges of the keyhole differ by a factor $e^{2\pi i \alpha}$, which gives the key cancellation.

**Schwarz–Christoffel mapping.** The Schwarz–Christoffel formula for conformal mapping of the upper half-plane to a polygon involves products of fractional powers $(z - a_k)^{\alpha_k - 1}$ — these require branches of $z^\alpha$ defined on appropriate cut planes. The existence theorem ensures these branches can be chosen consistently.

---

# Bridges

- **[[Thm - Cauchy's Theorem for Simply Connected Domains]]** — the foundational tool. The primitive that yields $\log$ comes from Cauchy.

- **[[Def - Branch of the Logarithm]]** — the object being constructed.

- **[[Def - Simply Connected Domain in Complex Analysis]]** — the topological hypothesis that makes the construction work.

- **[[Def - Complex Power]]** — once $\log$ exists, all complex powers are defined as $z^\alpha = e^{\alpha\log z}$.

---

# Unlocked by This

> [!tip] Riemann Mapping Theorem *(from §3.5+)*
> The [[Thm - Riemann Mapping Theorem (Statement)|Riemann mapping theorem]] uses branches of $\log$ and $z^{1/2}$ in its proof: the construction of an injective holomorphic map from a simply connected $U$ to the disc uses $z^{1/2}$ to "open up" branch points.

> [!tip] Riemann Surfaces *(from Algebraic Geometry)*
> When the domain is *not* simply connected, branches of $\log$ live on the **universal cover** of the domain. The universal cover of $\mathbb{C}^\times$ is $\mathbb{C}$ itself, with covering map $w \mapsto e^w$ — so the "global" $\log$ is the inverse of $\exp$, but it lives on $\mathbb{C}$, not on $\mathbb{C}^\times$. This is the seed of **Riemann surface theory**.
