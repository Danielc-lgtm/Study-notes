---
type: prereq-dag
paper: "BH26"
subject: brownian-loops
tags: [paper, prereq-dag, probability, geometry]
---

# How to read this page

Indentation is dependency: a child is something its parent needs in order to make sense. A leaf marked 🟢 is an **anchor** — a concept coming from a 🟢 node of `Study notes/Prerequisite DAG.md`, or from the background paragraph of `CLAUDE.md`, where the backchain stops because the knowledge is already there. Every non-anchor is a wikilink to a page in this folder or elsewhere in the vault.

The point of the page is a single glance that answers one question: *does this paper bottom out at things I actually know?* An unlinked, unmarked leaf is a bug, and finding one is what this page is for. The last section records the gaps honestly rather than hiding them in the tree.

---

# Anchors this paper stands on

These are the floor. Nothing below them is explained anywhere in the note-set, and nothing needs to be.

- 🟢 **Heat kernel, heat semigroup, and the correspondence with the generator** — from *Analysis of PDEs* (🟢, "strong background") and *Functional Analysis* (🟢, 8/10). Includes: $e^{-t\Delta}$ as a strongly continuous contraction semigroup, its integral kernel as a density against a reference measure, short-time on-diagonal asymptotics $p(t,x,x) \sim 1/(4\pi t)$ on a surface, and the heat trace $\operatorname{Tr}(e^{-t\Delta}) = \int_X p(t,x,x)\,\mathrm{d}\mathrm{vol}$.
- 🟢 **Laplace–Beltrami operator, Riemannian volume measure, conformal rescaling** — from the *Riemannian geometry* strand of `CLAUDE.md`'s background paragraph (the DAG node itself is 🔵, but the owner's stated background is strong here; if that ever stops being true, this is the first line to demote). Includes: $\Delta_g = -\operatorname{div}_g\operatorname{grad}_g$, the behaviour $\Delta_{e^{2\sigma}g} = e^{-2\sigma}\Delta_g$ in two dimensions, geodesics as locally length-minimising curves, and isometries. Vault pages: [[Def - Riemannian Metric]], [[Def - Riemannian Volume Form]], [[Def - Geodesic]], [[Def - Isometry of Riemannian Manifolds]], [[Def - The Hyperbolic Space H^n]].
- 🟢 **Brownian motion, the Brownian bridge, and disintegration by endpoint** — from *SDEs* (🟢, 7/10) and *Advanced Probability* (🟢, 7/10). The one point worth flagging, because the paper leans on it constantly, is that $W^t_{x\to y}$ is the **unnormalised** bridge: it has total mass $p(t,x,y)$, and the conditional law is $W^t_{x\to y}/p(t,x,y)$.
- 🟢 **Self-adjoint operators and the spectral picture** — from *Functional Analysis* (🟢). Includes: non-negative self-adjoint operators, functional calculus $f(A)$, the discrete-versus-continuous spectrum dichotomy, and trace-class operators with Lidskii's theorem. Vault pages: [[Def - Self-Adjoint Operator]], [[Thm - Complex Spectral Theorem]].
- 🟢 **Measure theory: σ-finiteness, pushforward, Tonelli, Radon–Nikodym** — from *Advanced Probability / Measure-Theoretic* (🟢). Vault pages: [[Def - σ-Finite Measure]], [[Thm - Fubini-Tonelli Theorem]], [[Thm - Radon-Nikodym Theorem]]. The paper's manipulations of $\int_0^\infty \frac{\mathrm{d}t}{t}\int\cdots$ are all Tonelli on non-negative integrands; there is never a dominated-convergence subtlety.
- 🟢 **Feynman–Kac** — from *SDEs* (🟢). Used exactly once substantively, in §3.2, to identify $p^V(t,x,y) = \int e^{-\int_0^t V(\omega(r))\,\mathrm{d}r}\,W^t_{x\to y}(\mathrm{d}\omega)$.
- 🟢 **Poisson point processes and the exponential formula** — from *Advanced Probability* (🟢). Any $\sigma$-finite measure is a legitimate intensity; $\mathbb{E}[\prod_{\eta\in\mathcal{L}}e^{F(\eta)}] = \exp(\lambda\int(e^{F}-1)\,\mathrm{d}\mu)$. This is the entirety of §3.3 and the proof of Proposition 6.7.
- 🟢 **Complex analysis: holomorphy, meromorphic continuation, order of a zero, Euler products** — from the *Complex Analysis* strand. The DAG node is 🔵 (4/10) but the vault carries Complex Analysis I–IV and the uses here are elementary: expanding $-\log(1-x) = \sum_m x^m/m$, reading off a simple zero, and taking a logarithmic derivative. **If any single anchor on this list is worth double-checking, it is this one** — §5 leans on the meromorphic continuation of $\zeta_X$ and of $Z_X$ as black boxes.

---

# The backchain

## The central formula: Theorem 3.5 (mass of a homotopy class)

- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]]
	- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]]
		- [[Constr - The Dirichlet-Form Loop Measure]]
			- [[Def - Dirichlet Form and the Hunt Process Correspondence]]
				- 🟢 self-adjoint operators, closed quadratic forms, $L^2$ semigroups
				- 🟢 Markov processes and transition densities
			- [[Def - The Space of Unrooted Unparametrised Loops]]
				- 🟢 càdlàg path spaces, disintegration by endpoint
				- 🟢 pushforward of a measure under a quotient map
			- 🟢 σ-finiteness; the multiplicative Haar measure $\mathrm{d}t/t$ on $(0,\infty)$
		- [[Constr - The Periodised Kernel]]
			- [[Def - Fuchsian Group and the Quotient Surface]]
				- [[Def - Geometrically Finite Surfaces, Cusps and Funnels]]
					- 🟢 hyperbolic plane $\mathbb{H}^2$, its isometry group $\mathrm{PSL}(2,\mathbb{R})$, its area measure
				- 🟢 group actions, free and properly discontinuous actions ([[Def - Group Action]])
			- [[Def - Deck Transformations and the Lift of a Rooted Loop]]
				- [[Def - Covering Space]]
				- [[Def - Regular (Galois) Covering]]
				- [[Def - Path-Product and the Fundamental Group]]
				- [[Thm - Galois Correspondence for Covering Spaces]]
		- [[Constr - Standard-Form Representative and the Fundamental Strip]]
			- [[Def - Primitive Hyperbolic Element and Translation Length]]
				- 🟢 conjugation in $\mathrm{PSL}(2,\mathbb{R})$; classification of isometries by trace
			- [[Def - Centraliser and Coset Enumeration of a Conjugacy Class]]
				- [[Def - Conjugacy Class]]
				- [[Def - Centraliser and Centre]]
				- 🟢 left cosets and the partition of a group by them
		- [[Def - Free Homotopy Class and Conjugacy Class Correspondence]]
			- [[Def - Deck Transformations and the Lift of a Rooted Loop]] *(as above)*
			- 🟢 free homotopy of loops (basepoint-free), conjugation as change of basepoint
		- [[Constr - Loop Mass in a Homotopy Class for Jump Processes]] *(only in the jump case)*
			- [[Constr - The Periodised Kernel]] *(as above)*
	- [[Thm - The Wang–Xue Fundamental-Strip Identity]]
		- 🟢 explicit hyperbolic heat kernel on $\mathbb{H}^2$; the identity $\int_0^\infty s^{-3/2}e^{-as-b/s}\,\mathrm{d}s = \sqrt{\pi/b}\,e^{-2\sqrt{ab}}$
	- [[Thm - Collapsing the Time Integral into the Weighted Potential Measure]]
		- [[Constr - The Weighted Potential Measure Vϕ]]
			- [[Def - Subordinator and Subordination of a Semigroup]]
				- [[Def - Bernstein Function and the Lévy–Khintchine Representation]]
					- 🟢 completely monotone functions; Laplace transforms
					- 🟢 Lévy processes and Laplace exponents
				- [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)]]
			- 🟢 Tonelli ([[Thm - Fubini-Tonelli Theorem]])
	- [[Constr - The Subordinate Brownian Loop Measure]]
		- [[Constr - The Dirichlet-Form Loop Measure]] *(as above)*
		- [[Def - Subordinator and Subordination of a Semigroup]] *(as above)*
	- [[Constr - The Weighted Heat-Kernel Integral Iϕ]]
		- [[Constr - The Weighted Potential Measure Vϕ]] *(as above)*

## The Brownian loop measure and its two structural properties

- [[Constr - The Brownian Loop Measure]]
	- [[Def - The Space of Unrooted Unparametrised Loops]] *(as above)*
	- 🟢 heat kernel and unnormalised bridge measures
	- 🟢 conformal rescaling of the Laplacian in two dimensions
	- [[Def - Conformal Map]]

## §3.4: what the two structural properties buy

- [[Thm - Length-Spectrum Identity under Puncturing]]
	- [[Constr - The Brownian Loop Measure]] *(restriction and conformal invariance)*
	- [[Def - Polar Set]]
		- 🟢 potential theory of Markov processes; hitting probabilities
		- 🟢 logarithmic capacity in a chart
	- 🟢 uniformisation: existence of a unique complete hyperbolic metric on a punctured surface **(see the gaps section)**
- [[Thm - Loop Masses Determine the Marked Length Spectrum]]
	- [[Def - Marked Length Spectrum]]
	- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]] *(as above)*
- [[Thm - Loop Masses Determine the Hyperbolic Surface]]
	- [[Thm - Loop Masses Determine the Marked Length Spectrum]] *(as above)*
	- 🟢 Teichmüller space as the space of hyperbolic metrics up to isotopy **(see the gaps section)**

## §4: the zeta identities

- [[Thm - Selberg Zeta Identity (Killing Case)]]
	- [[Thm - Selberg Zeta Criterion]]
		- [[Def - Selberg Zeta Function]]
			- [[Def - Critical Exponent and the Prime Geodesic Theorem]]
				- [[Def - Primitive Hyperbolic Element and Translation Length]] *(as above)*
				- 🟢 exponent of convergence of a series; Poincaré series
			- 🟢 Euler products; $-\log(1-x)=\sum_m x^m/m$; geometric series
		- [[Constr - The Weighted Heat-Kernel Integral Iϕ]] *(as above)*
- [[Thm - Twisted Ruelle Zeta Identity]]
	- [[Def - Ruelle Zeta Function and its Twist]]
		- [[Def - Selberg Zeta Function]] *(as above)*
		- 🟢 finite-dimensional representations; $-\log\det(I-M)=\sum_m \operatorname{tr}(M^m)/m$
	- [[Thm - Selberg Zeta Identity (Killing Case)|the killing-case mass formula (26)]]
- [[Thm - Finiteness of the Total Mass]]
	- [[Def - Critical Exponent and the Prime Geodesic Theorem]] *(as above)*
	- [[Def - Systole]]
	- 🟢 Riemann–Stieltjes integration by parts against a counting function

## §5: renormalisation

- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)]]
	- [[Def - Zeta-Regularised Determinant of the Laplacian]]
		- 🟢 spectral zeta $\sum_j \lambda_j^{-s}$; Mellin transform; the Gamma function's pole structure
		- 🟢 Weyl's law; the small-time heat-trace expansion
		- [[Def - Euler Characteristic]]
	- [[Def - Critical Exponent and the Prime Geodesic Theorem|the refined prime geodesic theorem (43)]]
	- 🟢 Selberg trace formula for the heat semigroup on a closed hyperbolic surface **(see the gaps section)**
	- [[Thm - Selberg Zeta Identity (Killing Case)]] *(as above, for part (ii))*
- [[Thm - Polyakov's Formula via Brownian Loop Measure]]
	- [[Thm - Polyakov's Conformal Anomaly Formula]]
		- 🟢 conformal rescaling; Gauss curvature ([[Thm - Gauss-Bonnet Theorem for Surfaces]])
	- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)]] *(as above)*
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)]]
	- [[Def - Renormalised Integral and the 0-Trace]]
		- [[Def - Eisenstein Series and the Continuous Spectrum]]
			- 🟢 continuous spectrum; generalised eigenfunctions
		- 🟢 finite part of a meromorphic continuation (Riesz / Hadamard regularisation)
	- [[Thm - Borthwick–Judge–Perry Determinant Formula]]
		- [[Def - Selberg Zeta Function]] *(as above)*
		- 🟢 Barnes $G$-function **(see the gaps section)**
	- [[Thm - Selberg Zeta Identity (Killing Case)]] *(as above)*

## §6: the probability measures

- [[Constr - The Probability Measure on Free Homotopy Classes]]
	- [[Thm - Selberg Zeta Identity (Killing Case)]] *(the normalising constant)*
	- [[Thm - Finiteness of the Total Mass]] *(that the normalisation exists)*
- [[Thm - Moments of the Length via the Selberg Zeta Function]]
	- [[Constr - The Probability Measure on Free Homotopy Classes]] *(as above)*
	- 🟢 moment generating functions; cumulants as derivatives of a log
- [[Thm - Concentration on Systolic Classes]]
	- [[Def - Systole]]
	- 🟢 dominance of the slowest-decaying exponential term
- [[Thm - Fourier Expansion and Inversion by Homology Class]]
	- [[Constr - The Mass in a Homology Class]]
		- 🟢 abelianisation; [[Def - Hurewicz Map]], [[Thm - Hurewicz Theorem (Statement)]]
		- 🟢 first homology of a surface, $H_1 \cong \mathbb{Z}^{2g}$ for a closed surface of genus $g$
	- [[Thm - Selberg L-Function Identity]]
		- [[Def - Selberg L-Function]]
			- [[Def - Character Torus and the Pontryagin Dual]]
				- 🟢 characters of a finitely generated abelian group; Haar measure on a compact torus; orthogonality of characters
	- [[Def - The Jacobian as a Principally Polarised Abelian Variety]] *(only for the closed-case restatement)*
		- [[Thm - Hodge Decomposition Theorem]]
		- [[Def - The Hodge Star Operator]]
		- [[Def - de Rham Cohomology]]
- [[Thm - Distribution of the Total Homology of the Loop Soup]]
	- [[Thm - Poissonian Structure of Homotopy Classes]]
		- 🟢 Poisson point processes; disjoint sets give independent counts
	- [[Thm - Selberg L-Function Identity]] *(as above)*
	- 🟢 the exponential formula for a Poisson point process

## §7: three dimensions

- [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds]]
	- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds]]
		- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds]]
			- [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab]]
				- [[Def - Kleinian Group and Loxodromic Complex Length]]
					- 🟢 $\mathbb{H}^3$ and $\mathrm{PSL}(2,\mathbb{C})$; classification of isometries
					- [[Def - Fuchsian Group and the Quotient Surface]] *(the 2D analogue this generalises)*
				- [[Def - Centraliser and Coset Enumeration of a Conjugacy Class]] *(as above — verbatim the same argument)*
		- [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity]]
			- 🟢 explicit $\mathbb{H}^3$ heat kernel $p_{\mathbb{H}^3}(t,z,w) = (4\pi t)^{-3/2}\frac{u}{\sinh u}e^{-t-u^2/4t}$
			- 🟢 change of variables; polar coordinates in $\mathbb{C}$
		- [[Thm - Collapsing the Time Integral into the Weighted Potential Measure]] *(as above)*

---

# Leaves that are not anchors

Five honest gaps. In each case the paper uses a result as a black box, and so does this note-set; what is recorded here is the result used, what it is used for, and what would have to be studied to close the gap.

**The Selberg trace formula for the heat semigroup** (equation (44), used in Theorem 5.1). The paper quotes the identity $\sum_j e^{-t\lambda_j} = \text{(identity contribution)} + \text{(geometric contribution)}$ on a closed hyperbolic surface, and everything in §5.1 is arithmetic on top of it. This is the deepest single input to the paper and it is not proved anywhere here. Home node: *Automorphic Forms / Selberg Trace Formula* (🔵), which lists Iwaniec and Bergeron as references, and whose own prereqs are Modular Forms, Harmonic Analysis, Spectral Theory, Lie Groups and Riemann Surfaces. The trace formula is described in that node as "non-abelian Poisson summation identifying the Laplace eigenvalue spectrum of $\Gamma\backslash\mathbb{H}$ with the length spectrum of its closed geodesics" — which is exactly the shape of what §5 uses it for. **Closing this gap means studying that node**, and it is the highest-leverage study target the paper suggests.

**The prime geodesic theorem** ($N_X(R) \sim e^{\delta R}/\delta R$, and its refined form (43)). Stated and used, not proved; it is a corollary of the trace formula, so it closes with the same study. Recorded on [[Def - Critical Exponent and the Prime Geodesic Theorem]] as a black box with its role spelled out.

**Otal's and Croke's theorem** (a negatively curved metric on a closed surface is determined up to isometry by its marked length spectrum), used in [[Thm - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]], together with the description of Teichmüller space. This is genuinely outside everything in the vault; it belongs to a *Hyperbolic geometry / Teichmüller theory* strand that has no DAG node yet. The corollary is the only place it is used, and the rest of the paper is unaffected by taking it on faith.

**Uniformisation** — the existence of a unique complete hyperbolic metric on a punctured hyperbolic surface, used in [[Thm - Length-Spectrum Identity under Puncturing|Theorem 3.9]]. Home node: *Riemann Surfaces* (🔵). Only §3.4 needs it.

**Borthwick–Judge–Perry and the Barnes $G$-function**, used in [[Thm - Borthwick–Judge–Perry Determinant Formula|Theorem 5.5]]. The identification of $\det_0(\Delta_X - s(1-s))$ with an explicit expression in $Z_X$, $G_\infty$ and $\Gamma$ is quoted wholesale. Borthwick's *Spectral theory of infinite-area hyperbolic surfaces* is the reference the paper gives. Only §5.2 needs it; §5.1 is self-contained modulo the trace formula.

Everything else on this page reduces to an anchor.
