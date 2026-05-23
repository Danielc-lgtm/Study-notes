---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - Smooth Vector Field"
  - "Def - Lie Derivative of a Vector Field"
tags: [geometry, differential-geometry]
---

# Problem Statement

(a) Let $X \in \mathfrak{X}(M)$ be a smooth vector field on a smooth manifold $M$ and let $f \in C^\infty(M)$. Show that the Lie derivative of $f$ along $X$ is

$$\mathcal{L}_X f = X f,$$

i.e. the action of $X$ on $f$ as a derivation of $C^\infty(M)$. In particular, for any constant function $f \equiv c$,

$$\mathcal{L}_X f = 0.$$

(b) Conclude that $f$ is **constant along the flow of $X$** — i.e. $f(\phi^X_t(p))$ is independent of $t$ for every $p$ — if and only if $X f \equiv 0$.

**Recall:**

![[Def - Lie Derivative of a Vector Field#The Definition]]

The Lie derivative of a smooth function $f$ along $X$ is, by the general definition of Lie derivative, the rate of change of the pullback of $f$ along the flow $\phi^X$:

$$\mathcal{L}_X f \big|_p = \frac{d}{dt}\bigg|_{t=0} (\phi^X_t)^* f \big|_p = \frac{d}{dt}\bigg|_{t=0} f(\phi^X_t(p)).$$

(For functions the "pullback" $(\phi^X_t)^* f := f \circ \phi^X_t$ does not require differentials, only function composition.)

A smooth function is **conserved** or **invariant** under a flow if its values do not change as the flow runs. In physics, conserved quantities of a Hamiltonian flow are exactly the functions Poisson-commuting with the Hamiltonian.

---

# Convergent Strategy

**Problem class:** Identify the Lie derivative of a function with the action of the vector field as a derivation, then use this to characterize flow-invariance. The class is "verify a foundational identity in the Lie derivative calculus".

**Assumption pattern:** A smooth vector field $X$, a smooth function $f$, and the flow $\phi^X$ of $X$ (given by [[Thm - Fundamental Theorem on Flows]]). The integral curve $t \mapsto \phi^X_t(p)$ starts at $p$ with velocity $X_p$, by definition of the flow.

**Theorem routing:** The chain rule for the composition $t \mapsto f(\phi^X_t(p))$. The velocity of $\phi^X_t(p)$ at $t = 0$ is $X_p$ (by definition of the infinitesimal generator). The chain rule gives the Lie derivative.

**Key decision point:** The non-obvious step is realizing that the Lie derivative of a function is just the directional derivative — there is no "transport via differential" complication as there is for vector fields, because functions live in $\mathbb{R}$ at every point and can be compared without identifying tangent spaces. This makes the function case trivial; the substance lies in seeing how it extends to vector fields and tensors via the flow-pullback construction.

---

# Legal Operations Used

1. **Operation 4 from the topic page (differentiate the flow at $t = 0$ to recover the vector field).** $\frac{d}{dt}\big|_{t=0} \phi^X_t(p) = X_p$ — the velocity of the flow at $t = 0$ is the vector field.

2. **Operation 12 from the topic page (use the Lie derivative formula).** $\mathcal{L}_X f = Xf$ is the function-case of the Lie derivative.

---

# Hints

> [!note]- Hint 1
> By the chain rule, $\frac{d}{dt}\big|_{t=0} f(\phi^X_t(p)) = df_p(\phi^X_t(p))'|_{t=0} = df_p(X_p) = X_p f$. So the Lie derivative of $f$ along $X$ is exactly the action of $X_p$ as a derivation on $f$.

> [!note]- Hint 2
> For a constant function $f \equiv c$, $X_p f = X_p(c) = 0$ for every $p$ (since the action of any tangent vector on a constant function is zero). So $\mathcal{L}_X f \equiv 0$.

> [!note]- Hint 3
> For (b): if $f \circ \phi^X_t$ is constant in $t$ (i.e. $f$ is conserved along the flow), then its derivative is zero, hence $\mathcal{L}_X f = 0$. Conversely if $\mathcal{L}_X f = 0$ everywhere, then $\frac{d}{dt} f(\phi^X_t(p)) = \mathcal{L}_X f|_{\phi^X_t(p)} = 0$ for all $t$, so $f \circ \phi^X_t$ is constant.

---

# Solution

The proof has three steps. Step 1 derives $\mathcal{L}_X f = Xf$ from the definition of the Lie derivative for functions. Step 2 observes that constants are annihilated by any tangent vector, so $\mathcal{L}_X (\text{const}) = 0$. Step 3 uses the result to characterize conservation along the flow.

**Step 1: $\mathcal{L}_X f = Xf$.**

By the definition of the Lie derivative of a function,
$$\mathcal{L}_X f \big|_p = \frac{d}{dt}\bigg|_{t=0} f(\phi^X_t(p)).$$
By the chain rule, this equals $df_p(\sigma'(0))$, where $\sigma(t) = \phi^X_t(p)$. By definition of the flow, $\sigma'(0) = X_p$. So $\mathcal{L}_X f|_p = df_p(X_p) = X_p f$, where the last equality is the action of $X_p$ as a derivation on $f$. Since $p$ is arbitrary, $\mathcal{L}_X f = Xf$.

> [!note]- Derivation (Step 1)
> Apply the chain rule to $g(t) := f(\phi^X_t(p))$, a smooth function of $t$:
> $$g'(t) = df_{\phi^X_t(p)}\left(\frac{d}{dt}\phi^X_t(p)\right) = df_{\phi^X_t(p)}(X_{\phi^X_t(p)}) = (Xf)(\phi^X_t(p)),$$
> using the defining property of the flow $\frac{d}{dt} \phi^X_t(p) = X_{\phi^X_t(p)}$ and the action of $X$ as a derivation: $df_q(X_q) = X_q f = (Xf)(q)$.
>
> At $t = 0$: $g'(0) = (Xf)(p) = X_p f$. So $\mathcal{L}_X f|_p = g'(0) = X_p f$, hence $\mathcal{L}_X f = Xf$ as functions on $M$.

**Step 2: Constants are annihilated.**

If $f \equiv c$ is a constant function, then $X_p f = c'(p) = 0$ by the action of $X_p$ on a constant. (Concretely: in any chart, $X_p f = X^i(p) \partial_i c = 0$ since $\partial_i c = 0$.) So $\mathcal{L}_X f = Xf \equiv 0$.

> [!note]- Derivation (Step 2)
> For $f \equiv c$ a constant function: $X_p f = c \cdot X_p(1) = c \cdot 0 = 0$, since $X_p(1) = 0$ (the action of any derivation at a point on the constant $1$ is zero — this follows from $1 \cdot 1 = 1$ and the Leibniz rule: $X_p(1) = X_p(1 \cdot 1) = 2 \cdot 1 \cdot X_p(1)$, hence $X_p(1) = 0$).
>
> So $\mathcal{L}_X f = Xf = 0$.

**Step 3: $f$ conserved along flow ⟺ $Xf = 0$.**

By Step 1, $\mathcal{L}_X f = Xf$. Now $f$ is constant along the flow of $X$ means $\frac{d}{dt} f(\phi^X_t(p)) = 0$ for all $t, p$. By the chain rule (extending Step 1 to general $t$, not just $t = 0$):
$$\frac{d}{dt} f(\phi^X_t(p)) = (Xf)(\phi^X_t(p)).$$
So $\frac{d}{dt} f \circ \phi^X_t \equiv 0$ on the flow domain iff $Xf \equiv 0$ on $M$ (varying $p$, the image of $\phi^X_t$ covers $M$). Hence $f$ is conserved iff $Xf = 0$ iff $\mathcal{L}_X f = 0$.

> [!note]- Derivation (Step 3)
> From Step 1's chain rule (at general $t$, not just $t = 0$):
> $$\frac{d}{dt} f(\phi^X_t(p)) = (Xf)(\phi^X_t(p)).$$
>
> *($\Leftarrow$)* If $Xf \equiv 0$, then for every $(t, p)$ in the flow domain, $(Xf)(\phi^X_t(p)) = 0$, so $f \circ \phi^X_t$ has zero derivative. Hence $f(\phi^X_t(p))$ is constant in $t$ — $f$ is conserved along the flow.
>
> *($\Rightarrow$)* If $f$ is conserved along the flow, $\frac{d}{dt} f(\phi^X_t(p)) = 0$ for all $(t, p)$. In particular at $t = 0$: $(Xf)(p) = 0$. Since $p$ was arbitrary, $Xf \equiv 0$.

> [!note]- Complete formal solution
> **(a) $\mathcal{L}_X f = Xf$.** By definition, $\mathcal{L}_X f|_p = \frac{d}{dt}\big|_{t=0} f(\phi^X_t(p))$. The chain rule gives $\frac{d}{dt} f(\phi^X_t(p)) = df_{\phi^X_t(p)}\big(\frac{d}{dt}\phi^X_t(p)\big) = df_{\phi^X_t(p)}(X_{\phi^X_t(p)}) = (Xf)(\phi^X_t(p))$. At $t = 0$, $\mathcal{L}_X f|_p = (Xf)(p) = X_p f$. Hence $\mathcal{L}_X f = Xf$.
>
> For $f \equiv c$ constant: $X_p f = 0$ since the action of a tangent vector on the constant function is zero. So $\mathcal{L}_X f = 0$.
>
> **(b) Characterization of conservation.** $f$ is constant along the flow of $X$ iff for all $(t, p)$ in the flow domain, $f(\phi^X_t(p))$ is independent of $t$, iff $\frac{d}{dt} f(\phi^X_t(p)) = 0$ for all $(t, p)$. By the chain rule (a) extended to general $t$, this derivative is $(Xf)(\phi^X_t(p))$. So conservation is equivalent to $Xf = 0$ identically on the flow's reachable set; by surjectivity of $\phi^X_t$ for small $t$ (and density of reachable points), this is equivalent to $Xf = 0$ on $M$. Hence $f$ is conserved along the flow iff $\mathcal{L}_X f = 0$. $\qquad\blacksquare$

---

# Key Takeaways

**The Lie derivative of a function is the directional derivative.** For functions, $\mathcal{L}_X f = Xf$ — no flow-pullback subtlety is needed because functions take values in $\mathbb{R}$, the same vector space at every point, so they can be compared directly. This contrasts with the Lie derivative of a vector field, which requires transporting tangent vectors via $d\phi$ before comparison. The trigger pattern: any "Lie derivative of a function" reduces immediately to the action of the vector field as a derivation.

**Constants and conservation laws are dual notions.** A function $f$ is *conserved* (a constant of the motion) along the flow of $X$ if and only if $Xf = 0$, equivalently $\mathcal{L}_X f = 0$. The geometric content: $f$ is "constant in the direction of $X$" — its level sets are invariant under $\phi^X$. The constant-function case is trivial ($f$ is constant globally, hence trivially constant along the flow); the substantive case is where $f$ varies on $M$ but happens to be constant along the flow, in which case $X$ is tangent to the level sets of $f$. This is the geometric source of *first integrals* in mechanics.

**Energy conservation as a Lie derivative statement.** In Hamiltonian mechanics, the Hamiltonian $H : T^*M \to \mathbb{R}$ is conserved along its own flow: $X_H H = 0$, equivalently $\{H, H\} = 0$ (the Poisson bracket vanishes by antisymmetry). This is the differential-geometric content of energy conservation. More generally, any function $f$ with $\{f, H\} = 0$ is a conserved quantity for the Hamiltonian flow, by the same Lie derivative argument. Noether's theorem then identifies conserved quantities with symmetries: $\{f, H\} = 0$ iff the flow of $X_f$ preserves $H$.

**The Lie derivative on functions extends to all tensors.** This exercise is the simplest case of the general principle: the Lie derivative $\mathcal{L}_X$ is defined on every tensor field by pulling back along the flow of $X$ and differentiating at $t = 0$. For functions it reduces to $Xf$; for vector fields it reduces to $[X, Y]$; for differential forms it satisfies **Cartan's magic formula** $\mathcal{L}_X = d \iota_X + \iota_X d$. The function case is the calibration point against which the general theory is built. The fundamental property — $\mathcal{L}_X$ is a derivation of the tensor algebra, commutes with contractions, and reduces to $Xf$ on functions — characterizes it uniquely. See [[Differential Geometry VIII — Differential Forms]] for the form case.
