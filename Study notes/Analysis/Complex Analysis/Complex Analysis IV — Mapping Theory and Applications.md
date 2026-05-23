---
type: topic
subject: complex-analysis
chapter: "3.5-3.6 + applications"
title: "Complex Analysis IV — Argument Principle, Möbius and Conformal Maps, Harmonic Functions, Applications"
tags: [analysis, complex-analysis]
---

# Notation Registry

- $z, w \in \mathbb{C}$ — complex variables
- $\mathbb{D} = \{z : |z| < 1\}$ — open unit disc
- $\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$ — Riemann sphere
- $\mathbb{H} = \{z : \operatorname{Im} z > 0\}$ — upper half-plane
- $\gamma$ — a closed piecewise $C^1$ contour
- $I(\gamma; w)$ — winding number
- $\operatorname{ord}_a f$ — order of $f$ at $a$ (positive for zeros, negative for poles)
- $N(f, D)$ — number of zeros of $f$ in $D$ counted with multiplicity
- $P(f, D)$ — number of poles of $f$ in $D$ counted with multiplicity
- $T(z) = \frac{az + b}{cz + d}$ — a **Möbius transformation** with $ad - bc \neq 0$
- A function is **conformal** at $z_0$ if its derivative at $z_0$ is nonzero
- $u : U \to \mathbb{R}$ — a harmonic function on $U \subseteq \mathbb{R}^2 \cong \mathbb{C}$
- $\Delta u = u_{xx} + u_{yy}$ — Laplacian
- $P_r(\theta) = (1 - r^2)/(1 - 2r\cos\theta + r^2)$ — **Poisson kernel** for the disc
- $f_n \to f$ **locally uniformly** if $f_n \to f$ uniformly on every compact subset

---

# Motivation

§3.5–3.6 plus the applied material of the complex methods notes form the final layer of complex analysis: the *mapping theory* (how holomorphic functions transform regions), the *harmonic function theory* (the real-variable shadow of holomorphic), and the *applied calculus* (conformal mapping for fluid flow and signal processing). This is where complex analysis flowers into a tool for solving problems that have nothing visibly to do with complex numbers — Laplace's equation on irregular domains, the lift on an aerofoil, the response of a linear system, the conformal classification of plane regions.

The chapter opens in §3.5 with the **argument principle** and **Rouché's theorem**. The argument principle says: for $f$ meromorphic on a closed curve $\gamma$ (avoiding zeros and poles), $\frac{1}{2\pi i}\int_\gamma \frac{f'(z)}{f(z)}\,dz = N - P$, where $N$ is the number of zeros and $P$ the number of poles enclosed (counted with multiplicity and weighted by winding number). The proof is direct from the residue theorem applied to the logarithmic derivative: $f'/f$ has a simple pole at each zero of $f$ (with residue equal to the order) and at each pole (with residue negative the order). The argument principle has a topological reading: the integer $\frac{1}{2\pi i}\int_\gamma f'/f \,dz$ equals the winding number of $f \circ \gamma$ around $0$ — so the principle is "the winding number of the image of $\gamma$ under $f$ counts the zeros and poles inside $\gamma$".

**Rouché's theorem** is the immediate corollary: if $f, g$ are holomorphic on a domain bounded by $\gamma$ and $|f - g| < |f|$ on $\gamma$, then $f$ and $g$ have the same number of zeros inside. The intuition is that $|f - g| < |f|$ means the "perturbation" $g - f$ never reaches all the way to $0$ on $\gamma$, so the winding numbers of $f \circ \gamma$ and $g \circ \gamma$ around $0$ are equal. Rouché is the standard counting tool: count zeros of $g$ by comparing it to a simpler $f$, locate zeros without computing them. It gives a one-line proof of the fundamental theorem of algebra and is the workhorse for stability analysis of polynomials.

The **open mapping theorem** and the **local mapping degree** follow. A non-constant holomorphic function maps open sets to open sets — *no* real-variable analog of this exists ($f(x) = x^2$ maps $\mathbb{R}$ to $[0, \infty)$, not open). The local mapping degree says: if $f$ has a zero of order $k$ at $a$, then for $z$ near $a$ and $w$ near $0$, the equation $f(z) = w$ has exactly $k$ solutions near $a$ — locally $f$ behaves like $w \mapsto w^k$ near $0$. This is the source of the **inverse function theorem for holomorphic functions** ($f'$ nonzero ⇒ $f$ locally biholomorphic) and the **maximum modulus principle** (a non-constant open map cannot have a local max of $|f|$).

§3.6 introduces **locally uniform convergence** and **Hurwitz's theorem**. A sequence $f_n$ of holomorphic functions converging locally uniformly on a domain converges to a *holomorphic* function (by Morera's theorem applied to triangles, in [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]]). Moreover, the derivatives also converge locally uniformly. **Hurwitz's theorem**: if $f_n \to f$ locally uniformly and each $f_n$ is nonvanishing, then either $f$ is identically zero or $f$ is also nonvanishing. The proof uses the argument principle: zeros of $f$ would be detected by winding numbers, and they would already be detected for large $n$ by the locally uniform convergence — contradicting nonvanishing of $f_n$. These results are the source of **normal families** (a la Montel) and the proof of the Riemann mapping theorem in [[Complex Analysis IV — Mapping Theory and Applications|this same topic]].

The applied portion introduces **Möbius transformations** and **conformal maps**. A Möbius transformation is $T(z) = (az + b)/(cz + d)$ with $ad - bc \neq 0$, viewed as a holomorphic bijection $\hat{\mathbb{C}} \to \hat{\mathbb{C}}$. The Möbius transformations form a group $\operatorname{PGL}_2(\mathbb{C}) \cong \operatorname{PSL}_2(\mathbb{C})$, acting transitively on triples of distinct points (the cross-ratio is the unique Möbius-invariant of four points). Möbius maps preserve generalized circles (circles or lines in $\mathbb{C}$, corresponding to circles on the Riemann sphere). They are the building blocks of *conformal maps* — bijections preserving angles — between domains. The **conformal automorphisms of the unit disc** are exactly the Möbius transformations preserving $\mathbb{D}$, which form a 3-parameter group ($e^{i\theta}$ rotations × Blaschke factors $(z - a)/(1 - \bar a z)$). The **Riemann mapping theorem** (statement; proof uses normal families and is involved) says: every simply connected proper open subset of $\mathbb{C}$ is biholomorphically equivalent to $\mathbb{D}$. This is the classification theorem for simply connected domains: there is exactly *one* such domain up to biholomorphism (and $\mathbb{C}$ itself, which is excluded by being non-proper).

**Harmonic functions** and the **Poisson kernel** form the bridge to PDE. Real and imaginary parts of holomorphic functions are harmonic. Conversely, every harmonic function on a simply connected open set is the real part of a holomorphic function (the harmonic conjugate exists, unique up to additive constants). On the disc, harmonic functions are reconstructed from their boundary values via the **Poisson integral formula**: $u(re^{i\theta}) = \frac{1}{2\pi}\int_0^{2\pi} P_r(\theta - \phi) u(e^{i\phi})\,d\phi$, where $P_r$ is the Poisson kernel. This solves the Dirichlet problem on the disc — given boundary values, find a harmonic function on the interior matching them. Combined with conformal mapping (the Riemann mapping theorem), one can solve the Dirichlet problem on *any* simply connected domain by mapping to the disc and using Poisson.

The applied chapter culminates in **conformal mapping for physical problems**. The Joukowski transformation $w = z + 1/z$ maps the exterior of a circle to a slit plane, which under a small perturbation becomes the exterior of an aerofoil profile. The Kutta condition (circulation chosen to ensure smooth flow at the trailing edge) gives the lift of an aerofoil. The Schwarz–Christoffel transformation maps the upper half-plane to a polygonal region, useful for solving Laplace's equation in polygons. In signal processing, the **transfer function** $H(s) = \int_0^\infty h(t) e^{-st}\,dt$ of a linear system is a meromorphic function whose pole locations classify stability — left half-plane (stable), imaginary axis (marginal), right half-plane (unstable). The **Z-transform** is the discrete analog. Inverse transforms via residues give explicit solutions of differential equations and signal responses.

The unifying frame for §3.5–3.6 and the applied material: **holomorphic functions are conformal maps, and conformal maps solve Laplace's equation by pulling back**. Once you have the equivalence between holomorphic and angle-preserving bijection, every Laplace-equation problem (electrostatics, steady fluid flow, steady heat) on a complicated domain can be conformally mapped to a simple one (typically the disc or upper half-plane), solved there, and pulled back. This is one of the most productive single ideas in applied mathematics, and it is the reason complex analysis is taught to physicists and engineers, not just mathematicians.

---

# Concept Map

## §3.5 Argument Principle and Mapping Theorems

- **[[Thm - Argument Principle]]**
	- Let $f$ be meromorphic on an open set containing a closed piecewise $C^1$ curve $\gamma$ (avoiding zeros and poles of $f$). Then $\frac{1}{2\pi i}\int_\gamma \frac{f'(z)}{f(z)}\,dz = \sum_a I(\gamma; a)\operatorname{ord}_a f$, where the sum is over zeros and poles of $f$ enclosed by $\gamma$, with $\operatorname{ord}_a f > 0$ for zeros and $< 0$ for poles. Equivalently, the left side equals $I(f \circ \gamma; 0)$ — the winding number of the image of $\gamma$ under $f$ around $0$. The result of the integral is the *signed count of zeros minus poles*.

- **[[Thm - Rouché's Theorem]]**
	- Let $\gamma$ bound a domain $D$ and $f, g$ be holomorphic on $\overline{D}$. If $|f(z) - g(z)| < |f(z)|$ on $\gamma$, then $f$ and $g$ have the same number of zeros in $D$, counted with multiplicity. The proof: consider $h(t, z) = (1 - t)f + t g$ for $t \in [0, 1]$; the hypothesis forces $h(t, z) \neq 0$ on $\gamma$ for every $t$, so $I(h(t, \cdot) \circ \gamma; 0)$ is continuous integer-valued, hence constant. At $t = 0, 1$ it gives the zero counts of $f, g$ via the argument principle.

- **[[Thm - Fundamental Theorem of Algebra via Rouché]]**
	- A degree-$n$ polynomial $p(z) = z^n + a_{n-1} z^{n-1} + \ldots + a_0$ has exactly $n$ zeros in $\mathbb{C}$ counted with multiplicity. Proof: compare $p(z)$ to $z^n$ on the circle $|z| = R$ for large $R$; the difference $|p(z) - z^n| \leq |a_{n-1}| R^{n-1} + \ldots + |a_0|$ is less than $|z^n| = R^n$ for $R$ large enough, so by Rouché $p$ has the same number of zeros as $z^n$, which is $n$ counted with multiplicity at $0$.

- **[[Thm - Open Mapping Theorem]]**
	- A non-constant holomorphic $f : U \to \mathbb{C}$ on a domain $U$ is an open map — it sends open subsets of $U$ to open subsets of $\mathbb{C}$. The proof uses the local mapping degree: near any $z_0 \in U$, $f(z) - f(z_0) = (z - z_0)^k h(z)$ for $h$ nonvanishing nearby; locally $f$ behaves like $w \mapsto w^k$, which is open. This is the "no folding back" theorem for holomorphic maps and a striking failure of any real-variable analog.

- **[[Thm - Local Mapping Degree]]**
	- Let $f$ be holomorphic at $a$ with $f(a) = w_0$ and $\operatorname{ord}_a(f - w_0) = k \geq 1$. Then for $w$ sufficiently close to but distinct from $w_0$, the equation $f(z) = w$ has exactly $k$ distinct solutions near $a$, each a simple solution. So $f$ is locally $k$-to-$1$ near $a$. When $k = 1$ (the case $f'(a) \neq 0$), $f$ is locally a biholomorphism.

- **[[Thm - Holomorphic Inverse Function Theorem]]**
	- If $f$ is holomorphic at $a$ with $f'(a) \neq 0$, then there exist neighborhoods $U \ni a, V \ni f(a)$ and a holomorphic bijection $f|_U : U \to V$ with holomorphic inverse. The proof uses local mapping degree with $k = 1$. Equivalently, $f$ is conformal at $a$ (preserves angles) iff $f'(a) \neq 0$. This is the *holomorphic* version of [[Thm - The Inverse Function Theorem|the real inverse function theorem]], with the conclusion automatic from a *single* derivative condition (no Jacobian determinant computation needed beyond $f'(a) \neq 0$).

- **[[Ex - Counting zeros via Rouché]]** (⭐⭐)
	- Show that $p(z) = z^5 + 3z + 1$ has exactly one zero in $|z| < 1$. Compare with $g(z) = 3z$ on $|z| = 1$: $|p(z) - g(z)| = |z^5 + 1| \leq 2 < 3 = |g(z)|$ on $|z| = 1$. Hence $p$ has same zero count as $3z$, namely $1$.

- **[[Ex - Open mapping in action]]** (⭐⭐)
	- Show that if $f$ is holomorphic on a domain $D$ and $|f|$ is constant, then $f$ is constant. (By open mapping, $f(D)$ is open, but it lies on a circle, hence not open unless $f$ is constant.) Compare with the more direct proof via Cauchy–Riemann.

- **[[Ex - Argument principle applied to polynomials]]** (⭐⭐⭐)
	- Show that for any polynomial $p$ of degree $n$, $\frac{1}{2\pi i}\int_{|z| = R} \frac{p'(z)}{p(z)}\,dz = n$ for $R$ large enough that all zeros are inside the disc. Verify by the argument principle, and use this as an alternative proof of FTA.

> [!note] Exercise Index — §3.5
> [[Exercise Index - §3.5 Argument Principle and Mapping]]

## §3.6 Locally Uniform Convergence and Hurwitz

- **[[Def - Locally Uniform Convergence]]**
	- A sequence $f_n : U \to \mathbb{C}$ converges to $f : U \to \mathbb{C}$ **locally uniformly** on $U$ if for every $z_0 \in U$ there is a neighborhood $V \ni z_0$ such that $f_n \to f$ uniformly on $V$. Equivalently, $f_n \to f$ uniformly on every compact subset of $U$. This is the natural convergence for holomorphic functions: it is preserved under termwise differentiation, integration, and limits.

- **[[Thm - Locally Uniform Limit of Holomorphic is Holomorphic]]**
	- If $f_n : U \to \mathbb{C}$ are holomorphic and converge locally uniformly to $f$, then $f$ is holomorphic on $U$, and $f_n^{(k)} \to f^{(k)}$ locally uniformly for every $k$. Proof: continuity of $f$ from uniform limit; holomorphicity via Morera (integral over each triangle is the limit of integrals over triangles, each zero by Cauchy). Higher derivatives via CIF and the same interchange.

- **[[Thm - Hurwitz's Theorem]]**
	- Let $f_n : U \to \mathbb{C}$ be holomorphic and nonvanishing on $U$, with $f_n \to f$ locally uniformly. Then either $f$ is identically zero or $f$ is nonvanishing on $U$. The proof: if $f$ has an isolated zero at $a$, choose a small circle around $a$ where $|f| \geq \delta > 0$; for $n$ large, $|f_n - f| < \delta$ on the circle, so by Rouché $f_n$ has the same number of zeros as $f$ inside, contradicting nonvanishing of $f_n$.

- **[[Ex - Limit of nonvanishing functions]]** (⭐⭐)
	- Show $e^z = \lim_n (1 + z/n)^n$ locally uniformly on $\mathbb{C}$. Each $(1 + z/n)^n$ has zeros only at $z = -n$ (each of multiplicity $n$, but a single point), so for $|z| < R$ and $n > R$, $(1 + z/n)^n$ is nonvanishing on $|z| < R$. By Hurwitz, $e^z$ is nonvanishing on every $|z| < R$, hence everywhere.

## §3.5 (continued) Möbius and Conformal Maps

- **[[Def - Möbius Transformation]]**
	- A **Möbius transformation** is a map $T : \hat{\mathbb{C}} \to \hat{\mathbb{C}}$ of the form $T(z) = (az + b)/(cz + d)$ with $ad - bc \neq 0$, extended to $\infty$ by $T(\infty) = a/c$ and $T(-d/c) = \infty$. The set of Möbius transformations forms a group $\operatorname{Möb}(\hat{\mathbb{C}}) \cong \operatorname{PGL}_2(\mathbb{C}) \cong \operatorname{PSL}_2(\mathbb{C})$. The group acts triply transitively on $\hat{\mathbb{C}}$: any three distinct points can be mapped to any three distinct points by a unique Möbius transformation.

- **[[Thm - Möbius Transformations Preserve Generalized Circles]]**
	- A **generalized circle** in $\hat{\mathbb{C}}$ is a circle in $\mathbb{C}$ or a line in $\mathbb{C}$ (which is a circle through $\infty$ on the Riemann sphere). Every Möbius transformation maps generalized circles to generalized circles. Proof: a generalized circle has equation $A|z|^2 + Bz + \bar B \bar z + C = 0$ for real $A, C$ and complex $B$; verify this form is preserved under $z \mapsto 1/z$ and under affine maps $z \mapsto az + b$; every Möbius transformation is a composition of these.

- **[[Def - Conformal Map]]**
	- A continuous map $f : U \to V$ between open subsets of $\mathbb{C}$ is **conformal at $z_0 \in U$** if $f$ is (real-) differentiable at $z_0$ with non-zero derivative, and the differential preserves angles and orientation. Equivalently, $f$ is holomorphic at $z_0$ with $f'(z_0) \neq 0$. A **conformal map** $U \to V$ is one conformal at every point of $U$. A **biholomorphism** is a conformal bijection.

- **[[Thm - Conformal Automorphisms of the Unit Disc]]**
	- The group of biholomorphisms $\mathbb{D} \to \mathbb{D}$ consists exactly of the Möbius transformations $z \mapsto e^{i\theta} \frac{z - a}{1 - \bar a z}$ for $\theta \in \mathbb{R}, a \in \mathbb{D}$. Equivalently, $\operatorname{Aut}(\mathbb{D}) \cong \operatorname{PSU}(1, 1)$. The proof uses **Schwarz's lemma** (next entry) and reduction to the case $f(0) = 0$ via Möbius pre-composition.

- **[[Thm - Schwarz Lemma]]**
	- If $f : \mathbb{D} \to \mathbb{D}$ is holomorphic with $f(0) = 0$, then $|f(z)| \leq |z|$ for all $z \in \mathbb{D}$ and $|f'(0)| \leq 1$. Equality holds at any nonzero point (or in either inequality) iff $f$ is a rotation $f(z) = e^{i\theta} z$. Proof: $g(z) = f(z)/z$ extends holomorphically to $\mathbb{D}$ (removable at $0$); by max modulus on $|z| = r$, $|g| \leq 1/r$ on $|z| \leq r$; take $r \to 1$. This is the cornerstone of the theory of bounded holomorphic functions on the disc.

- **[[Thm - Riemann Mapping Theorem (Statement)]]**
	- Every nonempty, simply connected, proper open subset $U$ of $\mathbb{C}$ is biholomorphic to the open unit disc $\mathbb{D}$. The biholomorphism is unique up to post-composition with $\operatorname{Aut}(\mathbb{D})$ (a 3-parameter family). The proof uses normal families (Montel's theorem) and an extremization argument: choose the $f : U \to \mathbb{D}$ injective holomorphic with $f(z_0) = 0$ maximizing $|f'(z_0)|$, then show it is surjective. The statement is one of the deepest results of complex analysis; this topic states it without proof.

- **[[Ex - Möbius transformation mapping three points to three points]]** (⭐⭐)
	- Find the Möbius transformation mapping $\{0, 1, \infty\}$ to $\{1, i, -1\}$. Use the cross-ratio: $T(z) = (z, 0, 1, \infty) \mapsto (T(z), 1, i, -1)$, equate, solve for $T$.

- **[[Ex - Conformal map from upper half-plane to disc]]** (⭐⭐)
	- Show $T(z) = (z - i)/(z + i)$ is a biholomorphism $\mathbb{H} \to \mathbb{D}$, mapping $i \mapsto 0$, the real line to the unit circle, and $\infty \mapsto 1$.

- **[[Ex - The Joukowski transformation maps a circle to an aerofoil]]** (⭐⭐⭐)
	- Show that $w = z + 1/z$ maps the unit circle to the segment $[-2, 2]$ on the real axis (squashed). When applied to a circle of radius $r > 1$ slightly off-centred, the image is an aerofoil-like curve (Joukowski profile). Used in classical 2D aerodynamics.

> [!tip] Unlocked: Hyperbolic Geometry on the Disc *(from Differential Geometry)*
> The unit disc with the **Poincaré metric** $ds^2 = \frac{4|dz|^2}{(1 - |z|^2)^2}$ is the **hyperbolic plane**. The biholomorphisms of $\mathbb{D}$ are exactly the isometries of this metric. Möbius transformations preserving $\mathbb{D}$ are the orientation-preserving hyperbolic isometries, $\operatorname{PSL}_2(\mathbb{R})$. The whole subject of hyperbolic geometry is the complex analysis of the disc viewed through this metric.

> [!note] Exercise Index — §3.5b Möbius and Conformal
> [[Exercise Index - §3.5b Möbius and Conformal]]

## Harmonic Functions and the Poisson Kernel

- **[[Def - Harmonic Function]]**
	- A function $u : U \to \mathbb{R}$ on an open $U \subseteq \mathbb{R}^2 \cong \mathbb{C}$ is **harmonic** if $u \in C^2(U)$ and $\Delta u = u_{xx} + u_{yy} = 0$. Equivalently (using the complex structure), $\partial^2 u/\partial z \partial \bar z = 0$. Real and imaginary parts of holomorphic functions are harmonic. Examples: $u(x, y) = x, y, \log|z|, \operatorname{Re}(z^n)$.

- **[[Thm - Harmonic ↔ Real Part of Holomorphic (on Simply Connected)]]**
	- Let $U$ be simply connected. A function $u : U \to \mathbb{R}$ is harmonic iff $u = \operatorname{Re} f$ for some holomorphic $f : U \to \mathbb{C}$. The **harmonic conjugate** $v$ is unique up to additive constant, with $f = u + iv$. On non-simply-connected $U$, the conjugate may not exist globally — example: $u(x, y) = \log|z|$ on $\mathbb{C}^\times$ has no global harmonic conjugate (would be $\arg z$, multi-valued).

- **[[Thm - Mean Value Property of Harmonic Functions]]**
	- For $u$ harmonic on $D(a, R)$, $u(a) = \frac{1}{2\pi}\int_0^{2\pi} u(a + re^{i\theta})\,d\theta$ for any $0 < r < R$. Direct consequence of the holomorphic mean value property applied to a holomorphic extension. Conversely, mean value characterizes harmonicity in the appropriate regularity class. This is the basis of the Dirichlet problem and the Perron method.

- **[[Thm - Maximum Principle for Harmonic Functions]]**
	- A non-constant harmonic function on a domain $D$ does not attain an interior maximum or minimum. From mean value: if $u(a)$ is a local max, $u(a + re^{i\theta}) \leq u(a)$ on the circle and the average equals $u(a)$, forcing equality on the circle, hence $u$ constant. This is the unique-solution theorem for the Dirichlet problem (two harmonic functions with the same boundary values are equal).

- **[[Def - Poisson Kernel]]**
	- The **Poisson kernel** on the unit disc is $P_r(\theta) = \frac{1 - r^2}{1 - 2r\cos\theta + r^2}$ for $0 \leq r < 1$ and $\theta \in \mathbb{R}$. Equivalently, $P_r(\theta) = \operatorname{Re}\frac{e^{i\theta} + re^{i\theta}}{e^{i\theta} - re^{i\theta}}$ wait — more cleanly, $P_r(\theta) = \operatorname{Re}\left(\frac{1 + re^{i\theta}}{1 - re^{i\theta}}\right)$ for $|re^{i\theta}| < 1$. Properties: positive, integrates to $2\pi$ over $[0, 2\pi]$, concentrates as $r \to 1$ on $\theta = 0$ (Dirac-like).

- **[[Thm - Poisson Integral Formula]]**
	- For $u$ continuous on $\overline{\mathbb{D}}$ and harmonic on $\mathbb{D}$, $u(re^{i\theta}) = \frac{1}{2\pi}\int_0^{2\pi} P_r(\theta - \phi) u(e^{i\phi})\,d\phi$ for $r < 1$. Conversely, for any continuous boundary data $u_0 : S^1 \to \mathbb{R}$, the Poisson integral defines the unique harmonic extension to $\mathbb{D}$ taking those boundary values. This solves the Dirichlet problem on the disc; combined with conformal mapping, it solves the Dirichlet problem on any simply-connected domain.

- **[[Ex - Solving Laplace's equation on a disc]]** (⭐⭐)
	- Given boundary values $u(e^{i\theta}) = \cos(2\theta)$, find the harmonic function $u(re^{i\theta})$ on the disc. Recognize: $\cos(2\theta) = \operatorname{Re}(e^{2i\theta}) = \operatorname{Re}(z^2)$ on the boundary. The harmonic extension is $\operatorname{Re}(z^2) = r^2 \cos(2\theta)$.

- **[[Ex - Solving Dirichlet on a half-plane via conformal mapping]]** (⭐⭐⭐)
	- Solve Laplace's equation on $\mathbb{H}$ with $u(x, 0) =$ a step function. Map $\mathbb{H} \to \mathbb{D}$ by $z \mapsto (z - i)/(z + i)$, transfer the boundary data, apply Poisson on $\mathbb{D}$, pull back.

> [!note] Exercise Index — §3.6 Harmonic Functions and Poisson
> [[Exercise Index - §3.6 Harmonic and Poisson]]

## Applications to Signal Processing and Fluid Dynamics

- **[[Def - Laplace Transform]]**
	- The **Laplace transform** of a function $f : [0, \infty) \to \mathbb{R}$ is $F(s) = \int_0^\infty f(t) e^{-st}\,dt$, defined for $\operatorname{Re} s$ large enough. $F$ is holomorphic on a half-plane $\{\operatorname{Re} s > c\}$ (and often extends meromorphically further). The inverse transform is the **Bromwich integral** $f(t) = \frac{1}{2\pi i}\int_{c - i\infty}^{c + i\infty} F(s) e^{st}\,ds$, evaluable by closing the contour to the left and applying residues.

- **[[Def - Transfer Function and Stability]]**
	- For a linear time-invariant system with impulse response $h(t)$, the **transfer function** is $H(s) = \mathcal{L}h(s)$. The system is **stable** if all poles of $H$ lie in $\{\operatorname{Re} s < 0\}$ (left half-plane); marginal if poles on the imaginary axis; unstable if any pole has $\operatorname{Re} s > 0$. This dichotomy is read off the pole locations of a meromorphic function — a clean application of complex analysis.

- **[[Def - Complex Potential]]**
	- For 2D incompressible irrotational fluid flow in a domain $D \subseteq \mathbb{C}$, the velocity field $(v_x, v_y)$ is derived from a **complex potential** $w(z) = \phi(z) + i\psi(z)$ holomorphic on $D$. The **velocity potential** $\phi$ satisfies $\nabla\phi = (v_x, v_y)$; the **stream function** $\psi$ is its harmonic conjugate. The complex velocity is $\bar v(z) = w'(z) = v_x - i v_y$. Singularities of $w$ have physical meaning: poles = sources/sinks, logs = vortices, dipoles = source/sink limits.

- **[[Thm - Joukowski Aerofoil Construction]]**
	- The **Joukowski transformation** $w = z + 1/z$ maps a circle $|z - z_0| = a > |z_0 - 1|$ (avoiding $z = \pm 1$, centred near $1$) to a closed curve in $w$-plane resembling an aerofoil — sharp trailing edge at $w = 2$, blunt nose near $w = -2$. The image is the boundary of an aerofoil region; flow past the aerofoil is obtained by conformally mapping flow past a circle (the Joukowski potential) through $w$. The Kutta condition selects the circulation so the velocity at the trailing edge is finite, giving the lift formula $L = \rho U \Gamma$ (Kutta–Joukowski theorem).

- **[[Ex - Inverse Laplace via residues]]** (⭐⭐)
	- Compute the inverse Laplace transform of $F(s) = 1/(s^2 + 1)$. Poles at $\pm i$, residues $\frac{1}{2i}\cdot e^{it}$ and $-\frac{1}{2i} \cdot e^{-it}$. Sum gives $\sin t$.

- **[[Ex - Transfer function stability analysis]]** (⭐⭐)
	- For $H(s) = 1/(s^2 + 2\zeta\omega_0 s + \omega_0^2)$ (damped harmonic oscillator), classify stability as $\zeta$ varies. For $\zeta > 0$ (underdamped or overdamped), poles in left half-plane, stable. For $\zeta = 0$, poles on imaginary axis, marginally stable. For $\zeta < 0$, unstable.

- **[[Ex - Flow past a cylinder via complex potential]]** (⭐⭐⭐)
	- Show that $w(z) = U(z + a^2/z) - i\Gamma \log z / (2\pi)$ is the complex potential for flow past a cylinder of radius $a$ in a uniform stream $U$ with circulation $\Gamma$. Identify the velocity field by $\bar v = w'$, verify boundary conditions ($\psi$ constant on the cylinder), compute the lift via residues / Kutta–Joukowski.

- **[[Ex - Schwarz–Christoffel for a polygon]]** (⭐⭐⭐)
	- State the Schwarz–Christoffel formula for a conformal map $\mathbb{H} \to$ interior of a polygon. Verify it for a simple case (e.g. mapping $\mathbb{H}$ to the interior of an isoceles triangle, identifying corners with prescribed images on $\mathbb{R}$).

> [!note] Exercise Index — Applications
> [[Exercise Index - Applications Signal and Fluid]]

---

# Sources and Targets

**Targets — What do we usually try to prove?**

Three signature target classes. First, *counting zeros* of a holomorphic or meromorphic function — Rouché's theorem is the standard tool. Second, *constructing a conformal map* between two specific domains — Möbius transformations on simply connected domains, Riemann mapping in general, Schwarz–Christoffel for polygons. Third, *solving a boundary value problem* — typically Laplace's equation with prescribed boundary values, via Poisson kernel on the disc and conformal pullback to other domains.

A fourth class is *applied evaluation* — inverse Laplace transforms via residues, stability classification via pole location, lift computation via circulation. These convert complex-analytic facts into directly engineering- or physics-relevant statements.

**Sources — What assumptions do we usually leverage?**

The standard hypotheses: (1) *meromorphic function on a domain* — gives access to the argument principle, Rouché, and pole-counting tools; (2) *holomorphic bijection between domains* — gives conformal pullback for Laplace's equation; (3) *boundary data* (continuous, on a closed curve) — gives the Dirichlet problem with Poisson kernel solution; (4) *simply connected domain* — gives Riemann mapping and harmonic conjugate existence.

The pattern is: identify the holomorphic/conformal structure, transform to a canonical domain (disc or half-plane), solve there, transform back.

---

# Legal Operations

1. **Apply Rouché to count zeros.** When you want the number of zeros of $g$ in a region, find a simpler $f$ with the same number of zeros there and $|f - g| < |f|$ on the boundary. *Trigger:* "how many zeros does this have inside $|z| < R$?" *Pattern:* dominant term comparison on the boundary.

2. **Use the argument principle to count.** Integrate $f'/f$ around the boundary; result is $N - P$ counted with multiplicity. *Trigger:* a counting problem where you want signed count, or where you can compute the logarithmic-derivative integral.

3. **Apply Hurwitz to deduce nonvanishing.** If a limit of nonvanishing holomorphic functions converges locally uniformly to $f$, then $f$ is either identically zero or nonvanishing. *Trigger:* limit-of-functions problem where vanishing properties matter.

4. **Use a Möbius transformation to normalize.** Möbius maps act transitively on triples; you can always move $\{0, 1, \infty\}$ (or any three points) to wherever convenient. *Trigger:* problem with a specific configuration of three points. *Pattern:* apply Möbius to standardize, solve in normalized form, transform back.

5. **Conformally map to the disc or half-plane.** When solving Laplace's equation on a complicated simply-connected domain, conformally map it to $\mathbb{D}$ (Riemann mapping or explicit construction), solve there via Poisson, pull back. *Trigger:* boundary value problem on a non-canonical domain.

6. **Use Schwarz's lemma to bound a function on the disc.** $f : \mathbb{D} \to \mathbb{D}$ with $f(0) = 0$ satisfies $|f(z)| \leq |z|$. *Trigger:* a holomorphic self-map of a disc with a fixed point. *Pattern:* normalize the fixed point to $0$ via Möbius, apply Schwarz.

7. **Compute an inverse Laplace transform by residues.** Close the Bromwich contour to the left (for $t > 0$), sum residues of $F(s) e^{st}$ at poles in the closed contour. *Trigger:* a Laplace transform with known meromorphic structure.

8. **Identify physical singularities by their complex potential.** Sources at simple poles, vortices at logarithmic singularities, dipoles at higher-order poles. *Trigger:* a physical 2D flow problem.

**Illegal but tempting operations:**

> [!warning] 1. Applying Rouché on a boundary where the inequality fails at a single point
> The strict inequality $|f - g| < |f|$ must hold *strictly* on the entire boundary $\gamma$. Equality at a single point breaks the argument (the homotopy $h(t, z)$ would touch $0$). Always verify strict inequality, especially when the bound is tight.

> [!warning] 2. Using Möbius transformations on $\mathbb{C}$ instead of $\hat{\mathbb{C}}$
> Möbius transformations are bijections $\hat{\mathbb{C}} \to \hat{\mathbb{C}}$, not $\mathbb{C} \to \mathbb{C}$ (they have a pole at $z = -d/c$). To use them, work on the Riemann sphere or identify the pole's image as $\infty$.

> [!warning] 3. Conformal mapping inappropriately to non-simply-connected domains
> The Riemann mapping theorem applies to simply connected proper open subsets of $\mathbb{C}$. An annulus is not simply connected, and the conformal classification of annuli is a one-parameter family (parametrized by the modulus, the ratio of radii). Trying to conformally map every domain to $\mathbb{D}$ is incorrect; non-simply-connected domains require richer classification.

> [!warning] 4. Computing inverse Laplace by direct integration
> The Bromwich integral $\int_{c - i\infty}^{c + i\infty} F(s) e^{st}\,ds$ is divergent for typical $F$; one needs to close the contour and apply residues, NOT evaluate the integral as a real improper integral. The closure direction (left for $t > 0$, right for $t < 0$) depends on the sign of $t$ and the decay of $F$.

---

# Problem-Solving Strategy

For **counting zeros**, the universal first step is to identify a dominant term on the contour. For a polynomial $z^n + \ldots$ on a large circle, the dominant term is $z^n$. For $z^n + \ldots + a_0$ on a small circle (looking for low-order zeros), the dominant term is $a_0$. Apply Rouché with the dominant term, count its zeros (a polynomial $z^n$ has $n$ zeros at $0$ counted with multiplicity), conclude.

For **conformal mapping problems**, the first move is to identify whether the domain is simply connected. If yes, Riemann mapping guarantees a conformal map to $\mathbb{D}$ (or to $\mathbb{H}$, which is biholomorphic via $z \mapsto (z - i)/(z + i)$). Then either construct the map explicitly (using Möbius transformations, powers, exponential/log to handle wedges and strips) or rely on the existence theorem. For non-simply-connected domains, the conformal type is a moduli problem (annuli classified by modulus, tori classified by $\tau$ in the upper half-plane).

For **boundary value problems on a domain**, the recipe: (1) conformally map to a canonical domain (disc or half-plane); (2) transfer the boundary data via the conformal map; (3) solve on the canonical domain using Poisson kernel; (4) conformally pull back. For Laplace's equation specifically, the conformal invariance of harmonic functions ($u$ harmonic + $f$ conformal ⇒ $u \circ f$ harmonic) is what makes the pullback step work.

For **transform inversion** (Laplace, Fourier, $Z$-transform), close the inversion contour appropriately and apply residues. The art is in choosing the closure: for $t > 0$ close the Laplace inversion to the left half-plane (where $e^{st}$ decays); for $t < 0$ to the right. Bound the contribution of the closing arc by ML estimate or Jordan's lemma. The residue sum gives the time-domain function.

A non-obvious general principle: **complex analysis problems often have a "geometric heart" obscured by formulas**. The Joukowski aerofoil is "conformally a circle"; the polygonal interior is "conformally the upper half-plane"; the transfer function stability is "pole position in the complex plane"; the Dirichlet problem on a domain is "Poisson on the disc, pulled back". When stuck, ask: what is the underlying geometry, and what canonical conformal model does it correspond to?

---

# Most Reusable Properties

- **[[Thm - Rouché's Theorem|Rouché]]**: $|f - g| < |f|$ on $\gamma$ ⇒ $f, g$ have same zero count. The standard tool for counting zeros without computing them. Use it whenever a "how many roots in this region?" question appears, by comparing the function to a dominant term.

- **[[Thm - Argument Principle|Argument principle]]**: $\frac{1}{2\pi i}\oint f'/f\,dz = N - P$. The exact-count tool; combined with Rouché it handles all counting problems for holomorphic/meromorphic functions.

- **[[Thm - Open Mapping Theorem|Open mapping theorem]]**: holomorphic non-constant ⇒ open. The structural fact that distinguishes holomorphic from real-differentiable; underlies the maximum modulus principle and the local mapping degree.

- **[[Thm - Riemann Mapping Theorem (Statement)|Riemann mapping]]**: every simply connected proper open $U \subset \mathbb{C}$ is biholomorphic to $\mathbb{D}$. The classification of simply-connected planar domains up to biholomorphism; *the* theorem that lets one assume the domain is a disc.

- **[[Thm - Poisson Integral Formula|Poisson integral]]**: $u(re^{i\theta}) = \frac{1}{2\pi}\int P_r(\theta - \phi) u(e^{i\phi})\,d\phi$ for harmonic $u$ on $\mathbb{D}$. The explicit solution of the Dirichlet problem on the disc; pulled back via conformal maps to any simply connected domain. Use it whenever a Laplace-equation problem appears.

---

# Bridges

1. **Multivariable Analysis — Cauchy–Riemann as closedness of a 1-form, CIF as Stokes.** The whole apparatus of complex contour integration is differential-form integration on $\mathbb{R}^2$ specialized to the holomorphic case. $f\,dz$ is a closed 1-form iff $f$ holomorphic; Cauchy's theorem is Stokes for closed forms; the residue theorem is Stokes with prescribed point sources. See [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]] for the framework.

2. **Measure Theory — Harmonic Measure and the Poisson Kernel.** The **harmonic measure** $\omega(z, \cdot)$ at $z \in D$ is the probability distribution on $\partial D$ assigning to a Borel set $E \subset \partial D$ the value $\omega(z, E)$ = the harmonic function in $D$ with boundary values $\mathbf{1}_E$ evaluated at $z$. For the disc, $\omega(0, d\theta) = d\theta/(2\pi)$ is uniform; for $z \in \mathbb{D}$, $\omega(z, d\theta) = P_r(\theta - \theta_0)/2\pi\,d\theta$ with $z = re^{i\theta_0}$ — the Poisson kernel is the density of the harmonic measure! This bridges complex analysis (Poisson) and measure theory (harmonic measure) — see [[Measure Theory I — §1 Measure Spaces]].

3. **Group Theory — Möbius Group and Hyperbolic Geometry.** The **Möbius group** $\operatorname{PGL}_2(\mathbb{C})$ acts on $\hat{\mathbb{C}}$ as biholomorphic automorphisms. The subgroup preserving the disc is $\operatorname{PSU}(1, 1) \cong \operatorname{PSL}_2(\mathbb{R})$ — the orientation-preserving isometries of the hyperbolic plane. This is the entry point to hyperbolic geometry, Fuchsian groups, and the theory of Riemann surfaces. See [[Group Theory I — §1.1–1.2]] for the algebraic side.

4. **Signal Processing / Linear Systems — Transfer Function Pole Geometry.** A linear time-invariant system has a transfer function $H(s)$ holomorphic on a half-plane and meromorphic on $\mathbb{C}$. Stability is determined by pole location (left half-plane = stable). Bode plots, Nyquist criterion, root locus — all classical tools of control theory — are visualizations of the pole-zero geometry. The whole subject is the applied side of complex analysis §3.5–3.6 and the residue theorem of §3.3.

5. **Fluid Dynamics — Conformal Maps and Aerofoil Theory.** 2D incompressible irrotational flow is described by a holomorphic complex potential. Conformal maps preserve the form of the potential: if $w(z)$ is the potential for a flow in $D$ and $\zeta = T(z)$ is a conformal map to $D'$, then $w(T^{-1}(\zeta))$ is the potential in $D'$. The **Joukowski transformation** maps a circle to an aerofoil; the **Kutta–Joukowski theorem** gives the lift as $L = \rho U \Gamma$ where $\Gamma$ is the circulation. The whole classical 2D aerodynamics is conformal mapping in disguise.

---

# Insights

The **unifying frame** of §3.5–3.6 and the applied material is *holomorphic = conformal*, and conformal pull-back solves PDEs. A holomorphic function is exactly an angle-preserving (and orientation-preserving) map. Such maps preserve the Laplace equation: $u$ harmonic + $f$ conformal ⇒ $u \circ f$ harmonic. So solving Laplace on a complicated domain reduces to conformally mapping to a simple one (disc, half-plane), solving there, and pulling back. This is the *one trick* underlying almost all applied complex analysis.

The **true name** of the **argument principle** is "$\frac{f'}{f}$ has residue equal to the order at each zero or pole". The topological reading — "the winding number of $f \circ \gamma$ around $0$ counts zeros minus poles" — is what makes it geometric. The two readings together are the source of every counting argument in complex analysis: Rouché, Hurwitz, the local mapping degree, the residue theorem itself.

A **trigger-reaction pattern**: when faced with a Laplace equation on a complicated domain, the trigger is "is the domain conformally a disc?", and the reaction is to find or invoke a conformal map to $\mathbb{D}$, solve via Poisson kernel, pull back. The two-step "conformal + Poisson" combination handles enormously many engineering problems — heat conduction, electrostatic potential, ideal fluid flow, capacitance.

A **density-as-strategy** observation: **rational functions are dense in holomorphic functions on a compact set** (Runge's theorem, a deep result we do not prove here). So any property that holds for rational functions and is preserved under uniform limits holds for all holomorphic functions. This generalizes the polynomial density of [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]] to handle holomorphic functions on multiply-connected domains.

A final structural observation: **the argument principle is the topological content of complex analysis**. Almost every theorem in §3.5 — Rouché, open mapping, local mapping degree, Hurwitz — is a corollary of the argument principle in a different guise. When stuck on a §3.5 problem, reduce to the argument principle: which integers are we counting, and what does the integral of $f'/f$ give us?

A final pragmatic observation about **the role of the unit disc**: the unit disc is the "model" of all simply-connected proper open subsets of $\mathbb{C}$, by Riemann mapping. Everything one wants to know about simply-connected planar domains can in principle be transferred to and from $\mathbb{D}$. This is why so much of the theory — Schwarz's lemma, the Poisson kernel, the Hardy spaces, the Nevanlinna theory — is developed on the disc. When stuck, ask: what does this problem look like on $\mathbb{D}$? The answer is often the cleanest formulation.
