---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Principal Bundles are Classified by Cocycles"
  - "Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles"
  - "Def - Transition Functions and the Cocycle Condition"
  - "Def - Principal G-Bundle"
  - "Thm - Sections of a Principal Bundle and Triviality"
  - "Def - Sphere Bundles and Mapping Tori"
  - "Thm - The Mapping Torus of a Diffeomorphism is a Fibre Bundle over the Circle"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $X$ is a **closed** (compact without boundary) connected smooth $n$-manifold, $G$ is a [[Def - Lie Group|Lie group]] with identity $e$, and $\Gamma(\cdot)$, right actions, and transition functions are as in the standing series conventions: $G$ acts on a [[Def - Principal G-Bundle|principal G-bundle]] $\pi\colon P\to X$ on the **right**, $R_h(p)=p\cdot h$, freely and transitively on each fibre $P_x:=\pi^{-1}(x)$; a **local section** over an open $U\subseteq X$ is a smooth $s\colon U\to P$ with $\pi\circ s=\operatorname{id}_U$; and for two sections $s_\alpha,s_\beta$ over an overlap the **transition function** $g_{\alpha\beta}\colon U_\alpha\cap U_\beta\to G$ is the unique smooth map with $s_\beta=s_\alpha\cdot g_{\alpha\beta}$, established on [[Def - Transition Functions and the Cocycle Condition]]. A principal bundle is **trivial** if it is isomorphic (over $\operatorname{id}_X$) to $X\times G$; equivalently, by [[Thm - Sections of a Principal Bundle and Triviality|the section–triviality theorem]], if it admits a global smooth section. All isomorphisms of principal bundles below cover $\operatorname{id}_X$ unless stated otherwise.

**The coordinate disc and its collar.** A **closed coordinate disc** $D\subseteq X$ is the image $D=\varphi(\overline{B}_1)$ of the closed unit ball under a chart
$$\varphi\colon B_2\longrightarrow X,\qquad B_\rho:=\{u\in\mathbb{R}^n:\lvert u\rvert<\rho\},$$
a diffeomorphism onto an open set $V=\varphi(B_2)\subseteq X$; here $\overline{B}_1=\{\lvert u\rvert\le1\}$. We write $D^\circ=\varphi(B_1)$ for its interior, $S:=\partial D=\varphi(\Sigma)$ for its boundary, where $\Sigma:=\{u\in\mathbb{R}^n:\lvert u\rvert=1\}\cong S^{n-1}$, and $x_0:=\varphi(0)$ for its centre. Because $D$ is a round ball in the chart, the boundary sphere $S$ carries an **explicit collar**: the radial coordinate $u\mapsto\lvert u\rvert$ furnishes, for any $\varepsilon\in(0,1)$, the diffeomorphism $\Sigma\times(1-\varepsilon,1+\varepsilon)\to\varphi\big(\{1-\varepsilon<\lvert u\rvert<1+\varepsilon\}\big)$, $(w,\rho)\mapsto\varphi(\rho w)$, whose central slice $\rho=1$ is $S$.

**The two-set cover.** Fix a real number $\delta\in(0,1)$, taken small when needed (see the callout below), and set
$$U_O:=X\setminus\varphi(\overline{B}_{1-\delta}),\qquad U_D:=\varphi(B_{1+\delta}).$$
Both are open; $U_D$ is a coordinate ball, hence diffeomorphic to $\mathbb{R}^n$ and **contractible**. We have $U_O\supseteq X\setminus D^\circ$ (since $\overline{B}_{1-\delta}\subseteq B_1$), $U_D\supseteq D$, and $U_O\cup U_D=X$ (as $U_D\supseteq\varphi(\overline{B}_{1-\delta})$, whose complement is $U_O$); note $x_0=\varphi(0)\notin U_O$. Their overlap is the open **spherical shell**
$$\Sigma_\delta:=U_O\cap U_D=\varphi(A_\delta),\qquad A_\delta:=\{u\in\mathbb{R}^n:1-\delta<\lvert u\rvert<1+\delta\}.$$

**The radial retraction.** Define $r\colon\Sigma_\delta\to S$ and its deformation
$$r(\varphi(u)):=\varphi\!\left(\frac{u}{\lvert u\rvert}\right),\qquad r_\tau(\varphi(u)):=\varphi\!\left((1-\tau)\,u+\tau\,\frac{u}{\lvert u\rvert}\right)\quad(\tau\in[0,1]).$$
These are smooth on $\Sigma_\delta$ because $u\ne0$ there. The norm of $(1-\tau)u+\tau u/\lvert u\rvert$ equals $(1-\tau)\lvert u\rvert+\tau$, a convex combination of $\lvert u\rvert\in(1-\delta,1+\delta)$ and $1\in(1-\delta,1+\delta)$, hence again in $(1-\delta,1+\delta)$; so $r_\tau$ maps $\Sigma_\delta$ into $\Sigma_\delta$, with $r_0=\operatorname{id}_{\Sigma_\delta}$ and $r_1=\iota_S\circ r$, where $\iota_S\colon S\hookrightarrow\Sigma_\delta$ is the inclusion. Thus $r_\tau$ is a smooth deformation retraction of $\Sigma_\delta$ onto $S$, and $r$ restricts to the identity on $S$ (for $\lvert u\rvert=1$, $u/\lvert u\rvert=u$).

**Clutching maps.** A **clutching map** is a smooth map $g\colon S\to G$. Its **collar extension** is the smooth map $\hat g:=g\circ r\colon\Sigma_\delta\to G$, constant along radii, with $\hat g|_S=g$. Given a smooth $c\colon\Sigma_\delta\to G$, we write $P(c)$ for the principal $G$-bundle reconstructed from the two-set cocycle it determines (defined in Lemma 1), and abbreviate the **clutching bundle** of $g$ by $P_g:=P(\hat g)$.

> [!warning] Convention: the transition-function placement and the meaning of "trivial over a closed region"
> We use the series convention $s_\beta=s_\alpha\cdot g_{\alpha\beta}$ of [[Def - Transition Functions and the Cocycle Condition]]; a source writing $s_\alpha=s_\beta\cdot g_{\alpha\beta}$ obtains our $g_{\alpha\beta}$ as its $g_{\beta\alpha}$. Throughout, "$P$ is **trivial over the closed region** $C$" ($C=X\setminus D^\circ$ or $C=D$) means $P$ is trivial over some open set $W\supseteq C$; equivalently $P$ admits a section smooth on an open neighbourhood of $C$. Whenever such a hypothesis is present we shrink $\delta$ so that $U_O\subseteq W_O$ and $U_D\subseteq W_D$ for the ambient trivialising neighbourhoods $W_O\supseteq X\setminus D^\circ$, $W_D\supseteq D$; this is possible because $S$ and $D$ are compact and $W_O,W_D$ are open (an open neighbourhood of the compact $S$ contains the thin inner shell $\varphi(\{1-\delta<\lvert u\rvert\le1\})$ for all small $\delta$, and $U_D\subseteq W_D$ for all small $\delta$ since $D$ is compact). The isomorphism class of $P_g$ does not depend on $\delta$: this is Lemma 3 applied to the two collar extensions of the same $g$ for two radii.

The full symbol registry for the chapter is on the parent page **Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles**.

---

# Statement

> **Theorem (clutching construction over a closed manifold).** Let $X$ be a closed connected smooth $n$-manifold, $D=\varphi(\overline{B}_1)\subseteq X$ a closed coordinate disc with interior $D^\circ$, boundary $S=\partial D\cong S^{n-1}$, and centre $x_0=\varphi(0)$, and let $G$ be a Lie group. With the cover $\{U_O,U_D\}$ and the collar extension $\hat g=g\circ r$ of a clutching map fixed above:
>
> **(a) Construction.** For every smooth clutching map $g\colon S\to G$ there is a principal $G$-bundle $P_g\to X$, trivial over $X\setminus D^\circ$ and over $D$, whose transition function from its canonical section over $U_O$ to its canonical section over $U_D$ is $\hat g=g\circ r$; in particular that transition function restricts on $S$ to $g$.
>
> **(b) Every such bundle is a clutching bundle.** If a principal $G$-bundle $P\to X$ is trivial over $X\setminus D^\circ$ and over $D$, then $P\cong P_g$ for some clutching map $g\colon S\to G$ (namely $g=c|_S$, where $c\colon\Sigma_\delta\to G$ is the transition function of $P$ for the cover $\{U_O,U_D\}$). Moreover, if $G$ is connected and $P$ is trivial over $X\setminus\{x_0\}$, then $P$ is trivial over $X\setminus D^\circ$ and over $D$, and hence $P\cong P_g$.
>
> **(c) Classification.** For clutching maps $g,g'\colon S\to G$,
> $$P_g\cong P_{g'}\quad\Longleftrightarrow\quad g'=(a|_S)\,g\,(b|_S)\ \text{ on }S\ \text{ for some smooth }a\colon X\setminus D^\circ\to G,\ b\colon D\to G.$$
> In particular, if $g$ and $g'$ are smoothly homotopic then $P_g\cong P_{g'}$.
>
> **(d) Triviality criterion.** $P_g$ is trivial if and only if $g=(a|_S)\,(b|_S)$ on $S$ for some smooth $a\colon X\setminus D^\circ\to G$ and $b\colon D\to G$.

> **Corollary (bundles over the sphere).** Let $X=S^n$ with $D$ a closed hemispherical cap, so that both $D$ and $X\setminus D^\circ$ are closed discs and $S\cong S^{n-1}$. Then $g\mapsto P_g$ descends to a bijection from the set $[S^{n-1},G]$ of free homotopy classes of smooth maps $S^{n-1}\to G$ onto the set of isomorphism classes of principal $G$-bundles over $S^n$ that are trivial over the complement of a point; and if $G$ is connected every principal $G$-bundle over $S^n$ is of this form. In particular $P_g$ is trivial if and only if $g$ is null-homotopic.

> **Corollary (mapping tori).** Let $F$ be a smooth manifold and $\phi\colon F\to F$ a diffeomorphism, with mapping torus $\pi\colon E_\phi\to S^1$ of [[Def - Sphere Bundles and Mapping Tori]]. Then $E_\phi$ is trivial as a fibre bundle over $S^1$ **if and only if** $\phi$ is isotopic to $\operatorname{id}_F$ through diffeomorphisms. The "if" is Part II of [[Thm - The Mapping Torus of a Diffeomorphism is a Fibre Bundle over the Circle|the mapping-torus theorem]]; the "only if" is proved here. (The theorem itself is stated for a Lie group $G$; the mapping-torus corollary is the fibre-bundle version with the diffeomorphism group $\operatorname{Diff}(F)$ playing the role of the structure group, and its proof below is direct and does not require $\operatorname{Diff}(F)$ to be a Lie group. Only the Lie-group statements (a)–(d) are claimed at the vault's proof standard.)

---

# Motivation

A principal bundle over a manifold $X$ is a global object, and the two questions one most wants to answer about the collection of all such bundles — *how do I build one with prescribed behaviour?* and *when are two of them the same?* — are, phrased for total spaces, questions about constructing and comparing manifolds-with-group-action by hand. The [[Thm - Principal Bundles are Classified by Cocycles|cocycle classification]] already reduces these to bookkeeping about $G$-valued functions on overlaps, but for a general cover that bookkeeping is still unbounded: arbitrarily many patches, arbitrarily many transition functions, an arbitrary coboundary equivalence. The clutching construction is the observation that for a bundle which is trivial away from a single disc — which, as §3.5 and §3.6 show, is the generic situation for the bundles gauge theory actually cares about — the entire cocycle collapses to **one** map $g\colon S^{n-1}\to G$ on the boundary sphere of that disc, and the coboundary equivalence collapses to a concrete relation on that one map. The whole classification problem is thereby transported from the geometry of bundles to the homotopy theory of maps into the structure group.

The problem this solves is the recurring shape of the classification theorems downstream. To classify line bundles over a closed surface, or $SU(2)$-bundles over a closed four-manifold, one first shows (using generic sections and the [[Thm - Homogeneity Lemma for Connected Manifolds|homogeneity lemma]]) that the bundle is trivial off a small disc; the clutching construction then says the bundle is $P_g$ for a boundary map $g$, and that its isomorphism class is a homotopy invariant of $g$. Everything that remains — computing $\pi_1(U(1))=\mathbb{Z}$, or $\pi_3(SU(2))=\mathbb{Z}$, and matching the resulting integer to a degree or a Chern number — is downstream of the single reduction performed here. Without clutching, each classification would have to wrangle a full cocycle; with it, each becomes a homotopy computation in the group.

There is a second reading, the one that makes the construction inevitable. A bundle trivial over $D$ and over $X\setminus D^\circ$ is two trivial pieces, $U_O\times G$ and $U_D\times G$, that agree away from a collar of $S$ and must be told how to be glued across it. Telling them is exactly naming a map on the collar valued in $G$; but the collar deformation-retracts onto $S$, so up to homotopy the gluing datum is a map on $S$ alone. Changing the trivialisation over the outer piece by $a$ and over the disc by $b$ changes the datum by $g\mapsto(a|_S)g(b|_S)$, and nothing else can change it. Part (c) is the precise statement that this is the only freedom, and part (d) is the statement that the trivial bundle is exactly the one whose gluing datum can be so absorbed. The construction is not a trick; it is the cocycle classification read off the smallest cover that a "trivial-off-a-disc" bundle admits.

The reader is assumed to know the [[Thm - Principal Bundles are Classified by Cocycles|cocycle classification]] (reconstruction from a cocycle, and the fact that cohomologous cocycles classify bundles up to isomorphism on a fixed cover) and [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|the homotopy-invariance theorem]] (a bundle over $X\times[0,1]$ restricts isomorphically to the two ends; a bundle over a contractible manifold is trivial). Both are recalled at their points of use.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis of the construction is a single smooth map $g\colon S^{n-1}\to G$, so the skill is recognising when a geometric problem secretly presents such a boundary map or a "trivial-off-a-disc" bundle.

The first disguised source is **a bundle with a section that vanishes, or fails to be defined, only on a small set**. If a rank-$r$ real or complex bundle admits a section transverse to the zero section (which the [[Thm - Generic Sections are Transverse to the Zero Section|generic-sections theorem]] guarantees), its zero set is a submanifold of codimension $r$; when $r$ exceeds the base dimension the zero set is empty and the bundle is trivial, and when the zero set is finite the [[Thm - Homogeneity Lemma for Connected Manifolds|homogeneity lemma]] slides all the zeros into one coordinate disc $D$. The bundle is then trivial over $X\setminus D^\circ$ (the normalised nowhere-zero section) and over the contractible $D$, so part (b) presents it as a clutching bundle. The non-obvious bridge is that "a section with finitely many zeros" is exactly the hypothesis "trivial off a disc" once the zeros are gathered. *Example problem:* show that an oriented rank-two real bundle over a closed surface is $P_g$ for a clutching map $S^1\to SO(2)=U(1)$, and read its degree off the winding number of $g$.

The second disguised source is **a bundle over a sphere presented by hemispheres**. Any principal $G$-bundle over $S^n$ restricts to a trivial bundle over each closed hemispherical cap (each is a disc, hence contractible, so triviality is automatic by the homotopy-invariance theorem), and the two trivialisations disagree on the equatorial collar by a single map $S^{n-1}\to G$. The bridge is that the two-set cover by caps has exactly one essential overlap, so the cocycle is one clutching map; this is the source of the identification of bundles over $S^n$ with $\pi_{n-1}(G)$ in the sphere corollary. *Example problem:* classify principal $SU(2)$-bundles over $S^4$ by the clutching map $S^3\to SU(2)$, whose homotopy classes are $\pi_3(SU(2))\cong\mathbb{Z}$, the instanton number.

The third disguised source is **a fibre bundle over the circle, or any mapping torus**. A bundle over $S^1$ is trivial over each of two arcs and glued along the two overlap components by clutching data; concentrating the twist on one arc exhibits it as a mapping torus $E_\phi$, and the mapping-torus corollary tests its triviality against the isotopy class of $\phi$. The bridge is that the clutching datum of a circle bundle is a single monodromy element (a diffeomorphism of the fibre, or a group element in the principal case). *Example problem:* prove that a principal $G$-bundle over $S^1$ with $G$ connected is trivial, because its clutching datum is a map $S^0\to G$ whose two values lie in the connected $G$ and are therefore joined to $e$.

**Targets (Output Amplification)**

Combine part (c) with **a computation of a homotopy group of $G$**. Once the sphere corollary identifies bundles over $S^n$ with $[S^{n-1},G]$, any calculation of $\pi_{n-1}(G)$ becomes a complete count of bundles. The extra ingredient is the homotopy group; the payoff is a classification: $\pi_0(G)$ counts bundles over $S^1$, $\pi_1(U(1))=\mathbb{Z}$ counts line bundles over $S^2$, $\pi_3(SU(2))=\mathbb{Z}$ counts $SU(2)$-bundles over $S^4$.

Combine part (c) with **an invariant of the clutching map that is stable under $g\mapsto(a|_S)g(b|_S)$**. A functional of $g$ unchanged by left multiplication by a boundary value extending over $X\setminus D^\circ$ and right multiplication by one extending over $D$ is a bundle invariant. The extra ingredient is such a functional — a degree, a winding number, an integral of $\operatorname{tr}((g^{-1}dg)^{\wedge3})$ — and the payoff is a numerical isomorphism invariant, the engine of the degree and Chern-number pages of §3.6.

Combine part (d) with **the extendability of the clutching map over the outer region**. When $X\setminus D^\circ$ is itself contractible (as for $X=S^n$) both $a|_S$ and $b|_S$ are null-homotopic, so triviality is exactly null-homotopy of $g$; for general $X$ the criterion measures instead whether $g$ factors as a product of a map extending inward over the disc and one extending outward over the complement. The extra ingredient is the topology of $X\setminus D^\circ$, and the payoff is the precise obstruction to triviality, refined per base manifold.

---

# Why Is It True

Forget the total spaces and picture the two trivial slabs. Over the closed complement $X\setminus D^\circ$ the bundle is $(X\setminus D^\circ)\times G$; over the disc $D$ it is $D\times G$. These two product pieces are supposed to be the same bundle, so along the boundary $S$ where they meet, a point $(x,h)$ of the outer slab and a point $(x,h')$ of the inner slab must be declared equal according to some smoothly varying group rule $h=g(x)h'$. That rule is the clutching map $g\colon S\to G$, and it is the *entire* content of the bundle: two trivial pieces plus one instruction for gluing them.

> **The mechanism in one sentence: a bundle that is trivial off a disc is two trivial pieces glued along a collar of the boundary sphere, the glue is a single map $g\colon S^{n-1}\to G$, and the only freedom in $g$ is to re-choose the trivialisation of each piece — which multiplies $g$ on the left by a boundary value from outside and on the right by one from the disc.**

Part (a) is the statement that any such instruction can be carried out: form the two trivial pieces on the open cover $\{U_O,U_D\}$, glue them across the collar $\Sigma_\delta$ by the collar extension $\hat g=g\circ r$, and the cocycle classification manufactures the bundle. The retraction $r$ is doing exactly one thing: it turns a map defined only on $S$ into a map on the two-dimensional-worth-of-collar overlap that a cocycle needs, without adding information, because it is constant along the radial direction the collar contributes.

Parts (b), (c), (d) are then homotopy statements read off one lemma: on the two-set cover, the reconstructed bundle depends on the transition map only up to homotopy, and every transition map is homotopic — by collapsing the collar onto $S$ — to the collar extension of its own restriction to $S$. So a bundle trivial off the disc is $P_g$ for $g$ its boundary transition (part b); two clutching maps give isomorphic bundles exactly when their transitions are cohomologous, which on $S$ reads $g'=(a|_S)g(b|_S)$ (part c); and the trivial bundle is $P_e$, so $P_g$ is trivial exactly when $g$ is cohomologous to the constant $e$, that is $g=(a|_S)(b|_S)$ (part d). The single engine behind all three is that the collar has no topology of its own: it retracts to the sphere, so nothing on it survives except what its restriction to $S$ already carried.

---

# What Makes This Hard

The construction is easy to state and easy to get subtly wrong in three places. First, the two natural pieces $X\setminus D^\circ$ and $D$ are **closed**, not open, and overlap only in the sphere $S$; a cocycle needs an *open* cover with an overlap of full dimension, so one must thicken to $\{U_O,U_D\}$ and extend $g$ across the collar — and one must check that the thickened overlap $\Sigma_\delta$ genuinely retracts onto $S$ so that no information is lost or invented. Second, the temptation is to prove part (c) by writing down an explicit bundle isomorphism and radially extending $a$ and $b$ over the thickened sets; but a strict radial retraction of $U_O$ onto $X\setminus D^\circ$ has a crease along $S$ and is not smooth. The clean route avoids all extension of $a$ and $b$: it works entirely with the cocycle classification and the one homotopy lemma, using that $a$ and $b$ are already defined on the (shrunk) open sets $U_O,U_D$. Third, in the mapping-torus corollary the structure "group" is the infinite-dimensional $\operatorname{Diff}(F)$, to which the Lie-group theorem does not literally apply; the correct move is to prove that corollary directly, by lifting the trivialisation to the universal cover $\mathbb{R}\times F$ and reading the isotopy off the monodromy, rather than by invoking parts (a)–(d).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Thicken the closed pieces $X\setminus D^\circ$ and $D$ to the open cover $\{U_O,U_D\}$ whose overlap is a spherical shell retracting onto $S$. Reconstruct $P_g$ from the two-set cocycle whose one essential entry is the collar extension $\hat g=g\circ r$ (part a). Prove one master lemma — the reconstructed bundle depends on the transition map only up to homotopy — and one collapse lemma — every transition map is homotopic to the collar extension of its boundary restriction. From these, read (b), (c), (d) as statements about cohomology and homotopy of the single boundary map. Finally prove the mapping-torus converse directly on the universal cover.

**Subgoal decomposition:**

1. **The cover and the cocycle (Lemma 1).** Build $\{U_O,U_D\}$, show it covers $X$ with $U_O\supseteq X\setminus D^\circ$, $U_D\supseteq D$ contractible, and overlap $\Sigma_\delta$ retracting onto $S$; check that $g_{OD}=\hat g$ is a two-set cocycle.
   - *Hint:* On a two-set cover, conditions $g_{OO}=g_{DD}=e$ and $g_{OD}=g_{DO}^{-1}$ force the triple condition, since every triple of indices from $\{O,D\}$ repeats one.
   - *Why needed:* It licenses the reconstruction of $P_g$ from $\hat g$ and supplies the retraction used everywhere below.

2. **Homotopy invariance of the two-set reconstruction (Lemma 2).** If $c_0,c_1\colon\Sigma_\delta\to G$ are smoothly homotopic, then $P(c_0)\cong P(c_1)$.
   - *Hint:* Thread the homotopy through the base: build a bundle over $X\times[0,1]$ whose slices are $P(c_t)$, and quote that a bundle over $X\times[0,1]$ has isomorphic ends.
   - *Why needed:* It is the single mechanism behind (b), (c), (d).

3. **Collar collapse (Lemma 3).** For every smooth $c\colon\Sigma_\delta\to G$, $P(c)\cong P_{c|_S}$.
   - *Hint:* $c$ is homotopic to $(c|_S)\circ r$ through $c\circ r_\tau$; apply Lemma 2.
   - *Why needed:* It says the reconstruction sees only the boundary restriction, up to homotopy.

4. **Part (a).** Reconstruct $P_g=P(\hat g)$; it is trivial over $U_O\supseteq X\setminus D^\circ$ and $U_D\supseteq D$, and its canonical transition is $\hat g$, restricting to $g$ on $S$.

5. **Part (b).** A bundle trivial over $U_O,U_D$ has a transition $c\colon\Sigma_\delta\to G$ and $\cong P(c)\cong P_{c|_S}$ by the cocycle classification and Lemma 3; the punctured-triviality clause reduces to this because $U_O\subseteq X\setminus\{x_0\}$ and $U_D$ is contractible.

6. **Part (c).** For $\Leftarrow$, turn $g'=(a|_S)g(b|_S)$ into a coboundary of $\hat g$ on $\Sigma_\delta$ and apply the cocycle classification and Lemma 3; for $\Rightarrow$, read the coboundary of an isomorphism off the cover and restrict to $S$. The homotopy clause is Lemma 2 applied to $\hat g\simeq\hat g'$.

7. **Part (d) and corollaries.** Specialise (c) to $g'=e$; specialise the base to $S^n$; and prove the mapping-torus converse on the universal cover.

---

# Lemma Decomposition

> [!note]- Lemma 1: the two-set clutching cover and its cocycle
> **Statement:** With the notation above, $\{U_O,U_D\}$ is an open cover of $X$ with $U_O\supseteq X\setminus D^\circ$, $U_D\supseteq D$, $U_D$ contractible, $U_O\subseteq X\setminus\{x_0\}$, and overlap $\Sigma_\delta$ that deformation-retracts onto $S$ via the smooth $r_\tau$. For any smooth $c\colon\Sigma_\delta\to G$, the family $g_{OO}=g_{DD}=e$, $g_{OD}=c$, $g_{DO}=c^{-1}$ is a cocycle on $\{U_O,U_D\}$, so the reconstruction $P(c)$ of [[Thm - Principal Bundles are Classified by Cocycles|the cocycle classification]] is defined.
>
> **Hint:** Every geometric claim is a statement about the radii $1-\delta,1,1+\delta$; the cocycle claim is the two-set collapse of the triple condition.
>
> **Why needed:** It provides the objects $P(c)$ and $P_g=P(\hat g)$ and the retraction $r_\tau$ used in Lemmas 2 and 3.
>
> > [!note]- Full proof
> > **The sets are open and cover $X$.** $U_D=\varphi(B_{1+\delta})$ is the image of an open ball under the open embedding $\varphi$, hence open, and is diffeomorphic to the ball $B_{1+\delta}\cong\mathbb{R}^n$, which is contractible; so $U_D$ is contractible. $U_O=X\setminus\varphi(\overline{B}_{1-\delta})$ is the complement of the compact (hence closed) set $\varphi(\overline{B}_{1-\delta})$, so it is open. For the covering, $U_D\supseteq\varphi(\overline{B}_{1-\delta})$ (as $\overline{B}_{1-\delta}\subseteq B_{1+\delta}$), and $U_O=X\setminus\varphi(\overline{B}_{1-\delta})$; the union of a set and its complement is $X$, so $U_O\cup U_D\supseteq(X\setminus\varphi(\overline{B}_{1-\delta}))\cup\varphi(\overline{B}_{1-\delta})=X$.
> >
> > **The inclusions.** Since $\overline{B}_{1-\delta}\subseteq B_1$, we have $\varphi(\overline{B}_{1-\delta})\subseteq\varphi(B_1)=D^\circ$, so $X\setminus D^\circ\subseteq X\setminus\varphi(\overline{B}_{1-\delta})=U_O$. Also $D=\varphi(\overline{B}_1)\subseteq\varphi(B_{1+\delta})=U_D$. Finally $x_0=\varphi(0)$ and $\lvert0\rvert=0<1-\delta$, so $x_0\in\varphi(\overline{B}_{1-\delta})$, whence $x_0\notin U_O$, i.e. $U_O\subseteq X\setminus\{x_0\}$.
> >
> > **The overlap and its retraction.** $U_O\cap U_D=\varphi(B_{1+\delta})\setminus\varphi(\overline{B}_{1-\delta})=\varphi(\{1-\delta<\lvert u\rvert<1+\delta\})=\varphi(A_\delta)=\Sigma_\delta$, using that $\varphi$ is injective. The map $r_\tau$ of the Notation section is smooth on $\Sigma_\delta$ (the argument $(1-\tau)u+\tau u/\lvert u\rvert$ is smooth in $(\tau,u)$ for $u\ne0$, and $u\ne0$ on $A_\delta$), maps $\Sigma_\delta$ into $\Sigma_\delta$ (its radius $(1-\tau)\lvert u\rvert+\tau$ lies in $(1-\delta,1+\delta)$ as shown above), and satisfies $r_0=\operatorname{id}_{\Sigma_\delta}$, $r_1=\iota_S\circ r$; hence it is a smooth deformation retraction of $\Sigma_\delta$ onto $S$.
> >
> > **The cocycle conditions.** On a cover with the two indices $\{O,D\}$ the three [[Def - Transition Functions and the Cocycle Condition|cocycle conditions]] are: (1) $g_{\alpha\alpha}=e$, satisfied by construction ($g_{OO}=g_{DD}=e$); (2) $g_{\alpha\beta}=g_{\beta\alpha}^{-1}$, satisfied since $g_{OD}=c=(c^{-1})^{-1}=g_{DO}^{-1}$ and $g_{OO}=e=e^{-1}$; (3) $g_{\alpha\beta}g_{\beta\gamma}g_{\gamma\alpha}=e$ on triple overlaps $U_{\alpha\beta\gamma}$ with $\alpha,\beta,\gamma\in\{O,D\}$. In a triple $(\alpha,\beta,\gamma)$ drawn from a two-element set at least two indices coincide; we verify the representative cases and note the rest are identical after relabelling. If $\alpha=\gamma$: $g_{\alpha\beta}g_{\beta\alpha}g_{\alpha\alpha}=g_{\alpha\beta}g_{\alpha\beta}^{-1}e=e$ (by (2) and (1)). If $\beta=\gamma$: $g_{\alpha\beta}g_{\beta\beta}g_{\beta\alpha}=g_{\alpha\beta}\,e\,g_{\alpha\beta}^{-1}=e$. If $\alpha=\beta$: $g_{\alpha\alpha}g_{\alpha\gamma}g_{\gamma\alpha}=e\,g_{\alpha\gamma}g_{\alpha\gamma}^{-1}=e$. As these exhaust all triples from $\{O,D\}$, condition (3) holds. Therefore $\{g_{OO},g_{OD},g_{DO},g_{DD}\}$ is a cocycle, and by the reconstruction clause of [[Thm - Principal Bundles are Classified by Cocycles|the cocycle classification]] — *a $G$-valued cocycle on an open cover of $X$ reconstructs a principal $G$-bundle whose canonical sections have that cocycle as their transition functions* — the bundle $P(c)$ is defined, with canonical sections $s_O,s_D$ satisfying $s_D=s_O\cdot c$ on $\Sigma_\delta$. $\blacksquare$

> [!note]- Lemma 2: the two-set reconstruction is a homotopy invariant of the transition map
> **Statement:** Fix the cover $\{U_O,U_D\}$. If $c_0,c_1\colon\Sigma_\delta\to G$ are smoothly homotopic (there is a smooth $C\colon\Sigma_\delta\times[0,1]\to G$ with $C(\cdot,0)=c_0$, $C(\cdot,1)=c_1$), then $P(c_0)\cong P(c_1)$ as principal $G$-bundles over $X$.
>
> **Hint:** Reconstruct a bundle over $X\times[0,1]$ from the cover $\{U_O\times[0,1],U_D\times[0,1]\}$ and the transition $C$; its restrictions to the two ends are $P(c_0)$ and $P(c_1)$, and a bundle over $X\times[0,1]$ has isomorphic ends.
>
> **Why needed:** It is the sole mechanism converting the geometry of the disc into homotopy statements in parts (b), (c), (d).
>
> > [!note]- Full proof
> > **Reconstruct over the cylinder.** The sets $\widetilde U_O:=U_O\times[0,1]$ and $\widetilde U_D:=U_D\times[0,1]$ form an open cover of the manifold-with-boundary $X\times[0,1]$, with overlap $\widetilde U_O\cap\widetilde U_D=\Sigma_\delta\times[0,1]$. Declare the two-set cocycle $\tilde g_{OD}:=C\colon\Sigma_\delta\times[0,1]\to G$ (with $\tilde g_{OO}=\tilde g_{DD}=e$, $\tilde g_{DO}=C^{-1}$); it is a cocycle by the two-set argument of Lemma 1 (the triple condition again collapses). By [[Thm - Principal Bundles are Classified by Cocycles|the cocycle classification]], there is a principal $G$-bundle $\mathcal{Q}\to X\times[0,1]$ with canonical sections $\tilde s_O,\tilde s_D$ and $\tilde s_D=\tilde s_O\cdot C$ on $\Sigma_\delta\times[0,1]$.
> >
> > **The ends are $P(c_0)$ and $P(c_1)$.** Fix $t\in\{0,1\}$ and let $j_t\colon X\to X\times[0,1]$, $j_t(x)=(x,t)$, be the slice inclusion; the restriction $\mathcal{Q}|_{X\times\{t\}}$ is a principal $G$-bundle over $X$ (identifying $X\times\{t\}$ with $X$). Its canonical sections are the restrictions $\tilde s_O(\cdot,t)$, $\tilde s_D(\cdot,t)$ over $U_O,U_D$, whose transition function on $\Sigma_\delta$ is the restriction $C(\cdot,t)=c_t$ (from $\tilde s_D=\tilde s_O\cdot C$, evaluating the second argument at $t$). A principal bundle over $X$ trivial over $U_O$ and $U_D$ with transition $c_t$ is, by the reconstruction and reconstruction-recognition clauses of [[Thm - Principal Bundles are Classified by Cocycles|the cocycle classification]] — *every principal bundle is isomorphic to the reconstruction from its own cocycle* — isomorphic to $P(c_t)$. Hence $\mathcal{Q}|_{X\times\{0\}}\cong P(c_0)$ and $\mathcal{Q}|_{X\times\{1\}}\cong P(c_1)$.
> >
> > **The ends are isomorphic.** By part (a) of [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|the homotopy-invariance theorem]] — *for a principal $G$-bundle $\mathcal{Q}\to X\times[0,1]$, the restrictions to $X\times\{0\}$ and $X\times\{1\}$ are isomorphic* — we have $\mathcal{Q}|_{X\times\{0\}}\cong\mathcal{Q}|_{X\times\{1\}}$. Combining the three isomorphisms,
> > $$P(c_0)\cong\mathcal{Q}|_{X\times\{0\}}\cong\mathcal{Q}|_{X\times\{1\}}\cong P(c_1).\qquad\blacksquare$$

> [!note]- Lemma 3: the reconstruction depends only on the boundary restriction
> **Statement:** For every smooth $c\colon\Sigma_\delta\to G$, $P(c)\cong P_{c|_S}$, where $c|_S\colon S\to G$ is the restriction of $c$ to the boundary sphere and $P_{c|_S}=P((c|_S)\circ r)$ is its clutching bundle.
>
> **Hint:** $c$ and $(c|_S)\circ r$ are the two ends of the homotopy $c\circ r_\tau$; apply Lemma 2.
>
> **Why needed:** It is the collapse that reduces the transition function on the two-dimensional-worth-of-collar to a single map on $S^{n-1}$.
>
> > [!note]- Full proof
> > Consider the smooth map $C\colon\Sigma_\delta\times[0,1]\to G$, $C(y,\tau):=c(r_\tau(y))$, using the smooth deformation retraction $r_\tau$ of Lemma 1 (smooth in $(y,\tau)$ because $r_\tau$ is smooth in $(y,\tau)$ and $c$ is smooth). Its endpoints are
> > $$C(\cdot,0)=c\circ r_0=c\circ\operatorname{id}_{\Sigma_\delta}=c\qquad\text{(since }r_0=\operatorname{id}\text{)},$$
> > $$C(\cdot,1)=c\circ r_1=c\circ(\iota_S\circ r)=(c\circ\iota_S)\circ r=(c|_S)\circ r\qquad\text{(since }r_1=\iota_S\circ r\text{ and }c\circ\iota_S=c|_S\text{)}.$$
> > Thus $c$ is smoothly homotopic to $(c|_S)\circ r$. By **Lemma 2**, $P(c)\cong P((c|_S)\circ r)=P_{c|_S}$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix $X$, $D$, $S$, $G$, and the cover $\{U_O,U_D\}$ with retraction $r_\tau$ as above.
>
> **Part (a) — construction.** Let $g\colon S\to G$ be smooth and $\hat g=g\circ r\colon\Sigma_\delta\to G$ its collar extension. By **Lemma 1** the family with $g_{OD}=\hat g$ is a cocycle on $\{U_O,U_D\}$, so $P_g:=P(\hat g)$ is a principal $G$-bundle over $X$ with canonical sections $s_O\colon U_O\to P_g$, $s_D\colon U_D\to P_g$ satisfying
> $$s_D=s_O\cdot\hat g\qquad\text{on }\Sigma_\delta\qquad\text{(reconstruction clause of the cocycle classification).}$$
> Since $s_O$ is a global section of $P_g$ over $U_O$, the bundle $P_g|_{U_O}$ is trivial by [[Thm - Sections of a Principal Bundle and Triviality|the section–triviality theorem]] — *a principal bundle admitting a global section over an open set is trivial over that set* — and hence $P_g$ is trivial over the smaller set $X\setminus D^\circ\subseteq U_O$ (restriction of a trivial bundle). Likewise $s_D$ trivialises $P_g$ over $U_D$, hence over $D\subseteq U_D$. The transition function from $s_O$ to $s_D$ is $\hat g$, and its restriction to $S$ is $\hat g|_S=(g\circ r)|_S=g$ (since $r|_S=\operatorname{id}_S$). This establishes (a). $\ \checkmark$
>
> **Part (b) — every such bundle is a clutching bundle.** Suppose $P\to X$ is trivial over $X\setminus D^\circ$ and over $D$, i.e. trivial over open sets $W_O\supseteq X\setminus D^\circ$ and $W_D\supseteq D$. Shrink $\delta$ so that $U_O\subseteq W_O$ and $U_D\subseteq W_D$ (possible by the compactness of $S$ and $D$, as in the Convention callout). Then $P$ is trivial over $U_O$ and over $U_D$ (restrictions), so by [[Thm - Sections of a Principal Bundle and Triviality|the section–triviality theorem]] there are sections $s_O^P\colon U_O\to P$, $s_D^P\colon U_D\to P$, with a transition function
> $$c\colon\Sigma_\delta\to G,\qquad s_D^P=s_O^P\cdot c.$$
> By the reconstruction-recognition clause of [[Thm - Principal Bundles are Classified by Cocycles|the cocycle classification]] — *every principal $G$-bundle is isomorphic to the reconstruction from its own cocycle* — we have $P\cong P(c)$. By **Lemma 3**, $P(c)\cong P_{c|_S}$. Setting $g:=c|_S\colon S\to G$ therefore gives $P\cong P_g$.
>
> *The punctured-triviality clause.* Assume now $G$ is connected and $P$ is trivial over $X\setminus\{x_0\}$. First, $P$ is trivial over $D$: the open set $U_D$ is contractible (Lemma 1), so by part (c) of [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|the homotopy-invariance theorem]] — *every principal $G$-bundle over a contractible manifold is trivial* — $P|_{U_D}$ is trivial, hence so is $P|_D$. Second, $P$ is trivial over $X\setminus D^\circ$: by Lemma 1, $U_O\subseteq X\setminus\{x_0\}$, over which $P$ is trivial by hypothesis, so $P|_{U_O}$ is trivial and hence so is $P|_{X\setminus D^\circ}$. Thus $P$ is trivial over $X\setminus D^\circ$ and over $D$, and the first part of (b) gives $P\cong P_g$. (The connectedness of $G$ is stated as a hypothesis for consistency with the applications, where it is what makes triviality over $X\setminus\{x_0\}$ available; the deduction just given uses only that hypothesis, taking $\delta$ small enough that $U_O\subseteq X\setminus\{x_0\}$, which Lemma 1 already guarantees for every $\delta$.) $\ \checkmark$
>
> **Part (c) — classification.**
>
> *Direction $\Leftarrow$ (coboundary $\Rightarrow$ isomorphic).* Assume $g'=(a|_S)\,g\,(b|_S)$ on $S$ for smooth $a\colon X\setminus D^\circ\to G$ and $b\colon D\to G$. As in (b), shrink $\delta$ so that $U_O$ lies in an open set on which $a$ is defined and smooth and $U_D$ in one on which $b$ is defined and smooth (the hypotheses provide $a,b$ smooth on neighbourhoods of the closed sets $X\setminus D^\circ$ and $D$); write $a,b$ also for the restrictions to $U_O,U_D$. Consider the transition maps $\hat g=g\circ r$ and $\hat g'=g'\circ r$ on $\Sigma_\delta$, so that $P_g=P(\hat g)$ and $P_{g'}=P(\hat g')$. Define on $\Sigma_\delta$
> $$\tilde c:= a\cdot\hat g\cdot b = a\cdot(g\circ r)\cdot b.$$
> Writing $h_O:=a^{-1}\colon U_O\to G$ and $h_D:=b\colon U_D\to G$, we have $\tilde c=h_O^{-1}\,\hat g\,h_D$ on $\Sigma_\delta$, which is exactly the coboundary relation exhibiting $\{\tilde c\}$ as cohomologous to $\{\hat g\}$ on $\{U_O,U_D\}$; the remaining coboundary equations $g'_{OO}=h_O^{-1}e\,h_O=e$ and $g'_{DD}=h_D^{-1}e\,h_D=e$ hold automatically. By the classification clause of [[Thm - Principal Bundles are Classified by Cocycles|the cocycle classification]] — *cohomologous cocycles on a fixed cover reconstruct isomorphic principal bundles* —
> $$P(\tilde c)\cong P(\hat g)=P_g.$$
> On the other hand, the boundary restriction of $\tilde c$ is
> $$\tilde c|_S=(a|_S)\,(\hat g|_S)\,(b|_S)=(a|_S)\,g\,(b|_S)=g'\qquad\text{(since }\hat g|_S=g\text{ and the hypothesis).}$$
> By **Lemma 3**, $P(\tilde c)\cong P_{\tilde c|_S}=P_{g'}$. Combining, $P_g\cong P(\tilde c)\cong P_{g'}$.
>
> *Direction $\Rightarrow$ (isomorphic $\Rightarrow$ coboundary).* Assume $P_g\cong P_{g'}$. Both are reconstructed on the cover $\{U_O,U_D\}$, from the cocycles with $g_{OD}=\hat g$ and $g'_{OD}=\hat g'$ respectively. By the classification clause of [[Thm - Principal Bundles are Classified by Cocycles|the cocycle classification]] — *isomorphic principal bundles on a fixed cover have cohomologous cocycles* — there are smooth $h_O\colon U_O\to G$, $h_D\colon U_D\to G$ with $\hat g'=h_O^{-1}\,\hat g\,h_D$ on $\Sigma_\delta$. Restrict to $S$, where $r|_S=\operatorname{id}$ gives $\hat g|_S=g$, $\hat g'|_S=g'$:
> $$g'=(h_O|_S)^{-1}\,g\,(h_D|_S)\qquad\text{on }S.$$
> Set $a:=(h_O|_{X\setminus D^\circ})^{-1}\colon X\setminus D^\circ\to G$ (defined since $X\setminus D^\circ\subseteq U_O$) and $b:=h_D|_D\colon D\to G$ (defined since $D\subseteq U_D$); both are smooth. Then $a|_S=(h_O|_S)^{-1}$ and $b|_S=h_D|_S$, so $g'=(a|_S)\,g\,(b|_S)$, as required.
>
> *The homotopy clause.* If $g$ and $g'$ are smoothly homotopic via $H\colon S\times[0,1]\to G$, then $\hat g=g\circ r$ and $\hat g'=g'\circ r$ are smoothly homotopic on $\Sigma_\delta$ via $(y,\tau)\mapsto H(r(y),\tau)$; by **Lemma 2**, $P_g=P(\hat g)\cong P(\hat g')=P_{g'}$. This proves (c). $\ \checkmark$
>
> **Part (d) — triviality criterion.** The trivial bundle $X\times G$ is $P_e$, the clutching bundle of the constant map $e\colon S\to G$: its collar extension is the constant $e$, whose reconstruction is the bundle with all transition functions equal to $e$, namely $X\times G$ (reconstruction clause of the cocycle classification). Hence $P_g$ is trivial if and only if $P_g\cong P_e$. By part (c) with $g'=e$,
> $$P_g\cong P_e\iff e=(a|_S)\,g\,(b|_S)\ \text{ for some smooth }a\colon X\setminus D^\circ\to G,\ b\colon D\to G.$$
> The right-hand relation solves to $g=(a|_S)^{-1}(b|_S)^{-1}=(a^{-1})|_S\,(b^{-1})|_S$; renaming $a^{-1}\rightsquigarrow a$ and $b^{-1}\rightsquigarrow b$ (again smooth maps $X\setminus D^\circ\to G$ and $D\to G$) yields the stated form $g=(a|_S)(b|_S)$, and the substitution is reversible, so the equivalence holds in both directions. Therefore $P_g$ is trivial if and only if $g=(a|_S)(b|_S)$ for some such $a,b$. $\ \blacksquare$

> [!note]- Complete proof of the sphere corollary
> Let $X=S^n$ and let $D$ be a closed hemispherical cap, so that its complement's interior's closure $X\setminus D^\circ$ is the opposite closed cap, itself a disc, and $S\cong S^{n-1}$ is the equator.
>
> **Every clutching class gives a well-defined bundle class.** By the homotopy clause of part (c), $g\simeq g'$ implies $P_g\cong P_{g'}$, so $[g]\mapsto[P_g]$ is a well-defined map from $[S^{n-1},G]$ (free homotopy classes of smooth maps) to isomorphism classes of principal $G$-bundles over $S^n$.
>
> **Injectivity.** Suppose $P_g\cong P_{g'}$. By part (c) there are smooth $a\colon X\setminus D^\circ\to G$, $b\colon D\to G$ with $g'=(a|_S)g(b|_S)$ on $S$. Both $X\setminus D^\circ$ and $D$ are discs, hence contractible; a smooth map from a contractible manifold to $G$ is smoothly null-homotopic, so $a$ and $b$ are each null-homotopic, and therefore so are the restrictions $a|_S$ and $b|_S$ (restrict the null-homotopies to $S$). Consequently the boundary values $a|_S$ and $b|_S$ are smoothly homotopic to the constant $e$, and pointwise multiplication is continuous, so $g'=(a|_S)g(b|_S)$ is smoothly homotopic to $e\cdot g\cdot e=g$. Hence $[g]=[g']$, and the map is injective.
>
> **Surjectivity onto bundles trivial off a point.** If $P\to S^n$ is trivial over $S^n\setminus\{x_0\}$ for a point $x_0\in D^\circ$, then $P$ is trivial over $X\setminus D^\circ$ (a subset of $S^n\setminus\{x_0\}$) and over the contractible $D$ (homotopy-invariance theorem (c)), so by part (b), $P\cong P_g$ for some $g$. If in addition $G$ is connected, then every principal $G$-bundle over $S^n$ is trivial over $S^n\setminus\{x_0\}$: over the disc $D$ it is trivial (contractibility), and over the disc $X\setminus\overline{D'}$ for a slightly smaller cap $D'$ it is trivial, and these two discs cover $S^n$ with contractible pieces — in particular the complement of the single point $x_0$ is contained in the union of trivialising discs, and a principal bundle over the contractible $S^n\setminus\{x_0\}\simeq\mathbb{R}^n$ is trivial by the homotopy-invariance theorem (c). Thus for connected $G$ every bundle is of the form $P_g$, and $[g]\mapsto[P_g]$ is onto.
>
> **The triviality clause.** By part (d), $P_g$ is trivial iff $g=(a|_S)(b|_S)$; since $X\setminus D^\circ$ and $D$ are discs, $a|_S$ and $b|_S$ are null-homotopic, so their product $g$ is null-homotopic. Conversely, if $g\colon S^{n-1}\to G$ is null-homotopic, a null-homotopy is a smooth map $\overline{b}\colon D\to G$ (extending $g$ over the cap $D$, using that a null-homotopic map on $S^{n-1}$ extends over the disc it bounds) with $\overline{b}|_S=g$; taking $a\equiv e$ and $b:=\overline{b}$ gives $(a|_S)(b|_S)=e\cdot g=g$, so $P_g$ is trivial by part (d). Hence $P_g$ is trivial iff $g$ is null-homotopic. $\blacksquare$

> [!note]- Complete proof of the mapping-torus corollary
> Let $F$ be a smooth manifold, $\phi\colon F\to F$ a diffeomorphism, and $E_\phi=\mathbb{Z}\backslash(\mathbb{R}\times F)$ its mapping torus, with quotient map $q_a\colon\mathbb{R}\times F\to E_\phi$, $q_a(t,f)=[t,f]$, the projection $\pi([t,f])=[t]\in S^1=\mathbb{Z}\backslash\mathbb{R}$, and the $\mathbb{Z}$-action $k\cdot(t,f)=(t+k,\phi^k(f))$, all as on [[Def - Sphere Bundles and Mapping Tori]]. Recall the orbit relation $[t+1,\phi(f)]=[t,f]$ (the case $k=1$ of the action). Write $q_b\colon\mathbb{R}\times F\to S^1\times F$, $q_b(t,f)=([t],f)$, for the product quotient, a smooth covering map.
>
> **The "if" direction** is Part II of [[Thm - The Mapping Torus of a Diffeomorphism is a Fibre Bundle over the Circle|the mapping-torus theorem]]: if $\phi$ is isotopic to $\operatorname{id}_F$ through diffeomorphisms then $E_\phi\cong S^1\times F$.
>
> **The "only if" direction.** Assume $E_\phi$ is trivial, with a bundle isomorphism $\Psi\colon E_\phi\to S^1\times F$ over $\operatorname{id}_{S^1}$ (so $\operatorname{pr}_{S^1}\circ\Psi=\pi$).
>
> *Step 1 — the monodromy family.* Define, for $t\in\mathbb{R}$,
> $$G_t\colon F\to F,\qquad G_t(f):=\operatorname{pr}_F\big(\Psi([t,f])\big),$$
> where $\operatorname{pr}_F\colon S^1\times F\to F$ is the projection. The map $(t,f)\mapsto G_t(f)=\operatorname{pr}_F(\Psi(q_a(t,f)))$ is smooth, being a composite of the smooth maps $q_a$, $\Psi$, $\operatorname{pr}_F$. For each fixed $t$, the map $G_t$ is a diffeomorphism of $F$: it is the composite of the diffeomorphism $f\mapsto[t,f]$ from $F$ onto the fibre $(E_\phi)_{[t]}$ (a bundle chart of $E_\phi$) with the restriction of $\Psi$ to that fibre (a diffeomorphism onto $\{[t]\}\times F$, since $\Psi$ is a bundle isomorphism over $\operatorname{id}$) followed by $\operatorname{pr}_F$.
>
> *Step 2 — the recursion.* Applying the orbit relation $[t+1,\phi(f)]=[t,f]$,
> $$G_{t+1}(\phi(f))=\operatorname{pr}_F\big(\Psi([t+1,\phi(f)])\big)=\operatorname{pr}_F\big(\Psi([t,f])\big)=G_t(f)\qquad\text{(orbit relation, then definition of }G\text{).}$$
> Since this holds for all $f\in F$, $G_{t+1}\circ\phi=G_t$, that is $G_{t+1}=G_t\circ\phi^{-1}$ for all $t\in\mathbb{R}$; in particular $G_1=G_0\circ\phi^{-1}$.
>
> *Step 3 — the family $(t,f)\mapsto G_t(f)$ has smooth inverse.* The map $\Xi\colon\mathbb{R}\times F\to\mathbb{R}\times F$, $\Xi(t,f)=(t,G_t(f))$, satisfies $q_b\circ\Xi=\Psi\circ q_a$ (indeed $q_b(t,G_t(f))=([t],G_t(f))=\Psi([t,f])=\Psi(q_a(t,f))$). Near any point $\Xi$ equals $q_b^{-1}\circ\Psi\circ q_a$ for a local smooth inverse of the covering $q_b$, a composite of local diffeomorphisms, so $\Xi$ is a local diffeomorphism; it is a bijection because it covers $\operatorname{id}_\mathbb{R}$ and is fibrewise the bijection $G_t$; hence $\Xi$ is a diffeomorphism, with smooth inverse $\Xi^{-1}(t,g)=(t,G_t^{-1}(g))$. Therefore $(t,g)\mapsto G_t^{-1}(g)$ is smooth.
>
> *Step 4 — the isotopy.* Define $h\colon[0,1]\times F\to F$ by $h_s:=G_s^{-1}\circ G_0$, i.e. $h(s,f)=G_s^{-1}(G_0(f))$. Each $h_s$ is a diffeomorphism (a composite of the diffeomorphisms $G_0$ and $G_s^{-1}$), and the map $(s,f)\mapsto h_s(f)=G_s^{-1}(G_0(f))$ is smooth by Steps 1 and 3, as is $(s,f)\mapsto h_s^{-1}(f)=G_0^{-1}(G_s(f))$. At the endpoints,
> $$h_0=G_0^{-1}\circ G_0=\operatorname{id}_F,\qquad h_1=G_1^{-1}\circ G_0=(G_0\circ\phi^{-1})^{-1}\circ G_0=\phi\circ G_0^{-1}\circ G_0=\phi\qquad\text{(by }G_1=G_0\circ\phi^{-1}\text{).}$$
> Thus $\{h_s\}_{s\in[0,1]}$ is a smooth isotopy through diffeomorphisms from $\operatorname{id}_F$ to $\phi$, so $\phi$ is isotopic to $\operatorname{id}_F$ through diffeomorphisms.
>
> Combining the two directions, $E_\phi$ is trivial if and only if $\phi$ is isotopic to $\operatorname{id}_F$ through diffeomorphisms. The argument is the clutching mechanism over $S^1$: the trivialisation $\Psi$, pulled back to the universal cover $\mathbb{R}$ of the base circle, is precisely the collar datum, and the monodromy recursion $G_{t+1}=G_t\circ\phi^{-1}$ is the two-set gluing rule; it runs verbatim with $\operatorname{Diff}(F)$ in the role of the structure group, so no finite-dimensionality of the group is used. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Line bundles over a Riemann surface and the degree.** Take $X=\Sigma$ a closed oriented surface, $G=U(1)$, and a Hermitian line bundle $L$ with associated principal $U(1)$-bundle $P$. A generic smooth section of $L$ has finitely many transverse zeros; gathering them into a disc $D$ by the homogeneity lemma makes $P$ trivial off $D$, so $P\cong P_g$ for a clutching map $g\colon S^1\to U(1)$, and the winding number of $g$ is the degree. The exercise is to prove that this winding number is well-defined (invariant under the freedom $g\mapsto(a|_S)g(b|_S)$ of part (c), since $a|_S$ and $b|_S$ contribute winding numbers that cancel — $b|_S$ extends over the disc and so has winding number zero, and $a|_S$ extends over $\Sigma\setminus D^\circ$) and additive under tensor product. This is non-obvious because the section, the disc, and the trivialisations are all choices, and only the theorem guarantees the resulting integer is not one of them.

**Instanton number of an $SU(2)$-bundle over the four-sphere.** With $X=S^4$, $G=SU(2)$, the sphere corollary gives a bijection between principal $SU(2)$-bundles over $S^4$ and $[S^3,SU(2)]=\pi_3(SU(2))\cong\mathbb{Z}$. The exercise is to build, for each integer $k$, the bundle $P_{g}$ with clutching map $g(q)=q^k$ (viewing $S^3=SU(2)$ as the unit quaternions), and to argue from part (c) that $P_{q^k}\cong P_{q^{k'}}$ forces $k=k'$ because the two power maps are non-homotopic. The theorem is what turns "count the bundles" into "compute a homotopy group of the group"; the non-obvious step is that no bundle datum other than the homotopy class of $g$ survives.

**Three-manifolds fibring over the circle.** Let $F$ be a closed surface and $\phi$ a self-diffeomorphism; the mapping-torus corollary says the closed three-manifold $E_\phi$ is a product $S^1\times F$ exactly when $\phi$ is isotopic to the identity, and otherwise records a non-trivial element of the mapping class group $\pi_0\operatorname{Diff}(F)$. The exercise is to show that a Dehn twist on a surface is not isotopic to the identity, and hence that its mapping torus is not a product, using the corollary to convert the topological question about the total space into the isotopy question about $\phi$. This is non-obvious because the total space and the fibre look innocuous; the obstruction lives entirely in the isotopy class of the gluing map, which is exactly what the corollary isolates.

---

# Bridges

- **The cocycle classification (§3.3).** The clutching construction is the two-set specialisation of [[Thm - Principal Bundles are Classified by Cocycles|the cocycle classification]]: the cover is $\{U_O,U_D\}$, the single essential transition is $\hat g$, and the coboundary relation $g_{\alpha\beta}\mapsto h_\alpha^{-1}g_{\alpha\beta}h_\beta$ restricts on the boundary sphere to $g\mapsto(a|_S)g(b|_S)$. Everything on this page is that theorem read off the smallest cover a trivial-off-a-disc bundle admits, with the collar retraction discarding the collar's spurious direction.

- **Homotopy invariance of bundles (§3.5).** Lemma 2 is a direct consequence of [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|the homotopy-invariance theorem]]: a homotopy of clutching data becomes a bundle over $X\times[0,1]$, whose ends the theorem declares isomorphic. Conversely, the mapping-torus corollary supplies the deferred converse of [[Thm - The Mapping Torus of a Diffeomorphism is a Fibre Bundle over the Circle|the mapping-torus theorem]], completing the biconditional "$E_\phi$ trivial $\iff\phi\simeq\operatorname{id}$ through diffeomorphisms" whose sufficiency was proved there.

- **The classification of $U(1)$- and $SU(2)$-bundles (§3.6).** Both [[Thm - Classification of Principal U(1)-Bundles by the First Chern Class|the U(1) classification]] and [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds|the SU(2) classification]] run through this page: a generic section makes the bundle trivial off a disc (via [[Thm - Generic Sections are Transverse to the Zero Section|generic sections]] and [[Thm - Homogeneity Lemma for Connected Manifolds|the homogeneity lemma]]), part (b) presents it as $P_g$, and part (c) makes its class a homotopy invariant of $g$, matched to a winding number or a degree by [[Thm - Winding Number of a Map from the Circle to U(1)|the winding-number theorem]] and [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree theorem]].

- **Characteristic classes (chapter VI).** Because part (c) makes $[P_g]$ depend only on $[g]$, any characteristic number is a homotopy invariant of the clutching map; the Chern–Weil integral $\tfrac{1}{8\pi^2}\int\operatorname{tr}(F\wedge F)$ of an $SU(2)$-bundle over a four-manifold, computed in chapter VI, equals the clutching degree precisely because both are invariants of $[g]$, and the equality is proved by evaluating each on the standard generators $q\mapsto q^k$.

---

# Unlocked by This

> [!tip] Bundles over spheres are homotopy groups of the group *(from §3.6)*
> The sphere corollary identifies principal $G$-bundles over $S^n$ (for connected $G$) with $[S^{n-1},G]=\pi_{n-1}(G)$, turning bundle classification into a computation in the homotopy of the structure group; this is developed for $U(1)$ over surfaces and $SU(2)$ over four-manifolds on **[[Thm - Classification of Principal U(1)-Bundles by the First Chern Class]]** and **[[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds]]**.

> [!tip] The converse triviality criterion for mapping tori *(from §3.1)*
> The mapping-torus corollary completes [[Thm - The Mapping Torus of a Diffeomorphism is a Fibre Bundle over the Circle|the mapping-torus theorem]]: $E_\phi$ is a product exactly when $\phi$ is isotopic to the identity, so isomorphism classes of $F$-bundles over the circle are measured by the mapping class group $\pi_0\operatorname{Diff}(F)$, as used for the Möbius and Klein non-examples on **[[Ex - The Möbius Strip as a Mapping Torus is a Nontrivial Bundle]]** and **[[Ex - The Klein Bottle as a Mapping Torus]]**.
