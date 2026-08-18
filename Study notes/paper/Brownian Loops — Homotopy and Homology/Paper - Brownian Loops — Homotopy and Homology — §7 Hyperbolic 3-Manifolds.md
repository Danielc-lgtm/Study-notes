---
type: paper-section
paper: "Belyaev–Huseynli, A probability measure on homotopy & homology classes via Brownian loops"
section: "7 — Brownian loops on hyperbolic 3-manifolds"
tags: [paper, brownian-loops, hyperbolic-geometry]
---

# §7 — Brownian loops on hyperbolic 3-manifolds

Back to the [[Paper - Brownian Loops — Homotopy and Homology|hub]]. The whole construction repeats one dimension up. §2's loop measure used $X$ only through its heat kernel, bridge measures, and the weights $dt/t$, $\operatorname{vol}_g$ — all of which exist on any complete Riemannian manifold — and §3's decomposition used only the descent-and-unfold over a cyclic centraliser. The single thing tying the paper to surfaces was *conformal invariance* (needed for Polyakov and the length-spectrum identity); with a killing rate or any non-linear subordination it plays no role, so nothing obstructs 3D. This section takes $X=\Gamma\backslash\mathbb{H}^3$ for a [[Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length|Kleinian group]] $\Gamma$ and re-derives the mass formulas — and, because the $\mathbb{H}^3$ heat kernel is explicit, does so *without* citing an external strip-integral (unlike §3, which used Wang–Xue).

**Symbols.** $\mathbb{H}^3$ hyperbolic 3-space; $\Gamma\subset\mathrm{PSL}(2,\mathbb{C})$ Kleinian; a geodesic $\gamma$ has **complex length** $L_\gamma=\ell_\gamma+i\theta_\gamma$ (translation $+i$ holonomy); $L=mL_\gamma$; $\mathcal F_\tau$ the fundamental slab.

> [!recall]- Hyperbolic 3-space, loxodromic elements, complex length, the H³ heat kernel
> **Formally:** **hyperbolic 3-space** is $\mathbb{H}^3:=\{(z,y):z\in\mathbb{C},y>0\}$ (the "upper half-space" — complex plane times positive reals) with Riemannian metric $ds^2=(|dz|^2+dy^2)/y^2$ and volume form $y^{-3}\,dA(z)\,dy$; its isometry group is $\mathrm{PSL}(2,\mathbb{C})$. An isometry $\tau\in\mathrm{PSL}(2,\mathbb{C})$ is **loxodromic** if it is conjugate to a *standard form* $(z,y)\mapsto(e^{L_\gamma}z,e^{\ell_\gamma}y)$ where $L_\gamma=\ell_\gamma+i\theta_\gamma\in\mathbb{C}$; $\ell_\gamma>0$ is the **translation length** (real part; distance moved along the axis), $\theta_\gamma\in\mathbb{R}$ the **holonomy angle** (imaginary part; rotation around the axis). The number $L_\gamma$ is called the **complex length**. The Brownian heat kernel on $\mathbb{H}^3$ has closed form $p_{\mathbb{H}^3}(t,z,w)=\frac{1}{(4\pi t)^{3/2}}\frac{u}{\sinh u}e^{-t-u^2/(4t)}$ where $u=d(z,w)$ is the hyperbolic distance.
> **In words:** the 3-dimensional analogue of the hyperbolic upper half-plane you know from §3. The isometry group is now the *complex* Möbius group $\mathrm{PSL}(2,\mathbb{C})$ (matrices with entries in $\mathbb{C}$ instead of $\mathbb{R}$), which is bigger. A closed geodesic in a 3-manifold quotient does two things at once: translate a distance $\ell_\gamma$ along its axis *and* rotate by $\theta_\gamma$ around the axis (like a screw). Packaging these two real numbers into one complex number $L_\gamma=\ell_\gamma+i\theta_\gamma$ (the *complex length*) is a bookkeeping convenience — it makes the mass formulas look like the surface formulas with $\ell$ upgraded to $L$. The heat kernel on $\mathbb{H}^3$ depends only on distance $u$ (as in flat space), but the flat-space Gaussian $\frac{1}{(4\pi t)^{3/2}}e^{-u^2/4t}$ gets multiplied by the curvature-correction factor $\frac{u}{\sinh u}e^{-t}$, which accounts for the negative curvature.
> **Concretely:** the loxodromic $\tau:(z,y)\mapsto(e^{\log 2}z,e^{\log 2}y)=(2z,2y)$ has $\ell_\gamma=\log 2\approx 0.693$, $\theta_\gamma=0$, so its complex length is real; the corresponding closed geodesic in the quotient is a purely-translational loop of length $\log 2$. The loxodromic $\tau':(z,y)\mapsto(e^{\log 2+i\pi/2}z,e^{\log 2}y)=(2iz,2y)$ has $\ell_\gamma=\log 2$, $\theta_\gamma=\pi/2$: same axis but with a $90°$ twist per period. At $u=1$, $t=1$: $p_{\mathbb{H}^3}(1,z,w)=\frac{1}{(4\pi)^{3/2}}\frac{1}{\sinh 1}e^{-1-1/4}\approx 0.0141$, versus the flat-space value $\frac{1}{(4\pi)^{3/2}}e^{-1/4}\approx 0.0350$: the curvature suppresses long paths. See [[Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length]].

---

## §7.1 — The homotopy-class decomposition (Theorem 7.1)

The lifting picture is identical to §3: free homotopy classes ↔ loxodromic conjugacy classes, cyclic centralisers $C_\Gamma(\tau^m)=\langle\tau\rangle$, coset enumeration $[\tau^m]_{\mathrm{conj}}=\bigsqcup_{r\in\Gamma/\langle\tau\rangle}\{r\tau^m r^{-1}\}$. The height scales by the real factor $e^{\ell_\gamma}$ (the rotation stays within a slab), so the fundamental region is the **slab** $\mathcal F_\tau=\{(z,y):1\le y<e^{\ell_\gamma}\}$.

> **Theorem 7.1 (homotopy-class decomposition, 3-manifolds).** For $\gamma\in\mathcal P_X$ with loxodromic representative $\tau$ (standard form) and $m\ge1$, the Dirichlet-form loop mass of $C_X(\gamma^m)$ is
> $$\mu^E_X(C_X(\gamma^m))=\int_0^\infty\frac{dt}{t}\int_{\mathcal F_\tau}p^E_{\mathbb{H}^3}(t,w,\tau^m w)\,d\!\operatorname{vol}_{\mathbb{H}^3}(w).$$
> **Proof.** Identical in structure to [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]] (isolate the conjugacy class, unfold over cosets $\Gamma/\langle\tau\rangle$ using $\Gamma$-invariance of the kernel, reassemble onto the slab using $\langle\tau\rangle$-invariance of $w\mapsto p^E_{\mathbb{H}^3}(t,w,\tau^m w)$), now with the loxodromic standard form from the recall above. $\blacksquare$

Stub: [[Thm - Homotopy Decomposition for 3-Manifolds]].

---

## §7.2 — Subordinate masses, with a self-contained strip integral

Specialising to a subordinate Brownian loop measure and expanding gives $\mu^\phi_X(C_X(\gamma^m))=\int_0^\infty\frac{dt}{t}\int_{\mathcal F_\tau}\int_{[0,\infty)}p_{\mathbb{H}^3}(s,w,\tau^m w)\,\psi^\phi_t(ds)\,d\!\operatorname{vol}_{\mathbb{H}^3}(w)$. The paper evaluates the spatial integral directly from the explicit $\mathbb{H}^3$ heat kernel.

> [!note]- Gap-free derivation of the H³ strip integral
> **Distance to the image.** For $w=(z,y)$ in standard coordinates, $\tau^m w=(e^{L}z,e^{m\ell_\gamma}y)$ with $L=mL_\gamma$. The hyperbolic distance $u=d(w,\tau^m w)$ satisfies
> $$\cosh u=1+\frac{|z-e^{L}z|^2+(y-e^{m\ell_\gamma}y)^2}{2\,e^{m\ell_\gamma}y^2}=\cosh(m\ell_\gamma)+\frac{|e^{L}-1|^2\,|z|^2}{2\,e^{m\ell_\gamma}y^2},$$
> using $|e^{L}-1|^2=1-2e^{m\ell_\gamma}\cos(m\theta_\gamma)+e^{2m\ell_\gamma}$ and $1+\frac{(1-e^{m\ell_\gamma})^2}{2e^{m\ell_\gamma}}=\cosh(m\ell_\gamma)$. So $u$ depends on $z$ only through $|z|=r$.
> **Integrate the slab.** With $d\!\operatorname{vol}_{\mathbb{H}^3}=y^{-3}\,dA(z)\,dy$ and polar $z=re^{i\varphi}$ ($dA=r\,dr\,d\varphi$), the $\varphi$-integral gives $2\pi$:
> $$\int_{\mathcal F_\tau}p_{\mathbb{H}^3}(t,w,\tau^m w)\,d\!\operatorname{vol}_{\mathbb{H}^3}=2\pi\int_1^{e^{\ell_\gamma}}\!\!\int_0^\infty p_{\mathbb{H}^3}(t,u)\,r\,dr\,\frac{dy}{y^3}.$$
> **Change $r\to u$.** At fixed $y$, differentiating $\cosh u$ gives $\sinh u\,du=\frac{|e^L-1|^2\,r}{e^{m\ell_\gamma}y^2}\,dr$, i.e. $r\,dr=\frac{e^{m\ell_\gamma}y^2}{|e^L-1|^2}\sinh u\,du$, and $r:0\to\infty$ corresponds to $u:m\ell_\gamma\to\infty$. The $\sinh u$ cancels the $1/\sinh u$ in $p_{\mathbb{H}^3}=\frac{1}{(4\pi t)^{3/2}}\frac{u}{\sinh u}e^{-t-u^2/4t}$, leaving a clean Gaussian in $u$:
> $$\int_0^\infty p_{\mathbb{H}^3}(t,u)\,r\,dr=\frac{e^{m\ell_\gamma}y^2}{|e^L-1|^2}\cdot\frac{1}{(4\pi t)^{3/2}}\int_{m\ell_\gamma}^\infty u\,e^{-t-u^2/4t}\,du=\frac{e^{m\ell_\gamma}y^2}{|e^L-1|^2}\cdot\frac{2t\,e^{-t}}{(4\pi t)^{3/2}}e^{-(m\ell_\gamma)^2/4t},$$
> since $\int_{a}^\infty u\,e^{-u^2/4t}\,du=2t\,e^{-a^2/4t}$. The $y^2$ meets $y^{-3}$ and $\int_1^{e^{\ell_\gamma}}y^{-1}\,dy=\ell_\gamma$, giving
> $$\int_{\mathcal F_\tau}p_{\mathbb{H}^3}(t,w,\tau^m w)\,d\!\operatorname{vol}_{\mathbb{H}^3}=2\pi\,\frac{e^{m\ell_\gamma}\ell_\gamma}{|e^L-1|^2}\cdot\frac{2t\,e^{-t}}{(4\pi t)^{3/2}}e^{-(m\ell_\gamma)^2/4t}=\frac{\ell_\gamma}{2(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma))}\cdot\frac{e^{-t-(m\ell_\gamma)^2/4t}}{\sqrt{4\pi t}},$$
> the last form using $|e^{a+ib}-1|^2=2e^{a}(\cosh a-\cos b)$ and $2\pi\cdot\frac{2t}{(4\pi t)^{3/2}}=\frac{1}{\sqrt{4\pi t}}$. This is the $\mathbb{H}^3$ analogue of Wang–Xue's Lemma 3.4 — **derived, not cited.** ∎

> **Theorem 7.2 (subordinate mass, 3-manifolds).** For a Bernstein $\phi$ of the paper, $\gamma\in\mathcal P_X$, $m\ge1$ (with $L=mL_\gamma=m\ell_\gamma+im\theta_\gamma$),
> $$\mu^\phi_X(C_X(\gamma^m))=2\pi\,\frac{e^{m\ell_\gamma}\ell_\gamma}{|e^{L}-1|^2}\int_{(0,\infty)}\frac{2s\,e^{-s}}{(4\pi s)^{3/2}}\,e^{-(m\ell_\gamma)^2/4s}\,V_\phi(ds).$$
> **Proof.** Put the strip integral above (at subordination time $s$) into the expanded mass, then apply [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]] with $h(s)=\frac{2s\,e^{-s}}{(4\pi s)^{3/2}}e^{-(m\ell_\gamma)^2/4s}$ to collapse the $\frac{dt}{t}$-integral against $V_\phi$. $\blacksquare$

Stub: [[Thm - Mass of Subordinate Loops on 3-Manifolds]].

> **Corollary 7.3 (Brownian mass, 3-manifolds).** For pure Brownian motion,
> $$\mu_X(C_X(\gamma^m))=\frac1m\cdot\frac{1}{|e^{mL_\gamma}-1|^2}=\frac{e^{-m\ell_\gamma}}{2m\,(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma))}=\frac1m\Big[(e^{m\ell_\gamma}-1)^2+4e^{m\ell_\gamma}\sin^2\frac{m\theta_\gamma}{2}\Big]^{-1}.$$
> When $\theta_\gamma=0$ (no holonomy) the denominator is $(e^{m\ell_\gamma}-1)^2$ — but note this is the *square* of the surface answer, the extra factor being the "cross-section" of the 3D geodesic.

> [!note]- Gap-free proof of Corollary 7.3
> For Brownian motion $V_\phi(ds)=ds/s$ (Example 2.10), so Theorem 7.2 becomes
> $$\mu_X(C_X(\gamma^m))=2\pi\,\frac{e^{m\ell_\gamma}\ell_\gamma}{|e^{L}-1|^2}\cdot\frac{2}{(4\pi)^{3/2}}\int_0^\infty s^{-3/2}e^{-s-(m\ell_\gamma)^2/4s}\,ds.$$
> The integral is $\int_0^\infty s^{-3/2}e^{-as-b/s}\,ds=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$ (proved in [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3.1]]) with $a=1$, $b=(m\ell_\gamma)^2/4$: it equals $\sqrt{\pi/(m\ell_\gamma)^2/4}\,e^{-2\sqrt{(m\ell_\gamma)^2/4}}=\frac{2\sqrt\pi}{m\ell_\gamma}e^{-m\ell_\gamma}$. Substituting,
> $$\mu_X(C_X(\gamma^m))=2\pi\,\frac{e^{m\ell_\gamma}\ell_\gamma}{|e^{L}-1|^2}\cdot\frac{2}{(4\pi)^{3/2}}\cdot\frac{2\sqrt\pi}{m\ell_\gamma}e^{-m\ell_\gamma}=\frac{1}{m}\cdot\frac{e^{m\ell_\gamma}e^{-m\ell_\gamma}}{|e^L-1|^2}\cdot\underbrace{\frac{2\pi\cdot2\cdot2\sqrt\pi}{(4\pi)^{3/2}}}_{=1},$$
> since $(4\pi)^{3/2}=8\pi\sqrt\pi$ and $2\pi\cdot2\cdot2\sqrt\pi=8\pi\sqrt\pi$. Hence $\mu_X(C_X(\gamma^m))=\frac1m\frac{1}{|e^{mL_\gamma}-1|^2}$. The equivalent forms follow from $|e^{mL_\gamma}-1|^2=2e^{m\ell_\gamma}(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma))$ and $1-\cos(m\theta_\gamma)=2\sin^2(m\theta_\gamma/2)$, giving $|e^{mL_\gamma}-1|^2=(e^{m\ell_\gamma}-1)^2+4e^{m\ell_\gamma}\sin^2(m\theta_\gamma/2)$. $\blacksquare$

Stub: [[Cor - Brownian Mass on 3-Manifolds]]. This closes the paper: the same random-loop weights, now on a 3-manifold, packaged by the complex length. (§4–§6's zeta/probability apparatus carries over with $\ell_\gamma\to L_\gamma$ and $\sinh^2\to|e^{L}-1|^2$, though the paper develops that only for surfaces.)

---

## Section verification log (§7)

**Verified.** The $\mathbb{H}^3$ strip integral (eqs. 88–89) is derived in full from the explicit heat kernel — the change of variables $r\to u$, the cancellation of $\sinh u$, the Gaussian $\int_a^\infty u\,e^{-u^2/4t}du=2t\,e^{-a^2/4t}$, and the constant bookkeeping $2\pi\cdot2\cdot2\sqrt\pi=(4\pi)^{3/2}$. Theorem 7.2 and Corollary 7.3 (both equivalent forms) proved gap-free; Theorem 7.1 by explicit reduction to Theorem 3.2's structure.
**Flagged / uncertain.** None outstanding for §7. The identity $\cosh u=\cosh(m\ell_\gamma)+\frac{|e^L-1|^2|z|^2}{2e^{m\ell_\gamma}y^2}$ is the paper's; I verified the two auxiliary identities it rests on ($|e^L-1|^2$ and the $\cosh$ constant).
**Intuition not yet formalised.** The remark that §4–§6's zeta/probability results carry over to 3-manifolds with $\ell_\gamma\to L_\gamma$ is stated but not developed (the paper leaves it for surfaces); flagged as a pointer, not a proved extension.
