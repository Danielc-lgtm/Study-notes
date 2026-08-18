---
type: paper-section
paper: "Belyaev–Huseynli, A probability measure on homotopy & homology classes via Brownian loops"
section: "4 — Zeta functions and the total mass"
tags: [paper, brownian-loops, zeta-functions, spectral-geometry]
---

# §4 — Zeta functions and the total mass of Brownian loops

Back to the [[Paper - Brownian Loops — Homotopy and Homology|hub]]. §3 gave each free homotopy class a finite, closed-form mass. This section **sums those masses over all classes** and recognises the sum as a classical object: a value of the **Selberg zeta function**. That identification is the paper's bridge from probability to spectral geometry, and it comes with a companion (the Ruelle zeta, twisted by a representation) and a sharp convergence criterion (the total mass is finite exactly when the loops decay faster than geodesics proliferate). Throughout, *total mass* means the sum over **non-trivial, non-peripheral** classes; the full loop measure is always infinite because of the trivial (contractible) class.

**Symbols.** $s\in\mathbb{C}$ the spectral/zeta variable (distinct from the §2 subordination variable); $\delta$ the critical exponent; $Z_X,R_X$ the Selberg and Ruelle zeta functions; $I_\phi$ the [[Def - The Loop-Length Integral|loop-length integral]]; $L=m\ell_\gamma$.

---

## §4.1 — Selberg zeta identities

> [!recall]- Selberg zeta function and critical exponent
> **Formally:** $Z_X(s)=\prod_{\gamma\in\mathcal P_X}\prod_{k\ge0}(1-e^{-(s+k)\ell_\gamma})$ for $\operatorname{Re}s>\delta$, with $-\log Z_X(s)=\sum_{\gamma}\sum_{m\ge1}\frac1m\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$; the **critical exponent** $\delta$ is the exponent of convergence of $\sum_{h\in\Gamma}e^{-s\,d(z,hz)}$ ($\delta=1$ finite area, $\delta<1$ infinite area). See [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]].
> **In words:** the generating function of the length spectrum — the geodesics' analogue of the Riemann zeta over primes; $\delta$ is how fast geodesics multiply.

The engine of §4.1 is a matching lemma: whenever the §3 mass has the *shape* $\frac{L}{2\sinh(L/2)}I_\phi(L)=C\,e^{(1-s)L}/(e^L-1)$, the total mass is a Selberg zeta value.

> **Lemma 4.2 (Selberg zeta criterion).** Suppose there are constants $C>0$ and real $s>\delta$, independent of $L$, with
> $$\frac{L}{2\sinh(L/2)}\,I_\phi(L)=C\cdot\frac{e^{(1-s)L}}{e^{L}-1}\qquad(L>0).$$
> Then $\displaystyle\sum_{\gamma\in\mathcal P_X}\sum_{m=1}^\infty\mu^\phi_X(C_X(\gamma^m))=-C\log Z_X(s)$.

> [!note]- Gap-free proof of Lemma 4.2
> **Step 1 — rewrite one class-mass.** By [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] and $L=m\ell_\gamma$ (so $\ell_\gamma/L=1/m$),
> $$\mu^\phi_X(C_X(\gamma^m))=\frac{\ell_\gamma}{2\sinh(L/2)}I_\phi(L)=\frac1m\cdot\frac{L}{2\sinh(L/2)}I_\phi(L).$$
> **Step 2 — apply the hypothesis.** Substituting the assumed shape, $\mu^\phi_X(C_X(\gamma^m))=C\cdot\frac1m\cdot\frac{e^{(1-s)L}}{e^{L}-1}=C\cdot\frac1m\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$.
> **Step 3 — sum and recognise $-\log Z_X$.** Summing over $\gamma\in\mathcal P_X$ and $m\ge1$,
> $$\sum_{\gamma,m}\mu^\phi_X(C_X(\gamma^m))=C\sum_{\gamma}\sum_{m\ge1}\frac1m\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}=-C\log Z_X(s),$$
> the last equality being exactly the log-expansion of the [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent|Selberg zeta]]. The rearrangement is legitimate because $s>\delta$ makes the double series absolutely convergent (all terms positive when $C>0$, $s$ real). $\blacksquare$

**§4.1.1 — the killing case (Corollary 4.3).** For $\phi(\lambda)=\lambda+\kappa$, §3.1 gave $I_\kappa(L)=e^{-L\sqrt{1/4+\kappa}}/L$, so
$$\frac{L}{2\sinh(L/2)}I_\kappa(L)=\frac{e^{-L\sqrt{1/4+\kappa}}}{2\sinh(L/2)}=\frac{e^{-L\sqrt{1/4+\kappa}}}{e^{L/2}-e^{-L/2}}=\frac{e^{-L(\sqrt{1/4+\kappa}-1/2)}}{e^{L}-1}=\frac{e^{(1-s)L}}{e^L-1},$$
with $s=\frac12+\sqrt{\frac14+\kappa}$ (check: $1-s=\frac12-\sqrt{\frac14+\kappa}=-(\sqrt{1/4+\kappa}-1/2)$) and $C=1$. Lemma 4.2 gives:

> **Corollary 4.3 (Selberg zeta identity).** For $\kappa\ge-\frac14$ with $s=\frac12+\sqrt{\frac14+\kappa}>\delta$,
> $$\sum_{\gamma\in\mathcal P_X}\sum_{m=1}^\infty\mu^\kappa_X(C_X(\gamma^m))=-\log Z_X\!\Big(\frac12+\sqrt{\frac14+\kappa}\Big).$$
> In particular $\kappa=0$ ($s=1$): the total Brownian loop mass is $-\log Z_X(1)$, finite iff $\delta<1$ (infinite area) and divergent when $\delta=1$ (finite area).

Stubs: [[Lemma - Selberg Zeta Criterion]], [[Thm - Selberg Zeta Identity for the Total Loop Mass]].

**Remark 4.4 (bosonic partition function).** Writing $Z_\gamma(s)=\prod_{k\ge0}(1-e^{-(s+k)\ell_\gamma})^{-1}$ and $\mathcal Z(s)=\prod_\gamma Z_\gamma(s)=Z_X(s)^{-1}$, the identity reads $\sum_{\gamma,m}\mu^\kappa_X(C_X(\gamma^m))=\log\mathcal Z(s)$. Each $Z_\gamma(s)$ is the partition function of bosonic modes indexed by $k\ge0$ with energies $(s+k)\ell_\gamma$, so $\mathcal Z(s)$ is the grand-canonical partition function of a free Bose gas at zero chemical potential — the total loop mass is its log. ⚠️ *(Physical interpretation; the mathematical content is the zeta identity above.)*

**§4.1.2 — Ruelle and twisted Ruelle (Corollary 4.6).**

> [!recall]- Ruelle zeta and its twist by a representation
> **Formally:** $R_X(s)=\prod_\gamma(1-e^{-s\ell_\gamma})=Z_X(s)/Z_X(s+1)$; for a finite-dimensional $\rho:\Gamma\to\mathrm{GL}(V_\rho)$ with $\tau$ representing $\gamma$'s class, $R_X(s,\rho)=\prod_\gamma\det(I-\rho(\tau)e^{-s\ell_\gamma})$, converging for $\operatorname{Re}s>c_\rho$ ($c_\rho=\delta$ if $\rho$ unitary). See [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]].
> **In words:** a one-factor-per-geodesic zeta; the twist weights each geodesic by a matrix, so the total "mass" becomes a trace — the device §6 uses to project onto a homology class.

> **Corollary 4.6 (twisted Ruelle identity).** Set $\kappa_-(s):=s(s-1)$, $\kappa_+(s):=s(s+1)$; for $\operatorname{Re}s>\frac12$ the principal root gives $\frac12+\sqrt{\frac14+\kappa_-(s)}=s$ and $\frac12+\sqrt{\frac14+\kappa_+(s)}=s+1$. Then for $\operatorname{Re}s>\max(c_\rho,\frac12)$,
> $$-\log R_X(s,\rho)=\sum_{\gamma}\sum_{m\ge1}\operatorname{tr}\rho(\tau^m)\big[\mu^{\kappa_-(s)}_X(C_X(\gamma^m))-\mu^{\kappa_+(s)}_X(C_X(\gamma^m))\big]=\sum_\gamma\sum_{m\ge1}\frac{\operatorname{tr}\rho(\tau^m)\,e^{-sm\ell_\gamma}}{m}.$$

> [!note]- Gap-free proof of Corollary 4.6
> **Step 1 — expand the twisted product.** With $-\log\det(I-M)=\sum_{m\ge1}\operatorname{tr}(M^m)/m$ (valid for $\|M\|<1$; here $M=\rho(\tau)e^{-s\ell_\gamma}$, and $\rho(\tau^m)=\rho(\tau)^m$ since $\rho$ is a homomorphism),
> $$-\log R_X(s,\rho)=\sum_\gamma\sum_{m\ge1}\frac{\operatorname{tr}\rho(\tau^m)\,e^{-sm\ell_\gamma}}{m}.$$
> This is the right-hand equality; it remains to match it to the mass difference.
> **Step 2 — evaluate the mass difference.** By the killed-mass formula (§3.1.2), $\mu^\kappa_X(C_X(\gamma^m))=\frac1m\frac{e^{(1-\sigma)L}}{e^L-1}$ with $\sigma=\frac12+\sqrt{\frac14+\kappa}$ and $L=m\ell_\gamma$. For $\kappa_-(s)$ the spectral parameter is $\sigma_-=s$, for $\kappa_+(s)$ it is $\sigma_+=s+1$ (the stated root identities). Hence
> $$\mu^{\kappa_-(s)}_X(C_X(\gamma^m))-\mu^{\kappa_+(s)}_X(C_X(\gamma^m))=\frac1m\cdot\frac{e^{(1-s)L}-e^{(1-(s+1))L}}{e^L-1}=\frac1m\cdot\frac{e^{(1-s)L}-e^{-sL}}{e^L-1}.$$
> Factor the numerator: $e^{(1-s)L}-e^{-sL}=e^{-sL}(e^{L}-1)$. So the difference is $\frac1m\cdot\frac{e^{-sL}(e^L-1)}{e^L-1}=\frac{e^{-sL}}{m}=\frac{e^{-sm\ell_\gamma}}{m}$.
> **Step 3 — insert the trace and sum.** Multiplying by $\operatorname{tr}\rho(\tau^m)$ and summing reproduces Step 1's series term by term, giving the middle expression $=$ the right expression $=-\log R_X(s,\rho)$. Absolute convergence for $\operatorname{Re}s>\max(c_\rho,\frac12)$ comes from that of the twisted product. $\blacksquare$

Stub: [[Thm - Twisted Ruelle Zeta Identity]]. The difference $\mu^{\kappa_-}-\mu^{\kappa_+}$ isolates each class's *net* contribution between two killing rates — the mechanism that makes the trace-weighted sum telescope to a clean $e^{-sm\ell_\gamma}/m$.

---

## §4.2 — Finiteness of the total mass

When is the summed mass finite? The answer is a race between the loops' decay rate $s$ and the geodesics' proliferation rate $\delta$.

> [!recall]- Prime geodesic theorem
> **Formally:** $N_X(R):=\#\{\gamma\in\mathcal P_X:\ell_\gamma\le R\}\sim e^{\delta R}/(\delta R)$ as $R\to\infty$. See [[Thm - Prime Geodesic Theorem]].
> **In words:** closed geodesics are the "primes" of $X$ and multiply exponentially at rate $\delta$.

> **Corollary 4.7 (finiteness).** For any Bernstein $\phi$ in the paper, with spectral parameter $s=s(\phi)$ ($s=1$ for Brownian and $\alpha$-stable; $s=\frac12+\sqrt{\frac14+\kappa}$ for killing/shifted-stable): if $s(\phi)>\delta$ then $\sum_{\gamma,m}\mu^\phi_X(C_X(\gamma^m))<\infty$.

> [!note]- Gap-free proof of Corollary 4.7
> In each case $\mu^\phi_X(C_X(\gamma^m))=\frac{C}{m}\frac{e^{(1-s)L}}{e^L-1}$, $L=m\ell_\gamma$, $s=s(\phi)$, $C>0$ ($C=1$ Brownian/killing, $C=\alpha/2$ stable).
> **Step 1 — sum over iterates $m$, reduce to a geodesic sum.** Let $\ell_{\mathrm{sys}}=\min_\gamma\ell_\gamma$ be the systole (shortest closed geodesic). For $L\ge\ell_{\mathrm{sys}}$, $e^L-1\ge(1-e^{-\ell_{\mathrm{sys}}})e^L$, so $\frac{e^{(1-s)L}}{e^L-1}\le\frac{e^{-sL}}{1-e^{-\ell_{\mathrm{sys}}}}$. Using $\sum_{m\ge1}x^m/m=-\log(1-x)$ with $x=e^{-s\ell_\gamma}$,
> $$\sum_{m\ge1}\mu^\phi_X(C_X(\gamma^m))\le\frac{C}{1-e^{-\ell_{\mathrm{sys}}}}\sum_{m\ge1}\frac{e^{-sm\ell_\gamma}}{m}=-\frac{C}{1-e^{-\ell_{\mathrm{sys}}}}\log\big(1-e^{-s\ell_\gamma}\big).$$
> Keeping only $m=1$ gives the lower bound $\sum_{m\ge1}\mu^\phi_X(C_X(\gamma^m))\ge C\frac{e^{(1-s)\ell_\gamma}}{e^{\ell_\gamma}-1}\ge C\,e^{-s\ell_\gamma}$. Since $N_X(R)<\infty$ for each $R$, $\ell_\gamma\to\infty$ along $\mathcal P_X$, so $e^{-s\ell_\gamma}\to0$ and $-\log(1-x)=x+O(x^2)$ makes the upper bound asymptotically $\frac{C}{1-e^{-\ell_{\mathrm{sys}}}}e^{-s\ell_\gamma}$. **Therefore the total mass is finite iff $\sum_{\gamma\in\mathcal P_X}e^{-s\ell_\gamma}<\infty$.**
> **Step 2 — evaluate the geodesic sum via the counting function.** Write the sum as a Stieltjes integral against $N_X$ and integrate by parts on $[0,T]$ (using $N_X(R)=0$ for $R<\ell_{\mathrm{sys}}$):
> $$\sum_{\ell_\gamma\le T}e^{-s\ell_\gamma}=\int_0^T e^{-sR}\,dN_X(R)=e^{-sT}N_X(T)+s\int_0^T e^{-sR}N_X(R)\,dR.$$
> By the [[Thm - Prime Geodesic Theorem|prime geodesic theorem]], $N_X(R)\asymp e^{\delta R}/R$ for large $R$, so the integrand $\asymp e^{-(s-\delta)R}/R$, and $\int^\infty e^{-(s-\delta)R}/R\,dR$ converges iff $s>\delta$ (at $s=\delta$ it diverges like $\int^\infty dR/R$; for $s<\delta$ worse). For $s>\delta$ the boundary term $e^{-sT}N_X(T)\to0$, so the sum converges — the total mass is finite. $\blacksquare$

Stub: [[Thm - Finiteness of the Total Loop Mass]]. **The threshold is sharp:** at $s=\delta$ the sum diverges, and since $-\log Z_X(s)\uparrow$ this divergent sum as $s\downarrow\delta$, monotone convergence gives $Z_X(s)\to0$ as $s\downarrow\delta$ — the total mass blows up at the critical exponent. For finite area ($\delta=1$), a strictly positive killing rate $\kappa>0$ (i.e. $s>1$) is needed to make the total mass finite; this sets up §5, where the *contractible* class's divergence is renormalised. Continue to [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5]].

---

## Section verification log (§4)

**Verified.** Lemma 4.2, Corollary 4.3 (with the $s=\frac12+\sqrt{1/4+\kappa}$ and $C=1$ computation), Corollary 4.6 (twisted Ruelle; the numerator factorisation $e^{(1-s)L}-e^{-sL}=e^{-sL}(e^L-1)$ made explicit), and Corollary 4.7 (both the sum-over-$m$ reduction and the integration-by-parts against $N_X$) rewritten gap-free. The Selberg/Ruelle zeta facts and the prime geodesic theorem are external inputs, stated + typed + cited (atomic notes).
**Flagged / uncertain.** The zeta variable is $s$ throughout §4 (matching the paper); it is *not* the §2 subordination variable — noted in the symbols line. No unresolved uncertainties.
**Intuition not yet formalised.** Remark 4.4's Bose-gas reading is physical interpretation (flagged); the mathematics is the zeta identity.
