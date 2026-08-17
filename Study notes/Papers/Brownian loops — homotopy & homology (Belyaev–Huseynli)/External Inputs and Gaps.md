---
type: paper-imports
paper: "BH26"
subject: brownian-loops
tags: [paper, imports, gaps, self-contained]
---

> [!info] Optional reference. Every result below is already stated, in full and at point of use, inside the section page that needs it (as a `> [!import]-` box). This page is the consolidated ledger: the same statements plus **source** and **gap-depth**, so you can see the whole floor at once. Part of [[Map - Brownian Loops on Homotopy and Homology Classes]].

# What "gap" means here

An **import** is a result the paper invokes without proving. It is **not a gap** if a reader with the anchor set (see [[Anchors and Prerequisites]]) could reconstruct it — those are labelled *anchor-level* below. It **is a gap** if it needs machinery outside the anchor set (hyperbolic geometry, the Selberg trace formula, microlocal analysis, …); a gap is honest and usable — you assume its stated conclusion and every proof using it still typechecks.

**The floor holds because each import states precondition→conclusion exactly.** A reader who grants every conclusion below can follow every proof in the note-set.

---

# Genuine gaps, ranked by how much rests on them

| # | import | Says (conclusion) | source | used at | closes with |
|---|---|---|---|---|---|
| 1 | **Wang–Xue strip identity** | $\int_{F_\tau}p_{\mathbb H^2}(u,w,e^Lw)\,\mathrm d\mathrm{vol}=\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-u/4}e^{-L^2/4u}}{2\sqrt{\pi u}}$ | [WX25, Lem 3.2] | §3 (Thm 3.5) — **underlies the entire paper** | Spectral geometry / hyperbolic analysis; the $\mathbb H^2$ heat kernel has no elementary closed form |
| 2 | **Naud's log-det formula** | $-\log\det{}_\zeta\Delta_X=-\text{Area}(X)E-\gamma_{\mathrm{EM}}+\int_0^1\!\frac{S_X}{t}+\int_1^\infty\!\frac{S_X-1}{t}$ | Naud | §5.1 (Thm 5.1) — deepest of §5.1 | Selberg trace formula + refined prime geodesic theorem |
| 3 | **Borthwick–Judge–Perry** | $\det_0(\Delta_X-s(1-s))=Z_X(s)\,e^{M+Fs(1-s)}\cdot(\text{Barnes }G,\ \Gamma\text{ factors in }\chi,n_C)$ | [BJP] | §5.2 (Thm 5.7) — deepest of §5.2 | Spectral geometry + microlocal (b-calculus) |
| 4 | **Selberg trace formula** (heat form) | $\sum_je^{-t\lambda_j}=[\text{identity}]+S_X(t)$, $S_X$ the geometric length-spectrum sum | Selberg | §5.1 (via Naud) | Automorphic forms / Selberg trace formula |
| 5 | **Prime geodesic theorem** | $N_X(R)=\#\{\gamma:\ell_\gamma\le R\}\sim e^{\delta R}/(\delta R)$ | Huber, Selberg, Naud | §4.4 (finiteness), §5.1 | Automorphic forms / Selberg trace formula |
| 6 | **Meromorphic continuation of $Z_X$, $L_X$** | $Z_X,L_X(\cdot,\chi)$ extend meromorphically to $\mathbb C$; on a closed surface $Z_X$ is entire with a simple zero at $s=1$ | Selberg; Patterson–Perry | §5 (needs $Z_X'(1)$), §6 (naming $L_X$) | Automorphic forms + spectral geometry |
| 7 | **Otal–Croke rigidity** | equal marked length spectra of two negatively-curved closed surfaces ⟹ isometric | Otal (1990), Croke (1990) | §3.4 (Cor 3.12) — sole use | Teichmüller theory (no DAG node) |
| 8 | **Melrose renormalised trace** | the $0$-trace ${}^0\mathrm{Tr}(e^{-t\Delta_X})$ is well defined; $\zeta^0_X$ regular at $0$; $\det_0$ exists, $=\det_\zeta$ when closed | Melrose (b-calculus) | §5.2 (defines $\det_0$) | Microlocal analysis (no DAG node) |
| 9 | **Wang–Xue length-spectrum identity** | puncturing at a polar set relates the two surfaces' length spectra; only a trivial form survives for subordinate diffusions | [WX25, Thm 4.2] | §3.4 | Random conformal geometry / hyperbolic analysis |
| 10 | **Polyakov conformal anomaly** | $\log\det_\zeta\Delta_{e^{2\sigma}g}=-\frac{1}{12\pi}\!\int|\nabla\sigma|^2-\frac{1}{6\pi}\!\int K_0\sigma+\log\frac{\mathrm{vol}_{e^{2\sigma}g}}{\mathrm{vol}_g}+\log\det_\zeta\Delta_g$ | Polyakov (1981) | §5.1.1 (Cor 5.4) — sole use | Spectral / conformal geometry (shallow) |
| 11 | **Uniformisation** (cusped) | each conformal class on a punctured surface has a unique complete hyperbolic metric with cusps | classical | §3.4 (length identity) | Riemann surfaces |
| 12 | **Hodge theorem & period lattice** | $\widehat{H_1(X,\mathbb Z)}\cong\mathrm{Jac}(X)$ (closed $X$), via harmonic $1$-forms with integer periods | classical | §6.2 (Remark 6.6) — decorative | Hodge theory / Riemann surfaces (shallow) |

---

# Imports that are NOT gaps (anchor-level — a reader could reconstruct them)

| import | Says | why not a gap |
|---|---|---|
| **Gaussian reciprocal integral** | $\int_0^\infty u^{-3/2}e^{-au-b/u}\,\mathrm du=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$ ($a,b>0$) | elementary substitution $w=\sqrt a\,u^{1/2}-\sqrt b\,u^{-1/2}$; used six times |
| **Lemma 2.11 collapse** | $\int_0^\infty\frac{\mathrm dt}{t}\int h\,\mathrm d\psi^\phi_t=\int h\,\mathrm dV_\phi$ | Tonelli (anchor) + the definition of $V_\phi$ |
| **Phillips subordination** | $e^{-t\phi(\Delta)}$ has kernel $\int p(u,\cdot,\cdot)\,\psi^\phi_t(\mathrm du)$ | functional calculus / Bochner; anchor-adjacent |
| **Fukushima correspondence** | a regular symmetric Dirichlet form is the form of a symmetric Hunt process (hence a heat kernel) | Dirichlet-form theory; stated, used only to produce a heat semigroup |
| **Feynman–Kac** | $p_V(t,x,y)=\int e^{-\int_0^tV(\omega)}\,W^t_{x\to y}(\mathrm d\omega)$ | anchor (SDEs); only in the §3.2 digression |
| **Poisson point process facts** | $\sigma$-finite intensity ⟹ a PPP; disjoint sets ⟹ independent counts; exponential formula $\mathbb E[\prod e^{F}]=\exp\int(e^F-1)\,\mathrm d\nu$ | anchor (advanced probability); the §3.3/§6.3 engine |
| **Orthogonality of characters** | $\int_{\widehat A}\chi(\beta')\overline{\chi(\beta)}\,\mathrm d\chi=\mathbb 1[\beta'=\beta]$ | anchor (Fourier on $\mathbb Z^r$/$(S^1)^r$); §6.2 inversion |
| **Explicit $\mathbb H^3$ heat kernel** | $p_{\mathbb H^3}(t,z,w)=\frac{1}{(4\pi t)^{3/2}}\frac{u}{\sinh u}e^{-t-u^2/4t}$, $u=d(z,w)$ | classical, elementary in odd dimension; **this is why §7 derives its slab identity instead of importing it** |

---

# The pattern

The gaps cluster in two places, and the note-set makes the cluster visible. **§3's Wang–Xue strip identity** is imported because the $\mathbb H^2$ heat kernel is not elementary — and everything downstream rests on it. **§5's determinant machinery** (Naud, Borthwick–Judge–Perry, Melrose, the trace formula) is imported because zeta-regularised determinants of the Laplacian are a subject of their own. Between them sits the **prime geodesic theorem** and the **continuation of $Z_X$**, both consequences of the Selberg trace formula. Closing that one node — *Automorphic Forms / Selberg Trace Formula* — would discharge imports 2, 4, 5, and half of 6 at once (see [[Anchors and Prerequisites]] for the repair order). Section 7's single computation, by contrast, has **no** gap: the $\mathbb H^3$ kernel is elementary, so its slab identity is derived rather than quoted.
