---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Free and Properly Discontinuous Action"
tags: [paper, group-theory, hyperbolic-geometry]
---

# Signature

| symbol | type |
|---|---|
| $M$ | $\mathbb{H}^2$ or $\mathbb{H}^3$, with its isometry-invariant measure $\rho$ |
| $G$ | a group acting on $M$ freely and properly discontinuously ([[Def - Free and Properly Discontinuous Action\|(D1),(D2)]]) by $\rho$-preserving maps |
| $F$ | $\subseteq M$ Borel; a fundamental region for $G$ |
| $\rho$ | the $G$-invariant Radon measure: $\rho(hA)=\rho(A)$ for all $h\in G$, Borel $A$ |
| $\pi$ | $M\to G\backslash M$; $\rho_{G\backslash M}$ the induced measure |
| $f$ | $M\to[0,\infty]$ Borel, $G$-invariant: $f\circ h=f$ for all $h\in G$ |

---

# Definition

> **Definition (fundamental region).** A Borel set $F\subseteq M$ is a **fundamental region** for $G$ acting on $(M,\rho)$ if
> **(D1)** $\ \bigcup_{h\in G}hF=M$;
> **(D2)** $\ \rho(hF\cap F)=0$ for every $h\in G\setminus\{1\}$.
>
> When the union in (D1) is disjoint and (D2) holds with $hF\cap F=\emptyset$, $F$ meets each orbit in exactly one point; this is the form used throughout.

> **(U) Unfolding.** If $F$ is a fundamental region for $G$ then for every $G$-invariant Borel $f\geq0$,
> $$\int_{G\backslash M}\bar f\,\mathrm{d}\rho_{G\backslash M}=\int_F f\,\mathrm{d}\rho,\qquad \bar f\circ\pi=f.$$

> **(I) Independence of the region.** If $F,F'$ are both fundamental regions for $G$ and $f\geq0$ is $G$-invariant Borel, then
> $$\int_F f\,\mathrm{d}\rho=\int_{F'}f\,\mathrm{d}\rho.$$

> **(R) Reassembly.** Let $H\leq G$ and let $R\subseteq G$ be a set of representatives for the left cosets $G/H$, so $G=\bigsqcup_{r\in R}rH$. If $F$ is a fundamental region for $G$ then
> $$\widetilde F:=\bigsqcup_{r\in R}r^{-1}F$$
> is a fundamental region for $H$.

**Gloss.** (U) converts "integrate downstairs" into "integrate over $F$"; (R) plus (I) is the unfolding move of §3 and §7 in two lines.

**Strategy.** (I) compares two regions by translating one into the other and using $G$-invariance of the integrand; (R) partitions $H$-cosets inside a $G$-region.

> [!note]- Proof of (I) and (R) (skippable)
> **(I).** By (D1) for $F'$, $\int_Ff\,\mathrm{d}\rho=\sum_{h\in G}\int_{F\cap hF'}f\,\mathrm{d}\rho$ up to a $\rho$-null overlap by (D2). Substituting $z=hw$ and using $\rho$-invariance and $f(hw)=f(w)$, $\int_{F\cap hF'}f\,\mathrm{d}\rho=\int_{h^{-1}F\cap F'}f\,\mathrm{d}\rho$. Summing over $h$ and applying (D1) for $F$ gives $\int_{F'}f\,\mathrm{d}\rho$.
>
> **(R).** For (D1): given $z\in M$, by (D1) for $F$ there is $g\in G$ with $g z\in F$; write $g=rh$ with $r\in R$, $h\in H$, so $hz\in r^{-1}F\subseteq\widetilde F$. For (D2): if $h\in H\setminus\{1\}$ and $\rho(h\widetilde F\cap\widetilde F)>0$ then $\rho(hr^{-1}F\cap r'^{-1}F)>0$ for some $r,r'\in R$, so $r'hr^{-1}\in G$ fixes a positive-measure piece of $F$, whence $r'hr^{-1}=1$ by (D2) for $F$; then $h=r'^{-1}r\in H$ forces $rH=r'H$, so $r=r'$ and $h=1$.

---

# Type card

> [!abstract] Type card — fundamental region
> **Given.** **(H1)** $G$ acting on $(M,\rho)$ freely and properly discontinuously by $\rho$-preserving maps. **(H2)** $F\subseteq M$ Borel satisfying (D1), (D2).
>
> **Produces.** Three transfer identities: (U) between $\int_{G\backslash M}$ and $\int_F$; (I) between any two fundamental regions; (R) a fundamental region for a subgroup $H\leq G$, assembled from $G/H$-translates of $F$.
>
> **Lets you.** Perform the §3 and §7 unfolding as a citation rather than an argument: (R) turns a conjugacy-class sum into a $\langle\tau\rangle$-region, and (I) then swaps that region for an explicit strip or slab.

---

# Depends on

- [[Def - Free and Properly Discontinuous Action]] — (D1),(D2) there are the hypothesis (H1) here
- 🟢 invariance of a measure under a group of measure-preserving maps; countable additivity

---

# Checks

**Instance.** $G=\langle\tau\rangle$, $\tau:z\mapsto e^{\ell}z$ on $\mathbb{H}^2$ with $\rho=\operatorname{Im}(z)^{-2}\,\mathrm{d}x\,\mathrm{d}y$. Take $F_\tau=\{1\leq\operatorname{Im}z<e^{\ell}\}$. **(D1):** the orbit of $z$ has imaginary parts $\{e^{k\ell}\operatorname{Im}z\}_{k\in\mathbb{Z}}$, and exactly one lies in $[1,e^{\ell})$, namely $k=-\lfloor\log\operatorname{Im}z/\ell\rfloor$. **(D2):** $\tau^kF_\tau\cap F_\tau=\emptyset$ for $k\neq0$, since the imaginary-part ranges $[e^{k\ell},e^{(k+1)\ell})$ are disjoint.

**Non-instance (fails D2).** $F=\{1\leq\operatorname{Im}z\leq e^{\ell}\}$, the *closed* band. (D1) holds. (D2) fails as stated with $hF\cap F=\emptyset$ — the boundary lines $\operatorname{Im}z=1$ and $\operatorname{Im}z=e^\ell$ are identified by $\tau$. It does satisfy the $\rho$-null version of (D2), since a geodesic line is $\rho$-null, so it is a legitimate fundamental region in the measure-theoretic sense; only the "exactly one point per orbit" reading fails.

**Non-instance (fails D1).** $F=\{1\leq\operatorname{Im}z<e^{\ell/2}\}$ — half the strip. (D2) holds; (D1) fails, and $\int_Ff\,\mathrm{d}\rho$ undercounts. This is the error that would halve every mass in §3.

---

# Used at

- [[Constr - Standard-Form Representative and the Fundamental Strip]] — $F_\tau$ is a fundamental region for $\langle\tau\rangle$
- [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab]] — same in $\mathbb{H}^3$
- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]] — (U) in Step 2, then (R) and (I)
- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds]] — the same three, verbatim
- [[Def - Fuchsian Group and the Quotient Surface]] — (U) defines $\rho_X$

---

# Commentary

> [!note]- Commentary (skippable)
> The paper does not isolate (I) or (R); they appear inline in the proof of Theorem 3.2 as "the union $\bigsqcup_r r^{-1}F$ is a fundamental region for $\langle\tau\rangle$" and "its integral over any fundamental region of $\langle\tau\rangle$ is the same". Both are one-line consequences of (D1)–(D2), but the proof reads as geometry rather than bookkeeping unless they are named.
>
> Separating them also makes visible what the unfolding actually costs. The conjugacy class is indexed by $G/H$ with $H=C_\Gamma(\tau^m)=\langle\tau\rangle$; (R) says the same index set reassembles $F$ into a fundamental region for $H$. So the sum over the class and the enlargement of the region are the *same* combinatorial fact seen twice, which is why they cancel exactly.
