---
type: paper-section
paper: "Belyaev–Huseynli, A probability measure on homotopy & homology classes via Brownian loops"
section: "3 — Decomposition over homotopy classes"
tags: [paper, brownian-loops, hyperbolic-geometry]
---

# §3 — Decomposition over homotopy classes

Back to the [[Paper - Brownian Loops — Homotopy and Homology|hub]]. In §2 the total Brownian loop mass came out infinite, and the divergence was a small-$t$ (short-loop) effect. This section is the paper's turning point: it **sorts loops by topological type** and shows each type carries *finite* mass, with an explicit closed form. The mechanism is geometric — a loop's type is recorded by a [[Def - Fuchsian Group and the Hyperbolic Quotient Surface|deck transformation]], winding around a hole forces the loop to be at least as long as the corresponding closed geodesic, and that length lower bound is exactly what cuts off the small-$t$ divergence. The headline is **Theorem 3.2**, a formula for the mass of a free homotopy class as a single integral over a strip; §3.1 evaluates it in closed form for every process the paper uses; §3.2–3.4 draw out the physics (loop-soup, partition functions) and the geometry (length spectra).

**Setup.** $\Gamma\subset\mathrm{PSL}(2,\mathbb{R})$ a torsion-free [[Def - Fuchsian Group and the Hyperbolic Quotient Surface|Fuchsian group]], $X=\Gamma\backslash\mathbb{H}^2$ geometrically finite; $\pi:\mathbb{H}^2\to X$; $\rho_{\mathbb{H}^2}$, $\rho_X$ the [[Def - Hyperbolic Plane|hyperbolic]] area measures upstairs/downstairs; $(\mathcal E,\mathcal F)$ a $\Gamma$-invariant [[Def - Dirichlet Form and its Operator and Semigroup|Dirichlet form]] on $L^2(\mathbb{H}^2,\rho)$ with $\Gamma$-invariant kernel $p^E_{\mathbb{H}^2}(t,z,w)=p^E_{\mathbb{H}^2}(t,hz,hw)$ ($h\in\Gamma$).

---

## §3.0 — The lifting picture

Everything rests on translating a loop's *topology* into an *algebraic* datum in $\Gamma$.

> [!recall]- Universal cover and deck transformations
> **Formally:** $\pi:\mathbb{H}^2\to X=\Gamma\backslash\mathbb{H}^2$ is the [[Def - Universal Cover|universal covering map]]; its **deck transformation group** is $\Gamma$ itself — the isometries $h$ of $\mathbb{H}^2$ with $\pi\circ h=\pi$. Fixing $x\in X$ and $\tilde x\in\pi^{-1}(x)$ gives an isomorphism $\pi_1(X,x)\cong\Gamma$. Every path in $X$ has a unique lift to $\mathbb{H}^2$ once its start is chosen (path-lifting).
> **In words:** $\mathbb{H}^2$ is the "unrolled" surface; $\Gamma$ is the group of ways to re-roll it. A loop downstairs becomes an *arc* upstairs whose endpoints differ by the group element you re-rolled by. See [[Def - Universal Cover]], [[Def - Fuchsian Group and the Hyperbolic Quotient Surface]].

A loop $\omega:[0,t]\to X$ rooted at $x$ lifts to an arc $\tilde\omega$ from $\tilde x$ to $h_\omega\tilde x$ for a **unique $h_\omega\in\Gamma$** (its endpoint lies in the fibre $\pi^{-1}(x)=\Gamma\tilde x$). This $h_\omega$ is the **monodromy**; $h_\omega=\mathrm{id}$ iff $\omega$ is contractible. Moving the basepoint conjugates $h_\omega$ (start at $q\tilde x$ instead of $\tilde x$ and the recorded element becomes $qh_\omega q^{-1}$, same translation length), so the basepoint-free invariant is the *conjugacy class*.

> [!recall]- Free homotopy classes ↔ conjugacy classes; closed geodesics; fundamental strip
> **Formally:** free homotopy classes of oriented closed curves on $X$ correspond bijectively to conjugacy classes in $\Gamma$; a non-trivial non-peripheral class corresponds to a primitive hyperbolic $\tau$, conjugated to standard form $\tau:z\mapsto e^{\ell_\gamma}z$ with axis the imaginary half-line and translation length $\ell_\gamma$; the class contains the unique closed geodesic $\gamma$ of length $\ell_\gamma$. The class winding $m$ times is $C_X(\gamma^m)\leftrightarrow[\tau^m]_{\mathrm{conj}}$. The centraliser is $C_\Gamma(\tau^m)=\langle\tau\rangle$, so $[\tau^m]_{\mathrm{conj}}=\bigsqcup_{r\in\Gamma/\langle\tau\rangle}\{r\tau^m r^{-1}\}$ (one conjugate per coset). Since $\operatorname{Im}(\tau z)=e^{\ell_\gamma}\operatorname{Im}z$, the **fundamental strip** $\mathcal F_\tau=\{z:1\le\operatorname{Im}z<e^{\ell_\gamma}\}$ is a fundamental region for $\langle\tau\rangle$.
> **In words:** "which hole, how many times" is recorded by a conjugacy class; each class has one taut geodesic representative of a definite length; the strip is one period of the cylinder that $\langle\tau\rangle$ wraps up. See [[Def - Closed Geodesics, Conjugacy Classes, and Translation Length]].

**Descent of the heat kernel (the periodisation).** The downstairs kernel is the sum of the upstairs kernel over the group — the standard way a $\Gamma$-invariant object on $\mathbb{H}^2$ becomes one on $X$:
$$p^E_X(t,z,w)=\sum_{h\in\Gamma}p^E_{\mathbb{H}^2}(t,\tilde z,h\tilde w),$$
convergent because the geometrically-finite $\Gamma$'s orbit grows slower than the kernel decays. Restricting the sum to a conjugacy class picks out loops of the corresponding type.

**Jump processes (Remark 3.1).** An $\alpha$-stable loop is a càdlàg path with deleted segments, so it has no honest lift and no free homotopy class. The paper *defines* the class-mass for jump processes by restricting the periodisation to $[\tau^m]_{\mathrm{conj}}$: $\mu^E_X(C_X(\gamma^m)):=\int_0^\infty\frac{dt}{t}\int_X\sum_{h\in[\tau^m]_{\mathrm{conj}}}p^E_{\mathbb{H}^2}(t,\tilde z,h\tilde z)\,d\rho_X(z)$. ⚠️ *(Intuition, flagged: for jump processes this is a definition, not a theorem — the class is recovered from the underlying Brownian arc $B$ of the pair $(B,S)=Y$, not from the càdlàg path $Y$ alone, which the paper notes is not intrinsically recoverable. The formula below therefore reads as the same integral in both the continuous and jump cases; only its interpretation differs.)*

---

## §3.1 (statement) — Theorem 3.2: the mass of a free homotopy class

> **Theorem 3.2 (mass of a free homotopy class).** Let $\gamma\in\mathcal P_X$ be a primitive closed geodesic with hyperbolic representative $\tau:z\mapsto e^{\ell_\gamma}z$ and winding number $m\ge1$. The mass of the Dirichlet-form loop measure in the free homotopy class is
> $$\mu^E_X\big(C_X(\gamma^m)\big)=\int_0^\infty\frac{dt}{t}\int_{\mathcal F_\tau}p^E_{\mathbb{H}^2}\big(t,z,\tau^m z\big)\,d\rho_{\mathbb{H}^2}(z),$$
> an integral of the upstairs heat kernel between a point and its $\tau^m$-image, over one fundamental strip.

Stub: [[Thm - Mass of a Free Homotopy Class]]. The point is that the messy sum over the whole group has collapsed to a *single* term $p^E_{\mathbb{H}^2}(t,z,\tau^m z)$ integrated over *one* strip — that is what makes the mass computable and, as §3.1 shows, finite.

**Why one should expect it.** A loop in class $C_X(\gamma^m)$ lifts to an arc from $z$ to $\tau^m z$ (up to conjugacy/basepoint). Its "amount" is the bridge mass $p^E_{\mathbb{H}^2}(t,z,\tau^m z)$. Summing over basepoints and unwrapping the conjugacy-class-and-orbit redundancy should leave exactly one copy per period — one strip. The proof makes "one copy per period" precise via the coset enumeration.

> [!note]- Gap-free proof of Theorem 3.2
> **Step 1 — isolate the conjugacy class.** For a continuous process the lifting picture gives the bridge decomposition $\mathbb{W}^{t,E}_{z\to z,\,X}=\sum_{h\in\Gamma}\pi_*\mathbb{W}^{t,E}_{\tilde z\to h\tilde z,\,\mathbb{H}^2}$: a loop rooted at $z$ is classified by the deck element $h$ its lift records, so its bridge measure is the sum over $h\in\Gamma$ of the (pushed-down) upstairs bridges from $\tilde z$ to $h\tilde z$. Taking total masses ($|\mathbb{W}^{t,E}_{\tilde z\to h\tilde z}|=p^E_{\mathbb{H}^2}(t,\tilde z,h\tilde z)$) and restricting to loops of type $C_X(\gamma^m)$ keeps only $h\in[\tau^m]_{\mathrm{conj}}$ (for a jump process this restriction *is* the definition, Remark 3.1). Hence
> $$\mu^E_X(C_X(\gamma^m))=\int_0^\infty\frac{dt}{t}\int_X\sum_{h\in[\tau^m]_{\mathrm{conj}}}p^E_{\mathbb{H}^2}(t,\tilde z,h\tilde z)\,d\rho_X(z).\tag{16}$$
> **Step 2 — lift the base integral to a fundamental region.** Let $F\subset\mathbb{H}^2$ be a fundamental region for $\Gamma$. Since $\pi$ is one-to-one from $F$ onto (almost all of) $X$ and the integrand is a $\Gamma$-invariant function of $z$ downstairs, $\int_X(\cdots)\,d\rho_X=\int_F(\cdots)\,d\rho_{\mathbb{H}^2}$, turning (16) into
> $$\int_0^\infty\frac{dt}{t}\int_F\sum_{h\in[\tau^m]_{\mathrm{conj}}}p^E_{\mathbb{H}^2}(t,z,hz)\,d\rho_{\mathbb{H}^2}(z).\tag{17}$$
> **Step 3 — unfold the conjugacy-class sum over cosets.** Enumerate $[\tau^m]_{\mathrm{conj}}$ by cosets: each $h=r\tau^m r^{-1}$ for a unique $r\in\Gamma/\langle\tau\rangle$. Using $\Gamma$-invariance of the kernel twice, $p^E_{\mathbb{H}^2}(t,z,r\tau^m r^{-1}z)=p^E_{\mathbb{H}^2}(t,r^{-1}z,\tau^m r^{-1}z)$ (apply $h=r^{-1}$ to both slots). Substituting $w=r^{-1}z$ (an isometry, so $d\rho$ is preserved) gives, for each coset,
> $$\int_F p^E_{\mathbb{H}^2}(t,z,r\tau^m r^{-1}z)\,d\rho_{\mathbb{H}^2}(z)=\int_{r^{-1}F}p^E_{\mathbb{H}^2}(t,w,\tau^m w)\,d\rho_{\mathbb{H}^2}(w).$$
> Summing over the cosets $r\in\Gamma/\langle\tau\rangle$ and using that the regions $r^{-1}F$ are disjoint and tile,
> $$\sum_{r\in\Gamma/\langle\tau\rangle}\int_{r^{-1}F}p^E_{\mathbb{H}^2}(t,w,\tau^m w)\,d\rho_{\mathbb{H}^2}(w)=\int_{\bigcup_r r^{-1}F}p^E_{\mathbb{H}^2}(t,w,\tau^m w)\,d\rho_{\mathbb{H}^2}(w).\tag{18}$$
> **Step 4 — replace the tiled union by the strip.** Because $\Gamma=\bigsqcup_{r}r\langle\tau\rangle$ (cosets partition $\Gamma$), the union $\bigcup_r r^{-1}F$ is a fundamental region for the subgroup $\langle\tau\rangle$. The integrand $w\mapsto p^E_{\mathbb{H}^2}(t,w,\tau^m w)$ is $\langle\tau\rangle$-invariant: for $k\in\mathbb{Z}$, $p^E_{\mathbb{H}^2}(t,\tau^k w,\tau^m\tau^k w)=p^E_{\mathbb{H}^2}(t,\tau^k w,\tau^k\tau^m w)=p^E_{\mathbb{H}^2}(t,w,\tau^m w)$ (using $\tau^k\tau^m=\tau^m\tau^k$ and $\Gamma$-invariance). A $\langle\tau\rangle$-invariant function has the *same* integral over any fundamental region of $\langle\tau\rangle$, so we may replace $\bigcup_r r^{-1}F$ by the strip $\mathcal F_\tau=\{1\le\operatorname{Im}z<e^{\ell_\gamma}\}$ of the same period. This yields
> $$\mu^E_X(C_X(\gamma^m))=\int_0^\infty\frac{dt}{t}\int_{\mathcal F_\tau}p^E_{\mathbb{H}^2}(t,z,\tau^m z)\,d\rho_{\mathbb{H}^2}(z).\qquad\blacksquare$$
> *(This is the paper's two-step proof — "isolating the conjugacy class" and "unfolding to the fundamental strip" — with the two uses of $\Gamma$-invariance written out, the isometry substitution's Jacobian noted, and the $\langle\tau\rangle$-invariance of the integrand verified explicitly.)*

---

## §3.1 — Subordinate cases: closed-form masses

Specialising Theorem 3.2 to a [[Def - Subordinate Brownian Loop Measure|subordinate Brownian loop measure]] ($p^E_{\mathbb{H}^2}=p^\phi_{\mathbb{H}^2}$) and expanding $p^\phi$ by subordination gives a double integral in $(t,s)$; [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]] collapses the $t$-integral into the [[Def - Weighted Potential Measure|weighted potential measure]] $V_\phi$. Write $L:=m\ell_\gamma$ throughout. The one geometric input is a heat-kernel integral over the strip, due to Wang–Xue.

> [!cite]- External input — Wang–Xue strip integral (Lemma 3.4)
> **Statement (typed):** for the Brownian heat kernel $p_{\mathbb{H}^2}$ on $\mathbb{H}^2$, every $s>0$ and $m\ge1$ (with $L=m\ell_\gamma$),
> $$\int_{\mathcal F_\tau}p_{\mathbb{H}^2}(s,z,e^{L}z)\,d\rho_{\mathbb{H}^2}(z)=\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}.$$
> **Why it's true (intuition):** on $\mathbb{H}^2$ the heat kernel depends only on distance, and $d(z,e^Lz)$ is minimised along the axis where it equals $L$ (the geodesic length); the Gaussian factor $e^{-L^2/4s}$ is the leading "cost" of travelling that distance, $e^{-s/4}$ is the curvature/bottom-of-spectrum correction ($1/4=(\frac12)^2$ is the spectral gap of $\mathbb{H}^2$), and $\ell_\gamma/(2\sinh(L/2))$ is the geometric volume factor from integrating a distance-only kernel across the strip. **Source:** Wang–Xue [WX25]; a self-contained derivation uses the explicit $\mathbb{H}^2$ heat kernel and Fermi (distance-along/across-axis) coordinates on the strip. Take on faith with the stated form; the paper cites it.

> **Theorem 3.5 (mass of a subordinate loop class).** For a Bernstein $\phi$ (Assumption 2.3), $\gamma\in\mathcal P_X$, $m\ge1$,
> $$\mu^\phi_X(C_X(\gamma^m))=\frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty\frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(ds),\qquad L=m\ell_\gamma.$$

> [!note]- Proof of Theorem 3.5
> Theorem 3.2 with $p^E=p^\phi_{\mathbb{H}^2}$ and the subordination formula $p^\phi_{\mathbb{H}^2}(t,z,w)=\int_{[0,\infty)}p_{\mathbb{H}^2}(s,z,w)\psi^\phi_t(ds)$ give
> $$\mu^\phi_X(C_X(\gamma^m))=\int_0^\infty\frac{dt}{t}\int_{\mathcal F_\tau}\int_{[0,\infty)}p_{\mathbb{H}^2}(s,z,\tau^m z)\,\psi^\phi_t(ds)\,d\rho_{\mathbb{H}^2}(z).$$
> Do the spatial integral first (Tonelli, non-negative integrand): by the Wang–Xue input it equals $\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-s/4}e^{-L^2/4s}}{2\sqrt{\pi s}}$, independent of $z$. The remaining double integral in $(t,s)$ is $\int_0^\infty\frac{dt}{t}\int_{[0,\infty)}h(s)\,\psi^\phi_t(ds)$ with $h(s)=\frac{e^{-s/4}e^{-L^2/4s}}{2\sqrt{\pi s}}$; [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]]/Def 2.9 collapse it to $\int_{(0,\infty)}h(s)\,V_\phi(ds)$, giving the claim. $\blacksquare$

**Definition 3.6 (the loop-length integral).** Isolate $I_\phi(L):=\int_0^\infty\frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(ds)$, so $\mu^\phi_X(C_X(\gamma^m))=\frac{\ell_\gamma}{2\sinh(L/2)}\,I_\phi(L)$, $L=m\ell_\gamma$. Stub: [[Def - The Loop-Length Integral]]. The whole of §4–5 studies $I_\phi$; here we evaluate it for the concrete processes, using one elementary integral.

> [!recall]- The Gaussian-type integral identity
> **Formally:** for $a,b>0$, $\displaystyle\int_0^\infty s^{-3/2}e^{-as-b/s}\,ds=\sqrt{\frac{\pi}{b}}\;e^{-2\sqrt{ab}}$.
> **In words:** the standard "heat-kernel in disguise" integral; it is why every closed-form mass below is an exponential in $L$.
> **Proof (short):** substitute $s=\sqrt{b/a}\,u$ to reduce to $\int_0^\infty u^{-3/2}e^{-\sqrt{ab}(u+1/u)}\,du$; then $u\mapsto1/u$ shows $\int_0^\infty u^{-3/2}e^{-c(u+1/u)}du=\int_0^\infty u^{-1/2}e^{-c(u+1/u)}du$, and their average, with $w=\sqrt u-1/\sqrt u$ (so $dw=\frac12(u^{-1/2}+u^{-3/2})du$ and $u+1/u=w^2+2$), becomes $\int_{-\infty}^\infty e^{-c(w^2+2)}dw=\sqrt{\pi/c}\,e^{-2c}$. Back-substituting $c=\sqrt{ab}$ and the $s$-scaling gives $\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$. (This is the standard evaluation; see e.g. Gradshteyn–Ryzhik 3.471.)

**Case computations** (each $V_\phi$ from Example 2.10):

- **Brownian ($\phi=\lambda$, $V_\phi=\frac{ds}{s}$).** $I_{\mathrm{BM}}(L)=\int_0^\infty\frac{e^{-s/4}e^{-L^2/4s}}{2\sqrt\pi\,s^{3/2}}\,ds=\frac{1}{2\sqrt\pi}\sqrt{\frac{\pi}{L^2/4}}\,e^{-2\sqrt{(1/4)(L^2/4)}}=\frac{1}{2\sqrt\pi}\cdot\frac{2\sqrt\pi}{L}\,e^{-L/2}=\frac{e^{-L/2}}{L}$ (identity with $a=\frac14$, $b=\frac{L^2}{4}$, so $2\sqrt{ab}=L/2$). Hence
$$\mu_X(C_X(\gamma^m))=\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-L/2}}{L}=\frac{\ell_\gamma}{L}\cdot\frac{e^{-L/2}}{2\sinh(L/2)}=\frac1m\cdot\frac{1}{e^{L}-1},$$
using $\ell_\gamma/L=1/m$ and $e^{-L/2}/(2\sinh(L/2))=e^{-L/2}/(e^{L/2}-e^{-L/2})=1/(e^{L}-1)$. This recovers Wang–Xue [WX25].
- **Killing ($\phi=\lambda+\kappa$, $\kappa\ge0$, $V_\phi=e^{-\kappa s}\frac{ds}{s}$).** Same identity with $a=\frac14+\kappa$, $b=\frac{L^2}{4}$: $I_\kappa(L)=\frac{e^{-L\sqrt{1/4+\kappa}}}{L}$, so
$$\mu^\kappa_X(C_X(\gamma^m))=\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-L\sqrt{1/4+\kappa}}}{L}=\frac1m\cdot\frac{e^{(\frac12-\sqrt{1/4+\kappa})L}}{e^{L}-1},$$
exactly Lemonde–Wang [LW26]; $\kappa=0$ recovers the Brownian formula.
- **$\alpha$-stable ($\phi=\lambda^{\alpha/2}$, $V_\phi=\frac\alpha2\frac{ds}{s}$).** $I_\alpha(L)=\frac\alpha2 I_{\mathrm{BM}}(L)=\frac\alpha2\cdot\frac{e^{-L/2}}{L}$, so $\mu^\alpha_X(C_X(\gamma^m))=\frac\alpha2\,\mu_X(C_X(\gamma^m))$ — just a constant multiple of the Brownian answer. This is forced by scale-invariance: stable subordinators are the self-similar ones and $dt/t$ is scale-invariant, so $V_\phi$ can only be a constant times $ds/s$; the geometry drops out. **Breaking scale-invariance** (e.g. shifting to $(\Delta+\kappa)^{\alpha/2}$, the *shifted $\alpha$-stable* case, giving $V_\phi=\frac\alpha2 e^{-\kappa s}\frac{ds}{s}$ and $\mu=\frac\alpha2\cdot\frac1m\cdot\frac{e^{(\frac12-\sqrt{1/4+\kappa})L}}{e^L-1}$) is what makes the decomposition see the geometry again.

**Remark 3.7 (the range $\kappa\ge-\frac14$).** For $\kappa\in[-\frac14,0)$, $\phi(\lambda)=\lambda+\kappa$ is no longer Bernstein (negative killing), but formula for $\mu^\kappa_X$ still makes sense analytically. Writing the **spectral parameter** $\mathfrak s=\frac12+\sqrt{\frac14+\kappa}$ (⚠️ the paper calls this $s$; here $\mathfrak s$, to avoid clashing with the subordination variable $s$), the condition $\kappa\ge-\frac14$ is exactly what keeps $\mathfrak s$ real, with $\kappa=-\frac14\Rightarrow\mathfrak s=\frac12$ — the bottom of the $L^2$-spectrum of $\mathbb{H}^2$. The integral $I_\kappa$ converges throughout $[-\frac14,\infty)$. This $\mathfrak s\leftrightarrow\kappa$ dictionary $\kappa=\mathfrak s(\mathfrak s-1)$ is the bridge to the Selberg zeta variable in §4.

---

## §3.2 — Quantum-mechanical digression (physics motivation)

This subsection is motivation, not new theorems; it explains *why* the killed loop measure equals a partition function, which §5 makes rigorous. It is safe to skim on a first pass.

> [!recall]- Wick rotation, Feynman–Kac, Schwinger proper time
> **Wick rotation:** replacing real time $t$ by imaginary time $t=-i\tau$ turns the Schrödinger unitary group $e^{-it\hat H/\hbar}$ into the contraction semigroup $e^{-\tau\hat H/\hbar}$ (well-defined for $\tau\ge0$ since $\hat H\ge0$); the "Euclidean time" $\tau$ is the diffusion time $t$ of §2.
> **Feynman–Kac formula (typed):** for a killing potential $V\ge0$, the killed heat kernel is $p_V(t,x,y)=\int_{C([0,t];X)}e^{-\int_0^t V(\omega(r))\,dr}\,\mathbb{W}^t_{x\to y}(d\omega)$ — each Brownian bridge weighted by its survival probability. For $V\equiv\kappa$ this is $e^{-\kappa t}p(t,x,y)$, recovering Example 2.6.
> **Schwinger proper-time:** $-\log\det(\Delta_X+\kappa)=\int_0^\infty\frac{dt}{t}e^{-\kappa t}\operatorname{Tr}(e^{-t\Delta_X})$, expressing a determinant as a $\frac{dt}{t}$-integral of the heat trace with killing weight — exactly the structure of the killed loop measure.
> **In words:** statistical mechanics (heat) and quantum mechanics (waves) are the same equations in imaginary time; Feynman–Kac writes the killed kernel as a path integral; Schwinger's formula is the bridge to §5's determinant. See the external inputs; full treatment of the determinant is [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5]].

The upshot the paper draws: for a free real scalar field of mass $\sqrt\kappa$ on $X$, the Gaussian path integral gives the partition function $Z^\kappa_X\propto\det(\Delta_X+\kappa)^{-1/2}$, and the Schwinger representation identifies $-\log\det(\Delta_X+\kappa)=|\mu^\kappa_X|_{\mathrm{reg}}$ (the **regularised total mass** of the killed loop measure — the divergent contractible/peripheral part renormalised, §5). Thus $Z^\kappa_X\propto\exp(\frac12|\mu^\kappa_X|_{\mathrm{reg}})$: the scalar partition function is, up to normalisation, the exponential of half the regularised total loop mass, the $\frac12$ being the power $\det^{-1/2}$ of one real field. ⚠️ *Intuition/heuristic (path-integral level); made rigorous only after §5's regularisation. The "$Dω\,e^{-S[\omega]}$" path integral is formal (no Lebesgue measure on paths), the rigorous content being Feynman–Kac.*

---

## §3.3 — The loop soup and its Poissonian structure

Any σ-finite measure can be the intensity of a Poisson process, so the class-masses become means of Poisson counts — upgrading expectations to distributions.

> [!recall]- Poisson point process / loop soup
> **Formally:** the [[Def - Poisson Point Process and the Loop Soup|Poisson point process]] $\mathcal L_c$ with intensity $c\,\mu^\phi_X$ is a random countable set of loops with $N_A=\#\{\eta\in\mathcal L_c:\eta\in A\}\sim\mathrm{Poisson}(c\,\mu^\phi_X(A))$ for each measurable $A$ with finite mass, and independent counts over disjoint $A$'s. (For jump processes, use the marked-loop process on which classes are measurable.)
> **In words:** scatter loops at random so each region holds a Poisson-many, disjoint regions independent; "mean = mass" is built in. See [[Def - Poisson Point Process and the Loop Soup]].

> **Proposition 3.8 (Poissonian structure).** For $\gamma\in\mathcal P_X$ and $m\ge1$, the number of soup loops in $C_X(\gamma^m)$ is Poisson of mean $c\,\mu^\phi_X(C_X(\gamma^m))$; for finitely many pairwise-distinct classes these counts are jointly independent.
> **Proof.** Distinct free homotopy classes are disjoint measurable sets of loops, so the two claims are exactly the Poisson-count and independent-scattering axioms of the [[Def - Poisson Point Process and the Loop Soup|Poisson process]]. $\blacksquare$

Stub: [[Prop - Poissonian Structure of Homotopy Classes]]. So each closed-form mass from §3.1 is literally the mean number of soup loops of that type.

---

## §3.4 — Length-spectrum identities

The two fundamental properties of §2 (restriction, conformal invariance) yield relations between the geodesic-length spectra of different surfaces.

> [!recall]- Polar set / logarithmic capacity
> **Formally:** a Borel set $P\subset X$ is **polar** for a process if from every start it a.s. never hits $P$ at a positive time; for Brownian motion on a surface, $P$ is polar iff it has zero **logarithmic capacity** in every chart (in particular every singleton, hence every countable set, is polar). Polar sets form a σ-ideal (closed under subsets and countable unions). A killing rate does not change paths, so $\phi(\lambda)=\lambda+\kappa$ has the same polar sets.
> **In words:** a polar set is invisible to the random path — small enough that the particle never lands on it. Removing one does not change loop masses. **Source:** Blumenthal–Getoor, potential theory of Markov processes.

Taking $P$ a closed discrete (hence countable, polar) set, restriction gives $\mu^\kappa_{X,g}(C_X(\gamma^m))=\mu^\kappa_{X\setminus P,\,g}(C_X(\gamma^m))$ — puncturing along $P$ leaves the killed loop mass unchanged, **provided the metric $g$ is unchanged**. This is weaker than the Brownian case, where conformal invariance additionally lets one swap $g$ for the *complete hyperbolic* metric $g'$ of $X\setminus P$ (with a cusp at each puncture), turning the identity into a genuine comparison of length spectra. For a subordinate process the swap fails: a conformal change rescales $\Delta_{X,g'}=e^{-2\sigma}\Delta_{X,g}$, and $\phi$ does not commute with this rescaling ($\phi(e^{-2\sigma}\Delta)\ne e^{-2\sigma}\phi(\Delta)$ unless $\phi(\lambda)=c\lambda$).

> [!cite]- External input — Wang–Xue length-spectrum identity (Theorem 3.9)
> **Statement (typed):** for a complete hyperbolic surface $X$ (without boundary, possibly infinite type, cusps/funnels) and a non-empty closed polar $P\subset X$, with $X'=X\setminus P$ given its unique complete hyperbolic metric, for every $\gamma\in\mathcal P_X$, $m\ge1$:
> $$\frac1m\cdot\frac{1}{e^{m\ell_\gamma}-1}=\sum_{\substack{\gamma'\in\mathcal P_{X'},\,m'\ge1\\ \gamma'^{m'}\simeq_X\gamma^m}}\frac{1}{m'}\cdot\frac{1}{e^{m'\ell_{\gamma'}}-1},$$
> where $\simeq_X$ is free homotopy in $X$ and $\ell_\gamma,\ell_{\gamma'}$ are primitive lengths in $X,X'$.
> **Why it's true:** both sides are the Brownian loop mass of the class, computed on $X$ (left, via §3.1.1) and on the conformally-equivalent punctured surface $X'$ (right, where the class splits into several $X'$-classes); conformal invariance forces equality. **Source:** Wang–Xue [WX25, Thm 4.2]. The paper states it for context; the notes cite it.

**The marked length spectrum, recovered.**

> **Definition 3.10 (marked length spectrum).** $\mathrm{MLS}:C_X(\gamma^m)\mapsto\inf_{\eta\in C_X(\gamma^m)}\ell_g(\eta)$, the shortest length in each non-trivial free homotopy class; on a hyperbolic surface the infimum is attained by the unique geodesic, so $\mathrm{MLS}(C_X(\gamma^m))=m\ell_\gamma$.

Stub: [[Def - Marked Length Spectrum]]. The *marking* — which class realises which length — matters: isospectral-but-non-isometric surfaces exist (Vignéras), so the bare set of lengths does not determine $X$, but (Otal, Croke, in 2D) the *marked* spectrum does.

> **Proposition 3.11 (loop masses ⇒ length).** For every $\gamma\in\mathcal P_X$, $\ \ell_\gamma=\log\!\big(1+\frac{1}{\mu_X(C_X(\gamma))}\big)$. For $\phi=\lambda+\kappa$ with $\kappa\ge-\frac14$, $\mu^\kappa_X(C_X(\gamma))$ is strictly decreasing in $\ell_\gamma$, so again determines it. Hence in either case the loop masses determine $\mathrm{MLS}$.
> **Proof.** By §3.1.1, $\mu_X(C_X(\gamma))=1/(e^{\ell_\gamma}-1)$ (case $m=1$, $L=\ell_\gamma$); solving, $e^{\ell_\gamma}-1=1/\mu_X(C_X(\gamma))$, i.e. $\ell_\gamma=\log(1+1/\mu_X(C_X(\gamma)))$. For the killed case, $\mu^\kappa_X(C_X(\gamma))=e^{(\frac12-\sqrt{1/4+\kappa})\ell_\gamma}/(e^{\ell_\gamma}-1)$; its logarithmic derivative in $\ell_\gamma$ is $\big(\frac12-\sqrt{\frac14+\kappa}\big)-\frac{e^{\ell_\gamma}}{e^{\ell_\gamma}-1}<\frac12-1<0$ (the first bracket is $\le\frac12$ since $\kappa\ge-\frac14\Rightarrow\sqrt{1/4+\kappa}\ge0$, and $\frac{e^{\ell}}{e^\ell-1}>1$), so the mass strictly decreases in $\ell_\gamma$ and is injective. The same computations hold for every $m$. $\blacksquare$

> **Corollary 3.12 (loop masses determine the surface).** If two hyperbolic metrics $g_1,g_2$ on a closed surface $X$ give equal killed loop masses $\mu^\kappa_{X,g_1}(C_X(\gamma^m))=\mu^\kappa_{X,g_2}(C_X(\gamma^m))$ for all classes (fixed $\kappa\ge-\frac14$), then $(X,g_1)\cong(X,g_2)$ by an isometry isotopic to the identity — the same point of Teichmüller space.
> **Proof.** By Prop 3.11 the masses determine the marked length spectrum with its marking; equal masses ⇒ equal marked spectra. Hyperbolic metrics are negatively curved, so by Otal–Croke the marked length spectrum determines the metric up to an isometry isotopic to the identity. $\blacksquare$

Stubs: [[Prop - Loop Masses Determine the Length Spectrum]], [[Cor - Loop Masses Determine the Hyperbolic Surface]]. Continue to [[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4]], which sums these class-masses into a zeta function.

---

## Section verification log (§3)

**Verified.** Theorem 3.2 proof rewritten gap-free (both $\Gamma$-invariance uses, the isometry substitution, and the $\langle\tau\rangle$-invariance of the integrand made explicit). The §3.1 closed-form masses (Brownian $1/m(e^L-1)$, killed, $\alpha$-stable) reproduced in full via the Gaussian-type integral $\int_0^\infty s^{-3/2}e^{-as-b/s}ds=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$, which is proved here. Prop 3.8 and Prop 3.11/Cor 3.12 proved in full.
**Flagged / uncertain.** ⚠️ The paper's Remark 3.7 spectral parameter is written $s$, colliding with the subordination variable $s$; renamed $\mathfrak s$ here. The jump-process class definition (Remark 3.1) is a definition, not recovered from the càdlàg path — flagged at §3.0.
**Intuition not yet formalised.** §3.2 (quantum digression) is physics motivation: the partition-function identity $Z^\kappa_X\propto\exp(\frac12|\mu^\kappa_X|_{\mathrm{reg}})$ is heuristic until §5 defines the regularised mass; the formal path integral $Dω\,e^{-S}$ is not a measure. Both flagged. The Wang–Xue strip integral (Lemma 3.4) and length-spectrum identity (Thm 3.9) are external inputs, stated + typed + cited, not re-proved (the strip integral's derivation is sketched).
