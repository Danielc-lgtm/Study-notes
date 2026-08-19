---
type: definition
subject: topology
prereqs:
  - "Def - Closed Geodesics, Conjugacy Classes, and Translation Length"
tags: [topology, algebra, harmonic-analysis, paper-prereq]
source: "Brownian Loops — Homotopy and Homology"
---

# Notation

$X=\Gamma\backslash\mathbb{H}^2$ a hyperbolic surface, $\pi_1(X)\cong\Gamma$ its fundamental group. $H_1(X,\mathbb{Z})$ its first homology group. A **character** is a homomorphism $\chi:H_1(X,\mathbb{Z})\to\mathbb{C}^\times$; a **unitary character** maps into the unit circle $S^1=\{z\in\mathbb{C}:|z|=1\}$. $\widehat{H_1(X,\mathbb{Z})}$ the group of unitary characters (the dual). $S^1\cong\mathbb{R}/\mathbb{Z}$ via $\theta\mapsto e^{2\pi i\theta}$.

---

# Axiom Motivation

§3–§6 sort loops ever more coarsely: first by free homotopy class (a *conjugacy* class in the non-abelian $\Gamma$, remembering the order in which handles are traversed), then — in §6.2 — by **homology class**, which forgets that order and remembers only the *net* winding around each independent cycle. Homology is the abelian shadow of homotopy: $H_1(X,\mathbb{Z})$ is the abelianisation of $\pi_1(X)$. Because it is an abelian group (indeed a lattice $\mathbb{Z}^r$), one can do **Fourier analysis** on it, and that is exactly what lets the paper *extract* the mass in a single homology class from a generating function summed over all classes.

The tool is **Pontryagin duality / character orthogonality**. A function on the abelian group $H_1$ (like "mass in class $\beta$") is encoded by its Fourier transform, a function on the dual group of characters (here, the Selberg $L$-function values); and the transform is inverted by integrating against $\overline{\chi(\beta)}$ over all characters, because distinct characters are orthogonal. This is the same mechanism by which Dirichlet $L$-functions detect primes in arithmetic progressions — characters of $(\mathbb{Z}/n)^\times$ there, characters of $H_1(X,\mathbb{Z})$ here. The paper's Fourier inversion (Theorem 6.5) *is* this orthogonality, applied to the length spectrum sorted by homology.

---

# The Definition

> **Definition (first homology; characters; orthogonality).** The **first homology group** $H_1(X,\mathbb{Z})$ is the abelianisation of $\pi_1(X)\cong\Gamma$: $H_1(X,\mathbb{Z})=\Gamma/[\Gamma,\Gamma]$, with the **Hurewicz** quotient map $\Gamma\twoheadrightarrow H_1(X,\mathbb{Z})$, $\gamma\mapsto[\gamma]$ (so $[\gamma^m]=m[\gamma]$). For a closed surface of genus $g$, $H_1(X,\mathbb{Z})\cong\mathbb{Z}^{2g}$; for a geometrically finite non-compact surface of genus $g$ with $b=n_C+n_F\ge1$ ends ($n_C$ cusps, $n_F$ funnels), $H_1(X,\mathbb{Z})\cong\mathbb{Z}^{r}$, $r=2g+b-1$.
> A **unitary character** is a homomorphism $\chi:H_1(X,\mathbb{Z})\to S^1$; the set of them is the **character torus** (Pontryagin dual) $\widehat{H_1(X,\mathbb{Z})}\cong(S^1)^r\cong(\mathbb{R}/\mathbb{Z})^r$ (a character is fixed by its values $\chi(e_j)=e^{2\pi i\theta_j}$ on a $\mathbb{Z}$-basis $e_1,\dots,e_r$). With the normalised Haar measure $d\chi$ on the torus, characters are **orthonormal**:
> $$\int_{\widehat{H_1(X,\mathbb{Z})}}\chi(\beta')\,\overline{\chi(\beta)}\,d\chi=\begin{cases}1,&\beta'=\beta,\\0,&\beta'\ne\beta,\end{cases}$$
> which is the **Fourier inversion** identity on the abelian group.

> [!recall]- De Rham $H^1$ / harmonic $1$-forms on a closed surface
> **Formally:** on a closed Riemannian surface $X$, a **$1$-form** is an object that can be integrated along a curve; a **harmonic form** is a $1$-form $\omega$ with $d\omega=0=d{*}\omega$ (closed and co-closed). The space of harmonic $1$-forms is a finite-dimensional real vector space $\mathcal H^1(X)$ of dimension $2g$ (Hodge theorem), naturally isomorphic to the first **de Rham cohomology** $H^1_{\mathrm{dR}}(X,\mathbb{R})$.
> **In words:** on a torus you can integrate a $1$-form $\omega=f\,dx+g\,dy$ along a curve; harmonic forms are the ones that solve the vector Laplace equation; there are exactly $2g$ independent ones on a genus-$g$ surface.
> **Concretely:** on the flat torus $T^2=\mathbb{R}^2/\mathbb{Z}^2$, the harmonic $1$-forms are exactly the constant-coefficient forms $a\,dx+b\,dy$ for $(a,b)\in\mathbb{R}^2$; integrating along the standard cycles gives $\int_{(1,0)}=a$, $\int_{(0,1)}=b$, so the associated character is $\chi_{(a,b)}(m,n)=e^{2\pi i(am+bn)}$.

> **Definition (Jacobian picture, closed case — sketch).** When $X$ is closed, harmonic $1$-forms give a concrete model of the dual: a harmonic form $\omega\in\mathcal H^1(X)$ defines the character $\chi_\omega(\beta)=e^{2\pi i\int_\beta\omega}$ (unitary holonomy of the period), and two forms give the same character iff they differ by one with integer periods. The upshot is that the character torus is the **Jacobian** $\operatorname{Jac}(X)$ — the *dual torus of harmonic forms modulo integer periods*, a real $2g$-dimensional torus.

**Concrete unpacking.** For the torus $X=\mathbb{R}^2/\mathbb{Z}^2$ (flat, but illustrative), $H_1=\mathbb{Z}^2$ (two independent cycles), characters are $\chi_{(\theta_1,\theta_2)}(m,n)=e^{2\pi i(m\theta_1+n\theta_2)}$, the dual torus is $(\mathbb{R}/\mathbb{Z})^2$, and orthogonality is the statement $\int_0^1 e^{2\pi i(m-m')\theta}\,d\theta=\delta_{m,m'}$ — ordinary Fourier series. Inverting "$F(\chi)=\sum_\beta a_\beta\chi(\beta)$" to recover $a_\beta=\int F(\chi)\overline{\chi(\beta)}\,d\chi$ is exactly reading off a Fourier coefficient.

**Standard names.** **First homology group**, **abelianisation**, **Hurewicz homomorphism**, **(unitary) character**, **Pontryagin dual / character group**, **character orthogonality / Fourier inversion**, **Jacobian variety**, **harmonic $1$-forms** (Hodge theory). Reference: Hatcher, *Algebraic Topology*, §2.A (Hurewicz, $H_1=\pi_1^{\mathrm{ab}}$); Rudin, *Fourier Analysis on Groups* (Pontryagin duality).

---

# Examples and Non-Examples

**Is an instance.** Genus-2 closed surface: $H_1=\mathbb{Z}^4$, dual $(S^1)^4=\operatorname{Jac}(X)$ a 2-dimensional complex torus. A once-punctured torus: $g=1$, $b=1$, $r=2\cdot1+1-1=2$, so $H_1=\mathbb{Z}^2$.

**Is NOT an instance.** The *conjugacy class* of $\gamma$ in the non-abelian $\Gamma$ is **not** a homology class: homology forgets conjugation-order information, so infinitely many distinct free homotopy (conjugacy) classes map to the same $\beta\in H_1$. This many-to-one collapse is precisely what §6.2 sums over.

**Calibration check.** (1) Verify $[\gamma^m]=m[\gamma]$ from the Hurewicz map being a homomorphism. (2) Check character orthogonality on $\mathbb{Z}/n$: $\frac1n\sum_{a}e^{2\pi i k a/n}=\delta_{k\equiv0}$. (3) Confirm $r=2g$ for a closed surface and $r=2g+b-1$ with one end removed (an extra relation among the boundary cycles).

---

# Where the paper uses this

§6.2 groups the loop measure by homology class (Def 6.1), defines the Selberg $L$-function by twisting the Selberg zeta with a unitary character $\chi$, and uses **character orthogonality** (this note) to prove the Fourier inversion formula (Theorem 6.5) that extracts the mass in a single class $\beta$. Proposition 6.7's distribution of the loop soup's total homology is a Fourier transform over the character torus. The Jacobian picture reformulates the inversion as an integral over $\operatorname{Jac}(X)$ in the closed case. **[[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6.2]]**.

---

# Verified against

Hatcher, *Algebraic Topology*, §2.A (Hurewicz theorem, $H_1(X)=\pi_1(X)^{\mathrm{ab}}$, ranks of surface homology); Rudin, *Fourier Analysis on Groups*, Ch. 1–2 (Pontryagin dual, Haar measure, character orthogonality); Farkas–Kra, *Riemann Surfaces*, for the Jacobian and harmonic-form picture. Ranks $2g$ (closed) and $2g+b-1$ (with $b$ ends) standard. Matches the paper's §6.2.
