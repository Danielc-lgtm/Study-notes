---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Complex Projective Space as a Quotient"
  - "Thm - Quotient Manifold Theorem for Free Proper Actions"
  - "Def - Free, Transitive, Effective, and Proper Group Actions"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $n\ge 1$ is an integer and $\mathbb{C}^n$ carries its standard Hermitian inner product $\langle v,w\rangle=\sum_{j=1}^{n}v_j\overline{w_j}$, so that $\lvert w\rvert^2=\sum_{j=1}^{n}\lvert w_j\rvert^2$. We write
$$S^{2n-1}=\{w=(w_1,\dots,w_n)\in\mathbb{C}^n:\lvert w\rvert^2=1\}$$
for the unit sphere, a smooth $(2n-1)$-dimensional manifold, and
$$U(1)=\{z\in\mathbb{C}:\lvert z\rvert=1\}$$
for the circle group, a compact Lie group of dimension $1$. The circle acts on the sphere on the left by scalar multiplication, $z\cdot w=(zw_1,\dots,zw_n)$; this is the **scalar $U(1)$-action** on $S^{2n-1}$. Its orbit space is the **complex projective space**
$$\mathbb{CP}^{n-1}:=S^{2n-1}/U(1),$$
with quotient map $\pi\colon S^{2n-1}\to\mathbb{CP}^{n-1}$, $\pi(w)=U(1)\cdot w$, and the orbit of $w$ is written $[w]=[w_1:\dots:w_n]$ in homogeneous coordinates. All of this is fixed on **[[Def - Complex Projective Space as a Quotient]]**, whose manifold structure is the one used here; the standing conventions on smooth manifolds ($C^\infty$, Hausdorff, second countable) and on group actions (a compact group acts properly; a free action has trivial stabilisers) are those of the series, restated where used.

For the diffeomorphism statement we specialise to $n=2$, so $S^3\subset\mathbb{C}^2$. The target is the unit sphere
$$S^2=\{(y,y_3)\in\mathbb{C}\times\mathbb{R}:\lvert y\rvert^2+y_3^2=1\}\subset\mathbb{R}^3,$$
where we identify $\mathbb{R}^3=\mathbb{C}\times\mathbb{R}$ by writing the first two real coordinates as one complex number $y\in\mathbb{C}$ and keeping the third as $y_3\in\mathbb{R}$. Its **north pole** is $N=(0,1)$ and its **south pole** is $S=(0,-1)$. We use Bär's **Hopf map** in its stereographic normalisation,
$$\operatorname{Hopf}\colon S^3\to S^2,\qquad \operatorname{Hopf}(w_1,w_2)=\frac{1}{4\lvert w_2\rvert^2+\lvert w_1\rvert^2}\bigl(4\,w_1\overline{w_2},\ 4\lvert w_2\rvert^2-\lvert w_1\rvert^2\bigr),$$
and denote by $\widetilde{\operatorname{Hopf}}\colon\mathbb{CP}^1\to S^2$ the map it induces on the quotient (constructed in the proof). On $\mathbb{CP}^1$ we use the two standard affine charts
$$U_2=\{[w_1:w_2]:w_2\ne 0\},\quad \zeta=w_1/w_2\in\mathbb{C};\qquad U_1=\{[w_1:w_2]:w_1\ne 0\},\quad \eta=w_2/w_1\in\mathbb{C}.$$
The symbols $\zeta,\eta$ are the chart coordinates; each of $U_1,U_2$ is an open subset of $\mathbb{CP}^1$ diffeomorphic to $\mathbb{C}$, and $U_1\cup U_2=\mathbb{CP}^1$ because a nonzero vector has $w_1\ne 0$ or $w_2\ne 0$.

> [!warning] Convention: Bär's stereographic Hopf map versus the homogeneous-coordinate form
> Bär (B) writes the Hopf map in the stereographic normalisation displayed above, with the factor $4$ inherited from his stereographic projection $u\mapsto\frac{1}{4+\lvert u\rvert^2}(4u,\,4-\lvert u\rvert^2)$. The algebraic-topology notes **[[Def - The Hopf Map]]** (Algebraic Topology III) and Haydys's $w\mapsto[w]$ form use the unscaled representative $[w_1:w_2]\mapsto(2w_1\overline{w_2},\,\lvert w_1\rvert^2-\lvert w_2\rvert^2)$ (up to normalisation). The two formulas parametrise the **same** circle fibration $S^1\hookrightarrow S^3\to S^2$ and differ only by the choice of stereographic scaling and by an orientation-preserving reflection of $S^2$; the explicit conversion is recorded on [[Def - Complex Projective Space as a Quotient]]. Every displayed computation on this page uses Bär's normalisation, stated in the Notation, so the constants match Bär exactly.

---

# Statement

> **Theorem (the projective line is the two-sphere).** Let $n\ge 1$ and let $U(1)$ act on $S^{2n-1}\subset\mathbb{C}^n$ by scalar multiplication, with quotient the complex projective space $\mathbb{CP}^{n-1}=S^{2n-1}/U(1)$. Then:
> 1. $\mathbb{CP}^{n-1}$ is a smooth manifold of real dimension $\dim_{\mathbb{R}}\mathbb{CP}^{n-1}=2(n-1)$;
> 2. $\mathbb{CP}^{n-1}$ is compact and connected;
> 3. for $n=2$, the Hopf map $\operatorname{Hopf}\colon S^3\to S^2$ descends through the quotient $\pi\colon S^3\to\mathbb{CP}^1$ to a unique smooth map $\widetilde{\operatorname{Hopf}}\colon\mathbb{CP}^1\to S^2$ with $\widetilde{\operatorname{Hopf}}\circ\pi=\operatorname{Hopf}$, and this induced map is a **diffeomorphism**. In particular $\mathbb{CP}^1$ and $S^2$ are diffeomorphic.

The three parts are proved in the order stated. Parts 1 and 2 hold for every $n$; part 3 is the special feature of the lowest interesting dimension, where the base of the Hopf fibration is a sphere.

---

# Motivation

The complex projective spaces are the first family of manifolds gauge theory needs that are neither vector spaces nor Lie groups: $\mathbb{CP}^{n-1}$ is the space of complex lines in $\mathbb{C}^n$, it is compact, and it carries the tautological and hyperplane line bundles whose Chern numbers organise the whole theory of characteristic classes. Before any of that machinery can run, one has to know that $\mathbb{CP}^{n-1}$ *is* a manifold and what its dimension is, and one wants a completely explicit model of the smallest case to compute against. This theorem supplies both: it names the dimension for all $n$, and it identifies the smallest projective space $\mathbb{CP}^1$ with the round two-sphere $S^2$ in a way one can differentiate by hand.

The identification is not a formality. The two-sphere is the base of the Hopf fibration $S^1\hookrightarrow S^3\to S^2$, the unique nontrivial principal $U(1)$-bundle over $S^2$ and the prototype for every instanton and monopole computation later in the series; the same $S^3\to S^2$ appears as the generator of $\pi_3(S^2)=\mathbb{Z}$. To use the Hopf fibration as a bundle over $S^2$ one must first know that its base, which the quotient construction presents as $\mathbb{CP}^1=S^3/U(1)$, is genuinely the two-sphere and that the presentation is smooth in both directions. The content of part 3 is exactly this bridge: the abstract orbit space $S^3/U(1)$ and the concrete round sphere in $\mathbb{R}^3$ are the same smooth manifold, and the diffeomorphism between them is the Hopf map read off the quotient.

There is a second reason the result matters as a piece of technique. It is the cleanest illustration of the standard method for proving that an induced map on a quotient is a diffeomorphism: one gets smoothness for free from the universal property of the quotient, one gets bijectivity by identifying the fibres of the descending map with the orbits, and one gets the differential from a local section, reducing the whole rank computation to a formula one already understands — here, the inverse of stereographic projection. Every later proof that an equivariant map descends to a diffeomorphism of moduli or of orbit spaces follows this same three-move pattern.

---

# Sources and Targets

**Sources (Input Broadening).** The theorem is applied whenever one has a smooth map out of a total space that is constant on orbits and wants to recognise the induced map on the quotient as a diffeomorphism; the disguised inputs are the situations that secretly present such a map.

The first disguised source is **a free proper action together with an orbit-invariant smooth map into a manifold of the right dimension**. Whenever a Lie group $G$ acts freely and properly on $M$ and $f\colon M\to N$ is smooth with $f(g\cdot x)=f(x)$, the universal property makes $f$ descend to a smooth $\widetilde f\colon M/G\to N$; if in addition $\dim N=\dim M-\dim G$ and $f$ has fibres exactly equal to the orbits and is a submersion, then $\widetilde f$ is a local diffeomorphism, and bijectivity upgrades it to a diffeomorphism. The bridge $B\Rightarrow A$ is "orbit-invariant submersion with orbit-fibres" $\Rightarrow$ "descends to a local diffeomorphism". *Example problem:* show that for a compact Lie group $G$ the orbit map through a point with trivial stabiliser identifies the orbit $G\cdot x$ with $G$ itself as a manifold.

The second disguised source is **a homogeneous space presented two ways**. If a compact group acts transitively on a manifold with stabiliser $H$, the orbit map descends to a diffeomorphism $G/H\to$ (the orbit), and one recognises a familiar manifold as a coset space. For $\mathbb{CP}^1$ this is the statement $SU(2)/U(1)\cong S^2$, the Hopf fibration read group-theoretically; the bridge is "transitive action with closed stabiliser" $\Rightarrow$ "the coset space is the manifold acted on". *Example problem:* identify $S^{n}=SO(n+1)/SO(n)$ and deduce its dimension.

The third disguised source is **a chart-by-chart formula that turns out to be a stereographic projection**. When an induced map, expressed in an affine chart of a projective space, has the form of the inverse of a stereographic projection, it is automatically a diffeomorphism onto the sphere minus a point, and two such charts cover the sphere. The bridge is "the local expression is a Möbius-type or inverse-stereographic formula" $\Rightarrow$ "local diffeomorphism". *Example problem:* recognise the map $\mathbb{CP}^1\to S^2$ given in a chart by $\zeta\mapsto\frac{1}{1+\lvert\zeta\rvert^2}(2\zeta,\lvert\zeta\rvert^2-1)$ as a diffeomorphism without any further computation.

**Targets (Output Amplification).** The bare conclusion is a diffeomorphism $\mathbb{CP}^1\cong S^2$ and the dimension count $\dim_{\mathbb{R}}\mathbb{CP}^{n-1}=2(n-1)$; combined with other facts it does much more.

Combine the diffeomorphism with **the classification of principal $U(1)$-bundles over $S^2$ by the first Chern number**. The Hopf fibration $S^3\to S^2$, once its base is identified with $S^2$, is the generator of $\operatorname{Pic}(S^2)\cong\mathbb{Z}$; every Hermitian line bundle over $S^2$ is a tensor power of the tautological bundle $\mathcal{O}(-1)$, and the diffeomorphism of this page is what lets one transport the tautological bundle of $\mathbb{CP}^1$ to a bundle over the round sphere. The extra ingredient is the integrality of the first Chern class, and the payoff is the entire monopole numbering over $S^2$.

Combine the dimension count with **the cell decomposition $\mathbb{CP}^{n}=\mathbb{CP}^{n-1}\sqcup\mathbb{C}^{n}$** (proved on [[Def - Complex Projective Space as a Quotient]]). Iterating gives $\mathbb{CP}^{n}$ a CW structure with one cell in each even dimension $0,2,\dots,2n$, from which its homology and its Euler characteristic $\chi(\mathbb{CP}^n)=n+1$ follow; the base case of the induction is exactly $\mathbb{CP}^1=S^2\sqcup\mathbb{C}$, i.e. the two-cell attached to a point. The extra ingredient is the attaching map, and the payoff is the cohomology ring used in Chern–Weil theory.

Combine the diffeomorphism with **the long exact homotopy sequence of the fibration $S^1\to S^3\to S^2$**. With the base identified as $S^2$ and the fibre as $S^1$, the sequence yields $\pi_3(S^2)\cong\pi_3(S^3)=\mathbb{Z}$, the first nonzero higher homotopy group of a sphere in a range where naive dimension counting predicts zero. The extra ingredient is the exactness of the fibration sequence, and the payoff is the nontriviality of the Hopf class.

---

# Why Is It True

Strip away the formulas and picture the scalar action of the circle on $S^3\subset\mathbb{C}^2$. A point $w=(w_1,w_2)$ is a pair of complex numbers with $\lvert w_1\rvert^2+\lvert w_2\rvert^2=1$, and multiplying by a unit complex number $z$ rotates both entries by the same phase. Two data survive this rotation: the *ratio* $w_1/w_2\in\mathbb{C}\cup\{\infty\}$, which is unchanged because the common phase cancels in the quotient, and nothing else — the ratio is a complete invariant of the orbit, because once the ratio is fixed the constraint $\lvert w\rvert=1$ pins down the two moduli and only a common phase remains free. So the orbit space $\mathbb{CP}^1$ is exactly the set of possible ratios, the Riemann sphere $\mathbb{C}\cup\{\infty\}$.

The Hopf map is the same invariant, dressed as a point of the round sphere. Bär's formula is built by taking the ratio $u=w_1/w_2$ and pushing it through stereographic projection $u\mapsto\frac{1}{4+\lvert u\rvert^2}(4u,4-\lvert u\rvert^2)$, which is the standard bijection from the plane-plus-infinity to the two-sphere. Everything downstream is forced by this: the map is constant on orbits because it depends only on the ratio; its fibres are exactly the orbits because the ratio is a complete orbit invariant; and it hits every point of $S^2$ because stereographic projection is onto once the point at infinity (the orbit $w_2=0$) is included.

> The induced map $\widetilde{\operatorname{Hopf}}\colon\mathbb{CP}^1\to S^2$ is nothing but "the ratio $w_1/w_2$, read as a point of the Riemann sphere by stereographic projection", and it is a diffeomorphism because in each affine chart it *is* the inverse of a stereographic projection.

The remaining question is why it is smooth with a smooth inverse and not merely a continuous bijection. Smoothness one way is automatic: the universal property of the quotient manifold structure turns the smooth orbit-invariant map $\operatorname{Hopf}$ into a smooth map $\widetilde{\operatorname{Hopf}}$ on the quotient, at no cost. Smoothness of the inverse is where the two affine charts earn their keep. In the chart $U_2$, where $w_2\ne 0$, the natural section of the quotient sends the ratio $\zeta$ to the normalised representative $\tfrac{1}{\sqrt{1+\lvert\zeta\rvert^2}}(\zeta,1)$, and feeding this into $\operatorname{Hopf}$ returns precisely the inverse stereographic formula $\zeta\mapsto\frac{1}{4+\lvert\zeta\rvert^2}(4\zeta,4-\lvert\zeta\rvert^2)$, whose smooth inverse (stereographic projection itself) is written down explicitly. The chart $U_1$ covers the one point $U_2$ misses. A smooth bijection that is a local diffeomorphism has a smooth inverse, so the map is a diffeomorphism. The local-to-global step is the covering of $S^2$ by the two charts; the mechanism that makes each chart a diffeomorphism is the explicit inverse-stereographic formula.

---

# What Makes This Hard

The one genuinely non-obvious step is the maximal-rank claim, and the trap is to try to differentiate the Hopf map directly on $S^3$ — a submersion computation on a hypersurface, with the constraint $\lvert w\rvert=1$ complicating every partial derivative. The clean route is to work on the quotient through a **local section**: composing the Hopf map with the section $\zeta\mapsto\tfrac{1}{\sqrt{1+\lvert\zeta\rvert^2}}(\zeta,1)$ collapses the whole computation to the inverse of stereographic projection, whose rank is transparent because its inverse is written down. The two other places a proof can silently fail are forgetting that "bijective plus local diffeomorphism" is what gives a *smooth* inverse (a continuous bijection between manifolds need not be a diffeomorphism — for example $t\mapsto t^3$ on $\mathbb{R}$ is a smooth bijection but not a diffeomorphism, its inverse failing to be differentiable at $0$), and omitting the single point $w_2=0$ that the chart $U_2$ does not see, which is exactly why the second chart $U_1$ is not optional.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** For parts 1 and 2, apply the quotient manifold theorem to the scalar $U(1)$-action after checking it is free and proper, and read compactness and connectedness off the continuous surjection from the sphere. For part 3, produce the induced map by the universal property (this gives smoothness), show its fibres are the orbits (this gives bijectivity), express it in each of the two affine charts as an inverse stereographic projection (this gives local-diffeomorphism), and finish with the general fact that a smooth bijective local diffeomorphism is a diffeomorphism.

**Subgoal decomposition:**

1. **The action is free and proper.** Show the stabiliser of every point of $S^{2n-1}$ is trivial, and that a compact group acts properly.
   - *Hint:* If $z\cdot w=w$ and some $w_j\ne 0$, then $z=1$. Properness is the standing fact that compact groups act properly.
   - *Why needed:* These are the exact hypotheses of the quotient manifold theorem, which supplies the smooth structure, the dimension, the submersion property, the local sections, and the universal property used later.

2. **Dimension.** Deduce $\dim_{\mathbb{R}}\mathbb{CP}^{n-1}=2(n-1)$.
   - *Hint:* $\dim M-\dim G=(2n-1)-1$.
   - *Why needed:* It is part 1 of the statement, and it is what makes $\dim\mathbb{CP}^1=2=\dim S^2$, so that a local diffeomorphism can exist.

3. **Compactness and connectedness.** Show $\mathbb{CP}^{n-1}$ is compact and connected.
   - *Hint:* It is $\pi(S^{2n-1})$ with $\pi$ continuous; $S^{2n-1}$ is compact and, for $2n-1\ge 1$, connected.
   - *Why needed:* It is part 2, and compactness is what will let "injective immersion" reach "diffeomorphism" without appealing to properness a second time.

4. **The induced map exists and is smooth.** Show $\operatorname{Hopf}$ is constant on orbits and invoke the universal property.
   - *Hint:* $\operatorname{Hopf}(zw)=\operatorname{Hopf}(w)$ for $\lvert z\rvert=1$ because every term $w_1\overline{w_2}$, $\lvert w_j\rvert^2$ is phase-invariant.
   - *Why needed:* It defines $\widetilde{\operatorname{Hopf}}$ and gives its smoothness for free.

5. **Fibres are orbits, hence bijectivity.** Show $\operatorname{Hopf}(w)=\operatorname{Hopf}(w')\iff w'=z\cdot w$ for some $z\in U(1)$, and that $\operatorname{Hopf}$ is onto.
   - *Hint:* The third coordinate determines $\lvert w_1\rvert^2/\lvert w_2\rvert^2$, and then the first coordinate determines the ratio $w_1/w_2$; onto-ness follows from the chart computation of subgoal 6.
   - *Why needed:* Equal-fibres-are-orbits is exactly injectivity of $\widetilde{\operatorname{Hopf}}$; surjectivity of $\operatorname{Hopf}$ is surjectivity of $\widetilde{\operatorname{Hopf}}$.

6. **Chart expressions are inverse stereographic projections.** Compute $\widetilde{\operatorname{Hopf}}$ in $U_2$ and $U_1$ using the sections $\zeta\mapsto\tfrac{1}{\sqrt{1+\lvert\zeta\rvert^2}}(\zeta,1)$ and $\eta\mapsto\tfrac{1}{\sqrt{1+\lvert\eta\rvert^2}}(1,\eta)$, and show each result is a diffeomorphism onto $S^2$ minus a pole.
   - *Hint:* The $U_2$ expression is $\zeta\mapsto\frac{1}{4+\lvert\zeta\rvert^2}(4\zeta,4-\lvert\zeta\rvert^2)$; solve for $\zeta$ to exhibit the smooth inverse.
   - *Why needed:* It is the maximal-rank / local-diffeomorphism statement, done in the two charts that cover $\mathbb{CP}^1$.

7. **Assemble.** A smooth bijective local diffeomorphism is a diffeomorphism.
   - *Hint:* The set-inverse agrees near each point with the local smooth inverse.
   - *Why needed:* It converts subgoals 4–6 into part 3.

---

# Lemma Decomposition

> [!note]- Lemma 1: The scalar $U(1)$-action on $S^{2n-1}$ is free and proper, so $\mathbb{CP}^{n-1}$ is a smooth $2(n-1)$-manifold
> **Statement:** For every $n\ge 1$ the scalar action $z\cdot w=(zw_1,\dots,zw_n)$ of $U(1)$ on $S^{2n-1}$ is smooth, free, and proper. Consequently, by the quotient manifold theorem, $\mathbb{CP}^{n-1}=S^{2n-1}/U(1)$ carries a unique smooth manifold structure of dimension $\dim_{\mathbb{R}}S^{2n-1}-\dim U(1)=(2n-1)-1=2(n-1)$ for which $\pi\colon S^{2n-1}\to\mathbb{CP}^{n-1}$ is a smooth submersion admitting smooth local sections, and satisfying the universal property that every smooth orbit-constant map out of $S^{2n-1}$ factors uniquely and smoothly through $\pi$.
>
> **Hint:** Freeness is a one-line consequence of "some coordinate is nonzero on the sphere"; properness is the standing fact that a compact group acts properly; then quote the quotient manifold theorem verbatim.
>
> **Why needed:** It furnishes every structural fact about $\mathbb{CP}^{n-1}$ used on this page: the smooth structure, the dimension (part 1), the submersion $\pi$, the local sections used in the chart computation, and the universal property used to build $\widetilde{\operatorname{Hopf}}$.
>
> > [!note]- Full proof
> > **Smoothness of the action.** The map $U(1)\times S^{2n-1}\to S^{2n-1}$, $(z,w)\mapsto z\cdot w$, is the restriction of the smooth bilinear map $\mathbb{C}\times\mathbb{C}^n\to\mathbb{C}^n$, $(z,w)\mapsto zw$, to the embedded submanifold $U(1)\times S^{2n-1}$, and its image lies in $S^{2n-1}$ because $\lvert z\cdot w\rvert=\lvert z\rvert\,\lvert w\rvert=1\cdot 1=1$ (using $\lvert z\rvert=1$ and $\lvert w\rvert=1$). A restriction of a smooth map to submanifolds of source and target is smooth, so the action is smooth.
> >
> > **Freeness.** Fix $w\in S^{2n-1}$ and suppose $z\cdot w=w$ for some $z\in U(1)$. Then $zw_j=w_j$ for every $j$. Because $w\in S^{2n-1}$ we have $\lvert w\rvert=1\ne 0$, so at least one coordinate is nonzero, say $w_k\ne 0$. From $zw_k=w_k$ and $w_k\ne 0$ we may cancel $w_k$ to obtain $z=1$. Hence the only group element fixing $w$ is the identity, and this holds for every $w$; the action is free (the stabiliser of every point is trivial), as defined on **[[Def - Free, Transitive, Effective, and Proper Group Actions]]**.
> >
> > **Properness.** By the standing convention recorded on [[Def - Free, Transitive, Effective, and Proper Group Actions]], *a smooth action of a compact Lie group on a manifold is proper.* We recall the argument for completeness. Properness means the map $\Theta\colon U(1)\times S^{2n-1}\to S^{2n-1}\times S^{2n-1}$, $\Theta(z,w)=(z\cdot w,w)$, is a proper map, i.e. preimages of compact sets are compact. Let $K\subseteq S^{2n-1}\times S^{2n-1}$ be compact. Then $\Theta^{-1}(K)$ is a closed subset of $U(1)\times S^{2n-1}$: it is closed because $\Theta$ is continuous and $K$ is closed (compact subsets of a Hausdorff space are closed). Moreover $\Theta^{-1}(K)\subseteq U(1)\times S^{2n-1}$, which is compact as a product of the compact group $U(1)$ with the compact sphere $S^{2n-1}$ (a closed bounded subset of $\mathbb{R}^{2n}$, compact by Heine–Borel). A closed subset of a compact space is compact, so $\Theta^{-1}(K)$ is compact. Hence the action is proper.
> >
> > **Applying the quotient manifold theorem.** With the action smooth, free, and proper, the hypotheses of the quotient manifold theorem are met. We restate it at the point of use:
> > > *[[Thm - Quotient Manifold Theorem for Free Proper Actions|Quotient manifold theorem]]. If a Lie group $G$ acts smoothly, freely, and properly on a smooth manifold $M$, then the orbit space $M/G$ carries a unique smooth manifold structure of dimension $\dim M-\dim G$ for which the quotient map $\pi\colon M\to M/G$ is a smooth submersion; the quotient is Hausdorff and second countable, $\pi$ admits smooth local sections, and for every smooth $f\colon M\to N$ constant on the orbits there is a unique smooth $\widetilde f\colon M/G\to N$ with $\widetilde f\circ\pi=f$.*
> >
> > Taking $G=U(1)$ and $M=S^{2n-1}$, the theorem gives $\mathbb{CP}^{n-1}=S^{2n-1}/U(1)$ its smooth structure, with
> > $$\dim_{\mathbb{R}}\mathbb{CP}^{n-1}=\dim_{\mathbb{R}}S^{2n-1}-\dim_{\mathbb{R}}U(1)=(2n-1)-1=2(n-1),$$
> > and with $\pi$ a smooth submersion admitting smooth local sections and satisfying the stated universal property. This is exactly part 1 of the theorem, together with the tools needed for part 3.

> [!note]- Lemma 2: $\mathbb{CP}^{n-1}$ is compact and connected
> **Statement:** For every $n\ge 1$ the complex projective space $\mathbb{CP}^{n-1}$ is compact and connected.
>
> **Hint:** It is the continuous image of the sphere; compactness and connectedness are preserved by continuous images.
>
> **Why needed:** It is part 2 of the theorem. Compactness is also what makes the final assembly clean, since a diffeomorphism carries the compact $\mathbb{CP}^1$ onto the compact $S^2$ consistently.
>
> > [!note]- Full proof
> > The quotient map $\pi\colon S^{2n-1}\to\mathbb{CP}^{n-1}$ is continuous, being a smooth submersion by Lemma 1, and it is surjective by construction (every orbit is $\pi(w)$ for some $w$). Thus $\mathbb{CP}^{n-1}=\pi(S^{2n-1})$ is a continuous image of $S^{2n-1}$.
> >
> > **Compactness.** The sphere $S^{2n-1}=\{w\in\mathbb{R}^{2n}:\lvert w\rvert=1\}$ is closed and bounded in $\mathbb{R}^{2n}$, hence compact by the Heine–Borel theorem. The continuous image of a compact space is compact. Therefore $\mathbb{CP}^{n-1}$ is compact.
> >
> > **Connectedness.** For $n\ge 1$ we have $2n-1\ge 1$, and a sphere $S^m$ with $m\ge 1$ is path-connected: any two points $p,q\in S^m$ are joined by the path $t\mapsto\frac{(1-t)p+tq}{\lvert(1-t)p+tq\rvert}$ when $q\ne -p$ (the denominator never vanishes because $(1-t)p+tq=0$ would force $q=-\tfrac{1-t}{t}p$ with the two unit vectors antiparallel, i.e. $q=-p$), and when $q=-p$ one routes through any third point $r\notin\{p,q\}$, which exists since $m\ge 1$. A path-connected space is connected. The continuous image of a connected space is connected. Therefore $\mathbb{CP}^{n-1}=\pi(S^{2n-1})$ is connected.

> [!note]- Lemma 3: The Hopf map is constant on orbits, and its fibres are exactly the $U(1)$-orbits
> **Statement:** For $w,w'\in S^3$ one has $\operatorname{Hopf}(w)\in S^2$, and
> $$\operatorname{Hopf}(w)=\operatorname{Hopf}(w')\quad\Longleftrightarrow\quad w'=z\cdot w\ \text{ for some }z\in U(1).$$
> In particular $\operatorname{Hopf}$ is constant on the $U(1)$-orbits, and the induced set map $\mathbb{CP}^1\to S^2$, $[w]\mapsto\operatorname{Hopf}(w)$, is well defined and injective.
>
> **Hint:** For "$\Leftarrow$", every building block $w_1\overline{w_2}$ and $\lvert w_j\rvert^2$ is invariant under a common phase. For "$\Rightarrow$", the third coordinate is a strictly monotone function of $\lvert w_1\rvert^2/\lvert w_2\rvert^2$, so it recovers the two moduli; the first coordinate then recovers the ratio $w_1/w_2$.
>
> **Why needed:** Constancy on orbits is the hypothesis of the universal property (giving the smooth $\widetilde{\operatorname{Hopf}}$); "fibres are orbits" is precisely injectivity of $\widetilde{\operatorname{Hopf}}$.
>
> > [!note]- Full proof
> > **The image lies in $S^2$.** Fix $w=(w_1,w_2)\in S^3$, and abbreviate $a=\lvert w_1\rvert^2\ge 0$, $b=\lvert w_2\rvert^2\ge 0$, so $a+b=1$ and the denominator $D:=4b+a=1+3b\ge 1>0$ never vanishes. Writing $\operatorname{Hopf}(w)=(y,y_3)$ with $y=\frac{4w_1\overline{w_2}}{D}\in\mathbb{C}$ and $y_3=\frac{4b-a}{D}\in\mathbb{R}$,
> > $$\lvert y\rvert^2+y_3^2=\frac{\lvert 4w_1\overline{w_2}\rvert^2+(4b-a)^2}{D^2}=\frac{16ab+16b^2-8ab+a^2}{D^2}=\frac{a^2+8ab+16b^2}{D^2}=\frac{(a+4b)^2}{D^2}=1,$$
> > using $\lvert 4w_1\overline{w_2}\rvert^2=16\lvert w_1\rvert^2\lvert w_2\rvert^2=16ab$ and $D=a+4b$. Hence $\operatorname{Hopf}(w)\in S^2$.
> >
> > **Direction ($\Leftarrow$): constancy on orbits.** Let $z\in U(1)$, so $\lvert z\rvert=1$ and $z\overline z=1$. For $w'=z\cdot w=(zw_1,zw_2)$ we compute each ingredient of the formula:
> > $$\lvert zw_j\rvert^2=\lvert z\rvert^2\lvert w_j\rvert^2=\lvert w_j\rvert^2\quad(j=1,2)\qquad\text{(since }\lvert z\rvert=1),$$
> > $$(zw_1)\overline{(zw_2)}=z\overline z\,w_1\overline{w_2}=\lvert z\rvert^2 w_1\overline{w_2}=w_1\overline{w_2}\qquad\text{(since }z\overline z=\lvert z\rvert^2=1).$$
> > Every term appearing in $\operatorname{Hopf}$ — the denominator $4\lvert w_2\rvert^2+\lvert w_1\rvert^2$, the numerator $4w_1\overline{w_2}$, and $4\lvert w_2\rvert^2-\lvert w_1\rvert^2$ — is therefore unchanged, so $\operatorname{Hopf}(z\cdot w)=\operatorname{Hopf}(w)$. Thus $\operatorname{Hopf}$ is constant on each orbit, and $[w]\mapsto\operatorname{Hopf}(w)$ does not depend on the representative $w$, i.e. it is well defined on $\mathbb{CP}^1$.
> >
> > **Direction ($\Rightarrow$): equal images force one orbit.** Suppose $\operatorname{Hopf}(w)=\operatorname{Hopf}(w')$, with $a=\lvert w_1\rvert^2$, $b=\lvert w_2\rvert^2$, $a+b=1$ and correspondingly $a'=\lvert w_1'\rvert^2$, $b'=\lvert w_2'\rvert^2$, $a'+b'=1$.
> >
> > *Step A — the moduli agree.* Equating third coordinates,
> > $$\frac{4b-a}{4b+a}=\frac{4b'-a'}{4b'+a'}.$$
> > Consider the function $\varphi(s)=\frac{4-s}{4+s}$ for $s\in[0,\infty)$; here $s$ plays the role of $a/b$. We have $\varphi(s)=-1+\frac{8}{4+s}$, which is strictly decreasing in $s$, hence injective. Dividing numerator and denominator of each side by the respective $b$ (treating first the generic case $b,b'\ne 0$), the equation reads $\varphi(a/b)=\varphi(a'/b')$, so injectivity of $\varphi$ gives $a/b=a'/b'$. Together with $a+b=a'+b'=1$ this linear system forces $a=a'$ and $b=b'$; explicitly, $a/b=a'/b'=:r$ gives $a=\frac{r}{1+r}=a'$ and $b=\frac{1}{1+r}=b'$. The degenerate case $b=0$ (equivalently $y_3=\frac{-a}{a}=-1$, the south pole) forces $y_3'=y_3=-1$, hence $\frac{4b'-a'}{4b'+a'}=-1$, i.e. $4b'-a'=-(4b'+a')$, i.e. $8b'=0$, so $b'=0$ as well, and then $a=a'=1$. If instead $b'=0$, then $y_3=y_3'=\frac{-a'}{a'}=-1$ forces $\frac{4b-a}{4b+a}=-1$, i.e. $4b-a=-(4b+a)$, i.e. $8b=0$, so $b=0$, and again $a=a'=1$. In all cases $\lvert w_1\rvert=\lvert w_1'\rvert$ and $\lvert w_2\rvert=\lvert w_2'\rvert$.
> >
> > *Step B — the ratios agree.* If $b=b'=0$ then $w=(w_1,0)$, $w'=(w_1',0)$ with $\lvert w_1\rvert=\lvert w_1'\rvert=1$; put $z=w_1'/w_1$, so $\lvert z\rvert=\lvert w_1'\rvert/\lvert w_1\rvert=1$ and $w'=(zw_1,0)=z\cdot w$, and we are done. Otherwise $b=b'\ne 0$. Since the denominators are equal ($4b+a=4b'+a'$ by Step A), equating first coordinates gives $4w_1\overline{w_2}=4w_1'\overline{w_2'}$, hence $w_1\overline{w_2}=w_1'\overline{w_2'}$. Dividing by $\lvert w_2\rvert^2=b=b'=\lvert w_2'\rvert^2\ne 0$,
> > $$\frac{w_1}{w_2}=\frac{w_1\overline{w_2}}{\lvert w_2\rvert^2}=\frac{w_1'\overline{w_2'}}{\lvert w_2'\rvert^2}=\frac{w_1'}{w_2'}=:\zeta.$$
> > Set $z=w_2'/w_2$. Then $\lvert z\rvert=\lvert w_2'\rvert/\lvert w_2\rvert=1$ (Step A), so $z\in U(1)$, and
> > $$w_2'=z\,w_2,\qquad w_1'=\zeta\,w_2'=\zeta\,z\,w_2=z\,(\zeta w_2)=z\,w_1,$$
> > using $w_1=\zeta w_2$. Hence $w'=(zw_1,zw_2)=z\cdot w$. This proves the forward direction: equal Hopf images lie in a single $U(1)$-orbit.
> >
> > **Consequence.** The two directions say the fibre $\operatorname{Hopf}^{-1}(p)$ through any $w$ is exactly the orbit $U(1)\cdot w$. Therefore the induced map $[w]\mapsto\operatorname{Hopf}(w)$ is well defined (by $\Leftarrow$) and injective (by $\Rightarrow$: if two orbits have the same image they are the same orbit).

> [!note]- Lemma 4: In each affine chart $\widetilde{\operatorname{Hopf}}$ is an inverse stereographic projection, hence a diffeomorphism onto $S^2$ minus a pole
> **Statement:** Write $\widetilde{\operatorname{Hopf}}\colon\mathbb{CP}^1\to S^2$ for the map $[w]\mapsto\operatorname{Hopf}(w)$ of Lemma 3. In the chart $U_2$ (coordinate $\zeta=w_1/w_2$) it is
> $$\Phi_2(\zeta)=\frac{1}{4+\lvert\zeta\rvert^2}\bigl(4\zeta,\ 4-\lvert\zeta\rvert^2\bigr),$$
> a diffeomorphism from $\mathbb{C}$ onto $S^2\setminus\{S\}$; in the chart $U_1$ (coordinate $\eta=w_2/w_1$) it is
> $$\Phi_1(\eta)=\frac{1}{4\lvert\eta\rvert^2+1}\bigl(4\overline{\eta},\ 4\lvert\eta\rvert^2-1\bigr),$$
> a diffeomorphism from $\mathbb{C}$ onto $S^2\setminus\{N\}$. Consequently $\widetilde{\operatorname{Hopf}}$ is a local diffeomorphism at every point of $\mathbb{CP}^1$, and it is surjective onto $S^2$.
>
> **Hint:** Feed the unit-length section $s_2(\zeta)=\tfrac{1}{\sqrt{1+\lvert\zeta\rvert^2}}(\zeta,1)$ into $\operatorname{Hopf}$; the normalising factors cancel and leave the inverse stereographic formula. Invert it explicitly to exhibit the smooth inverse.
>
> **Why needed:** This is the maximal-rank content (item I1.5.4 in the source), delivered on the two charts that cover $\mathbb{CP}^1$; surjectivity here supplies the remaining half of bijectivity.
>
> > [!note]- Full proof
> > **A smooth local section over $U_2$.** Define $s_2\colon U_2\to S^3$ by
> > $$s_2([w_1:w_2])=\frac{1}{\sqrt{1+\lvert\zeta\rvert^2}}(\zeta,1),\qquad \zeta=\frac{w_1}{w_2}.$$
> > This is well defined: on $U_2$ the coordinate $\zeta$ is a genuine complex number, the argument lies on $S^3$ because $\frac{\lvert\zeta\rvert^2+1}{1+\lvert\zeta\rvert^2}=1$, and $\pi(s_2([w_1:w_2]))=[\zeta:1]=[w_1:w_2]$ (as $(\zeta,1)$ and $(w_1,w_2)=w_2(\zeta,1)$ are complex-proportional, hence in one orbit; the positive real scalar $1/\sqrt{1+\lvert\zeta\rvert^2}$ does not change the orbit either). It is smooth because $\zeta$ is a smooth chart coordinate and $\zeta\mapsto\tfrac{1}{\sqrt{1+\lvert\zeta\rvert^2}}(\zeta,1)$ is smooth ($\mathbb{R}$-valued denominator never zero). Thus $s_2$ is a smooth local section of $\pi$ over $U_2$, and since $\widetilde{\operatorname{Hopf}}\circ\pi=\operatorname{Hopf}$,
> > $$\widetilde{\operatorname{Hopf}}([w_1:w_2])=\widetilde{\operatorname{Hopf}}\bigl(\pi(s_2([w_1:w_2]))\bigr)=\operatorname{Hopf}\bigl(s_2([w_1:w_2])\bigr).$$
> >
> > **Computing the chart expression $\Phi_2$.** With $w_1=\zeta/\sqrt{1+\lvert\zeta\rvert^2}$ and $w_2=1/\sqrt{1+\lvert\zeta\rvert^2}$ we read off $\lvert w_1\rvert^2=\frac{\lvert\zeta\rvert^2}{1+\lvert\zeta\rvert^2}$, $\lvert w_2\rvert^2=\frac{1}{1+\lvert\zeta\rvert^2}$, and $w_1\overline{w_2}=\frac{\zeta}{1+\lvert\zeta\rvert^2}$. Substituting into $\operatorname{Hopf}$,
> > $$4\lvert w_2\rvert^2+\lvert w_1\rvert^2=\frac{4+\lvert\zeta\rvert^2}{1+\lvert\zeta\rvert^2},\qquad 4w_1\overline{w_2}=\frac{4\zeta}{1+\lvert\zeta\rvert^2},\qquad 4\lvert w_2\rvert^2-\lvert w_1\rvert^2=\frac{4-\lvert\zeta\rvert^2}{1+\lvert\zeta\rvert^2},$$
> > so, dividing the last two by the first (the common factor $\frac{1}{1+\lvert\zeta\rvert^2}$ cancels),
> > $$\Phi_2(\zeta)=\operatorname{Hopf}(s_2)=\frac{1}{4+\lvert\zeta\rvert^2}\bigl(4\zeta,\ 4-\lvert\zeta\rvert^2\bigr).$$
> >
> > **$\Phi_2$ is a diffeomorphism onto $S^2\setminus\{S\}$.** The map $\Phi_2\colon\mathbb{C}\to\mathbb{R}^3$ is smooth (rational with nonvanishing denominator $4+\lvert\zeta\rvert^2\ge 4$) and lands in $S^2$ by Lemma 3. Its third coordinate is $y_3=\frac{4-\lvert\zeta\rvert^2}{4+\lvert\zeta\rvert^2}=-1+\frac{8}{4+\lvert\zeta\rvert^2}\in(-1,1]$, which never equals $-1$, so the image avoids the south pole $S=(0,-1)$; conversely we show it hits every other point. Given $(y,y_3)\in S^2$ with $y_3\ne -1$, set
> > $$\sigma(y,y_3)=\frac{2y}{1+y_3}\in\mathbb{C}.$$
> > This is smooth on the open set $S^2\setminus\{S\}=\{y_3\ne -1\}$. We check $\sigma$ and $\Phi_2$ are mutually inverse. First, from the two identities $1+y_3=\frac{8}{4+\lvert\zeta\rvert^2}$ (add $1$ to the third coordinate of $\Phi_2$) and $y=\frac{4\zeta}{4+\lvert\zeta\rvert^2}$, we get
> > $$\sigma(\Phi_2(\zeta))=\frac{2y}{1+y_3}=\frac{2\cdot\frac{4\zeta}{4+\lvert\zeta\rvert^2}}{\frac{8}{4+\lvert\zeta\rvert^2}}=\frac{8\zeta}{8}=\zeta,$$
> > so $\sigma\circ\Phi_2=\mathrm{id}_{\mathbb{C}}$. Second, for $(y,y_3)\in S^2\setminus\{S\}$ put $\zeta=\sigma(y,y_3)=\frac{2y}{1+y_3}$; then, using $\lvert y\rvert^2=1-y_3^2=(1-y_3)(1+y_3)$,
> > $$\lvert\zeta\rvert^2=\frac{4\lvert y\rvert^2}{(1+y_3)^2}=\frac{4(1-y_3)(1+y_3)}{(1+y_3)^2}=\frac{4(1-y_3)}{1+y_3},\qquad 4+\lvert\zeta\rvert^2=\frac{4(1+y_3)+4(1-y_3)}{1+y_3}=\frac{8}{1+y_3}.$$
> > Hence the first coordinate of $\Phi_2(\zeta)$ is $\frac{4\zeta}{4+\lvert\zeta\rvert^2}=\frac{4\cdot\frac{2y}{1+y_3}}{\frac{8}{1+y_3}}=y$, and its third coordinate is $\frac{4-\lvert\zeta\rvert^2}{4+\lvert\zeta\rvert^2}=1-\frac{2\lvert\zeta\rvert^2}{4+\lvert\zeta\rvert^2}=1-\frac{2\cdot\frac{4(1-y_3)}{1+y_3}}{\frac{8}{1+y_3}}=1-(1-y_3)=y_3$, so $\Phi_2(\sigma(y,y_3))=(y,y_3)$. Thus $\Phi_2\circ\sigma=\mathrm{id}_{S^2\setminus\{S\}}$. A smooth bijection between (open subsets of) manifolds with a smooth inverse is a diffeomorphism, so $\Phi_2\colon\mathbb{C}\to S^2\setminus\{S\}$ is a diffeomorphism. (The map $\sigma$ is precisely stereographic projection from the south pole in Bär's normalisation; $\Phi_2$ is its inverse.)
> >
> > **A smooth local section over $U_1$, and the chart expression $\Phi_1$.** Define $s_1\colon U_1\to S^3$ by
> > $$s_1([w_1:w_2])=\frac{1}{\sqrt{1+\lvert\eta\rvert^2}}(1,\eta),\qquad \eta=\frac{w_2}{w_1}.$$
> > This is well defined: on $U_1$ the coordinate $\eta$ is a genuine complex number, the argument lies on $S^3$ because $\frac{1+\lvert\eta\rvert^2}{1+\lvert\eta\rvert^2}=1$, and $\pi(s_1([w_1:w_2]))=[1:\eta]=[w_1:w_2]$ (as $(1,\eta)$ and $(w_1,w_2)=w_1(1,\eta)$ are complex-proportional, hence in one orbit, and the positive real scalar $1/\sqrt{1+\lvert\eta\rvert^2}$ does not change the orbit). It is smooth because $\eta$ is a smooth chart coordinate and the $\mathbb{R}$-valued denominator never vanishes. Thus $s_1$ is a smooth local section of $\pi$ over $U_1$, and, exactly as for $U_2$, $\widetilde{\operatorname{Hopf}}([w_1:w_2])=\operatorname{Hopf}(s_1([w_1:w_2]))$. With $w_1=1/\sqrt{1+\lvert\eta\rvert^2}$ and $w_2=\eta/\sqrt{1+\lvert\eta\rvert^2}$ we read off $\lvert w_1\rvert^2=\frac{1}{1+\lvert\eta\rvert^2}$, $\lvert w_2\rvert^2=\frac{\lvert\eta\rvert^2}{1+\lvert\eta\rvert^2}$, $w_1\overline{w_2}=\frac{\overline{\eta}}{1+\lvert\eta\rvert^2}$, so
> > $$4\lvert w_2\rvert^2+\lvert w_1\rvert^2=\frac{4\lvert\eta\rvert^2+1}{1+\lvert\eta\rvert^2},\qquad 4w_1\overline{w_2}=\frac{4\overline{\eta}}{1+\lvert\eta\rvert^2},\qquad 4\lvert w_2\rvert^2-\lvert w_1\rvert^2=\frac{4\lvert\eta\rvert^2-1}{1+\lvert\eta\rvert^2},$$
> > and dividing the last two by the first (the common factor $\frac{1}{1+\lvert\eta\rvert^2}$ cancels),
> > $$\Phi_1(\eta)=\operatorname{Hopf}(s_1)=\frac{1}{4\lvert\eta\rvert^2+1}\bigl(4\overline{\eta},\ 4\lvert\eta\rvert^2-1\bigr).$$
> >
> > **$\Phi_1$ is a diffeomorphism onto $S^2\setminus\{N\}$.** The map $\Phi_1\colon\mathbb{C}\to\mathbb{R}^3$ is smooth (rational with nonvanishing denominator $4\lvert\eta\rvert^2+1\ge 1$) and lands in $S^2$ by Lemma 3. Its third coordinate is $y_3=\frac{4\lvert\eta\rvert^2-1}{4\lvert\eta\rvert^2+1}=1-\frac{2}{4\lvert\eta\rvert^2+1}\in[-1,1)$, which never equals $1$, so the image avoids the north pole $N=(0,1)$. Here the factor $4$ sits on the $\lvert\eta\rvert^2$ term of the denominator rather than on the constant term as in $\Phi_2$, so the inverse is **not** the $U_2$ formula and we compute it afresh. Define
> > $$\sigma_1(y,y_3)=\frac{\overline{y}}{2(1-y_3)}\in\mathbb{C},$$
> > which is smooth on the open set $S^2\setminus\{N\}=\{y_3\ne 1\}$. We check $\sigma_1$ and $\Phi_1$ are mutually inverse. First, from $1-y_3=\frac{2}{4\lvert\eta\rvert^2+1}$ (subtract the third coordinate of $\Phi_1$ from $1$) and $y=\frac{4\overline{\eta}}{4\lvert\eta\rvert^2+1}$, so that $\overline{y}=\frac{4\eta}{4\lvert\eta\rvert^2+1}$, we get
> > $$\sigma_1(\Phi_1(\eta))=\frac{\overline{y}}{2(1-y_3)}=\frac{\frac{4\eta}{4\lvert\eta\rvert^2+1}}{2\cdot\frac{2}{4\lvert\eta\rvert^2+1}}=\frac{4\eta}{4}=\eta,$$
> > so $\sigma_1\circ\Phi_1=\mathrm{id}_{\mathbb{C}}$. Second, for $(y,y_3)\in S^2\setminus\{N\}$ put $\eta=\sigma_1(y,y_3)=\frac{\overline{y}}{2(1-y_3)}$; then, using $\lvert y\rvert^2=1-y_3^2=(1-y_3)(1+y_3)$,
> > $$\lvert\eta\rvert^2=\frac{\lvert y\rvert^2}{4(1-y_3)^2}=\frac{(1-y_3)(1+y_3)}{4(1-y_3)^2}=\frac{1+y_3}{4(1-y_3)},\qquad 4\lvert\eta\rvert^2+1=\frac{(1+y_3)+(1-y_3)}{1-y_3}=\frac{2}{1-y_3}.$$
> > Hence the first coordinate of $\Phi_1(\eta)$ is $\frac{4\overline{\eta}}{4\lvert\eta\rvert^2+1}=\frac{4\cdot\frac{y}{2(1-y_3)}}{\frac{2}{1-y_3}}=\frac{\frac{2y}{1-y_3}}{\frac{2}{1-y_3}}=y$ (using $\overline{\eta}=\frac{y}{2(1-y_3)}$), and its third coordinate is $\frac{4\lvert\eta\rvert^2-1}{4\lvert\eta\rvert^2+1}=1-\frac{2}{4\lvert\eta\rvert^2+1}=1-\frac{2}{\frac{2}{1-y_3}}=1-(1-y_3)=y_3$, so $\Phi_1(\sigma_1(y,y_3))=(y,y_3)$. Thus $\Phi_1\circ\sigma_1=\mathrm{id}_{S^2\setminus\{N\}}$, and $\Phi_1\colon\mathbb{C}\to S^2\setminus\{N\}$ is a diffeomorphism with smooth inverse $\sigma_1$ — the stereographic projection from the north pole in Bär's normalisation.
> >
> > **Local diffeomorphism and surjectivity.** The affine coordinate maps $c_2\colon U_2\to\mathbb{C}$, $[w]\mapsto\zeta$, and $c_1\colon U_1\to\mathbb{C}$, $[w]\mapsto\eta$, are diffeomorphisms onto $\mathbb{C}$ (part of the smooth structure of $\mathbb{CP}^1$; see [[Def - Complex Projective Space as a Quotient]]). On $U_2$ we have $\widetilde{\operatorname{Hopf}}=\Phi_2\circ c_2$, a composition of the diffeomorphism $c_2\colon U_2\to\mathbb{C}$ with the diffeomorphism $\Phi_2\colon\mathbb{C}\to S^2\setminus\{S\}$, hence a diffeomorphism $U_2\to S^2\setminus\{S\}$; and on $U_1$ we have $\widetilde{\operatorname{Hopf}}=\Phi_1\circ c_1$, a composition of the diffeomorphism $c_1\colon U_1\to\mathbb{C}$ with the diffeomorphism $\Phi_1\colon\mathbb{C}\to S^2\setminus\{N\}$, hence a diffeomorphism $U_1\to S^2\setminus\{N\}$. Since $U_1,U_2$ are open and cover $\mathbb{CP}^1$, every point of $\mathbb{CP}^1$ has an open neighbourhood on which $\widetilde{\operatorname{Hopf}}$ restricts to a diffeomorphism onto an open subset of $S^2$; that is, $\widetilde{\operatorname{Hopf}}$ is a local diffeomorphism. Finally $\widetilde{\operatorname{Hopf}}(\mathbb{CP}^1)\supseteq\widetilde{\operatorname{Hopf}}(U_2)\cup\widetilde{\operatorname{Hopf}}(U_1)=(S^2\setminus\{S\})\cup(S^2\setminus\{N\})=S^2$, so $\widetilde{\operatorname{Hopf}}$ is surjective.

> [!note]- Lemma 5: A smooth bijective local diffeomorphism is a diffeomorphism
> **Statement:** Let $F\colon X\to Y$ be a smooth map between smooth manifolds that is bijective and a local diffeomorphism (every $x\in X$ has an open neighbourhood $V$ with $F|_V\colon V\to F(V)$ a diffeomorphism onto an open subset of $Y$). Then $F$ is a diffeomorphism.
>
> **Hint:** The set-theoretic inverse $F^{-1}$ exists by bijectivity; show it is smooth by comparing it, near each point of $Y$, with a local smooth inverse of $F$.
>
> **Why needed:** It is the final assembly step: Lemmas 3–4 make $\widetilde{\operatorname{Hopf}}$ a smooth bijective local diffeomorphism, and this lemma upgrades it to a diffeomorphism.
>
> > [!note]- Full proof
> > Since $F$ is bijective it has a set-theoretic inverse $G:=F^{-1}\colon Y\to X$; we must show $G$ is smooth, for then $F$ is a smooth bijection with smooth inverse, i.e. a diffeomorphism. Smoothness is local, so fix $y_0\in Y$ and let $x_0=G(y_0)$, the unique preimage. Because $F$ is a local diffeomorphism, there is an open $V\ni x_0$ with $F|_V\colon V\to F(V)$ a diffeomorphism onto the open set $W:=F(V)\ni y_0$; write $H:=(F|_V)^{-1}\colon W\to V$, a smooth map.
> >
> > We claim $G|_W=H$. Let $y\in W$. By surjectivity of $F|_V$ onto $W$ there is $x\in V$ with $F(x)=y$, and $H(y)=x$. But $F$ is injective on all of $X$, so $x$ is the unique global preimage of $y$, whence $G(y)=x=H(y)$. Thus $G$ agrees with the smooth map $H$ on the open neighbourhood $W$ of $y_0$, so $G$ is smooth at $y_0$. As $y_0\in Y$ was arbitrary, $G$ is smooth on $Y$. Therefore $F$ is a diffeomorphism. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $U(1)$ act on $S^{2n-1}$ by scalar multiplication, with quotient $\mathbb{CP}^{n-1}$ and quotient map $\pi$.
>
> **Part I — dimension.** By Lemma 1 the action is smooth, free (the only $z\in U(1)$ fixing a point $w\in S^{2n-1}$ is $z=1$, because some coordinate $w_k$ is nonzero and $zw_k=w_k$ cancels to $z=1$), and proper ($U(1)$ is compact, so the map $(z,w)\mapsto(z\cdot w,w)$ is proper). Hence the quotient manifold theorem applies and endows $\mathbb{CP}^{n-1}$ with a unique smooth structure of dimension
> $$\dim_{\mathbb{R}}\mathbb{CP}^{n-1}=\dim_{\mathbb{R}}S^{2n-1}-\dim_{\mathbb{R}}U(1)=(2n-1)-1=2(n-1),$$
> for which $\pi$ is a smooth submersion admitting smooth local sections and satisfying the universal property. This is part 1.
>
> **Part II — compactness and connectedness.** By Lemma 2, $\mathbb{CP}^{n-1}=\pi(S^{2n-1})$ is the continuous image of the sphere $S^{2n-1}$, which is compact (closed and bounded in $\mathbb{R}^{2n}$, by Heine–Borel) and, since $2n-1\ge 1$, path-connected hence connected. Continuous images preserve both properties, so $\mathbb{CP}^{n-1}$ is compact and connected. This is part 2.
>
> **Part III — the diffeomorphism $\widetilde{\operatorname{Hopf}}\colon\mathbb{CP}^1\to S^2$.** Take $n=2$.
>
> *Step 0 — preconditions.* By Part I, $\mathbb{CP}^1$ is a smooth $2$-manifold and $\pi\colon S^3\to\mathbb{CP}^1$ is a smooth submersion with the universal property; $S^2\subset\mathbb{R}^3$ is a smooth $2$-manifold; and $\operatorname{Hopf}\colon S^3\to S^2$ is smooth, being the restriction to $S^3$ of the map $\mathbb{C}^2\setminus\{w_2=w_1=0\}\to\mathbb{R}^3$ given by the same rational formula with nonvanishing denominator $4\lvert w_2\rvert^2+\lvert w_1\rvert^2$, and taking values in $S^2$ by Lemma 3.
>
> *Step 1 — existence and smoothness of the induced map.* By Lemma 3, $\operatorname{Hopf}$ is constant on the $U(1)$-orbits. The universal property of the quotient (Part I) then produces a unique map $\widetilde{\operatorname{Hopf}}\colon\mathbb{CP}^1\to S^2$ with $\widetilde{\operatorname{Hopf}}\circ\pi=\operatorname{Hopf}$, and this $\widetilde{\operatorname{Hopf}}$ is smooth. On representatives it is $[w]\mapsto\operatorname{Hopf}(w)$.
>
> *Step 2 — bijectivity.* By Lemma 3, the fibres of $\operatorname{Hopf}$ are exactly the $U(1)$-orbits; equivalently $\widetilde{\operatorname{Hopf}}([w])=\widetilde{\operatorname{Hopf}}([w'])$ holds if and only if $[w]=[w']$, so $\widetilde{\operatorname{Hopf}}$ is injective. By Lemma 4, $\widetilde{\operatorname{Hopf}}$ is surjective (its image contains $\widetilde{\operatorname{Hopf}}(U_2)\cup\widetilde{\operatorname{Hopf}}(U_1)=(S^2\setminus\{S\})\cup(S^2\setminus\{N\})=S^2$). Hence $\widetilde{\operatorname{Hopf}}$ is a bijection.
>
> *Step 3 — local diffeomorphism.* By Lemma 4, on the chart $U_2$ the map is $\widetilde{\operatorname{Hopf}}=\Phi_2\circ c_2$ with $\Phi_2(\zeta)=\frac{1}{4+\lvert\zeta\rvert^2}(4\zeta,4-\lvert\zeta\rvert^2)$ a diffeomorphism $\mathbb{C}\to S^2\setminus\{S\}$ (its inverse being the stereographic projection $(y,y_3)\mapsto\frac{2y}{1+y_3}$), and on $U_1$ it is $\Phi_1\circ c_1$ with $\Phi_1$ a diffeomorphism $\mathbb{C}\to S^2\setminus\{N\}$. Since $U_1\cup U_2=\mathbb{CP}^1$, the map $\widetilde{\operatorname{Hopf}}$ restricts to a diffeomorphism onto an open set on a neighbourhood of every point, i.e. it is a local diffeomorphism; in particular its differential has maximal rank $2$ everywhere, which is item I1.5.4.
>
> *Step 4 — conclude.* By Steps 1–3, $\widetilde{\operatorname{Hopf}}$ is a smooth, bijective, local diffeomorphism. By Lemma 5 (a smooth bijective local diffeomorphism is a diffeomorphism), $\widetilde{\operatorname{Hopf}}\colon\mathbb{CP}^1\to S^2$ is a diffeomorphism. In particular $\mathbb{CP}^1$ and $S^2$ are diffeomorphic. This is part 3, and the theorem is proved. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemann surfaces and the complex structure of $\mathbb{CP}^1$.** In complex analysis the Riemann sphere $\widehat{\mathbb{C}}=\mathbb{C}\cup\{\infty\}$ is built by gluing two copies of $\mathbb{C}$ along $z\mapsto 1/z$. The theorem applies because the two affine charts $U_2,U_1$ of $\mathbb{CP}^1$ with coordinates $\zeta,\eta$ glue by exactly $\eta=1/\zeta$, and the diffeomorphism $\widetilde{\operatorname{Hopf}}$ carries this complex-analytic sphere to the round metric sphere $S^2$. It is non-obvious because it says the *smooth* structure coming from an abstract free quotient coincides with the one coming from holomorphic charts; students who only know $\widehat{\mathbb{C}}$ analytically are surprised the quotient $S^3/U(1)$ gives the same object.

**Quantum mechanics and the Bloch sphere.** The state space of a single qubit is the set of complex lines in $\mathbb{C}^2$, that is, $\mathbb{CP}^1$; physicists draw it as the Bloch sphere $S^2$ and read a qubit as a point $(\text{latitude},\text{longitude})$. The theorem applies because the identification "line in $\mathbb{C}^2$" $\leftrightarrow$ "point of $S^2$" used throughout quantum information is precisely $\widetilde{\operatorname{Hopf}}$, with the overall phase of a state vector being the $U(1)$-orbit that is quotiented out. It is non-obvious that the Bloch-sphere picture is a genuine diffeomorphism rather than a heuristic; the maximal-rank computation is what guarantees smooth families of qubit states correspond to smooth curves on $S^2$.

**Fluid dynamics and the Hopf fibration of a vector field.** In magnetohydrodynamics and in the study of knotted field lines, one seeks divergence-free fields on $S^3\subset\mathbb{R}^4$ whose integral curves are the Hopf circles. The theorem applies because those circles are exactly the fibres of $\operatorname{Hopf}$, whose base — now known to be a genuine $S^2$ — parametrises the field lines; a field line is a point of $S^2$, and linking of field lines is the linking of Hopf circles. It is non-obvious because the pleasant round base is not visible from the $\mathbb{R}^4$ picture until the quotient is identified with $S^2$ by this theorem.

---

# Bridges

- **[[Def - The Hopf Map]]** (Algebraic Topology III) — the same map, read as the generator of $\pi_3(S^2)$. There the Hopf map is presented as the quotient $S^3\to S^3/U(1)=\mathbb{CP}^1$ followed by the identification $\mathbb{CP}^1\cong S^2$; the present theorem *is* that identification, made explicit and shown to be a diffeomorphism in Bär's stereographic normalisation. Composing the quotient map $\pi$ with $\widetilde{\operatorname{Hopf}}$ recovers Bär's $\operatorname{Hopf}$, and the two normalisations (the factor-$4$ stereographic form here, the $(2w_1\overline{w_2},\lvert w_1\rvert^2-\lvert w_2\rvert^2)$ form there) differ by an orientation-preserving isometry of $S^2$, so both present the same fibration.

- **[[Def - The Hopf Bundle]]** (Gauge Theory III) — the principal $U(1)$-bundle $U(1)\hookrightarrow S^3\xrightarrow{\pi}\mathbb{CP}^1$ whose base this theorem identifies with $S^2$. The construction turns the free proper action of Lemma 1 into a principal bundle; its total space is $S^3$, its structure group $U(1)$, and its base the two-sphere via $\widetilde{\operatorname{Hopf}}$. This is the bundle whose first Chern number is $\pm 1$ and which generates every Hermitian line bundle on $S^2$; the diffeomorphism proved here is what lets one transport the tautological bundle $\mathcal{O}(-1)\to\mathbb{CP}^1$ onto the round sphere.

- **[[Ex - The Hopf Map is a Submersion]]** (Differential Geometry IV) — the complementary fact that $\operatorname{Hopf}\colon S^3\to S^2$ is a submersion. Where that exercise computes the rank of $\operatorname{Hopf}$ on the total space directly, the present proof obtains maximal rank of the *induced* map $\widetilde{\operatorname{Hopf}}$ through a local section, reducing the rank question to the transparency of the inverse stereographic formula; the two are related by $\operatorname{Hopf}=\widetilde{\operatorname{Hopf}}\circ\pi$ and $d\pi$ being surjective.

- **[[Ex - The Scalar Action of U(1) on Odd Spheres is Free]]** — the freeness half of Lemma 1, isolated as a drill. It supplies exactly the hypothesis that lets the quotient manifold theorem manufacture $\mathbb{CP}^{n-1}$, and it identifies the transitive case $n=1$ ($\mathbb{CP}^0$ a point) as the boundary of the phenomenon.

---

# Unlocked by This

> [!tip] The Fubini–Study metric *(from Kähler geometry)*
> Once $\mathbb{CP}^1\cong S^2$ is a diffeomorphism, one can ask which metric on $S^2$ the projective structure prefers. Pushing the Fubini–Study metric of $\mathbb{CP}^1$ forward through $\widetilde{\operatorname{Hopf}}$ yields a round metric on $S^2$ (of total area $\pi$ in the standard normalisation), and the Hopf map becomes a Riemannian submersion from the round $S^3$. This is the base case of the Fubini–Study family on all $\mathbb{CP}^{n-1}$. See **Def - The Fubini–Study Metric**.

> [!tip] Instantons on $S^4$ and the basic bundle *(from Gauge Theory)*
> The identification of the base of the Hopf fibration as a genuine sphere is the two-dimensional shadow of the quaternionic Hopf fibration $S^3\hookrightarrow S^7\to S^4$, whose associated $SU(2)$-bundle carries the basic instanton. The pattern "free proper action $\Rightarrow$ smooth quotient $\Rightarrow$ the quotient is a sphere" recurs there with $U(1)$ replaced by $SU(2)$. See **Def - The Basic Instanton on S^4**.
