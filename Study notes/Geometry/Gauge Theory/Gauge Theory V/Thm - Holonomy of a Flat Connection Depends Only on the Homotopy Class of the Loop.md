---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Local Triviality of Flat Connections"
  - "Def - Holonomy Group of a Connection"
  - "Def - Parallel Transport in a Principal Bundle"
  - "Thm - Properties of Parallel Transport"
  - "Thm - Existence and Uniqueness of Horizontal Lifts"
  - "Def - Flat Connection"
  - "Def - Homotopy of Paths"
  - "Def - Path-Product and the Fundamental Group"
  - "Thm - The Fundamental Group is a Group"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\pi\colon P\to M$ is a principal $G$-bundle over a connected smooth manifold $M$, with the structure group $G$ a Lie group acting on the **right**, $R_g(p)=p\cdot g$; the fibre over $m\in M$ is $P_m=\pi^{-1}(m)$, and the right action is free and transitive on each fibre. A **connection** on $P$ is a $\mathfrak{g}$-valued one-form $\omega\in\Omega^1(P;\mathfrak{g})$ with $\omega(\xi_P)=\xi$ for $\xi\in\mathfrak{g}$ and $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$; its curvature is $\Omega=d\omega+\tfrac12[\omega\wedge\omega]\in\Omega^2(P;\mathfrak{g})$, and $\omega$ is **flat** when $\Omega=0$ (see [[Def - Flat Connection]]). We write $\mathfrak{g}=T_eG$ for the Lie algebra.

For a piecewise smooth curve $c\colon[0,1]\to M$ we write $\Gamma(c)\colon P_{c(0)}\to P_{c(1)}$ for the **parallel transport** it induces, the map $p\mapsto\tilde c(1)$ where $\tilde c$ is the unique horizontal lift of $c$ with $\tilde c(0)=p$ (see [[Def - Parallel Transport in a Principal Bundle]] and [[Thm - Existence and Uniqueness of Horizontal Lifts]]). When $c$ is a loop based at $m$ and $p\in P_m$, the **holonomy** $\operatorname{hol}_p(c)\in G$ is the unique group element with $\Gamma(c)(p)=p\cdot\operatorname{hol}_p(c)$ (see [[Def - Holonomy Group of a Connection]]).

A **local section** is a smooth map $s\colon U\to P$ over an open $U\subseteq M$ with $\pi\circ s=\operatorname{id}_U$; its **local connection form** (gauge potential) is $A_s=s^*\omega\in\Omega^1(U;\mathfrak{g})$. A **flat chart** (or flat gauge) is a connected open $U\subseteq M$ carrying a local section $s_U$ with $s_U^*\omega=0$; by [[Thm - Local Triviality of Flat Connections]] every point of a manifold with a flat connection lies in one. We write $I=[0,1]$ and $\theta$ for the left Maurer–Cartan form of $G$ (see [[Def - The Maurer-Cartan Form]]), the $\mathfrak{g}$-valued one-form $\theta_g=(dL_{g^{-1}})_g\colon T_gG\to\mathfrak{g}$, which is a linear isomorphism at every $g\in G$.

The **fundamental group** $\pi_1(M,m)$ is the group of path-homotopy classes $[c]$ of continuous loops at $m$ under the path-product, and its group law is $[a][b]=[a\cdot b]$, where $a\cdot b$ traverses $a$ on $[0,\tfrac12]$ and $b$ on $[\tfrac12,1]$ (see [[Def - Path-Product and the Fundamental Group]] and [[Thm - The Fundamental Group is a Group]]). Two paths are **homotopic relative to endpoints**, written $c_0\simeq c_1$, when there is a continuous $H\colon I\times I\to M$ with $H(0,\cdot)=c_0$, $H(1,\cdot)=c_1$, and $H(s,0)$, $H(s,1)$ independent of $s$ (see [[Def - Homotopy of Paths]]).

> [!warning] Convention: order of the path product and the sign of the monodromy
> Parallel transport composes in the order opposite to concatenation: transporting first along $a$ and then along $b$ gives $\Gamma(a\cdot b)=\Gamma(b)\circ\Gamma(a)$ (do $a$'s transport first). With the fundamental-group law $[a][b]=[a\cdot b]$ fixed on [[Def - Path-Product and the Fundamental Group]], the raw holonomy map $[c]\mapsto\operatorname{hol}_p(c)$ is therefore an **anti-homomorphism**. To obtain a genuine homomorphism we compose with group inversion and set $\rho_\omega([c]):=\operatorname{hol}_p(c)^{-1}$, which equals the holonomy of the reversed loop. Under the opposite convention for the fundamental group (reading the product right-to-left, as several gauge-theory texts do) the raw map $\operatorname{hol}_p$ is itself the homomorphism; the two conventions differ only by this inversion. The series fixes $\rho_\omega([c])=\operatorname{hol}_p(c)^{-1}$.

> [!warning] Convention: source statement and its typographical slips
> Haydys states this result as the unlabelled assertion (his §3.3.2, p. 33) that for a flat connection the map $\gamma\mapsto\operatorname{Hol}(\nabla;\gamma)$ "depends on the homotopy class of $\gamma$ only", citing Kobayashi–Nomizu I, Ch. II §9, and gives no proof; the proof below is supplied in full. In the adjacent construction (his D3.3.6) the source writes a representation as "$\rho\colon\tilde M\to GL_k(\mathbb{R})$", a typo for $\rho\colon\pi_1(M)\to GL_k(\mathbb{R})$; we use the corrected form. The source also uses the same letter for a connection and for the local one-form; we keep $\omega$ for the connection and $A_s$ for its local form.

---

# Statement

> **Theorem (homotopy invariance of parallel transport for a flat connection).** Let $\pi\colon P\to M$ be a principal $G$-bundle carrying a flat connection $\omega$ (so $\Omega_\omega=0$). Let $m,m'\in M$ and let $c_0,c_1\colon I\to M$ be piecewise smooth paths with $c_0(0)=c_1(0)=m$ and $c_0(1)=c_1(1)=m'$. If $c_0$ and $c_1$ are homotopic relative to their endpoints — there is a continuous map $H\colon I\times I\to M$ with
> $$H(0,t)=c_0(t),\qquad H(1,t)=c_1(t),\qquad H(s,0)=m,\qquad H(s,1)=m'\quad(s,t\in I)$$
> — then their parallel transports coincide:
> $$\Gamma(c_0)=\Gamma(c_1)\colon P_m\longrightarrow P_{m'}.$$
> The homotopy $H$ is required only to be continuous, not smooth.

> **Corollary (the monodromy representation).** Fix a base point $m\in M$ and a point $p\in P_m$. Every class in $\pi_1(M,m)$ contains a piecewise smooth loop, and for any two piecewise smooth loops $a,b$ at $m$ representing the same class one has $\operatorname{hol}_p(a)=\operatorname{hol}_p(b)$. Hence
> $$\rho_\omega\colon\pi_1(M,m)\longrightarrow G,\qquad \rho_\omega([c]):=\operatorname{hol}_p(c)^{-1}\quad(c\text{ any piecewise smooth loop in the class }[c])$$
> is a well-defined group homomorphism, the **monodromy representation of $\omega$ at $p$**. Replacing $p$ by $p\cdot g$ conjugates it: $\rho_{\omega,\,p\cdot g}=g^{-1}\rho_{\omega,p}\,g$; so $[\rho_\omega]$ is a well-defined conjugacy class of homomorphisms, independent of the choice of $p\in P_m$. If instead $E=P\times_\rho V$ is an associated vector bundle with induced connection $\nabla$, the same construction gives a linear representation
> $$\rho_\nabla\colon\pi_1(M,m)\longrightarrow GL(E_m),\qquad \rho_\nabla([c])=PT_c^{-1},$$
> where $PT_c\colon E_m\to E_m$ is parallel transport around $c$; for $E$ of rank $k$ this is $\rho_\nabla\colon\pi_1(M,m)\to GL_k(\mathbb{R})$ after a choice of basis of $E_m$ (Haydys's $\rho_A$).

---

# Motivation

For a general connection the parallel transport $\Gamma(c)$ genuinely records the *path* $c$, not merely its endpoints: carrying a vector around a small loop on the round sphere rotates it by the enclosed area, so the holonomy of a loop is an honest geometric measurement that changes when the loop is deformed. This is precisely what makes curvature detectable. A flat connection is the opposite extreme, the case $\Omega=0$, and the question this theorem answers is: *what survives of holonomy when the local obstruction to path-independence has been switched off?*

The answer is the sharpest possible one. When $\omega$ is flat, parallel transport still depends on the path in general — a flat connection on a bundle over a non-simply-connected base can have wildly non-trivial holonomy, as the flat band on the Möbius bundle already shows — but it depends on the path *only through its homotopy class*. Deform the loop continuously without moving its endpoints and the holonomy does not budge. Locally, flatness makes parallel transport path-independent outright (this is [[Thm - Local Triviality of Flat Connections]]: in a flat chart the transport between two points is the same along every curve joining them); the theorem is the global upgrade of that local fact, and the upgrade is governed by exactly the invariant that measures the failure of a space to be locally trivial, namely $\pi_1$.

The consequence is structural and is the reason the theorem is stated at all. Homotopy invariance is exactly the statement that holonomy descends from the set of loops to the set of homotopy classes of loops, which is the fundamental group. So a flat connection determines, and is largely determined by, a homomorphism
$$\rho_\omega\colon\pi_1(M,m)\longrightarrow G,$$
its monodromy representation. This is the first appearance in the series of the dictionary
$$\{\text{flat connections}\}\;\longleftrightarrow\;\{\text{representations of }\pi_1\},$$
completed on [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group]], which turns a differential-geometric object (a solution of the first-order equation $\Omega=0$, considered up to gauge) into a purely algebraic one (a conjugacy class of homomorphisms from a discrete group). The present theorem is the half of that dictionary that produces the algebra from the geometry; every later statement about the moduli space of flat connections — that it is compact when $G$ is compact, that for a surface it is the representation variety with its symplectic structure — rests on it. In physics the same homomorphism is the Aharonov–Bohm phase: an electron transported around a solenoid it never touches picks up the holonomy of a flat $U(1)$-connection, and the theorem says this phase is a topological invariant of the electron's path, foreshadowed here and taken up in chapter VII.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypotheses are "the connection is flat" and "the two paths are homotopic rel endpoints". Each is met by problems that do not announce it.

A first disguised source is **a connection built from a bundle with locally constant transition functions**, for instance a bundle associated to a covering space or, more generally, a bundle with discrete structure group. Such a bundle carries a canonical connection whose local connection forms vanish, and $\Omega=dA+\tfrac12[A\wedge A]=0$ because $A=0$ in each chart; the bridge $B\Rightarrow A$ is the implication *locally constant cocycle $\Rightarrow$ flat connection* proved on [[Thm - Local Triviality of Flat Connections]]. One recognises the hypothesis not by seeing "$\Omega=0$" written down but by seeing a bundle glued from constant data. *Example problem:* on the Möbius line bundle, presented as $\mathbb{R}\times_{\pm1}\mathbb{R}$ with the two charts glued by the constant $-1$, deduce that the natural connection is flat, so the theorem applies and holonomy is a homomorphism $\pi_1(S^1)=\mathbb{Z}\to O(1)$.

A second disguised source is **a curvature that vanishes only on a subregion**. If $F$ is supported away from an open set $U$ — the field of an idealised solenoid, zero outside the coil — then $\omega|_U$ is flat, and the theorem applies to loops confined to $U$ even though the ambient connection is not flat. The bridge is that flatness is a local, open condition: $\Omega=0$ on $\pi^{-1}(U)$ suffices to run the whole argument inside $U$. *Example problem:* show that the Aharonov–Bohm holonomy of a loop encircling a thin solenoid depends only on how many times the loop winds, because outside the solenoid the connection is flat.

A third disguised source is **any statement of the form "the loop bounds a disc"**, that is, a null-homotopic loop. A loop bounding a piecewise smooth disc is homotopic rel base point to the constant loop, so the theorem forces its holonomy to be trivial; the bridge $B\Rightarrow A$ is the observation that "bounds a disc" is a special case of "homotopic to a constant path". This is how one proves that a flat connection over a simply connected base is gauge-trivial: *every* loop is null-homotopic, so the monodromy representation is trivial. *Example problem:* prove that a flat $U(1)$-connection on the two-sphere has $\operatorname{hol}(c)=1$ for every loop $c$, hence is gauge-equivalent to the product connection.

**Targets (Output Amplification).** The bare conclusion "$\Gamma(c_0)=\Gamma(c_1)$" is amplified by combining it with structure on $G$ or on $M$.

Combine the conclusion with **the group structure of $G$ and the composition law of parallel transport** to obtain the monodromy homomorphism $\rho_\omega\colon\pi_1(M,m)\to G$ (the Corollary). The extra ingredient $D$ is [[Thm - Properties of Parallel Transport]] (concatenation of paths composes their transports) together with the equivariance $\Gamma(c)\circ R_g=R_g\circ\Gamma(c)$; the payoff $E$ is that a differential-geometric object is converted into a representation of a discrete group, the input to the entire flat-connection–representation correspondence.

Combine the conclusion with **a presentation of $\pi_1(M,m)$ by generators and relations** to *compute* the holonomy of every loop from finitely many holonomies. The extra ingredient is a set of generating loops; the payoff is that on a surface of genus $g$, whose group is $\langle a_i,b_i\mid\prod_i[a_i,b_i]=1\rangle$, a flat connection is pinned down by $2g$ group elements $\rho_\omega(a_i),\rho_\omega(b_i)$ subject to the single relation $\prod_i[\rho_\omega(a_i),\rho_\omega(b_i)]=1$ — the equation cutting out the representation variety.

Combine the conclusion with **compactness of $G$** to bound the moduli space. Once $\rho_\omega$ lands in a compact group and $\pi_1$ is finitely generated, the set of possible monodromies is a closed subset of a compact product $G^N$; the payoff, developed on [[Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact]], is that the moduli space of flat connections with compact structure group is itself compact — the first compactness theorem of gauge theory.

---

# Why Is It True

Strip away the bookkeeping and the mechanism is a single idea repeated across a grid. Flatness has one immediate, local consequence, proved separately as [[Thm - Local Triviality of Flat Connections]]: around every point there is a chart in which parallel transport is completely blind to the route — any two curves with the same endpoints inside the chart give the same transport, because in the flat gauge the horizontal lift is just "hold the fibre coordinate constant". So on the small scale, holonomy of a loop is trivial and transport between two nearby points is a fixed isomorphism.

The homotopy $H$ between $c_0$ and $c_1$ is a continuous map of a square into $M$. Because the square is compact, its image is covered by finitely many of these flat charts, and — this is the quantitative heart — we can rule the square into a fine grid so fine that each little cell lands entirely inside one flat chart. Inside a single cell nothing can go wrong: transport around the boundary of the cell is trivial, precisely because the cell sits in a chart where holonomy vanishes. The full homotopy is then assembled from these harmless cells. Sliding the path from the bottom edge of the grid ($c_0$) to the top edge ($c_1$) one cell-row at a time changes the transport by a product of cell-boundary holonomies, each of which is the identity, so the total transport never changes.

> **The mechanism in one sentence:** flatness makes the holonomy of every sufficiently small loop trivial, and a homotopy is nothing but a way of writing the difference between two paths as a stack of arbitrarily small loops.

There is one subtlety worth flagging as intuition, because it is where a naive argument fails and the correct one is cleaner. One is tempted to transport along the intermediate paths $t\mapsto H(s,t)$ for each fixed $s$ and watch the transport vary with $s$. But $H$ is only continuous, so these intermediate paths are only continuous, and parallel transport is not even defined for a merely continuous path. The fix is to never transport along an image of $H$ at all. Instead we use $H$ only to certify that certain points lie together in a common flat chart, and we transport between those points along smooth curves *inside the charts*, where flatness guarantees the route is irrelevant. Continuity of $H$ is all that is needed for the certification; smoothness is never asked of it. That is why the theorem holds for continuous homotopies between piecewise smooth paths, which is exactly the generality the fundamental group demands.

---

# What Makes This Hard

The non-obvious step is organisational, not analytic: one must resist transporting along the homotopy's intermediate curves (which are only continuous, so their transport is undefined) and instead transport only along smooth curves inside flat charts, using the homotopy purely to place points in common charts. The common error is to treat the intermediate paths $H(s,\cdot)$ as if $\frac{d}{ds}\Gamma(H(s,\cdot))$ made sense and "differentiate the holonomy", which both requires a smooth homotopy the fundamental group does not provide and hides the real content. A second trap is the composition order: parallel transport reverses concatenation, so the raw holonomy map is an *anti*-homomorphism, and forgetting the reversal (or silently using the opposite $\pi_1$ convention) produces a map that fails to respect the group law.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Use flatness (via [[Thm - Local Triviality of Flat Connections]]) to define, in each flat chart, a route-independent transport $T^U_{x,y}$ between points of the chart. Cover the homotopy square by flat charts, subdivide it into a grid so fine that each cell lands in one chart, and show that the transport read off along the bottom edge (which is $\Gamma(c_0)$) equals the transport along the top edge (which is $\Gamma(c_1)$) by pushing the comparison across the grid one cell at a time; inside a cell the four edge-transports commute because they all live in one chart. Then turn the geometric conclusion into the algebraic monodromy homomorphism.

**Subgoal decomposition:**

1. **A subdivision fine enough for the cover (Lebesgue number).** Show that a continuous image of the compact square, covered by open flat charts, can be ruled into a grid of cells each mapping into a single chart.
   - *Hint:* Prove the Lebesgue number lemma for a compact metric space directly (finite subcover of doubled balls), then take cells of diameter below the number.
   - *Why needed:* Every later step transports only inside one chart, so each cell must lie in one chart.

2. **Route-independent transport in a flat chart.** In a flat gauge the horizontal lift holds the fibre coordinate constant, so define $T^U_{x,y}\colon P_x\to P_y$ and prove it depends only on $x,y$, composes ($T^U_{y,z}T^U_{x,y}=T^U_{x,z}$), fixes points ($T^U_{x,x}=\operatorname{id}$), and is right-equivariant.
   - *Hint:* Restate the horizontal-lift equation $\dot h=-dR_h(A_s(\dot c))$ and set $A_s=0$.
   - *Why needed:* It is the atom every cell is built from, and it is where flatness enters.

3. **Chart compatibility.** Show $T^U_{x,y}=T^{U'}_{x,y}$ whenever $x,y$ lie in one connected component of $U\cap U'$.
   - *Hint:* Two flat gauges differ by a locally constant transition function; on a connected overlap component it is constant.
   - *Why needed:* Adjacent cells share an edge but sit in different charts; the shared edge's transport must be unambiguous.

4. **The commuting square.** For one grid cell, prove that going right-then-up equals up-then-right: $\sigma_{i,j+1}\circ\tau_{i,j}=\tau_{i+1,j}\circ\sigma_{i,j}$.
   - *Hint:* All four corners lie in the cell's chart; apply subgoal 2's composition law there and subgoal 3 to name the edges consistently.
   - *Why needed:* This is the single algebraic identity the whole grid telescopes.

5. **Every class has a piecewise smooth representative (for the Corollary).** Show a continuous loop is homotopic rel base point to a piecewise smooth one.
   - *Hint:* Subdivide the loop into arcs inside convex coordinate balls and replace each by the coordinate straight segment; the straight-line homotopy stays in the ball.
   - *Why needed:* Holonomy is defined only for piecewise smooth loops, but $\pi_1$ is built from continuous ones.

6. **Assemble.** Telescope the commuting squares to get $\Gamma(c_0)=\Gamma(c_1)$; then deduce well-definedness of $\rho_\omega$, the homomorphism property (with the reversal), and conjugation under change of $p$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Lebesgue number of an open cover of a compact metric space
> **Statement:** Let $(K,d)$ be a compact metric space and $\{O_\alpha\}_{\alpha\in\mathcal{A}}$ an open cover. Then there is $\delta>0$ (a *Lebesgue number*) such that every subset $S\subseteq K$ with $\operatorname{diam}(S)<\delta$ is contained in some single $O_\alpha$.
>
> **Hint:** For each point choose a ball whose double lies in a cover member; take a finite subcover of the (undoubled) balls and let $\delta$ be the smallest radius.
>
> **Why needed:** Applied to $H\colon I\times I\to M$ it lets us rule the homotopy square into cells each landing in one flat chart; applied to a loop $[0,1]\to M$ it produces the subdivision for the smoothing Lemma 5.
>
> > [!note]- Full proof
> > We must produce $\delta>0$ with the stated property. **Choose local radii.** For each $x\in K$, since $\{O_\alpha\}$ covers $K$ there is $\alpha(x)$ with $x\in O_{\alpha(x)}$, and since $O_{\alpha(x)}$ is open there is $r(x)>0$ with the open ball $B(x,2r(x))\subseteq O_{\alpha(x)}$. The balls $\{B(x,r(x))\}_{x\in K}$ form an open cover of $K$.
> >
> > **Extract a finite subcover.** By compactness of $K$ there are finitely many points $x_1,\dots,x_n$ with $K=\bigcup_{i=1}^n B(x_i,r(x_i))$. Set
> > $$\delta:=\min\{r(x_1),\dots,r(x_n)\}>0 \qquad\text{(a finite minimum of positive numbers, hence positive).}$$
> >
> > **Verify the covering property.** Let $S\subseteq K$ with $\operatorname{diam}(S)<\delta$. If $S=\varnothing$ it lies in any $O_\alpha$; otherwise pick $y\in S$. As the finite balls cover $K$, there is an index $i$ with $y\in B(x_i,r(x_i))$, that is $d(y,x_i)<r(x_i)$. For any $z\in S$,
> > $$d(z,x_i)\le d(z,y)+d(y,x_i)<\operatorname{diam}(S)+r(x_i)<\delta+r(x_i)\le r(x_i)+r(x_i)=2r(x_i),$$
> > using the triangle inequality, then $d(z,y)\le\operatorname{diam}(S)<\delta$, then $\delta\le r(x_i)$ (as $\delta$ is the minimum). Thus $z\in B(x_i,2r(x_i))\subseteq O_{\alpha(x_i)}$. Since $z\in S$ was arbitrary, $S\subseteq O_{\alpha(x_i)}$. Therefore $\delta$ is a Lebesgue number. $\blacksquare$
> >
> > *(This reproves the statement of `Thm - Lebesgue Number Lemma`, which the vault does not yet carry with a complete proof; the argument is self-contained here.)*

> [!note]- Lemma 2: Route-independent parallel transport inside a flat chart
> **Statement:** Let $U\subseteq M$ be a connected flat chart with flat gauge $s\colon U\to P$ (so $A_s=s^*\omega=0$). Then:
> (i) for every piecewise smooth $\gamma\colon[0,1]\to U$ and every $g\in G$, the horizontal lift of $\gamma$ starting at $s(\gamma(0))\cdot g$ is $\tilde\gamma(t)=s(\gamma(t))\cdot g$;
> (ii) consequently $\Gamma(\gamma)\colon P_{\gamma(0)}\to P_{\gamma(1)}$ sends $s(\gamma(0))\cdot g\mapsto s(\gamma(1))\cdot g$ and depends only on the endpoints $x=\gamma(0)$, $y=\gamma(1)$, not on $\gamma$; write $T^U_{x,y}$ for this map;
> (iii) $T^U_{x,x}=\operatorname{id}_{P_x}$, and $T^U_{y,z}\circ T^U_{x,y}=T^U_{x,z}$ for all $x,y,z\in U$, and $T^U_{x,y}\circ R_g=R_g\circ T^U_{x,y}$ for all $g\in G$.
>
> **Hint:** Put the horizontal-lift equation in the gauge $s$ and use $A_s=0$; read the composition and equivariance off the closed-form $s(x)g\mapsto s(y)g$.
>
> **Why needed:** This is the atomic transport out of which the whole grid is built, and the only place flatness is used; part (iii) is what makes the cell-diagram commute.
>
> > [!note]- Full proof
> > **Part (i): the lift formula.** By [[Thm - Existence and Uniqueness of Horizontal Lifts]] every lift of $\gamma$ through a point of $P_{\gamma(0)}$ is of the form $t\mapsto s(\gamma(t))\cdot h(t)$ for a unique piecewise smooth $h\colon[0,1]\to G$, and such a lift is horizontal if and only if $h$ solves
> > $$\dot h(t)=-\,dR_{h(t)}\big(A_s(\dot\gamma(t))\big)\qquad\text{(the local horizontal-lift equation, }A_s=s^*\omega\text{ the local connection form).}$$
> > Since $U$ is a flat chart, $A_s=s^*\omega=0$, so the right-hand side vanishes and the equation reads $\dot h(t)=0$. Hence $h$ is constant, $h(t)\equiv h(0)$. Imposing the initial condition $\tilde\gamma(0)=s(\gamma(0))\cdot g$ gives $h(0)=g$, so $h(t)\equiv g$ and $\tilde\gamma(t)=s(\gamma(t))\cdot g$. Uniqueness of the horizontal lift with a given initial point (same theorem) shows this is the horizontal lift.
> >
> > **Part (ii): endpoint dependence only.** By the definition of parallel transport, $\Gamma(\gamma)(p)=\tilde\gamma(1)$ where $\tilde\gamma$ is the horizontal lift through $p=\tilde\gamma(0)$ (see [[Def - Parallel Transport in a Principal Bundle]]). Every $p\in P_{\gamma(0)}=P_x$ is uniquely $p=s(x)\cdot g$ for some $g\in G$, because the right action is free and transitive on the fibre. By part (i), $\Gamma(\gamma)(s(x)g)=\tilde\gamma(1)=s(\gamma(1))\cdot g=s(y)\cdot g$. The right-hand side names $x$ and $y$ only through $s(x),s(y)$ and does not mention $\gamma$; so any two piecewise smooth curves in $U$ from $x$ to $y$ induce the same map, which we call $T^U_{x,y}$. (This route-independence is also the parallel-transport clause of [[Thm - Local Triviality of Flat Connections]]; we have re-derived it here from the lift formula for self-containedness.)
> >
> > **Part (iii): the algebraic identities.** All three follow by evaluating on a general fibre element $s(x)\cdot g$:
> > $$T^U_{x,x}(s(x)g)=s(x)g\qquad\Rightarrow\qquad T^U_{x,x}=\operatorname{id}_{P_x};$$
> > $$\big(T^U_{y,z}\circ T^U_{x,y}\big)(s(x)g)=T^U_{y,z}(s(y)g)=s(z)g=T^U_{x,z}(s(x)g)\qquad\Rightarrow\qquad T^U_{y,z}\circ T^U_{x,y}=T^U_{x,z},$$
> > where the middle equality uses part (ii) twice (transport $x\to y$, then $y\to z$), and since every element of $P_x$ has the form $s(x)g$ the operator identity follows;
> > $$\big(T^U_{x,y}\circ R_{g'}\big)(s(x)g)=T^U_{x,y}(s(x)\,gg')=s(y)\,gg'=\big(s(y)g\big)\cdot g'=\big(R_{g'}\circ T^U_{x,y}\big)(s(x)g),$$
> > using $R_{g'}(s(x)g)=s(x)(gg')$ and part (ii); hence $T^U_{x,y}\circ R_{g'}=R_{g'}\circ T^U_{x,y}$ for every $g'\in G$. $\blacksquare$

> [!note]- Lemma 3: Compatibility of the transport across overlapping flat charts
> **Statement:** Let $U$ and $U'$ be flat charts and let $x,y$ lie in a common connected component $C$ of $U\cap U'$. Then $T^U_{x,y}=T^{U'}_{x,y}$.
>
> **Hint:** The two flat gauges differ by a $G$-valued function whose derivative vanishes; a locally constant function is constant on the connected set $C$.
>
> **Why needed:** In the grid, a cell edge is shared by two cells sitting in different charts; without this compatibility the transport across the shared edge would be ambiguous and the telescoping would not close.
>
> > [!note]- Full proof
> > We must show two operators $P_x\to P_y$ agree. **Compare the two gauges on the overlap.** Over $U\cap U'$ both $s_U$ and $s_{U'}$ are local sections of the same principal bundle, so there is a unique smooth $h\colon U\cap U'\to G$ with
> > $$s_{U'}(z)=s_U(z)\cdot h(z)\qquad(z\in U\cap U'),$$
> > because the right $G$-action is free and transitive on each fibre. **Use flatness of both gauges.** The local connection forms transform by
> > $$A_{s_{U'}}=\operatorname{Ad}_{h^{-1}}A_{s_U}+h^*\theta\qquad\text{(transformation law for local connection forms under a change of section, [[Thm - Transformation of Local Connection and Curvature Forms]]),}$$
> > with $\theta$ the left Maurer–Cartan form. Both gauges are flat, $A_{s_U}=0$ and $A_{s_{U'}}=0$, so the identity collapses to $0=h^*\theta$, i.e. $\theta\circ dh=0$ pointwise. **Conclude $h$ is locally constant.** At each point $z$ the map $\theta_{h(z)}\colon T_{h(z)}G\to\mathfrak{g}$ is a linear isomorphism (a defining property of the Maurer–Cartan form, [[Def - The Maurer-Cartan Form]]), so $\theta_{h(z)}\big(dh_z(v)\big)=0$ forces $dh_z(v)=0$ for every tangent vector $v$; hence $dh\equiv0$ on $U\cap U'$, and $h$ is locally constant. (This is the (c)$\Rightarrow$(d) implication of [[Thm - Local Triviality of Flat Connections]], that two flat gauges differ by a locally constant transition function.) On the connected component $C$ a locally constant function is constant: $h\equiv h_0\in G$ on $C$.
> >
> > **Match the two transports.** Fix $p\in P_x$; since $x\in C$, write $p=s_U(x)\cdot g$, and note $p=s_{U'}(x)\cdot(h_0^{-1}g)$ because $s_{U'}(x)=s_U(x)h_0$. Then, using the closed form of Lemma 2(ii) in each chart,
> > $$T^{U'}_{x,y}(p)=s_{U'}(y)\cdot(h_0^{-1}g)=\big(s_U(y)h_0\big)\cdot(h_0^{-1}g)=s_U(y)\cdot g=T^U_{x,y}(p),$$
> > where the second equality uses $s_{U'}(y)=s_U(y)h_0$ (valid because $y\in C$ too). As $p\in P_x$ was arbitrary, $T^U_{x,y}=T^{U'}_{x,y}$. $\blacksquare$

> [!note]- Lemma 4: The grid, and the commuting-square identity
> **Statement:** Let $H\colon I\times I\to M$ be continuous with $H(s,0)$ and $H(s,1)$ independent of $s$, and let $\{U_\alpha\}$ be a cover of $M$ by connected flat charts. Then there is $N\in\mathbb{N}$ such that, writing $v_{i,j}=(i/N,\,j/N)$ and $x_{i,j}=H(v_{i,j})$ for $0\le i,j\le N$, each closed cell $R_{i,j}=[\tfrac{i}{N},\tfrac{i+1}{N}]\times[\tfrac{j}{N},\tfrac{j+1}{N}]$ satisfies $H(R_{i,j})\subseteq U_{\alpha(i,j)}$ for some chart $U_{\alpha(i,j)}$. For each vertical edge $E_{i,j}=\{i/N\}\times[\tfrac{j}{N},\tfrac{j+1}{N}]$ (with $0\le i\le N$, $0\le j\le N-1$) the transport
> $$\tau_{i,j}:=T^{U}_{x_{i,j},\,x_{i,j+1}}\qquad\text{for any flat chart }U\supseteq H(E_{i,j})$$
> is independent of the chart $U$; likewise for each horizontal edge $F_{i,j}=[\tfrac{i}{N},\tfrac{i+1}{N}]\times\{j/N\}$ (with $0\le i\le N-1$, $0\le j\le N$) the transport $\sigma_{i,j}:=T^{U}_{x_{i,j},\,x_{i+1,j}}$ is chart-independent, with $\sigma_{i,0}=\operatorname{id}_{P_m}$ and $\sigma_{i,N}=\operatorname{id}_{P_{m'}}$. Moreover, for every cell $0\le i\le N-1$, $0\le j\le N-1$,
> $$\sigma_{i,j+1}\circ\tau_{i,j}=\tau_{i+1,j}\circ\sigma_{i,j}.\tag{$\star$}$$
>
> **Hint:** Get $N$ from a Lebesgue number of $\{H^{-1}(U_\alpha)\}$; each edge is connected and lies in the cell's chart, so Lemma 3 makes $\tau,\sigma$ unambiguous; then apply Lemma 2(iii) inside the single cell chart.
>
> **Why needed:** ($\star$) is the one identity the whole homotopy invariance telescopes from.
>
> > [!note]- Full proof
> > **Existence of the grid.** The sets $\{H^{-1}(U_\alpha)\}$ form an open cover of the compact metric space $I\times I$ (with the Euclidean metric). By Lemma 1 it has a Lebesgue number $\delta>0$. Choose $N$ with $\sqrt{2}/N<\delta$; then each cell $R_{i,j}$ has diameter $\sqrt{2}/N<\delta$, so $R_{i,j}\subseteq H^{-1}(U_{\alpha(i,j)})$ for some $\alpha(i,j)$, that is $H(R_{i,j})\subseteq U_{\alpha(i,j)}$. Fix one such chart $U_{i,j}:=U_{\alpha(i,j)}$ for each cell.
> >
> > **Chart-independence of the edge transports.** Consider a vertical edge $E_{i,j}$. Its image $H(E_{i,j})$ is connected (continuous image of an interval) and contains the endpoints $x_{i,j}$, $x_{i,j+1}$. If two flat charts $U,U'$ both contain $H(E_{i,j})$, then $H(E_{i,j})$ is a connected subset of $U\cap U'$ containing both endpoints, so $x_{i,j}$ and $x_{i,j+1}$ lie in one connected component of $U\cap U'$; by Lemma 3, $T^{U}_{x_{i,j},x_{i,j+1}}=T^{U'}_{x_{i,j},x_{i,j+1}}$. Hence $\tau_{i,j}$ is well-defined independent of the admissible chart. At least one admissible chart exists: $E_{i,j}$ is an edge of a cell (of $R_{i,j}$ when $i\le N-1$, of $R_{i-1,j}$ when $i=N$), whose chart contains $H(E_{i,j})$. The same argument gives chart-independence of $\sigma_{i,j}$ for horizontal edges. For the boundary rows, $H(F_{i,0})\subseteq H(\{(s,0)\})=\{m\}$ since $H(s,0)\equiv m$, so $x_{i,0}=x_{i+1,0}=m$ and $\sigma_{i,0}=T^{U}_{m,m}=\operatorname{id}_{P_m}$ by Lemma 2(iii); likewise $H(F_{i,N})=\{m'\}$ gives $\sigma_{i,N}=\operatorname{id}_{P_{m'}}$.
> >
> > **The commuting square.** Fix a cell with $0\le i,j\le N-1$ and its chart $U_{i,j}$. All four corners $x_{i,j},x_{i+1,j},x_{i,j+1},x_{i+1,j+1}$ lie in $H(R_{i,j})\subseteq U_{i,j}$. Each of the four bounding edges of $R_{i,j}$ has its image inside $U_{i,j}$ (the edges are subsets of $R_{i,j}$) and is connected, so by chart-independence the four edge transports may all be computed inside the single chart $U_{i,j}$:
> > $$\tau_{i,j}=T^{U_{i,j}}_{x_{i,j},x_{i,j+1}},\quad \tau_{i+1,j}=T^{U_{i,j}}_{x_{i+1,j},x_{i+1,j+1}},\quad \sigma_{i,j}=T^{U_{i,j}}_{x_{i,j},x_{i+1,j}},\quad \sigma_{i,j+1}=T^{U_{i,j}}_{x_{i,j+1},x_{i+1,j+1}}.$$
> > (For $\tau_{i+1,j}$ and $\sigma_{i,j+1}$ this uses Lemma 3: those edges are shared with the neighbouring cells $R_{i+1,j}$ and $R_{i,j+1}$, but their transports agree when computed in $U_{i,j}$.) Now apply the composition law Lemma 2(iii) inside $U_{i,j}$ to the two routes from $x_{i,j}$ to the opposite corner $x_{i+1,j+1}$:
> > $$\sigma_{i,j+1}\circ\tau_{i,j}=T^{U_{i,j}}_{x_{i,j+1},x_{i+1,j+1}}\circ T^{U_{i,j}}_{x_{i,j},x_{i,j+1}}=T^{U_{i,j}}_{x_{i,j},x_{i+1,j+1}}\qquad\text{(route }x_{i,j}\to x_{i,j+1}\to x_{i+1,j+1}\text{),}$$
> > $$\tau_{i+1,j}\circ\sigma_{i,j}=T^{U_{i,j}}_{x_{i+1,j},x_{i+1,j+1}}\circ T^{U_{i,j}}_{x_{i,j},x_{i+1,j}}=T^{U_{i,j}}_{x_{i,j},x_{i+1,j+1}}\qquad\text{(route }x_{i,j}\to x_{i+1,j}\to x_{i+1,j+1}\text{).}$$
> > Both equal $T^{U_{i,j}}_{x_{i,j},x_{i+1,j+1}}$, so $\sigma_{i,j+1}\circ\tau_{i,j}=\tau_{i+1,j}\circ\sigma_{i,j}$, which is ($\star$). $\blacksquare$

> [!note]- Lemma 5: Every continuous loop is path-homotopic to a piecewise smooth one
> **Statement:** Let $c\colon[0,1]\to M$ be a continuous loop at $m$ (so $c(0)=c(1)=m$). Then there is a piecewise smooth loop $c'$ at $m$ with $c\simeq c'$ relative to $\{0,1\}$. The same holds for continuous paths from $m$ to $m'$, rel endpoints.
>
> **Hint:** Cut $[0,1]$ into arcs each mapping into a convex coordinate ball, replace each arc by the coordinate straight segment, and interpolate by straight lines in the chart.
>
> **Why needed:** Holonomy $\operatorname{hol}_p$ is defined only for piecewise smooth loops, but classes in $\pi_1(M,m)$ are represented by continuous loops; this lets the monodromy map be defined on all of $\pi_1$.
>
> > [!note]- Full proof
> > **Choose convex charts.** Every point of $M$ has a coordinate chart whose image is an open ball in $\mathbb{R}^n$ (shrink any chart to a coordinate ball); a ball is convex, so any two of its points are joined by the coordinate straight segment, which stays in the ball. Let $\{V_\beta\}$ be the cover of $M$ by such convex coordinate charts, with coordinate maps $\phi_\beta\colon V_\beta\to\phi_\beta(V_\beta)\subseteq\mathbb{R}^n$ onto convex open sets.
> >
> > **Subdivide the loop.** The sets $\{c^{-1}(V_\beta)\}$ cover the compact interval $[0,1]$; by Lemma 1 there is a Lebesgue number, and we choose a partition $0=t_0<t_1<\cdots<t_N=1$ with each mesh $t_{k+1}-t_k$ below it, so that $c([t_k,t_{k+1}])\subseteq V_{\beta(k)}$ for some convex chart $V_{\beta(k)}$.
> >
> > **Replace each arc by a straight segment.** For each $k$ define $c'|_{[t_k,t_{k+1}]}$ to be the curve whose $\phi_{\beta(k)}$-coordinate is the affine segment
> > $$\phi_{\beta(k)}\big(c'(t)\big)=\frac{t_{k+1}-t}{t_{k+1}-t_k}\,\phi_{\beta(k)}(c(t_k))+\frac{t-t_k}{t_{k+1}-t_k}\,\phi_{\beta(k)}(c(t_{k+1})),\qquad t\in[t_k,t_{k+1}],$$
> > which lies in $\phi_{\beta(k)}(V_{\beta(k)})$ by convexity; thus $c'(t)\in V_{\beta(k)}$. This $c'|_{[t_k,t_{k+1}]}$ is smooth, agrees with $c$ at the junctions $c'(t_k)=c(t_k)$ and $c'(t_{k+1})=c(t_{k+1})$, so the pieces glue to a piecewise smooth curve $c'$ with $c'(0)=c(0)=m$ and $c'(1)=c(1)$ (equal to $m$ for a loop, to $m'$ for a path).
> >
> > **Build the homotopy.** On each subinterval define $H_k\colon[0,1]\times[t_k,t_{k+1}]\to M$ by straight-line interpolation in coordinates,
> > $$\phi_{\beta(k)}\big(H_k(u,t)\big)=(1-u)\,\phi_{\beta(k)}(c(t))+u\,\phi_{\beta(k)}(c'(t)),$$
> > which lies in the convex set $\phi_{\beta(k)}(V_{\beta(k)})$, so $H_k(u,t)\in V_{\beta(k)}$ is defined and continuous. At the junction $t=t_k$ both $c$ and $c'$ take the value $c(t_k)$, so $H_k(u,t_k)=c(t_k)$ for all $u$, and likewise $H_{k-1}(u,t_k)=c(t_k)$; hence the $H_k$ agree on the shared parameter lines and glue to a continuous $H\colon[0,1]\times[0,1]\to M$ with $H(0,\cdot)=c$, $H(1,\cdot)=c'$. Finally $H(u,0)=c(0)=m$ and $H(u,1)=c(1)$ are independent of $u$ (the endpoints are fixed under each straight-line interpolation since $c,c'$ agree there), so $H$ is a homotopy rel endpoints. Therefore $c\simeq c'$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\omega$ be flat on $P\to M$.
>
> **Step 0 — a cover by flat charts.** Because $\omega$ is flat, [[Thm - Local Triviality of Flat Connections]] provides, around every point of $M$, a connected open set on which a flat gauge $s$ with $s^*\omega=0$ exists (clause (c) of that theorem; shrink each to a connected set if necessary, and a flat gauge restricts to any connected open subset). Fix such a cover $\{U_\alpha\}$ of $M$ by connected flat charts. All transports $T^U_{x,y}$ below refer to these charts and are governed by Lemma 2.
>
> **Part I — homotopy invariance: $\Gamma(c_0)=\Gamma(c_1)$.**
>
> Let $H\colon I\times I\to M$ be the given homotopy rel endpoints, $H(0,\cdot)=c_0$, $H(1,\cdot)=c_1$, $H(s,0)\equiv m$, $H(s,1)\equiv m'$. Apply Lemma 4 to $H$ and the cover $\{U_\alpha\}$: we obtain $N$, the grid points $x_{i,j}=H(i/N,j/N)$, the edge transports $\tau_{i,j}$ (vertical edges) and $\sigma_{i,j}$ (horizontal edges), the boundary identities $\sigma_{i,0}=\operatorname{id}_{P_m}$, $\sigma_{i,N}=\operatorname{id}_{P_{m'}}$, and the commuting square ($\star$).
>
> **Row transports.** For $0\le i\le N$ define the composite of the vertical-edge transports across row $i$,
> $$\Theta_i:=\tau_{i,N-1}\circ\tau_{i,N-2}\circ\cdots\circ\tau_{i,1}\circ\tau_{i,0}\;\colon\;P_{x_{i,0}}\longrightarrow P_{x_{i,N}},$$
> which is a map $P_m\to P_{m'}$ because $x_{i,0}=H(i/N,0)=m$ and $x_{i,N}=H(i/N,1)=m'$.
>
> **Claim A: $\Theta_0=\Gamma(c_0)$ and $\Theta_N=\Gamma(c_1)$.** The bottom row is the path $c_0$: for $0\le j\le N-1$, the restriction $c_0|_{[j/N,(j+1)/N]}$ is a piecewise smooth curve from $x_{0,j}$ to $x_{0,j+1}$ whose image lies in the chart of the cell $R_{0,j}$ (indeed $c_0(t)=H(0,t)$ and $\{0\}\times[j/N,(j+1)/N]=E_{0,j}\subseteq R_{0,j}$, so $c_0([j/N,(j+1)/N])\subseteq H(R_{0,j})\subseteq U_{0,j}$). By Lemma 2(ii) route-independence, parallel transport along this arc equals the endpoint transport,
> $$\Gamma\big(c_0|_{[j/N,(j+1)/N]}\big)=T^{U_{0,j}}_{x_{0,j},x_{0,j+1}}=\tau_{0,j}\qquad\text{(Lemma 4 chart-independence of }\tau_{0,j}\text{).}$$
> Parallel transport turns concatenation of curves into composition of transports (property (4) of [[Thm - Properties of Parallel Transport]]: $\Gamma(d_2\ast d_1)=\Gamma(d_2)\circ\Gamma(d_1)$, and $\Gamma$ is unchanged under reparametrisation, its properties (1)–(2)); writing $c_0$ as the concatenation of its $N$ arcs,
> $$\Gamma(c_0)=\Gamma\big(c_0|_{[(N-1)/N,1]}\big)\circ\cdots\circ\Gamma\big(c_0|_{[0,1/N]}\big)=\tau_{0,N-1}\circ\cdots\circ\tau_{0,0}=\Theta_0.$$
> The identical argument with $c_1(t)=H(1,t)$ and the cells $R_{N-1,j}$ gives $\Gamma(c_1)=\Theta_N$, proving Claim A.
>
> **Claim B: $\Theta_i=\Theta_{i+1}$ for every $0\le i\le N-1$.** We show $\sigma_{i,N}\circ\Theta_i=\Theta_{i+1}\circ\sigma_{i,0}$ by telescoping ($\star$) from the right end of the row to the left. Starting from $\sigma_{i,N}\circ\Theta_i$ and inserting the definition of $\Theta_i$,
> $$\sigma_{i,N}\circ\tau_{i,N-1}\circ\tau_{i,N-2}\circ\cdots\circ\tau_{i,0}.$$
> Apply ($\star$) with $j=N-1$, namely $\sigma_{i,N}\circ\tau_{i,N-1}=\tau_{i+1,N-1}\circ\sigma_{i,N-1}$, to rewrite the leftmost pair:
> $$=\tau_{i+1,N-1}\circ\sigma_{i,N-1}\circ\tau_{i,N-2}\circ\cdots\circ\tau_{i,0}.$$
> Apply ($\star$) with $j=N-2$, $\sigma_{i,N-1}\circ\tau_{i,N-2}=\tau_{i+1,N-2}\circ\sigma_{i,N-2}$, to the pair $\sigma_{i,N-1}\circ\tau_{i,N-2}$:
> $$=\tau_{i+1,N-1}\circ\tau_{i+1,N-2}\circ\sigma_{i,N-2}\circ\tau_{i,N-3}\circ\cdots\circ\tau_{i,0}.$$
> Continuing to apply ($\star$) with $j=N-3,\dots,1,0$ in turn — each step moves one $\tau_{i,\,\cdot}$ from the $i$-th row to the $(i+1)$-th while sliding the $\sigma$ one column to the left — we reach after $N$ steps
> $$=\tau_{i+1,N-1}\circ\tau_{i+1,N-2}\circ\cdots\circ\tau_{i+1,0}\circ\sigma_{i,0}=\Theta_{i+1}\circ\sigma_{i,0}.$$
> Thus $\sigma_{i,N}\circ\Theta_i=\Theta_{i+1}\circ\sigma_{i,0}$. Now invoke the boundary identities from Lemma 4: $\sigma_{i,N}=\operatorname{id}_{P_{m'}}$ and $\sigma_{i,0}=\operatorname{id}_{P_m}$. Hence $\Theta_i=\Theta_{i+1}$, proving Claim B.
>
> **Conclusion of Part I.** Combining Claims A and B along the chain of rows,
> $$\Gamma(c_0)\overset{\text{A}}{=}\Theta_0\overset{\text{B}}{=}\Theta_1\overset{\text{B}}{=}\cdots\overset{\text{B}}{=}\Theta_N\overset{\text{A}}{=}\Gamma(c_1).$$
> Therefore $\Gamma(c_0)=\Gamma(c_1)\colon P_m\to P_{m'}$, and this used only that $H$ is continuous. This proves the theorem.
>
> **Part II — the monodromy representation (Corollary).** Fix $p\in P_m$.
>
> **Step 1 — $\operatorname{hol}_p$ is defined on every homotopy class, and depends only on the class.** For a piecewise smooth loop $c$ at $m$, $\operatorname{hol}_p(c)\in G$ is defined by $\Gamma(c)(p)=p\cdot\operatorname{hol}_p(c)$ (see [[Def - Holonomy Group of a Connection]]; the element exists and is unique because the $G$-action is free and transitive on $P_m$). If $a,b$ are piecewise smooth loops at $m$ with $a\simeq b$ rel $\{0,1\}$, then by Part I $\Gamma(a)=\Gamma(b)$, so $p\cdot\operatorname{hol}_p(a)=\Gamma(a)(p)=\Gamma(b)(p)=p\cdot\operatorname{hol}_p(b)$, and cancelling the free action gives $\operatorname{hol}_p(a)=\operatorname{hol}_p(b)$. By Lemma 5 every class $[c]\in\pi_1(M,m)$ contains a piecewise smooth loop, and any two piecewise smooth loops in the same class are (continuously) homotopic rel base point, so $\operatorname{hol}_p$ takes a single value on each class. Define $\rho_\omega([c]):=\operatorname{hol}_p(c)^{-1}$ for any piecewise smooth representative $c$; this is well-defined.
>
> **Step 2 — the composition law of holonomy.** Let $a,b$ be piecewise smooth loops at $m$; their path-product $a\cdot b$ (traverse $a$, then $b$) is again piecewise smooth. Parallel transport reverses concatenation (property (4) of [[Thm - Properties of Parallel Transport]]): $\Gamma(a\cdot b)=\Gamma(b)\circ\Gamma(a)$. Compute the holonomy of $a\cdot b$ at $p$:
> $$p\cdot\operatorname{hol}_p(a\cdot b)=\Gamma(a\cdot b)(p)=\Gamma(b)\big(\Gamma(a)(p)\big)=\Gamma(b)\big(p\cdot\operatorname{hol}_p(a)\big)\qquad\text{(definition of }\operatorname{hol}_p(a)\text{).}$$
> By the equivariance of parallel transport, $\Gamma(c)\circ R_g=R_g\circ\Gamma(c)$ (property (5) of [[Thm - Properties of Parallel Transport]]), the right-hand side equals
> $$\Gamma(b)(p)\cdot\operatorname{hol}_p(a)=\big(p\cdot\operatorname{hol}_p(b)\big)\cdot\operatorname{hol}_p(a)=p\cdot\big(\operatorname{hol}_p(b)\,\operatorname{hol}_p(a)\big).$$
> Cancelling the free action of $p$ gives the composition law
> $$\operatorname{hol}_p(a\cdot b)=\operatorname{hol}_p(b)\,\operatorname{hol}_p(a),$$
> so the raw map $c\mapsto\operatorname{hol}_p(c)$ reverses order (it is an anti-homomorphism), as anticipated in the Convention callout.
>
> **Step 3 — $\rho_\omega$ is a homomorphism.** Take classes $[a],[b]\in\pi_1(M,m)$ with piecewise smooth representatives $a,b$; then $a\cdot b$ represents $[a][b]$ (the group law of [[Thm - The Fundamental Group is a Group]] and [[Def - Path-Product and the Fundamental Group]]). Using Step 1 (well-definedness), Step 2, and the anti-automorphism identity $(xy)^{-1}=y^{-1}x^{-1}$ in $G$,
> $$\rho_\omega([a][b])=\rho_\omega([a\cdot b])=\operatorname{hol}_p(a\cdot b)^{-1}=\big(\operatorname{hol}_p(b)\,\operatorname{hol}_p(a)\big)^{-1}=\operatorname{hol}_p(a)^{-1}\,\operatorname{hol}_p(b)^{-1}=\rho_\omega([a])\,\rho_\omega([b]).$$
> The identity class $[c_m]$ (constant loop) has $\Gamma(c_m)=\operatorname{id}$ (property (1) of [[Thm - Properties of Parallel Transport]]), so $\operatorname{hol}_p(c_m)=e$ and $\rho_\omega([c_m])=e$. Hence $\rho_\omega\colon\pi_1(M,m)\to G$ is a group homomorphism.
>
> **Step 4 — dependence on the point $p$.** Let $g\in G$ and consider the base point $p\cdot g\in P_m$. For any loop $c$ at $m$,
> $$\Gamma(c)(p\cdot g)=\Gamma(c)(p)\cdot g=\big(p\cdot\operatorname{hol}_p(c)\big)\cdot g=(p\cdot g)\cdot\big(g^{-1}\operatorname{hol}_p(c)\,g\big),$$
> using equivariance (property (5)) then the definition of $\operatorname{hol}_p$; comparing with $\Gamma(c)(p\cdot g)=(p\cdot g)\cdot\operatorname{hol}_{p\cdot g}(c)$ and cancelling the free action gives $\operatorname{hol}_{p\cdot g}(c)=g^{-1}\operatorname{hol}_p(c)\,g$. Therefore
> $$\rho_{\omega,\,p\cdot g}([c])=\operatorname{hol}_{p\cdot g}(c)^{-1}=g^{-1}\operatorname{hol}_p(c)^{-1}g=g^{-1}\rho_{\omega,p}([c])\,g,$$
> so changing the point of $P_m$ conjugates the representation by the corresponding $g$; the conjugacy class $[\rho_\omega]$ is therefore independent of the choice of $p\in P_m$.
>
> **Step 5 — the vector-bundle version.** Let $E=P\times_\rho V$ be associated to $P$ by a representation $\rho\colon G\to GL(V)$, with its induced connection $\nabla$ (see [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles]]). Parallel transport in $E$ along a curve $c$ is $PT_c([q,v])=[\Gamma(c)(q),v]$ for $q\in P_{c(0)}$, $v\in V$ (a linear isomorphism $E_{c(0)}\to E_{c(1)}$, [[Def - Parallel Transport in a Principal Bundle]]). If $c_0\simeq c_1$ rel endpoints, then $\Gamma(c_0)=\Gamma(c_1)$ by Part I, whence $PT_{c_0}=PT_{c_1}$; so parallel transport in $E$ also depends only on the homotopy class. Defining $\rho_\nabla([c]):=PT_c^{-1}\in GL(E_m)$ and repeating Steps 1–4 verbatim with $PT$ in place of $\Gamma$ (using that $PT$ composes and is functorial in the same way) yields a homomorphism $\rho_\nabla\colon\pi_1(M,m)\to GL(E_m)$; for $E$ of rank $k$ a choice of basis of $E_m$ identifies it with a homomorphism $\pi_1(M,m)\to GL_k(\mathbb{R})$, which is Haydys's monodromy representation $\rho_A$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Covering-space theory: monodromy of a locally constant sheaf.** A locally constant sheaf (local system) of vector spaces on $M$ is the same data as a representation of $\pi_1(M,m)$, and the theorem is the differential-geometric incarnation of that equivalence: the flat bundle $E$ with connection $\nabla$ is the local system whose stalk is $E_m$ and whose monodromy is $\rho_\nabla$. The theorem applies because the sheaf's transition data is locally constant, hence the associated connection is flat; the exercise — reconstruct the local system from a loop's transport — is non-obvious because it identifies a topological gluing (the sheaf) with an analytic one (parallel transport of a flat connection).

**Ordinary differential equations: monodromy of a Fuchsian system.** A linear system $\frac{dy}{dz}=A(z)y$ on a punctured Riemann surface, with $A$ holomorphic, defines a flat connection $d-A\,dz$ on the trivial bundle over the complement of the singular points; its solutions are the flat (parallel) sections, and continuing a solution around a loop encircling a puncture multiplies it by the *monodromy matrix* $\rho_\nabla([c])^{\pm1}$. The theorem applies because the connection is flat away from the punctures (the system is integrable there), and it explains why monodromy depends only on which punctures a loop encloses and how — the homotopy class in the punctured surface — not on the exact contour. The non-obvious content is that the highly analytic operation "analytically continue a solution" is a topological invariant.

**Condensed-matter physics: the Aharonov–Bohm and Berry phases.** For a charged quantum particle confined outside a solenoid, the electromagnetic potential is a flat $U(1)$-connection in the field-free region, and the phase acquired on a closed path is its holonomy; the theorem says this phase is a homotopy invariant of the path, so it detects the *topology* of the excluded region (how many times the path winds the solenoid) rather than any local field. More generally, adiabatic transport of a quantum state around a loop in parameter space, when the relevant Berry connection is flat, produces a geometric phase depending only on the loop's class. The application is non-obvious because a measurable physical phase is being certified as a purely topological quantity, invisible to any local measurement.

---

# Bridges

- **[[Thm - Local Triviality of Flat Connections]]** — the local half. That theorem says flatness makes parallel transport route-independent *inside a chart*; the present theorem is the global upgrade, replacing "inside a chart" by "within a homotopy class". Its parallel-transport clause is literally the content of Lemma 2 here, and its (c)$\Rightarrow$(d) implication (two flat gauges differ by a locally constant transition) is the content of Lemma 3. The grid argument is exactly the device that promotes the local statement to the global one, with the fundamental group appearing as the precise measure of how many charts one must cross.

- **[[Thm - Flat Connections and Monodromy Representations of the Fundamental Group]]** — the completion of the dictionary. The present theorem produces a homomorphism $\rho_\omega$ from a flat connection; that theorem shows the assignment $\omega\mapsto[\rho_\omega]$ is a *bijection* between the moduli space of flat connections and the representation variety $\mathcal{R}(M;G)=\operatorname{Hom}(\pi_1(M,m),G)/\mathrm{conjugation}$, by constructing an inverse (the associated bundle $\tilde M\times_\rho G$ of a representation) via the universal cover. Homotopy invariance is the well-definedness that makes the forward map exist at all.

- **[[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group]]** — the geometric model behind the algebra. The monodromy homomorphism can be read as the action of $\pi_1$ on the fibre $P_m$ obtained by transporting along loops; the universal cover $\tilde M$, whose points are homotopy classes of paths from $m$, is the space on which this transport becomes single-valued, and the deck action realises $\rho_\omega$ concretely. This is why the next theorem builds the flat bundle of a representation as an associated bundle of $\tilde M$.

- **[[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral]]** — the abelian special case seen through curvature. When $G$ is abelian and a loop bounds a surface inside a trivialising set, holonomy is $\exp(-\int_S F)$; for a flat connection $F=0$, so a null-homotopic loop has trivial holonomy — exactly the specialisation of the present theorem to the constant class, now with the flux integral making the vanishing visible.

- **[[Def - Simply Connected Space]]** — the degenerate case. If $M$ is simply connected, $\pi_1(M,m)$ is trivial, so $\rho_\omega$ is trivial and every loop has holonomy $e$; combined with the monodromy correspondence this shows every flat connection over a simply connected base is gauge-equivalent to the product connection. The theorem thus explains why non-trivial flat connections are a phenomenon of non-simply-connected spaces.

---

# Unlocked by This

> [!tip] The representation variety as a moduli space *(from Gauge Theory / Geometric Representation Theory)*
> Because $\rho_\omega$ depends only on the conjugacy class $[\rho_\omega]$ and (as the next theorem shows) captures the flat connection up to gauge, the moduli space of flat connections is identified with $\mathcal{R}(M;G)=\operatorname{Hom}(\pi_1(M,m),G)/\mathrm{conjugation}$. For a closed surface this is the character variety, the central object of two-dimensional gauge theory and the geometric Langlands programme. See **Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact**.

> [!tip] Flat bundles as bundles with discrete structure group *(from Topology)*
> A flat connection is equivalent to a reduction of the structure group of $P$ to the discrete group underlying $G$: the monodromy $\rho_\omega\colon\pi_1(M,m)\to G$ factors the bundle through the universal cover, exhibiting $P$ as glued from locally constant data. This is the bridge to the classification of flat bundles by cohomology with coefficients in the (discrete) group, and to characteristic classes of flat bundles.
