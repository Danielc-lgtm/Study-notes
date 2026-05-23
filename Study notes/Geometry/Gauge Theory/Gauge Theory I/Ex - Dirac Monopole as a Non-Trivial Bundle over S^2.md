---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The Dirac Monopole Bundle"
  - "Def - Complex Line Bundle"
  - "Def - U(1) Gauge Field and Electromagnetic Connection"
  - "Thm - Dirac Quantization Condition"
tags: [geometry, gauge-theory, monopole, Chern, line-bundle]
---

# Problem Statement

A magnetic monopole of strength $g$ is located at the origin of $\mathbb{R}^3$. The magnetic field outside the origin is $\vec B = (g/r^2)\hat r$, equivalently the 2-form $B = g\sin\theta\,d\theta \wedge d\phi$ on $\mathbb{R}^3 \setminus \{0\}$.

**(a)** Construct the **Dirac monopole bundle** $L_g \to S^2$ as a hermitian complex line bundle by explicit two-patch construction. Define:
- $U_N = S^2 \setminus \{\text{south pole}\}$ with $A_N = g(1 - \cos\theta)d\phi$
- $U_S = S^2 \setminus \{\text{north pole}\}$ with $A_S = -g(1 + \cos\theta)d\phi$

Verify both $A$'s give $dA = B$ and compute the transition function $c_{SN}$ on $U_N \cap U_S$.

**(b)** Show that the transition function $c_{SN}$ is single-valued *if and only if* $\frac{2eg}{\hbar} \in \mathbb{Z}$. (This is the [[Thm - Dirac Quantization Condition|Dirac quantization condition]].)

**(c)** Compute the first Chern number of $L_g$ via
$$c_1(L_g) = \frac{1}{2\pi}\int_{S^2}F.$$
Verify it equals $\frac{2eg}{\hbar}$ (with $e = 1$ in suitable units), giving a *topological* derivation of the quantization independent of the local patching argument.

**(d)** Conclude: the Dirac monopole bundle is isomorphic to the $n$-fold tensor power $H^{\otimes n}$ of the Hopf line bundle, where $n = 2eg/\hbar$ is the first Chern number.

**Recall:**

![[Def - The Dirac Monopole Bundle#The Definition]]

![[Thm - Dirac Quantization Condition#Statement]]

A complex line bundle on $S^2$ is classified up to isomorphism by its first Chern class $c_1 \in H^2(S^2, \mathbb{Z}) = \mathbb{Z}$.

---

# Convergent Strategy

**Problem class:** This is the constructive complement to [[Thm - Dirac Quantization Condition|the Dirac Quantization Theorem]]: rather than *prove* the integer condition, we *build* the bundle that requires it and verify the construction works exactly when $2eg/\hbar \in \mathbb{Z}$. The exercise is the topological-geometric flagship of the chapter, where bundle theory, gauge invariance, and topological quantization all come together. It also exhibits the simplest non-trivial complex line bundle in physics — the analogue of "$\mathbb{Z}$ is the smallest non-trivial abelian group".

**Assumption pattern:** The magnetic field $\vec B = (g/r^2)\hat r$ is given, equivalently the 2-form $B = g\sin\theta\,d\theta \wedge d\phi$. The two-patch potentials are chosen to be smooth on their respective domains (each avoiding one pole). On the overlap, the difference $A_S - A_N$ is a closed 1-form whose primitive (the gauge function) defines the transition function. Single-valuedness of the transition function on the overlap (which is topologically a cylinder $S^1 \times \mathbb{R}$, with $\pi_1 = \mathbb{Z}$) imposes the integer condition.

**Theorem routing:** Direct calculations: (i) $dA_N = dA_S = g\sin\theta\,d\theta \wedge d\phi = B$, by exterior differentiation. (ii) $A_S - A_N = -2g\,d\phi$, gauge function $f_{SN} = -2g\phi$, transition function $c_{SN} = e^{(ie/\hbar)f_{SN}} = e^{-2ieg\phi/\hbar}$. (iii) Single-valuedness on $\phi \in [0, 2\pi)$ requires $2eg/\hbar \in \mathbb{Z}$. (iv) Chern number $c_1 = \frac{1}{2\pi}\int_{S^2}F$ with $F = g\sin\theta\,d\theta \wedge d\phi$ gives $c_1 = \frac{1}{2\pi}\cdot 4\pi g = 2g$ in units $e/\hbar = 1$, i.e., $2eg/\hbar$ in general.

**Key decision point:** The non-obvious choice is the two-patch covering with hemispheres avoiding *opposite* poles. The vector potentials $A_N$ and $A_S$ each have a "Dirac string" singularity along the *avoided* pole's axis; by covering $S^2$ with both patches, the singularities are sidestepped — at the cost of having to glue with a non-trivial transition function. This is the original geometric resolution of the Dirac string artifact.

---

# Legal Operations Used

1. **Choose a local trivialization (chart) and compute everything component-wise** (operation 1 of the topic page). The two-patch trivialization $\{U_N, U_S\}$ of $L_g$ is the basic setup.

2. **Apply the curvature formula $F = d\omega + \omega \wedge \omega$** (operation 2). For $U(1)$ (abelian), $F = d\omega = -(ie/\hbar)dA = -(ie/\hbar)F_{\mathrm{phys}}$, where $F_{\mathrm{phys}} = dA$ is the EM field strength.

3. **Integrate the curvature over a closed surface to extract a Chern number** (operation 3). $\int_{S^2}F_{\mathrm{phys}} = 4\pi g$, giving $c_1 = 2eg/\hbar$ after the appropriate normalization.

9. **Detect non-triviality of a bundle by a non-zero topological invariant** (operation 9). $c_1(L_g) = 2eg/\hbar \ne 0$ for any $g \ne 0$ — the monopole bundle is fundamentally non-trivial.

---

# Hints

> [!note]- Hint 1
> Compute $dA_N = d[g(1 - \cos\theta)d\phi]$. Since $g$ and $1$ are constants and $d(\cos\theta) = -\sin\theta\,d\theta$, we get $g\sin\theta\,d\theta \wedge d\phi = B$. The same for $A_S$.

> [!note]- Hint 2
> On the overlap, the two potentials differ by $A_S - A_N = -2g\,d\phi$, which is *not exact* in the standard sense on the overlap (since $\phi$ is multi-valued there). Treat $-2g\,d\phi$ as the differential of the multi-valued function $f_{SN} = -2g\phi$.

> [!note]- Hint 3
> The transition function is $c_{SN} = e^{(ie/\hbar)f_{SN}} = e^{-2ieg\phi/\hbar}$. For this to be a well-defined single-valued function on the overlap (which is topologically a cylinder, with $\phi \in [0, 2\pi)$ wrapped around), need $c_{SN}(\theta, 0) = c_{SN}(\theta, 2\pi)$, hence $e^{-2ieg \cdot 2\pi/\hbar} = 1$, i.e., $2eg/\hbar \in \mathbb{Z}$.

> [!note]- Hint 4
> Compute the Chern number $c_1$ by integrating the curvature 2-form over $S^2$. The curvature on either patch is $F = -(ie/\hbar)dA = -(ie/\hbar)g\sin\theta\,d\theta \wedge d\phi$. The Chern number is $\frac{1}{2\pi i}\int_{S^2}F = \frac{1}{2\pi i}\cdot(-ie/\hbar)\cdot 4\pi g = \frac{2eg}{\hbar}$.

> [!note]- Hint 5
> For $n = 1$ (i.e., $g = \hbar/(2e)$, the minimum Dirac charge), the bundle $L_1$ is the **Hopf line bundle** over $S^2 \cong \mathbb{CP}^1$. Higher-charge bundles are tensor powers: $L_n \cong H^{\otimes n}$.

---

# Solution

The proof has four steps. Step 1 verifies the two potentials yield the correct field. Step 2 computes the transition function and derives the quantization. Step 3 computes the Chern number via curvature integration. Step 4 identifies the bundle.

**Step 1: Both potentials yield $dA = B$.**

> [!note]- Derivation
> Compute $dA_N$:
> $$dA_N = d[g(1 - \cos\theta)d\phi] = -g \cdot (-\sin\theta\,d\theta) \wedge d\phi = g\sin\theta\,d\theta \wedge d\phi = B. \checkmark$$
>
> Compute $dA_S$:
> $$dA_S = d[-g(1 + \cos\theta)d\phi] = -g \cdot (-\sin\theta\,d\theta) \wedge d\phi = g\sin\theta\,d\theta \wedge d\phi = B. \checkmark$$
>
> Both potentials reproduce the monopole field. They are smooth on their respective domains:
> - $A_N = g(1 - \cos\theta)d\phi$ — at the *north pole* ($\theta = 0$), $(1 - \cos\theta) \to 0$, so the apparent singularity of $d\phi$ at the pole is killed. At the *south pole* ($\theta = \pi$), $(1 - \cos\theta) \to 2$, so $A_N \to 2g\,d\phi$ — singular there. Hence $A_N$ is well-defined on $U_N = S^2 \setminus \{\text{south pole}\}$ but blows up at the south pole.
> - $A_S$ is symmetric: well-defined on $U_S = S^2 \setminus \{\text{north pole}\}$, singular at the north pole.

**Step 2: Transition function and quantization.**

> [!note]- Derivation
> On the overlap $U_N \cap U_S$ (the punctured equatorial band), both $A_N$ and $A_S$ give the same $B$, so they differ by a *closed* 1-form. Compute:
> $$A_S - A_N = -g(1 + \cos\theta)d\phi - g(1 - \cos\theta)d\phi = -2g\,d\phi.$$
>
> The form $-2g\,d\phi$ is closed but *not exact* in the strict sense (since $\phi$ is multi-valued on the punctured plane); treating $\phi$ as the (multi-valued) angle function, $-2g\,d\phi = d(-2g\phi)$. The **gauge function** relating the two patches is therefore $f_{SN} = -2g\phi$.
>
> The transition function is
> $$c_{SN}(\theta, \phi) = \exp\Bigl(\tfrac{ie}{\hbar}f_{SN}\Bigr) = \exp\Bigl(-\tfrac{2ieg}{\hbar}\phi\Bigr).$$
>
> For $c_{SN}$ to be a well-defined function from the overlap to $U(1)$, it must be single-valued in $\phi \in [0, 2\pi)$. Since $c_{SN}(\theta, \phi + 2\pi) = c_{SN}(\theta, \phi) \cdot e^{-2ieg \cdot 2\pi/\hbar}$, single-valuedness requires
> $$e^{-2ieg \cdot 2\pi/\hbar} = 1 \quad\Leftrightarrow\quad \frac{2eg}{\hbar} \in \mathbb{Z}.$$
>
> **This is the Dirac quantization condition.** If satisfied, $c_{SN}$ is a valid $U(1)$-valued transition function, the cocycle condition $c_{NS}c_{SN} = 1$ is automatic (two-patch cover), and the bundle $L_g$ exists. If not, no consistent bundle exists.

**Step 3: First Chern number via curvature integration.**

> [!note]- Derivation
> The curvature of the $U(1)$-connection $\omega = -(ie/\hbar)A$ on either patch is
> $$F_{\mathrm{conn}} = d\omega = -\frac{ie}{\hbar}dA = -\frac{ie}{\hbar}B = -\frac{ie}{\hbar}\cdot g\sin\theta\,d\theta \wedge d\phi.$$
>
> The first Chern number of the bundle is
> $$c_1(L_g) = \frac{1}{2\pi i}\int_{S^2}F_{\mathrm{conn}} = \frac{1}{2\pi i}\int_{S^2}\Bigl(-\frac{ie}{\hbar}\Bigr)g\sin\theta\,d\theta\,d\phi = -\frac{e}{2\pi\hbar}\int_{S^2}g\sin\theta\,d\theta\,d\phi.$$
>
> Computing the integral:
> $$\int_{S^2}g\sin\theta\,d\theta\,d\phi = g \cdot \int_0^\pi\sin\theta\,d\theta \cdot \int_0^{2\pi}d\phi = g \cdot 2 \cdot 2\pi = 4\pi g.$$
>
> Hence
> $$c_1(L_g) = -\frac{e}{2\pi\hbar}\cdot 4\pi g = -\frac{2eg}{\hbar}.$$
>
> The sign convention for $c_1$ varies; with the absolute value, $|c_1| = \frac{2eg}{\hbar}$. The integrality of $c_1$ (i.e., it must be in $\mathbb{Z}$ to be a valid Chern number) gives an alternative derivation of the Dirac quantization condition: $\frac{2eg}{\hbar} \in \mathbb{Z}$. ✓

**Step 4: Identification with $H^{\otimes n}$.**

> [!note]- Derivation
> Complex line bundles over $S^2$ are classified up to isomorphism by their first Chern class $c_1 \in H^2(S^2, \mathbb{Z}) = \mathbb{Z}$. So the bundle $L_g$ with $c_1 = n := 2eg/\hbar$ is uniquely determined up to isomorphism by the integer $n$.
>
> The generator of $\mathrm{Pic}(S^2) = \mathbb{Z}$ is the **Hopf line bundle** $H \to S^2 = \mathbb{CP}^1$ — the tautological bundle whose fibre at $[v] \in \mathbb{CP}^1$ is the complex line $\mathbb{C}v \subset \mathbb{C}^2$. Its first Chern class is $c_1(H) = -1$ (or $+1$, depending on conventions).
>
> Since Chern classes are additive under tensor products ($c_1(L_1 \otimes L_2) = c_1(L_1) + c_1(L_2)$), the bundle with first Chern class $n$ is the $n$-fold tensor power $H^{\otimes n}$ (or $H^{\otimes(-n)} = (H^*)^{\otimes n}$ depending on the sign of $n$).
>
> Hence:
> $$L_g \cong H^{\otimes (2eg/\hbar)}.$$
>
> The unit-modulus subbundle (with structure group $U(1)$) of $L_n$ is the **lens space** $L(n, 1) = S^3/\mathbb{Z}_n$. For $n = 1$, this is $S^3$ itself, with the bundle being the famous **Hopf fibration** $S^3 \to S^2$.

> [!note]- Complete formal solution
> **Setup.** A magnetic monopole of charge $g$ at the origin of $\mathbb{R}^3$ produces $B = g\sin\theta\,d\theta \wedge d\phi$ on $\mathbb{R}^3 \setminus \{0\}$. Restricted to $S^2 \subset \mathbb{R}^3 \setminus \{0\}$ (any sphere, by rotational symmetry), $B$ integrates to $4\pi g \ne 0$, so $B$ is closed but not exact on $\mathbb{R}^3 \setminus \{0\}$.
>
> **Two-patch construction.** Cover $S^2$ by $U_N = S^2 \setminus \{\text{south pole}\}$ and $U_S = S^2 \setminus \{\text{north pole}\}$. Choose potentials $A_N = g(1 - \cos\theta)d\phi$ on $U_N$ (smooth, since $(1 - \cos\theta) = 0$ at the north pole) and $A_S = -g(1 + \cos\theta)d\phi$ on $U_S$ (smooth, since $(1 + \cos\theta) = 0$ at the south pole). Verify $dA_N = dA_S = B$.
>
> **Transition function.** On the overlap, $A_S - A_N = -2g\,d\phi$, so the gauge function is $f_{SN} = -2g\phi$ and the transition function is $c_{SN} = \exp(-2ieg\phi/\hbar)$. Single-valuedness on $\phi \in [0, 2\pi)$ requires $\frac{2eg}{\hbar} \in \mathbb{Z}$ — the Dirac quantization condition.
>
> **Chern number.** $c_1(L_g) = \frac{1}{2\pi i}\int_{S^2}F_{\mathrm{conn}} = \frac{1}{2\pi i}\int_{S^2}(-\frac{ie}{\hbar})B = -\frac{2eg}{\hbar}$. Integer-valuedness of $c_1$ is the same as the quantization condition.
>
> **Identification.** $L_g \cong H^{\otimes(2eg/\hbar)}$, where $H$ is the Hopf line bundle on $S^2$. The unit-modulus subbundle is the lens space $L(2eg/\hbar, 1)$. $\blacksquare$

> [!warning] Verification via Stokes' theorem and the equator
> An alternative computation: the holonomy of the EM connection around the equator $\gamma_{\mathrm{eq}}$ of $S^2$ (at $\theta = \pi/2$) is $\exp((ie/\hbar)\oint_{\gamma_{\mathrm{eq}}}A_N) = \exp((ie/\hbar)\oint g\,d\phi)$. Using $A_N = g(1 - \cos\theta)d\phi$ at $\theta = \pi/2$: $A_N = g\,d\phi$. So $\oint A_N = 2\pi g$, holonomy $e^{2\pi i eg/\hbar}$. For the bundle to exist (so this holonomy is meaningful as a $U(1)$-element), need $eg/\hbar$ rational with denominator dividing 1 (i.e., $eg/\hbar \in \mathbb{Z}/2$, or $2eg/\hbar \in \mathbb{Z}$). Same condition. The same calculation with $A_S$ gives a holonomy differing by the transition function $c_{SN}$ across the equator, also consistent with quantization.

---

# Key Takeaways

**The two-patch construction with non-trivial transition function is the natural geometric way to handle topologically obstructed gauge potentials.**

The classical "Dirac string" — a singular line from the monopole to infinity along which $A$ has a delta-function — is an *artifact* of insisting on a single-patch description. The bundle-theoretic description with two patches and a non-trivial transition function is *cleaner*: no singularities anywhere, just a non-trivial gluing. This is the modern way to think about *any* topologically non-trivial gauge configuration: the *bundle* is the fundamental object, with gauge fields being local descriptions of the connection on the bundle.

**The first Chern number is the universal topological invariant of complex line bundles, computed from any connection's curvature integral.**

The recipe is: pick any hermitian connection $\nabla$ on $L$, integrate its curvature over a closed 2-cycle, normalize by $1/(2\pi i)$, and the answer is an integer — the first Chern number $c_1(L) \in H^2(M, \mathbb{Z})$. The integer is *independent of the connection*: changing $\nabla$ by a tensorial $D \in \Omega^1(M, \mathrm{End}(L))$ changes $F$ by an exact form, leaving the integral invariant. The Dirac quantization is the simplest instance of this universal pattern, and the same recipe applied to other bundles (in condensed matter, in algebraic geometry, in differential topology) produces all the "topological integers" that classify line bundles.

**Two ways to derive the same quantization: gluing-consistency vs. integrality of characteristic class.**

Step 2 derives the quantization from the *local* gluing condition: the transition function $e^{-2ieg\phi/\hbar}$ must be single-valued. Step 3 derives the same quantization from the *global* topological condition: the first Chern number $c_1 = 2eg/\hbar$ must be integer. These are *equivalent* — both express the same underlying topological fact, but from complementary angles. The lesson: in gauge theory, integer quantization conditions almost always have *two* derivations (local cocycle consistency and global characteristic class integrality), and either suffices. The global one is more elegant; the local one is more directly computable in coordinates.

**Cross-link to companion exercise:** See [[Ex - The Aharonov-Bohm Phase from the Magnetic Solenoid]]. The Aharonov-Bohm effect is the *complementary* topological effect: a *flat* connection (zero curvature) on a domain with non-trivial $\pi_1$, classified by a continuous holonomy parameter in $U(1)$. The Dirac monopole is the opposite: a *non-flat* connection on a simply-connected domain $S^2$ ($\pi_1 = 0$), classified by a discrete integer Chern number. Together they exhibit the two ways a $U(1)$-gauge field can carry global topological information — flatness with non-trivial homotopy vs. non-trivial topology with curvature.
