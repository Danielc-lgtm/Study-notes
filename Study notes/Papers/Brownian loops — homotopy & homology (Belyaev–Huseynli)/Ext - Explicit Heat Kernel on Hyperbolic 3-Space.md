---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, hyperbolic-geometry, heat-kernels]
---

# Signature

| symbol | type |
|---|---|
| $\mathbb{H}^3$ | hyperbolic $3$-space, curvature $\equiv-1$ |
| $p_{\mathbb{H}^3}$ | $(0,\infty)\times\mathbb{H}^3\times\mathbb{H}^3\to(0,\infty)$ — the Brownian transition density |
| $u$ | $=d(z,w)$, the hyperbolic distance |
| $p_{\mathbb{H}^2}$ | the $2$-dimensional kernel, for contrast |

---

# Statement

> **(HK3) Closed form of the $\mathbb{H}^3$ heat kernel.** *Precondition:* **(P1)** the generator is $\Delta_{\mathbb{H}^3}$ (positive Laplacian), Brownian motion normalised as in §2.3.3. *Conclusion:* $p_{\mathbb{H}^3}$ depends on $(z,w)$ only through $u=d(z,w)$, and
> $$p_{\mathbb{H}^3}(t,z,w)=\frac{1}{(4\pi t)^{3/2}}\cdot\frac{u}{\sinh u}\cdot e^{-t-\frac{u^2}{4t}}.\tag{87}$$

> **(F1) The structure that makes §7 work.** Three factors: a Euclidean Gaussian $\frac{e^{-u^2/4t}}{(4\pi t)^{3/2}}$, a curvature factor $\frac{u}{\sinh u}$, and a constant killing $e^{-t}$ (the bottom of the $\mathbb{H}^3$ spectrum is $1=\big(\frac{n-1}{2}\big)^2$ at $n=3$). **The $1/\sinh u$ is cancelled exactly by the Jacobian of the change of variables $r\mapsto u$ in [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab|(P2)]].**
>
> **(F2) Contrast with $\mathbb{H}^2$.** In even dimension there is **no** elementary closed form: $p_{\mathbb{H}^2}(t,u)=\frac{\sqrt2e^{-t/4}}{(4\pi t)^{3/2}}\int_u^\infty\frac{re^{-r^2/4t}}{\sqrt{\cosh r-\cosh u}}\,\mathrm{d}r$ — an integral that does not evaluate. **This is why §3 had to import [[Ext - Wang–Xue Strip Identity|(WX)]] while §7 derives its identity directly.**
>
> **(F3) Odd dimensions generally.** $p_{\mathbb{H}^{2k+1}}$ is elementary for every $k$, by the Millson recursion $p_{\mathbb{H}^{n+2}}=-\frac{e^{-nt}}{2\pi\sinh u}\partial_up_{\mathbb{H}^n}$. Only $n=3$ is used here.

---

# Type card

> [!abstract] Type card — (HK3)
> **Given.** (P1).
>
> **Produces.** The closed form (87): a function of $(t,u)$ built from elementary functions only.
>
> **Lets you.** Evaluate $\int_{F_\tau}p_{\mathbb{H}^3}(t,w,\tau^mw)\,\mathrm{d}\mathrm{vol}$ **by hand**, which is [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity|(88),(89)]] and the technical core of §7.

---

# Status

- **Proved here:** no, quoted as "recall".
- **Source:** classical; Davies, *Heat Kernels and Spectral Theory*; Grigor'yan, *Heat Kernel and Analysis on Manifolds*; Chavel.
- **DAG node that would close this:** 🟢 *Analysis of PDEs / SDEs* (7,10) together with 🔵 *Spectral Geometry*. The formula is elementary to verify once stated. **Not a substantive gap.**
- **What is safe to assume:** (87) and the parity contrast (F2). Nothing beyond $n=3$ is used.
- **Scope:** §7.2, in the derivation of (88).

> [!warning] Normalisation
> (87) carries the factor $e^{-t}$, not $e^{-t/4}$ as in the $\mathbb{H}^2$ kernel — the bottom of the spectrum is $\big(\frac{n-1}{2}\big)^2$, i.e. $1$ in dimension $3$ and $\tfrac14$ in dimension $2$. This is why the Gaussian identity [[Ext - Gaussian Reciprocal Integral Identity|(GI)]] is applied with $a=1$ in §7 and $a=\tfrac14+\kappa$ in §3.

---

# Used at

- [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity]] — the sole consumer
- [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds]] — via (88) and (GI) at $a=1$
- [[Def - Transition Density and Heat Kernel]] — (F4) there, on when a kernel exists
- [[§7 Brownian Loops on Hyperbolic 3-Manifolds]]

---

# Commentary

> [!note]- Commentary (skippable)
> The parity phenomenon (F2)–(F3) is the reason §7 reads more self-contained than §3 despite being the more exotic setting. In odd dimensions the hyperbolic heat kernel is elementary; in even dimensions it is an integral of Millson type that does not close. §3 therefore had to quote Wang–Xue for the strip identity; §7 can do the corresponding computation on one page, and the paper says so explicitly: "In the surface case we relied on the identity of [WX25], but on $\mathbb{H}^3$ we derive the corresponding identity ourselves."
>
> The cancellation in (F1) is the mechanism. The volume element in the slab, after passing to polar coordinates and changing variables from $r$ to $u$, produces a Jacobian proportional to $\sinh u$; the kernel supplies $1/\sinh u$; the product is a bare Gaussian. Nothing analogous is available in dimension $2$, where the kernel's $u$-dependence is not a ratio of elementary functions.
