---
type: paper-section
paper: "Belyaev–Huseynli, A probability measure on homotopy & homology classes via Brownian loops"
section: "6 — A probability measure on homotopy and homology classes"
tags: [paper, brownian-loops, spectral-geometry, homology]
---

# §6 — A probability measure on homotopy and homology classes

Back to the [[Paper - Brownian Loops — Homotopy and Homology|hub]]. Now the payoff. §4–§5 made the total loop mass finite (a Selberg zeta value, or a determinant after renormalisation); dividing each class-mass by that total turns the loop measure into an honest **probability measure on topological types**. §6.1 does this for free homotopy classes and reads off the moments of the geodesic length from derivatives of the Selberg zeta; §6.2 coarsens to **homology** classes and uses Fourier analysis on the abelian group $H_1(X,\mathbb{Z})$ (via Selberg $L$-functions) to extract the mass in each class and the distribution of the loop soup's total homology.

**Symbols.** $s=\frac12+\sqrt{\frac14+\kappa}$, $\kappa>0$; $Z_X$ the Selberg zeta, $L_X(s,\chi)$ the Selberg $L$-function; $H_1(X,\mathbb{Z})$ first homology, $\chi$ a unitary character, $\beta$ a homology class; $L=m\ell_\gamma$ the geodesic length (a random variable under the measure).

---

## §6.1 — A probability measure on free homotopy classes

> **Definition (probability measure on homotopy classes).** With $\kappa>0$ and $s=\frac12+\sqrt{\frac14+\kappa}$,
> $$\mathbb P_s\big(C_X(\gamma^m)\big):=\frac{\mu^\kappa_X(C_X(\gamma^m))}{-\log Z_X(s)}=\frac{\mu^\kappa_X(C_X(\gamma^m))}{\sum_{\gamma\in\mathcal P_X}\sum_{m\ge1}\mu^\kappa_X(C_X(\gamma^m))}.$$

This is a genuine probability measure: the masses are positive and sum to $-\log Z_X(s)$ ([[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]]), which is finite and positive for $s>\delta$. Stub: [[Def - Probability Measure on Homotopy Classes]]. The natural random variable is the geodesic length $L=m\ell_\gamma$; its moments come for free from the Selberg zeta.

**Moments via the zeta function (gap-free).** Write $F(s):=-\log Z_X(s)=\sum_{\gamma,m}\mu^\kappa_X(C_X(\gamma^m))$ for the total mass. Since $\mu^\kappa_X(C_X(\gamma^m))$ depends on $s$ only through the factor $e^{(1-s)m\ell_\gamma}$,
$$\frac{d}{ds}\mu^\kappa_X(C_X(\gamma^m))=-(m\ell_\gamma)\,\mu^\kappa_X(C_X(\gamma^m))=-L\,\mu^\kappa_X(C_X(\gamma^m)).$$
The clean way to get *all* moments at once is to notice that **shifting $s$ tilts by the length**: for $r>1-s$,
$$\mathbb E_s\big[e^{-rL}\big]=\frac{\sum_{\gamma,m}\mu^\kappa_X(C_X(\gamma^m))\,e^{-rm\ell_\gamma}}{-\log Z_X(s)}=\frac{-\log Z_X(s+r)}{-\log Z_X(s)}=\frac{\log Z_X(s+r)}{\log Z_X(s)},$$
because multiplying the parameter-$s$ summand by $e^{-rm\ell_\gamma}$ gives exactly the parameter-$(s+r)$ summand ($e^{(1-s)m\ell_\gamma}e^{-rm\ell_\gamma}=e^{(1-(s+r))m\ell_\gamma}$). Differentiating $F$ $n$ times pulls down $(m\ell_\gamma)^n=L^n$ with sign $(-1)^n$, so $\sum_{\gamma,m}\mu^\kappa_X(C_X(\gamma^m))L^n=(-1)^nF^{(n)}(s)$ and hence **all moments**:
$$\mathbb E_s[L^n]=\frac{(-1)^nF^{(n)}(s)}{F(s)},\qquad n\ge1.$$
The first two cumulants are derivatives of $\log F$:
$$\mathbb E_s[L]=-\frac{d}{ds}\log\big(-\log Z_X(s)\big)=-\frac{F'(s)}{F(s)}=-\frac{Z_X'(s)}{Z_X(s)\log Z_X(s)},\qquad \operatorname{Var}_s(L)=\frac{d^2}{ds^2}\log\big(-\log Z_X(s)\big)=\frac{F''(s)F(s)-F'(s)^2}{F(s)^2}.$$
Since $\log F$ is strictly convex on $(1,\infty)$ (as $\operatorname{Var}_s(L)>0$), $s\mapsto\mathbb E_s[L]$ is strictly decreasing: **more killing shortens the typical class**, as expected.

**The systole limit ($s\to\infty$).** As $s\to\infty$ the weights $\mu^\kappa_X(C_X(\gamma^m))\sim e^{-sm\ell_\gamma}$ are dominated by the primitive ($m=1$) classes of shortest length — the **systole** $\ell_{\mathrm{sys}}=\min_\gamma\ell_\gamma$. Because a hyperbolic element of a torsion-free Fuchsian group is never conjugate to its inverse, the systole is realised by at least two oriented classes, $N_{\mathrm{sys}}:=\#\{\gamma\in\mathcal P_X:\ell_\gamma=\ell_{\mathrm{sys}}\}\ge2$. The measure concentrates uniformly on the systolic classes:
$$\mathbb P_s(C_X(\gamma))\xrightarrow{s\to\infty}\frac{1}{N_{\mathrm{sys}}}\ (\ell_\gamma=\ell_{\mathrm{sys}}),\quad\mathbb P_s(C_X(\gamma^m))\xrightarrow{s\to\infty}0\ (\text{else}),\quad\mathbb E_s[L]\xrightarrow{s\to\infty}\ell_{\mathrm{sys}}.$$
Analytically this is visible in $-\log Z_X(s)\sim\frac{N_{\mathrm{sys}}}{1-e^{-\ell_{\mathrm{sys}}}}e^{-s\ell_{\mathrm{sys}}}$ as $s\to\infty$ (only the $N_{\mathrm{sys}}$ primitive systolic terms survive), so the systole *and* its multiplicity are recovered from asymptotics: $\ell_{\mathrm{sys}}=-\lim_{s\to\infty}\frac1s\log(-\log Z_X(s))$ and $N_{\mathrm{sys}}=(1-e^{-\ell_{\mathrm{sys}}})\lim_{s\to\infty}e^{s\ell_{\mathrm{sys}}}(-\log Z_X(s))$.

---

## §6.2 — A probability measure on homology classes

Homotopy is a fine partition (a conjugacy class in the non-abelian $\Gamma$); **homology** is much coarser — it forgets the order handles are traversed and keeps only net winding.

> [!recall]- First homology, characters, character orthogonality
> **Formally:** the **first homology group** $H_1(X,\mathbb{Z})$ of a hyperbolic surface $X$ is the **abelianisation** of its fundamental group $\Gamma$: quotient $\Gamma$ by its commutator subgroup $[\Gamma,\Gamma]$ (the subgroup generated by all elements $ghg^{-1}h^{-1}$). Concretely $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$ where $r=2g$ for a closed genus-$g$ surface and $r=2g+b-1$ for a surface with $b$ boundary ends. The Hurewicz map $\Gamma\twoheadrightarrow H_1$ sends $\gamma\mapsto[\gamma]$; iterating gives $[\gamma^m]=m[\gamma]$. A **unitary character** $\chi:H_1\to S^1$ (the unit circle in $\mathbb{C}$) is a group homomorphism into complex numbers of modulus $1$; the set $\widehat{H_1}$ of all such is itself a group (the *dual group*), isomorphic to the torus $(S^1)^r$. Characters satisfy the **orthogonality relation** $\int_{\widehat{H_1}}\chi(\beta')\,\overline{\chi(\beta)}\,d\chi=\mathbf 1_{\beta'=\beta}$ under normalised Haar measure $d\chi$.
> **In words:** homology forgets everything about a loop except its *net winding* around each hole. Two loops are in the same free homotopy class if you can slide one into the other; they are in the same *homology* class if you additionally allow rearranging the order of the winding — commuting the group operation. Characters are the "Fourier modes" of the homology group: each character assigns a complex-number-of-modulus-one to each homology class, and the orthogonality relation is exactly Fourier inversion adapted to this group. So writing a function on $H_1$ as a sum of character values, then integrating against a specific character, extracts the coefficient on one specific homology class — the same recipe as Fourier series on the circle.
> **Concretely:** for the closed torus $X=T^2$ (genus $1$), $\Gamma=\pi_1(T^2)=\mathbb{Z}^2$ is already abelian, so $[\Gamma,\Gamma]=\{0\}$ and $H_1(T^2,\mathbb{Z})=\mathbb{Z}^2$: a class is an integer pair $(a,b)=$ (net winding around meridian, net winding around longitude). A character $\chi_{(u,v)}(a,b):=e^{2\pi i(au+bv)}$ is parametrised by $(u,v)$ in the "dual torus" $\widehat{H_1}=[0,1)^2$; the orthogonality relation $\int_0^1\int_0^1 e^{2\pi i((a'-a)u+(b'-b)v)}\,du\,dv=\mathbf 1_{a=a',b=b'}$ is elementary 2-D Fourier orthogonality. For a genus-2 surface, $\Gamma$ has 4 generators (2 per handle) with one commutator relation, so $H_1=\mathbb{Z}^4$ and characters live on the 4-torus. See [[Def - First Homology, Characters, and Finite Fourier Analysis]].

> **Definition 6.1 (mass in a homology class).** For $\beta\in H_1(X,\mathbb{Z})$ and $s=\frac12+\sqrt{\frac14+\kappa}$, $\operatorname{Re}s>\delta$,
> $$\mu^\kappa_X(\beta):=\sum_{\substack{\gamma\in\mathcal P_X,\,m\ge1\\ m[\gamma]=\beta}}\mu^\kappa_X(C_X(\gamma^m))=\sum_{\substack{\gamma,m\\ m[\gamma]=\beta}}\frac1m\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1},$$
> the loop mass summed over the infinitely many free homotopy classes lying in $\beta$.

Stub: [[Def - Mass in a Homology Class]].

**Remark 6.2 (provenance and motivation).** A notion of Brownian loop measure on homology classes appeared earlier in Le Jan's work [LJ11]; the authors developed the definition above independently (differing conventions made the earlier one initially opaque to them) and then found the two agree, with the Selberg-$L$-function route here giving a *dual* approach that recovers Le Jan's results in greater generality — in particular extending to the non-compact case. The motivation for grading by homology rather than homotopy: geometric intersection numbers of geodesics are homotopy invariants, but *algebraic* intersection numbers are defined on homology, so the homology-graded measure is the right object for intersection questions. The technical fact that makes homology tractable is that the character weight $\chi([\gamma])^m=\chi(m[\gamma])$ appearing below depends only on the homology class $\beta=m[\gamma]$ of the iterate, not on the representative geodesic — so the double sum may be regrouped by $\beta$.

To detect this by homology one twists the Selberg zeta by a character — the exact analogue of Dirichlet $L$-functions detecting primes in arithmetic progressions.

> **Definition 6.3 (Selberg $L$-function).** For a unitary character $\chi:H_1(X,\mathbb{Z})\to S^1$ and $\operatorname{Re}s>\delta$,
> $$L_X(s,\chi):=\prod_{\gamma\in\mathcal P_X}\prod_{k=0}^\infty\big(1-\chi([\gamma])\,e^{-(s+k)\ell_\gamma}\big),$$
> the Selberg zeta twisted by the one-dimensional representation $\chi$ (trivial $\chi\Rightarrow L_X(s,\chi)=Z_X(s)$); it continues meromorphically to $\mathbb{C}$.

Stub: [[Def - Selberg L-Function]]. Its log-expansion (same computation as $Z_X$, with the character weight $\chi([\gamma])^m=\chi(m[\gamma])$ inserted) gives:

> **Corollary 6.4 ($L$-function identity).** For unitary $\chi$ and $s=\frac12+\sqrt{\frac14+\kappa}$, $\operatorname{Re}s>\delta$,
> $$-\log L_X(s,\chi)=\sum_{\gamma}\sum_{m\ge1}\chi([\gamma])^m\,\mu^\kappa_X(C_X(\gamma^m))=\sum_\gamma\sum_{m\ge1}\frac1m\,\chi([\gamma])^m\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}.$$
> *(Proof: expand $-\log(1-z)=\sum_m z^m/m$ with $z=\chi([\gamma])e^{-(s+k)\ell_\gamma}$, $|z|=e^{-(\operatorname{Re}s+k)\ell_\gamma}<1$ since $|\chi([\gamma])|=1$; sum over $k$ via $\sum_{k\ge0}e^{-(s+k)m\ell_\gamma}=e^{(1-s)m\ell_\gamma}/(e^{m\ell_\gamma}-1)$; the character weight is $\chi([\gamma])^m$.)*

The key point: since $\chi([\gamma])^m=\chi(m[\gamma])=\chi(\beta)$ whenever $m[\gamma]=\beta$, the double sum **regroups by homology class** — which is exactly a Fourier expansion.

> **Theorem 6.5 (Fourier expansion and inversion by homology class).** For $\operatorname{Re}s>\delta$ and every unitary $\chi\in\widehat{H_1(X,\mathbb{Z})}$,
> $$-\log L_X(s,\chi)=\sum_{\beta\in H_1(X,\mathbb{Z})}\chi(\beta)\,\mu^\kappa_X(\beta),\qquad\text{and inversely}\qquad \mu^\kappa_X(\beta)=\int_{\widehat{H_1(X,\mathbb{Z})}}\big(-\log L_X(s,\chi)\big)\,\overline{\chi(\beta)}\,d\chi.$$

> [!note]- Gap-free proof of Theorem 6.5
> **Step 1 — regroup Corollary 6.4 by homology class.** In $-\log L_X(s,\chi)=\sum_{\gamma,m}\chi([\gamma])^m\mu^\kappa_X(C_X(\gamma^m))$, use $\chi([\gamma])^m=\chi(m[\gamma])$ and collect all $(\gamma,m)$ with the same $\beta=m[\gamma]$:
> $$-\log L_X(s,\chi)=\sum_{\beta\in H_1(X,\mathbb{Z})}\Big(\sum_{\substack{\gamma,m\\ m[\gamma]=\beta}}\mu^\kappa_X(C_X(\gamma^m))\Big)\chi(\beta)=\sum_{\beta}\mu^\kappa_X(\beta)\,\chi(\beta),$$
> by Definition 6.1. This is the Fourier expansion (its coefficients are the homology masses).
> **Step 2 — invert by character orthogonality.** Multiply by $\overline{\chi(\beta)}$ and integrate over the character torus $\widehat{H_1}$ against normalised Haar measure $d\chi$; absolute convergence (from $\operatorname{Re}s>\delta$) lets us swap sum and integral:
> $$\int_{\widehat{H_1}}\big(-\log L_X(s,\chi)\big)\overline{\chi(\beta)}\,d\chi=\sum_{\beta'}\mu^\kappa_X(\beta')\int_{\widehat{H_1}}\chi(\beta')\overline{\chi(\beta)}\,d\chi.$$
> By [[Def - First Homology, Characters, and Finite Fourier Analysis|character orthogonality]] the inner integral is $\mathbf 1_{\beta'=\beta}$, so only $\beta'=\beta$ survives, giving $\mu^\kappa_X(\beta)=\int_{\widehat{H_1}}(-\log L_X(s,\chi))\overline{\chi(\beta)}\,d\chi$. $\blacksquare$

Stub: [[Thm - Fourier Inversion by Homology Class]].

**Remark 6.6 (Jacobian form of the inversion, closed case).** On a closed surface the character torus is the (real) Jacobian $\widehat{H_1(X,\mathbb{Z})}\cong\operatorname{Jac}(X)$: a harmonic $1$-form $\omega$ gives the character $\chi_{[\omega]}(\beta)=e^{2\pi i\int_\beta\omega}$, and the inversion formula of Theorem 6.5 becomes
$$\mu^\kappa_X(\beta)=\int_{\operatorname{Jac}(X)}\big(-\log L_X(s,\chi_{[\omega]})\big)\,e^{-2\pi i\int_\beta\omega}\,d[\omega],$$
with $d[\omega]$ the normalised Haar measure on the Jacobian torus. This is the same statement as Theorem 6.5, written in the Hodge-theoretic coordinates that make the characters explicit periods of harmonic forms.

Finally, the loop soup's total homology has an explicit distribution.

> **Proposition 6.7 (distribution of the loop soup's total homology).** Let $\mathcal L_\lambda$ be the [[Def - Poisson Point Process and the Loop Soup|loop soup]] of intensity $\lambda>0$, and $\beta(\lambda):=\sum_{\eta\in\mathcal L^*_\lambda}[\eta]\in H_1(X,\mathbb{Z})$ the total homology of its non-contractible, non-cusp-peripheral loops (a finite sum: $\#\mathcal L^*_\lambda$ is Poisson with mean $-\lambda\log Z_X(s)<\infty$). Then for every unitary $\chi$,
> $$\mathbb E\big[\chi(\beta(\lambda))\big]=\Big(\frac{Z_X(s)}{L_X(s,\chi)}\Big)^{\!\lambda},\qquad\text{and}\qquad \mathbb P\big(\beta(\lambda)=\beta\big)=Z_X(s)^\lambda\int_{\widehat{H_1}}L_X(s,\chi)^{-\lambda}\,\overline{\chi(\beta)}\,d\chi.$$

> [!note]- Gap-free proof of Proposition 6.7
> **Step 1 — the Poisson exponential (Campbell) formula.** For a Poisson process $\mathcal L_\lambda$ of intensity $\lambda\mu^\kappa_X$ and any measurable $F$ on loops with $\int(e^{F}-1)\,d\mu^\kappa_X<\infty$, $\mathbb E\big[\prod_{\eta\in\mathcal L_\lambda}e^{F(\eta)}\big]=\exp\big(\lambda\int(e^{F(\eta)}-1)\,\mu^\kappa_X(d\eta)\big)$.
> **Step 2 — choose $e^{F}=\chi([\eta])$.** Then $\prod_\eta e^{F(\eta)}=\chi\big(\sum_{\eta\in\mathcal L^*_\lambda}[\eta]\big)=\chi(\beta(\lambda))$, and the exponent is
> $$\lambda\int(\chi([\eta])-1)\,\mu^\kappa_X(d\eta)=\lambda\sum_{\gamma,m}(\chi([\gamma])^m-1)\,\mu^\kappa_X(C_X(\gamma^m))=\lambda\big(-\log L_X(s,\chi)+\log Z_X(s)\big),$$
> using Corollary 6.4 above for the $\chi([\gamma])^m$ term and [[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]] ($\chi\equiv1$) for the $-1$ term. Exponentiating gives $\mathbb E[\chi(\beta(\lambda))]=(Z_X(s)/L_X(s,\chi))^\lambda$.
> **Step 3 — invert.** Multiply by $\overline{\chi(\beta)}$ and integrate over $\widehat{H_1}$; character orthogonality isolates $\beta$, giving $\mathbb P(\beta(\lambda)=\beta)=Z_X(s)^\lambda\int_{\widehat{H_1}}L_X(s,\chi)^{-\lambda}\overline{\chi(\beta)}\,d\chi$. $\blacksquare$

Stub: [[Prop - Total Homology of the Loop Soup]]. Continue to [[Paper - Brownian Loops — Homotopy and Homology — §7 Hyperbolic 3-Manifolds|§7]], which lifts everything to hyperbolic 3-manifolds.

---

## Section verification log (§6)

**Verified.** The probability measure and its moment generating identity $\mathbb E_s[e^{-rL}]=\log Z_X(s+r)/\log Z_X(s)$, all moments $\mathbb E_s[L^n]=(-1)^nF^{(n)}(s)/F(s)$, mean/variance as $\log F$ derivatives, and the systole limit are reproduced in full. Corollary 6.4, Theorem 6.5 (Fourier inversion via character orthogonality), and Proposition 6.7 (via the Poisson exponential formula) are proved gap-free.
**Flagged / uncertain.** The character-orthogonality integral and the Poisson exponential (Campbell) formula are standard results, recalled/linked (their own atomic notes carry the citations). No unresolved uncertainties.
**Intuition not yet formalised.** The Jacobian reformulation (Remark 6.6) is stated; the Hodge-theoretic identification $\widehat{H_1}\cong\operatorname{Jac}(X)$ is recalled from the homology note, not re-derived (external, closed-case only).
