---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds"
  - "Constr - The Weighted Potential Measure Vϕ"
  - "Def - Kleinian Group and Loxodromic Complex Length"
tags: [paper, probability, hyperbolic-geometry, loop-measures]
---

# Notation

- $X=\Gamma\backslash\mathbb{H}^3$ — a geometrically finite hyperbolic $3$-manifold; $\gamma\in\mathcal{P}_X$ a primitive closed geodesic
- $L_\gamma=\ell_\gamma+i\theta_\gamma$ — the [[Def - Kleinian Group and Loxodromic Complex Length|complex length]]; $m\geq1$ the winding number
- $mL_\gamma=m\ell_\gamma+im\theta_\gamma$ — the complex length of the iterate
- $\mu_X$ — the Brownian loop measure ($\phi(\lambda)=\lambda$, so $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$)

---

# Type card

> [!abstract] Type card — Corollary 7.3 (Brownian mass in a class, 3-manifolds)
> **Given.** A geometrically finite hyperbolic $3$-manifold $X=\Gamma\backslash\mathbb{H}^3$; pure Brownian motion, so $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$ by [[Constr - The Weighted Potential Measure Vϕ|Example 2.10(a)]]; a primitive closed geodesic $\gamma\in\mathcal{P}_X$ with complex length $L_\gamma=\ell_\gamma+i\theta_\gamma$; a winding number $m\geq1$.
>
> **Produces.** The closed-form mass $\mu_X(\mathcal{C}_X(\gamma^m)) = \frac1m\cdot\frac{1}{|e^{mL_\gamma}-1|^2}$ — a positive real number, with two equivalent trigonometric forms.
>
> **Lets you.** See the two-dimensional formula $\frac1m\frac{1}{e^L-1}$ as a specialisation: three dimensions **square** the denominator, and holonomy enters through a **modulus**. The two effects are independent, and separating them is the point of the corollary.

---

# Statement

> **Corollary 7.3 (mass of Brownian loop measure in free homotopy classes on hyperbolic 3-manifolds).** Let $X=\Gamma\backslash\mathbb{H}^3$ be a geometrically finite hyperbolic $3$-manifold, $\gamma\in\mathcal{P}_X$ a primitive closed geodesic with winding number $m\geq1$. The mass of Brownian loop measure in a free homotopy class $\mathcal{C}_X(\gamma^m)$ is
> $$\mu_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac1m\cdot\frac{1}{\big|e^{mL_\gamma}-1\big|^2},\qquad mL_\gamma=m\ell_\gamma+im\theta_\gamma.\tag{91}$$
> Two equivalent forms are
> $$\mu_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac{e^{-m\ell_\gamma}}{2m\big(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma)\big)} = \frac1m\left[\big(e^{m\ell_\gamma}-1\big)^2+4e^{m\ell_\gamma}\sin^2\tfrac{m\theta_\gamma}{2}\right]^{-1}.\tag{92}$$
> When $\theta_\gamma=0$ the holonomy term drops and the denominator becomes $\big(e^{m\ell_\gamma}-1\big)^2$.

---

# Why it is true

One substitution into [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds|Theorem 7.2]], and the same Gaussian identity that discharged every case in §3.1.

With $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$ the integral in (90) becomes $\int_0^\infty s^{-3/2}e^{-s-(m\ell_\gamma)^2/4s}\,\mathrm{d}s$ up to constants, which the identity $\int_0^\infty s^{-3/2}e^{-as-b/s}\,\mathrm{d}s=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$ evaluates with $a=1$ and $b=(m\ell_\gamma)^2/4$. **Note $a=1$, where in two dimensions $a=\tfrac14+\kappa$** — the constant is the bottom of the $L^2$-spectrum of $\Delta_{\mathbb{H}^n}$, which is $(n-1)^2/4$. Everything then cancels: the $e^{m\ell_\gamma}$ against the $e^{-m\ell_\gamma}$ from the exponential, and the $\ell_\gamma$ against the $m\ell_\gamma$ in the denominator, leaving $\frac1m|e^{mL_\gamma}-1|^{-2}$.

**The two effects, separated.** It is worth being precise about what the extra structure does, because it is easy to conflate.

- **The exponent $2$ is dimensional.** Setting $\theta_\gamma=0$ leaves $\frac1m(e^{m\ell_\gamma}-1)^{-2}$, still squared, where the two-dimensional answer is $\frac1m(e^{m\ell_\gamma}-1)^{-1}$. So "three dimensions squares the denominator" is correct, and it has nothing to do with holonomy.
- **The modulus is the holonomy.** The complex length enters as $|e^{mL_\gamma}-1|^2$, and by $|e^{a+ib}-1|^2=2e^a(\cosh a-\cos b)$ the rotation contributes the $-\cos(m\theta_\gamma)$, or equivalently the $+4e^{m\ell_\gamma}\sin^2(m\theta_\gamma/2)$ in the third form. **Holonomy makes the mass smaller**: the denominator is largest when $\cos(m\theta_\gamma)=-1$, so a class whose $m$-fold iterate rotates by $\pi$ carries less loop mass than a pure translation of the same length.

**The mechanism in one line: the $\mathbb{H}^3$ heat kernel's Gaussian integral evaluates to $e^{-m\ell_\gamma}$ against a prefactor $e^{+m\ell_\gamma}$, everything cancels, and what survives is $\frac1m$ times the reciprocal of $|e^{mL_\gamma}-1|^2$ — the modulus carrying the holonomy and the square carrying the dimension.**

---

# Strategy

**Strategy.** Substitute $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$ into Theorem 7.2 and apply the same integral identity $\int_0^\infty s^{-3/2}e^{-as-b/s}\,\mathrm{d}s=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$ that discharged every case in §3.1, now with $a=1$ and $b=(m\ell_\gamma)^2/4$.

> [!note]- Calculation (skippable)
> For pure Brownian motion, $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$ by [[Constr - The Weighted Potential Measure Vϕ|Example 2.10]], and (90) becomes
> $$\mu_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{|e^L-1|^2}\cdot\frac{2}{(4\pi)^{3/2}}\int_0^\infty s^{-3/2}e^{-s-(m\ell_\gamma)^2/4s}\,\mathrm{d}s.$$
> The integral $\int_0^\infty s^{-3/2}e^{-as-b/s}\,\mathrm{d}s=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$, with $a=1$ and $b=(m\ell_\gamma)^2/4$, equals $\sqrt\pi\cdot\frac{2}{m\ell_\gamma}e^{-m\ell_\gamma}$.
>
> Substituting and cancelling — the $e^{m\ell_\gamma}$ against $e^{-m\ell_\gamma}$, and $\ell_\gamma$ against $m\ell_\gamma$ — gives (91).
>
> The equivalent forms (92) follow from $|e^{mL_\gamma}-1|^2 = 2e^{m\ell_\gamma}\big(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma)\big)$ and, using $1-\cos(m\theta_\gamma)=2\sin^2(m\theta_\gamma/2)$, from
> $$\big|e^{mL_\gamma}-1\big|^2 = \big(e^{m\ell_\gamma}-1\big)^2+4e^{m\ell_\gamma}\sin^2\tfrac{m\theta_\gamma}{2}.$$

---

# What this assumes, and where to climb

**Theorem 7.2** — [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds]], hence Theorem 7.1, the slab identity, and Lemma 2.11.

**$V_\phi(\mathrm{d}s)=\mathrm{d}s/s$ for Brownian motion** — [[Constr - The Weighted Potential Measure Vϕ]], Example 2.10(a). Note this is where the $\mathrm{d}t/t$ integral localising at $s=t$ comes in; the Haar measure passes through untouched.

**The Gaussian identity** $\int_0^\infty s^{-3/2}e^{-as-b/s}\,\mathrm{d}s=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$ — anchor material, and the same identity used four times in §3.1. Provable by the substitution $u=\sqrt{as}-\sqrt{b/s}$.

**The complex-length identities** $|e^{a+ib}-1|^2=2e^a(\cosh a-\cos b)$ and $1-\cos\theta=2\sin^2(\theta/2)$ — elementary, and worth checking once so that the three forms in (92) are visibly the same number.

---

# What consumes this

Nothing. This is the terminal result of §7 and of the paper.

**And that fact is the paper's most concrete open question**, so it belongs on this page. The mass here is $\frac1m|e^{mL_\gamma}-1|^{-2}$, and [[Thm - Selberg Zeta Criterion|Lemma 4.2]] requires the shape
$$\frac{C}{m}\cdot\frac{e^{(1-s)L}}{e^L-1}$$
for constants $C>0$ and $s>\delta$ independent of $L$. The three-dimensional answer is not of that shape — the denominator is squared and the numerator has no $e^{(1-s)L}$ factor to match. **So the Selberg criterion does not apply as stated, and §7 has no zeta identity, no finiteness criterion, and no probability measure on the free homotopy classes of a hyperbolic $3$-manifold.**

The natural object is presumably a Selberg zeta function for $\Gamma\subset\mathrm{PSL}(2,\mathbb{C})$ built from **complex** lengths — such functions exist in the literature for Kleinian groups — and the natural question is which functional equation replaces (33) so that the criterion goes through. Answering it would carry §4, §5 and §6 into three dimensions in one step, since everything in those sections runs on the criterion rather than on the geometry.

---

# Reading it against the rest of the paper

The corollary is the paper's closing formula, and reading it against the opening one is the efficient summary of §7:
$$\text{2D: }\ \mu_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac1m\cdot\frac{1}{e^{m\ell_\gamma}-1},\qquad\qquad \text{3D: }\ \mu_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac1m\cdot\frac{1}{\big|e^{mL_\gamma}-1\big|^2}.$$
The $\frac1m$ persists — it comes from the coset enumeration over the *primitive* centraliser, which is dimension-independent. The $e^{L}-1$ persists in form, with the real length replaced by the complex one. What changes is the exponent, and that is the whole of what dimension does to this formula.

Whether the squared denominator is a coincidence of dimension $3$ or the $n=3$ case of a pattern — one might guess $|e^{L}-1|^{n-1}$, matching the $(n-1)^2/4$ spectral constant — the paper does not say, and the computation on [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity]] would have to be redone on $\mathbb{H}^n$ to find out. That is a well-posed and apparently short question the note-set flags as worth asking.
