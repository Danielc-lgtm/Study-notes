---
type: remark
subject: probability-geometry
prereqs:
  - "Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length"
  - "Def - Hyperbolic Plane"
  - "Def - Heat Kernel and Heat Semigroup"
  - "Def - Brownian Motion on a Riemannian Manifold"
tags: [paper, brownian-loops, hyperbolic-geometry, heat-kernel]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "unnumbered; §7.2 opening — why the $\\mathbb{H}^3$ strip integral is derived rather than imported from Wang–Xue"
---

# Notation

- $p_{\mathbb{H}^n}(t, z, w)$ — Brownian heat kernel on $\mathbb{H}^n$: the fundamental solution of $\partial_t f = \frac12 \Delta_{\mathbb{H}^n} f$.
- $d(z, w)$ — hyperbolic distance on $\mathbb{H}^n$.
- $\Delta_{\mathbb{H}^n}$ — the Laplace–Beltrami operator on $\mathbb{H}^n$ (negative definite as a self-adjoint operator; its spectral bottom is $-((n-1)/2)^2$).
- $\mathcal{F}_\tau$ — the fundamental slab of a loxodromic (in 3D) or hyperbolic (in 2D) isometry $\tau$; a fundamental region for $\langle\tau\rangle$ acting on the ambient hyperbolic space.
- $L_\gamma = \ell_\gamma + i\theta_\gamma$ — complex length of a closed geodesic on a 3-manifold.
- [WX25] — Wang–Xue, whose length-spectrum identity is invoked at [[Lemma - Wang-Xue Strip Integral|Lemma 3.4]] to evaluate the $\mathbb{H}^2$ strip integral in closed form.

> [!recall]- The $\mathbb{H}^2$ heat kernel (as an integral)
> **Formally:** the Brownian heat kernel on $\mathbb{H}^2$ has the standard McKean formula
> $$p_{\mathbb{H}^2}(t, z, w) = \frac{\sqrt 2\,e^{-t/8}}{(4\pi t)^{3/2}} \int_u^\infty \frac{r\,e^{-r^2/4t}}{\sqrt{\cosh r - \cosh u}}\,dr,\quad u = d(z, w),$$
> a *one-parameter integral*, not a closed elementary function. The integrand depends on the ambient dimension being even (in odd dimensions the Selberg-transform inversion is a derivative, not an integral).
> **In words:** on $\mathbb{H}^2$ the probability density that a Brownian particle started at $z$ is near $w$ at time $t$ is *not* expressible in elementary functions of $u = d(z, w)$ and $t$; it is a specific integral against an elementary integrand. This is a genuine obstruction to closed-form computation — any spatial integral of $p_{\mathbb{H}^2}$ becomes a double integral, hard to evaluate directly.
> **Concretely:** at $t \to 0$ the McKean formula recovers the leading Euclidean Gaussian $(4\pi t)^{-1}e^{-u^2/(4t)}$ plus curvature corrections; there is no elementary closed form even for $u = 0$ (though $p_{\mathbb{H}^2}(t, z, z)$ is a specific analytic function of $t$ known via the Selberg trace formula). See [[Def - Heat Kernel and Heat Semigroup]].

> [!recall]- The $\mathbb{H}^3$ heat kernel (closed form)
> **Formally:** the Brownian heat kernel on $\mathbb{H}^3$ is the elementary closed form
> $$p_{\mathbb{H}^3}(t, z, w) = \frac{1}{(4\pi t)^{3/2}}\,\frac{u}{\sinh u}\,e^{-t - u^2/(4t)},\quad u = d(z, w),$$
> where the $e^{-t}$ prefactor is the spectral shift $e^{-((n-1)/2)^2 t}$ at $n = 3$ (bottom of the $L^2$ spectrum of $-\frac12\Delta_{\mathbb{H}^3}$ is $1$).
> **In words:** on $\mathbb{H}^3$ (and on every odd-dimensional real hyperbolic space) the heat kernel is a genuine elementary function of the hyperbolic distance $u$ and the time $t$ — the Gaussian $(4\pi t)^{-3/2}e^{-u^2/(4t)}$ modified by two curvature factors: $u/\sinh u$ suppresses long paths, $e^{-t}$ suppresses long times. Spatial integrals of $p_{\mathbb{H}^3}$ collapse to elementary Gaussians via the substitution $r \to u$ that cancels $\sinh u$.
> **Concretely:** at $t = 1$, $u = 1$: $p_{\mathbb{H}^3}(1) = (4\pi)^{-3/2}\,(1/\sinh 1)\,e^{-1 - 1/4} \approx 0.014$. At $u \to 0$: $u/\sinh u \to 1$, on-diagonal $p_{\mathbb{H}^3}(1, z, z) = (4\pi)^{-3/2}e^{-1} \approx 0.017$. See [[Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length]].

> [!recall]- Even-vs-odd hyperbolic dimensions and the Selberg transform
> **Formally:** on $\mathbb{H}^n$ any $\mathrm{Isom}(\mathbb{H}^n)$-invariant kernel is a function of hyperbolic distance $u$; the Selberg transform inverts the Fourier decomposition of such kernels. In *odd* dimensions the inverse is a differential operator applied to a Gaussian in $u$, giving an elementary closed form (the "descent method"). In *even* dimensions the inverse involves a further integral, giving a one-parameter integral representation.
> **In words:** hyperbolic spaces of odd dimension are computationally friendly for heat-kernel work: their heat kernels are elementary. Even-dimensional hyperbolic spaces are computationally unfriendly: their heat kernels involve residual integrals. §7 exploits this parity to derive its strip integral without importing anything.
> **Concretely:** $\mathbb{H}^1 = \mathbb{R}$ has the flat-space Gaussian; $\mathbb{H}^3$ has the McKean/Millson formula above; $\mathbb{H}^5$ has a formula with two curvature corrections; all odd-$n$ formulas are elementary. $\mathbb{H}^2$'s formula is the integral above; $\mathbb{H}^4$'s and $\mathbb{H}^{2k}$'s formulas are similar integrals. This parity is why the paper cites [WX25] for the surface case but derives §7.2 from first principles.

---

# Claim / Identity

> **Claim (in-house derivation of the $\mathbb{H}^3$ strip integral).** For any loxodromic $\tau$ in standard form $\tau(z, y) = (e^{L_\gamma} z, e^{\ell_\gamma} y)$, any winding $m \ge 1$, and $L := mL_\gamma$, the identity
> $$\int_{\mathcal{F}_\tau} p_{\mathbb{H}^3}(t, w, \tau^m w)\,d\operatorname{vol}_{\mathbb{H}^3}(w) = \frac{\ell_\gamma}{2(\cosh(m\ell_\gamma) - \cos(m\theta_\gamma))} \cdot \frac{e^{-t - (m\ell_\gamma)^2/(4t)}}{\sqrt{4\pi t}}$$
> is proved *without invoking any external length-spectrum result* — in particular without citing [WX25]. The proof uses only the explicit closed form of $p_{\mathbb{H}^3}$, the change of variables $r \to u$ that lets $\sinh u$ cancel, one elementary Gaussian integral, and one $y$-integral. This is in contrast to the surface case [[Lemma - Wang-Xue Strip Integral|(Lemma 3.4)]], where the analogous identity is *imported* from Wang–Xue [WX25] because the $\mathbb{H}^2$ heat kernel is not elementary and the surface-strip integral is not obviously evaluable from first principles.

---

# In One Line

Odd-dimensional real hyperbolic spaces have elementary heat kernels; the $\mathbb{H}^3$ kernel's $u/\sinh u$ factor is cancelled by the Jacobian of the polar substitution on the strip, leaving an elementary Gaussian — so the 3-manifold analogue of Wang–Xue's length-spectrum identity is derivable in-house rather than imported.

---

# Why It's True

The Wang–Xue identity for the $\mathbb{H}^2$ strip integral is a real theorem whose proof exploits the Selberg transform / trace-formula machinery for 2D hyperbolic geometry — the $\mathbb{H}^2$ heat kernel does not simplify enough to permit a direct polar-coordinate evaluation, so one needs the spectral apparatus. Even the *statement* of Lemma 3.4 requires the [WX25] framework to write cleanly.

On $\mathbb{H}^3$ the situation is entirely different. Millson's / McKean's formula gives $p_{\mathbb{H}^3}(t, z, w)$ as an elementary function of hyperbolic distance $u$ and time $t$, with the crucial $u/\sinh u$ factor sitting *in front* of a Gaussian in $u$. When one sets up the strip integral in polar coordinates $z = re^{i\phi}$ and changes variables from the horizontal radius $r$ to the hyperbolic distance $u$, the Jacobian factor $\sinh u\,du$ *cancels* the $1/\sinh u$ in the kernel exactly, and what remains is $\int_a^\infty u\,e^{-u^2/(4t)}\,du = 2t\,e^{-a^2/(4t)}$ — an elementary Gaussian moment. The $y$-integral over the slab collapses to $\int_1^{e^{\ell_\gamma}} y^{-1}\,dy = \ell_\gamma$. The two auxiliary algebraic identities $\cosh a = 1 + (1 - e^a)^2/(2e^a)$ and $|e^{a+ib} - 1|^2 = 2e^a(\cosh a - \cos b)$ organise the constants into the answer. Total computation: half a page. **Mechanism: the $\mathbb{H}^3$ heat kernel's $u/\sinh u$ prefactor is exactly the reciprocal of the Jacobian $\sinh u\,du/dr$ produced by the polar change of variables, so the whole spatial integral evaluates to a Gaussian by first-principles calculus — no spectral / trace-formula machinery required.**

The consequence for the paper's structure is that §7.2's central computation is *self-contained*: the paper needs no external reference to state or prove its 3-manifold class-mass formulas (Theorem 7.2, Corollary 7.3), whereas the surface case at Theorem 3.5 leans on the imported [WX25] identity. This is not merely an aesthetic difference — it means §7 could in principle be read before §§3–6 by a reader interested only in the 3-manifold picture, using only §2's set-up and the elementary calculus in this remark.

---

# Derivation

> [!note]- Gap-free derivation
>
> This remark is a meta-observation, not a computation. The full step-by-step evaluation of the $\mathbb{H}^3$ strip integral lives in [[Lemma - Hyperbolic 3-Space Strip Integral]]; here we just record *why* it is doable in-house.
>
> **Step 1 (identify the obstruction in 2D).** The $\mathbb{H}^2$ heat kernel is
> $$p_{\mathbb{H}^2}(t, z, w) = \frac{\sqrt 2\,e^{-t/8}}{(4\pi t)^{3/2}}\int_u^\infty \frac{r\,e^{-r^2/4t}}{\sqrt{\cosh r - \cosh u}}\,dr,\quad u = d(z, w).$$
> Its dependence on $u$ is through the outer integral only, so any spatial integral $\int p_{\mathbb{H}^2}(t, w, \tau^m w)\,d\rho_{\mathbb{H}^2}(w)$ becomes a *double* integral (one over $w$, one over the inner $r$). Fubini and a substitution do not collapse it to a single elementary formula. The Wang–Xue evaluation of this double integral uses the Selberg transform and the length-spectrum identity for $\mathbb{H}^2$; the paper imports it as [WX25]'s Lemma 3.4.
>
> **Step 2 (identify the simplification in 3D).** The $\mathbb{H}^3$ heat kernel is elementary:
> $$p_{\mathbb{H}^3}(t, z, w) = \frac{1}{(4\pi t)^{3/2}}\,\frac{u}{\sinh u}\,e^{-t - u^2/(4t)},\quad u = d(z, w).$$
> The three factors are (i) the constant $(4\pi t)^{-3/2}$, (ii) the geometric correction $u/\sinh u$, (iii) the "shifted Gaussian" $e^{-t - u^2/(4t)}$. Odd-dimensional real hyperbolic spaces admit elementary heat-kernel formulas via the descent method: the invariant heat operator commutes with the Selberg transform, and in odd dimensions the inverse Selberg transform is a differential operator applied to a Gaussian, giving an elementary closed form. $n = 3$ is the first non-trivial case.
>
> **Step 3 (show the polar Jacobian cancels the geometric factor).** Set $\tau^m(z, y) = (e^L z, e^{m\ell_\gamma} y)$ with $L = mL_\gamma$. Fix a height $y > 0$ and pass to polar coordinates $z = r e^{i\phi}$ on the horizontal plane; $dA(z) = r\,dr\,d\phi$. The distance is
> $$\cosh u = \cosh(m\ell_\gamma) + \frac{|e^L - 1|^2\,r^2}{2\,e^{m\ell_\gamma}\,y^2},$$
> depending on $z$ only through $r$. The angular integral gives $2\pi$. Change variables from $r$ to $u$: differentiating $\cosh u$ gives $\sinh u\,du = \frac{|e^L - 1|^2\,r}{e^{m\ell_\gamma}\,y^2}\,dr$, so
> $$r\,dr = \frac{e^{m\ell_\gamma}\,y^2}{|e^L - 1|^2}\,\sinh u\,du.$$
> The factor $\sinh u$ *cancels* the $1/\sinh u$ in $p_{\mathbb{H}^3}$. The inner integral becomes
> $$\int_0^\infty p_{\mathbb{H}^3}(t, u)\,r\,dr = \frac{e^{m\ell_\gamma}\,y^2}{|e^L - 1|^2} \cdot \frac{1}{(4\pi t)^{3/2}}\,e^{-t}\,\int_{m\ell_\gamma}^\infty u\,e^{-u^2/(4t)}\,du.$$
> The remaining $u$-integral is a first-moment Gaussian:
> $$\int_a^\infty u\,e^{-u^2/(4t)}\,du = 2t\,e^{-a^2/(4t)}\quad (a = m\ell_\gamma).$$
> Elementary — no external input.
>
> **Step 4 (evaluate the $y$-integral).** The volume element is $d\operatorname{vol}_{\mathbb{H}^3} = y^{-3}\,dA(z)\,dy$. The $y^2$ from Step 3 combines with $y^{-3}$ to give $y^{-1}$, and
> $$\int_1^{e^{\ell_\gamma}} \frac{dy}{y} = \ell_\gamma.$$
> Again elementary.
>
> **Step 5 (assemble and simplify).** Multiplying the pieces:
> $$\int_{\mathcal{F}_\tau} p_{\mathbb{H}^3}(t, w, \tau^m w)\,d\operatorname{vol}_{\mathbb{H}^3}(w) = 2\pi \cdot \frac{e^{m\ell_\gamma}\,\ell_\gamma}{|e^L - 1|^2} \cdot \frac{2 t\,e^{-t}}{(4\pi t)^{3/2}}\,e^{-(m\ell_\gamma)^2/(4t)}.$$
> Applying $|e^{a+ib} - 1|^2 = 2 e^a(\cosh a - \cos b)$ with $a = m\ell_\gamma$, $b = m\theta_\gamma$ and $2\pi \cdot 2t/(4\pi t)^{3/2} = 1/\sqrt{4\pi t}$ gives the compact form
> $$\int_{\mathcal{F}_\tau} p_{\mathbb{H}^3}(t, w, \tau^m w)\,d\operatorname{vol}_{\mathbb{H}^3}(w) = \frac{\ell_\gamma}{2(\cosh(m\ell_\gamma) - \cos(m\theta_\gamma))} \cdot \frac{e^{-t - (m\ell_\gamma)^2/(4t)}}{\sqrt{4\pi t}}.$$
> No external result invoked at any step — the calculation lives entirely inside elementary calculus and the explicit heat-kernel formula.
>
> **Step 6 (contrast).** Attempting Steps 3–5 with $p_{\mathbb{H}^2}$ in place of $p_{\mathbb{H}^3}$ fails at Step 3: the $\mathbb{H}^2$ kernel's dependence on $u$ is *inside* an integral, and the polar change of variables $r \to u$ does not remove that integral. This is the obstruction Wang–Xue's length-spectrum machinery is designed to overcome, and the reason the paper imports [WX25]'s Lemma 3.4 in §3.4 but derives the corresponding identity in §7.2 for free.
>
> $\square$

---

# Where the paper uses this

The observation opens [[Paper - Brownian Loops — Homotopy and Homology — §7 Hyperbolic 3-Manifolds|§7]] and licenses [[Lemma - Hyperbolic 3-Space Strip Integral|the §7.2 strip lemma]], which in turn feeds [[Thm - Mass of Subordinate Loops on 3-Manifolds|Theorem 7.2]] and [[Cor - Brownian Mass on 3-Manifolds|Corollary 7.3]]. The corresponding surface-case identity is [[Lemma - Wang-Xue Strip Integral|Lemma 3.4]], imported from Wang–Xue [WX25]. The parity phenomenon behind this — "odd-dimensional real hyperbolic spaces have elementary heat kernels, even-dimensional ones do not" — is a general fact and applies to any $\mathbb{H}^{2k+1}$, so the same "derive in-house" pattern would work for the paper's hypothetical extension to higher odd-dimensional hyperbolic manifolds.
