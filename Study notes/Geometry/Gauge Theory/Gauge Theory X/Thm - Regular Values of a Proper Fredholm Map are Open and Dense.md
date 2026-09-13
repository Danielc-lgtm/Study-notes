---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Fredholm Map and Its Index"
  - "Def - Regular Value and Transversality for Fredholm Maps"
  - "Def - Mod-2 Degree of a Proper Fredholm Map"
  - "Thm - Proper Maps are Closed and Fredholm Maps are Locally Proper"
  - "Thm - Sard-Smale Theorem"
  - "Thm - Stabilisation of Fredholm Operators and Continuity of the Kernel"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $X$ and $Y$ are **[[Def - Banach Manifold and Smooth Maps between Banach Spaces|Banach manifolds]]** that are second countable: $X$ is a Hausdorff topological space with a countable base, covered by charts $\phi_\alpha : U_\alpha \to \widetilde{U}_\alpha \subseteq E$ modelled on a fixed Banach space $E$ (the model space of $X$), with smooth transition maps, and likewise $Y$ is modelled on a Banach space $G$. Being second countable and locally metrisable, both $X$ and $Y$ are metrisable (this standing fact from the chapter's opening page is the only topological property of the models we use besides completeness). For a point $x \in X$ we write $T_xX$ for the tangent space, a Banach space isomorphic to $E$ through any chart differential $d_x\phi_\alpha : T_xX \to E$.

A smooth map $F : X \to Y$ is a **[[Def - Fredholm Map and Its Index|Fredholm map]]** if its differential $d_xF : T_xX \to T_{F(x)}Y$ is a **[[Def - Fredholm Operator and Index|Fredholm operator]]** for every $x \in X$; that is, $d_xF$ is a bounded linear map with finite-dimensional kernel $\ker d_xF$, closed range, and finite-dimensional cokernel $\operatorname{coker} d_xF = T_{F(x)}Y / \operatorname{im} d_xF$, and its **index** is the integer $\operatorname{index} d_xF = \dim\ker d_xF - \dim\operatorname{coker} d_xF$. We write $L(E,G)$ for the Banach space of bounded linear operators $E \to G$ with the operator norm $\lVert T \rVert = \sup_{\lVert v\rVert \le 1}\lVert Tv\rVert$, and $\Phi(E,G) \subseteq L(E,G)$ for the subset of Fredholm operators.

A map $F : X \to Y$ is **proper** if the preimage $F^{-1}(K)$ of every compact set $K \subseteq Y$ is compact. Given $F$, a point $x \in X$ is a **critical point** if $d_xF$ is not surjective, and we write
$$\operatorname{Crit}(F) = \{x \in X : d_xF \text{ is not surjective}\}$$
for the set of critical points; a point $y \in Y$ is a **critical value** if $y = F(x)$ for some critical point $x$, so the set of critical values is $F(\operatorname{Crit}(F))$. A point $y \in Y$ is a **[[Def - Regular Value and Transversality for Fredholm Maps|regular value]]** if $d_xF$ is surjective for every $x \in F^{-1}(y)$ — vacuously so when $F^{-1}(y) = \varnothing$. We write
$$\operatorname{Reg}(F) = \{y \in Y : d_xF \text{ is surjective for every } x \in F^{-1}(y)\}$$
for the set of regular values. A subset of a topological space is **[[Def - Dense Subset|dense]]** if its closure is the whole space, and a subset is **[[Def - Residual Set and Generic Property|residual]]** (of second category) if it contains a countable intersection of open dense sets; in a [[Thm - Baire Category Theorem|Baire space]] — and every Banach manifold is one — a residual set is dense.

> [!warning] Convention: regular values are the complement of the critical values
> We adopt the convention (Haydys, §6.2; the customary one in degree theory) that a point $y$ **not** in the image of $F$ is a regular value, because the surjectivity requirement quantifies over the empty preimage vacuously. With this convention the set of regular values is exactly the set-theoretic complement $\operatorname{Reg}(F) = Y \setminus F(\operatorname{Crit}(F))$, which is what makes openness a statement purely about the closedness of $F(\operatorname{Crit}(F))$; this identity is proved as Lemma 1 below.

---

# Statement

> **Theorem (regular values of a proper Fredholm map are open and dense).** Let $X$ and $Y$ be second countable Banach manifolds and let $F : X \to Y$ be a proper Fredholm map. Then the set of regular values
> $$\operatorname{Reg}(F) = \{y \in Y : d_xF \text{ is surjective for every } x \in F^{-1}(y)\}$$
> is **open** and **dense** in $Y$.

This is Step 1 of Haydys' proof of Theorem 166 (the well-definedness and homotopy invariance of the $\mathbb{Z}/2\mathbb{Z}$ degree); it is the geometric input that makes the [[Def - Mod-2 Degree of a Proper Fredholm Map|mod-2 degree]] well-defined at all, and it is proved here in full, with the two gaps Haydys leaves implicit — the closedness of the critical set and the closedness of a proper map — supplied.

---

# Motivation

The whole theory of the degree of a map rests on being able to count preimages of a chosen target point and to know that the count does not depend on which target point was chosen. The counting is only sensible at a **regular value**, where the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] (in its Banach-manifold form) presents the preimage as a smooth manifold of dimension equal to the index, so that for an index-zero map the preimage is a zero-manifold — a discrete set — and, when $F$ is proper, a *finite* set that can be counted. If regular values were rare, or clustered so that one could not move a chosen value slightly and stay regular, this counting programme would collapse: one could not compare the count at two different values, and the number $\deg_2 F = \# F^{-1}(y) \bmod 2$ would depend on an arbitrary choice.

The present theorem removes both dangers at once. **Density** guarantees that regular values exist, indeed sit arbitrarily close to any point of $Y$, so that any target — even a critical value, even a point outside the image — can be approximated by regular values at which the count is defined. **Openness** guarantees that once a regular value is found, a whole neighbourhood of it consists of regular values, so that the count is stable under small perturbations of the target and one may deform the target continuously without ever leaving the regular set except across a nowhere-dense wall of critical values. Together they say that the regular values form a large, robust, connected-enough set on which the degree can be defined and then shown to be locally constant.

The finite-dimensional prototype is Sard's theorem: for a smooth map between finite-dimensional manifolds, almost every value is regular, and the critical values form a set of measure zero, which is in particular nowhere dense, so its complement is dense; when the domain is compact the map is proper and the critical values are closed, giving openness of the regular set for free. The subtlety in the infinite-dimensional setting is twofold. First, "measure zero" has no meaning on an infinite-dimensional Banach manifold, so density cannot come from a measure argument; it comes instead from the [[Thm - Sard-Smale Theorem|Sard–Smale theorem]], which produces a *residual* (rather than full-measure) set of regular values and appeals to the [[Thm - Baire Category Theorem|Baire category theorem]] to conclude density. Second, properness is no longer automatic even when it would be in finite dimensions, so it must be assumed, and it is precisely properness — through the closedness of proper maps — that delivers openness. This division of labour, density from Sard–Smale and openness from properness, is the content of the proof.

---

# Sources and Targets

**Sources (Input Broadening).** The hypothesis is "$F$ is a proper Fredholm map"; the skill is to recognise when a map presented in some other language is secretly of this kind.

The first disguised source is a **semilinear elliptic partial differential operator on a closed manifold, read as a map between Sobolev spaces**. A map of the form $F(u) = L u + N(u)$, with $L$ an elliptic differential operator and $N$ a lower-order nonlinearity, is presented as a differential equation, not as a Fredholm map; but on a closed base manifold elliptic regularity together with the [[Thm - Baire Category Theorem|Rellich–Kondrachov compact embedding]] shows that $L$ (hence $F$, since $N$ is a compact perturbation) has finite-dimensional kernel and cokernel and closed range, so $F$ is Fredholm, and a priori elliptic estimates combined with the same compact embedding show that $F$ is proper on the relevant Sobolev completions. The bridge $B \Rightarrow A$ is "elliptic on a closed manifold $\Rightarrow$ proper Fredholm between Sobolev spaces", and it is non-obvious because it converts the analytic estimates of elliptic theory into the topological hypotheses of degree theory. *Example problem:* show that a nonlinear equation $\Delta u + f(u) = g$ on a closed surface, with $f$ bounded and $C^1$, has a solution for a dense set of right-hand sides $g$, by recognising the left-hand side as a proper Fredholm map of index zero and applying this theorem to produce regular values.

The second disguised source is a **smooth map out of a compact finite-dimensional manifold**. Any smooth map $F : M \to N$ between finite-dimensional manifolds is a Fredholm map, since every linear map between finite-dimensional spaces is Fredholm with index $\dim M - \dim N$; and if $M$ is compact then $F$ is automatically proper, because a closed subset of a compact space is compact. The bridge $B \Rightarrow A$ is "compact domain $\Rightarrow$ proper", and it is easy to state but easy to forget: the whole finite-dimensional degree theory is the special case of the present theorem in which properness is free. *Example problem:* recover the openness and density of regular values for a smooth map $S^n \to \mathbb{R}^{n}$ (compact domain, hence proper) as an instance of this theorem, so that its Brouwer degree is defined.

The third disguised source is a **compact perturbation of a linear isomorphism in the Leray–Schauder style**. A map $F = \operatorname{id} + K$ on a Banach space, or more generally $F = L + K$ with $L$ a linear isomorphism and $K$ a (nonlinear) compact map, has differential $d_xF = L + d_xK$ with $d_xK$ compact; a compact perturbation of an invertible operator is Fredholm of index zero (by the [[Thm - Stabilisation of Fredholm Operators and Continuity of the Kernel|stability of the Fredholm property under compact perturbations]]), so $F$ is a Fredholm map, and under a coercivity or bounded-orbit condition $F$ is proper on closed bounded sets. The bridge $B \Rightarrow A$ is "identity-plus-compact with coercivity $\Rightarrow$ proper Fredholm of index zero", and it is non-obvious because the compactness of $K$ does double duty, giving both the Fredholm property of the differential and the properness of the map. *Example problem:* for an integral equation $u(t) = \int_0^1 k(t,s)\,g(u(s))\,ds + h(t)$ with continuous kernel $k$, recognise the solution map as identity-minus-compact and use this theorem to find a dense set of forcing terms $h$ that are regular values.

**Targets (Output Amplification).** The bare conclusion — an open dense regular set — is the launching point for the entire degree construction.

Combine the conclusion with **connectedness of $Y$ and vanishing index**. When $Y$ is connected and $\operatorname{index} F = 0$, the regular preimages are finite, and openness makes the count $y \mapsto \# F^{-1}(y) \bmod 2$ a locally constant function on the open set $\operatorname{Reg}(F)$; density then lets one connect any two regular values through the regular set (after crossing the nowhere-dense critical wall, controlled by homotopy). The further result $E$ is that $\deg_2 F$ is well defined, independent of the regular value: this is exactly the payoff carried out on [[Thm - Well-Definedness and Homotopy Invariance of the Degree|the degree page]], for which the present theorem is the first step.

Combine the conclusion with **a nonzero degree**. If $\deg_2 F \neq 0$, then some regular value has an odd — in particular nonempty — preimage; density gives regular values arbitrarily close to any prescribed point $y_0 \in Y$, each with nonempty preimage, and properness (through closedness of $F$) forces the limit $y_0$ itself to lie in the image. The further result $E$ is that a proper Fredholm map of nonzero degree is **surjective**, the infinite-dimensional analogue of the fundamental theorem of algebra ([[Thm - Nonzero Degree Implies Surjectivity|nonzero degree implies surjectivity]]).

Combine the conclusion with **a smooth family of such maps parametrised by a Banach manifold $W$**. Applying openness and density fibrewise, together with the [[Thm - Sard-Smale Theorem|Sard–Smale theorem]] applied to the total map, produces a residual set of parameters $w$ for which the fibre map $F_w$ has $y$ as a regular value. The further result $E$ is [[Thm - Parametric Transversality|parametric transversality]]: for a generic parameter the equation $F_w = y$ is cut out transversally, which is the mechanism behind every "for a generic metric the moduli space is a manifold" statement in gauge theory.

---

# Why Is It True

Strip the statement to its logical skeleton. Openness of $\operatorname{Reg}(F)$ is the same as closedness of its complement $Y \setminus \operatorname{Reg}(F)$; and by the convention that unattained points are regular, this complement is exactly the set of critical values $F(\operatorname{Crit}(F))$. So openness reduces to a single assertion: **the set of critical values is closed.** A set of the form $F(A)$ is closed whenever two things hold — the set $A$ being mapped is closed, and the map $F$ carries closed sets to closed sets. Here $A = \operatorname{Crit}(F)$, and both facts are available: the critical set is closed because surjectivity of a Fredholm operator is preserved under small perturbations (so its failure, criticality, is preserved under passage to limits), and $F$ is a closed map because it is proper and the target is metrisable (so a proper map cannot let the image of a closed set accumulate at a point without the point itself being an image).

> **The mechanism in one sentence: critical points form a closed set because surjectivity of a Fredholm operator is an open condition, and a proper map carries that closed set to a closed set of critical values, whose complement — the regular values — is therefore open.**

Density is a different mechanism entirely, and it does not use properness. It is the Sard–Smale theorem: for any Fredholm map between second countable Banach manifolds, the regular values form a residual set, and a residual set in a Baire space is dense. Sard–Smale is the infinite-dimensional replacement for "critical values have measure zero"; it localises the map near each point to a finite-dimensional model (a Kuranishi chart) where the classical Sard theorem applies, and then patches the countably many local statements together using second countability.

The two halves fit because they answer complementary worries. Density says regular values are everywhere — you can always find one near where you want it. Openness says regular values are stable — once you have one, small motions keep it regular. Neither alone would let the degree be defined; together they present $\operatorname{Reg}(F)$ as an open dense set, the natural home for a locally constant integer invariant.

---

# What Makes This Hard

The one genuinely subtle point is the treatment of a regular value $y_0$ **with empty preimage**. Such a point is a regular value by convention, but there is no local structure near it — no preimage points, no local diffeomorphisms, nothing on which to build a neighbourhood of regular values directly. A first attempt at openness, "take a regular value, use the inverse function theorem at each preimage point to get a neighbourhood of regular values", simply has nothing to work with at such a $y_0$ and stalls. The resolution is to prove openness *globally and negatively*, never pointwise: one shows the complement (the critical values) is closed, so its complement is open, and this argument is completely indifferent to whether any given regular value is attained. This is why the proof routes through closedness of $F(\operatorname{Crit}(F))$ rather than through local charts of preimages. The second, easily-skipped point is that closedness of $F(\operatorname{Crit}(F))$ needs *both* inputs: dropping properness lets a smooth non-proper Fredholm map have a critical-value set that fails to be closed (its image can accumulate at a non-attained point), and dropping the openness of surjectivity lets $\operatorname{Crit}(F)$ itself fail to be closed. Haydys writes both facts in a single sentence ("the set of critical points is closed; since any proper map is closed, the set of critical values is closed"); the work is in justifying each clause.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Split the conclusion into openness and density, which use disjoint hypotheses. For openness, prove the set identity $\operatorname{Reg}(F) = Y \setminus F(\operatorname{Crit}(F))$ and then show $F(\operatorname{Crit}(F))$ is closed, by showing $\operatorname{Crit}(F)$ is closed and $F$ is a closed map. For density, quote the Sard–Smale theorem and Baire's theorem.

**Subgoal decomposition:**

1. **Regular values are the complement of the critical values.** Prove $\operatorname{Reg}(F) = Y \setminus F(\operatorname{Crit}(F))$.
   - *Hint:* Unwind both definitions; the only care needed is the empty-preimage case, where both sides contain $y$.
   - *Why needed:* It converts "openness of $\operatorname{Reg}(F)$" into "closedness of $F(\operatorname{Crit}(F))$", the only form the rest of the argument can attack.

2. **The critical set is closed.** Prove $\operatorname{Crit}(F)$ is closed in $X$.
   - *Hint:* In a chart the differential $x \mapsto d_xF$ is a continuous map into $\Phi(E,G)$; the surjective Fredholm operators form an open subset there (openness of surjectivity), so the regular points are open and their complement closed.
   - *Why needed:* Half of the input to "$F(\operatorname{Crit}(F))$ is closed".

3. **A proper map to a metrisable space is closed.** Prove that $F$ carries closed sets to closed sets.
   - *Hint:* $Y$ metrisable means closedness is tested by sequences; a convergent image sequence together with its limit is compact, so properness makes the corresponding domain points live in a compact set, from which a convergent subsequence is extracted.
   - *Why needed:* The other half of the input; together with subgoal 2 it gives that $F(\operatorname{Crit}(F))$ is closed.

4. **Assemble openness.** Combine subgoals 1–3: $\operatorname{Crit}(F)$ closed and $F$ closed give $F(\operatorname{Crit}(F))$ closed, whose complement $\operatorname{Reg}(F)$ is open.
   - *Hint:* Pure set theory once the three subgoals are in hand.
   - *Why needed:* It is the openness half of the theorem.

5. **Density.** Quote the Sard–Smale theorem to get $\operatorname{Reg}(F)$ residual, then Baire to get it dense.
   - *Hint:* Sard–Smale needs only "Fredholm map between second countable Banach manifolds"; properness is not used here.
   - *Why needed:* It is the density half of the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: The regular values are exactly the complement of the critical values
> **Statement:** For any smooth map $F : X \to Y$ between manifolds, $\operatorname{Reg}(F) = Y \setminus F(\operatorname{Crit}(F))$.
>
> **Hint:** Negate the definition of a regular value pointwise and read off membership in $F(\operatorname{Crit}(F))$; handle the empty-preimage case explicitly.
>
> **Why needed:** It rephrases "$\operatorname{Reg}(F)$ is open" as "$F(\operatorname{Crit}(F))$ is closed", the only formulation the properness argument can reach, and it is the step that quietly disposes of unattained points.
>
> > [!note]- Full proof
> > We show the two inclusions.
> >
> > **($\subseteq$) A regular value is not a critical value.** Let $y \in \operatorname{Reg}(F)$; we must show $y \notin F(\operatorname{Crit}(F))$. Suppose, for contradiction, that $y \in F(\operatorname{Crit}(F))$. Then $y = F(x)$ for some $x \in \operatorname{Crit}(F)$, so this $x$ lies in $F^{-1}(y)$ and has $d_xF$ **not** surjective (by the definition of $\operatorname{Crit}(F)$). But $y \in \operatorname{Reg}(F)$ means $d_{x'}F$ is surjective for **every** $x' \in F^{-1}(y)$ (by the definition of $\operatorname{Reg}(F)$), in particular for $x' = x$ — contradicting that $d_xF$ is not surjective. The contradiction is between "$d_xF$ not surjective" (from $x \in \operatorname{Crit}(F)$) and "$d_xF$ surjective" (from $y \in \operatorname{Reg}(F)$). Hence $y \notin F(\operatorname{Crit}(F))$, i.e. $y \in Y \setminus F(\operatorname{Crit}(F))$.
> >
> > **($\supseteq$) A non-critical value is regular.** Let $y \in Y \setminus F(\operatorname{Crit}(F))$; we must show $y \in \operatorname{Reg}(F)$, that is, $d_xF$ is surjective for every $x \in F^{-1}(y)$. Take any $x \in F^{-1}(y)$, so $F(x) = y$. If $x$ were a critical point, then $y = F(x) \in F(\operatorname{Crit}(F))$, contradicting the choice of $y$; therefore $x \notin \operatorname{Crit}(F)$, which by the definition of $\operatorname{Crit}(F)$ means $d_xF$ is surjective. As $x \in F^{-1}(y)$ was arbitrary, every point of $F^{-1}(y)$ is regular, so $y \in \operatorname{Reg}(F)$. (When $F^{-1}(y) = \varnothing$ the quantifier "for every $x \in F^{-1}(y)$" is vacuously satisfied, so $y \in \operatorname{Reg}(F)$; and such a $y$ is not in $F(\operatorname{Crit}(F)) \subseteq \operatorname{im} F$, so it lies in the left set too — both sides contain every unattained point, consistently.)
> >
> > **Conclusion.** Both inclusions hold, so $\operatorname{Reg}(F) = Y \setminus F(\operatorname{Crit}(F))$.

> [!note]- Lemma 2: The critical set of a Fredholm map is closed
> **Statement:** Let $F : X \to Y$ be a Fredholm map between Banach manifolds. Then $\operatorname{Crit}(F) = \{x \in X : d_xF \text{ not surjective}\}$ is closed in $X$; equivalently, the set of regular points $\{x : d_xF \text{ surjective}\}$ is open.
>
> **Hint:** Work in a chart, where $x \mapsto d_xF$ becomes a continuous map into the Fredholm operators; use that the surjective Fredholm operators form an open set.
>
> **Why needed:** It supplies one of the two inputs to the closedness of the critical-value set — namely that the set being mapped by $F$ is closed.
>
> > [!note]- Full proof
> > We prove the equivalent statement that the regular-point set $R = \{x \in X : d_xF \text{ surjective}\}$ is open, so its complement $\operatorname{Crit}(F)$ is closed. Openness is a local property, so it suffices to show that each $x_0 \in R$ has an open neighbourhood contained in $R$.
> >
> > **Step 0 — the local model of the differential.** Fix $x_0 \in R$. Since $F$ is smooth, choose charts $\phi : U \to \widetilde{U} \subseteq E$ about $x_0$ and $\psi : V \to \widetilde{V} \subseteq G$ about $F(x_0)$ with $F(U) \subseteq V$, and set $\widetilde{F} = \psi \circ F \circ \phi^{-1} : \widetilde{U} \to \widetilde{V}$, a smooth map between open subsets of the model Banach spaces $E$ and $G$. For $x \in U$ with $\widetilde{x} = \phi(x)$, the chain rule gives
> > $$d_xF = (d_{F(x)}\psi)^{-1} \circ D\widetilde{F}(\widetilde{x}) \circ d_x\phi \qquad \text{(chain rule applied to } F = \psi^{-1} \circ \widetilde{F} \circ \phi\text{),}$$
> > where $D\widetilde{F}(\widetilde{x}) \in L(E,G)$ is the (Fréchet) derivative of $\widetilde{F}$ at $\widetilde{x}$, and $d_x\phi : T_xX \to E$, $d_{F(x)}\psi : T_{F(x)}Y \to G$ are the chart differentials, which are Banach-space isomorphisms. Because $d_x\phi$ and $d_{F(x)}\psi$ are isomorphisms, $d_xF$ is surjective **if and only if** $D\widetilde{F}(\widetilde{x})$ is surjective (post- and pre-composition with isomorphisms preserves surjectivity). Thus, inside the chart, $x \in R$ if and only if $D\widetilde{F}(\phi(x))$ is a surjective operator.
> >
> > **Step 1 — the differential varies continuously and stays Fredholm.** The map $\widetilde{F}$ is smooth, so its derivative
> > $$D\widetilde{F} : \widetilde{U} \longrightarrow L(E,G), \qquad \widetilde{x} \longmapsto D\widetilde{F}(\widetilde{x})$$
> > is continuous with respect to the operator norm on $L(E,G)$ (a $C^1$ map has continuous Fréchet derivative). Moreover, for every $\widetilde{x} \in \widetilde{U}$ the operator $D\widetilde{F}(\widetilde{x})$ is Fredholm: it is conjugate, by the displayed formula and the isomorphisms $d_x\phi, d_{F(x)}\psi$, to $d_xF$, which is a Fredholm operator because $F$ is a Fredholm map (by hypothesis), and conjugation by isomorphisms preserves the Fredholm property and the index. Hence $D\widetilde{F}$ takes values in the set $\Phi(E,G)$ of Fredholm operators, and $D\widetilde{F} : \widetilde{U} \to \Phi(E,G)$ is continuous.
> >
> > **Step 2 — surjective Fredholm operators form an open set.** We use part (ii) of the stabilisation theorem:
> > > **Stabilisation of Fredholm operators, part (ii) (restated).** For bounded operators between Banach spaces, the maps $T \mapsto \dim\ker T$ and $T \mapsto \dim\operatorname{coker} T$ are upper semicontinuous on the space $\Phi(E,G)$ of Fredholm operators (in the operator norm): for each $T_0 \in \Phi(E,G)$ there is $\varepsilon > 0$ such that $\dim\operatorname{coker} T \le \dim\operatorname{coker} T_0$ for all $T \in L(E,G)$ with $\lVert T - T_0\rVert < \varepsilon$; moreover every such $T$ is itself Fredholm. The complete proof is on [[Thm - Stabilisation of Fredholm Operators and Continuity of the Kernel]].
> >
> > Let $T_0 \in \Phi(E,G)$ be surjective, so $\dim\operatorname{coker} T_0 = 0$. By the restated part (ii) there is $\varepsilon > 0$ such that every $T$ with $\lVert T - T_0\rVert < \varepsilon$ is Fredholm with $\dim\operatorname{coker} T \le \dim\operatorname{coker} T_0 = 0$, hence $\dim\operatorname{coker} T = 0$, i.e. $\operatorname{im} T = G$ and $T$ is surjective (its range is closed and of finite codimension zero). Therefore the set $S = \{T \in \Phi(E,G) : T \text{ surjective}\}$ contains an operator-norm ball around each of its points, and $S$ is open in $\Phi(E,G)$.
> >
> > **Step 3 — conclude openness of $R$.** By Step 0, on the chart neighbourhood $U$ we have $R \cap U = \{x \in U : D\widetilde{F}(\phi(x)) \in S\} = \phi^{-1}\big((D\widetilde{F})^{-1}(S)\big)$. The set $(D\widetilde{F})^{-1}(S)$ is open in $\widetilde{U}$ because $D\widetilde{F}$ is continuous (Step 1) and $S$ is open (Step 2); pulling back by the homeomorphism $\phi$ shows $R \cap U$ is open in $U$, hence in $X$. In particular the point $x_0 \in R \cap U$ has the open neighbourhood $R \cap U \subseteq R$. As $x_0 \in R$ was arbitrary, $R$ is open.
> >
> > **Conclusion.** The regular-point set $R$ is open, so its complement $\operatorname{Crit}(F) = X \setminus R$ is closed in $X$.

> [!note]- Lemma 3: A proper continuous map to a metrisable space is closed
> **Statement:** Let $X$ be a topological space, $Y$ a metrisable space, and $F : X \to Y$ a continuous proper map (preimages of compact sets are compact). Then $F$ is a closed map: for every closed $C \subseteq X$, the image $F(C)$ is closed in $Y$.
>
> **Hint:** Metrisability lets you test closedness with sequences; use properness to trap the domain points in a compact set and extract a convergent subsequence.
>
> **Why needed:** It supplies the second input to the closedness of the critical-value set — that $F$ carries the closed set $\operatorname{Crit}(F)$ to a closed set. The general statement lives on the sibling page; the metrisable-target case, which is all we need since Banach manifolds are metrisable, is proved here in full for self-containedness.
>
> > [!note]- Full proof
> > Let $C \subseteq X$ be closed. To show $F(C)$ is closed in the metrisable space $Y$, it suffices to show it is sequentially closed: if $(y_n)_{n \ge 1}$ is a sequence in $F(C)$ with $y_n \to y$ in $Y$, then $y \in F(C)$. (In a metrisable space a set is closed if and only if it contains the limit of every convergent sequence of its points; this is the sequential characterisation of closedness in a metric space.)
> >
> > **Set up a compact target.** Write $y_n = F(x_n)$ with $x_n \in C$. Consider the set
> > $$K = \{y\} \cup \{y_n : n \ge 1\} \subseteq Y.$$
> > Then $K$ is compact: any open cover of $K$ has a member $O$ containing the limit $y$, and since $y_n \to y$ all but finitely many $y_n$ lie in $O$, so finitely many further members of the cover suffice for the remaining finitely many $y_n$; hence $K$ is covered by finitely many members. (Concretely, a convergent sequence together with its limit is compact in any metric space.)
> >
> > **Trap the domain points.** By properness, $F^{-1}(K)$ is compact. Each $x_n$ satisfies $F(x_n) = y_n \in K$, so $x_n \in F^{-1}(K)$; moreover $x_n \in C$. Thus $x_n \in C \cap F^{-1}(K)$ for all $n$. The set $C \cap F^{-1}(K)$ is compact, being the intersection of the closed set $C$ with the compact set $F^{-1}(K)$ (a closed subset of a compact set is compact). A metrisable space is compact if and only if it is sequentially compact, so the sequence $(x_n)$ in the compact metrisable set $C \cap F^{-1}(K)$ has a subsequence $x_{n_j} \to x$ with $x \in C \cap F^{-1}(K)$; in particular $x \in C$.
> >
> > **Pass to the limit.** By continuity of $F$, $F(x_{n_j}) \to F(x)$. But $F(x_{n_j}) = y_{n_j}$, and $y_{n_j} \to y$ as a subsequence of the convergent sequence $(y_n)$. Limits in the metric (hence Hausdorff) space $Y$ are unique, so $F(x) = y$. Since $x \in C$, this gives $y = F(x) \in F(C)$.
> >
> > **Conclusion.** Every sequential limit of points of $F(C)$ lies in $F(C)$, so $F(C)$ is closed. Therefore $F$ is a closed map. This is exactly the metrisable-target case of part (i) of [[Thm - Proper Maps are Closed and Fredholm Maps are Locally Proper]], whose statement — a proper continuous map into a locally compact Hausdorff space, or into any metrisable space, is closed — is used in the form just proved.

> [!note]- Lemma 4: Density of the regular values (Sard–Smale)
> **Statement:** Let $F : X \to Y$ be a Fredholm map between second countable Banach manifolds. Then $\operatorname{Reg}(F)$ is a residual subset of $Y$, and in particular it is dense.
>
> **Hint:** This is the Sard–Smale theorem, restated; the passage from residual to dense is the Baire category theorem, using that a Banach manifold is a Baire space.
>
> **Why needed:** It is the density half of the theorem outright. Properness plays no role here.
>
> > [!note]- Full proof
> > We invoke the Sard–Smale theorem in the form proved on its own page:
> > > **Sard–Smale theorem (restated).** Let $F : X \to Y$ be a smooth Fredholm map between second countable Banach manifolds. Then the set $\operatorname{Reg}(F)$ of regular values of $F$ is residual (of second category) in $Y$; that is, it contains a countable intersection of open dense subsets of $Y$. The complete proof is on [[Thm - Sard-Smale Theorem]].
> >
> > The hypotheses of the restated theorem are met: $F$ is a Fredholm map (by hypothesis of the present lemma) and $X, Y$ are second countable Banach manifolds (standing assumption). Hence $\operatorname{Reg}(F)$ is residual in $Y$.
> >
> > It remains to pass from residual to dense. A second countable Banach manifold is completely metrisable — each chart is modelled on a complete Banach space, and a second countable, locally completely-metrisable Hausdorff space is completely metrisable — so $Y$ is a complete metric space, hence a **Baire space** by the [[Thm - Baire Category Theorem|Baire category theorem]], which states that in a complete metric space the intersection of countably many open dense sets is dense. Write $\operatorname{Reg}(F) \supseteq \bigcap_{n \ge 1} O_n$ with each $O_n$ open and dense. By Baire's theorem $\bigcap_{n} O_n$ is dense, and a superset of a dense set is dense, so $\operatorname{Reg}(F)$ is dense in $Y$.
> >
> > **Conclusion.** $\operatorname{Reg}(F)$ is residual and dense in $Y$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $X, Y$ be second countable Banach manifolds and $F : X \to Y$ a proper Fredholm map. We prove that $\operatorname{Reg}(F)$ is open and dense; the two properties are proved separately, and their hypotheses differ — openness uses properness, density does not.
>
> **Step 0 — preconditions.** By hypothesis $d_xF$ is a Fredholm operator for every $x \in X$, so the notions "critical point" ($d_xF$ not surjective), "critical value", and "regular value" are defined as in the Notation section, with
> $$\operatorname{Crit}(F) = \{x \in X : d_xF \text{ not surjective}\}, \qquad \operatorname{Reg}(F) = \{y \in Y : d_xF \text{ surjective for all } x \in F^{-1}(y)\}.$$
> Both $X$ and $Y$ are metrisable, being second countable and locally metrisable; this is used in Step 1(c).
>
> ---
>
> **Step 1 — openness.** We show $\operatorname{Reg}(F)$ is open by showing its complement is closed.
>
> **(a) Reduce to closedness of the critical values.** By Lemma 1, $\operatorname{Reg}(F) = Y \setminus F(\operatorname{Crit}(F))$. Hence $\operatorname{Reg}(F)$ is open in $Y$ **if and only if** $F(\operatorname{Crit}(F))$ is closed in $Y$. We prove the latter.
>
> **(b) The critical set is closed.** By Lemma 2 — whose proof uses that surjectivity of a Fredholm operator is an open condition, part (ii) of [[Thm - Stabilisation of Fredholm Operators and Continuity of the Kernel]], and the continuity of the differential in charts — the set $\operatorname{Crit}(F)$ is closed in $X$. Here the Fredholm-map hypothesis is invoked: it is what makes every $d_xF$ Fredholm, so that the openness of surjectivity applies at every point.
>
> **(c) The map $F$ is closed.** Since $F$ is proper (by hypothesis) and $Y$ is metrisable (Step 0), Lemma 3 shows that $F$ carries closed subsets of $X$ to closed subsets of $Y$. Here the properness hypothesis is invoked; it is the only place in the openness argument where it is used.
>
> **(d) Combine.** The set $\operatorname{Crit}(F)$ is closed in $X$ (by (b)), and $F$ is a closed map (by (c)); therefore its image $F(\operatorname{Crit}(F))$ is closed in $Y$ (the image of a closed set under a closed map). By (a), $\operatorname{Reg}(F) = Y \setminus F(\operatorname{Crit}(F))$ is the complement of a closed set, hence **open** in $Y$.
>
> ---
>
> **Step 2 — density.** By Lemma 4, applied to the Fredholm map $F$ between the second countable Banach manifolds $X$ and $Y$ (the Sard–Smale theorem, [[Thm - Sard-Smale Theorem]], followed by the [[Thm - Baire Category Theorem|Baire category theorem]]), the set $\operatorname{Reg}(F)$ is residual in $Y$ and hence **dense** in $Y$. Properness is not used in this step.
>
> ---
>
> **Conclusion.** The set of regular values $\operatorname{Reg}(F)$ is open (Step 1) and dense (Step 2) in $Y$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Finite-dimensional degree from a compact domain.** Let $M$ be a compact smooth $n$-manifold and $F : M \to \mathbb{R}^n$ a smooth map. Every linear map $\mathbb{R}^n \to \mathbb{R}^n$ is Fredholm, so $F$ is a Fredholm map, and compactness of $M$ makes $F$ proper; the present theorem then hands you an open dense set of regular values in $\mathbb{R}^n$. The exercise is to see that this recovers the classical statement underlying Brouwer degree — critical values are nowhere dense, regular preimages are finite — *without* Sard's measure-zero argument for openness, using only closedness of the proper map. It is non-obvious because the finite-dimensional theory usually gets openness for free from compactness and never isolates the role of properness as this proof does.

**Roots of a complex polynomial map.** Consider $P : \mathbb{C} \to \mathbb{C}$ a nonconstant polynomial, viewed as a smooth map $\mathbb{R}^2 \to \mathbb{R}^2$. It is Fredholm (finite-dimensional) and proper (because $|P(z)| \to \infty$ as $|z| \to \infty$, so preimages of bounded sets are bounded, hence preimages of compact sets are compact). The theorem gives an open dense set of regular values; combined with the local degree at each root and the local-constancy of the count, this is the shortest route to the fundamental theorem of algebra. The exercise is to identify the properness of $P$ from its growth at infinity and to explain why the count of roots (with multiplicity mod 2, then refined) is the same at every regular value — this is exactly the well-definedness the present theorem sets up.

**Generic right-hand sides for a semilinear elliptic equation.** On a closed Riemannian manifold $(M,g)$, let $F : W^{2,p}(M) \to L^p(M)$ be $F(u) = \Delta_g u + f(u)$ with $f \in C^1$ bounded together with $f'$. Elliptic regularity and the Rellich–Kondrachov theorem make $F$ a Fredholm map of index zero, and elliptic a priori estimates make it proper. The theorem produces a dense open set of right-hand sides $h \in L^p(M)$ that are regular values, so that the solution set of $\Delta_g u + f(u) = h$ is a compact zero-manifold — a finite set — for a generic $h$. The exercise is to verify the Fredholm and properness hypotheses from the PDE estimates, and it is instructive because it shows the theorem is the abstract engine behind "for generic data the solution set is finite", a statement that looks purely analytic but is topological in origin.

---

# Bridges

- **[[Thm - Sard-Smale Theorem]]** — the density half, imported wholesale. The present theorem contributes nothing to density beyond quoting Sard–Smale and Baire; its own content is entirely the openness half. The construction that ties them is the observation that the *two* topological properties needed for a degree theory, existence of regular values (density) and stability of regular values (openness), have completely different sources — one analytic-cum-Baire, one purely point-set through properness — and the present page is where they are combined into the single statement "$\operatorname{Reg}(F)$ is open and dense".

- **[[Thm - Proper Maps are Closed and Fredholm Maps are Locally Proper]]** — the source of closedness. That page proves, in the generality of a proper continuous map into a locally compact Hausdorff or metrisable space, that the map is closed; the present page instantiates the metrisable-target case (Banach manifolds are metrisable) to turn "$\operatorname{Crit}(F)$ closed" into "$F(\operatorname{Crit}(F))$ closed". The bridge is the metrisability of second countable Banach manifolds, which is what makes the sequential proof of closedness available.

- **[[Thm - Stabilisation of Fredholm Operators and Continuity of the Kernel]]** — the source of "$\operatorname{Crit}(F)$ is closed". Its part (ii), the upper semicontinuity of the cokernel dimension, is exactly "surjectivity is an open condition among Fredholm operators", which pulls back through the continuity of the differential in charts to the openness of the regular-point set. The construction is the conjugation formula $d_xF = (d_{F(x)}\psi)^{-1} \circ D\widetilde{F}(\phi(x)) \circ d_x\phi$, which identifies surjectivity of $d_xF$ with surjectivity of a continuously-varying operator in a fixed Banach space, where the stabilisation theorem lives.

- **[[Thm - Well-Definedness and Homotopy Invariance of the Degree]]** — the immediate consumer. The mod-2 degree $\deg_2 F = \# F^{-1}(y) \bmod 2$ can only be defined once one knows that a regular value $y$ exists (density) and that the count does not depend on the choice (which uses local-constancy on the open regular set, then a homotopy across the nowhere-dense critical wall). The present theorem is Step 1 of that page's six-step proof; the construction connecting them is the finiteness of the regular preimage of an index-zero proper Fredholm map, established through the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] (giving a zero-manifold) and properness (giving compactness, hence finiteness).

---

# Unlocked by This

> [!tip] Locally constant degree count *(from Degree Theory)*
> With $\operatorname{Reg}(F)$ open, the preimage-count $y \mapsto \# F^{-1}(y) \bmod 2$ is defined on an open set and, by the inverse function theorem applied at each of the finitely many preimage points, is locally constant there. This is the next step toward the degree; see **[[Thm - The Degree Count is Locally Constant on Regular Values]]**.

> [!tip] Nonzero degree forces surjectivity *(from Nonlinear Analysis)*
> Density of $\operatorname{Reg}(F)$ together with a nonzero degree makes every point of $Y$ a limit of regular values with nonempty preimage; closedness of the proper map $F$ then puts the limit in the image, so $F$ is onto. See **[[Thm - Nonzero Degree Implies Surjectivity]]**.
