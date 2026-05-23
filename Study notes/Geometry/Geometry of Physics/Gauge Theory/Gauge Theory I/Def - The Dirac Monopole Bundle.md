---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Complex Line Bundle"
  - "Def - U(1) Gauge Field and Electromagnetic Connection"
  - "Def - Local Trivialization"
  - "Def - Transition Function of a Vector Bundle"
tags: [geometry, gauge-theory, monopole, line-bundle]
---

# Notation

$M = \mathbb{R}^3 \setminus \{0\}$ — the punctured 3-space with the monopole removed — or equivalently $S^2 \subset M$ (a sphere of any radius, since the bundle is invariant under radial scaling). The monopole has magnetic charge $g > 0$ (Frankel's notation; sometimes also written $q$). The electron has electric charge $e$ and Planck's constant is $\hbar$. We use the **standing convention** $c = 1$. The two patches covering $S^2$ are $U_N = S^2 \setminus \{\text{south pole}\}$ and $U_S = S^2 \setminus \{\text{north pole}\}$ — neither contains a Dirac string, and their overlap $U_N \cap U_S$ is the equatorial band, homotopic to $S^1$. Spherical coordinates: $\theta \in [0, \pi]$ (colatitude from north pole), $\phi \in [0, 2\pi)$ (azimuth). For the parent symbol registry see [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

---

# Axiom Motivation

The Dirac monopole bundle exists because **the magnetic field of a magnetic monopole cannot be written as $B = \nabla \times A$ for a globally defined $A$**. This is a topological obstruction, and the bundle is its resolution.

Start with the magnetic field $B = (g/r^2)\hat r$ of a hypothetical magnetic monopole of strength $g$ at the origin of $\mathbb{R}^3$. As a 2-form on $\mathbb{R}^3 \setminus \{0\}$,

$$B = g\sin\theta\,d\theta \wedge d\phi.$$

Compute its de Rham class. Integrating over the unit sphere $S^2$: $\int_{S^2}B = g\int_0^\pi\int_0^{2\pi}\sin\theta\,d\theta\,d\phi = 4\pi g \ne 0$. So $B$ is closed ($dB = 0$, since it is a 2-form on a 3-manifold and a quick check confirms) but *not exact* — there is no globally defined 1-form $A$ on $\mathbb{R}^3 \setminus \{0\}$ with $B = dA$. (If there were, Stokes' theorem would force $\int_{S^2}B = \oint_{\partial S^2}A = 0$, since $S^2$ has no boundary.)

The classical resolution is to introduce a **Dirac string**: a half-line from the origin to infinity along which $A$ has a delta-function singularity, so that $A$ is defined everywhere off the string. Different choices of string give different singular $A$'s, all yielding the correct $B$ away from the string. But the string is unphysical — there is no preferred axis — and the wave function must somehow "not see" the string.

The geometric resolution is to **cover $\mathbb{R}^3 \setminus \{0\}$ by two open sets, with $A$ defined separately on each, glued by a gauge transformation on the overlap**. Choose

- $U_N = S^2 \setminus \{\text{south pole}\}$ with $A_N = g(1 - \cos\theta)\,d\phi$ — finite everywhere on $U_N$ since $1 - \cos\theta = 0$ at the north pole, so $(1 - \cos\theta)d\phi$ is well-defined as a 1-form (the apparent singularity of $d\phi$ at the pole is cancelled). The Dirac string is at the *south* pole.
- $U_S = S^2 \setminus \{\text{north pole}\}$ with $A_S = -g(1 + \cos\theta)\,d\phi$ — finite everywhere on $U_S$ since $1 + \cos\theta = 0$ at the south pole. The Dirac string is at the *north* pole.

On the overlap $U_N \cap U_S$ (everything except the two poles), both $A_N$ and $A_S$ give the same $B$ via $B = dA$, so they differ by a closed 1-form. Compute: $A_S - A_N = -g(1 + \cos\theta)d\phi - g(1 - \cos\theta)d\phi = -2g\,d\phi$. This is *not exact* on the overlap — $d\phi$ is a closed 1-form on the punctured plane $\mathbb{R}^2 \setminus \{0\}$ generating $H^1(\mathbb{R}^2 \setminus \{0\}, \mathbb{R})$, and the overlap $U_N \cap U_S$ retracts onto an equatorial circle. But if we permit $\phi$ to be multi-valued (interpret $d\phi$ as the *exterior derivative of the angle function*, even though the angle is not single-valued), then $A_S = A_N + d(-2g\phi)$.

The wave function $\psi$ exists on both patches, related on the overlap by $\psi_S = c_{SN}\psi_N$ for a transition function $c_{SN} = e^{(ie/\hbar)f_{SN}}$ where $f_{SN}$ is the "gauge function" satisfying $A_S = A_N + df_{SN}$. Here $f_{SN} = -2g\phi$, so

$$c_{SN}(\theta, \phi) = \exp\bigl(-\tfrac{2ieg}{\hbar}\phi\bigr).$$

**Single-valuedness.** $c_{SN}$ is a map from the overlap $U_N \cap U_S$ (which we can take to be the equatorial band, parameterised by $(\theta, \phi)$ with $\theta$ near $\pi/2$) to $U(1)$. For this to be a well-defined function of $\phi \in [0, 2\pi)$ — i.e., for $c_{SN}(\theta, 0) = c_{SN}(\theta, 2\pi)$ — we need $e^{-(2ieg/\hbar) \cdot 2\pi} = 1$, that is,

$$\boxed{\frac{2eg}{\hbar} \in \mathbb{Z}.}$$

This is the **Dirac quantization condition**. If satisfied, the transition function is well-defined and we have a genuine $U(1)$-bundle over $S^2$; if not, no consistent bundle exists and the wave function of an electron in this monopole's field cannot be globally defined.

Why does this construction work? Three structural reasons. (i) The cocycle condition $c_{NS}c_{SN} = 1$ is automatic for a two-patch cover. (ii) The transition function is unitary ($|c_{SN}| = 1$), so the structure group reduces correctly to $U(1)$. (iii) The "magnetic charge in the bundle" — the first Chern number $c_1 = \frac{1}{2\pi}\int_{S^2}F = \frac{2eg}{\hbar}$ — is forced to be integer by the cocycle condition, matching the quantization. The bundle classifies completely as the $(2eg/\hbar)$-fold tensor power of the Hopf bundle $H \to S^2$ (or its dual).

Why is the bundle defined on $S^2$ rather than $\mathbb{R}^3 \setminus \{0\}$? Because $\mathbb{R}^3 \setminus \{0\}$ deformation-retracts onto $S^2$, so $U(1)$-bundles on the punctured space are the same as $U(1)$-bundles on $S^2$ — classified by $H^2(S^2, \mathbb{Z}) \cong \mathbb{Z}$. The integer in question is exactly the first Chern number $2eg/\hbar$. The bundle "exists on $\mathbb{R}^3 \setminus \{0\}$" but its topology is concentrated at the sphere.

What does this exclude? A single-patch description of the monopole bundle — by topology, no such description can exist for any $eg \ne 0$. The Dirac string of classical electromagnetism is the *price* of insisting on a single patch; the multi-patch bundle is the topologically correct description without artificial strings.

---

# The Definition

The **Dirac monopole bundle** of strength $g$ is the hermitian complex line bundle $L_g \to S^2$ specified by the following two-patch description:

**Patches:**
- $U_N = S^2 \setminus \{\text{south pole}\}$ — covers the northern hemisphere and equator
- $U_S = S^2 \setminus \{\text{north pole}\}$ — covers the southern hemisphere and equator

**Connection 1-forms** (in the EM dictionary $\omega = -(ie/\hbar)A$):
- On $U_N$: $A_N = g(1 - \cos\theta)\,d\phi$, hence $\omega_N = -\tfrac{ie}{\hbar}g(1 - \cos\theta)\,d\phi$
- On $U_S$: $A_S = -g(1 + \cos\theta)\,d\phi$, hence $\omega_S = \tfrac{ie}{\hbar}g(1 + \cos\theta)\,d\phi$

**Transition function** on $U_N \cap U_S$ (the punctured sphere minus both poles):

$$c_{SN}(\theta, \phi) := \exp\bigl(-\tfrac{2ieg}{\hbar}\phi\bigr) \in U(1).$$

**Well-definedness.** The transition function $c_{SN}$ is a single-valued function of $\phi$ iff

$$\frac{2eg}{\hbar} \in \mathbb{Z}.$$

This is the **Dirac quantization condition**. When it holds, $L_g$ is a genuine smooth hermitian line bundle over $S^2$ (and by extension over $\mathbb{R}^3 \setminus \{0\}$) — see [[Thm - Dirac Quantization Condition]].

**Curvature.** Computing on either patch (the result agrees on overlaps since $F$ is gauge-invariant):

$$F = dA_N = g\sin\theta\,d\theta \wedge d\phi.$$

This is the standard area form on $S^2$ multiplied by $g$ — the magnetic field of a monopole of strength $g$ expressed as a 2-form.

**First Chern number** (the topological invariant):

$$c_1(L_g) = \frac{1}{2\pi}\int_{S^2}F = \frac{1}{2\pi}\cdot 4\pi g = 2g \quad\text{(in units with } e/\hbar = 1\text{)}.$$

In general units: $c_1(L_g) = \frac{2eg}{\hbar}$, the same integer that appears in the Dirac quantization condition.

**Classification.** $L_g \cong H^{\otimes(2eg/\hbar)}$, where $H \to S^2 \cong \mathbb{CP}^1$ is the Hopf line bundle (or its dual, depending on orientation conventions). The bundle is non-trivial iff $eg \ne 0$.

---

# Categorical / Structural Definition

In the language of principal bundles, the Dirac monopole bundle is the principal $U(1)$-bundle over $S^2$ with first Chern class $2eg/\hbar \in H^2(S^2, \mathbb{Z}) = \mathbb{Z}$. The total space of the unit-modulus subbundle is the **lens space** $L(2eg/\hbar, 1)$ — for $2eg/\hbar = 1$, this is the *Hopf fibration* $S^3 \to S^2$ with fibre $S^1 = U(1)$.

From the homotopy-theory viewpoint, isomorphism classes of $U(1)$-bundles on $S^2$ are in bijection with $[S^2, BU(1)] = [S^2, \mathbb{CP}^\infty] = \pi_2(\mathbb{CP}^\infty) = \mathbb{Z}$. The Dirac monopole bundle with charge $g$ realizes the integer $2eg/\hbar$ in this classification.

From the Chern-class viewpoint, the line bundle $L_g$ is uniquely (up to isomorphism) determined by its first Chern class, and $\mathrm{Pic}(S^2) = \mathbb{Z}$ generated by $H$. So $L_g \cong H^{\otimes 2eg/\hbar}$.

---

# Relate to Other Fields / Compression

The Dirac monopole bundle is **"the simplest non-trivial $U(1)$-bundle in physics"**, and historically the first instance where the global topology of a bundle was forced by a physical consideration (the existence of magnetic monopoles).

**In algebraic topology**, the Dirac monopole bundle of charge $1$ ($2eg/\hbar = 1$) is the Hopf line bundle on $\mathbb{CP}^1 = S^2$, the generator of $\mathrm{Pic}(S^2) = \mathbb{Z}$. It is the basic example of a non-trivial complex line bundle and is the building block of all line bundles on the sphere via tensor products. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].

**In gauge theory**, the Dirac monopole bundle is the prototype of a non-trivial gauge bundle: a bundle whose existence cannot be reduced to a global gauge choice. Its analogues for non-abelian gauge groups include the **'t Hooft-Polyakov monopole** (a topological soliton in a spontaneously broken $SU(2)$ gauge theory whose long-range behaviour is precisely a Dirac monopole embedded in $SU(2)$). See [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet]] for the connection to general fibre-bundle classification.

**In condensed matter**, the analogue of the Dirac monopole appears in **band theory**: the Bloch wave function $\psi_n(k)$ of an electron in a crystalline solid is a section of a complex line bundle over the Brillouin zone (a torus $T^d$). When the band gap closes at isolated points in the Brillouin zone, these "Berry monopoles" or **Weyl points** carry an integer Berry curvature flux that is the analogue of the Dirac charge $2eg/\hbar$. This is the topological origin of **Weyl semimetals** and the surface "Fermi arcs" of topological materials.

**True name:** The Dirac monopole bundle is **"the bundle whose first Chern number is $2eg/\hbar$ on $S^2$"** — a topologically simple object indexed by a single integer. The geometric incarnation as "magnetic monopole field with quantized charge" is one realization; the algebraic-topological incarnation as "tensor power of the Hopf bundle" is another; the analytic incarnation as "two-patch potential glued by $e^{-2ieg\phi/\hbar}$" is a third.

---

# Examples / Corollaries

**Is an instance: Trivial monopole ($g = 0$).** No magnetic charge, $L_0$ is the trivial bundle $S^2 \times \mathbb{C}$ with constant transition function $c_{SN} = 1$. The wave function is a globally defined complex-valued function on $S^2$. First Chern number $= 0$.

**Is an instance: Minimal monopole ($2eg/\hbar = 1$).** The smallest non-zero charge satisfying Dirac quantization: $g = \hbar/(2e)$. The bundle $L_1$ is isomorphic to the Hopf bundle. The total space of the unit circle subbundle is $S^3$, and the bundle structure is the Hopf fibration $S^3 \to S^2$.

**Is an instance: Higher-charge monopole ($2eg/\hbar = n$).** Magnetic charge $g = n\hbar/(2e)$ for any integer $n$. The bundle is $L_n \cong H^{\otimes n}$, the $n$-fold tensor power of the Hopf bundle. The total space of the unit circle subbundle is the lens space $L(n, 1) = S^3 / \mathbb{Z}_n$.

**Is an instance: Magnetic charge in unified gauge theories.** Grand unified theories (gauge group $\supset SU(5)$ with $U(1)_{\mathrm{EM}}$ as a subgroup) automatically contain stable magnetic monopole solutions — the **'t Hooft-Polyakov monopoles**. Their long-range behaviour is precisely a Dirac monopole with the minimum quantized charge, embedded in the larger gauge structure.

**Is NOT an instance: A magnetic monopole with $2eg/\hbar = 1/2$ or other non-integer.** The transition function $e^{-i\phi}$ on a half-turn would be double-valued — the bundle does not exist. *Conclusion*: if magnetic monopoles exist at all, their charge is quantized in units of $\hbar/(2e)$. (This is currently a hypothesis; no monopole has been observed.)

**Corollary (existence of bundle ⟺ Dirac quantization).** The Dirac monopole bundle $L_g$ exists as a $U(1)$-bundle over $S^2$ if and only if $2eg/\hbar$ is an integer. This is a topological consequence of the cocycle condition; see [[Thm - Dirac Quantization Condition]].

**Corollary (consequence for electric charge).** If a single magnetic monopole of charge $g$ exists anywhere in the universe, then the electric charge $e$ of any particle satisfying $\frac{2eg}{\hbar} \in \mathbb{Z}$ — i.e., *every* charged particle — must be a multiple of $\hbar/(2g)$. This *explains* the observed quantization of electric charge: all observed elementary charges are integer multiples of $e/3$ (quark charges), and quark charges are exactly the unit appropriate to the existence of a minimum monopole. This argument, while assuming the unobserved monopole, was historically the original motivation for Dirac's introduction of magnetic monopoles.

**Corollary (sections are non-trivial)**. The bundle $L_g$ for $g \ne 0$ has no nowhere-vanishing global section — by the classification of line bundles, only $L_0$ admits a global section. Hence: the wave function of an electron in the field of a monopole has *zeros* at certain locations on every sphere around the monopole. This is the geometric counterpart of "phase ambiguity at the Dirac string".

**Calibration check.** (1) Verify the transition function: $A_S - A_N = -2g\,d\phi$, and $c_{SN} = \exp((ie/\hbar)\int(A_S - A_N))$. Here $\int(-2g\,d\phi) = -2g\phi$, giving $c_{SN} = e^{-2ieg\phi/\hbar}$. ✓ (2) Check the cocycle condition: there are only two patches, so it reduces to $c_{NS}c_{SN} = 1$, automatic from $c_{NS} = c_{SN}^{-1}$. ✓ (3) Compute the first Chern number: $\frac{1}{2\pi}\int_{S^2}F = \frac{1}{2\pi}\int_{S^2}g\sin\theta\,d\theta\,d\phi = \frac{4\pi g}{2\pi} = 2g$ in units with $e/\hbar = 1$, i.e., $2eg/\hbar$ in general. ✓

---

# Unlocked by This

> [!tip] 't Hooft-Polyakov Monopole and Magnetic Solitons *(from Particle Physics)*
> In a spontaneously broken non-abelian gauge theory — e.g., $SU(2)$ broken to $U(1)$ by a Higgs field — there exist topologically stable soliton solutions whose long-range fields look like Dirac monopoles. These **'t Hooft-Polyakov monopoles** carry mass $\sim M_W/\alpha$ (where $M_W$ is the symmetry-breaking scale and $\alpha$ the fine-structure constant), and they are an inevitable prediction of *any* grand unified theory containing $U(1)_{\mathrm{EM}}$. The early universe should have produced these monopoles in profusion — the **monopole problem** of cosmology — which was a major motivation for the inflationary cosmology.

> [!tip] The Hopf Fibration and Higher-Charge Monopoles *(from Algebraic Topology)*
> The unit circle bundle of $L_n$ (the $n$-charge Dirac monopole bundle) is the lens space $L(n, 1) = S^3/\mathbb{Z}_n$. For $n = 1$, this is $S^3$ itself, fibred over $S^2$ by the **Hopf fibration** — one of the most famous examples in algebraic topology and the only "non-trivial example" of a fibre bundle that exists below the topological-classification machinery. The higher-charge bundles give the family of lens spaces, which classify rational homology 3-spheres up to a finite ambiguity. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].

> [!tip] Berry Connection and Topological Phases of Matter *(from Condensed Matter Physics)*
> Replace the parameter $\phi$ of the Dirac monopole construction by some other parameter of a quantum system — say, the crystal momentum $k$ in a band insulator. The Bloch wave function $\psi(k)$ then defines a section of a complex line bundle over the Brillouin zone (a $d$-dimensional torus). Closing the band gap at isolated points produces "Berry monopoles" with integer Berry-curvature flux on small enclosing spheres in $k$-space — the same construction as the Dirac monopole, in a totally different physical setting. **Weyl semimetals** are precisely materials with such Berry monopoles in their band structure, and their existence is a manifestation of the same topological constraint that gave us Dirac quantization.
