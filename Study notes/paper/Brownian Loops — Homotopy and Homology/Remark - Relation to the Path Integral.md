---
type: remark
subject: probability-geometry
prereqs:
  - "Thm - Mass of a Free Homotopy Class"
  - "Def - Brownian Loop Measure"
  - "Def - Dirichlet Form Loop Measure"
  - "Def - Zeta-Regularised Determinant of the Laplacian"
tags: [paper, brownian-loops, quantum-mechanics, path-integral]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Remark 3.3 (and §3.2 QM digression)"
---

# Notation

- $X$ — a hyperbolic surface (or, more generally, a Riemannian manifold on which the process is defined); $\pi_1(X, x)$ its fundamental group at basepoint $x$.
- $\Delta_X$ — the *positive* Laplace–Beltrami operator on $X$ (the paper's sign convention: $\Delta_X \ge 0$, so $e^{-t\Delta_X}$ is contractive for $t\ge 0$).
- $\hat H$ — the quantum Hamiltonian on $L^2(X)$; the paper takes $\hat H = \frac{\hbar^2}{2m}\Delta_X + V(x)$ with a non-negative potential $V\ge 0$; in units $\hbar^2/2m = 1$ and $V\equiv\kappa$ constant, $\hat H = \Delta_X + \kappa$.
- $\psi(x,t)$ — the wave function; obeys the Schrödinger equation $i\hbar\,\partial_t\psi = \hat H\psi$; solution $\psi(x,t) = e^{-it\hat H/\hbar}\psi(x,0)$.
- $K(t,x,y) = \langle y|e^{-it\hat H/\hbar}|x\rangle$ — the (real-time) propagator; the amplitude for a particle at $x$ to be found at $y$ after time $t$.
- $p(t,x,y)$ — the Brownian heat kernel on $X$ (transition density); after Wick rotation to Euclidean time $\tau$, $p(\tau, x, y) = \langle y|e^{-\tau\Delta_X}|x\rangle$.
- $p_V(t,x,y)$, $p^\kappa(t,x,y)$ — the heat kernel of the Schrödinger operator $\Delta_X + V$, respectively $\Delta_X + \kappa$; $p^\kappa(t,x,y) = e^{-\kappa t}p(t,x,y)$.
- $\mu_X$, $\mu^E_X$, $\mu^\kappa_X$ — the Brownian, Dirichlet-form, and killed-Brownian loop measures on $X$.
- $\chi : \pi_1(X, x) \to U(1)$ — a unitary character of the fundamental group (a group homomorphism to the unit circle).
- $\varphi : X \to \mathbb{R}$ — a real scalar field on $X$; $S_E[\varphi]$ its Euclidean action; $Z^\kappa_X$ its partition function.

> [!recall]- Free homotopy classes $C_X(\gamma^m)$ vs. based homotopy classes $\pi_1(X, x)$
> **Formally:** $\pi_1(X, x)$ is the group of homotopy classes of loops *rooted at* the basepoint $x$ (basepoint fixed throughout the homotopy). The set of *free* homotopy classes (no basepoint) is $\pi_1(X,x)$ modulo conjugation: two based classes $[\alpha], [\beta]$ are freely homotopic iff $[\beta] = [\gamma]^{-1}[\alpha][\gamma]$ for some $[\gamma]\in\pi_1(X,x)$. So free classes $\leftrightarrow$ conjugacy classes in $\pi_1(X, x)$.
> **In words:** the difference is whether the loop is required to close at a fixed reference point (based) or is allowed to close anywhere (free). Fixing the point makes each loop remember more; forgetting it collapses loops-related-by-basepoint-drift into one class.
> **Concretely:** on the figure-eight, the based class of the loop $ab$ (traverse right circle, then left) is different from the based class of $ba$ (left then right) — a based homotopy cannot slide the join-point around. But $ab$ and $ba$ are *freely* homotopic (slide the join around the middle vertex); free classes see them as one class. In group terms, $ba = b(ab)b^{-1}$ is conjugate to $ab$ inside $\pi_1(\text{figure-eight}) = F_2$.

> [!recall]- Unitary character of a group $\chi : G\to U(1)$
> **Formally:** for a discrete group $G$, a *unitary character* is a group homomorphism $\chi : G\to U(1) = \{z\in\mathbb{C} : |z|=1\}$: $\chi(g_1 g_2) = \chi(g_1)\chi(g_2)$ and $\chi(g^{-1}) = \overline{\chi(g)}$. Characters form a group under pointwise multiplication (the *character group*, denoted $\widehat G$ when $G$ is abelian). The trivial character is $\chi\equiv 1$.
> **In words:** a rule that assigns a complex number of modulus $1$ to every group element in a way that respects multiplication. Because $|\chi(g)| = 1$, no information about "size" is carried — only a "phase".
> **Concretely:** for $G = \mathbb{Z}$, every character has the form $\chi(n) = e^{i\theta n}$ for some $\theta\in[0,2\pi)$; the character group is again $U(1)$. For $G = \mathbb{Z}/N\mathbb{Z}$, characters are $\chi(k) = e^{2\pi i k n/N}$, $n\in\{0,\ldots,N-1\}$. For $\pi_1(\text{closed genus-2 surface}) = \langle a,b,c,d : [a,b][c,d] = 1\rangle$, characters factor through the abelianisation $H_1 = \mathbb{Z}^4$, giving a $\mathbb{T}^4$-worth of characters.

> [!recall]- Zeta-regularised determinant $\det(\Delta_X + \kappa)$
> **Formally:** for a self-adjoint non-negative operator $A$ with discrete spectrum $0\le\lambda_1\le\lambda_2\le\cdots$ diverging to $\infty$ on a compact $X$, define the spectral zeta $\zeta_A(s) = \sum_{n\ge 1}\lambda_n^{-s}$ (converges for $\mathrm{Re}\,s$ large; extends meromorphically to $\mathbb{C}$ with $s=0$ regular). Set $\det A := \exp(-\zeta'_A(0))$. Applied to $A = \Delta_X + \kappa$ this is the *zeta-regularised functional determinant*.
> **In words:** an infinite product $\prod_n\lambda_n$ diverges, so it is not literally a determinant. Zeta regularisation replaces the divergent product with the finite quantity $e^{-\zeta'(0)}$, defined via analytic continuation of a spectral zeta function that converges for large real part.
> **Concretely:** on a circle of length $2\pi$, eigenvalues of $\Delta = -d^2/d\theta^2$ (excluding zero mode) are $\{n^2 : n\ge 1\}$ with multiplicity $2$; the zeta $\zeta_\Delta(s) = 2\sum_n n^{-2s} = 2\zeta_R(2s)$ where $\zeta_R$ is the Riemann zeta. Then $\det(\Delta) = e^{-\zeta'_\Delta(0)} = e^{-4\zeta_R'(0)} = e^{4\cdot\frac12\log(2\pi)} = 4\pi^2$. Full detail: [[Def - Zeta-Regularised Determinant of the Laplacian]].

> [!recall]- Heat trace $\operatorname{Tr}(e^{-t\Delta_X}) = \int_X p(t,x,x)\,d\!\operatorname{vol}_g(x)$
> **Formally:** when $e^{-t\Delta_X}$ is trace class (guaranteed for $t>0$ on compact $X$ with $\Delta_X\ge 0$), its trace equals the integral of its diagonal kernel: $\operatorname{Tr}(e^{-t\Delta_X}) = \sum_n e^{-t\lambda_n} = \int_X p(t,x,x)\,d\!\operatorname{vol}_g(x)$, where $p(t,x,y)$ is the kernel and $\lambda_n$ the eigenvalues.
> **In words:** summing $e^{-t\lambda_n}$ over eigenvalues equals integrating the return-probability density $p(t,x,x)$ over the manifold. Trace-of-the-heat-operator = total mass of Brownian round-trips.
> **Concretely:** for $\Delta = -d^2/dx^2$ on $\mathbb{R}/L\mathbb{Z}$ (circle of length $L$), $p(t,x,x) = (4\pi t)^{-1/2}\sum_{n\in\mathbb{Z}}e^{-(nL)^2/4t}$ (Gaussian summed over lattice translates); integrating over $x\in[0,L)$ gives $\operatorname{Tr}(e^{-t\Delta}) = L(4\pi t)^{-1/2}\sum_n e^{-(nL)^2/4t}$, which by Poisson summation equals $\sum_n e^{-t(2\pi n/L)^2}$ — the spectral sum. Both sides diverge as $t\to 0^+$ with leading term $L/\sqrt{4\pi t}$ (heat-kernel Weyl law).

---

# Statement

> **Remark (relation to the path integral; Belyaev–Huseynli 3.3, together with §3.2 QM digression).** The loop measure $\mu^E_X$ decomposes as a sum over conjugacy classes,
> $$\mu^E_X \;=\; \delta_{\text{trivial}}\,\mu^E_X\big|_{\text{contractible}} + \sum_{\gamma\in\mathcal{P}_X, m\ge 1}\mu^E_X\big(C_X(\gamma^m)\big) + \sum_{\text{peripheral}}(\cdots),$$
> with each $\mu^E_X(C_X(\gamma^m))$ given by [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]]. Heuristically, this is an interpretation, in the loop-measure setting, of the **homotopy theorem for path integration**: on a multiply-connected space $X$, the quantum-mechanical propagator between two points decomposes as a sum over homotopy classes,
> $$K(t; x, y) \;=\; \sum_{[\alpha]\in\pi_1(X, x)}\chi(\alpha)\,K_\alpha(t; x, y),$$
> where $K_\alpha(t;x,y)$ is the partial amplitude summing over paths in the class $[\alpha]$ and $\chi : \pi_1(X, x)\to U(1)$ is a unitary character. In the loop-measure setting the class-masses $\mu^E_X(C_X(\gamma^m))$ play the role of **Wick-rotated partial amplitudes**, conjugacy classes replace based classes (the loops are unrooted), and the character is trivial ($\chi\equiv 1$). Twisting the loop measure by a flat unitary bundle on $X$ — equivalently by a unitary representation of $\pi_1(X)$ — replaces the periodisation by its twisted form and reproduces the character-weighted decomposition; this is what §6 does with characters of homology.

The unnumbered §3.2 QM digression, reproduced below in this same subpage, unpacks *why* Brownian-loop constructions match Euclidean field-theory partition functions: the killed loop measure, summed over all loops, is (after §5 regularisation) exactly $-\log\det(\Delta_X + \kappa)$, so a free scalar field's partition function is $Z^\kappa_X \propto \exp(\frac12|\mu^\kappa_X|_{\mathrm{reg}})$.

---

# In One Line

The class-decomposition of the loop measure is a Wick-rotated, character-trivial, unrooted version of the sum-over-homotopy-classes for a path-integral quantum propagator on a multiply-connected space — and *summing* the class-masses reproduces the log-determinant of the Schrödinger operator, so the whole framework is the Euclidean partition function of a free scalar field.

---

# Unpacking

**The homotopy theorem for path integration.** On a *simply* connected space, every path from $x$ to $y$ is homotopic to every other, and the Feynman path integral is a single sum $K(t;x,y) = \int_{x\to y}\mathcal{D}\omega\,e^{iS[\omega]/\hbar}$. On a *multiply* connected space $X$, paths from $x$ to $y$ fall into distinct homotopy classes (indexed by $\pi_1(X,x)$ acting on the based paths from $x$ to $y$), each unable to deform to the others without cutting. The path integral splits accordingly:
$$K(t;x,y) \;=\; \sum_{[\alpha]\in\pi_1(X,x)}\chi(\alpha)\,K_\alpha(t;x,y),$$
where $K_\alpha$ is the partial amplitude confined to class $[\alpha]$. The weights $\chi(\alpha)$ must be *unitary characters* $\chi:\pi_1(X,x)\to U(1)$ (Laidlaw–DeWitt–Morette theorem): any other weighting produces a probability distribution that fails to be invariant under changes of basepoint or gives non-unitary evolution. Different characters give physically distinct quantisations of the same classical system — this is the origin of things like the $\theta$-angle in gauge theory and the Bose/Fermi statistics of identical particles.

**Wick rotation to the Euclidean side.** Under $t = -i\tau$ (real time $\to$ imaginary time), $e^{-it\hat H/\hbar} \to e^{-\tau\hat H/\hbar}$ (unitary $\to$ contractive); the Feynman integral $\int\mathcal{D}\omega\,e^{iS[\omega]/\hbar}$ becomes $\int\mathcal{D}\omega\,e^{-S_E[\omega]}$ with Euclidean action $S_E$. For a free particle in a constant potential $\kappa$, $S_E[\omega] = \int_0^\tau(\frac14|\dot\omega(r)|^2 + \kappa)\,dr$, and the Wick-rotated "sum over paths" is *the killed Brownian bridge measure* (rigorously, by the Feynman–Kac formula, see the callout below). So partial amplitudes $K_\alpha$ become masses of bridge measures restricted to the class $[\alpha]$, and closed-loop amplitudes (trace $\int_X K(t;x,x)\,d\!\operatorname{vol}(x)$) become loop-measure class-masses.

**The paper's specific match.** Because the paper's loop measure integrates over *loops*, not paths from $x$ to $y$, the objects that appear are *free* homotopy classes (not based), and the group $\pi_1(X,x)$ enters through its conjugacy classes. The character is trivial: $\mu^E_X$ is a positive measure, no phases. On a hyperbolic surface of genus $g\ge 2$ the fundamental group is non-abelian and its character variety is non-trivial; different characters give physically distinct theories. The paper introduces the twist in §6 via **homology characters** (which factor through the abelianisation $H_1(X;\mathbb{Z})\to U(1)$), producing a probability measure on homology classes — the Fourier-dual of the loop measure.

**Reference and physical intuition.** [LJ24] (Le Jan) and [PS25] (Papadopoulos–Serafinelli) develop the physical interpretation and give a rigorous construction of the twisted loop measure in this setting.

---

## §3.2 QM digression — the scalar-field partition function

This continues the remark, reproducing the paper's §3.2 in full. It is physics motivation for §5 (which renormalises $|\mu^\kappa_X|$ into a determinant); the formal manipulations here are heuristic at the path-integral level.

⚠️ *(Intuition, flagged.)* The formal expression "$\int\mathcal{D}\varphi\,e^{-S_E[\varphi]}$" is not an integral against any measure — no Lebesgue measure on infinite-dimensional path or field space exists. Everything below is heuristic at that level, and the determinant identities are rigorous only after §5's zeta-regularisation. The rigorous content of this section is the Feynman–Kac formula and, later, §5.

**Euclidean quantum mechanics.** After Wick rotation, ordinary Brownian motion is a free non-relativistic quantum particle; the interesting content appears when a potential is added, and here the potential is the constant killing rate $\kappa\ge 0$. In the paper's sign convention, the wave function $\psi:X\times[0,\infty)\to\mathbb{C}$ satisfies the **Schrödinger equation**
$$i\hbar\,\partial_t\psi \;=\; \hat H\psi, \qquad \hat H \;=\; \frac{\hbar^2}{2m}\Delta_X + V(x),$$
with $V(x)\ge 0$ a potential energy on $X$. Its solution is the **unitary group** $\psi(x,t) = e^{-it\hat H/\hbar}\psi(x,0)$ (unitary because $\hat H$ is self-adjoint), and the **propagator** (transition amplitude between two spacetime points) is
$$K(t; x, y) \;=\; \langle y \,|\, e^{-it\hat H/\hbar}\,|\, x\rangle,$$
which is exactly the object that appeared, sorted by homotopy class, in the statement of the Remark above.

> [!recall]- Wick rotation $t = -i\tau$
> **Formally:** under the substitution $t \mapsto -i\tau$ ($\tau\ge 0$ *Euclidean time*), the Schrödinger unitary group $e^{-it\hat H/\hbar}$ becomes the contraction semigroup $e^{-\tau\hat H/\hbar}$, well-defined for $\tau\ge 0$ since $\hat H\ge 0$. The Euclidean time $\tau$ is precisely the diffusion time (in units where $\hbar^2/2m = 1$ and absorbing $\hbar$ into $V$, the semigroup is $e^{-\tau(\Delta_X + V)}$, with integral kernel $p_V(\tau, x, y)$ — the transition density of Brownian motion on $X$ killed at rate $V$).
> **In words:** the Schrödinger equation $\partial_t\psi = -\frac{i}{\hbar}\hat H\psi$ and the heat equation $\partial_\tau u = -\frac{1}{\hbar}\hat H u$ differ by a factor of $i$; substituting $t = -i\tau$ trades one for the other. Wave-like oscillation becomes exponential decay; reversible unitary evolution becomes irreversible smoothing.
> **Concretely:** for the free particle $\hat H = -d^2/dx^2$ on the real line, the Schrödinger kernel $\langle y|e^{-it\hat H}|x\rangle = (4\pi it)^{-1/2}e^{i(x-y)^2/4t}$ (oscillating Gaussian) becomes, under $t = -i\tau$, the heat kernel $(4\pi\tau)^{-1/2}e^{-(x-y)^2/4\tau}$ — a decaying Gaussian, exactly Brownian motion's transition density. Euclidean-time quantum mechanics *is* Brownian motion.

> [!cite]- External input — Feynman–Kac formula
> **Statement (typed):** let $X$ be a Riemannian manifold, $V : X\to[0,\infty)$ a non-negative potential (or, more generally, bounded below), and $\mathbb{W}^t_{x\to y}$ the Brownian bridge measure from $x$ to $y$ over $[0,t]$ (total mass $p(t,x,y)$). Then the killed heat kernel $p_V(t,x,y)$ associated with the Schrödinger operator $\Delta_X + V$ satisfies
> $$p_V(t,x,y) \;=\; \int_{C([0,t];X)} e^{-\int_0^t V(\omega(r))\,dr}\,\mathbb{W}^t_{x\to y}(d\omega).$$
> **In particular:** for $V\equiv\kappa$ constant, the weight $e^{-\int_0^t\kappa\,dr} = e^{-\kappa t}$ is constant on paths, so $p^\kappa(t,x,y) = e^{-\kappa t}p(t,x,y)$.
> **Why it's true (intuition):** discretise time into $n$ steps of duration $t/n$; the semigroup $e^{-t(\Delta_X + V)}$ factors approximately as $(e^{-\frac{t}{n}V}\cdot e^{-\frac{t}{n}\Delta_X})^n$ (Trotter product); each Brownian short-step at position $\omega(r)$ picks up a decay factor $e^{-(t/n)V(\omega(r))}$; in the continuum limit the product becomes the exponential of the time integral $\int_0^t V(\omega(r))\,dr$ along the bridge path. **Source:** Simon, *Functional Integration and Quantum Physics*; the paper uses it as the rigorous form of the Euclidean path integral $\int\mathcal{D}\omega\,e^{-S[\omega]}$ with action $S[\omega] = \int_0^t(\frac14|\dot\omega|^2 + V(\omega))\,dr$: the kinetic part $\frac14|\dot\omega|^2$ is absorbed into $\mathbb{W}^t_{x\to y}$, the potential part into the weight.

Consequently $\mu^\kappa_X$ (the loop measure for Brownian motion with killing $\kappa$) is the intensity of the loop ensemble of a Euclidean quantum particle in a constant potential — the intensity of the loop soup of §3.3.

**The scalar-field partition function.** In Euclidean quantum field theory, take a free real scalar field $\varphi : X\to\mathbb{R}$ of mass $m$, so $\kappa = m^2 > 0$, and effective action
$$S_E[\varphi] \;=\; \frac12\int_X\big(|\nabla\varphi|^2 + \kappa\,\varphi^2\big)\,d\!\operatorname{vol}_g \;=\; \frac12\langle\varphi, (\Delta_X + \kappa)\varphi\rangle,$$
the second equality because $\Delta_X$ is the *positive* Laplacian and integration by parts gives $\int_X|\nabla\varphi|^2 = \langle\varphi, \Delta_X\varphi\rangle$. The action is quadratic in $\varphi$, so the Euclidean partition function is formally Gaussian:
$$Z^\kappa_X \;=\; \int\mathcal{D}\varphi\,e^{-S_E[\varphi]} \;\propto\; \det(\Delta_X + \kappa)^{-1/2},$$
by the finite-dimensional analogue $\int_{\mathbb{R}^n}d^n\varphi\,e^{-\frac12\langle\varphi,A\varphi\rangle} = (2\pi)^{n/2}\det(A)^{-1/2}$ for $A$ symmetric positive-definite. The **one-loop effective action** is
$$\Gamma^{(1)}_X(\kappa) \;=\; -\log Z^\kappa_X \;=\; \frac12\log\det(\Delta_X + \kappa).$$
The determinant is expressed through the heat semigroup by the **Schwinger proper-time representation**
$$-\log\det(\Delta_X + \kappa) \;=\; \int_0^\infty\frac{dt}{t}\,e^{-\kappa t}\,\operatorname{Tr}\big(e^{-t\Delta_X}\big),$$
(rigorously via zeta regularisation, details in §5). When $e^{-t\Delta_X}$ is trace class, $\operatorname{Tr}(e^{-t\Delta_X}) = \int_X p(t,x,x)\,d\!\operatorname{vol}_g(x)$ — the **heat trace**, built from Brownian round-trip densities. Integrating over $t$ against $dt/t$ and the killing weight $e^{-\kappa t}$ is *exactly* the structure of the [[Def - Brownian Loop Measure|Brownian loop measure]] with killing, so the Schwinger representation reads
$$-\log\det(\Delta_X + \kappa) \;=\; \big|\mu^\kappa_X\big|_{\mathrm{reg}},$$
the (regularised) total mass of the killed loop measure. The regularisation is needed because the unregularised total mass diverges (short-loop contribution of the trivial class + peripheral classes); §5 makes the identity rigorous. Hence
$$Z^\kappa_X \;\propto\; \exp\Big(\frac12\,|\mu^\kappa_X|_{\mathrm{reg}}\Big):$$
the partition function of a free real scalar field of mass $\sqrt\kappa$ is, up to normalisation, the exponential of *half* the regularised total mass of Brownian loops with killing rate $\kappa$. The factor $\frac12$ comes from the $\det^{-1/2}$ power of a single real (as opposed to complex) field; a complex field would give $\det^{-1}$ and no $\frac12$.

This is the physical motivation for §5: the ill-defined "sum over loops" of a Euclidean quantum field theory is exactly the divergent total mass of the Brownian loop measure; renormalising the latter renormalises the former, and the outcome is the zeta-regularised determinant.

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3]] (Remark 3.3 and §3.2). Motivates the entire renormalisation programme of [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5]], which turns the heuristic identity $Z^\kappa_X \propto \exp(\frac12|\mu^\kappa_X|_{\mathrm{reg}})$ into a rigorous statement ([[Thm - Determinant as Renormalised Loop Mass|Theorem 5.1]] and downstream). The character twist referenced in the last paragraph is realised in [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6]] via homology characters.
