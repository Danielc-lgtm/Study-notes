---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Sphere Bundles and Mapping Tori"
  - "Thm - The Mapping Torus of a Diffeomorphism is a Fibre Bundle over the Circle"
  - "Def - Fibre Bundle"
tags: [geometry, gauge-theory, fibre-bundles, mobius, nontriviality]
---

# Problem Statement

The **Möbius strip** is, in the language of §3.1, the mapping torus of a single sign flip. Fix the fibre $F=\mathbb{R}$ and the diffeomorphism $\phi=-\operatorname{id}\colon\mathbb{R}\to\mathbb{R}$, $\phi(x)=-x$, and form the mapping torus
$$E:=E_{-\operatorname{id}}=\mathbb{Z}\backslash(\mathbb{R}\times\mathbb{R}),\qquad k\cdot(t,f)=(t+k,(-1)^{k}f),\qquad \pi\big([t,f]\big)=[t]\in S^{1}=\mathbb{Z}\backslash\mathbb{R}.$$
By the mapping-torus theorem $(E,\pi,S^{1})$ is a fibre bundle with typical fibre $\mathbb{R}$. The task has two parts.

**(a) Identification.** Show that $(E,\pi,S^{1})$ is one and the same object as the **Möbius line bundle** constructed in Differential Geometry VI — the quotient $\mathbb{R}^{2}/\!\sim$ with $(x,y)\sim(x+1,-y)$ and projection $[x,y]\mapsto[x]$ — and that it carries a canonical rank-$1$ real vector-bundle structure.

**(b) Nontriviality.** Show that $(E,\pi,S^{1})$ is **not** isomorphic, as a fibre bundle over $S^{1}$, to the trivial bundle $S^{1}\times\mathbb{R}$. Equivalently, there is no global trivialisation.

> [!warning] Convention: fibre $(-1,1)$ versus fibre $\mathbb{R}$
> Bär's Example 2.1.5 takes the fibre to be the open interval $F=(-1,1)$, so that the total space is the classical bounded open Möbius strip; Differential Geometry VI takes the fibre to be $\mathbb{R}$, so that the total space is a genuine line bundle. The two are isomorphic bundles. Any **odd** diffeomorphism $h\colon(-1,1)\to\mathbb{R}$ — for instance $h(x)=\tan(\pi x/2)$, which satisfies $h(-x)=-h(x)$ — intertwines the two $\mathbb{Z}$-actions, $h((-1)^{k}x)=(-1)^{k}h(x)$, and therefore descends to a fibre-preserving diffeomorphism $E_{-\operatorname{id}}^{(-1,1)}\xrightarrow{\ \sim\ }E_{-\operatorname{id}}^{\mathbb{R}}$ over $\operatorname{id}_{S^{1}}$. We work throughout with $F=\mathbb{R}$; the argument below never uses more of $F$ than that it is a connected $1$-manifold on which $0$ is the unique fixed point of $\phi$ and whose complement $F\setminus\{0\}$ has two components, so it applies verbatim to $(-1,1)$.

**Recall:**

The mapping torus, the standing hypothesis that it is a bundle, and the notion of triviality are the following.

![[Def - Sphere Bundles and Mapping Tori#The mapping torus]]

![[Thm - The Mapping Torus of a Diffeomorphism is a Fibre Bundle over the Circle#Statement]]

For triviality we use the definition from the fibre-bundle page: a fibre bundle $(E,\pi,B)$ with typical fibre $F$ is **trivial** if and only if it is isomorphic to the product bundle $(B\times F,\operatorname{pr}_{1},B)$, equivalently if and only if it admits a global trivialisation $\psi\colon E\to B\times F$ with $\operatorname{pr}_{1}\circ\psi=\pi$.

![[Def - Fibre Bundle#The Definition]]

Finally, the companion vector-bundle statement — that the Möbius line bundle has no nowhere-vanishing section — is proved in Differential Geometry VI and restated where we use it:

![[Ex - The Möbius Bundle is Nontrivial#Problem Statement]]

---

# Convergent Strategy

**Problem class.** This is a *nontriviality* problem: we must exhibit a property that the mapping torus $E$ possesses and that the product bundle $S^{1}\times\mathbb{R}$ does not, and which is preserved by every fibre-bundle isomorphism. The generic obstruction for a bundle over the circle is that its total space is "twisted"; the concrete, coordinate-level form of that twist is that the sign flip $\phi=-\operatorname{id}$ swaps the two sides of the zero section. The whole difficulty is to turn "twist" into a genuine invariant that an isomorphism cannot destroy.

**Assumption pattern.** The bundle is built from a *reflection* of the fibre, $x\mapsto-x$, which fixes exactly one point, $0$, and interchanges the two components of $\mathbb{R}\setminus\{0\}$. Two structural consequences follow immediately and drive the solution: first, because $\phi(0)=0$, the constant value $0$ defines a global section — the **zero (core) section** $s_{0}[t]=[t,0]$; second, because $\phi$ swaps the two sides, one can walk along the base circle once and come back on the *other* side of the core, so that the core section does **not** separate the total space. A product bundle has the opposite behaviour: any section separates $S^{1}\times\mathbb{R}$ into an "above" piece and a "below" piece. Connectedness of the complement of the core is the invariant.

**Theorem routing.** The mapping torus is a bundle by [[Thm - The Mapping Torus of a Diffeomorphism is a Fibre Bundle over the Circle|the mapping-torus theorem]]; part (I) of that theorem furnishes the two-arc atlas whose seam transition is $\phi$. Part (a) is a direct comparison of two quotient constructions, using the [[Def - Sphere Bundles and Mapping Tori|mapping-torus definition]] and the [[Ex - The Möbius Bundle is Nontrivial|Differential Geometry VI construction of the Möbius line bundle]]. Part (b) routes through elementary point-set topology of the quotient: build the core section from $\phi(0)=0$; prove its complement path-connected by an explicit loop that uses the seam sign flip; and prove that in any product bundle the complement of a section is disconnected, because a fibre-bundle isomorphism carries the core section to the graph of a smooth function $h\colon S^{1}\to\mathbb{R}$, whose complement is separated by the sign of $f-h([t])$. The clash of the two connectedness verdicts is the contradiction.

**Key decision point.** The subtle choice is *which* notion of triviality to disprove and by *which* argument. The Möbius object is simultaneously a plain fibre bundle (fibre $\mathbb{R}$, arbitrary fibre diffeomorphisms allowed) and a vector bundle (fibrewise-linear maps only). Nontriviality as a *fibre* bundle is the stronger statement, because it forbids more isomorphisms, and it is the one the mapping-torus setting asks for; the naive "a trivialisation gives a nowhere-vanishing section, kill it by the intermediate value theorem" argument, taken literally, only forbids *linear* trivialisations and so proves the weaker vector-bundle nontriviality. We therefore run the connectedness argument, which is the correct rigorous form of the same core-circle idea, and then show it specialises exactly to the nowhere-vanishing-section contradiction on the vector-bundle structure, recovering the Differential Geometry VI statement as a corollary.

---

# Legal Operations Used

1. **Descend a map through the quotient (operation: universal property of a covering quotient).** The zero section, the projection, and the comparison map in part (a) are all defined on the covering space $\mathbb{R}\times\mathbb{R}$ and shown to be constant on $\mathbb{Z}$-orbits, hence to descend to smooth maps on $E$; this is the universal property of the properly-discontinuous quotient recalled on the [[Def - Sphere Bundles and Mapping Tori|mapping-torus page]] and used there to build $\pi$ itself.

2. **Read a section off its principal part in a trivialisation (operation: local frames span sections).** On each trivialising arc we describe a section of $E$ by a scalar function, the coordinate of its value in the fibre $\mathbb{R}$; this is how the core section and, later, the image section $\Psi\circ s_{0}$ are handled.

3. **Transport a topological property along a homeomorphism (operation: invariance under isomorphism).** A fibre-bundle isomorphism is in particular a homeomorphism, so it preserves connectedness of the complement of the core section. This is the single move that converts the coordinate computation into an obstruction.

4. **Compare two quotient constructions by matching fundamental domains (operation: recognise the same bundle).** Part (a) matches $\mathbb{Z}\backslash(\mathbb{R}\times\mathbb{R})$ with $\mathbb{R}^{2}/\!\sim$ by observing the two equivalence relations are generated by the same identification, so the identity of $\mathbb{R}^{2}$ descends to a bundle isomorphism.

---

# Hints

> [!note]- Hint 1
> Write down the two equivalence relations — the one generating the mapping torus of $-\operatorname{id}$ and the one defining the Differential Geometry VI Möbius bundle — as identifications on $\mathbb{R}^{2}$. Are they the same relation?

> [!note]- Hint 2
> The reflection $\phi(x)=-x$ has a fixed point. What global section of $E$ does that fixed point give you, and why is it well defined on the quotient?

> [!note]- Hint 3
> Call the image of that section the core circle $C$. Try to walk from a point just *above* the core at the base point $[0]$ to a point just *below* it, staying off $C$ the whole time. Use the seam: pushing the first coordinate from $0$ to $1$ returns you to the same fibre but flips the sign of the second coordinate.

> [!note]- Hint 4
> Suppose $\Psi\colon E\to S^{1}\times\mathbb{R}$ were a fibre-bundle isomorphism. Because $\Psi$ commutes with the projection, the image $\Psi(C)$ of the core section is again a section of a bundle — but of the *product* bundle. What does a section of $S^{1}\times\mathbb{R}$ look like, and does its complement stay connected?

> [!note]- Hint 5
> A section of $S^{1}\times\mathbb{R}$ is the graph of a smooth function $h\colon S^{1}\to\mathbb{R}$. On the complement of the graph the quantity $f-h([t])$ never vanishes, so its sign is a continuous, locally constant function taking both values. Two connectedness verdicts, one for $E\setminus C$ and one for $(S^{1}\times\mathbb{R})\setminus\Psi(C)$, cannot both hold.

---

# Solution

**Plan.** In part (a) we observe that the mapping torus of $-\operatorname{id}$ and the Differential Geometry VI Möbius line bundle are literally the same quotient with the same projection, and note that the fibrewise-linear structure makes it a rank-$1$ vector bundle. In part (b) we build the zero (core) section from the fixed point $\phi(0)=0$; prove that its complement in $E$ is path-connected by an explicit path that exploits the seam sign flip; prove that the complement of *any* section in a product bundle $S^{1}\times\mathbb{R}$ is disconnected; and derive a contradiction from the assumption that a fibre-bundle isomorphism $E\cong S^{1}\times\mathbb{R}$ exists. A closing remark specialises the argument to the linear structure and recovers the nowhere-vanishing-section obstruction.

**Step 1: The mapping torus of $-\operatorname{id}$ is the Differential Geometry VI Möbius bundle — what part (a) achieves.**

> [!note]- Derivation
> The mapping torus $E=E_{-\operatorname{id}}$ is by definition the orbit space of the $\mathbb{Z}$-action on $\mathbb{R}\times\mathbb{R}$ given by $k\cdot(t,f)=(t+k,(-1)^{k}f)$ (by the [[Def - Sphere Bundles and Mapping Tori|mapping-torus definition]] with $\phi=-\operatorname{id}$, so that $\phi^{k}(f)=(-1)^{k}f$). The orbit relation is generated by its generator $k=1$, namely
> $$(t,f)\ \sim\ (t+1,-f)\qquad\text{(the case }k=1\text{; all others are its iterates).}$$
> The Differential Geometry VI Möbius line bundle is $\mathbb{R}^{2}/\!\sim$ for the relation generated by $(x,y)\sim(x+1,-y)$ (by [[Ex - The Möbius Bundle is Nontrivial|its construction]]). Renaming the coordinates $(t,f)=(x,y)$, these are the **same** equivalence relation on $\mathbb{R}^{2}$, so
> $$E_{-\operatorname{id}}=\mathbb{R}^{2}/\!\sim\ \ \text{as sets, and the identity of }\mathbb{R}^{2}\text{ descends to a bijection commuting with the quotient maps.}$$
> The two projections agree: $\pi([t,f])=[t]$ in both cases (the mapping-torus projection is induced by $\operatorname{pr}_{1}$, and the Differential Geometry VI projection is $[x,y]\mapsto[x]$). Because both quotient maps $\mathbb{R}^{2}\to E$ are smooth covering maps (each action is free and properly discontinuous, by the quotient theorem recalled on the mapping-torus page), the descended identity is a diffeomorphism over $\operatorname{id}_{S^{1}}$, that is, a fibre-bundle isomorphism. Hence $E_{-\operatorname{id}}$ and the Differential Geometry VI Möbius bundle are the same bundle.
>
> **Vector-bundle structure.** The fibre diffeomorphism $\phi=-\operatorname{id}$ is a **linear** map of $\mathbb{R}$. Consequently the covering identification $(t,f)\sim(t+1,-f)$ is linear in the fibre coordinate $f$, so each fibre $E_{[t]}=\{[t,f]:f\in\mathbb{R}\}$ inherits a well-defined real vector-space structure ($[t,f]+[t,f']:=[t,f+f']$ and $\lambda[t,f]:=[t,\lambda f]$, independent of the representative because $-(f+f')=(-f)+(-f')$ and $-(\lambda f)=\lambda(-f)$), and the arc trivialisations of the mapping-torus theorem are fibrewise linear. Thus $(E,\pi,S^{1})$ is a rank-$1$ real vector bundle — the Möbius line bundle — which is what part (a) asserts.

**Step 2: The zero (core) section and its image $C$.**

> [!note]- Derivation
> Because $\phi(0)=-0=0$, the point $(t,0)$ has $\mathbb{Z}$-orbit $\{(t+k,0):k\in\mathbb{Z}\}$, and the assignment $t\mapsto[t,0]$ is constant on $\mathbb{Z}$-orbits of the base ($[t,0]=[t+1,0]$). By the universal property of the covering quotient (operation 1), the smooth map $\mathbb{R}\to E$, $t\mapsto[t,0]$, descends to a smooth section
> $$s_{0}\colon S^{1}\to E,\qquad s_{0}([t])=[t,0],\qquad \pi\circ s_{0}=\operatorname{id}_{S^{1}},$$
> the **zero section** of the line bundle (its value in every fibre is the zero vector). Write $C:=s_{0}(S^{1})=\{[t,0]:t\in\mathbb{R}\}\subset E$ for its image, the **core circle**. Every point of $E$ has a unique representative $(t,f)$ with $t\in[0,1)$, and
> $$E\setminus C=\{[t,f]:f\neq0\},$$
> a well-posed description because $f\neq0$ forces every representative $(t+k,(-1)^{k}f)$ to have nonzero second coordinate.

**Step 3: $E\setminus C$ is path-connected.**

> [!note]- Derivation
> We connect an arbitrary point of $E\setminus C$ to one of the two reference points $[0,\tfrac12]$ or $[0,-\tfrac12]$, and then connect those two to each other, all inside $E\setminus C$.
>
> **Slide the base coordinate to $0$.** Let $[t,f]\in E\setminus C$ with representative $t\in[0,1)$ and $f\neq0$. The path
> $$\alpha(r)=[(1-r)t,\ f],\qquad r\in[0,1],$$
> is continuous (it is the image under the quotient map of the continuous path $r\mapsto((1-r)t,f)$), has $\alpha(0)=[t,f]$ and $\alpha(1)=[0,f]$, and stays in $E\setminus C$ because its second coordinate is the constant $f\neq0$.
>
> **Slide within the fibre over $[0]$ to $\pm\tfrac12$.** If $f>0$, the path $\beta(r)=[0,(1-r)f+r\tfrac12]$, $r\in[0,1]$, joins $[0,f]$ to $[0,\tfrac12]$ and has second coordinate $(1-r)f+r\tfrac12>0$ throughout (a convex combination of two positive numbers), so it avoids $C$. If $f<0$, the analogous path with endpoint value $-\tfrac12$ joins $[0,f]$ to $[0,-\tfrac12]$ through negative values, again avoiding $C$.
>
> **Cross the seam.** Finally,
> $$\gamma(r)=[r,\tfrac12],\qquad r\in[0,1],$$
> is continuous, has $\gamma(0)=[0,\tfrac12]$ and, using the generating identification $(1,\tfrac12)\sim(1-1,(-1)^{-1}\tfrac12)=(0,-\tfrac12)$,
> $$\gamma(1)=[1,\tfrac12]=[0,-\tfrac12]\qquad\text{(by }(t,f)\sim(t+1,-f)\text{ with }t=0,\ f=-\tfrac12\text{).}$$
> Its second coordinate is the constant $\tfrac12\neq0$, so $\gamma$ stays in $E\setminus C$. Concatenating $\alpha$, then $\beta$, then (if the fibre coordinate landed on the negative side) nothing more, and using $\gamma$ to pass between the two reference points, any two points of $E\setminus C$ are joined by a path in $E\setminus C$. Hence **$E\setminus C$ is path-connected**, and in particular connected.

**Step 4: In a product bundle, the complement of any section is disconnected.**

> [!note]- Derivation
> Let $\sigma\colon S^{1}\to S^{1}\times\mathbb{R}$ be any continuous section, that is $\operatorname{pr}_{1}\circ\sigma=\operatorname{id}$. Then $\sigma([t])=([t],h([t]))$ for a continuous function $h\colon S^{1}\to\mathbb{R}$ (its second component; operation 2), so the image $\Gamma:=\sigma(S^{1})=\{([t],h([t])):[t]\in S^{1}\}$ is the graph of $h$. Define
> $$\rho\colon(S^{1}\times\mathbb{R})\setminus\Gamma\to\{-1,+1\},\qquad \rho([t],f)=\operatorname{sgn}\big(f-h([t])\big).$$
> On the complement $f\neq h([t])$, so $f-h([t])\neq0$ and $\rho$ is well defined; it is continuous because $\operatorname{sgn}$ is continuous away from $0$ and $([t],f)\mapsto f-h([t])$ is continuous. It is **surjective**: for any fixed $[t_{0}]$ the points $([t_{0}],h([t_{0}])+1)$ and $([t_{0}],h([t_{0}])-1)$ lie in the complement and have $\rho=+1$ and $\rho=-1$ respectively. A continuous surjection onto the two-point discrete space $\{-1,+1\}$ exhibits its domain as a disjoint union of two nonempty (relatively) open sets $\rho^{-1}(+1)$ and $\rho^{-1}(-1)$. Hence **$(S^{1}\times\mathbb{R})\setminus\Gamma$ is disconnected**.

**Step 5: Conclusion of part (b).**

> [!note]- Derivation
> Suppose, for contradiction, that $(E,\pi,S^{1})$ is trivial: there is a fibre-bundle isomorphism $\Psi\colon E\to S^{1}\times\mathbb{R}$, a diffeomorphism with $\operatorname{pr}_{1}\circ\Psi=\pi$. Then $\Psi\circ s_{0}$ is a section of the product bundle, since $\operatorname{pr}_{1}\circ(\Psi\circ s_{0})=\pi\circ s_{0}=\operatorname{id}_{S^{1}}$; by Step 4 its image $\Gamma=\Psi(C)$ is the graph of a smooth $h\colon S^{1}\to\mathbb{R}$, and $(S^{1}\times\mathbb{R})\setminus\Gamma$ is disconnected. But $\Psi$ is a homeomorphism carrying $C$ onto $\Gamma$, hence restricts to a homeomorphism $E\setminus C\to(S^{1}\times\mathbb{R})\setminus\Gamma$ (operation 3), and connectedness is a homeomorphism invariant. This contradicts Step 3, where $E\setminus C$ was shown connected. The assumption was false: **$(E,\pi,S^{1})$ admits no global trivialisation, so it is a nontrivial fibre bundle.**

> [!note]- Complete formal solution
> **Part (a).** By the [[Def - Sphere Bundles and Mapping Tori|mapping-torus definition]] with $\phi=-\operatorname{id}$, the space $E=E_{-\operatorname{id}}=\mathbb{Z}\backslash(\mathbb{R}\times\mathbb{R})$ is the quotient by the $\mathbb{Z}$-action $k\cdot(t,f)=(t+k,(-1)^{k}f)$, whose orbit relation is generated by $(t,f)\sim(t+1,-f)$. This is the identical relation defining the Differential Geometry VI Möbius line bundle $\mathbb{R}^{2}/\!\sim$, $(x,y)\sim(x+1,-y)$, under $(t,f)=(x,y)$, and both projections send a class to $[t]=[x]\in S^{1}$. Since each quotient map is a smooth covering (free, properly discontinuous $\mathbb{Z}$-action), the identity of $\mathbb{R}^{2}$ descends to a diffeomorphism $E_{-\operatorname{id}}\xrightarrow{\sim}\mathbb{R}^{2}/\!\sim$ over $\operatorname{id}_{S^{1}}$, a fibre-bundle isomorphism. Because $\phi=-\operatorname{id}$ is linear, the fibre coordinate identification is linear, so $[t,f]+[t,f']:=[t,f+f']$ and $\lambda\cdot[t,f]:=[t,\lambda f]$ are representative-independent ($-(f+f')=(-f)+(-f')$, $-(\lambda f)=\lambda(-f)$); with the fibrewise-linear arc trivialisations of [[Thm - The Mapping Torus of a Diffeomorphism is a Fibre Bundle over the Circle|the mapping-torus theorem]], $(E,\pi,S^{1})$ is a rank-$1$ real vector bundle.
>
> **Part (b).** *Core section.* Since $\phi(0)=0$, the map $t\mapsto[t,0]$ is constant on base orbits and descends to a smooth section $s_{0}\colon S^{1}\to E$, $s_{0}([t])=[t,0]$, with image $C=\{[t,0]\}$; and $E\setminus C=\{[t,f]:f\neq0\}$.
>
> *Complement of the core is connected.* Fix $[t,f]\in E\setminus C$ with $t\in[0,1)$, $f\neq0$. The path $\alpha(r)=[(1-r)t,f]$ ($r\in[0,1]$) lies in $E\setminus C$ (second coordinate $f\neq0$) and joins $[t,f]$ to $[0,f]$. The path $\beta(r)=[0,(1-r)f\pm r\tfrac12]$ (sign chosen equal to $\operatorname{sgn}f$) lies in $E\setminus C$ (a convex combination of two same-sign nonzero reals) and joins $[0,f]$ to $[0,\pm\tfrac12]$. The path $\gamma(r)=[r,\tfrac12]$ ($r\in[0,1]$) lies in $E\setminus C$ (second coordinate $\tfrac12\neq0$) and joins $[0,\tfrac12]$ to $[1,\tfrac12]=[0,-\tfrac12]$ (by the identification $(t,f)\sim(t+1,-f)$ at $t=0$, $f=-\tfrac12$). Concatenating, every point of $E\setminus C$ is path-joined to $[0,\tfrac12]$, so $E\setminus C$ is path-connected, hence connected.
>
> *Complement of a section in the product is disconnected.* For any continuous section $\sigma$ of $S^{1}\times\mathbb{R}$, $\sigma([t])=([t],h([t]))$ with $h$ continuous, and $\rho([t],f)=\operatorname{sgn}(f-h([t]))$ is a continuous surjection $(S^{1}\times\mathbb{R})\setminus\sigma(S^{1})\to\{-1,+1\}$ (well defined off the graph; both values attained at $([t_{0}],h([t_{0}])\pm1)$). Hence that complement is disconnected.
>
> *Contradiction.* If $\Psi\colon E\to S^{1}\times\mathbb{R}$ were a fibre-bundle isomorphism, then $\Psi\circ s_{0}$ is a section of the product bundle, $\Gamma:=\Psi(C)$ is its graph, and $(S^{1}\times\mathbb{R})\setminus\Gamma$ is disconnected; but $\Psi$ restricts to a homeomorphism $E\setminus C\to(S^{1}\times\mathbb{R})\setminus\Gamma$, and $E\setminus C$ is connected — a contradiction, since connectedness is preserved by homeomorphisms. Therefore $E$ has no global trivialisation and is a **nontrivial fibre bundle**. $\qquad\blacksquare$

> [!note]- The same argument in the vector-bundle picture — recovering the nowhere-vanishing-section obstruction
> The connectedness proof above is the correct rigorous form of the informal route "a trivialisation gives a nowhere-vanishing section, killed by the intermediate value theorem along the core circle". To see the equivalence, restrict attention to the vector-bundle structure and to *linear* trivialisations. A vector-bundle isomorphism $\Psi\colon E\to S^{1}\times\mathbb{R}$ carries the zero section $s_{0}$ to the zero section (linear maps send $0$ to $0$), so the function $h$ of Step 4 is identically $0$ and $\Gamma=S^{1}\times\{0\}$. In that case the section $\sigma([t])=\Psi^{-1}([t],1)$ is a genuinely **nowhere-vanishing** global section: its value in each fibre is $\Psi^{-1}$ of a nonzero vector, hence nonzero. This is exactly the object whose non-existence is proved in Differential Geometry VI:
> $$\text{(Differential Geometry VI) the Möbius line bundle admits no smooth nowhere-vanishing global section,}$$
> where the proof lifts such a $\sigma$ to a smooth $\tilde\sigma\colon\mathbb{R}\to\mathbb{R}$ with $\tilde\sigma(x+1)=-\tilde\sigma(x)$, so that $\tilde\sigma(1)=-\tilde\sigma(0)$ have opposite signs and the **intermediate value theorem** forces a zero of $\tilde\sigma$ in $(0,1)$, contradicting nowhere-vanishing. That statement, restated here, is proved in full on [[Ex - The Möbius Bundle is Nontrivial]]. Thus the vector-bundle nontriviality is a special case of the fibre-bundle nontriviality established above; the general fibre-bundle statement is stronger because it forbids nonlinear trivialisations as well, which is precisely why the crude section argument had to be upgraded to the connectedness argument.

> [!warning] Illegal but tempting shortcut — reading nontriviality off local triviality
> It is tempting to argue "the seam transition of the mapping torus is $\phi=-\operatorname{id}\neq\operatorname{id}$, so the bundle is nontrivial". This is not a proof: a *nontrivial-looking* transition function can be a coboundary, describing a bundle that is in fact trivial (the tangent bundle of the circle has a nonconstant transition function in a natural atlas yet is trivial). Triviality is a property of the transition **cocycle modulo coboundaries**, not of a single chosen transition map. The extra condition that *would* make the shortcut legal is to check that the transition class is nontrivial in $H^{1}(S^{1};\{\pm1\})=\mathbb{Z}/2$ — which is a computation of the same difficulty as the argument we gave, and is carried out for this cocycle in [[Ex - Reconstructing the Möbius Bundle from a Z over 2 Cocycle]].

---

# Key Takeaways

**A fixed point of the gluing map produces a canonical section, and how that section sits in the total space is a bundle invariant.** The reflection $\phi=-\operatorname{id}$ fixes $0$, and that single fact hands us the zero (core) section for free; the entire nontriviality proof is then a statement about the *complement* of that section. This is a reusable template: whenever a bundle is built as a mapping torus $E_{\phi}$ and $\phi$ has a fixed point $p_{0}$, the constant $p_{0}$ gives a global section, and the separation properties of its complement — does removing it disconnect the total space? — distinguish the bundle from the product. The trigger is "a bundle presented by a gluing map with a fixed point"; the reaction is "form that section and study its complement".

**Nontriviality is proved by transporting a topological invariant, not by inspecting a transition function.** A single transition map can look twisted and yet be gauge-equivalent to the identity, so the honest obstruction must be invariant under all admissible isomorphisms. Here the invariant is connectedness of the complement of the core section, which any fibre-bundle isomorphism — being a homeomorphism over the base — must preserve. The diagnostic transfers directly to other settings: to separate a bundle $P$ from a model $P_{0}$, find a feature (a section's complement, an orientation of the total space, a characteristic number, a holonomy) that is manifestly invariant under the isomorphisms in play and takes different values on $P$ and $P_{0}$. The weaker the class of allowed isomorphisms, the more features become invariant, and the finer the distinctions one can draw — which is why fibre-bundle nontriviality is a stronger claim than vector-bundle nontriviality and needed the sharper, non-linear-proof connectedness argument.

**The mapping-torus and vector-bundle descriptions of the Möbius strip are two faces of one object, and the sign flip is the shared source of the twist.** Part (a) showed that Bär's mapping torus of $-\operatorname{id}$ and the Differential Geometry VI Möbius line bundle are literally the same quotient; the linearity of $-\operatorname{id}$ is exactly what upgrades the fibre bundle to a vector bundle, and the fibre choice $(-1,1)$ versus $\mathbb{R}$ is immaterial because an odd diffeomorphism intertwines the actions. The transferable lesson is that a fibre bundle whose structure group can be reduced to a *linear* group (here $\{\pm1\}\subset\mathrm{GL}(1,\mathbb{R})$) is a vector bundle, and every extra structure one imposes both narrows the isomorphisms and sharpens the invariants: the same twist that makes the complement of the core connected is the twist that obstructs a nowhere-vanishing section, is the nontrivial class in $H^{1}(S^{1};\mathbb{Z}/2)$, and is the first Stiefel–Whitney class $w_{1}\neq0$. Companion exercises: [[Ex - The Klein Bottle as a Mapping Torus]] runs the same machine on the reflection of $S^{1}$ and detects the twist through non-orientability of the total space; [[Ex - A Flat Connection on the Möbius Line Bundle with Holonomy Minus One]] detects the identical twist through the holonomy $-1$ of a flat connection.
