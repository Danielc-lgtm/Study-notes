---
type: exercise
subject: algebraic-topology
difficulty: "⭐⭐"
prereqs:
  - "Def - First Chern Class"
  - "Thm - First Chern Class Classifies Line Bundles over a CW Complex"
tags: [geometry, algebraic-topology, characteristic-classes, gauge-theory, physics]
---

# Problem Statement

A **magnetic monopole** of charge $g$ at the origin of $\mathbb{R}^3$ produces a magnetic field

$$\vec B = \frac{g}{r^2}\hat r, \qquad r = |\vec x|.$$

The corresponding magnetic flux through any sphere $S^2$ surrounding the origin is

$$\Phi = \oint_{S^2} \vec B \cdot d\vec S = 4\pi g.$$

The vector potential $\vec A$ such that $\vec B = \nabla \times \vec A$ **does not exist globally** on $\mathbb{R}^3 \setminus \{0\}$ — the singularity at the origin forces a defect. Instead, $\vec A$ is defined on two patches, with a gauge transformation on their overlap.

This data is the structure of a **complex line bundle** $L \to S^2$ (where $S^2$ surrounds the monopole). Quantum mechanically, the wavefunction $\psi$ of a charged particle (charge $e$) is a section of $L$, and for $\psi$ to be globally well-defined, the bundle must be a *complex* line bundle — characterised by the [[Def - First Chern Class|first Chern class]] $c_1(L) \in H^2(S^2; \mathbb{Z}) = \mathbb{Z}$.

Compute $c_1(L)$ in terms of $g$ and $e$, and derive the **Dirac quantisation condition**:

$$\frac{2eg}{\hbar c} = n \in \mathbb{Z}.$$

**Recall:**

![[Def - First Chern Class#The Definition]]

![[Thm - First Chern Class Classifies Line Bundles over a CW Complex#Statement]]

The **first Chern form** of a $U(1)$ bundle with curvature $F$ is $c_1 = F/(2\pi)$ (in mathematician's units). In physics units, with the charge $e$ and Planck's constant $\hbar$, the connection 1-form for the wavefunction is $\omega = -i(e/\hbar c) A$ where $A$ is the EM vector potential, so the relevant Chern form is $c_1 = (e/2\pi\hbar c) F$ where $F = dA$ is the EM field strength 2-form (whose "magnetic part" is $\vec B$).

---

# Convergent Strategy

**Problem class.** This is a **derive topological quantisation from a physical setup** problem. The strategy is to identify the structure of the magnetic monopole as a $U(1)$ bundle on $S^2$, compute its first Chern class, and use [[Thm - First Chern Class Classifies Line Bundles over a CW Complex|the line bundle classification theorem]] to force integrality.

**Assumption pattern.** The hypothesis is the magnetic monopole physics: a singular point source of magnetic charge $g$ produces a magnetic field $\vec B = g\hat r/r^2$ on $\mathbb{R}^3 \setminus \{0\}$. The quantum-mechanical demand is that the wavefunction $\psi$ (a section of the relevant $U(1)$ bundle) be globally well-defined. The classification of $U(1)$ bundles on $S^2$ by integer cohomology in degree 2 is what forces the integrality.

**Theorem routing.** The route:
1. Identify the EM field-strength 2-form $F$ such that integrating over $S^2$ gives the magnetic flux $4\pi g$.
2. Compute $c_1 = (e/2\pi\hbar c)F$ and integrate: $\int_{S^2} c_1 = 2eg/(\hbar c)$.
3. By [[Thm - First Chern Class Classifies Line Bundles over a CW Complex|the classification theorem]], $\int c_1 \in \mathbb{Z}$, so $2eg/(\hbar c) \in \mathbb{Z}$.
4. This is the Dirac quantisation condition.

**Key decision point.** The non-obvious step is recognising that *the wavefunction is a section of a complex line bundle, not a function*. The monopole creates a topological obstruction to defining $\vec A$ globally; the wavefunction must accommodate this via patch-wise gauge transformations, and the consistency requirement is precisely the existence of a $U(1)$ bundle on $S^2$. This identification is the conceptual move that converts a physical question (when is a magnetic monopole consistent with quantum mechanics?) into a topological one (when does a $U(1)$ bundle exist?).

---

# Legal Operations Used

This solution deploys the following legal operations from [[Algebraic Topology III — Higher Homotopy and Chern Forms#Legal Operations|the topic page's Legal Operations]]:

1. **Compute Chern forms from curvature in a chosen frame** (operation 5). The EM field strength $F$ is the curvature of the $U(1)$ connection $\omega = -i(e/\hbar c) A$.

2. **Integrate Chern forms over cycles to get integers** (operation 6). The integral over $S^2$ enclosing the monopole gives the Chern number, forced to be an integer.

3. **Use the obstruction-cocycle interpretation** (operation 10). The integer $\int c_1$ counts the number of zeros of any generic section — equivalently, the topological obstruction to global existence of the section.

---

# Hints

> [!note]- Hint 1
> What is the field-strength 2-form $F$ corresponding to the magnetic field $\vec B = g\hat r/r^2$? Integrate over a sphere surrounding the monopole.

> [!note]- Hint 2
> In differential-form language, $F = (1/2)F_{ij}dx^i \wedge dx^j$ with $F_{ij} = \epsilon_{ijk}B^k$. For $\vec B = g\hat r/r^2$ in spherical coordinates, $F = g\sin\theta\,d\theta\wedge d\phi$. Integrate over $S^2$: $\int_{S^2} F = 4\pi g$.

> [!note]- Hint 3
> The first Chern class of the wavefunction's $U(1)$ bundle is $c_1 = (e/2\pi\hbar c) F$. Integrate: $\int_{S^2} c_1 = (e/2\pi\hbar c)\cdot 4\pi g = 2eg/(\hbar c)$. This must be an integer by [[Thm - First Chern Class Classifies Line Bundles over a CW Complex|the classification theorem]].

---

# Solution

The proof has three steps: identify the field-strength 2-form, compute the Chern number, derive the quantisation condition.

**Plan paragraph:** the key conceptual move is recognising the wavefunction as a section of a complex line bundle on $S^2$ surrounding the monopole. Once this identification is made, the rest is mechanical: compute $\int F$ (giving the magnetic flux), multiply by the right factors of $e/\hbar c$ (giving $c_1$), and demand integrality (giving Dirac's condition).

**Step 1: The EM field-strength 2-form.**

The magnetic field $\vec B = g\hat r/r^2$ corresponds to the 2-form $F = g\sin\theta\,d\theta\wedge d\phi$ in spherical coordinates on $\mathbb{R}^3 \setminus \{0\}$. The total flux through any sphere $S^2$ centred at the origin is

$$\int_{S^2} F = g \int_0^\pi \sin\theta\,d\theta \int_0^{2\pi} d\phi = g \cdot 2 \cdot 2\pi = 4\pi g.$$

> [!note]- Derivation
> In Maxwell's equations, the magnetic field is a 2-form $F$ with components $F_{ij} = \epsilon_{ijk}B^k$. For a radial magnetic field $\vec B = B(r)\hat r$, the corresponding 2-form is the **solid angle form** rescaled: $F = B(r) r^2 \sin\theta\,d\theta\wedge d\phi$.
>
> For the monopole, $B(r) = g/r^2$, so $F = g\sin\theta\,d\theta\wedge d\phi$. The $r$-dependence cancels, and $F$ is "constant" on every sphere $S^2_r$ centred at the origin. This is a closed form ($dF = 0$ on $\mathbb{R}^3 \setminus \{0\}$, by Maxwell's $\nabla\cdot\vec B = 0$ except at the source) but not globally exact — there is no globally defined $A$ with $F = dA$, exhibiting the topological obstruction.
>
> Integrating over $S^2$ (any radius, since $F$ does not depend on $r$):
> $$\int_{S^2} F = g\int_0^\pi\!\int_0^{2\pi}\sin\theta\,d\phi\,d\theta = 4\pi g,$$
> matching the Gauss-law expectation $\Phi = 4\pi g$ for a monopole of charge $g$.

**Step 2: Compute $c_1$ and the Chern number.**

The wavefunction of a charged particle is a section of a $U(1)$ bundle on $S^2$, with connection 1-form $\omega = -i(e/\hbar c) A$ (the standard minimal coupling). The corresponding curvature is $\theta = -i(e/\hbar c) F$, and the first Chern form is

$$c_1 = \frac{i}{2\pi}\mathrm{Tr}(\theta) = \frac{i}{2\pi}\cdot\!\left(-i\frac{e}{\hbar c}F\right) = \frac{e}{2\pi\hbar c}F.$$

Integrating over $S^2$:

$$\int_{S^2} c_1 = \frac{e}{2\pi\hbar c}\int_{S^2} F = \frac{e}{2\pi\hbar c}\cdot 4\pi g = \frac{2eg}{\hbar c}.$$

> [!note]- Derivation
> The physical setup: a quantum-mechanical particle of charge $e$ in an electromagnetic field with 4-potential $A_\mu$. The wavefunction $\psi$ transforms under gauge transformations $A_\mu \to A_\mu + \partial_\mu\chi$ as $\psi \to e^{ie\chi/\hbar c}\psi$.
>
> Geometrically, this is the statement that $\psi$ is a section of a complex line bundle $L$ on spacetime (or, restricted to the spatial slice $\mathbb{R}^3 \setminus \{0\}$ around the monopole, on this base), with $U(1)$ connection of the form $\omega = -i(e/\hbar c)A$. The covariant derivative $D = d + \omega$ acts on sections: $D\psi = d\psi - i(e/\hbar c)A\psi$. The curvature is $\theta = d\omega = -i(e/\hbar c)dA = -i(e/\hbar c)F$.
>
> The first Chern form is $c_1 = (i/2\pi)\mathrm{Tr}(\theta) = (i/2\pi)(-i(e/\hbar c)F) = (e/2\pi\hbar c)F$.

**Step 3: Integrality forces Dirac quantisation.**

By [[Thm - First Chern Class Classifies Line Bundles over a CW Complex|the line bundle classification theorem]], $\int_{S^2} c_1(L) \in \mathbb{Z}$ for any complex line bundle on $S^2$. So

$$\frac{2eg}{\hbar c} \in \mathbb{Z},$$

i.e., $2eg = n\hbar c$ for some integer $n$. Solving for $g$:

$$g = \frac{n\hbar c}{2e}, \qquad n \in \mathbb{Z}.$$

This is the **Dirac quantisation condition**: magnetic charge is quantised in units of $\hbar c/(2e)$.

> [!note]- Derivation
> The classification theorem says: complex line bundles on a CW complex are in bijection with $H^2(X; \mathbb{Z})$, via the first Chern class. For $X = S^2$, $H^2(S^2; \mathbb{Z}) = \mathbb{Z}$. So $\int_{S^2}c_1(L) \in \mathbb{Z}$ for *any* complex line bundle $L$, with the integer determining the isomorphism class.
>
> If the magnetic monopole were to be consistent with quantum mechanics, the wavefunction must be a section of *some* complex line bundle on $S^2$, and the integer attached must be $2eg/(\hbar c)$ (from our calculation). The only way this is possible is if $2eg/(\hbar c) \in \mathbb{Z}$.
>
> Conversely, *every* integer $n$ corresponds to a valid magnetic monopole charge $g = n\hbar c/(2e)$, with the wavefunction being a section of the $n$-th tensor power of the Hopf bundle. So Dirac quantisation is both necessary (for consistency) and sufficient (no other constraints needed) for a magnetic monopole to exist in a quantum-mechanical theory.

> [!note]- Complete formal solution
> The magnetic monopole at the origin of $\mathbb{R}^3$ with charge $g$ produces field-strength 2-form $F = g\sin\theta\,d\theta\wedge d\phi$ on $\mathbb{R}^3 \setminus \{0\}$. On the sphere $S^2$ surrounding the origin, this 2-form is closed but not exact: there is no globally defined vector potential $A$ with $F = dA$ on $S^2$.
>
> The wavefunction of a charged particle (charge $e$) in this background is geometrically a section of a complex line bundle $L \to S^2$, with $U(1)$ connection $\omega = -i(e/\hbar c)A$ defined locally on patches of $S^2$, with the two-patch transition function being a gauge transformation.
>
> The curvature is $\theta = -i(e/\hbar c)F$, and the first Chern form is
> $$c_1(L) = \frac{e}{2\pi\hbar c}F.$$
>
> Integrating over $S^2$:
> $$\int_{S^2} c_1(L) = \frac{e}{2\pi\hbar c}\int_{S^2}F = \frac{e}{2\pi\hbar c}\cdot 4\pi g = \frac{2eg}{\hbar c}.$$
>
> By the line-bundle classification theorem, $\int c_1 \in \mathbb{Z}$, hence
> $$\frac{2eg}{\hbar c} \in \mathbb{Z} \quad\Longleftrightarrow\quad g = \frac{n\hbar c}{2e}, \quad n \in \mathbb{Z}.$$
>
> This is the **Dirac quantisation condition**: magnetic charge is quantised in units of $\hbar c/(2e)$. $\blacksquare$

> [!warning] Sanity check: $n = 0$ gives no monopole
> The integer $n = 0$ corresponds to $g = 0$ — no magnetic monopole. The wavefunction is then a section of the trivial line bundle $L = S^2 \times \mathbb{C}$, which has a global non-vanishing section (the constant function 1). This is the "no monopole" case, consistent with the absence of topological obstruction.

> [!warning] What if there are *no* magnetic monopoles?
> Dirac's argument shows: *if even one magnetic monopole exists anywhere in the universe, then electric charge is quantised* (the unit being $e = n\hbar c/(2g)$ for the monopole of smallest charge $g$). Experimentally, electric charge *is* quantised — every observed particle has charge in $\{0, \pm e/3, \pm 2e/3, \pm e\}$ — but no magnetic monopole has been observed. The Dirac argument suggests they should exist, providing a natural explanation for electric-charge quantisation. **'t Hooft–Polyakov monopoles** in non-Abelian gauge theories are predicted to exist (as solitons of grand unified theories), and the search for monopoles continues to be a topic of experimental physics.

---

# Key Takeaways

**The wavefunction is a section of a complex line bundle, not a function.** This is the *foundational* conceptual move that makes Dirac quantisation natural. In the absence of magnetic monopoles, the bundle is trivial and we can treat $\psi$ as an ordinary function (a section of the trivial bundle). When a monopole is present, the bundle becomes non-trivial, and the wavefunction *cannot* be a global function — it must be defined patch by patch with consistent gauge transformations on overlaps. The topological structure of the bundle (its Chern class) becomes a physical observable, and its integer values correspond to allowed monopole charges. The lesson is universal: *in gauge theory, the basic dynamical objects are sections of bundles, not functions*, and topological invariants of the bundles become topological quantum numbers of the physics.

**Topological quantisation = integrality of characteristic classes.** Every quantised topological quantity in physics — magnetic charge, electric charge (via Dirac), instanton number, Hall conductivity, vortex winding — is an integral of a characteristic class over a closed cycle. The integrality is *not* a postulate but a consequence of the existence of an underlying bundle structure. The lesson: *when faced with a quantised observable in physics, ask which bundle's characteristic class produces the integer*. The answer often reveals the deeper structural reason for the quantisation — Dirac for magnetic charge, $\pi_3(SU(n))$ for instantons, $H^2(T^2; \mathbb{Z})$ for the IQHE.

**Patches and transition functions are the geometric content of "gauge invariance".** The magnetic monopole forces the vector potential $A$ to be defined on two patches (e.g., $S^2$ minus north pole and $S^2$ minus south pole), with a gauge transformation $A_+ - A_- = -i d\log g_{+-}$ on the overlap (a circle around the equator). The transition function $g_{+-} : S^1 \to U(1)$ has a winding number, which is precisely the first Chern number of the bundle. The lesson is that the bookkeeping of "gauge transformations on overlaps" is the differential-geometric realisation of "the bundle is topologically non-trivial", with the winding number of the transition function being the integer Chern class. The same picture applies to non-Abelian gauge theory: transition functions $g : S^{n-1} \to G$ define principal $G$-bundles by clutching, and elements of $\pi_{n-1}(G)$ classify the topology.
