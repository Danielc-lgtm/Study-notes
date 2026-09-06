---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - Line Integral of a 1-Form"
  - "Def - Covector Field and Differential 1-Form"
  - "Def - Smooth Map between Manifolds"
tags: [geometry, differential-geometry, line-integral, parameterization]
---

# Problem Statement

Let $M$ be a smooth manifold, $\omega \in \Omega^1(M)$ a smooth 1-form, and $\gamma : [a, b] \to M$ a smooth curve. Let $\sigma : [c, d] \to [a, b]$ be an orientation-preserving smooth [[Def - Diffeomorphism|diffeomorphism]] (i.e., $\sigma'(s) > 0$ for all $s$, with $\sigma(c) = a, \sigma(d) = b$). Define the reparameterized curve $\tilde\gamma := \gamma \circ \sigma : [c, d] \to M$. Show that
$$\int_{\tilde\gamma} \omega = \int_\gamma \omega.$$

What happens for an orientation-reversing reparameterization (i.e., $\sigma'(s) < 0$, $\sigma(c) = b, \sigma(d) = a$)?

**Recall:**

The [[Def - Line Integral of a 1-Form|line integral]] of $\omega$ along $\gamma$ is
$$\int_\gamma \omega := \int_a^b \omega_{\gamma(t)}(\gamma'(t)) \, dt.$$
The chain rule for smooth curves: $\tilde\gamma'(s) = (\gamma \circ \sigma)'(s) = \sigma'(s) \cdot \gamma'(\sigma(s))$.

---

# Convergent Strategy

**Problem class:** Verification of a naturality / invariance property of an integral. The strategy is the **substitution rule** for ordinary Riemann integrals, applied to the parameterization.

**Assumption pattern:** $\sigma$ is an orientation-preserving diffeomorphism, so $\sigma' > 0$ and the substitution $t = \sigma(s)$ in the integral $\int_a^b f(t) dt$ gives $\int_c^d f(\sigma(s)) \sigma'(s) ds$ by the chain rule for derivatives. Apply this with $f(t) = \omega_{\gamma(t)}(\gamma'(t))$.

**Theorem routing:** Pull back the line integral $\int_\gamma \omega$ via the substitution. The integrand transforms as $f(\sigma(s)) \sigma'(s) = \omega_{\gamma(\sigma(s))}(\gamma'(\sigma(s))) \cdot \sigma'(s) = \omega_{\tilde\gamma(s)}(\tilde\gamma'(s))$, where the last equality uses $\tilde\gamma(s) = \gamma(\sigma(s))$ and $\tilde\gamma'(s) = \sigma'(s) \gamma'(\sigma(s))$ and the linearity of $\omega$ in the velocity. The transformed integrand is exactly the integrand for $\int_{\tilde\gamma} \omega$.

**Key decision point:** The non-obvious step is that **the chain rule combined with linearity of the pairing $\omega(v)$ produces exactly the velocity of the reparameterized curve**. This is the structural reason the line integral is well-defined as a path integral — the substitution is forced by the pairing's linearity.

---

# Legal Operations Used

1. **Operation 6 from the topic page (pull back a 1-form along an arbitrary smooth map).** The diffeomorphism $\sigma : [c, d] \to [a, b]$ allows pulling back the 1-form $\omega$ on $M$ to the reparameterized curve, which is the substitution-rule mechanism.

2. **Substitution rule for ordinary Riemann integrals.** The standard $\int_a^b f(t) dt = \int_c^d f(\sigma(s)) \sigma'(s) ds$ for $\sigma$ an orientation-preserving diffeomorphism.

3. **Linearity of the pairing.** $\omega(c v) = c \omega(v)$ for $c \in \mathbb{R}$, used to factor $\sigma'(s)$ out of the integrand.

---

# Hints

> [!note]- Hint 1
> Start with $\int_{\tilde\gamma} \omega = \int_c^d \omega_{\tilde\gamma(s)}(\tilde\gamma'(s)) ds$. Compute $\tilde\gamma'(s)$ using the chain rule.

> [!note]- Hint 2
> $\tilde\gamma'(s) = \sigma'(s) \gamma'(\sigma(s))$ — the chain rule. Substitute into the line integral and use linearity of $\omega_{\tilde\gamma(s)}$ in its argument.

> [!note]- Hint 3
> The integral becomes $\int_c^d \omega_{\gamma(\sigma(s))}(\gamma'(\sigma(s))) \cdot \sigma'(s) \, ds$. Apply the substitution $t = \sigma(s)$ — recognize that this is $\int_a^b \omega_{\gamma(t)}(\gamma'(t)) dt = \int_\gamma \omega$.

> [!note]- Hint 4
> For orientation-reversing $\sigma$: $\sigma'(s) < 0$, $\sigma(c) = b, \sigma(d) = a$. The substitution gives $\int_c^d (\dots) \sigma'(s) ds = -\int_a^b (\dots) dt = -\int_\gamma \omega$. The sign reverses.

---

# Solution

**Plan:** Compute $\int_{\tilde\gamma} \omega$ by unfolding the definition. Apply the chain rule and the substitution rule to recover $\int_\gamma \omega$. For orientation-reversing $\sigma$, the substitution introduces a sign change.

**Step 1: Compute the velocity of the reparameterized curve.**

> [!note]- Derivation
> By the chain rule (smooth case), $\tilde\gamma'(s) = (d/ds)|_s \tilde\gamma = (d/ds)|_s (\gamma \circ \sigma) = \gamma'(\sigma(s)) \cdot \sigma'(s)$, where the multiplication makes sense because $\sigma'(s) \in \mathbb{R}$ is a scalar and $\gamma'(\sigma(s)) \in T_{\gamma(\sigma(s))}M$ is a tangent vector.

**Step 2: Compute the integrand at $s$.**

> [!note]- Derivation
> Plug into the line-integral integrand for $\int_{\tilde\gamma} \omega$:
> $$\omega_{\tilde\gamma(s)}(\tilde\gamma'(s)) = \omega_{\gamma(\sigma(s))} (\sigma'(s) \cdot \gamma'(\sigma(s))) = \sigma'(s) \cdot \omega_{\gamma(\sigma(s))}(\gamma'(\sigma(s))),$$
> using linearity of $\omega_{\gamma(\sigma(s))}$ in its argument.

**Step 3: Apply the substitution rule.**

> [!note]- Derivation
> Define $f(t) := \omega_{\gamma(t)}(\gamma'(t))$, a smooth function on $[a, b]$. Then
> $$\int_{\tilde\gamma} \omega = \int_c^d \omega_{\tilde\gamma(s)}(\tilde\gamma'(s)) ds = \int_c^d \sigma'(s) f(\sigma(s)) ds.$$
> By the substitution rule (with $t = \sigma(s)$, $dt = \sigma'(s) ds$, $\sigma$ orientation-preserving so $\sigma(c) = a$ and $\sigma(d) = b$):
> $$\int_c^d \sigma'(s) f(\sigma(s)) ds = \int_a^b f(t) dt = \int_\gamma \omega.$$
> So $\int_{\tilde\gamma} \omega = \int_\gamma \omega$.

**Step 4: Orientation-reversing case.**

> [!note]- Derivation
> If $\sigma : [c, d] \to [a, b]$ is orientation-reversing — $\sigma'(s) < 0$, $\sigma(c) = b, \sigma(d) = a$ — the substitution gives
> $$\int_c^d \sigma'(s) f(\sigma(s)) ds = \int_b^a f(t) dt = -\int_a^b f(t) dt = -\int_\gamma \omega.$$
> The sign change comes from the substitution's reversal of limits. So $\int_{\tilde\gamma} \omega = -\int_\gamma \omega$ — the integral reverses sign under orientation reversal.

> [!note]- Complete formal solution
> Let $\sigma : [c, d] \to [a, b]$ be a smooth orientation-preserving diffeomorphism ($\sigma'(s) > 0$ for all $s$, $\sigma(c) = a$, $\sigma(d) = b$), and let $\tilde\gamma := \gamma \circ \sigma$.
>
> **Chain rule:** $\tilde\gamma'(s) = \sigma'(s) \cdot \gamma'(\sigma(s))$ for all $s \in [c, d]$.
>
> **Line-integral computation:**
> \begin{align}
> \int_{\tilde\gamma} \omega &= \int_c^d \omega_{\tilde\gamma(s)}(\tilde\gamma'(s)) \, ds \\
> &= \int_c^d \omega_{\gamma(\sigma(s))}(\sigma'(s) \gamma'(\sigma(s))) \, ds \\
> &= \int_c^d \sigma'(s) \omega_{\gamma(\sigma(s))}(\gamma'(\sigma(s))) \, ds \quad [\text{linearity of } \omega] \\
> &= \int_a^b \omega_{\gamma(t)}(\gamma'(t)) \, dt \quad [\text{substitution } t = \sigma(s)] \\
> &= \int_\gamma \omega.
> \end{align}
>
> For an orientation-reversing $\sigma$ ($\sigma'(s) < 0$, $\sigma(c) = b, \sigma(d) = a$), the same computation gives $\int_{\tilde\gamma} \omega = \int_b^a f(t) dt = -\int_a^b f(t) dt = -\int_\gamma \omega$.
>
> So the line integral is invariant under orientation-preserving reparameterization and changes sign under orientation-reversing reparameterization. $\qquad\blacksquare$

---

# Key Takeaways

**The line integral depends on the oriented parametrized curve modulo admissible reparameterization, not merely on its image.** An orientation-preserving diffeomorphism of parameter intervals changes the clock but preserves the traversal, hence preserves the integral. The image set alone is insufficient: a curve may traverse the same arc twice, pause, or retrace part of it, and multiplicity and direction affect the integral.

**The structural reason is the chain rule plus linearity of the pairing.** The chain rule gives $\tilde\gamma' = \sigma' \cdot \gamma' \circ \sigma$; linearity of the pairing $\omega(v)$ in $v$ lets us factor the scalar $\sigma'$ out; the substitution rule converts the inner-integral measure $\sigma'(s) ds$ to $dt$. So the structural pieces of the proof are exactly the chain rule, linearity, and the substitution rule — each of which is a fundamental property of smooth maps and integration. The composite gives the invariance.

**Orientation reversal flips the sign.** This is what makes "line integral around a closed loop" a well-defined number rather than a class — given a closed loop $\gamma$, traversing it in the opposite direction gives the negative. For closed loops on a non-simply-connected manifold, this means the integral of a closed-but-not-exact 1-form (like the angle form on $S^1$) is a topological invariant of the *oriented* loop class.

**This is the simplest instance of naturality of $\omega$.** A smooth map $\sigma : [c, d] \to [a, b]$ pulled back $\omega$ from $M$ (via $\gamma$) gives an integrand on $[c, d]$. The theorem says the integral is preserved. The generalization to arbitrary smooth maps $F : N \to M$ is the **change-of-variables for 1-forms**: $\int_{F \circ \gamma} \omega = \int_\gamma F^*\omega$ — see [[Def - Pullback of a Covector Field]] and [[Thm - Pullback Commutes with d for 1-Forms]] for the broader naturality.
