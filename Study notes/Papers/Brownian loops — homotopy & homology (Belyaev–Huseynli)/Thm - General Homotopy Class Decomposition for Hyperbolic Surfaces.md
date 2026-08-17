---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Dirichlet-Form Loop Measure"
  - "Constr - The Periodised Kernel"
  - "Constr - Standard-Form Representative and the Fundamental Strip"
  - "Def - Centraliser and Coset Enumeration of a Conjugacy Class"
  - "Def - Fundamental Region"
tags: [paper, probability, hyperbolic-geometry, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $\Gamma$ | torsion-free Fuchsian $\subseteq\mathrm{PSL}(2,\mathbb{R})$; $X=\Gamma\backslash\mathbb{H}^2$; $\pi:\mathbb{H}^2\to X$ |
| $(\mathcal{E},\mathcal{F})$ | $\Gamma$-invariant regular symmetric Dirichlet form on $L^2(\mathbb{H}^2,\rho)$ |
| $p^{\mathcal{E}}_{\mathbb{H}^2}$ | its density; satisfies $p^{\mathcal{E}}_{\mathbb{H}^2}(t,hz,hw)=p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,w)$, $h\in\Gamma$ |
| $\mu^{\mathcal{E}}_X$ | the loop measure of the descended form; $\sigma$-finite on $\mathcal{C}_X$ |
| $\gamma$ | $\in\mathcal{P}_X$, length $\ell_\gamma>0$; $\tau:z\mapsto e^{\ell_\gamma}z$ its standard-form representative |
| $m$ | $\in\mathbb{Z}_{\geq1}$; $\mathcal{C}_X(\gamma^m)$ the class |
| $F_\tau$ | $=\{1\leq\operatorname{Im}z<e^{\ell_\gamma}\}$; fundamental region for $\langle\tau\rangle$ |
| $F$ | a fundamental region for $\Gamma$ |
| $[\tau^m]_{\mathrm{conj}}$, $\Gamma/\langle\tau\rangle$ | the class and its indexing cosets |
| $W^{t,\mathcal{E}}_{z\to z,X}$ | the downstairs diagonal bridge; $\pi_*$ pushforward |
| $\rho,\ \rho_X$ | hyperbolic area upstairs and downstairs |

---

# Type card

> [!abstract] Type card — Theorem 3.2
> **Given.**
> **(H1)** $(\mathcal{E},\mathcal{F})$ a [[Def - Regular Symmetric Dirichlet Form|regular symmetric Dirichlet form]] on $L^2(\mathbb{H}^2,\rho)$, $\Gamma$-invariant, with density satisfying [[Constr - The Periodised Kernel|(A1),(A2),(A3)]].
> **(H2)** $\gamma\in\mathcal{P}_X$ with [[Constr - Standard-Form Representative and the Fundamental Strip|standard-form representative]] $\tau:z\mapsto e^{\ell_\gamma}z$ and strip $F_\tau$.
> **(H3)** $m\in\mathbb{Z}_{\geq1}$.
> **(H4)** For jump processes, the left-hand side is read via [[Constr - Loop Mass in a Homotopy Class for Jump Processes|(13)]].
>
> **Produces.** An identity in $[0,\infty]$: a class mass, computed entirely **upstairs on $\mathbb{H}^2$**, against a **single** group element $\tau^m$, over an **explicit** region $F_\tau$.
>
> **Lets you.** Eliminate both the sum over $\Gamma$ and the quotient geometry of $X$, leaving a two-variable integral that an explicit heat kernel can discharge.

---

# Statement

> **Theorem 3.2.** Assume (H1)–(H4). Then
> $$\mu^{\mathcal{E}}_X\big(\mathcal{C}_X(\gamma^m)\big) \;=\; \int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau} p^{\mathcal{E}}_{\mathbb{H}^2}\big(t,z,\tau^m z\big)\,\mathrm{d}\rho(z).\tag{14}$$

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Def - Deck Transformations and the Lift of a Rooted Loop\|lifting dictionary]] | $W^{t,\mathcal{E}}_{z\to z,X}$ | $\sum_{h\in\Gamma}\pi_*W^{t,\mathcal{E}}_{\tilde z\to h\tilde z,\mathbb{H}^2}$ — eq. (15) |
| [[Def - Free Homotopy Class and Conjugacy Class Correspondence\|correspondence]] | restriction to $\mathcal{C}_X(\gamma^m)$ | restriction of the sum to $h\in[\tau^m]_{\mathrm{conj}}$ |
| [[Def - Fundamental Region\|(U)]] | $\int_X(\cdot)\,\mathrm{d}\rho_X$ | $\int_F(\cdot)\,\mathrm{d}\rho$ |
| [[Def - Centraliser and Coset Enumeration of a Conjugacy Class\|(E)]] | $[\tau^m]_{\mathrm{conj}}$ | $\bigsqcup_{r\in\Gamma/\langle\tau\rangle}\{r\tau^mr^{-1}\}$, one per coset |
| [[Constr - The Periodised Kernel\|(A1)]] | $p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,r\tau^mr^{-1}z)$ | $p^{\mathcal{E}}_{\mathbb{H}^2}(t,r^{-1}z,\tau^mr^{-1}z)$ |
| [[Def - Fundamental Region\|(R)]] | $\bigsqcup_{r}r^{-1}F$ | a fundamental region for $\langle\tau\rangle$ |
| [[Def - Fundamental Region\|(I)]] + [[Constr - Standard-Form Representative and the Fundamental Strip\|(F2)]] | $\int_{\bigsqcup_rr^{-1}F}$ of a $\langle\tau\rangle$-invariant integrand | $\int_{F_\tau}$ |

---

# Proof

**Strategy.** Unfold the conjugacy-class sum over the cosets of the cyclic centraliser $\langle\tau\rangle$, using (A1) to move each representative onto the region; then swap the reassembled $\langle\tau\rangle$-region for the strip $F_\tau$, legal by (I) since the integrand is $\langle\tau\rangle$-invariant.

> [!note]- Proof (skippable)
> **Step 1 — isolate the conjugacy class.** For a continuous process the lifting dictionary gives
> $$W^{t,\mathcal{E}}_{z\to z,X}=\sum_{h\in\Gamma}\pi_*W^{t,\mathcal{E}}_{\tilde z\to h\tilde z,\mathbb{H}^2},\tag{15}$$
> decomposing loops rooted at $z$ by the deck transformation their lifts record. Restricting to $\mathcal{C}_X(\gamma^m)$ therefore restricts the sum in (11) (with $\tilde z=\tilde w$) to $h\in[\tau^m]_{\mathrm{conj}}$; for a jump process this restriction **is** the definition (13). Either way,
> $$\mu^{\mathcal{E}}_X\big(\mathcal{C}_X(\gamma^m)\big)=\int_0^\infty\frac{\mathrm{d}t}{t}\int_X\sum_{h\in[\tau^m]_{\mathrm{conj}}}p^{\mathcal{E}}_{\mathbb{H}^2}(t,\tilde z,h\tilde z)\,\mathrm{d}\rho_X(z).\tag{16}$$
>
> **Step 2 — unfold to the strip.** By (U), (16) becomes
> $$\int_0^\infty\frac{\mathrm{d}t}{t}\int_F\sum_{h\in[\tau^m]_{\mathrm{conj}}}p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,hz)\,\mathrm{d}\rho(z).\tag{17}$$
> Unfold the class sum by (E). For each $r\in\Gamma/\langle\tau\rangle$, (A1) gives
> $$p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,r\tau^mr^{-1}z)=p^{\mathcal{E}}_{\mathbb{H}^2}(t,r^{-1}z,\tau^mr^{-1}z),$$
> and the substitution $w=r^{-1}z$ — an isometry, so $\rho$-preserving — gives
> $$\int_Fp^{\mathcal{E}}_{\mathbb{H}^2}(t,z,r\tau^mr^{-1}z)\,\mathrm{d}\rho(z)=\int_{r^{-1}F}p^{\mathcal{E}}_{\mathbb{H}^2}(t,w,\tau^mw)\,\mathrm{d}\rho(w).$$
> Summing over the cosets,
> $$\sum_{r\in\Gamma/\langle\tau\rangle}\int_{r^{-1}F}p^{\mathcal{E}}_{\mathbb{H}^2}(t,w,\tau^mw)\,\mathrm{d}\rho(w)=\int_{\bigsqcup_rr^{-1}F}p^{\mathcal{E}}_{\mathbb{H}^2}(t,w,\tau^mw)\,\mathrm{d}\rho(w).\tag{18}$$
>
> **Step 3 — swap the region.** By (R), $\bigsqcup_rr^{-1}F$ is a fundamental region for $\langle\tau\rangle$. By [[Constr - Standard-Form Representative and the Fundamental Strip|(F2)]] the integrand $w\mapsto p^{\mathcal{E}}_{\mathbb{H}^2}(t,w,\tau^mw)$ is $\langle\tau\rangle$-invariant, so by (I) its integral over any fundamental region of $\langle\tau\rangle$ is the same. Replace $\bigsqcup_rr^{-1}F$ by $F_\tau$. This is (14). $\;\square$

---

# What this assumes, and where to climb

- **The measure being decomposed** — [[Constr - The Dirichlet-Form Loop Measure]], and its Brownian special case [[Constr - The Brownian Loop Measure]].
- **The covering-space apparatus** — [[Def - Fuchsian Group and the Quotient Surface]], [[Def - Deck Transformations and the Lift of a Rooted Loop]], [[Constr - The Periodised Kernel]].
- **The group theory** — [[Def - Centraliser and Coset Enumeration of a Conjugacy Class]], [[Def - Free Homotopy Class and Conjugacy Class Correspondence]].
- **The unfolding identities (U),(I),(R)** — [[Def - Fundamental Region]].
- **Not assumed:** any property of $\phi$, or dimension $2$. See [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds]].

---

# Consumed by

- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]] — starts from (14) with $p^{\mathcal{E}}_{\mathbb{H}^2}=p^\phi_{\mathbb{H}^2}$
- [[§3 Decomposition over Homotopy Classes]] — the section's central result
- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds]] — the paper's proof there reads "identical in structure"; reading this proof is reading that one

---

# Commentary

> [!note]- Commentary (skippable)
> **The mechanism in one line: the conjugacy-class sum is exactly as big as the gap between a fundamental region for $\Gamma$ and one for the cyclic centraliser $\langle\tau\rangle$, so the two cancel and leave a single term on a band.**
>
> Both objects one starts with are large and neither is computable — an integral over a fundamental region for $\Gamma$, of a sum over a conjugacy class. But they are *complementary*: (E) indexes the class by $\Gamma/\langle\tau\rangle$, and (R) says the same index set reassembles $F$ into a fundamental region for $\langle\tau\rangle$. One sum-over-a-class times one $\Gamma$-region equals one term times one $\langle\tau\rangle$-region.
>
> This is the only genuinely structural argument in the paper, and it recurs verbatim in §7 — which is worth knowing, since it means §7 costs exactly one new computation rather than a new idea.
>
> Placing it: the unfolding is the standard device by which a conjugacy-class sum in the [[Ext - Selberg Trace Formula (Heat Kernel Form)|Selberg trace formula]] becomes an integral over a cylinder. Theorem 3.2 is what **one term of the trace formula's geometric side** looks like in isolation — and §5 will need the whole formula.
