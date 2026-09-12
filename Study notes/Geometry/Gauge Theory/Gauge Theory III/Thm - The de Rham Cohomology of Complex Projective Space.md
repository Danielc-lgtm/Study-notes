---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Complex Projective Space as a Quotient"
  - "Def - The Hopf Bundle"
  - "Thm - The Mayer-Vietoris Sequence"
  - "Thm - Homotopy Invariance of de Rham Cohomology"
  - "Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space"
  - "Def - de Rham Cohomology"
  - "Thm - Stokes' Theorem on Manifolds"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $N\ge 0$ is an integer and $\mathbb{CP}^N$ is [[Def - Complex Projective Space as a Quotient|complex projective space]], the quotient $\mathbb{CP}^N = (\mathbb{C}^{N+1}\setminus\{0\})/\mathbb{C}^\times$ of nonzero vectors by scalar multiplication; we write $[z] = [z_0 : \dots : z_N]$ for the line through $z = (z_0,\dots,z_N)$. It is a compact connected complex manifold of complex dimension $N$ (real dimension $2N$), carried onto itself by the affine charts $U_j = \{[z] : z_j\neq 0\}$ with holomorphic coordinates $(z_0/z_j,\dots,\widehat{z_j/z_j},\dots,z_N/z_j)\in\mathbb{C}^N$. We give $\mathbb{CP}^N$ its **complex orientation**: in any holomorphic coordinate $w = u + iv$ (one complex coordinate written as a pair of real ones), the pair $(\partial_u,\partial_v)$ is positively oriented, so that $du\wedge dv$ is a positive real $2$-form.

We write $z_j = x_j + i y_j$ for the real and imaginary parts of the complex coordinates on $\mathbb{C}^{N+1}$, so $|z|^2 = \sum_{j=0}^N (x_j^2 + y_j^2)$, and
$$S^{2N+1} = \{z\in\mathbb{C}^{N+1} : |z| = 1\}$$
is the unit sphere. The map $\pi : S^{2N+1}\to\mathbb{CP}^N$, $\pi(z) = [z]$, is the [[Def - The Hopf Bundle|Hopf bundle]], a principal $U(1)$-bundle for the right action $z\cdot\lambda = z\lambda$ ($\lambda\in U(1) = \{\lambda\in\mathbb{C} : |\lambda| = 1\}$). Its fundamental vector field, the generator of the action, is
$$v(z) = \left.\frac{d}{dt}\right|_{t=0} z\, e^{it} = iz = \sum_{j=0}^N\bigl(-y_j\,\partial_{x_j} + x_j\,\partial_{y_j}\bigr),$$
which is tangent to $S^{2N+1}$ and spans the vertical space $\ker d\pi_z$ at every $z$.

On $\mathbb{C}^{N+1}\cong\mathbb{R}^{2N+2}$ we single out the standard constant-coefficient $2$-form
$$\Sigma := \sum_{j=0}^N dx_j\wedge dy_j\in\Omega^2(\mathbb{C}^{N+1}),$$
the imaginary part of the Hermitian inner product $\langle z,w\rangle = \sum_j \overline{z_j}\,w_j$; it is closed and invariant under the unitary group $U(N+1)$. We write $\Sigma|_S$ for its restriction (pullback along the inclusion) to $S^{2N+1}$. The exterior derivative is $d$, the [[Def - Interior Product (Contraction with a Vector Field)|interior product]] (contraction) of a form $\omega$ with a vector field $X$ is $\iota_X\omega$, and $\Omega^k(P)$ denotes smooth $k$-forms. The [[Def - de Rham Cohomology|de Rham cohomology]] of a smooth manifold $M$ is $H^k_{dR}(M) = \ker(d\colon\Omega^k\to\Omega^{k+1})/\operatorname{im}(d\colon\Omega^{k-1}\to\Omega^k)$, a real vector space; $[\eta]$ denotes the class of a closed form $\eta$. All manifolds are smooth, Hausdorff, and second countable.

The standard inclusions are $\iota_N : \mathbb{CP}^N\hookrightarrow\mathbb{CP}^{N+1}$, $[z_0:\dots:z_N]\mapsto[z_0:\dots:z_N:0]$, and more generally $\iota_{m,N}:\mathbb{CP}^m\hookrightarrow\mathbb{CP}^N$ for $m\le N$ by padding with zeros; we abbreviate $\iota = \iota_{m,N}$ when $m$ and $N$ are clear. The wedge power of a class is written $[\omega_N]^k = [\omega_N^{\wedge k}]$, the class of the $k$-fold wedge.

> [!warning] Convention: the integral generator and de Rham
> Haydys works with the singular cohomology generator $a\in H^2(\mathbb{CP}^N;\mathbb{Z})$ normalised by his equation (73), so that $c_1(\mathcal{O}(-1)) = -a$. Under any comparison isomorphism between singular and de Rham cohomology, $a$ corresponds to the de Rham class $[\omega_N]$ produced below. **This series never constructs that comparison isomorphism** (it needs the de Rham theorem, whose full proof is flagged and not carried in this chapter); we work throughout with the de Rham class $[\omega_N]\in H^2_{dR}(\mathbb{CP}^N)$ directly, and every statement here is a statement about de Rham cohomology.

---

# Statement

> **Theorem (de Rham cohomology of complex projective space).** Fix $N\ge 0$.
>
> **(a) The Fubini–Study class.** There is a unique real closed $2$-form $\omega_N\in\Omega^2(\mathbb{CP}^N)$ with
> $$\pi^*\omega_N = \frac{1}{\pi}\,\Sigma|_S = \frac{1}{\pi}\sum_{j=0}^N dx_j\wedge dy_j\Big|_{S^{2N+1}}.$$
> It restricts compatibly along the standard inclusions, $\iota_N^*\,\omega_{N+1} = \omega_N$, and is normalised by
> $$\int_{\mathbb{CP}^1}\omega_1 = 1$$
> with respect to the complex orientation.
>
> **(b) The cohomology.** For $0\le k\le 2N$,
> $$H^k_{dR}(\mathbb{CP}^N)\;\cong\;\begin{cases}\mathbb{R}, & k\text{ even},\\[2pt] 0, & k\text{ odd},\end{cases}$$
> and $H^k_{dR}(\mathbb{CP}^N) = 0$ for $k > 2N$. For each even $k = 2m$ with $0\le m\le N$, the class $[\omega_N]^m$ is a generator of the one-dimensional space $H^{2m}_{dR}(\mathbb{CP}^N)$.
>
> **(c) Detection on the line.** The restriction $\iota_{1,N}^* : H^2_{dR}(\mathbb{CP}^N)\to H^2_{dR}(\mathbb{CP}^1)$ is an isomorphism, and a closed $2$-form $\eta$ on $\mathbb{CP}^N$ is exact if and only if $\int_{\mathbb{CP}^1}\eta = 0$ (the integral of $\iota_{1,N}^*\eta$ over the embedded line).

The form $\omega_N$ is the **Fubini–Study form**; its class $[\omega_N]$ is the de Rham first Chern class of the tautological bundle up to sign, made precise on the companion page [[Def - First Chern Class via the Classifying Map]].

> **Scope remark (not proved, not used).** The integral cohomology rings $H^\bullet(\mathbb{CP}^\infty;\mathbb{Z}) = \mathbb{Z}[a]$ and $H^\bullet(\mathbb{HP}^\infty;\mathbb{Z}) = \mathbb{Z}[b]$, which Haydys reads off from cell structures, are **not** computed in this series; neither is any integral cohomology of $\mathbb{HP}^N$. The quaternionic analogue of the present computation is never needed, because the quaternionic (second Chern) number of an $Sp(1) = SU(2)$-bundle is defined by the clutching construction rather than by pulling back a cohomology generator; see [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds]].

---

# Motivation

Complex projective space is the base of the Hopf bundle, the first nontrivial principal bundle in the subject, and it is the finite model of the classifying space for the circle group $U(1)$. Two questions about it must be answered before the classification of line bundles in §3.6 can even be stated. First, what is the receptacle $H^2_{dR}(\mathbb{CP}^N)$ in which the first Chern class of a line bundle will live, and how large is it? Second, is there a distinguished, computable generator of that receptacle, so that a numerical invariant — a single real number — can be attached to each bundle? The theorem answers both at once: the receptacle is one-dimensional, and it has a canonical generator, the Fubini–Study class $[\omega_N]$, pinned down by a normalisation that can be checked by a single integral over the projective line.

The reason this cannot be waved away is that the entire strength of the $U(1)$-classification rests on part (c). We will show later that every line bundle over a compact manifold is pulled back from $\mathbb{CP}^N$ by a classifying map, and that its first Chern class is the pullback of $[\omega_N]$. For this to be a complete invariant on a surface, two facts are indispensable: that $H^2_{dR}(\mathbb{CP}^N)$ is exactly one-dimensional (so a single number captures the whole class), and that the class is faithfully seen by its integral over the line $\mathbb{CP}^1\subset\mathbb{CP}^N$ (so the number is computable by an honest integral, not an abstract pairing). Without the one-dimensionality there could be several independent invariants; without part (c) the invariant would be uncomputable. The computation is therefore not decoration: it is the hinge on which "a line bundle over a surface is measured by one integer" turns.

There is also a structural payoff worth naming in advance. The cohomology comes out as a truncated polynomial algebra, $H^\bullet_{dR}(\mathbb{CP}^N) = \mathbb{R}[\,[\omega_N]\,]/([\omega_N]^{N+1})$ additively (every even class up to degree $2N$ is a power of the degree-two generator, and the top power $[\omega_N]^{N+1}$ has nowhere to live). This is the shadow of the cell structure of projective space — one cell in each even dimension — seen through de Rham theory, and it is the reason $\mathbb{CP}^N$ behaves like a "necklace" of spheres $S^2, S^4,\dots, S^{2N}$ that the Mayer–Vietoris induction below strings together one bead at a time.

The reader is assumed to know the definition of de Rham cohomology, the Mayer–Vietoris sequence, homotopy invariance, Stokes' theorem on manifolds, and the construction of the Hopf bundle and of complex projective space as a quotient; all are recalled at the point of use.

---

# Sources and Targets

**Sources (Input Broadening).** The theorem's hypothesis is simply "the manifold is $\mathbb{CP}^N$", so the useful sources are the disguises under which projective space, or the pattern of its proof, appears.

The first disguised source is **a smooth manifold assembled from one cell in each even dimension, or more concretely a space that is an $S^{2N}$-bundle-like extension of $\mathbb{CP}^{N-1}$**. The proof never uses that we started with projective space until the very last step; what it uses is the decomposition $\mathbb{CP}^N = U\cup V$ with $U$ contractible, $V\simeq\mathbb{CP}^{N-1}$, and $U\cap V\simeq S^{2N-1}$. Any manifold admitting such a Mayer–Vietoris triple has the same cohomology recursion. The non-obvious bridge is recognising that "remove a hyperplane" and "remove the complementary point" produce, respectively, an affine chart and a retract onto the previous stage. *Example problem:* compute the de Rham cohomology of the total space of the tautological $\mathbb{CP}^{N-1}$-bundle inside $\mathbb{CP}^N\times\mathbb{CP}^N$ near the diagonal by imitating the triple.

The second disguised source is **a compact complex manifold carrying a closed positive $(1,1)$-form (a Kähler manifold)**. The Fubini–Study form is the model of such a form, and the generator argument in part (b) uses nothing about $\mathbb{CP}^N$ beyond that its Kähler form $\omega$ is nondegenerate, so its top power $\omega^n$ is a volume form and integrates to a nonzero number. The bridge $B\Rightarrow A$ is: a nondegenerate closed $2$-form on a compact oriented $2n$-manifold forces $[\omega]^n\neq 0$, hence all its powers are nonzero classes. *Example problem:* show that a compact symplectic $2n$-manifold has $H^{2k}_{dR}\neq 0$ for every $0\le k\le n$, by the same nowhere-vanishing-top-power argument used here for $\mathbb{CP}^m$.

The third disguised source is **a principal $U(1)$-bundle whose total space is a sphere**. Part (a) is really a statement about the Hopf bundle: the horizontal, invariant $2$-form on the sphere descends. Whenever one has a circle bundle $P\to M$ with a chosen connection, the curvature is exactly a basic invariant $2$-form on $P$, and it descends to a distinguished class on $M$ by the same basic-forms theorem. The bridge is recognising the standard symplectic form on $\mathbb{C}^{N+1}$, restricted to the sphere, as (a multiple of) the curvature of the natural connection. *Example problem:* given any Hermitian line bundle with connection over a surface, show its curvature descends and integrates to a topological integer, mirroring $\int_{\mathbb{CP}^1}\omega_1 = 1$.

**Targets (Output Amplification).** The theorem is a supplier of receptacles and generators.

Combine part (b) with **the classifying-map theorem** [[Thm - Line Bundles over Compact Manifolds are Pulled Back from Projective Space]]. Every line bundle $L\to M$ is $f^*\mathcal{O}(-1)$ for some $f : M\to\mathbb{CP}^N$; the first Chern class is then defined as $-f^*[\omega_N]\in H^2_{dR}(M)$. The extra ingredient is the one-dimensionality of $H^2_{dR}(\mathbb{CP}^N)$, which guarantees the pulled-back class is well-defined independently of $N$ (using $\iota_N^*\omega_{N+1} = \omega_N$). The payoff is the de Rham first Chern class, the whole content of [[Def - First Chern Class via the Classifying Map]].

Combine part (c) with **Stokes' theorem and the degree of a map**. Because a closed $2$-form is exact if and only if its integral over $\mathbb{CP}^1$ vanishes, the number $\int_{\mathbb{CP}^1}\eta$ is a complete linear invariant of the class $[\eta]$. Fed the curvature of a connection, this becomes the statement that the Chern number is computed by an integral; fed a classifying map, it becomes the statement that homotopic maps give equal Chern classes. The payoff, worked out in chapter VI, is the identity $\deg L = \int_\Sigma c_1(L)$ on a surface.

Combine part (b) with **the Künneth-style geometry of products**. Since $H^\bullet_{dR}(\mathbb{CP}^N)$ is generated by one class in degree two, the cohomology of $\mathbb{CP}^N$ is completely transparent, and products such as $\mathbb{CP}^N\times\Sigma$ or $\mathbb{CP}^N\times\mathbb{CP}^M$ become computable. The extra ingredient is a product formula; the payoff includes the computation used in [[Thm - The Hopf Bundle is Nontrivial]], where $H^1_{dR}(\mathbb{CP}^n\times S^1)\neq 0$ distinguishes the sphere $S^{2n+1}$ from the product $\mathbb{CP}^n\times S^1$.

---

# Why Is It True

Picture $\mathbb{CP}^N$ built one dimension at a time. Inside it sits the previous stage $\mathbb{CP}^{N-1}$ as a hyperplane, and its complement is exactly one affine chart $\cong\mathbb{C}^N$, which is contractible and so has no cohomology above degree zero. Thicken the hyperplane slightly to an open set $V$ that deformation-retracts onto $\mathbb{CP}^{N-1}$, and thicken the chart to an open set $U\cong\mathbb{C}^N$; their overlap is $\mathbb{C}^N$ minus a point, which retracts onto the sphere $S^{2N-1}$. Mayer–Vietoris now glues the cohomology of $\mathbb{CP}^N$ from that of $\mathbb{CP}^{N-1}$ and the sphere. Because a sphere $S^{2N-1}$ only contributes cohomology in degrees $0$ and $2N-1$, the gluing is inert in every middle degree — there $\mathbb{CP}^N$ simply inherits the cohomology of $\mathbb{CP}^{N-1}$ — and produces exactly one new class, in the top degree $2N$.

> **The one-line mechanism:** each stage $\mathbb{CP}^N$ is the previous stage with one $2N$-cell glued on across an odd sphere, and an odd sphere is cohomologically silent except at its top, so each stage adds exactly one new even-degree class and copies everything below.

That accounts for the additive answer: a single $\mathbb{R}$ in every even degree up to $2N$. The generator statement is a separate, geometric fact. The Fubini–Study form $\omega_N$ is nondegenerate — it is the reduction of the standard symplectic form on $\mathbb{C}^{N+1}$ — so on the sub-projective-space $\mathbb{CP}^m$ its top power $\omega_m^{\wedge m}$ is a nowhere-vanishing top-degree form, hence a volume form, hence has nonzero integral. Since $\omega_N$ restricts to $\omega_m$ on $\mathbb{CP}^m\subset\mathbb{CP}^N$, the integral of $\omega_N^{\wedge m}$ over $\mathbb{CP}^m$ is that same nonzero number, so $[\omega_N]^m$ cannot be zero. In a one-dimensional space, "nonzero" is "generator", and part (b) is complete. Part (c) is then bookkeeping: the class is detected by integrating its restriction to the line, because the whole space is spanned by $[\omega_N]$ and $\int_{\mathbb{CP}^1}\omega_N = 1$.

---

# What Makes This Hard

The additive computation is routine once the cover is set up, but two steps carry the actual weight. The first is proving that the classes $[\omega_N]^m$ are *nonzero*, not merely that the spaces are one-dimensional: Mayer–Vietoris tells you the dimension but hands you no named generator, and the connecting homomorphism provides no visible reason to send anything to a power of $\omega_N$. The device that closes this gap is to integrate over the sub-projective-space $\mathbb{CP}^m$ and use nondegeneracy of the Fubini–Study form; missing it leaves the generator claim unproved even though the dimension count is finished. The second subtlety is the normalisation constant. The factor $1/\pi$ in part (a) is exactly what makes $\int_{\mathbb{CP}^1}\omega_1 = 1$ with the complex orientation; getting it wrong (a common slip is a stray factor of $2$ or $2\pi$, or the opposite orientation) silently corrupts every Chern number downstream. The safe route is the explicit Stokes computation in an affine chart, done once and checked against the source's independent Example 51.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Build the distinguished form by descending the standard symplectic form of $\mathbb{C}^{N+1}$ along the Hopf bundle (it is basic and invariant), fixing its constant by one Stokes computation. Compute the cohomology by induction on $N$ using the Mayer–Vietoris triple (affine chart, retract onto the previous stage, sphere overlap), with the cohomology of spheres as the only external input. Finally show the powers of the class are nonzero by integrating over sub-projective-spaces, using nondegeneracy of the descended form.

**Subgoal decomposition:**

1. **Cohomology of spheres.** Establish $H^k_{dR}(S^n) = \mathbb{R}$ for $k\in\{0,n\}$ and $0$ otherwise ($n\ge 1$).
   - *Hint:* Two contractible charts with overlap $\simeq S^{n-1}$; Mayer–Vietoris gives $H^k(S^n)\cong H^{k-1}(S^{n-1})$ for $k\ge 2$.
   - *Why needed:* It is the overlap term $U\cap V\simeq S^{2N-1}$ in the projective-space induction.

2. **Descent of $\Sigma|_S$.** Show $\Sigma|_S$ is basic and $U(1)$-invariant, so a unique real closed $\omega_N$ exists with $\pi^*\omega_N = \tfrac1\pi\Sigma|_S$, and $\iota_N^*\omega_{N+1} = \omega_N$.
   - *Hint:* Contract $\Sigma$ with the generator $v = iz$; the result is $-\tfrac12 d|z|^2$, zero on the sphere.
   - *Why needed:* It builds the named generator and its restriction compatibility.

3. **Normalisation.** Compute $\int_{\mathbb{CP}^1}\omega_1 = 1$.
   - *Hint:* Pull $\tfrac1\pi\Sigma|_S$ back by an explicit local section over the affine chart; it is exact there, and Stokes over expanding discs gives $1$.
   - *Why needed:* Pins the constant and drives part (c).

4. **The Mayer–Vietoris cover.** Exhibit $U\cong\mathbb{C}^N$, $V\simeq\mathbb{CP}^{N-1}$, $U\cap V\simeq S^{2N-1}$ with explicit maps.
   - *Hint:* $U = \{z_N\neq 0\}$; $V = \mathbb{CP}^N\setminus\{[0:\dots:0:1]\}$ retracts by $[z:w]\mapsto[z:tw]$; the overlap is $\mathbb{C}^N\setminus\{0\}$.
   - *Why needed:* It is the engine of the induction.

5. **The additive computation.** Run the induction, base case $\mathbb{CP}^1\cong S^2$.
   - *Hint:* The odd sphere is silent except at its top; middle degrees inherit $\mathbb{CP}^{N-1}$, the top degree gains one $\mathbb{R}$.
   - *Why needed:* It is part (b) minus the generators.

6. **Nonvanishing of the powers.** Show $\omega_m^{\wedge m}$ is nowhere-vanishing and integrate over $\mathbb{CP}^m$.
   - *Hint:* $\omega_m$ is nondegenerate at one point and $U(m+1)$-invariant; transport the nonvanishing everywhere.
   - *Why needed:* It upgrades "one-dimensional" to "generated by $[\omega_N]^m$", and gives part (c).

---

# Lemma Decomposition

> [!note]- Lemma 1: de Rham cohomology of spheres
> **Statement:** For every integer $n\ge 1$,
> $$H^k_{dR}(S^n)\cong\begin{cases}\mathbb{R}, & k = 0\text{ or }k = n,\\ 0, & \text{otherwise}.\end{cases}$$
>
> **Hint:** Cover $S^n$ by the complements of the two poles; each is diffeomorphic to $\mathbb{R}^n$, and their overlap deformation-retracts onto the equatorial $S^{n-1}$. Mayer–Vietoris then reduces degree and dimension together.
>
> **Why needed:** The Mayer–Vietoris triple for $\mathbb{CP}^N$ has overlap $U\cap V\simeq S^{2N-1}$; the induction on projective spaces cannot start without the cohomology of these odd spheres.
>
> > [!note]- Full proof
> > We argue by induction on $n$. Throughout we use, for a smooth manifold $M$, that $H^0_{dR}(M)\cong\mathbb{R}^{c}$ where $c$ is the number of connected components (a closed $0$-form is a locally constant function), and we use the [[Thm - Homotopy Invariance of de Rham Cohomology|homotopy invariance of de Rham cohomology]] — homotopy-equivalent manifolds have isomorphic de Rham cohomology — together with [[Ex - The de Rham Cohomology of R^n is Trivial in Positive Degrees|the vanishing of the positive de Rham cohomology of Euclidean space]]: $H^0_{dR}(\mathbb{R}^n) = \mathbb{R}$ and $H^k_{dR}(\mathbb{R}^n) = 0$ for $k\ge 1$.
> >
> > **Base case $n = 1$.** This is [[Ex - The de Rham Cohomology of S^1 is R|the computation for the circle]], recorded there in full: $H^0_{dR}(S^1) = H^1_{dR}(S^1) = \mathbb{R}$ and all other degrees vanish.
> >
> > **Step 0 — the cover.** Fix $n\ge 2$ and write $\mathrm{N} = (0,\dots,0,1)$ and $\mathrm{S} = (0,\dots,0,-1)$ for the north and south poles of $S^n\subset\mathbb{R}^{n+1}$. Set $U = S^n\setminus\{\mathrm{N}\}$ and $V = S^n\setminus\{\mathrm{S}\}$. Stereographic projection from a pole is a diffeomorphism onto $\mathbb{R}^n$, so $U\cong\mathbb{R}^n$ and $V\cong\mathbb{R}^n$; both are connected, and by homotopy invariance $H^0_{dR}(U) = H^0_{dR}(V) = \mathbb{R}$ and $H^k_{dR}(U) = H^k_{dR}(V) = 0$ for $k\ge 1$. The overlap $U\cap V = S^n\setminus\{\mathrm{N},\mathrm{S}\}$ deformation-retracts onto the equator $\{x_{n+1} = 0\}\cap S^n = S^{n-1}$ by the smooth homotopy $H(x,t) = \tfrac{(x_1,\dots,x_n,(1-t)x_{n+1})}{|(x_1,\dots,x_n,(1-t)x_{n+1})|}$ (well-defined because $(x_1,\dots,x_n)\neq 0$ on $U\cap V$), so $H^k_{dR}(U\cap V)\cong H^k_{dR}(S^{n-1})$ by homotopy invariance.
> >
> > **Step 1 — the Mayer–Vietoris sequence.** By [[Thm - The Mayer-Vietoris Sequence|the Mayer–Vietoris theorem]] — for open $U,V$ with $U\cup V = M$ there is a long exact sequence $\dots\to H^{k-1}_{dR}(U\cap V)\xrightarrow{\delta} H^k_{dR}(M)\xrightarrow{\beta} H^k_{dR}(U)\oplus H^k_{dR}(V)\xrightarrow{\alpha} H^k_{dR}(U\cap V)\to\dots$, with $\beta$ the difference of restrictions and $\alpha$ likewise — we read off the cohomology of $S^n = U\cup V$.
> >
> > **Step 2 — degrees $0$ and $1$.** The sphere $S^n$ ($n\ge 1$) is connected, so $H^0_{dR}(S^n) = \mathbb{R}$. For degree one, since $n\ge 2$ the equator $S^{n-1}$ is connected, so $H^0_{dR}(U\cap V) = \mathbb{R}$; the map $\alpha : H^0_{dR}(U)\oplus H^0_{dR}(V) = \mathbb{R}^2\to\mathbb{R} = H^0_{dR}(U\cap V)$ sends $(a,b)$ to $a - b$ (difference of constants), which is surjective. By exactness $\operatorname{im}\alpha = \ker(\delta : H^0_{dR}(U\cap V)\to H^1_{dR}(S^n))$, so $\delta = 0$ (its kernel is everything), hence $\operatorname{im}\delta = 0 = \ker\beta$ and $\beta : H^1_{dR}(S^n)\to H^1_{dR}(U)\oplus H^1_{dR}(V) = 0$ is injective; therefore $H^1_{dR}(S^n) = 0$.
> >
> > **Step 3 — degrees $k\ge 2$.** For $k\ge 2$ we have $H^{k-1}_{dR}(U)\oplus H^{k-1}_{dR}(V) = 0$ (as $k-1\ge 1$) and $H^k_{dR}(U)\oplus H^k_{dR}(V) = 0$. The Mayer–Vietoris segment
> > $$\underbrace{H^{k-1}_{dR}(U)\oplus H^{k-1}_{dR}(V)}_{=\,0}\xrightarrow{\alpha} H^{k-1}_{dR}(U\cap V)\xrightarrow{\delta} H^k_{dR}(S^n)\xrightarrow{\beta}\underbrace{H^k_{dR}(U)\oplus H^k_{dR}(V)}_{=\,0}$$
> > shows, by exactness, that $\delta$ is injective (its kernel is $\operatorname{im}\alpha = 0$) and surjective (its cokernel injects into $H^k_{dR}(U)\oplus H^k_{dR}(V) = 0$). Hence $\delta$ is an isomorphism and $H^k_{dR}(S^n)\cong H^{k-1}_{dR}(U\cap V)\cong H^{k-1}_{dR}(S^{n-1})$.
> >
> > **Step 4 — assemble.** Combining Steps 2 and 3 with the inductive hypothesis for $S^{n-1}$: $H^0_{dR}(S^n) = \mathbb{R}$, $H^1_{dR}(S^n) = 0$, and for $k\ge 2$, $H^k_{dR}(S^n)\cong H^{k-1}_{dR}(S^{n-1})$, which by hypothesis is $\mathbb{R}$ exactly when $k-1 = n-1$, that is $k = n$, and $0$ otherwise. Therefore $H^k_{dR}(S^n) = \mathbb{R}$ for $k\in\{0,n\}$ and $0$ otherwise. This closes the induction. $\blacksquare$

> [!note]- Lemma 2: the standard symplectic form descends to the Fubini–Study form
> **Statement:** The restriction $\Sigma|_S\in\Omega^2(S^{2N+1})$ vanishes on vertical vectors (is basic) and is invariant under the right $U(1)$-action. Consequently there is a unique $2$-form $\omega_N\in\Omega^2(\mathbb{CP}^N)$ with $\pi^*\omega_N = \tfrac1\pi\Sigma|_S$; it is real and closed, and $\iota_N^*\,\omega_{N+1} = \omega_N$.
>
> **Hint:** Contract $\Sigma$ with the fundamental field $v = iz$; the answer is $-\tfrac12 d|z|^2$, which restricts to zero on the sphere. Invariance is unitarity of $z\mapsto z\lambda$. Then quote the basic-forms theorem for the trivial representation.
>
> **Why needed:** It manufactures the generator $\omega_N$, gives closedness, and provides the compatibility $\iota_N^*\omega_{N+1} = \omega_N$ used to make the first Chern class independent of $N$ and to detect classes on sub-projective-spaces.
>
> > [!note]- Full proof
> > **Step 0 — the vertical space.** By construction of the [[Def - The Hopf Bundle|Hopf bundle]] the fibres of $\pi$ are the $U(1)$-orbits, so the vertical space $\ker d\pi_z$ at $z\in S^{2N+1}$ is one-dimensional and spanned by the fundamental vector field $v(z) = iz = \sum_j(-y_j\,\partial_{x_j} + x_j\,\partial_{y_j})$, the velocity of the orbit $t\mapsto z e^{it}$. This field is tangent to $S^{2N+1}$ because the flow $z\mapsto z e^{it}$ preserves $|z|$. A $2$-form on $S^{2N+1}$ is **basic** (vanishes on vertical vectors) precisely when its contraction with $v$ is zero, the vertical space being spanned by $v$.
> >
> > **Step 1 — $\Sigma|_S$ is basic.** Contract the ambient form $\Sigma = \sum_j dx_j\wedge dy_j$ with $v$. For each $j$, using $dx_j(v) = -y_j$ and $dy_j(v) = x_j$,
> > $$\iota_v(dx_j\wedge dy_j) = dx_j(v)\,dy_j - dy_j(v)\,dx_j = -y_j\,dy_j - x_j\,dx_j\qquad(\text{definition of }\iota_v\text{ on a }2\text{-form}).$$
> > Summing over $j$,
> > $$\iota_v\Sigma = -\sum_{j=0}^N\bigl(x_j\,dx_j + y_j\,dy_j\bigr) = -\tfrac12\,d\!\left(\sum_{j=0}^N (x_j^2 + y_j^2)\right) = -\tfrac12\,d|z|^2\qquad(\text{since } x\,dx = \tfrac12 d(x^2)).$$
> > Restricting to $S^{2N+1}$, and using that $v$ is tangent to the sphere so that contraction commutes with restriction, $\iota_v(\Sigma|_S) = (\iota_v\Sigma)|_S = -\tfrac12\,d\bigl(|z|^2|_S\bigr) = -\tfrac12\,d(1) = 0$ (because $|z|^2 \equiv 1$ on $S^{2N+1}$). Hence $\Sigma|_S$ is basic.
> >
> > **Step 2 — $\Sigma|_S$ is $U(1)$-invariant.** The right action $R_\lambda(z) = z\lambda$ is the restriction to $S^{2N+1}$ of the complex-linear map $z\mapsto\lambda z$ on $\mathbb{C}^{N+1}$, which is unitary ($|\lambda| = 1$) and therefore preserves the Hermitian inner product $\langle\cdot,\cdot\rangle$ and hence its imaginary part $\Sigma$: $R_\lambda^*\Sigma = \Sigma$ on $\mathbb{C}^{N+1}$. Restricting, $R_\lambda^*(\Sigma|_S) = \Sigma|_S$. So $\Sigma|_S$ is invariant, that is, basic and $U(1)$-invariant with respect to the trivial representation of $U(1)$ on $\mathbb{R}$.
> >
> > **Step 3 — descent.** By [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|the basic-forms theorem]] — for a principal $G$-bundle $\pi : P\to M$ and the trivial representation on $\mathbb{R}$, pullback $\pi^* : \Omega^q(M)\to\Omega^q_{\mathrm{bas}}(P)^G$ is a bijection onto the basic $G$-invariant $q$-forms — there is a unique $\tilde\omega_N\in\Omega^2(\mathbb{CP}^N)$ with $\pi^*\tilde\omega_N = \Sigma|_S$. Set $\omega_N := \tfrac1\pi\tilde\omega_N$; then $\pi^*\omega_N = \tfrac1\pi\Sigma|_S$, and $\omega_N$ is unique with this property because $\pi^*$ is injective (part of the cited bijection).
> >
> > **Step 4 — real and closed.** The form $\tfrac1\pi\Sigma|_S$ has real coefficients, and $\pi^*$ carries real forms to real forms and is injective, so $\omega_N$ is real. For closedness, $\pi^*(d\omega_N) = d(\pi^*\omega_N) = \tfrac1\pi\,d(\Sigma|_S) = \tfrac1\pi\,(d\Sigma)|_S = 0$, because $\Sigma$ has constant coefficients so $d\Sigma = 0$, and $d$ commutes with the restriction (pullback) to $S^{2N+1}$. Since $\pi^*$ is injective, $d\omega_N = 0$.
> >
> > **Step 5 — compatibility with inclusions.** Let $\tilde\iota : S^{2N+1}\hookrightarrow S^{2N+3}$, $z\mapsto(z,0)$, be the sphere-level inclusion covering $\iota_N$, so $\pi_{N+1}\circ\tilde\iota = \iota_N\circ\pi_N$ (both send $z$ to $[z:0]$). Then
> > $$\pi_N^*\bigl(\iota_N^*\omega_{N+1}\bigr) = (\iota_N\circ\pi_N)^*\omega_{N+1} = (\pi_{N+1}\circ\tilde\iota)^*\omega_{N+1} = \tilde\iota^*\bigl(\pi_{N+1}^*\omega_{N+1}\bigr) = \tilde\iota^*\!\left(\tfrac1\pi\sum_{j=0}^{N+1} dx_j\wedge dy_j\Big|_{S^{2N+3}}\right).$$
> > On the image of $\tilde\iota$ the last coordinate is identically zero, so $\tilde\iota^*(dx_{N+1}) = \tilde\iota^*(dy_{N+1}) = 0$, while $\tilde\iota^*(dx_j\wedge dy_j) = dx_j\wedge dy_j|_{S^{2N+1}}$ for $j\le N$. Hence the right-hand side equals $\tfrac1\pi\sum_{j=0}^N dx_j\wedge dy_j|_{S^{2N+1}} = \pi_N^*\omega_N$. Injectivity of $\pi_N^*$ gives $\iota_N^*\omega_{N+1} = \omega_N$. $\blacksquare$

> [!note]- Lemma 3: the normalisation $\int_{\mathbb{CP}^1}\omega_1 = 1$
> **Statement:** With the complex orientation of $\mathbb{CP}^1$, $\displaystyle\int_{\mathbb{CP}^1}\omega_1 = 1$.
>
> **Hint:** Over the affine chart $U_0$ the form $\omega_1$ is exact, equal to $\tfrac{1}{2\pi}d(s^*\lambda)$ for the potential $\lambda = \sum_j(x_j\,dy_j - y_j\,dx_j)$ and the standard local section $s$. Integrate by Stokes over discs of radius $R$ and let $R\to\infty$.
>
> **Why needed:** It fixes the constant $1/\pi$ and is the seed of part (c): the integral of any closed $2$-form over $\mathbb{CP}^1$ reads off its $\omega_1$-coefficient.
>
> > [!note]- Full proof
> > **Step 0 — a potential on $\mathbb{C}^{N+1}$.** Let $\lambda = \sum_{j=0}^N(x_j\,dy_j - y_j\,dx_j)\in\Omega^1(\mathbb{C}^{N+1})$. Then $d\lambda = \sum_j(dx_j\wedge dy_j - dy_j\wedge dx_j) = 2\sum_j dx_j\wedge dy_j = 2\Sigma$, so $\Sigma = \tfrac12 d\lambda$ and $\Sigma|_S = \tfrac12 d(\lambda|_S)$.
> >
> > **Step 1 — the local section.** Work on $\mathbb{CP}^1$ with the affine chart $U_0 = \{[z_0:z_1] : z_0\neq 0\}$ and complex coordinate $w = z_1/z_0 = u + iv\in\mathbb{C}$; this is a holomorphic coordinate, so the complex orientation of $\mathbb{CP}^1$ on $U_0$ is the one for which $du\wedge dv$ is positive. The map
> > $$s : U_0\to S^3,\qquad s([1:w]) = \frac{1}{\rho}(1, w),\qquad \rho = \rho(w) = \sqrt{1 + |w|^2} = \sqrt{1 + u^2 + v^2},$$
> > is a smooth local section of the Hopf bundle, $\pi\circ s = \mathrm{id}_{U_0}$. Because $\pi\circ s = \mathrm{id}$, on $U_0$ we have $\omega_1 = s^*(\pi^*\omega_1) = \tfrac1\pi s^*(\Sigma|_S) = \tfrac{1}{2\pi}\,s^*\bigl(d(\lambda|_S)\bigr) = \tfrac{1}{2\pi}\,d\bigl(s^*\lambda\bigr)$, using Step 0 and that pullback commutes with $d$.
> >
> > **Step 2 — the potential in the chart.** In the coordinates of $s$ we have $x_0 = 1/\rho$, $y_0 = 0$, $x_1 = u/\rho$, $y_1 = v/\rho$. The $j = 0$ contribution to $\lambda$ is $x_0\,dy_0 - y_0\,dx_0 = 0$ (both $y_0 = 0$ and $dy_0 = 0$). For $j = 1$, with $d(v/\rho) = \tfrac{dv}{\rho} - \tfrac{v\,d\rho}{\rho^2}$ and $d(u/\rho) = \tfrac{du}{\rho} - \tfrac{u\,d\rho}{\rho^2}$,
> > $$x_1\,dy_1 - y_1\,dx_1 = \frac{u}{\rho}\!\left(\frac{dv}{\rho} - \frac{v\,d\rho}{\rho^2}\right) - \frac{v}{\rho}\!\left(\frac{du}{\rho} - \frac{u\,d\rho}{\rho^2}\right) = \frac{u\,dv - v\,du}{\rho^2}\qquad(\text{the two } \tfrac{uv\,d\rho}{\rho^3}\text{ terms cancel}).$$
> > Hence $s^*\lambda = \dfrac{u\,dv - v\,du}{1 + u^2 + v^2}$ on $U_0\cong\mathbb{R}^2$.
> >
> > **Step 3 — Stokes over expanding discs.** The complement $\mathbb{CP}^1\setminus U_0 = \{[0:1]\}$ is a single point, of measure zero, so $\int_{\mathbb{CP}^1}\omega_1 = \int_{U_0}\omega_1$; as $\omega_1$ is smooth on the compact manifold $\mathbb{CP}^1$ this integral is finite and equals $\lim_{R\to\infty}\int_{D_R}\omega_1$ for the closed discs $D_R = \{u^2 + v^2\le R^2\}$ exhausting $U_0$ (this is dominated convergence, the dominating function being $|\omega_1|$ in the Riemannian volume of $\mathbb{CP}^1$, which is integrable). On each $D_R$, oriented by $du\wedge dv$ (the complex orientation), $\omega_1 = \tfrac{1}{2\pi}d(s^*\lambda)$ is exact, so by [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] — $\int_D d\beta = \int_{\partial D}\beta$ for a compact oriented manifold with boundary, $\partial D$ carrying the induced (outward-normal-first) orientation —
> > $$\int_{D_R}\omega_1 = \frac{1}{2\pi}\int_{\partial D_R} s^*\lambda = \frac{1}{2\pi}\oint_{u^2+v^2 = R^2}\frac{u\,dv - v\,du}{1 + u^2 + v^2}.$$
> > Parametrising $\partial D_R$ counterclockwise (the induced orientation for $du\wedge dv$) by $u = R\cos\theta$, $v = R\sin\theta$, $\theta\in[0,2\pi]$, one has $u\,dv - v\,du = R^2\,d\theta$ and $1 + u^2 + v^2 = 1 + R^2$, so
> > $$\int_{D_R}\omega_1 = \frac{1}{2\pi}\cdot\frac{R^2}{1 + R^2}\int_0^{2\pi}d\theta = \frac{R^2}{1 + R^2}.$$
> >
> > **Step 4 — the limit.** Letting $R\to\infty$, $\int_{\mathbb{CP}^1}\omega_1 = \lim_{R\to\infty}\tfrac{R^2}{1 + R^2} = 1$. (As a consistency check against the source: Haydys' Example 51 computes $\int_{\mathbb{CP}^1}F_a = 2\pi i$ for the Hopf connection with $\pi^*F_a = 2i\,\Sigma|_S$; since $\pi^*F_a = 2\pi i\cdot\tfrac1\pi\Sigma|_S = \pi^*(2\pi i\,\omega_1)$ and $\pi^*$ is injective, $F_a = 2\pi i\,\omega_1$, whence $\int_{\mathbb{CP}^1}F_a = 2\pi i\int_{\mathbb{CP}^1}\omega_1 = 2\pi i$, in agreement.) $\blacksquare$

> [!note]- Lemma 4: the Mayer–Vietoris cover of $\mathbb{CP}^N$
> **Statement:** For $N\ge 1$ put $U = \{[z]\in\mathbb{CP}^N : z_N\neq 0\}$ and $V = \mathbb{CP}^N\setminus\{p_\infty\}$ with $p_\infty = [0:\dots:0:1]$. Then $U$ and $V$ are open with $U\cup V = \mathbb{CP}^N$; $U\cong\mathbb{C}^N$ is contractible; $V$ deformation-retracts onto the hyperplane $\mathbb{CP}^{N-1} = \{[z] : z_N = 0\}$; and $U\cap V\cong\mathbb{C}^N\setminus\{0\}$ deformation-retracts onto $S^{2N-1}$.
>
> **Hint:** $U$ is an affine chart; the retraction of $V$ is $[z:w]\mapsto[z:tw]$ scaling the last coordinate; in the chart of $U$ the removed point $p_\infty$ is the origin.
>
> **Why needed:** These three homotopy types feed the Mayer–Vietoris induction: $U$ is silent, $V$ carries the previous stage, and the overlap carries an odd sphere.
>
> > [!note]- Full proof
> > **Step 0 — the sets are open and cover.** The functions $[z]\mapsto z_N$ and $[z]\mapsto(z_0,\dots,z_{N-1})$ are only defined up to scale, but their vanishing loci are well-defined; $U = \{z_N\neq 0\}$ and $V = \{[z]\neq p_\infty\}$ are complements of the closed sets $\{z_N = 0\}$ and $\{p_\infty\}$, hence open. A point $[z]$ lies outside $U\cup V$ only if $z_N = 0$ and $[z] = p_\infty$, impossible since $p_\infty$ has $z_N = 1\neq 0$. So $U\cup V = \mathbb{CP}^N$.
> >
> > **Step 1 — $U$ is a contractible chart.** The affine chart map $\varphi : U\to\mathbb{C}^N$, $\varphi([z]) = (z_0/z_N,\dots,z_{N-1}/z_N)$, is a diffeomorphism (this is one of the standard holomorphic charts of $\mathbb{CP}^N$). Since $\mathbb{C}^N\cong\mathbb{R}^{2N}$ is star-shaped hence contractible, $U$ is contractible; by homotopy invariance and the vanishing of the positive de Rham cohomology of $\mathbb{R}^{2N}$, $H^0_{dR}(U) = \mathbb{R}$ and $H^k_{dR}(U) = 0$ for $k\ge 1$.
> >
> > **Step 2 — $V$ retracts onto $\mathbb{CP}^{N-1}$.** Write a point of $V$ as $[z : w]$ with $z = (z_0,\dots,z_{N-1})$ and $w = z_N$. Excluding $p_\infty = [0 : 1]$ means $z\neq 0$. Define $r : V\times[0,1]\to V$ by $r_t([z:w]) = [z : t w]$. For each $t$ the point $[z : tw]$ is legitimate because its first block $z$ is nonzero, so it is not the zero vector; $r$ is smooth in homogeneous coordinates (it scales one coordinate). We have $r_1 = \mathrm{id}_V$ and $r_0([z:w]) = [z : 0]\in\mathbb{CP}^{N-1}$, and $r_t$ fixes $\mathbb{CP}^{N-1} = \{w = 0\}$ pointwise. Thus the inclusion $j : \mathbb{CP}^{N-1}\hookrightarrow V$ and $r_0 : V\to\mathbb{CP}^{N-1}$ satisfy $r_0\circ j = \mathrm{id}$ and $j\circ r_0 = r_0\simeq\mathrm{id}_V$ via $r_t$, so they are [[Def - Homotopy Equivalence and Contractible Space|homotopy inverse]] to each other; by homotopy invariance $H^k_{dR}(V)\cong H^k_{dR}(\mathbb{CP}^{N-1})$ for all $k$.
> >
> > **Step 3 — the overlap is $\mathbb{C}^N\setminus\{0\}$.** In the chart $\varphi$ of Step 1, $\varphi(U\cap V) = \varphi(U\setminus\{p_\infty\})$; and $\varphi(p_\infty) = (0,\dots,0)$ because $p_\infty = [0:\dots:0:1]$. Hence $U\cap V\cong\mathbb{C}^N\setminus\{0\}\cong\mathbb{R}^{2N}\setminus\{0\}$. The map $x\mapsto x/|x|$ retracts $\mathbb{R}^{2N}\setminus\{0\}$ onto $S^{2N-1}$, and the straight-line homotopy $H(x,t) = (1-t)x + t\,x/|x| = x\bigl((1-t) + t/|x|\bigr)$ stays in $\mathbb{R}^{2N}\setminus\{0\}$ (the scalar factor is strictly positive for $x\neq 0$). So $U\cap V\simeq S^{2N-1}$ and $H^k_{dR}(U\cap V)\cong H^k_{dR}(S^{2N-1})$ for all $k$. $\blacksquare$

> [!note]- Lemma 5: the top power of $\omega_m$ is nowhere-vanishing, and $\int_{\mathbb{CP}^m}\omega_m^{\wedge m}\neq 0$
> **Statement:** For every $m\ge 0$ the $2m$-form $\omega_m^{\wedge m}\in\Omega^{2m}(\mathbb{CP}^m)$ is nowhere-vanishing; consequently $\int_{\mathbb{CP}^m}\omega_m^{\wedge m}\neq 0$.
>
> **Hint:** Compute $\omega_m$ in the affine chart at $[1:0:\dots:0]$; there it is $\tfrac1\pi\sum_a du_a\wedge dv_a$, nondegenerate. Spread nondegeneracy to every point using the transitive $U(m+1)$-action, under which $\omega_m$ is invariant.
>
> **Why needed:** It shows the class $[\omega_m]^m$ — and hence $[\omega_N]^m$ after restriction — is nonzero, turning the additive "one-dimensional" answer of part (b) into the explicit generator claim, and driving part (c).
>
> > [!note]- Full proof
> > **Step 0 — $\omega_m$ at the base point.** Repeat the computation of Lemma 3 in the affine chart $U_0 = \{z_0\neq 0\}$ of $\mathbb{CP}^m$, with complex coordinates $w_a = z_a/z_0 = u_a + iv_a$, $a = 1,\dots,m$, and local section $s([1:w]) = \tfrac1\rho(1, w_1,\dots,w_m)$, $\rho^2 = 1 + |w|^2 = 1 + \sum_a(u_a^2 + v_a^2)$. Exactly as there, $\omega_m|_{U_0} = \tfrac{1}{2\pi}d(s^*\lambda)$ with $s^*\lambda = \tfrac{1}{\rho^2}\sum_{a=1}^m(u_a\,dv_a - v_a\,du_a)$ (the $j = 0$ term vanishes, each $j = a$ term is $\tfrac{u_a\,dv_a - v_a\,du_a}{\rho^2}$). At the base point $o = [1 : 0 : \dots : 0]$, i.e. $w = 0$: writing $f = 1/\rho^2$, we have $d(s^*\lambda) = df\wedge\sum_a(u_a\,dv_a - v_a\,du_a) + f\sum_a d(u_a\,dv_a - v_a\,du_a)$; at $w = 0$ we have $f = 1$ and $df = 0$ (since $\partial_{u_a} f = -2u_a f^2 = 0$ there), and $d(u_a\,dv_a - v_a\,du_a) = 2\,du_a\wedge dv_a$, so
> > $$\omega_m\big|_o = \frac{1}{2\pi}\cdot 2\sum_{a=1}^m du_a\wedge dv_a = \frac{1}{\pi}\sum_{a=1}^m du_a\wedge dv_a.$$
> > This is a nondegenerate alternating form, and its $m$-fold wedge is
> > $$\omega_m^{\wedge m}\big|_o = \frac{1}{\pi^m}\left(\sum_a du_a\wedge dv_a\right)^{\wedge m} = \frac{m!}{\pi^m}\,du_1\wedge dv_1\wedge\dots\wedge du_m\wedge dv_m\neq 0,$$
> > since only the fully-distinct term survives and there are $m!$ orderings. So $\omega_m^{\wedge m}$ is nonzero at $o$.
> >
> > **Step 1 — the invariance group.** The group $U(m+1)$ acts on $\mathbb{CP}^m$ by $g\cdot[z] = [gz]$ (well-defined, as $g$ is linear and commutes with scalar multiplication). Its action is transitive: given $[z]$ with representative $|z| = 1$, extend $z$ to a unitary basis of $\mathbb{C}^{m+1}$; the matrix $g$ whose first column is $z$ is unitary and satisfies $g e_0 = z$, so $g\cdot[e_0] = [z]$, and $[e_0] = o$. Moreover $\omega_m$ is $U(m+1)$-invariant: the lift $\tilde g(z) = gz$ satisfies $\pi\circ\tilde g = g\circ\pi$ and $\tilde g^*(\Sigma|_S) = \Sigma|_S$ (because $g$ is unitary, hence preserves $\langle\cdot,\cdot\rangle$ and its imaginary part $\Sigma$), so
> > $$\pi^*(g^*\omega_m) = (g\circ\pi)^*\omega_m = (\pi\circ\tilde g)^*\omega_m = \tilde g^*(\pi^*\omega_m) = \tilde g^*\bigl(\tfrac1\pi\Sigma|_S\bigr) = \tfrac1\pi\Sigma|_S = \pi^*\omega_m,$$
> > and injectivity of $\pi^*$ gives $g^*\omega_m = \omega_m$, hence $g^*(\omega_m^{\wedge m}) = (g^*\omega_m)^{\wedge m} = \omega_m^{\wedge m}$.
> >
> > **Step 2 — nowhere-vanishing.** Let $p\in\mathbb{CP}^m$ be arbitrary. By transitivity choose $g\in U(m+1)$ with $g(o) = p$. From $g^*(\omega_m^{\wedge m}) = \omega_m^{\wedge m}$, evaluating both sides at $o$ gives, for tangent vectors $X_1,\dots,X_{2m}\in T_o\mathbb{CP}^m$,
> > $$\bigl(\omega_m^{\wedge m}\bigr)_p\bigl(dg_o X_1,\dots,dg_o X_{2m}\bigr) = \bigl(\omega_m^{\wedge m}\bigr)_o(X_1,\dots,X_{2m}).$$
> > Since $\bigl(\omega_m^{\wedge m}\bigr)_o\neq 0$ (Step 0), the right side is nonzero for some choice of the $X_i$, so the left side is nonzero, forcing $\bigl(\omega_m^{\wedge m}\bigr)_p\neq 0$. As $p$ was arbitrary, $\omega_m^{\wedge m}$ is nowhere-vanishing.
> >
> > **Step 3 — nonzero integral.** Fix the complex orientation of the compact connected manifold $\mathbb{CP}^m$, with Riemannian volume form $\mathrm{vol}$. Write $\omega_m^{\wedge m} = h\cdot\mathrm{vol}$ with $h\in C^\infty(\mathbb{CP}^m)$; by Step 2 $h$ is nowhere zero, and being continuous on the connected $\mathbb{CP}^m$ it has constant sign. Therefore $\int_{\mathbb{CP}^m}\omega_m^{\wedge m} = \int_{\mathbb{CP}^m} h\,\mathrm{vol}$ is an integral of a nowhere-zero function of constant sign over a manifold of positive volume, hence nonzero. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix $N\ge 0$. We prove (a), then (b) by induction, then (c).
>
> **Part (a) — the Fubini–Study form.** Existence, uniqueness, reality, closedness, and the compatibility $\iota_N^*\omega_{N+1} = \omega_N$ are Lemma 2; the normalisation $\int_{\mathbb{CP}^1}\omega_1 = 1$ with the complex orientation is Lemma 3. This is exactly the content of (a).
>
> **Part (b) — the cohomology.** We first record the ambient facts. $\mathbb{CP}^N$ is the image of the connected compact sphere $S^{2N+1}$ under $\pi$, hence connected and compact, so $H^0_{dR}(\mathbb{CP}^N) = \mathbb{R}$ and $\dim H^{2N}_{dR}(\mathbb{CP}^N)\le\infty$; it is oriented by its complex structure. We prove the additive statement by induction on $N$.
>
> **Step 0 — base case $N = 1$.** By [[Thm - CP^1 is Diffeomorphic to S^2 via the Hopf Map|the diffeomorphism from the projective line to the two-sphere]], $\mathbb{CP}^1\cong S^2$, the cohomology of $\mathbb{CP}^1$ equals that of $S^2$, which by Lemma 1 (with $n = 2$) is $H^0 = H^2 = \mathbb{R}$ and $H^1 = 0$. This matches the claimed pattern for $N = 1$ ($\mathbb{R}$ in even degrees $0,2$; $0$ in degree $1$; nothing above degree $2$).
>
> **Step 1 — the inductive setup.** Let $N\ge 2$ and assume the additive statement for $\mathbb{CP}^{N-1}$: $H^k_{dR}(\mathbb{CP}^{N-1}) = \mathbb{R}$ for even $k$ with $0\le k\le 2N-2$, and $0$ otherwise. Take the cover $U,V$ of Lemma 4, so that (writing $\cong$ for the induced cohomology isomorphisms from Lemma 4)
> $$H^k_{dR}(U) = \begin{cases}\mathbb{R}, & k = 0\\ 0, & k\ge 1\end{cases},\qquad H^k_{dR}(V)\cong H^k_{dR}(\mathbb{CP}^{N-1}),\qquad H^k_{dR}(U\cap V)\cong H^k_{dR}(S^{2N-1}).$$
> Because $N\ge 2$, the overlap sphere $S^{2N-1}$ has dimension $2N-1\ge 3$, so by Lemma 1 its cohomology is $\mathbb{R}$ in degrees $0$ and $2N-1$ only. We now run the [[Thm - The Mayer-Vietoris Sequence|Mayer–Vietoris]] long exact sequence $\dots\to H^{k-1}_{dR}(U\cap V)\xrightarrow{\delta} H^k_{dR}(\mathbb{CP}^N)\xrightarrow{\beta} H^k_{dR}(U)\oplus H^k_{dR}(V)\xrightarrow{\alpha} H^k_{dR}(U\cap V)\to\dots$ degree by degree.
>
> **Step 2 — degree $1$.** As in Lemma 1 Step 2: $S^{2N-1}$ is connected, $\alpha : H^0_{dR}(U)\oplus H^0_{dR}(V) = \mathbb{R}^2\to\mathbb{R} = H^0_{dR}(U\cap V)$ is $(a,b)\mapsto a - b$, surjective, so the connecting map out of $H^0_{dR}(U\cap V)$ vanishes and $\beta : H^1_{dR}(\mathbb{CP}^N)\hookrightarrow H^1_{dR}(U)\oplus H^1_{dR}(V) = 0\oplus H^1_{dR}(\mathbb{CP}^{N-1}) = 0$ (the last equals $0$ by the inductive hypothesis, degree $1$ being odd). Hence $H^1_{dR}(\mathbb{CP}^N) = 0$.
>
> **Step 3 — degrees $2\le k\le 2N-2$.** Here $H^k_{dR}(U) = 0$; and $H^{k-1}_{dR}(S^{2N-1}) = 0$ (as $k-1$ lies strictly between $0$ and $2N-1$, since $1\le k-1\le 2N-3$) and $H^k_{dR}(S^{2N-1}) = 0$ (as $k$ lies strictly between $0$ and $2N-1$). The Mayer–Vietoris segment
> $$\underbrace{H^{k-1}_{dR}(U\cap V)}_{=\,0}\xrightarrow{\delta} H^k_{dR}(\mathbb{CP}^N)\xrightarrow{\beta} \underbrace{H^k_{dR}(U)}_{=\,0}\oplus H^k_{dR}(V)\xrightarrow{\alpha}\underbrace{H^k_{dR}(U\cap V)}_{=\,0}$$
> then shows $\beta$ is injective (kernel $= \operatorname{im}\delta = 0$) and surjective (image $= \ker\alpha = H^k_{dR}(V)$), so $H^k_{dR}(\mathbb{CP}^N)\cong H^k_{dR}(V)\cong H^k_{dR}(\mathbb{CP}^{N-1})$. By the inductive hypothesis this is $\mathbb{R}$ for even $k$ and $0$ for odd $k$, in the range $2\le k\le 2N-2$.
>
> **Step 4 — degree $2N-1$.** Now $H^{2N-2}_{dR}(S^{2N-1}) = 0$ ($2N-2\notin\{0, 2N-1\}$ for $N\ge 2$), $H^{2N-1}_{dR}(U) = 0$, and $H^{2N-1}_{dR}(V)\cong H^{2N-1}_{dR}(\mathbb{CP}^{N-1}) = 0$ (degree $2N-1$ exceeds the top degree $2N-2$ of $\mathbb{CP}^{N-1}$). The segment $\underbrace{H^{2N-2}_{dR}(U\cap V)}_{=0}\xrightarrow{\delta} H^{2N-1}_{dR}(\mathbb{CP}^N)\xrightarrow{\beta}\underbrace{H^{2N-1}_{dR}(U)\oplus H^{2N-1}_{dR}(V)}_{=0}$ forces $H^{2N-1}_{dR}(\mathbb{CP}^N) = 0$.
>
> **Step 5 — degree $2N$.** Consider
> $$\underbrace{H^{2N-1}_{dR}(U)\oplus H^{2N-1}_{dR}(V)}_{=\,0}\xrightarrow{\alpha} \underbrace{H^{2N-1}_{dR}(U\cap V)}_{\cong\,\mathbb{R}}\xrightarrow{\delta} H^{2N}_{dR}(\mathbb{CP}^N)\xrightarrow{\beta}\underbrace{H^{2N}_{dR}(U)\oplus H^{2N}_{dR}(V)}_{=\,0},$$
> where the left group is $0$ (both summands vanish, as in Step 4), the third group is $H^{2N-1}_{dR}(S^{2N-1}) = \mathbb{R}$, and the right group is $0$ ($H^{2N}_{dR}(U) = 0$ and $H^{2N}_{dR}(V)\cong H^{2N}_{dR}(\mathbb{CP}^{N-1}) = 0$ since $2N > 2N-2$). Exactness makes $\delta$ injective (kernel $= \operatorname{im}\alpha = 0$) and surjective (image $= \ker\beta = H^{2N}_{dR}(\mathbb{CP}^N)$), so $H^{2N}_{dR}(\mathbb{CP}^N)\cong\mathbb{R}$.
>
> **Step 6 — degrees $k > 2N$.** For $k = 2N+1$: $H^{2N}_{dR}(U\cap V) = H^{2N}_{dR}(S^{2N-1}) = 0$ and $H^{2N+1}_{dR}(U)\oplus H^{2N+1}_{dR}(V) = 0$, so $H^{2N+1}_{dR}(\mathbb{CP}^N) = 0$ by the same squeeze as in Step 3. For $k\ge 2N+2$ all four neighbours vanish (the sphere contributes nothing above $2N-1$, $U$ nothing above $0$, $V$ nothing above $2N-2$), so $H^k_{dR}(\mathbb{CP}^N) = 0$. This completes the induction: $H^k_{dR}(\mathbb{CP}^N) = \mathbb{R}$ for even $k$ with $0\le k\le 2N$, and $0$ otherwise.
>
> **Step 7 — the generators.** Fix even $k = 2m$ with $0\le m\le N$; we show $[\omega_N]^m := [\omega_N^{\wedge m}]$ generates the one-dimensional space $H^{2m}_{dR}(\mathbb{CP}^N)$, equivalently that it is nonzero. Let $\iota = \iota_{m,N} : \mathbb{CP}^m\hookrightarrow\mathbb{CP}^N$ be the standard inclusion. Iterating the compatibility $\iota_j^*\omega_{j+1} = \omega_j$ of Lemma 2 along $\mathbb{CP}^m\subset\mathbb{CP}^{m+1}\subset\dots\subset\mathbb{CP}^N$ gives $\iota^*\omega_N = \omega_m$, hence $\iota^*(\omega_N^{\wedge m}) = (\iota^*\omega_N)^{\wedge m} = \omega_m^{\wedge m}$. Therefore
> $$\int_{\mathbb{CP}^m}\iota^*\bigl(\omega_N^{\wedge m}\bigr) = \int_{\mathbb{CP}^m}\omega_m^{\wedge m}\neq 0\qquad(\text{by Lemma 5}).$$
> If $\omega_N^{\wedge m}$ were exact, say $\omega_N^{\wedge m} = d\gamma$, then $\iota^*(\omega_N^{\wedge m}) = d(\iota^*\gamma)$ would be exact on the closed manifold $\mathbb{CP}^m$ and integrate to $0$ by [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] — a contradiction. Hence $[\omega_N]^m\neq 0$, and since $H^{2m}_{dR}(\mathbb{CP}^N)\cong\mathbb{R}$ is one-dimensional, the nonzero class $[\omega_N]^m$ is a generator. This proves (b) in full.
>
> **Part (c) — detection on the line.** By (b), $H^2_{dR}(\mathbb{CP}^N) = \mathbb{R}\,[\omega_N]$ and $H^2_{dR}(\mathbb{CP}^1) = \mathbb{R}\,[\omega_1]$, each one-dimensional, with $[\omega_1]\neq 0$ because $\int_{\mathbb{CP}^1}\omega_1 = 1\neq 0$ (Lemma 3). The restriction $\iota_{1,N}^*$ sends $[\omega_N]\mapsto[\iota_{1,N}^*\omega_N] = [\omega_1]$ (Lemma 2's compatibility, iterated), a nonzero element; a linear map $\mathbb{R}\to\mathbb{R}$ carrying a basis vector to a nonzero vector is an isomorphism, so $\iota_{1,N}^* : H^2_{dR}(\mathbb{CP}^N)\to H^2_{dR}(\mathbb{CP}^1)$ is an isomorphism.
>
> For the exactness criterion, let $\eta\in\Omega^2(\mathbb{CP}^N)$ be closed. By (b) there is a unique $c\in\mathbb{R}$ and a $1$-form $\beta$ with $\eta = c\,\omega_N + d\beta$. Restricting to the line and using $\iota_{1,N}^*\omega_N = \omega_1$,
> $$\int_{\mathbb{CP}^1}\eta = \int_{\mathbb{CP}^1}\iota_{1,N}^*\eta = c\int_{\mathbb{CP}^1}\omega_1 + \int_{\mathbb{CP}^1} d(\iota_{1,N}^*\beta) = c\cdot 1 + 0 = c,$$
> the middle integral vanishing by Stokes on the closed manifold $\mathbb{CP}^1$ and the normalisation of Lemma 3. Now $\eta$ is exact if and only if $[\eta] = 0$ in $H^2_{dR}(\mathbb{CP}^N) = \mathbb{R}\,[\omega_N]$, which (as $[\omega_N]\neq 0$) holds if and only if $c = 0$, that is, if and only if $\int_{\mathbb{CP}^1}\eta = 0$. This proves (c). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Symplectic and Kähler geometry — nonvanishing of powers.** On any closed symplectic $2n$-manifold $(M,\omega)$, the classes $[\omega]^k$ for $0\le k\le n$ are all nonzero, by the very argument of Lemma 5: nondegeneracy makes $\omega^{\wedge n}$ a volume form, so $\int_M\omega^{\wedge n}\neq 0$, and if some intermediate power were exact one wedges with $\omega^{\wedge(n-k)}$ and integrates to a contradiction. The theorem applies because the Fubini–Study form is symplectic; the exercise is non-obvious because it produces cohomology purely from a nondegeneracy hypothesis, with no cover or induction, and it explains why no closed manifold with vanishing $H^{2}_{dR}$ (such as a sphere $S^{2n}$, $n\ge 2$) can carry a symplectic form.

**Algebraic topology — the cohomology of the flag and Grassmann manifolds.** The Mayer–Vietoris triple used here (affine chart, retract onto the previous stage, sphere overlap) is the de Rham shadow of a cell decomposition with one cell per even dimension. The same skeleton computes the cohomology of complex Grassmannians $\mathrm{Gr}_k(\mathbb{C}^n)$ and flag manifolds by stratifying them into affine cells (Schubert cells). The theorem applies because $\mathbb{CP}^N = \mathrm{Gr}_1(\mathbb{C}^{N+1})$ is the base case; the transfer is non-obvious because one must find, in each of these homogeneous spaces, the analogue of "remove a hyperplane, keep an affine chart".

**Gauge theory and physics — the monopole number.** A magnetic monopole on $S^2$ is a connection on a $U(1)$-bundle whose curvature $F$ integrates to $2\pi$ times an integer, the monopole charge. Part (c) is the statement that this integer is a complete invariant of the bundle at the level of de Rham cohomology: a closed $2$-form on $\mathbb{CP}^1 = S^2$ is a coboundary exactly when its integral vanishes, so the flux $\tfrac{1}{2\pi}\int_{S^2}F$ is the only cohomological datum. The theorem applies once one recognises $S^2 = \mathbb{CP}^1$; the point that makes it worth stating is that the quantisation of charge is not a physical postulate but the one-dimensionality of $H^2_{dR}(S^2)$ read through the normalisation $\int_{\mathbb{CP}^1}\omega_1 = 1$.

---

# Bridges

- **The first Chern class.** The single generator $[\omega_N]$ constructed here is the fixed target of the classifying-map construction: for a line bundle $L = f^*\mathcal{O}(-1)$ over a compact manifold, one sets $c_1(L) = -f^*[\omega_N]\in H^2_{dR}(M)$. The compatibility $\iota_N^*\omega_{N+1} = \omega_N$ is precisely what makes this independent of the dimension $N$ into which $M$ is classified, and the one-dimensionality of $H^2_{dR}(\mathbb{CP}^N)$ is what makes $c_1$ a single well-defined class rather than a choice among several. The construction is carried out on [[Def - First Chern Class via the Classifying Map]].

- **The nontriviality of the Hopf bundle.** The product $\mathbb{CP}^n\times S^1$ has $H^1_{dR}\neq 0$ (the pullback of $d\theta$ from the circle factor is closed and, by Stokes, not exact), whereas the additive computation here combined with the sphere Lemma shows $H^1_{dR}(S^{2n+1}) = 0$. Hence $S^{2n+1}$ is not diffeomorphic to $\mathbb{CP}^n\times S^1$, which is one route to the nontriviality of the Hopf bundle on [[Thm - The Hopf Bundle is Nontrivial]].

- **Detection by integration and the degree.** Part (c) says the class of a closed $2$-form on $\mathbb{CP}^N$ is faithfully recorded by one integral over the line. Fed the curvature of a Hermitian connection and combined with the top-cohomology theorem for surfaces, this becomes the identity between the degree of a line bundle and the integral of its first Chern class, the bridge to Chern–Weil theory developed for surfaces in [[Thm - Classification of Principal U(1)-Bundles by the First Chern Class]].

- **The classifying-space picture.** As $N\to\infty$ the spaces $\mathbb{CP}^N$ exhaust $\mathbb{CP}^\infty$, the classifying space of $U(1)$, and the compatible generators $[\omega_N]$ assemble into a single universal class. The additive answer here — one $\mathbb{R}$ in each even degree — is the de Rham reflection of the cell structure of $\mathbb{CP}^\infty$; the integral refinement (the polynomial ring $\mathbb{Z}[a]$) is recorded as a scope remark and not proved. See [[Def - Classifying Bundle and Classifying Map]].

---

# Unlocked by This

> [!tip] The de Rham first Chern class *(from Gauge Theory)*
> With $H^2_{dR}(\mathbb{CP}^N) = \mathbb{R}\,[\omega_N]$ and its detection on the line in hand, the first Chern class of a line bundle over a compact manifold becomes a well-defined de Rham class, and its integral over a surface becomes an honest integer-valued invariant. See **[[Def - First Chern Class via the Classifying Map]]** and **[[Thm - Classification of Principal U(1)-Bundles by the First Chern Class]]**.

> [!tip] The intersection form on $H^2(\mathbb{CP}^2)$ *(from Four-Manifold Topology)*
> The computation $H^2_{dR}(\mathbb{CP}^2)\cong\mathbb{R}$ with generator $[\omega_2]$ and $\int_{\mathbb{CP}^2}\omega_2\wedge\omega_2\neq 0$ (Lemma 5 with $m = 2$) is the de Rham input to the intersection form of $\mathbb{CP}^2$, the simplest positive-definite unimodular form, used in the classification of four-manifolds in chapter XIII.
