---
type: paper-section
paper: "BH26"
subject: brownian-loops
section: "3, 3.1, 3.4"
prereqs:
  - "Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces"
  - "Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces"
  - "Constr - The Periodised Kernel"
  - "Constr - Standard-Form Representative and the Fundamental Strip"
tags: [paper, probability, hyperbolic-geometry, loop-measures]
---

> [!info] Part of [[Map - Brownian Loops on Homotopy and Homology Classes]]

# Signature

| symbol | type |
|---|---|
| $\Gamma$ | torsion-free Fuchsian $\subseteq\mathrm{PSL}(2,\mathbb{R})$; $X=\Gamma\backslash\mathbb{H}^2$ geometrically finite; $\pi:\mathbb{H}^2\to X$ |
| $(\mathcal{E},\mathcal{F})$ | $\Gamma$-invariant regular symmetric Dirichlet form on $L^2(\mathbb{H}^2,\rho)$ |
| $p^{\mathcal{E}}_{\mathbb{H}^2}$ | density; $p^{\mathcal{E}}_{\mathbb{H}^2}(t,hz,hw)=p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,w)$ for $h\in\Gamma$ |
| $p^{\mathcal{E}}_X$ | $=\sum_{h\in\Gamma}p^{\mathcal{E}}_{\mathbb{H}^2}(t,\tilde z,h\tilde w)$ — the periodisation (11) |
| $h_\omega$ | $\in\Gamma$; the deck transformation recorded by a rooted **continuous** loop |
| $\mathcal{P}_X$ | primitive oriented closed geodesics; $\ell_\gamma>0$ |
| $\tau$ | $z\mapsto e^{\ell_\gamma}z$; $F_\tau=\{1\leq\operatorname{Im}z<e^{\ell_\gamma}\}$ |
| $[\tau^m]_{\mathrm{conj}}$ | $=\bigsqcup_{r\in\Gamma/\langle\tau\rangle}\{r\tau^mr^{-1}\}$; $C_\Gamma(\tau^m)=\langle\tau\rangle$ |
| $L$ | $:=m\ell_\gamma\in(0,\infty)$ — **real** in §3–§6 |
| $I_\phi$ | $(0,\infty)\to(0,\infty]$; Definition 3.6 |
| $P$ | $\subseteq X$ closed discrete, hence [[Def - Polar Set\|polar]] — §3.4 only |
| $\kappa,\alpha$ | $\kappa\geq-\tfrac14$; $\alpha\in(0,2)$ |

**Standing hypotheses of §3.** All free homotopy classes are **non-trivial** and **non-peripheral** ([[Def - Geometrically Finite Surfaces, Cusps and Funnels|(D3),(D4)]]). $\Gamma$ satisfies [[Def - Free and Properly Discontinuous Action|(D1),(D2)]].

---

# The lifting dictionary

Three pages, in this order.

| page | content |
|---|---|
| [[Def - Deck Transformations and the Lift of a Rooted Loop]] | unique lift of a **continuous** rooted loop; $h_\omega$ defined by $\tilde\omega(t)=h_\omega\tilde x$; $h_\omega=1\iff$ contractible; conjugation law under change of lift |
| [[Def - Free Homotopy Class and Conjugacy Class Correspondence]] | the bijection $\{$free classes$\}\leftrightarrow\{$conjugacy classes$\}$; indexing by $(\gamma,m)$; unique closed geodesic of length $m\ell_\gamma$ |
| [[Def - Centraliser and Coset Enumeration of a Conjugacy Class]] | $C_\Gamma(\tau^m)=\langle\tau\rangle$ and $[\tau^m]_{\mathrm{conj}}=\bigsqcup_{r\in\Gamma/\langle\tau\rangle}\{r\tau^mr^{-1}\}$ |

Plus two constructions appearing later as hypotheses: [[Constr - The Periodised Kernel]] and [[Constr - Standard-Form Representative and the Fundamental Strip]].

## Remark 3.1 — jump processes

> [!abstract] Type card — Remark 3.1
> **Given.** **(H1)** $\phi$ with $\nu\neq0$, so sample loops are càdlàg. **(H2)** the periodisation (11). **(H3)** $\gamma,\tau,m$.
>
> **Produces.** A **definition** (13): $\mu^{\mathcal{E}}_X(\mathcal{C}_X(\gamma^m)):=\int_0^\infty\frac{\mathrm{d}t}{t}\int_X\sum_{h\in[\tau^m]_{\mathrm{conj}}}p^{\mathcal{E}}_{\mathbb{H}^2}(t,\tilde z,h\tilde z)\,\mathrm{d}\rho_X(z)$.
>
> **Lets you.** State Theorems 3.5 and 7.2 uniformly — at the price that for jump processes the left side is a definition, not a measured quantity.

Obstruction: unique path lifting requires continuity, so a càdlàg loop has no class and $\mathcal{C}_X(\gamma^m)$ is not measurable in $\mathcal{C}_X$. Justification on the marked space $(B,S)$, and the paper's open question, on [[Constr - Loop Mass in a Homotopy Class for Jump Processes]].

---

# Results

## Theorem 3.2 — the general decomposition

> [!abstract] Type card — Theorem 3.2
> **Given.** **(H1)** $\Gamma$-invariant regular symmetric form with (A1),(A2),(A3). **(H2)** $\gamma\in\mathcal{P}_X$, standard form $\tau$, strip $F_\tau$. **(H3)** $m\geq1$. **(H4)** jump case via (13).
>
> **Produces.** An identity in $[0,\infty]$:
> $$\mu^{\mathcal{E}}_X\big(\mathcal{C}_X(\gamma^m)\big)=\int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau}p^{\mathcal{E}}_{\mathbb{H}^2}\big(t,z,\tau^mz\big)\,\mathrm{d}\rho(z).\tag{14}$$
>
> **Lets you.** Eliminate the $\Gamma$-sum and the quotient geometry; compute upstairs, against one group element, over an explicit band.

**Strategy.** Unfold the class sum over cosets of $\langle\tau\rangle$ using (A1); then swap the reassembled $\langle\tau\rangle$-region for $F_\tau$ by [[Def - Fundamental Region|(I)]]. · Full page: [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]].

## Lemma 3.4 — the strip identity (imported)

> [!abstract] Type card — (WX)
> **Given.** **(P1)** $s>0$; **(P2)** $m\geq1$, $\ell_\gamma>0$, $L=m\ell_\gamma$; **(P3)** $\tau$ in standard form, $F_\tau$; **(P4)** $p_{\mathbb{H}^2}$ the speed-2 kernel.
>
> **Produces.** $\displaystyle\int_{F_\tau}p_{\mathbb{H}^2}(s,z,e^Lz)\,\mathrm{d}\rho(z)=\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}$ — **geometric prefactor $\times$ analytic factor**.
>
> **Lets you.** Discharge the spatial integral of (14), leaving a one-dimensional integral in $t$.

Imported, not proved: [[Ext - Wang–Xue Strip Identity]].

## Theorem 3.5 — the central formula

> [!abstract] Type card — Theorem 3.5
> **Given.** **(H1)** $\phi$ Bernstein with (A2.3). **(H2)** $\gamma\in\mathcal{P}_X$, $\ell_\gamma>0$. **(H3)** $m\geq1$, $L=m\ell_\gamma$. **(H4)** jump case via (13).
>
> **Produces.** $\mu^\phi_X(\mathcal{C}_X(\gamma^m))\in[0,\infty]$:
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)=\frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(\mathrm{d}s).\tag{21}$$
>
> **Lets you.** Replace the double $(t,s)$ integral by one against $V_\phi$; every special case is one substitution.

**Strategy.** Evaluate the spatial integral by (WX), then collapse $\int\mathrm{d}t/t$ into $V_\phi$ by Lemma 2.11. · Full page: [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]].

## Definition 3.6 — isolating the analytic factor

$$I_\phi(L):=\int_0^\infty\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(\mathrm{d}s),\qquad \mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)=\frac1m\cdot\frac{L}{2\sinh(L/2)}\,I_\phi(L).\tag{23,24}$$

See [[Constr - The Weighted Heat-Kernel Integral Iϕ]]. **(24) is the form [[Thm - Selberg Zeta Criterion|Lemma 4.2]] operates on.**

---

# Special cases (§3.1.1–3.1.4)

All four are [[Ext - Gaussian Reciprocal Integral Identity|(GI)]] with $b=L^2/4$ and $a$ shifted by the killing rate.

| $\phi(\lambda)$ | $V_\phi(\mathrm{d}s)$ | $(a,b)$ | $I_\phi(L)$ | $\mu^\phi_X(\mathcal{C}_X(\gamma^m))$ |
|---|---|---|---|---|
| $\lambda$ | $\mathrm{d}s/s$ | $(\tfrac14,\tfrac{L^2}4)$ | $e^{-L/2}/L$ | $\dfrac1m\cdot\dfrac{1}{e^L-1}$ |
| $\lambda+\kappa$ | $e^{-\kappa s}\mathrm{d}s/s$ | $(\tfrac14+\kappa,\tfrac{L^2}4)$ | $e^{-L\sqrt{1/4+\kappa}}/L$ | $\dfrac1m\cdot\dfrac{e^{(1-s)L}}{e^L-1}$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ |
| $\lambda^{\alpha/2}$ | $\tfrac\alpha2\mathrm{d}s/s$ | $(\tfrac14,\tfrac{L^2}4)$ | $\tfrac\alpha2 e^{-L/2}/L$ | $\tfrac\alpha2\cdot\dfrac1m\cdot\dfrac{1}{e^L-1}$ |
| $(\lambda+\kappa)^{\alpha/2}$ | $\tfrac\alpha2e^{-\kappa s}\mathrm{d}s/s$ | $(\tfrac14+\kappa,\tfrac{L^2}4)$ | $\tfrac\alpha2 e^{-L\sqrt{1/4+\kappa}}/L$ | $\tfrac\alpha2\cdot\dfrac1m\cdot\dfrac{e^{(1-s)L}}{e^L-1}$ |

Row 1 recovers Wang–Xue [WX25, Lemma 3.2]; row 2 recovers Lemonde–Wang [LW26, Lemma 3.1]. Calculations: [[Constr - The Weighted Heat-Kernel Integral Iϕ]].

> [!note] Remark 3.7 — the range $\kappa\geq-\tfrac14$
> For $\kappa>0$: $\mu^\kappa_X$ is the loop measure of Brownian motion killed at rate $\kappa$, generator a Schrödinger operator with constant potential $+\kappa$.
> For $\kappa\in[-\tfrac14,0)$: $\phi(\lambda)=\lambda+\kappa$ is **not** Bernstein (negative killing rate), but (26) still converges and makes analytic sense.
> The cutoff is spectral, not technical: $\kappa\geq-\tfrac14\iff s=\tfrac12+\sqrt{\tfrac14+\kappa}\in\mathbb{R}$, and $\kappa=-\tfrac14$ gives $s=\tfrac12=\inf\operatorname{spec}_{L^2}\Delta_{\mathbb{H}^2}$.

> [!warning] §3.1.3 — the stable case collapses
> $$\mu^\alpha_X\big(\mathcal{C}_X(\gamma^m)\big)=\tfrac\alpha2\,\mu_X\big(\mathcal{C}_X(\gamma^m)\big).$$
> **Structural, not accidental.** Self-similar subordinators $=$ stable ones; $\mathrm{d}t/t$ is scale-invariant; the only measures on $(0,\infty)$ compatible with both scalings are constant multiples of $\mathrm{d}s/s$ — [[Constr - The Weighted Potential Measure Vϕ|(P2)]]. So **no scale-invariant subordination can say anything about the geometry of $X$ that Brownian motion does not.** Row 4 breaks the scaling — but produces the *killing* profile times $\alpha/2$, so a genuinely different dependence on $L$ remains unfound.

---

# §3.4 Length-spectrum identities

| statement | hypotheses | conclusion |
|---|---|---|
| **(S1)** restriction survives | $P$ closed discrete hence [[Def - Polar Set\|polar]]; $\phi(\lambda)=\lambda+\kappa$ | $\mu^\kappa_{X,g}(\mathcal{C}_X(\gamma^m))=\mu^\kappa_{X\setminus P,g}(\mathcal{C}_X(\gamma^m))$, $g$ the **ambient** metric restricted |
| **(S2)** conformal invariance fails | $\phi(\lambda)\neq c\lambda$ | $\phi(e^{-2\sigma}\Delta_{X,g})\neq e^{-2\sigma}\phi(\Delta_{X,g})$; the metric cannot be swapped |
| **(WXL)** the full identity | pure Brownian motion; (P1)–(P5) of [[Ext - Wang–Xue Length-Spectrum Identity]] | $\frac1m\frac{1}{e^{m\ell_\gamma}-1}=\sum_{\gamma'^{m'}\simeq_X\gamma^m}\frac{1}{m'}\frac{1}{e^{m'\ell_{\gamma'}}-1}$ |

## §3.4.1 — recovering the marked length spectrum

> [!abstract] Type card — Proposition 3.11, Corollary 3.12
> **Given.** **(H1)** $\kappa\geq-\tfrac14$. **(H2)** the masses over all classes. For 3.12 additionally: **(H3)** $X$ **closed**, $g_1,g_2$ hyperbolic, masses equal in every class.
>
> **Produces.** 3.11: $\ell_\gamma=\log(1+1/\mu_X(\mathcal{C}_X(\gamma)))$ for $\kappa=0$; strict monotonicity in $\ell_\gamma$ for general $\kappa$; hence $\mathrm{MLS}$ is determined. 3.12: an isometry isotopic to $\mathrm{id}_X$, i.e. the same point of $\mathcal{T}(X)$.
>
> **Lets you.** Read the loop masses as a complete invariant of the marked hyperbolic structure.

**Strategy (3.11).** Invert the Brownian formula; for general $\kappa$ bound $\frac{\mathrm{d}}{\mathrm{d}\ell_\gamma}\log\mu^\kappa_X$ above by $\tfrac12-1<0$. **Strategy (3.12).** 3.11 gives equality of $\mathrm{MLS}$ with the identity marking; apply [[Ext - Otal–Croke Marked Length Spectrum Rigidity|(OC)]].

Pages: [[Def - Marked Length Spectrum]], [[Thm - Loop Masses Determine the Marked Length Spectrum]], [[Thm - Loop Masses Determine the Hyperbolic Surface]].

---

# Exports

**(E1)** $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=\frac1m\frac{e^{(1-s)L}}{e^L-1}$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$, $L=m\ell_\gamma$. **The single most reused formula in the paper.** → §4, §5, §6.

**(E2)** The general shape $\frac{C}{m}\frac{e^{(1-s)L}}{e^L-1}$, with $(C,s)$ from the table. → [[Thm - Selberg Zeta Criterion|Lemma 4.2]].

**(E3)** The unfolding move: class sum → cosets of the cyclic centraliser → change of fundamental region. → §7, verbatim.

**(E4)** Homotopy classes are **not** measurable for jump processes; all $\alpha$-stable statements are about a defined quantity on a marked space. → §3.3, §5.1(iii), §7.

**(E5)** $\alpha$-stable subordination adds nothing geometric, for a reason. → §3.1.3 warning above.

---

# Commentary

> [!note]- Commentary (skippable)
> This is the heart of the paper: everything before builds a measure on loops, everything after analyses the answer computed here.
>
> Why the question is answerable at all: a hyperbolic surface hands you a dictionary between topology and group theory, and the loop measure is built from a kernel that respects it. Topologically, free homotopy classes of oriented closed curves on $X$ correspond to conjugacy classes in $\Gamma$. Analytically, the kernel downstairs is a $\Gamma$-indexed sum. So restricting the sum to a conjugacy class **is** restricting the loop measure to a free homotopy class. That coincidence is the whole mechanism.
>
> What remains is a computation with exactly two steps, both recurring verbatim in §7. **Unfold:** the class is enumerated without repetition by $\Gamma/\langle\tau\rangle$, and translating a fundamental region for $\Gamma$ by those cosets reassembles a fundamental region for the *cyclic* group $\langle\tau\rangle$ — so the class sum and the region enlargement cancel. **Swap the region:** the integrand is $\langle\tau\rangle$-invariant, so any fundamental region gives the same answer, and the horizontal band $F_\tau$ is where an explicit computation is possible.
>
> §3.4 is a coda and its content is largely negative. The two structural properties of §2.1 combine, for pure Brownian motion, into a genuine identity between the length spectra of two *different* hyperbolic surfaces. For any nonlinear subordination the identity degenerates, and the reason is exact: a conformal change rescales the Laplacian, and $\phi$ does not commute with that rescaling unless $\phi$ is linear. Subordination and conformal geometry are simply incompatible except in the linear case — which is precisely the observation §7 opens by exploiting.
>
> Next, in any order: [[§4 Zeta Identities and Finiteness of the Total Mass]] (analytic payoff), [[§3.3 The Loop Soup and its Poissonian Structure]] (needed before §6.2), [[§3.2 Euclidean Quantum Mechanics and the Path Integral]] (skippable digression), [[§7 Brownian Loops on Hyperbolic 3-Manifolds]].
