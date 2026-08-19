---
type: example
subject: probability-geometry
prereqs:
  - "Def - Bernstein Function, Subordinator, and Subordination"
  - "Def - Dirichlet Form and its Operator and Semigroup"
  - "Def - Hyperbolic Plane"
tags: [paper, brownian-loops, dirichlet-forms, levy-processes]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Example 2.7"
---

# Notation

$\mathbb{H}^2$ the hyperbolic plane; $\rho$ its area measure; $\Delta_{\mathbb{H}^2}$ its positive Laplace–Beltrami operator; $p_{\mathbb{H}^2}(s,z,w)$ the hyperbolic heat kernel. $\alpha\in(0,2)$ the stability parameter; $\phi(\lambda)=\lambda^{\alpha/2}$ the Bernstein function; $\Delta^{\alpha/2}_{\mathbb{H}^2}:=\phi(\Delta_{\mathbb{H}^2})$ the fractional Laplacian (spectral calculus). $\eta^\alpha_t(s)$ the $\alpha/2$-stable subordinator density: $\eta^\alpha_t(s)=t^{-2/\alpha}g_{\alpha/2}(s\,t^{-2/\alpha})$, where $g_{\alpha/2}$ is the standard $\alpha/2$-stable density on $(0,\infty)$.

> [!recall]- Fractional Laplacian $\Delta_X^{\alpha/2}$ (spectral calculus)
> **Formally:** for a non-negative self-adjoint operator $A$ on $L^2$ with spectral resolution $A=\int_0^\infty\lambda\,dE_A(\lambda)$, and a measurable $\phi:[0,\infty)\to\mathbb{R}$, the operator $\phi(A):=\int_0^\infty\phi(\lambda)\,dE_A(\lambda)$ is defined on the domain $\{f\in L^2:\int|\phi(\lambda)|^2\,d\langle E_A(\lambda)f,f\rangle<\infty\}$. The **fractional Laplacian** on $X$ (of order $\alpha/2$) is $\Delta_X^{\alpha/2}:=\phi(\Delta_X)$ with $\phi(\lambda)=\lambda^{\alpha/2}$; it is non-negative self-adjoint, with semigroup $e^{-t\Delta_X^{\alpha/2}}$.
> **In words:** apply the *function* $\lambda\mapsto\lambda^{\alpha/2}$ to the Laplacian $\Delta_X$ using the spectral theorem — literally the $\alpha/2$-th power of the operator. It is not a local differential operator (it depends on all of $f$, not just $f$ and its derivatives at a point), so its generator is *non-local*: the associated process has jumps.
> **Concretely:** on $\mathbb{R}^n$, $\Delta_{\mathbb{R}^n}^{\alpha/2}f(x)=\mathcal F^{-1}(|\xi|^\alpha\hat f(\xi))(x)$ via the Fourier transform, and can also be written as the principal-value singular integral $\Delta_{\mathbb{R}^n}^{\alpha/2}f(x)=c_{n,\alpha}\,\mathrm{p.v.}\int_{\mathbb{R}^n}\frac{f(x)-f(y)}{|x-y|^{n+\alpha}}\,dy$ — a weighted average of *differences* $f(x)-f(y)$ over all $y\ne x$, weighted by $|x-y|^{-n-\alpha}$. So the value of $\Delta^{\alpha/2}f$ at $x$ genuinely depends on $f$ far from $x$; that non-locality is what makes the associated process a jump process. The boundary $\alpha=2$ recovers the ordinary Laplacian.

> [!recall]- Bernstein function $\phi(\lambda)=\lambda^{\alpha/2}$ and its subordinator ($\alpha/2$-stable, density $\eta^\alpha_t$)
> **Formally:** for $\alpha\in(0,2)$ (so $\alpha/2\in(0,1)$), $\phi(\lambda)=\lambda^{\alpha/2}$ is Bernstein; its Lévy–Khintchine data is $(a,b,\nu)=(0,0,\nu_\alpha)$ with $\nu_\alpha(ds)=\frac{\alpha/2}{\Gamma(1-\alpha/2)}s^{-1-\alpha/2}\,ds$. The subordinator law has density $\eta^\alpha_t(s)=t^{-2/\alpha}g_{\alpha/2}(s\,t^{-2/\alpha})$ on $(0,\infty)$, where $g_{\alpha/2}(u)$ is the standard (Zolotarev) $\alpha/2$-stable density.
> **In words:** the $\alpha/2$-stable subordinator is a heavy-tailed random clock. It has no drift (it advances only by jumps), no killing, and jumps by amount $s$ at Poisson intensity $\propto s^{-1-\alpha/2}\,ds$: many small jumps, occasional large ones. The scaling $S_t\overset{d}{=}t^{2/\alpha}S_1$ is why the density factors as $t^{-2/\alpha}g_{\alpha/2}(s\,t^{-2/\alpha})$.
> **Concretely:** at $\alpha=1$ this is the $1/2$-stable (Lévy) subordinator, whose density is the closed-form $\eta^1_t(s)=\frac{t}{2\sqrt\pi}s^{-3/2}e^{-t^2/(4s)}$; subordinating planar Brownian motion by it gives the Cauchy process on $\mathbb{R}^2$. See [[Def - Bernstein Function, Subordinator, and Subordination]] and [[Ex - The Four Bernstein Functions of the Paper]] (case 3).

> [!recall]- The hyperbolic plane $\mathbb{H}^2$ and its heat kernel $p_{\mathbb{H}^2}(t,z,w)$
> **Formally:** $\mathbb{H}^2$ is the upper half-plane with metric $ds^2=(dx^2+dy^2)/y^2$; the hyperbolic heat kernel $p_{\mathbb{H}^2}(t,z,w)$ is the integral kernel of $e^{-t\Delta_{\mathbb{H}^2}}$ with respect to $\rho=dx\,dy/y^2$. It is $\mathrm{PSL}(2,\mathbb{R})$-invariant: $p_{\mathbb{H}^2}(t,hz,hw)=p_{\mathbb{H}^2}(t,z,w)$ for every isometry $h$.
> **In words:** the probability density (times area) that a random walker on the hyperbolic plane starting at $z$ is at $w$ after time $t$. Because the plane is homogeneous under Möbius transformations, this kernel depends only on the hyperbolic distance from $z$ to $w$, not on their absolute positions.
> **Concretely:** the closed form is $p_{\mathbb{H}^2}(t,z,w)=\frac{\sqrt 2\,e^{-t/4}}{(4\pi t)^{3/2}}\int_{d(z,w)}^\infty\frac{r\,e^{-r^2/(4t)}}{\sqrt{\cosh r-\cosh d(z,w)}}\,dr$ where $d(z,w)$ is the hyperbolic distance — an explicit but somewhat opaque formula. The key facts the paper uses are that it is $\mathrm{PSL}(2,\mathbb{R})$-invariant and that its short-time on-diagonal behaviour is $p_{\mathbb{H}^2}(t,z,z)\sim 1/(4\pi t)$ (local flatness). See [[Def - Hyperbolic Plane]].

---

# Statement

> **Example (Belyaev–Huseynli 2.7).** For $\phi(\lambda)=\lambda^{\alpha/2}$ with $\alpha\in(0,2)$, the subordinate Dirichlet form's operator on $L^2(\mathbb{H}^2,\rho)$ is the **fractional Laplacian**
> $$\phi(\Delta_{\mathbb{H}^2}) \;=\; \Delta_{\mathbb{H}^2}^{\alpha/2},$$
> and its transition density is
> $$p^\alpha_{\mathbb{H}^2}(t,z,w) \;=\; \int_0^\infty p_{\mathbb{H}^2}(s,z,w)\,\eta^\alpha_t(s)\,ds,$$
> where $\eta^\alpha_t$ is the $\alpha/2$-stable subordinator density. The subordinate process is **pure-jump** (càdlàg with countably many jumps) for every $\alpha\in(0,2)$; the boundary case $\alpha=2$ recovers Brownian motion.

---

# Computation

**The operator via spectral calculus.** The subordinate generator is $-\phi(A)$ where $\phi(\lambda)=\lambda^{\alpha/2}$ and $A=\Delta_{\mathbb{H}^2}$ (spectrum in $[0,\infty)$). The spectral theorem defines $\phi(A):=\int_0^\infty\lambda^{\alpha/2}\,dE_A(\lambda)$; this is by definition the **fractional Laplacian of order $\alpha/2$**. The paper writes this simply as $\Delta_{\mathbb{H}^2}^{\alpha/2}$; unpacking with the abstract Lévy–Khintchine formula (data $(a,b,\nu)=(0,0,\nu_\alpha)$),
$$\phi(A) \;=\; 0\cdot I + 0\cdot A + \int_0^\infty (I-e^{-sA})\,\nu_\alpha(ds) \;=\; \int_0^\infty (I-e^{-s\Delta_{\mathbb{H}^2}})\,\frac{\alpha/2}{\Gamma(1-\alpha/2)}\,s^{-1-\alpha/2}\,ds,$$
which is Bochner's integral representation of the fractional power. So $\Delta_{\mathbb{H}^2}^{\alpha/2}$ acts on a function $f$ by "the weighted average, over all $s>0$, of $f$ minus its heat-flow at time $s$."

**The kernel via subordination.** The subordinate transition density is
$$p^\phi(t,z,w) \;=\; \int_{[0,\infty)} p^E(s,z,w)\,\psi^\phi_t(ds).$$
With $\psi^\phi_t(ds)=\eta^\alpha_t(s)\,ds$ (from case 3) and $p^E=p_{\mathbb{H}^2}$,
$$p^\alpha_{\mathbb{H}^2}(t,z,w) \;=\; \int_0^\infty p_{\mathbb{H}^2}(s,z,w)\,\eta^\alpha_t(s)\,ds.$$
Note the integration is genuinely over $(0,\infty)$: [[Remark - Non-Compound-Poisson Assumption on the Bernstein Function|Assumption 2.3]] applies because $\nu_\alpha(0,\infty)=+\infty$, so $\eta^\alpha_t$ has no atom at $s=0$.

**The subordinate Dirichlet form.** From $\mathcal E^\phi(f,f)=a\|f\|^2+b\,\mathcal E(f,f)+\int_0^\infty(\|f\|^2-\langle e^{-sA}f,f\rangle)\,\nu(ds)$ with $(a,b,\nu)=(0,0,\nu_\alpha)$,
$$\mathcal E^\phi(f,f)=\int_0^\infty\big(\|f\|_{L^2}^2-\langle e^{-s\Delta_{\mathbb{H}^2}}f,f\rangle\big)\,\nu_\alpha(ds).$$
This is a **non-local energy**: it measures $f$'s deviation from its heat-flow at every scale $s>0$, weighted by the Lévy measure. The domain is $\mathcal F^\phi=\{f\in L^2:\mathcal E^\phi(f,f)<\infty\}$, which is *strictly larger* than $\mathcal F=H^1$ (the fractional Sobolev space $H^{\alpha/2}$).

**Why the process jumps.** Because the Bernstein function has $b=0$ (no drift) and $\nu_\alpha\ne 0$ (a genuine Lévy measure), the subordinator's own paths are non-decreasing càdlàg with countably many jumps. When the subordinator jumps by $s>0$ at some real time $t$, the underlying continuous Brownian motion moves during subordination-time interval $s$ by a *random* hyperbolic displacement, and the observed process $B_{S_t}$ therefore jumps by that random displacement. Every $\alpha\in(0,2)$ produces such a pure-jump process (in the strict sense that its paths are càdlàg but not continuous almost surely) — the $\alpha$-stable process on $\mathbb{H}^2$.

**Sanity check: recover $\alpha=2$.** At the boundary $\alpha=2$, $\phi(\lambda)=\lambda$, so this is case 1 of [[Ex - The Four Bernstein Functions of the Paper|Example 2.5]]: trivial subordinator, no jumps, ordinary Brownian motion. The paper restricts to $\alpha\in(0,2)$ open, keeping the boundary as a limiting continuous case.

**Sanity check: recover the flat picture on $\mathbb{R}^n$.** On $\mathbb{R}^n$ with the flat Laplacian, the same construction gives the isotropic $\alpha$-stable process on $\mathbb{R}^n$ — a well-known Lévy process with characteristic function $\mathbb{E}[e^{i\xi\cdot X_t}]=e^{-t|\xi|^\alpha}$, jumps distributed according to $|x|^{-n-\alpha}\,dx$. On $\mathbb{H}^2$ the object is the natural non-Euclidean analogue: same construction (subordinate Brownian motion), but with the hyperbolic metric replacing the flat one.

**Loop-measure consequence.** The corresponding [[Def - Subordinate Brownian Loop Measure|subordinate loop measure]] $\mu^\alpha_{\mathbb{H}^2}$ lives on càdlàg loops in $\mathbb{H}^2$. Because the underlying process has jumps, a càdlàg "loop" no longer has an honest continuous lift to the universal cover, so §3's homotopy-class decomposition needs its Remark 3.1 tweak: the class-mass is *defined* by restricting the periodisation to a conjugacy class, and interpreted via the underlying Brownian arc rather than the observed jump path.

---

# Calibration

The two limits and the interior:
- **$\alpha=2$ (boundary):** ordinary Brownian motion, continuous paths.
- **$\alpha=1$ (interior, illuminating):** the "Cauchy on $\mathbb{H}^2$" process; subordinator density is the closed-form $\frac{t}{2\sqrt\pi}s^{-3/2}e^{-t^2/(4s)}$.
- **$\alpha\to 0^+$ (limit):** the fractional Laplacian $\Delta^{\alpha/2}\to I$, so the semigroup degenerates to a trivial one; the process becomes very "jumpy" and is not usually considered.

**A calibration check.** Verify by the scaling identity $S_t\overset{d}{=}t^{2/\alpha}S_1$ that $\eta^\alpha_t(s)=t^{-2/\alpha}g_{\alpha/2}(s\,t^{-2/\alpha})$: if $S_t=t^{2/\alpha}S_1$ in distribution, then $\mathbb{P}(S_t\in[s,s+ds])=\mathbb{P}(S_1\in[s\,t^{-2/\alpha},(s+ds)t^{-2/\alpha}])=g_{\alpha/2}(s\,t^{-2/\alpha})\cdot t^{-2/\alpha}\,ds$. ✓

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.3.3]] alongside [[Ex - The Subordinate Form of Brownian Motion with Killing|Example 2.6]] as the two headline subordinate specialisations. The $\alpha$-stable case is the paper's primary jump-process test-bed; its free-homotopy-class mass is computed in §3.1.3 via [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]] and [[Ex - Weighted Potential Measures of the Paper's Bernstein Functions|Example 2.10(c)]] ($V_\phi=\frac{\alpha}{2}\frac{ds}{s}$). Its shifted variant (case 4 of [[Ex - The Four Bernstein Functions of the Paper|Example 2.5]]) is treated in §3.1.4. Also underlies the 3-manifold analog of §7.
