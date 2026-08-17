---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Ext - Explicit Heat Kernel on Hyperbolic 3-Space"
  - "Constr - Loxodromic Standard Form and the H3 Fundamental Slab"
tags: [paper, hyperbolic-geometry, heat-kernels]
---

# Signature

| symbol | type |
|---|---|
| $\tau$ | standard-form loxodromic, $\tau^m(z,y)=(e^{mL_\gamma}z,e^{m\ell_\gamma}y)$ |
| $L$ | $:=mL_\gamma=m\ell_\gamma+im\theta_\gamma\in\mathbb{C}$ |
| $F_\tau$ | the slab $\{1\leq y<e^{\ell_\gamma}\}$ |
| $u$ | $=d(w,\tau^mw)$; ranges over $[m\ell_\gamma,\infty)$ as $r=\lvert z\rvert$ runs over $[0,\infty)$ |
| $\lvert e^{L}-1\rvert^2$ | $=1-2e^{m\ell_\gamma}\cos(m\theta_\gamma)+e^{2m\ell_\gamma}=2e^{m\ell_\gamma}\big(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma)\big)$ |

---

# Type card

> [!abstract] Type card — (88),(89)
> **Given.**
> **(H1)** $\tau$ in standard form (82), $m\geq1$, $L=mL_\gamma$.
> **(H2)** $p_{\mathbb{H}^3}(t,u)=\frac{1}{(4\pi t)^{3/2}}\frac{u}{\sinh u}e^{-t-u^2/4t}$ — [[Ext - Explicit Heat Kernel on Hyperbolic 3-Space|(HK3)]].
> **(H3)** the displacement formula and slab geometry — [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab|(P2),(P3),(P4)]].
>
> **Produces.** The closed-form slab integral
> $$\int_{F_\tau}p_{\mathbb{H}^3}\big(t,w,\tau^mw\big)\,\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}(w)=\frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{\lvert e^{L}-1\rvert^2}\cdot\frac{2t\,e^{-t}}{(4\pi t)^{3/2}}\,e^{-(m\ell_\gamma)^2/4t},\tag{88}$$
> equivalently
> $$=\frac{\ell_\gamma}{2\big(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma)\big)}\cdot\frac{e^{-t-(m\ell_\gamma)^2/4t}}{\sqrt{4\pi t}}.\tag{89}$$
>
> **Lets you.** Replace the entire spatial integral of [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds|(85)]] by an elementary function of $t$. **This is the $3$-dimensional analogue of [[Ext - Wang–Xue Strip Identity|(WX)]], and unlike (WX) it is proved here.**

---

# Statement

> **(88),(89).** Assume (H1)–(H3). Then the two displayed identities hold for every $t>0$.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab\|(P2)]] | $w=(z,y)$ | $\cosh u=\cosh(m\ell_\gamma)+\frac{\lvert e^{L}-1\rvert^2r^2}{2e^{m\ell_\gamma}y^2}$, $r=\lvert z\rvert$ |
| [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab\|(P3)]] | polar coordinates $z=re^{i\varphi}$ | angular integral $=2\pi$; $\mathrm{d}A(z)=r\,\mathrm{d}r\,\mathrm{d}\varphi$ |
| differentiating (P2) in $r$ | $\sinh u\,\mathrm{d}u=\frac{\lvert e^{L}-1\rvert^2r}{e^{m\ell_\gamma}y^2}\,\mathrm{d}r$ | $r\,\mathrm{d}r=\frac{e^{m\ell_\gamma}y^2}{\lvert e^{L}-1\rvert^2}\sinh u\,\mathrm{d}u$; $r:0\to\infty\iff u:m\ell_\gamma\to\infty$ |
| [[Ext - Explicit Heat Kernel on Hyperbolic 3-Space\|(HK3)]] | the $\sinh u$ from the Jacobian | cancels $\frac{1}{\sinh u}$; leaves $\frac{u\,e^{-t-u^2/4t}}{(4\pi t)^{3/2}}$ |
| $\int_{m\ell_\gamma}^\infty u\,e^{-u^2/4t}\,\mathrm{d}u=2t\,e^{-(m\ell_\gamma)^2/4t}$ | the $u$-integral | the factor $2te^{-(m\ell_\gamma)^2/4t}$ |
| [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab\|(P4)]] | $y^2\cdot y^{-3}$, $\int_1^{e^{\ell_\gamma}}\frac{\mathrm{d}y}{y}$ | the factor $\ell_\gamma$ |
| $\lvert e^{a+ib}-1\rvert^2=2e^a(\cosh a-\cos b)$ and $\frac{2\pi\cdot2t}{(4\pi t)^{3/2}}=\frac{1}{\sqrt{4\pi t}}$ | (88) | (89) |

---

# Proof

**Strategy.** Polar coordinates in $z$, then change variables $r\mapsto u$. The Jacobian's $\sinh u$ cancels the kernel's $1/\sinh u$ exactly, leaving a bare Gaussian in $u$ that integrates elementarily; the $y$-integral over the slab contributes $\ell_\gamma$.

> [!note]- Proof (skippable)
> With $\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}=y^{-3}\,\mathrm{d}A(z)\,\mathrm{d}y$ and $u$ depending on $z$ only through $r=\lvert z\rvert$ by (P3),
> $$\int_{F_\tau}p_{\mathbb{H}^3}(t,w,\tau^mw)\,\mathrm{d}\mathrm{vol}=2\pi\int_1^{e^{\ell_\gamma}}\!\!\int_0^\infty p_{\mathbb{H}^3}(t,u)\,\frac{r\,\mathrm{d}r\,\mathrm{d}y}{y^3}.$$
> Fix $y$ and change variables from $r$ to $u$. Differentiating (P2), $\sinh u\,\mathrm{d}u=\frac{\lvert e^{L}-1\rvert^2r}{e^{m\ell_\gamma}y^2}\,\mathrm{d}r$, so $r\,\mathrm{d}r=\frac{e^{m\ell_\gamma}y^2}{\lvert e^{L}-1\rvert^2}\sinh u\,\mathrm{d}u$, and $r:0\to\infty$ corresponds to $u:m\ell_\gamma\to\infty$. The $\sinh u$ cancels the $1/\sinh u$ in (87), so
> $$\int_0^\infty p_{\mathbb{H}^3}(t,u)\,r\,\mathrm{d}r=\frac{e^{m\ell_\gamma}y^2}{\lvert e^{L}-1\rvert^2}\cdot\frac{e^{-t}}{(4\pi t)^{3/2}}\int_{m\ell_\gamma}^\infty u\,e^{-u^2/4t}\,\mathrm{d}u=\frac{e^{m\ell_\gamma}y^2}{\lvert e^{L}-1\rvert^2}\cdot\frac{2t\,e^{-t}}{(4\pi t)^{3/2}}e^{-(m\ell_\gamma)^2/4t}.$$
> The $y^2$ meets the $y^{-3}$ of the volume element and $\int_1^{e^{\ell_\gamma}}y^{-1}\,\mathrm{d}y=\ell_\gamma$, giving (88). Using $\lvert e^{a+ib}-1\rvert^2=2e^a(\cosh a-\cos b)$ with $a=m\ell_\gamma$, $b=m\theta_\gamma$, and $\frac{2\pi\cdot2t}{(4\pi t)^{3/2}}=\frac{1}{\sqrt{4\pi t}}$, this is (89). $\;\square$

---

# What this assumes, and where to climb

- **(HK3)** — [[Ext - Explicit Heat Kernel on Hyperbolic 3-Space]]. The **only** import, and an elementary one. Contrast §3, which had to quote Wang–Xue for the corresponding $\mathbb{H}^2$ statement because no closed-form kernel exists there.
- **The standard form** — [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab]]. Conjugation-invariance of everything in sight is what makes normalising $\tau$ free of cost.
- **Convergence of the $r$-integral** — automatic: the integrand is a Gaussian in $u$ after the substitution.
- **Not assumed:** anything about $\Gamma$ beyond containing $\tau$. (88) is a computation about a **single** loxodromic isometry of $\mathbb{H}^3$; the group enters only via Theorem 7.1.

---

# Consumed by

- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds]] — (88) evaluates the inner integral of (86)
- [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds]]
- [[§7 Brownian Loops on Hyperbolic 3-Manifolds]] §7.2

---

# Commentary

> [!note]- Commentary (skippable)
> **The mechanism in one line: the volume element's Jacobian under $r\mapsto u$ produces exactly the $\sinh u$ that the $\mathbb{H}^3$ heat kernel divides by, so the slab integral collapses to $\int_{m\ell_\gamma}^\infty ue^{-u^2/4t}\,\mathrm{d}u$, which is elementary.**
>
> Compare the factorisation with the surface case. There, (WX) produced $\frac{\ell_\gamma}{2\sinh(L/2)}$ times an analytic factor; here one gets $\frac{\ell_\gamma}{2(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma))}$ times $\frac{e^{-t-(m\ell_\gamma)^2/4t}}{\sqrt{4\pi t}}$. The structure is identical — a purely geometric prefactor, and a $t$-dependent Gaussian factor — but the geometric prefactor is now *complex-length dependent*, and $2\sinh(L/2)$ has become $\lvert e^{L}-1\rvert^2/e^{m\ell_\gamma}$, a **squared modulus** rather than a first power. That square is where dimension $3$ shows up in the final answer.
>
> Note also what does **not** change: the Gaussian factor still has $b=(m\ell_\gamma)^2/4$, exactly as in §3, so the same identity [[Ext - Gaussian Reciprocal Integral Identity|(GI)]] evaluates the subsequent $s$-integral. Only $a$ moves — from $\tfrac14+\kappa$ to $1+\kappa$ — because the bottom of the $\mathbb{H}^n$ spectrum is $\big(\frac{n-1}{2}\big)^2$.
