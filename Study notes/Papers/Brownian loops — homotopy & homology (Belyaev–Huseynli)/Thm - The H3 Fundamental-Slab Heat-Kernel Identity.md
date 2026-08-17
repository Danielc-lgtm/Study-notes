---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - Loxodromic Standard Form and the H3 Fundamental Slab"
  - "Thm - The Wang–Xue Fundamental-Strip Identity"
tags: [paper, hyperbolic-geometry, heat-kernels]
---

# Notation

- $p_{\mathbb{H}^3}(t,z,w)=\dfrac{1}{(4\pi t)^{3/2}}\dfrac{u}{\sinh u}e^{-t-u^2/4t}$ with $u=d(z,w)$ — the Brownian heat kernel on $\mathbb{H}^3$
- $\tau : (z,y)\mapsto(e^{L_\gamma}z,e^{\ell_\gamma}y)$ — the [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab|loxodromic standard form]]; $\tau^m(z,y)=(e^Lz,e^{m\ell_\gamma}y)$
- $L=mL_\gamma=m\ell_\gamma+im\theta_\gamma$ — the complex length of the iterate
- $F_\tau=\{(z,y) : 1\leq y<e^{\ell_\gamma}\}$ — the fundamental slab; $\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}=y^{-3}\,\mathrm{d}A(z)\,\mathrm{d}y$
- $w=(z,y)$ — a point of $\mathbb{H}^3$; $z=re^{i\varphi}$ in polar coordinates on $\mathbb{C}$
- $u=d(w,\tau^mw)$ — the displacement

---

# Type card

> [!abstract] Type card — equations (88)–(89), the $\mathbb{H}^3$ slab identity
> **Given.** The explicit Brownian heat kernel on $\mathbb{H}^3$, $p_{\mathbb{H}^3}(t,z,w)=(4\pi t)^{-3/2}\frac{u}{\sinh u}e^{-t-u^2/4t}$ with $u=d(z,w)$; $\tau$ in [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab|loxodromic standard form]]; $t>0$, $m\geq1$; $L=mL_\gamma$.
>
> **Produces.** A closed form for the spatial integral over the fundamental slab — a positive real number, factorising as a purely geometric prefactor times a purely analytic factor in $(t,m\ell_\gamma)$.
>
> **Lets you.** Play the role [[Thm - The Wang–Xue Fundamental-Strip Identity|Lemma 3.4]] plays in §3. **This is the one genuinely new computation of §7**, because Wang–Xue's identity is two-dimensional and no citation is available here.

---

# Statement

> **Equations (88)–(89).** For $t>0$ and $m\geq1$, with $\tau$ in standard form and $L=mL_\gamma$,
> $$\int_{F_\tau}p_{\mathbb{H}^3}\big(t,w,\tau^m w\big)\,\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}(w) = \frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{\big|e^{L}-1\big|^2}\cdot\frac{2te^{-t}}{(4\pi t)^{3/2}}\,e^{-(m\ell_\gamma)^2/4t}.\tag{88}$$
> Using $|e^{a+ib}-1|^2=2e^a(\cosh a-\cos b)$ and $2\pi\cdot\frac{2t}{(4\pi t)^{3/2}}=\frac{1}{\sqrt{4\pi t}}$, this is equivalently
> $$\int_{F_\tau}p_{\mathbb{H}^3}\big(t,w,\tau^m w\big)\,\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}(w) = \frac{\ell_\gamma}{2\big(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma)\big)}\cdot\frac{e^{-t-(m\ell_\gamma)^2/4t}}{\sqrt{4\pi t}}.\tag{89}$$

---

# Why it is true

Three simplifications, and each is forced by the standard form.

**The angular integral is free.** In the standard form the displacement $u=d(w,\tau^mw)$ depends on $z$ only through $|z|$ — explicitly,
$$\cosh u = 1+\frac{|z-e^Lz|^2+(y-e^{m\ell_\gamma}y)^2}{2e^{m\ell_\gamma}y^2} = \cosh(m\ell_\gamma)+\frac{|e^L-1|^2|z|^2}{2e^{m\ell_\gamma}y^2}.$$
So in polar coordinates $z=re^{i\varphi}$ the integrand is independent of $\varphi$ and the angular integral contributes a bare $2\pi$. **This is a consequence of the axis being vertical, and it is what makes the three-dimensional computation as tractable as the two-dimensional one.**

**The $1/\sinh u$ cancels.** This is the trick. Changing variables from the radius $r$ to the displacement $u$ at fixed height, differentiating the $\cosh u$ formula gives $\sinh u\,\mathrm{d}u = \frac{|e^L-1|^2 r}{e^{m\ell_\gamma}y^2}\,\mathrm{d}r$, so
$$r\,\mathrm{d}r = \frac{e^{m\ell_\gamma}y^2}{|e^L-1|^2}\sinh u\,\mathrm{d}u,$$
and the $\sinh u$ produced by the substitution **cancels exactly the $1/\sinh u$ carried by the hyperbolic heat kernel.** What is left is an elementary Gaussian in $u$ over $[m\ell_\gamma,\infty)$ — the lower limit because $r=0$ corresponds to a point on the axis, where the displacement is the translation length.

**The heights work out.** The $y^2$ produced by the substitution meets the $y^{-3}$ of the volume element, leaving $y^{-1}$, and $\int_1^{e^{\ell_\gamma}}y^{-1}\,\mathrm{d}y=\ell_\gamma$ — the "height" of the slab in the $\log y$ coordinate, which is exactly the prefactor.

**The mechanism in one line: in standard form the displacement depends only on the radius, so the angular integral is free; the change of variables from radius to displacement produces a $\sinh u$ that cancels the kernel's $1/\sinh u$; and the slab's height integrates to $\ell_\gamma$.**

**Where the holonomy goes.** $\theta_\gamma$ enters only through $|e^L-1|^2=|e^{m\ell_\gamma+im\theta_\gamma}-1|^2$, that is only in the **geometric prefactor**. The analytic factor $e^{-t-(m\ell_\gamma)^2/4t}/\sqrt{4\pi t}$ involves only the real part $m\ell_\gamma$. That separation is why the subordination machinery of §2 goes through unchanged in §7: $V_\phi$ only ever meets the analytic factor.

**Compare with §3's identity.** Lemma 3.4 gave $\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-t/4}e^{-L^2/4t}}{2\sqrt{\pi t}}$; here the prefactor is $\frac{\ell_\gamma}{2(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma))}$ and the analytic factor is $\frac{e^{-t-(m\ell_\gamma)^2/4t}}{\sqrt{4\pi t}}$. **Both changed** — the $e^{-t/4}$ became $e^{-t}$ (a different bottom-of-spectrum constant in three dimensions), the $\sqrt{\pi t}$ normalisation changed, and $\sinh(L/2)$ became $\cosh(m\ell_\gamma)-\cos(m\theta_\gamma)$. What did **not** change is the *structure*: geometric prefactor times analytic factor. That structural persistence is what makes §7 short.

---

# Strategy

**Strategy.** Compute $\cosh u$ for $u=d(w,\tau^mw)$ in the upper half-space model; use polar coordinates in $z$ so the angular integral contributes $2\pi$; then change variables from the radius $r$ to $u$, at which point the $\sinh u\,\mathrm{d}u$ produced by the substitution **cancels the $1/\sinh u$ in the kernel** — that cancellation is the whole trick — leaving an elementary Gaussian integral in $u$ over $[m\ell_\gamma,\infty)$.

> [!note]- Calculation (skippable)
> Work in the upper half-space model $\mathbb{H}^3=\{(z,y) : z\in\mathbb{C},\ y>0\}$ with $\tau$ in the standard form (82), so $\tau^m(z,y)=(e^Lz,e^{m\ell_\gamma}y)$. For $w=(z,y)$, the distance $u=d(w,\tau^mw)$ satisfies
> $$\cosh u = 1+\frac{|z-e^Lz|^2+(y-e^{m\ell_\gamma}y)^2}{2e^{m\ell_\gamma}y^2} = \cosh(m\ell_\gamma)+\frac{|e^L-1|^2|z|^2}{2e^{m\ell_\gamma}y^2},$$
> using $|e^L-1|^2=1-2e^{m\ell_\gamma}\cos(m\theta_\gamma)+e^{2m\ell_\gamma}$ and $1+\frac{(1-e^{m\ell_\gamma})^2}{2e^{m\ell_\gamma}}=\cosh(m\ell_\gamma)$.
>
> The fundamental region $F_\tau=\{(z,y) : 1\leq y<e^{\ell_\gamma}\}$ ranges over all $z\in\mathbb{C}$, and the volume element is $\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}=y^{-3}\,\mathrm{d}A(z)\,\mathrm{d}y$ with $\mathrm{d}A$ Euclidean area on $\mathbb{C}$. In polar coordinates $z=re^{i\varphi}$, $\mathrm{d}A(z)=r\,\mathrm{d}r\,\mathrm{d}\varphi$, and since $u$ depends on $z$ only through $r$ the angular integral contributes $2\pi$:
> $$\int_{F_\tau}p_{\mathbb{H}^3}(t,w,\tau^mw)\,\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}(w) = 2\pi\int_1^{e^{\ell_\gamma}}\int_0^\infty p_{\mathbb{H}^3}(t,u)\,\frac{r\,\mathrm{d}r\,\mathrm{d}y}{y^3},\qquad \cosh u=\cosh(m\ell_\gamma)+\frac{|e^L-1|^2r^2}{2e^{m\ell_\gamma}y^2}.$$
>
> For fixed $y$, change variables from $r$ to $u$. Differentiating, $\sinh u\,\mathrm{d}u=\frac{|e^L-1|^2 r}{e^{m\ell_\gamma}y^2}\,\mathrm{d}r$, so
> $$r\,\mathrm{d}r = \frac{e^{m\ell_\gamma}y^2}{|e^L-1|^2}\,\sinh u\,\mathrm{d}u,$$
> and as $r$ runs from $0$ to $\infty$, $u$ runs from $m\ell_\gamma$ to $\infty$. **The factor $\sinh u$ cancels the $1/\sinh u$ in the kernel**, and the inner integral becomes
> $$\int_0^\infty p_{\mathbb{H}^3}(t,u)\,r\,\mathrm{d}r = \frac{e^{m\ell_\gamma}y^2}{|e^L-1|^2}\cdot\frac{2te^{-t}}{(4\pi t)^{3/2}}\,e^{-(m\ell_\gamma)^2/4t},$$
> the remaining $u$-integral being $\int_{m\ell_\gamma}^\infty u\,e^{-u^2/4t}\,\mathrm{d}u = 2t\,e^{-(m\ell_\gamma)^2/4t}$.
>
> The $y^2$ meets the $y^{-3}$ of the volume element, and $\int_1^{e^{\ell_\gamma}}y^{-1}\,\mathrm{d}y=\ell_\gamma$, giving (88). Using $|e^{a+ib}-1|^2=2e^a(\cosh a-\cos b)$ and $2\pi\cdot\frac{2t}{(4\pi t)^{3/2}}=\frac{1}{\sqrt{4\pi t}}$ gives the equivalent form (89).

---

# What this assumes, and where to climb

**The explicit $\mathbb{H}^3$ heat kernel** $p_{\mathbb{H}^3}(t,z,w)=(4\pi t)^{-3/2}\frac{u}{\sinh u}e^{-t-u^2/4t}$. This is the load-bearing input and it is quoted; it is standard, and the $\frac{u}{\sinh u}$ factor is what makes the cancellation possible. **Note the $e^{-t}$**, where the two-dimensional kernel has $e^{-t/4}$: the constant is $(n-1)^2/4$ for $\mathbb{H}^n$, giving $\tfrac14$ in dimension $2$ and $1$ in dimension $3$. It is the bottom of the $L^2$-spectrum of $\Delta_{\mathbb{H}^n}$, and it is the source of every $\tfrac14$ in §3–§6 and of the $e^{-s}$ in §7.

**The standard form and the slab** — [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab]]. The identity is stated for $\tau^m(z,y)=(e^Lz,e^{m\ell_\gamma}y)$ literally, so it presupposes the $\mathrm{PSL}(2,\mathbb{C})$-conjugation putting the axis vertical. Without it, $u$ would not depend on $z$ only through $|z|$, the angular integral would not be free, and the computation would not close.

**Brownian motion specifically.** As with Lemma 3.4, this is where §7 narrows from Dirichlet-form generality down to subordinate Brownian motion: the subordination formula writes $p^\phi_{\mathbb{H}^3}$ as an average of $p_{\mathbb{H}^3}(s,\cdot,\cdot)$, and it is the inner Brownian kernel that this identity evaluates.

**The distance formula in the upper half-space model**, $\cosh d(w,w')=1+\frac{|z-z'|^2+(y-y')^2}{2yy'}$ — anchor material via [[Def - The Hyperbolic Space H^n]].

---

# What consumes this

- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds|Theorem 7.2]] — the sole consumer, discharging the inner spatial integral of (86), after which [[Thm - Collapsing the Time Integral into the Weighted Potential Measure|Lemma 2.11]] does the rest
- [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds|Corollary 7.3]] — through Theorem 7.2
- [[§7 Brownian Loops on Hyperbolic 3-Manifolds]]

---

# Reading it against the rest of the paper

**This is one of the three proofs worth reading in full**, and the reason is that it is the paper's only original computation and it is short. It is also the honest model for what [[Thm - The Wang–Xue Fundamental-Strip Identity|Lemma 3.4]]'s proof looks like — that one is cited to Wang–Xue and not reproduced, and the structural points transfer: the angular direction integrates out, the change of variables to the displacement cancels the $1/\sinh$, the slab height gives the prefactor, and a Gaussian remains.

The asymmetry between §3 and §7 comes down to this one identity. §3 had a citation and §7 did not, so §3's corresponding step is one line and §7's is a page — and everything else in the two sections is the same argument. **If you want to know what work a "the extension is routine" claim is hiding, this is where it is.**
