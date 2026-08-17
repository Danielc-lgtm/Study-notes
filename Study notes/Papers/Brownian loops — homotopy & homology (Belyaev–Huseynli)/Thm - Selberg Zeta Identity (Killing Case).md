---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - Selberg Zeta Criterion"
  - "Def - Selberg Zeta Function"
tags: [paper, zeta-functions, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $\kappa$ | $\geq-\tfrac14$ — the killing rate |
| $s$ | $=\tfrac12+\sqrt{\tfrac14+\kappa}$; the hypothesis is $s>\delta$ |
| $\mu^\kappa_X$ | the killing loop measure |
| $Z_X$ | the [[Def - Selberg Zeta Function\|Selberg zeta function]] |
| $\delta$ | the [[Def - Critical Exponent\|critical exponent]]; $\delta=1$ iff $\mathrm{area}(X)<\infty$ |

---

# Type card

> [!abstract] Type card — Corollary 4.3
> **Given.**
> **(H1)** $X$ geometrically finite hyperbolic surface.
> **(H2)** $\kappa\geq-\tfrac14$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$.
> **(H3)** $s>\delta$.
>
> **Produces.** The scalar identity
> $$\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^{\infty}\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)=-\log Z_X\Big(\tfrac12+\sqrt{\tfrac14+\kappa}\Big)\ \in(0,\infty).\tag{35}$$
>
> **Lets you.** Normalise. The left side is the total mass over non-trivial classes; dividing by it turns the class masses into a **probability measure** — this number is the partition function of §6.

---

# Statement

> **Corollary 4.3 (Selberg zeta identity, killing case).** Assume (H1)–(H3). Then (35) holds.
>
> **Specialisation $\kappa=0$:** $s=1$ and $\sum_{\gamma,m}\mu_X(\mathcal{C}_X(\gamma^m))=-\log Z_X(1)$.
> - $\mathrm{area}(X)=\infty$: $\delta<1$, so (H3) holds and the quantity is **finite**.
> - $\mathrm{area}(X)<\infty$: $\delta=1$, so (H3) **fails** and the sum **diverges**.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Thm - Selberg Zeta Criterion\|Lem 4.2]] §4.1.1 | $\phi(\lambda)=\lambda+\kappa$; $C=1$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ | (33) holds, hence (34) with $C=1$ |
| [[Constr - The Weighted Heat-Kernel Integral Iϕ\|(25)]] | $\phi(\lambda)=\lambda+\kappa$ | $I_\kappa(L)=e^{-L\sqrt{1/4+\kappa}}/L$ |
| $2\sinh(L/2)=e^{-L/2}(e^L-1)$ | the $\sinh$ factor | the shape $e^{(1-s)L}/(e^L-1)$ |
| [[Def - Selberg Zeta Function\|(F1)]] | the resulting double sum | $-\log Z_X(s)$ |

---

# Proof

**Strategy.** One row of the Lemma 4.2 table: verify (33) with $C=1$ by the closed form of $I_\kappa$ and the identity $2\sinh(L/2)=e^{-L/2}(e^L-1)$.

> [!note]- Proof (skippable)
> By (25), $I_\kappa(L)=e^{-L\sqrt{1/4+\kappa}}/L$. Hence
> $$\frac{L}{2\sinh(L/2)}I_\kappa(L)=\frac{e^{-L\sqrt{1/4+\kappa}}}{2\sinh(L/2)}=\frac{e^{-L\sqrt{1/4+\kappa}}\,e^{L/2}}{e^L-1}=\frac{e^{(1-s)L}}{e^L-1},$$
> since $\tfrac12-\sqrt{\tfrac14+\kappa}=1-s$. This is (33) with $C=1$ and this $s$, both independent of $L$. Lemma 4.2 then gives (35), with convergence from $s>\delta$. $\;\square$

---

# What this assumes, and where to climb

- **(H3) is the whole content of the finiteness statement.** $s>\delta$ is not a technical convenience: at $s=\delta$ the sum diverges, by [[Ext - Prime Geodesic Theorem|(PGT)]] and the $1/R$ factor. See [[Thm - Finiteness of the Total Mass|Cor 4.7]].
- **The identity is term-by-term**, so it does not depend on any analytic continuation of $Z_X$; only on the Euler-product region $\mathrm{Re}(s)>\delta$.
- **$\kappa\in[-\tfrac14,0)$ is included** even though $\phi(\lambda)=\lambda+\kappa$ is then **not Bernstein** (Remark 3.7). The mass formula (26) still converges and the identity is an identity of convergent series; nothing probabilistic is claimed there.
- **Attribution.** The killing identity was first proved in Lemonde–Wang [LW26]; §4.1 recovers it as one row of the criterion.

---

# Consumed by

- [[Thm - Finiteness of the Total Mass]] — the $\phi(\lambda)=\lambda+\kappa$ row
- [[Constr - The Probability Measure on Free Homotopy Classes]] — $-\log Z_X(s)$ is the normalising constant
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)]] — the finite-area divergence is what §5 renormalises
- [[Thm - Moments of the Length via the Selberg Zeta Function]] — differentiating (35) in $s$
- [[Thm - Distribution of the Total Homology of the Loop Soup]] — $\#\mathcal{L}^*_\lambda\sim\mathrm{Poisson}(-\lambda\log Z_X(s))$
- [[§4 Zeta Identities and Finiteness of the Total Mass]] §4.1.1

---

# Commentary

> [!note]- Commentary (skippable)
> This is the paper's central identity, and it is worth stating in words: **the total Brownian-with-killing loop mass, summed over all non-trivial free homotopy classes, is exactly $-\log Z_X(s)$ with $s(s-1)=\kappa$.** A probabilistic quantity on the left, a number-theoretic one on the right, and the bridge is nothing more elaborate than two geometric series.
>
> Reading it as a partition function (Remark 4.4): with $Z(s):=Z_X(s)^{-1}=\prod_\gamma\prod_{k\geq0}(1-e^{-(s+k)\ell_\gamma})^{-1}$, (35) says the total mass is $\log Z(s)$, the free energy of a free Bose gas whose modes are indexed by pairs (primitive geodesic, $k\geq0$) with energies $(s+k)\ell_\gamma$. Combined with [[Thm - Poissonian Structure of Homotopy Classes|Prop 3.8]], the non-interacting Bose gas and the Poisson loop soup are the same object described twice.
>
> The dichotomy at $\kappa=0$ is the hinge of the second half of the paper. Infinite area: everything is finite, the probability measure of §6 exists immediately. Finite area: the sum diverges, and one must either add killing ($\kappa>0$, so $s>1=\delta$) or renormalise — which is §5, and which is where the zeta-regularised determinant enters.
