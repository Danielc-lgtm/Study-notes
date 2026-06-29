---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Spacetime Interval"
  - "Def - Minkowski Space and the Metric"
  - "Thm - Invariance of the Spacetime Interval"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. Points of [[Def - Minkowski Space and the Metric|Minkowski space]] are **events**; in an inertial frame an event has coordinates $x^\mu = (t,x,y,z)$, $\mu = 0,1,2,3$, with $x^0 = t$. The **Minkowski metric** is $\eta$, with components $\eta_{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$, and $X\cdot Y = \eta_{\mu\nu}X^\mu Y^\nu$. A Lorentz transformation is written $\Lambda$, a $4\times 4$ real matrix with components $\Lambda^\mu{}_\nu$ (upper index labels rows, lower labels columns); $\Lambda^{\mathsf T}$ is its transpose. We write the group as $O(1,3)$, with $SO(1,3)$ the proper subgroup and $SO^+(1,3)$ the proper orthochronous (restricted) subgroup. The Einstein summation convention is in force: a repeated index, once up once down, is summed over $0,1,2,3$. Full registry on [[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group]].

> [!warning] Convention: opposite signature in Gourgoulhon
> Gourgoulhon's *Special Relativity in General Frames* uses the mostly-**plus** signature $\eta = \mathrm{diag}(-1,1,1,1)$ and denotes the group $O(3,1)$, so for him a timelike vector has $X\cdot X < 0$ and the timelike basis vector $\vec e_0$ has scalar square $-1$. We use mostly-**minus**, $\mathrm{diag}(1,-1,-1,-1)$, and write $O(1,3)$. The two differ by an overall sign of $\eta$; the defining equation $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ is unchanged by the flip (both sides scale together), and so are the component conditions $\det\Lambda = \pm 1$ and $\Lambda^0{}_0 \ge 1$ that cut out the subgroups below. Only the labelling $(1,3)$ versus $(3,1)$ and the sign of "timelike" differ.

---

# Axiom Motivation

By the end of the postulate-based development there is a body of facts — the [[Def - The Lorentz Transformation|Lorentz transformation]], the [[Thm - Invariance of the Spacetime Interval|invariant interval]], the boost formulas — but they sit as a list. The single most clarifying move in the whole subject is to stop treating the boost formula as primary and ask instead: *what is the set of all coordinate changes that preserve the interval?* That set is the object this page defines, and the answer reorganises everything.

The desideratum is exact and it comes straight from the [[Thm - Invariance of the Spacetime Interval|invariance theorem]]'s converse half. We want the collection of linear maps $\Lambda$ of [[Def - Minkowski Space and the Metric|Minkowski space]] that leave the interval $\Delta s^2 = \eta_{\mu\nu}\,\Delta x^\mu\Delta x^\nu$ unchanged for *every* pair of events. The theorem already told us this collection is exactly the matrices solving $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$. The only design decision left is to recognise that this collection is a **group**, because that single algebraic fact organises the entire structure: it tells us the transformations compose, invert, and contain the identity, which is precisely the structure a "change of inertial frame" must have.

Why insist on *linearity*? Because inertia demands it. A free particle moves in a straight line at constant velocity in any inertial frame; a transformation between inertial frames must therefore carry straight lines to straight lines, and (fixing the origin) the only such maps are linear. Drop linearity and the maps no longer form a finite-dimensional matrix group, and a "boost" could bend a worldline — which would mean a free particle accelerates merely because you changed observers, a contradiction. Linearity is what makes $\Lambda$ a matrix and the group a matrix group.

Why insist on *preserving the full interval* rather than something weaker? Consider the two nearby variants and watch them fail. If you ask only for maps preserving the *light cone* $\Delta s^2 = 0$ (the set of light rays), you get a strictly larger collection — the maps $\Lambda$ with $\Lambda^{\mathsf T}\eta\,\Lambda = \kappa\,\eta$ for any positive scalar $\kappa$, which includes the dilations $x \mapsto \lambda x$ that rescale all of spacetime. These are the *conformal* transformations of the cone, and they are too many: a dilation changes the rest mass of every particle, so it is not a symmetry of physics. The principle of relativity, that the relation between two frames is symmetric ($\kappa(v)\kappa(-v) = 1$ with $\kappa$ depending only on $|v|$), is exactly what forces $\kappa = 1$ and cuts the conformal group down to the Lorentz group. Conversely, if you demanded preservation of the *Euclidean* form $\Delta t^2 + \Delta x^2 + \cdots$ (all plus signs) you would get $O(4)$, the rotation group of four-dimensional Euclidean space — which has no boosts at all, no light cone, and no distinction between time and space. The single sign flip from $+{+}{+}{+}$ to $+{-}{-}{-}$ in $\eta$ is the entire difference between $O(4)$ and the physically correct $O(1,3)$.

The group has a definite number of parameters, and counting them is itself motivation for the definition. The matrix $\Lambda$ has $16$ entries; the equation $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ equates two symmetric $4\times 4$ matrices, which is $10$ independent scalar equations; so the solution set is $16 - 10 = 6$-dimensional. Those six parameters split as three rotations of space and three boosts — and the fact that this count comes out to exactly the number of independent rotation planes in four dimensions ($\binom{4}{2} = 6$) is the first hint that the Lorentz group is the four-dimensional "rotation group" of an indefinite metric. The definition is not an arbitrary choice; it is forced, parameter for parameter, by the demand that the interval be preserved.

---

# The Definition

The **Lorentz group** $O(1,3)$ is the set of $4\times 4$ real matrices $\Lambda$ satisfying
$$
\Lambda^{\mathsf T}\,\eta\,\Lambda \;=\; \eta,
\qquad
\eta = \mathrm{diag}(1,-1,-1,-1),
$$
equipped with matrix multiplication. In index form the defining condition reads
$$
\eta_{\alpha\beta}\,\Lambda^{\alpha}{}_{\mu}\,\Lambda^{\beta}{}_{\nu} \;=\; \eta_{\mu\nu}.
$$
Equivalently — and this is the conceptual content — $O(1,3)$ is the set of linear maps of [[Def - Minkowski Space and the Metric|Minkowski space]] that preserve the [[Thm - Invariance of the Spacetime Interval|spacetime interval]]: $\Lambda \in O(1,3)$ if and only if $(\Lambda X)\cdot(\Lambda Y) = X\cdot Y$ for all four-vectors $X, Y$. The elements are called **Lorentz transformations**; a matrix representing one in an orthonormal (pseudo-orthonormal) basis is a **Lorentz matrix**.

**The four components.** Two scalar functions are constant on each connected piece of $O(1,3)$.

- Taking determinants of $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ and using $\det\eta = -1 \neq 0$ gives $(\det\Lambda)^2 = 1$, so $\det\Lambda = \pm 1$. Transformations with $\det\Lambda = +1$ are **proper**; they preserve orientation. They form a subgroup, the **proper Lorentz group** $SO(1,3)$.
- Setting $\mu = \nu = 0$ in the index form gives $(\Lambda^0{}_0)^2 = 1 + \sum_{i=1}^3 (\Lambda^i{}_0)^2 \ge 1$, so $\Lambda^0{}_0 \ge 1$ or $\Lambda^0{}_0 \le -1$. Transformations with $\Lambda^0{}_0 \ge 1$ are **orthochronous**; they preserve the direction of time (map future-pointing timelike vectors to future-pointing ones). They form a subgroup, the **orthochronous Lorentz group** $O^+(1,3)$.

The two signs are independent, so $O(1,3)$ has exactly **four connected components**:
$$
O(1,3) \;=\; \underbrace{SO^+(1,3) \ \cup\ SO^-_{\text{anti}}(1,3)}_{SO(1,3)} \ \cup\ O^{+}_{\text{improper}}(1,3) \ \cup\ O^-_{\text{anti, improper}}(1,3).
$$
The piece containing the identity is the **restricted Lorentz group**
$$
SO^+(1,3) \;=\; \{\Lambda \in O(1,3) : \det\Lambda = +1 \ \text{and}\ \Lambda^0{}_0 \ge 1\},
$$
the **proper orthochronous** Lorentz group — proper and orthochronous at once. It is the connected component of the identity, the only one of the four components that is a subgroup, and the one with direct physical meaning: it is precisely the set of transformations relating the local frames of two inertial observers, both right-handed and both with time running forwards. The other three components are reached from $SO^+(1,3)$ by composing with parity $P = \mathrm{diag}(1,-1,-1,-1)$, time reversal $T = \mathrm{diag}(-1,1,1,1)$, or the spacetime inversion $PT = -\,\mathrm{Id}$.

**Dimension.** $O(1,3)$ is a six-dimensional [[Def - Lie Algebra of the Lorentz Group|Lie group]]: three parameters for spatial rotations and three for boosts.

---

# Categorical / Structural Definition

The Lorentz group is most cleanly defined not by its matrix condition but by *what it is the symmetry of*. Fix the inner-product space $(\mathbb{R}^4, \eta)$ — a four-dimensional real vector space carrying the non-degenerate symmetric bilinear form $\eta$ of signature $(1,3)$. The **Lorentz group is the isometry group of this form**: the group of all linear maps $\Lambda : \mathbb{R}^4 \to \mathbb{R}^4$ that preserve $\eta$, written
$$
O(1,3) \;=\; \mathrm{Isom}(\mathbb{R}^4, \eta) \;=\; \mathrm{Aut}(\mathbb{R}^4, \eta).
$$
"Isometry" means $\eta(\Lambda X, \Lambda Y) = \eta(X, Y)$ for all $X, Y$; "automorphism" means a structure-preserving invertible self-map of the object $(\mathbb{R}^4, \eta)$ in the category of inner-product spaces with linear isometries as morphisms. The matrix equation $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ is simply this preservation written in coordinates.

This places the Lorentz group inside a uniform family, the **pseudo-orthogonal groups** $O(p,q)$, the isometry groups of the non-degenerate symmetric bilinear forms of signature $(p,q)$. The Euclidean rotation group $O(n) = O(n,0)$ is the isometry group of the positive-definite form, defined by $R^{\mathsf T} I\, R = I$. The Lorentz group $O(1,3)$ is its indefinite cousin, defined by the identical equation with the identity matrix $I$ replaced by $\eta$: $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$. The word **pseudo-orthogonal** names exactly this — "orthogonal with respect to an indefinite form". The single datum distinguishing the members of the family is the signature, and the entire qualitative difference between rotations and boosts — compactness versus non-compactness, bounded versus unbounded group elements, the existence of a light cone — is the difference between definite and indefinite signature.

The structural definition has three immediate payoffs the matrix definition obscures. First, the **group axioms are free**: a composition of isometries is an isometry, the identity is an isometry, and the inverse of an isometry is an isometry, so no separate verification is needed (this is the content of [[Ex - The Lorentz group as pseudo-orthogonal transformations]]). Second, it is **basis-independent**: the isometry group is intrinsic to $(\mathbb{R}^4, \eta)$ and does not refer to any choice of coordinates, whereas the matrix $\Lambda$ does. Third, it makes the analogy with rotations *literal* rather than poetic: a boost is an isometry of an indefinite form exactly as a rotation is an isometry of a definite form, and "boost = hyperbolic rotation" ([[Def - Boosts as Hyperbolic Rotations]]) is the statement that the indefiniteness turns the circular trigonometry of $O(2)$ into the hyperbolic trigonometry of $O(1,1)$.

---

# Relate to Other Fields / Compression

The Lorentz group is the first non-compact semisimple Lie group most physicists meet, and almost every structural fact about it has a familiar Euclidean counterpart that it deforms by one sign. The rotation group $SO(3)$ is its maximal compact subgroup (the block $\mathrm{diag}(1, H)$ with $H \in SO(3)$ sits inside $SO^+(1,3)$). The boosts are the non-compact directions — they form not a subgroup but a submanifold diffeomorphic to $\mathbb{R}^3$, and the failure of two non-collinear boosts to compose to a boost (their product is a boost times a rotation, the **Thomas rotation**) is the non-compactness made visible.

**True name:** the Lorentz group is **"the matrices that turn $\eta$ into $\eta$ by congruence"** — the solution set of $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$. This is the form you compute with: to check whether a given matrix is Lorentz, you do not picture a boost, you multiply out $\Lambda^{\mathsf T}\eta\,\Lambda$ and compare with $\eta$. To preserve the interval is to preserve $\eta$, and to preserve $\eta$ is to satisfy this one matrix equation; everything else — the group structure, the four components, the six parameters, the rapidity parametrisation — is read off from it.

The same congruence equation, with $\eta$ replaced by other forms, generates the whole zoo of classical groups: $R^{\mathsf T} I R = I$ gives the orthogonal group $O(n)$; $M^{\mathsf T} J M = J$ with $J$ the standard symplectic form gives the symplectic group $Sp(2n)$ of [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|Hamiltonian mechanics]]; the complex-linear maps preserving a Hermitian form give the unitary groups. The Lorentz group is the member of this family attached to the signature-$(1,3)$ symmetric form, and recognising it as such is what connects special relativity to the general theory of Lie groups and their representations.

---

# Examples / Corollaries

**Is an instance — a spatial rotation.** The matrix $\Lambda = \mathrm{diag}(1, R)$ built from a $3\times 3$ rotation matrix $R \in SO(3)$ (so $R^{\mathsf T}R = I$, $\det R = 1$) satisfies $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$: it leaves $t$ alone and preserves $x^2 + y^2 + z^2$, hence preserves $t^2 - x^2 - y^2 - z^2$. It has $\det\Lambda = +1$ and $\Lambda^0{}_0 = 1 \ge 1$, so it lies in $SO^+(1,3)$. Rotations are the "obvious" Lorentz transformations, the ones already present in Newtonian physics.

**Is an instance — a boost along $x$.** The matrix
$$
\Lambda[\varphi] = \begin{pmatrix} \cosh\varphi & \sinh\varphi & 0 & 0 \\ \sinh\varphi & \cosh\varphi & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}
$$
satisfies $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ because $\cosh^2\varphi - \sinh^2\varphi = 1$ (see [[Def - Boosts as Hyperbolic Rotations]]). It has $\det\Lambda = \cosh^2\varphi - \sinh^2\varphi = 1$ and $\Lambda^0{}_0 = \cosh\varphi \ge 1$, so it too lies in $SO^+(1,3)$. These are the genuinely relativistic elements, with $v = \tanh\varphi$ the velocity.

**Is an instance — parity, time reversal, spacetime inversion.** $P = \mathrm{diag}(1,-1,-1,-1)$ has $\det P = -1$, $P^0{}_0 = 1$: proper? No — $\det P = -1$ so it is *improper*, but orthochronous. $T = \mathrm{diag}(-1,1,1,1)$ has $\det T = -1$, $T^0{}_0 = -1$: improper and *antichronous*. $PT = -\,\mathrm{Id} = \mathrm{diag}(-1,-1,-1,-1)$ has $\det = +1$, $(PT)^0{}_0 = -1$: proper but antichronous. These three, together with the identity, are one representative of each of the four components, and they form the **Klein four-group** $\{\mathrm{Id}, P, T, PT\} \cong \mathbb{Z}/2 \times \mathbb{Z}/2$ — the discrete part of the Lorentz group.

**Is NOT an instance — a dilation.** The matrix $\Lambda = \lambda\,\mathrm{Id}$ with $\lambda \neq \pm 1$ satisfies $\Lambda^{\mathsf T}\eta\,\Lambda = \lambda^2\eta \neq \eta$. It preserves the *light cone* (it sends null vectors to null vectors) but not the interval, scaling every $\Delta s^2$ by $\lambda^2$. It is a *conformal* transformation of Minkowski space, not a Lorentz transformation, and the principle of relativity is exactly what excludes it: a dilation would change the rest mass of every particle.

**Is NOT an instance — a Galilean boost.** The Galilean transformation $\mathrm{diag\text{-}like}$ matrix sending $(t, x) \mapsto (t, x - vt)$, i.e.
$$
\begin{pmatrix} 1 & 0 \\ -v & 1 \end{pmatrix}
\quad\text{on } (t,x),
$$
does *not* satisfy $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$: it leaves $t$ alone (absolute time) and so cannot preserve $t^2 - x^2$. It is the $c \to \infty$ degeneration of a boost, and its failure to be Lorentz is the precise sense in which Newtonian mechanics violates the constancy of light.

**Corollary — the inverse is gotten by transposing with metric factors.** From $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ one gets $\Lambda^{-1} = \eta^{-1}\Lambda^{\mathsf T}\eta$, since $\eta^{-1} = \eta$. In index terms, $(\Lambda^{-1})^\mu{}_\nu = \eta^{\mu\alpha}\eta_{\nu\beta}\Lambda^\beta{}_\alpha = \Lambda_\nu{}^\mu$ — the inverse is the index-lowered-and-raised transpose. This is the relativistic analogue of "the inverse of a rotation is its transpose", deformed by the metric.

**Calibration check.** You should be able to: (1) verify $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ for the $x$-boost above by direct $2\times 2$ multiplication, watching $\cosh^2 - \sinh^2 = 1$ do the work; (2) compute $\det$ and $\Lambda^0{}_0$ for each of $P, T, PT$ and place each in its correct component; (3) explain in one sentence why $\lambda\,\mathrm{Id}$ with $\lambda > 1$ preserves the light cone but is not Lorentz.

---

# Unlocked by This

> [!tip] The Lie Algebra so(1,3) *(from the Lorentz Group as a Lie Group)*
> $SO^+(1,3)$ is a six-dimensional Lie group, so near the identity it is controlled by its **Lie algebra** $\mathfrak{so}(1,3)$ — the tangent space at $\mathrm{Id}$, spanned by three rotation generators $J_i$ and three boost generators $K_i$. Differentiating $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ at the identity gives the algebra's defining condition $\omega^{\mathsf T}\eta + \eta\,\omega = 0$ ($\eta$-antisymmetric matrices), and every $\Lambda \in SO^+(1,3)$ is $\exp(\omega)$ for such an $\omega$. The commutators $[J_i, J_j]$, $[J_i, K_j]$, $[K_i, K_j]$ are worked out in [[Special Relativity X — The Lorentz Group as a Lie Group]]; the last of these is what produces the **Thomas rotation**.

> [!tip] The Double Cover SL(2,C) *(from Spinors)*
> The restricted Lorentz group is not simply connected; its universal double cover is $SL(2,\mathbb{C})$, the group of $2\times 2$ complex matrices of determinant $1$, via the **spinor map** that sends a Hermitian $2\times 2$ matrix $X = x^\mu \sigma_\mu$ to $A X A^\dagger$. Two elements of $SL(2,\mathbb{C})$ map to each $\Lambda$, which is why a $2\pi$ rotation acts as $-1$ on spinors. This is the gateway to half-integer spin; see [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]].

> [!tip] The Poincaré Group and the Wigner Classification *(from Quantum Field Theory)*
> Adjoining the spacetime translations to the Lorentz group gives the **Poincaré group** $ISO^+(1,3) = SO^+(1,3) \ltimes \mathbb{R}^{1,3}$ ([[Def - The Poincaré Group]]), the full isometry group of Minkowski space. Its unitary irreducible representations are classified by Wigner using two **Casimir invariants** — $P^\mu P_\mu = m^2$ (the mass) and the square of the Pauli–Lubanski vector ($= -m^2 s(s+1)$, the spin). The upshot is that **mass and spin are the two labels of an elementary particle**, and they are exactly the invariants of the Poincaré group. See [[Special Relativity XII — Inertial Observers and the Poincaré Group]].
