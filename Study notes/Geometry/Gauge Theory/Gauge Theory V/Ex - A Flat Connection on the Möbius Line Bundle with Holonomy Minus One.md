---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Flat Connections and Monodromy Representations of the Fundamental Group"
  - "Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group"
  - "Def - Associated Bundle"
  - "Def - Flat Connection"
  - "Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop"
tags: [geometry, gauge-theory]
---

# Problem Statement

The flat-connection/monodromy correspondence says that flat bundles over $M$ are the same data as representations of $\pi_1(M)$. The smallest non-trivial instance is the circle: $\pi_1(S^1,\ast)\cong\mathbb Z$, and the smallest non-trivial group into which $\mathbb Z$ can map faithfully-enough-to-matter is $O(1)=\{\pm1\}$. The representation $\rho\colon\mathbb Z\to O(1)$ that sends the generator to $-1$ ought therefore to produce the simplest non-trivial flat line bundle over $S^1$. This exercise verifies, from the ground up, that this flat bundle is the **Möbius line bundle**, that its canonical flat connection has **holonomy $-1$**, and that the Möbius bundle carries **no** flat connection whose holonomy is trivial — so its non-triviality is an obstruction living entirely in the monodromy.

Throughout, $S^1=\mathbb R/\mathbb Z$ with base point $\ast=[0]$, and $q\colon\mathbb R\to S^1$, $q(t)=[t]$, is the universal covering map. By [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|the universal-cover theorem]] together with [[Thm - Pi_1 of S^1 is Z|π₁(S¹) ≅ ℤ]], the deck group of $q$ is $\mathbb Z$ acting on $\mathbb R$ by translation, $n\cdot t=t+n$, and this identifies $\mathbb R$ with the principal $\mathbb Z$-bundle whose associated bundles realise flat bundles over $S^1$. Let
$$\rho\colon\mathbb Z\longrightarrow O(1)=\{\pm1\}\subset GL_1(\mathbb R),\qquad \rho(n)=(-1)^n,\ \text{ so } \rho(1)=-1,$$
and form the associated real line bundle $L:=\mathbb R\times_\rho\mathbb R$.

**Problem.** Prove the following.

1. **(Identification.)** $L=\mathbb R\times_\rho\mathbb R$ is a real line bundle over $S^1$, and it is (isomorphic to) the Möbius line bundle — the total space is the open Möbius band, obtained from $[0,1]\times\mathbb R$ by gluing $(1,v)$ to $(0,-v)$.
2. **(Holonomy of the canonical connection.)** The canonical flat connection $\nabla^\rho$ on $L$ (the one whose $\rho$-equivariant constant maps are the parallel sections) has holonomy $-1$ around the generator of $\pi_1(S^1)$; equivalently its monodromy representation is $\rho$ itself.
3. **(Non-triviality via monodromy.)** $L$ admits no flat connection with trivial holonomy. Equivalently, $L$ is not the trivial line bundle: it has no nowhere-vanishing global section.

**Recall:**

The objects in play are the universal cover of the circle and its deck action, the associated bundle of a representation, the canonical flat connection built from the product connection, and the monodromy of a flat connection.

![[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group#Statement]]

For the circle this specialises to: $q\colon\mathbb R\to S^1=\mathbb R/\mathbb Z$ is the universal cover; the deck group is $\pi_1(S^1,\ast)\cong\mathbb Z$ acting on $\mathbb R$ by the translations $t\mapsto t+n$; and $q\colon\mathbb R\to S^1$ is thereby a principal $\mathbb Z$-bundle with the discrete group $\mathbb Z$ acting (this is verified independently in [[Ex - The Universal Cover of the Circle and of the Torus]]).

![[Def - Associated Bundle#The Definition]]

Given a principal $\Gamma$-bundle $\pi\colon\tilde M\to M$ (here $\Gamma=\mathbb Z$, $\tilde M=\mathbb R$, $M=S^1$) and a representation $\rho\colon\Gamma\to GL(V)$, the **associated bundle** is $\tilde M\times_\rho V:=(\tilde M\times V)/\Gamma$ with the relation $[\tilde x\cdot n,\,v]=[\tilde x,\,\rho(n)v]$; its projection is $[\tilde x,v]\mapsto\pi(\tilde x)$ and its fibres are copies of $V$. For $V=\mathbb R$ and $\rho$ as above this gives $L=\mathbb R\times_\rho\mathbb R$ with $[t+n,\,v]=[t,\,(-1)^n v]$.

![[Def - Flat Connection#The Definition]]

A connection is **flat** when its curvature vanishes. On $\tilde M\times_\rho V$ there is a canonical flat connection $\nabla^\rho$ characterised by $\pi^{*}\nabla^\rho s=d\hat s$, where a section $s$ is identified with the $\Gamma$-equivariant map $\hat s\colon\tilde M\to V$ (equivariance $\hat s(\tilde x\cdot n)=\rho(n)^{-1}\hat s(\tilde x)$); its parallel sections are those with $\hat s$ locally constant.

![[Thm - Flat Connections and Monodromy Representations of the Fundamental Group#Statement]]

The monodromy representation of $\nabla^\rho$ at the base point is $\rho$; conversely every flat connection arises this way, and gauge-equivalent flat connections have conjugate monodromy ([[Ex - Gauge-Equivalent Flat Connections have Conjugate Monodromy]]). For a flat connection, parallel transport around a loop depends only on its homotopy class ([[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|homotopy-invariance]]).

---

# Convergent Strategy

**Problem class.** This is a *concrete realisation* problem: an abstract construction (associated bundle of a representation, canonical flat connection, monodromy) is instantiated on the smallest interesting example so that every arrow of the general theory becomes a hand computation. Parts 1 and 2 are direct verifications; part 3 is an *obstruction* argument — proving a negative ("no flat connection with trivial holonomy exists") by showing that such a connection would force a nowhere-vanishing section, which the geometry forbids.

**Assumption pattern.** The representation $\rho(1)=-1$ is the entire input; everything else is forced. The recognisable pattern is "line bundle over $S^1$ $\leftrightarrow$ sign of the transition around the loop": a real line bundle over $S^1$ is trivial or Möbius according as its single gluing sign is $+1$ or $-1$, and that sign is exactly $\rho(1)$. For part 3 the pattern is "flat + trivial holonomy $\Rightarrow$ path-independent parallel transport $\Rightarrow$ a global parallel frame $\Rightarrow$ triviality," so proving non-triviality amounts to exhibiting the local obstruction to a global nowhere-zero section.

**Theorem routing.** Part 1: unwind [[Def - Associated Bundle|the associated-bundle relation]] $[t+n,v]=[t,(-1)^n v]$, restrict representatives to $t\in[0,1]$, and read off the Möbius gluing $[1,v]=[0,-v]$. Part 2: use the canonical connection's defining property (parallel $=$ constant lift), lift the generating loop to the segment $[0,1]\subset\mathbb R$, transport $[0,v_0]$ to $[1,v_0]=[0,-v_0]$, and read the holonomy $-1$; cross-check against [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the monodromy theorem]], which predicts monodromy $=\rho$. Part 3: assume a flat connection with trivial holonomy; use [[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|homotopy-invariance]] plus trivial holonomy to make parallel transport path-independent; build a global nowhere-vanishing parallel section; observe this trivialises $L$; contradict it with the intermediate value theorem applied to the equivariant description of sections.

**Key decision point.** The decisive move in part 3 is to encode a global section of $L$ as a single function $\hat s\colon\mathbb R\to\mathbb R$ with $\hat s(t+1)=-\hat s(t)$, because then non-vanishing becomes visibly impossible: $\hat s(0)$ and $\hat s(1)=-\hat s(0)$ have opposite signs, so $\hat s$ must cross zero. Choosing this representation — rather than arguing with local trivialisations and cocycles — turns the obstruction into one application of the intermediate value theorem.

---

# Legal Operations Used

The topic page for Gauge Theory V is not yet assembled, so the operations are named descriptively; the orchestrator will reconcile the numbering.

1. **Reduce an associated-bundle point to a fundamental-domain representative.** Every class $[t,v]\in L$ has a representative with $t\in[0,1]$, obtained by translating $t$ by an integer and absorbing the sign into $v$ via $[t+n,v]=[t,(-1)^n v]$.

2. **Read a real line bundle over $S^1$ off its single gluing sign.** After restricting to $[0,1]$, the only identification is $[1,v]=[0,-v]$; the sign $-1$ is the transition function around the loop, which is the definition of the Möbius bundle.

3. **Compute holonomy through the canonical connection's parallel sections.** For $\nabla^\rho$, parallel sections along a curve are those with constant lift $\hat s$; transporting an initial fibre value along the lifted segment and re-expressing the endpoint in the base-point fibre gives the holonomy.

4. **Turn trivial holonomy of a flat connection into path-independent transport, then into a global parallel section.** Flatness plus trivial holonomy makes parallel transport depend on neither the path nor its homotopy class, so transporting one nonzero vector defines a global nowhere-vanishing parallel section.

5. **Detect non-triviality by the intermediate value theorem on the equivariant description of sections.** A global section of $L$ is a continuous $\hat s\colon\mathbb R\to\mathbb R$ with $\hat s(t+1)=-\hat s(t)$; opposite signs at $0$ and $1$ force a zero, so no nowhere-vanishing global section exists.

---

# Hints

> [!note]- Hint 1
> Write down the equivalence relation defining $L=\mathbb R\times_\rho\mathbb R$ explicitly: which pairs $(t,v)$ and $(t',v')$ are identified? Use it to bring every point into the range $t\in[0,1]$, and see what happens at the two ends $t=0$ and $t=1$.

> [!note]- Hint 2
> You should find $[1,v]=[0,-v]$. That single sign flip *is* the Möbius band. For the connection, remember that "canonical flat connection" means: pull back to the cover $\mathbb R\times\mathbb R$ where it is the product (trivial) connection, so parallel means "constant in the $v$-coordinate on the cover."

> [!note]- Hint 3
> The generator of $\pi_1(S^1)$ lifts to the segment $t\in[0,1]$ in $\mathbb R$. Parallel transport of $[0,v_0]$ keeps the cover-coordinate constant, so it ends at $[1,v_0]$. Now use $[1,v_0]=[0,-v_0]$ to express the answer back in the fibre over $\ast=[0]$. What linear map of that fibre did you just compute?

> [!note]- Hint 4
> For part 3, suppose $\nabla'$ is flat with trivial holonomy. Then parallel transport around any loop is the identity, and (flatness) transport depends only on homotopy class, so transport between two points is completely path-independent. Fix $v_0\ne0$ over $\ast$ and transport it everywhere: you get a global section that never vanishes (transport is a linear isomorphism). Such a section trivialises the line bundle.

> [!note]- Hint 5
> To finish part 3, show $L$ has *no* nowhere-vanishing global section. A section corresponds to a continuous $\hat s\colon\mathbb R\to\mathbb R$ with $\hat s(t+1)=-\hat s(t)$. If $\hat s(0)\ne0$, compare the signs of $\hat s(0)$ and $\hat s(1)$ and apply the intermediate value theorem on $[0,1]$.

---

# Solution

The three parts share one device: a section of $L$ is the same thing as a function $\hat s\colon\mathbb R\to\mathbb R$ on the cover satisfying the equivariance $\hat s(t+1)=-\hat s(t)$, and a *parallel* section for the canonical connection is one with $\hat s$ constant on the cover. Part 1 unwinds the gluing to recognise the Möbius band; part 2 transports a constant lift once around and reads off the sign; part 3 shows the equivariance $\hat s(t+1)=-\hat s(t)$ is incompatible with $\hat s$ being nowhere zero, which obstructs both triviality and any flat connection with trivial holonomy.

## Part 1 — $L$ is the Möbius line bundle

**Step 1: $L$ is a real line bundle over $S^1$.**

The projection $[t,v]\mapsto[t]$ is a well-defined surjection with fibres $\cong\mathbb R$, and the two arcs of $S^1$ give local trivialisations, so $L$ is a rank-one real vector bundle.

> [!note]- Derivation
> By [[Def - Associated Bundle|the associated-bundle construction]], $L=(\mathbb R\times\mathbb R)/\mathbb Z$ where $n\in\mathbb Z$ identifies
> $$(t+n,\,v)\ \sim\ (t,\,(-1)^n v),\qquad\text{equivalently}\qquad [t+n,v]=[t,(-1)^n v] \qquad \text{(associated-bundle relation with } \rho(n)=(-1)^n\text{).}$$
> Define $\pi\colon L\to S^1$ by $\pi[t,v]=[t]=q(t)$. This is well defined: if $[t,v]=[t',v']$ then $t'=t+n$ for some $n$, so $[t']=[t+n]=[t]$ in $S^1$ (translation by an integer is the identity on $\mathbb R/\mathbb Z$). It is surjective because $q$ is. The fibre over $[t_0]$ is $\{[t_0,v]:v\in\mathbb R\}$, and $v\mapsto[t_0,v]$ is a bijection onto it: it is onto by definition, and injective because $[t_0,v]=[t_0,v']$ forces $t_0=t_0+n$ hence $n=0$ hence $v=v'$. So each fibre is a copy of $\mathbb R$.
>
> **Local triviality.** Cover $S^1$ by the two open arcs $U_1=q\big((0,1)\big)$ and $U_2=q\big((-\tfrac12,\tfrac12)\big)$. Over $U_1$ the restriction $(0,1)\ni t\mapsto[t]$ is a homeomorphism onto $U_1$, so every point of $\pi^{-1}(U_1)$ has a unique representative $[t,v]$ with $t\in(0,1)$, and $\Psi_1\colon\pi^{-1}(U_1)\to U_1\times\mathbb R$, $[t,v]\mapsto([t],v)$, is a fibrewise-linear homeomorphism. The same construction works over $U_2$: the restriction $(-\tfrac12,\tfrac12)\ni t\mapsto[t]$ is a homeomorphism onto $U_2$, so every point of $\pi^{-1}(U_2)$ has a unique representative with $t\in(-\tfrac12,\tfrac12)$, and $\Psi_2\colon\pi^{-1}(U_2)\to U_2\times\mathbb R$, $[t,v]\mapsto([t],v)$, is a fibrewise-linear homeomorphism. Since $U_1\cup U_2=S^1$, the bundle $L$ is a real line bundle over $S^1$.

**Step 2: The transition around the loop is $-1$; $L$ is the Möbius bundle.**

Restricting representatives to $t\in[0,1]$ shows the only identification is $[1,v]=[0,-v]$, so $L$ is $[0,1]\times\mathbb R$ with $(1,v)$ glued to $(0,-v)$ — the Möbius line bundle.

> [!note]- Derivation
> **Fundamental-domain representatives.** Every class $[t,v]\in L$ has a representative with $t\in[0,1]$: choose $n\in\mathbb Z$ with $t-n\in[0,1)$ and use $[t,v]=[t-n,(-1)^{-n}v]=[t-n,(-1)^n v]$ (operation 1; note $(-1)^{-n}=(-1)^n$). Thus the continuous surjection
> $$\Phi\colon[0,1]\times\mathbb R\longrightarrow L,\qquad \Phi(t,v)=[t,v]$$
> is onto. We determine when $\Phi(t,v)=\Phi(t',v')$ for $t,t'\in[0,1]$. This requires $t'=t+n$ with $t,t'\in[0,1]$, so $n\in\{-1,0,1\}$.
> - $n=0$: $t'=t$ and $v'=v$ (no identification beyond equality).
> - $n=1$: $t'=t+1\in[0,1]$ forces $t=0$, $t'=1$, and then $[t',v']=[1,v']=[0,-v']$, so $\Phi(0,v)=\Phi(1,v')$ iff $v=-v'$, i.e. $(1,v')\sim(0,-v')$.
> - $n=-1$: the same identification read backwards.
>
> Therefore the only non-trivial gluing on $[0,1]\times\mathbb R$ is
> $$(1,\,v)\ \longleftrightarrow\ (0,\,-v),\qquad\text{i.e.}\qquad [1,v]=[0,-v] \qquad \text{(operation 2; the loop transition function is } -1\text{).}$$
> This is exactly the standard presentation of the total space of the **Möbius line bundle**: the strip $[0,1]\times\mathbb R$ with the two ends glued by the reflection $v\mapsto -v$. The transition function of $L$ relative to the trivialisations of Step 1, computed on the overlap containing $t=0\sim1$, is multiplication by $-1$; a real line bundle over $S^1$ with transition sign $-1$ is the Möbius bundle (and with sign $+1$ the trivial bundle). Hence $L\cong$ Möbius line bundle. Its non-triviality is proved intrinsically in Part 3, and is also recorded in [[Ex - The Möbius Bundle is Nontrivial]].

## Part 2 — the canonical flat connection has holonomy $-1$

**Step 3: The canonical connection is flat and its parallel sections have constant lift.**

By construction $\nabla^\rho$ is the descent of the product connection on $\mathbb R\times\mathbb R$; it is flat, and a section is $\nabla^\rho$-parallel along a curve exactly when its lift $\hat s$ is constant there.

> [!note]- Derivation
> Identify a section $s\in\Gamma(L)$ with the equivariant map $\hat s\colon\mathbb R\to\mathbb R$ via $s([t])=[t,\hat s(t)]$; well-definedness of $s$ requires $[t+n,\hat s(t+n)]=[t,\hat s(t)]$, and since $[t+n,\hat s(t+n)]=[t,(-1)^n\hat s(t+n)]$ this is the equivariance
> $$\hat s(t+n)=(-1)^n\hat s(t)\qquad(n\in\mathbb Z),\qquad\text{in particular}\qquad \hat s(t+1)=-\hat s(t) \qquad \text{(descent condition for a section of } L\text{).}$$
> The [[Def - Flat Connection|canonical flat connection]] $\nabla^\rho$ is defined by $q^{*}\nabla^\rho s=d\hat s$: on the cover $\mathbb R$ it is the product (trivial) connection $d$ in the coordinate $v$. Its curvature is the descent of the curvature of $d$, which is $0$; hence $\nabla^\rho$ is flat. A section $s$ is parallel along a curve $c$ in $S^1$ iff $(c^{*}\nabla^\rho)s=0$ iff $d\hat s=0$ along the lift $\tilde c$ of $c$, i.e. iff $\hat s$ is constant along $\tilde c$ (operation 3).

**Step 4: Transport around the generator, and read off holonomy $-1$.**

Lifting the generating loop to the segment $[0,1]$ and transporting a constant lift gives $PT_\gamma\colon v_0\mapsto -v_0$, so the holonomy is $-1$ and the monodromy representation is $\rho$.

> [!note]- Derivation
> Let $\gamma$ be the loop $\gamma(t)=[t]$, $t\in[0,1]$, based at $\ast=[0]$; it generates $\pi_1(S^1,\ast)\cong\mathbb Z$ (by [[Thm - Pi_1 of S^1 is Z|π₁(S¹) ≅ ℤ]], the generator is the class of once around). Its lift starting at $0\in\mathbb R$ is $\tilde\gamma(t)=t$, ending at $\tilde\gamma(1)=1$.
>
> Fix an initial fibre element $[0,v_0]\in L_\ast$. By Step 3 the $\nabla^\rho$-parallel section $s$ along $\gamma$ with $s(\gamma(0))=[0,v_0]$ is the one whose lift is the constant $\hat s\equiv v_0$ along $\tilde\gamma$; its value at the endpoint of the lift is
> $$s(\gamma(1)) \;=\; [\tilde\gamma(1),\,\hat s(1)] \;=\; [1,\,v_0] \qquad \text{(parallel } \Rightarrow \text{ constant lift; } \tilde\gamma(1)=1\text{).}$$
> Re-express this in the fibre over $\ast=[0]$ using the gluing $[1,v_0]=[0,-v_0]$ from Part 1:
> $$s(\gamma(1)) \;=\; [1,v_0] \;=\; [0,\,-v_0] \qquad \text{(associated-bundle relation, } n=1\text{).}$$
> Therefore parallel transport of $\nabla^\rho$ around $\gamma$, expressed in the fibre $L_\ast$ under the linear identification $v\mapsto[0,v]$, is
> $$PT_\gamma\colon L_\ast\to L_\ast,\qquad v_0\longmapsto -v_0,\qquad\text{i.e. multiplication by } -1 \qquad \text{(operation 3).}$$
> By [[Def - Holonomy Group of a Connection|the definition of holonomy]] the holonomy of $\gamma$ is this map, $-1\in O(1)$, so
> $$\operatorname{Hol}_\ast(\nabla^\rho)=\{\pm1\}=O(1),$$
> generated by $-1$. Since $\gamma$ generates $\pi_1(S^1,\ast)$ and $\nabla^\rho$ is flat, [[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|homotopy-invariance]] makes $[\gamma]\mapsto\operatorname{hol}(\gamma)$ a representation, and it sends the generator $1\in\mathbb Z$ to $-1$. Hence the monodromy representation of $\nabla^\rho$ is
> $$\rho_{\nabla^\rho}(n)=(-1)^n=\rho(n) \qquad \text{(agreeing with the prediction of the monodromy theorem, part (a): monodromy of } \nabla^\rho \text{ is } \rho\text{).}$$
> This confirms both that the holonomy is $-1$ and that it is exactly the representation $\rho$ we started from.

## Part 3 — $L$ admits no flat connection with trivial holonomy

**Step 5: $L$ has no nowhere-vanishing global section.**

A global section of $L$ is a continuous $\hat s\colon\mathbb R\to\mathbb R$ with $\hat s(t+1)=-\hat s(t)$; the intermediate value theorem forces such an $\hat s$ to vanish, so no global section is nowhere-zero. In particular $L$ is non-trivial.

> [!note]- Derivation
> By Step 3, a global continuous section $s\in\Gamma(L)$ is the same as a continuous map $\hat s\colon\mathbb R\to\mathbb R$ with $\hat s(t+1)=-\hat s(t)$ for all $t$, and $s$ is nowhere vanishing iff $\hat s(t)\ne0$ for all $t$.
>
> Suppose, for contradiction, that such a nowhere-vanishing $\hat s$ exists. Evaluate the equivariance at $t=0$:
> $$\hat s(1) \;=\; -\hat s(0) \qquad \text{(descent condition at } t=0\text{).}$$
> Since $\hat s(0)\ne0$, the values $\hat s(0)$ and $\hat s(1)=-\hat s(0)$ are non-zero and of **opposite sign**. The function $\hat s$ is continuous on the interval $[0,1]$, so by the **intermediate value theorem** there is $t_\ast\in(0,1)$ with $\hat s(t_\ast)=0$ (operation 5). This contradicts $\hat s$ being nowhere zero. Hence $L$ has no nowhere-vanishing global section.
>
> A real line bundle is trivial if and only if it admits a nowhere-vanishing global section (given such a section $s$, the map $S^1\times\mathbb R\to L$, $([t],\lambda)\mapsto\lambda\,s([t])$, is a bundle isomorphism, being a fibrewise linear isomorphism because $s([t])\ne0$ spans the one-dimensional fibre; conversely the constant section $1$ of $S^1\times\mathbb R$ is nowhere vanishing). Therefore $L$ is **not** the trivial bundle.

**Step 6: No flat connection on $L$ has trivial holonomy.**

If a flat connection had trivial holonomy, parallel transport would be path-independent and would produce a nowhere-vanishing global section, trivialising $L$ — contradicting Step 5.

> [!note]- Derivation
> **Named goal.** We must show: there is no flat connection $\nabla'$ on $L$ with $\operatorname{Hol}_\ast(\nabla')=\{1\}$. Assume such a $\nabla'$ exists and derive a contradiction.
>
> **Transport is path-independent.** Let $x,y\in S^1$ and let $c_0,c_1$ be two piecewise-smooth paths from $x$ to $y$. Then $c_1^{-1}*c_0$ (traverse $c_0$, then $c_1$ backwards) is a loop at $x$. Its parallel transport is $PT^{\nabla'}_{c_1^{-1}*c_0}=(PT^{\nabla'}_{c_1})^{-1}\circ PT^{\nabla'}_{c_0}$ (parallel transport of a concatenation is the composite, and of a reversed path the inverse). Because $\nabla'$ has trivial holonomy, this loop transports to the identity:
> $$(PT^{\nabla'}_{c_1})^{-1}\circ PT^{\nabla'}_{c_0}=\operatorname{id}_{L_x}\qquad\Longrightarrow\qquad PT^{\nabla'}_{c_0}=PT^{\nabla'}_{c_1} \qquad \text{(trivial holonomy: every loop transports to } \operatorname{id}\text{).}$$
> Thus $\nabla'$-parallel transport between any two points is independent of the path. (Flatness is what guarantees the holonomy group is generated by actual loop-transports and that the notion is well behaved; homotopy-invariance is not even needed here, only that concatenation and reversal behave functorially and that all loops transport trivially.)
>
> **Build a global parallel section.** Fix $v_0\in L_\ast$ with $v_0\ne0$. Define $s\colon S^1\to L$ by
> $$s(x):=PT^{\nabla'}_{c_x}(v_0),\qquad c_x\text{ any piecewise-smooth path from }\ast\text{ to }x.$$
> This is well defined by path-independence, and it is smooth because parallel transport depends smoothly on the endpoint (locally, solve the transport ODE with smooth dependence on parameters). It is a section: $s(x)\in L_x$. It is parallel: for any path $c$ from $x$ to $y$, $PT^{\nabla'}_{c}(s(x))=PT^{\nabla'}_{c}\circ PT^{\nabla'}_{c_x}(v_0)=PT^{\nabla'}_{c*c_x}(v_0)=s(y)$, so $\nabla' s=0$. It is nowhere vanishing: each $PT^{\nabla'}_{c_x}\colon L_\ast\to L_x$ is a linear isomorphism, so $s(x)=PT^{\nabla'}_{c_x}(v_0)\ne0$ because $v_0\ne0$ (operation 4).
>
> **Contradiction.** We have produced a nowhere-vanishing global section $s$ of $L$. By Step 5 no such section exists. This is the contradiction: the assumption that $L$ carries a flat connection with trivial holonomy is untenable. Therefore **$L$ admits no flat connection with trivial holonomy.** $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** With $\rho\colon\mathbb Z\to O(1)$, $\rho(1)=-1$, the bundle $L=\mathbb R\times_\rho\mathbb R$ over $S^1=\mathbb R/\mathbb Z$ is the Möbius line bundle; its canonical flat connection $\nabla^\rho$ has holonomy $-1$ around the generator of $\pi_1(S^1)$; and $L$ carries no flat connection with trivial holonomy.
>
> *Identification.* $L=(\mathbb R\times\mathbb R)/\mathbb Z$ with $[t+n,v]=[t,(-1)^n v]$; $\pi[t,v]=[t]$ makes it a real line bundle over $S^1$ (fibres $\cong\mathbb R$; the two arcs of $S^1$ trivialise it). Restricting representatives to $t\in[0,1]$, the only identification is $[1,v]=[0,-v]$, so $L$ is $[0,1]\times\mathbb R$ glued by $(1,v)\sim(0,-v)$: the Möbius line bundle, transition sign $-1$.
>
> *Holonomy.* A section is a map $\hat s\colon\mathbb R\to\mathbb R$ with $\hat s(t+1)=-\hat s(t)$, via $s([t])=[t,\hat s(t)]$; $\nabla^\rho$ is the descent of the product connection $d$ on $\mathbb R\times\mathbb R$, hence flat, with parallel sections those having constant lift. The generator $\gamma(t)=[t]$, $t\in[0,1]$, lifts to $\tilde\gamma(t)=t$; transporting $[0,v_0]$ keeps the lift constant, ending at $[1,v_0]=[0,-v_0]$. So $PT_\gamma=(-1)\colon L_\ast\to L_\ast$, giving holonomy $-1$ and monodromy $\rho_{\nabla^\rho}(n)=(-1)^n=\rho(n)$.
>
> *Non-triviality.* If $\hat s\colon\mathbb R\to\mathbb R$ is continuous with $\hat s(t+1)=-\hat s(t)$ and $\hat s(0)\ne0$, then $\hat s(0),\hat s(1)=-\hat s(0)$ have opposite signs, so $\hat s$ vanishes on $(0,1)$ by the intermediate value theorem; hence $L$ has no nowhere-vanishing global section and is non-trivial. Now suppose $\nabla'$ were flat on $L$ with trivial holonomy. For any two paths $c_0,c_1$ from $x$ to $y$, the loop $c_1^{-1}*c_0$ transports to the identity, so $PT^{\nabla'}_{c_0}=PT^{\nabla'}_{c_1}$: transport is path-independent. Fixing $v_0\ne0$ in $L_\ast$ and setting $s(x)=PT^{\nabla'}_{c_x}(v_0)$ gives a well-defined smooth nowhere-vanishing global section (each transport is a linear isomorphism), trivialising $L$ — contradicting non-triviality. Hence no flat connection on $L$ has trivial holonomy. $\blacksquare$
>
> The three facts fit the monodromy dictionary exactly: $L$ corresponds to the non-trivial class $[\rho]\in\mathcal R(S^1;O(1))=\operatorname{Hom}(\mathbb Z,\{\pm1\})=\{\pm1\}$, its canonical connection realises $\rho$, and "no trivial-holonomy flat connection" is the statement that $[\rho]\ne[\text{trivial}]$.

> [!warning] Illegal but tempting shortcut
> One might try to prove Part 3 by asserting "$L$ is non-orientable, and non-orientable line bundles are non-trivial." Over $S^1$ this is true, but stating it is not a proof unless orientability of line bundles has been developed and connected to triviality; moreover it does not by itself rule out a flat connection with trivial holonomy — that step still needs the parallel-transport argument of Step 6. The intermediate-value-theorem argument of Step 5 is self-contained and avoids importing orientation theory; it is the honest route. The general trap is to substitute a name ("non-orientable", "non-trivial $w_1$") for the local obstruction it summarises; the exercise wants the obstruction exhibited, namely the sign flip $\hat s(t+1)=-\hat s(t)$ forcing a zero.

---

# Key Takeaways

**A real line bundle over $S^1$ is completely classified by one sign, and that sign is $\rho(1)$.** The reusable principle is that flat bundles over a space are read off representations of its fundamental group, and for $S^1$ the fundamental group is $\mathbb Z$, so a flat $G$-bundle is a single element $\rho(1)\in G$ up to conjugacy. For real line bundles $G=GL_1(\mathbb R)=\mathbb R^\times$, whose components are detected by sign, and the two flat line bundles with holonomy of a given sign are the trivial bundle ($+$) and the Möbius bundle ($-$). The trigger condition is "a bundle over a circle (or a bundle whose base retracts to a circle, or a bundle restricted to a loop)"; the reaction is "look at the single transition sign, equivalently the holonomy around the loop." This is the one-dimensional shadow of the whole theory: the first Stiefel–Whitney class $w_1$ of a real line bundle over any base is exactly the homomorphism $\pi_1\to\{\pm1\}$ recording holonomy signs of a flat connection, and its non-vanishing on a loop is the obstruction we exhibited by hand.

**Non-triviality of a bundle can be an obstruction that lives entirely in the holonomy of flat connections.** The striking content of Part 3 is not merely that $L$ is non-trivial, but that its non-triviality *cannot be undone by any choice of flat connection*: every flat connection on $L$ has non-trivial holonomy. The mechanism is a clean chain — flat plus trivial holonomy makes parallel transport path-independent, path-independent transport of one nonzero vector is a global nowhere-vanishing parallel frame, and a global nowhere-vanishing section trivialises a line bundle. So "trivial-holonomy flat connection exists" is equivalent to "the bundle is trivial (as a flat bundle)." The transferable diagnostic: to prove a bundle admits no flat connection of a given holonomy type, assume one, build the global frame that its holonomy type permits, and contradict a known topological obstruction to that frame. Here the obstruction is the intermediate-value sign flip; in higher rank it is a characteristic class.

**Encoding sections of an associated bundle as equivariant functions on the cover turns bundle questions into elementary analysis.** Every computation above ran through the identification $\Gamma(L)\cong\{\hat s\colon\mathbb R\to\mathbb R\ \text{continuous}\mid \hat s(t+1)=-\hat s(t)\}$. This is the special case $V=\mathbb R$, $\Gamma=\mathbb Z$, $\rho(1)=-1$ of the general dictionary "sections of $\tilde M\times_\rho V$ $=$ $\Gamma$-equivariant maps $\tilde M\to V$", and it converts geometric statements into statements about a single real function: a section is a function with a twist condition, a parallel section is a constant function (for the canonical connection), holonomy is the value of the twist over one period, and non-vanishing is obstructed by a sign change. The general lesson for spaced practice is that whenever a bundle is presented as an associated bundle of a cover, the first move is to pass to equivariant functions on the cover, where connections become ordinary derivatives and parallel transport becomes solving an ordinary differential equation with a boundary twist. A companion drill is [[Ex - Parallel Sections of the Flat Bundle of a Representation]], which runs the same identification to show global parallel sections of $\tilde M\times_\rho V$ are exactly the $\rho(\pi_1)$-invariant vectors of $V$ — here $\{v:\rho(1)v=v\}=\{v:-v=v\}=\{0\}$, consistent with the absence of a nowhere-vanishing parallel section found in Part 3.
