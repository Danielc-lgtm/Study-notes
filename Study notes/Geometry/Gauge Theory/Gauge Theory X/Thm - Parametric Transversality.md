---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Parametric Family of Fredholm Maps"
  - "Def - Fredholm Map and Its Index"
  - "Def - Regular Value and Transversality for Fredholm Maps"
  - "Def - Fredholm Operator and Index"
  - "Def - Residual Set and Generic Property"
  - "Thm - Sard-Smale Theorem"
  - "Thm - Regular Value and Transversality Theorems for Fredholm Maps"
  - "Thm - Stabilisation of Fredholm Operators and Continuity of the Kernel"
tags: [geometry, gauge-theory]
---

# Notation

Throughout this page we work in the setting of a [[Def - Parametric Family of Fredholm Maps|parametric family of Fredholm maps]], and every space is a [[Def - Banach Manifold and Smooth Maps between Banach Spaces|Banach manifold]] — a Hausdorff, second countable space with an atlas of charts into open subsets of a fixed separable Banach space and smooth transition maps.

We fix:

- Two Banach manifolds $X$ (the *configurations*) and $Y$ (the *target*), and a connected Banach manifold $W$ (the *parameters*). We take $X$ connected, so that the Fredholm index of a Fredholm map out of $X$ is a single well-defined integer; on a disconnected $X$ every statement below holds component by component.
- A smooth [[Def - Fredholm Map and Its Index|Fredholm map]] $\mathcal{F} : X \times W \to Y$. A smooth map between Banach manifolds is a Fredholm map when its differential $d_z\mathcal{F} : T_zX \times T_wW \to T_yY$ is a [[Def - Fredholm Operator and Index|Fredholm operator]] at every point — a bounded linear map with finite-dimensional kernel, closed range, and finite-dimensional cokernel.
- For each parameter $w \in W$, the *sliced map* $\mathcal{F}_w := \mathcal{F}(\,\cdot\,, w) : X \to Y$, $x \mapsto \mathcal{F}(x, w)$.
- A point $y \in Y$.

The three hypotheses of the family, restated from [[Def - Parametric Family of Fredholm Maps]], are:

- **(A)** each sliced map $\mathcal{F}_w : X \to Y$ is a Fredholm map;
- **(B)** there is a base parameter $w_0 \in W$ with $\mathcal{F}_{w_0} = F$, the individual map of interest, and $\operatorname{index} F$ denotes its Fredholm index;
- **(C)** $y$ is a [[Def - Regular Value and Transversality for Fredholm Maps|regular value]] of the total map $\mathcal{F}$, that is, $d_z\mathcal{F}$ is surjective at every $z \in \mathcal{F}^{-1}(y)$.

The objects the theorem is about are:

- the *universal zero set* $\mathcal{Z} := \mathcal{F}^{-1}(y) = \{(x, w) \in X \times W : \mathcal{F}(x, w) = y\}$;
- the *projection to parameters* $\pi : \mathcal{Z} \to W$, the restriction to $\mathcal{Z}$ of the canonical projection $\operatorname{pr}_W : X \times W \to W$, $(x, w) \mapsto w$;
- the *good-parameter set* $W_0 := \{w \in W : y \text{ is a regular value of } \mathcal{F}_w\}$.

At a point $z = (x, w) \in \mathcal{Z}$ we abbreviate the two partial differentials of $\mathcal{F}$ by
$$A := d_x\mathcal{F}_w : T_xX \to T_yY, \qquad B := \partial_w\mathcal{F}(x, w) : T_wW \to T_yY,$$
so that the total differential splits as $d_z\mathcal{F}(\dot{x}, \dot{w}) = A\dot{x} + B\dot{w}$ for $(\dot{x}, \dot{w}) \in T_xX \times T_wW$. We write $\operatorname{Im} T$, $\ker T$, and $\operatorname{coker} T := (\text{codomain of } T)/\operatorname{Im} T$ for the image, kernel, and cokernel of a linear map $T$, and $q_A : T_yY \to \operatorname{coker} A$ for the quotient projection onto $\operatorname{coker} A = T_yY / \operatorname{Im} A$.

A subset of a Banach manifold is [[Def - Residual Set and Generic Property|residual]] when it contains a countable intersection of open dense subsets; by the [[Thm - Baire Category Theorem|Baire category theorem]] a residual subset of a Banach manifold is dense. The full symbol registry for the chapter is on the parent page **Gauge Theory X — Fredholm Maps, Transversality, and Degree**.

> [!warning] Convention: "second category" versus "residual"
> Haydys states this result (Lemma 169) with the phrase "$W_0 \subset W$ of second category". Following the series convention, we say *residual* (a countable intersection of open dense sets, equivalently a comeagre set) throughout, because Baire's own terminology reserves "second category" for the weaker notion "not meagre". The conclusion we prove — residual, hence dense — is exactly the one the applications use.

---

# Statement

> **Theorem (Parametric Transversality; Haydys, Lemma 169).** Let $\mathcal{F} : X \times W \to Y$ be a smooth Fredholm map between Banach manifolds with $X$ and $W$ connected, satisfying hypotheses **(A)**, **(B)**, **(C)** above for a point $y \in Y$. Let $\mathcal{Z} := \mathcal{F}^{-1}(y)$, which by **(C)** and the [[Thm - Regular Value and Transversality Theorems for Fredholm Maps|regular-value theorem for Fredholm maps]] is a smooth embedded Banach submanifold of $X \times W$ with $T_z\mathcal{Z} = \ker d_z\mathcal{F}$, and let $\pi : \mathcal{Z} \to W$ be the restriction of the projection. Then:
>
> **(i)** $\pi$ is a smooth Fredholm map, with
> $$\operatorname{index}\pi = \operatorname{index}\mathcal{F}_w = \operatorname{index} F \qquad \text{for every } w,$$
> and a parameter $w \in W$ is a regular value of $\pi$ **if and only if** $y$ is a regular value of the sliced map $\mathcal{F}_w$; equivalently $W_0 = \{w : w \text{ is a regular value of } \pi\}$.
>
> **(ii)** The good-parameter set $W_0 = \{w \in W : y \text{ is a regular value of } \mathcal{F}_w\}$ is residual in $W$, and hence dense.

---

# Motivation

The Sard–Smale theorem is a statement about moving the *value*: given a Fredholm map $F : X \to Y$, almost every point $y' \in Y$ near a chosen $y$ is a regular value, so that $F^{-1}(y')$ is a manifold. In the problems this chapter exists to serve — the moduli spaces of gauge theory — one is not free to move the value. The Seiberg–Witten map, for instance, is equivariant for the action of the gauge group, and one must take $y$ to be a fixed point of that action (typically $y = 0$) so that the zero set $F^{-1}(y)$ carries the symmetry and descends to a moduli space. Perturbing $y$ off the fixed locus would destroy exactly the structure one is trying to study. So the value is frozen, and the Sard–Smale theorem, which perturbs the value, cannot be applied to $F$ directly.

Parametric transversality is the standard way out. Instead of moving $y$, one moves the *map*: one embeds $F$ into a family $\mathcal{F}_w$ of maps indexed by an auxiliary parameter $w$ ranging over a Banach manifold $W$ (a space of metrics, a space of perturbing forms, a space of connections), arranged so that the *total* map $\mathcal{F} : X \times W \to Y$ has $y$ as a genuine regular value. This is usually easy to arrange, because the extra freedom in the parameter direction can be used to hit whatever the individual maps miss. The question this theorem answers is then the decisive one: does hitting $y$ regularly *jointly* — with $x$ and $w$ both free — force $y$ to be hit regularly *for a fixed parameter* — with $x$ free but $w$ frozen — for enough choices of $w$?

The theorem says yes, and pinpoints the mechanism. The joint zero set $\mathcal{Z} = \mathcal{F}^{-1}(y)$ is a smooth manifold (that much is just the regular-value theorem applied to $\mathcal{F}$). It fibres over the parameters by the projection $\pi$. The content of the theorem is that $\pi$ is a Fredholm map whose regular values are exactly the good parameters, so that Sard–Smale applied *to $\pi$* — which is legitimate, because $\pi$ moves through the parameter manifold $W$, where we *are* free to move — delivers a residual set of good parameters. In one sentence: parametric transversality converts a transversality problem in which the value is frozen into a Sard–Smale problem in which the parameter is free, and the conversion is exact because the cokernel of the projection equals the cokernel of the sliced map.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypotheses are (A)–(C), but the skill is recognising when a problem secretly hands you a parametric family with $y$ regular for the total map even though no family is named.

The first disguised source is **a nonlinear equation with a free additive inhomogeneity or forcing term**. Whenever the equation of interest reads $\Phi(x) = 0$ for a Fredholm $\Phi : X \to Y$ and the ambient problem permits adding an arbitrary element of a Banach space $W \subseteq Y$ of "perturbations", the map $\mathcal{F}(x, w) := \Phi(x) - w$ is a parametric family whose $w$-derivative is $-\operatorname{id}_W$; the total differential $d\mathcal{F}(\dot{x}, \dot{w}) = d\Phi\,\dot{x} - \dot{w}$ is then automatically surjective onto $W$, so $y = 0$ is a regular value of $\mathcal{F}$ and hypothesis (C) holds for free. The non-obvious bridge is that a full linear direction of freedom in the target, added to a Fredholm map of any index, always produces a submersion in that direction. *Example problem:* on a closed surface, show that for a residual set of functions $w$ the semilinear equation $\Delta u + u^3 = w$ has $0$ as a regular value of $u \mapsto \Delta u + u^3 - w$.

The second disguised source is **an equivariant problem with a frozen fixed value**, which is the setting the theorem was built for. If a Lie group $G$ acts on $X$ and $Y$ and $F$ is $G$-equivariant, and $y$ is a $G$-fixed point, then the value cannot be perturbed without breaking equivariance. The bridge is to introduce a $G$-invariant space $W$ of perturbations acting only through the map, so that $\mathcal{F}$ remains $G$-equivariant while acquiring $y$ as a joint regular value; parametric transversality then produces $G$-invariantly-chosen good parameters. *Example problem:* the Seiberg–Witten equations, where $W$ is a space of self-dual two-forms and $y = 0$ is fixed by the gauge action; parametric transversality is the first step toward generic smoothness of the moduli space.

The third disguised source is **a geometric problem where the structure that defines the operator is itself variable**. When the Fredholm operator depends on a Riemannian metric, a connection, or a complex structure, that geometric datum *is* the parameter $w$, ranging over the (Banach manifold completion of the) space of such data. The bridge is that varying the geometric datum varies the operator, and one checks (C) by showing the derivative in the datum direction is enough to surject onto whatever the fixed-datum operator misses. *Example problem:* the generic-metric transversality theorem of Freed–Uhlenbeck, where $W$ is a Banach space of Riemannian metrics and the anti-self-duality operator is the sliced map.

**Targets (Output Amplification)**

The bare conclusion is a residual set of good parameters. Combined with other ingredients it produces the objects gauge theory actually needs.

Combine the conclusion with **the regular-value theorem for Fredholm maps**. Once $w \in W_0$ is chosen, $y$ is a regular value of $\mathcal{F}_w$, so $\mathcal{F}_w^{-1}(y)$ is a smooth manifold of dimension $\operatorname{index} F$. The extra ingredient is part (i) of [[Thm - Regular Value and Transversality Theorems for Fredholm Maps|the regular-value theorem]], and the payoff is that the *perturbed* moduli space is a smooth finite-dimensional manifold of the expected dimension. This is the sole route to smoothness of a moduli space that is singular for the unperturbed equation.

Combine the conclusion with **properness of the sliced maps (hypothesis (D)) and the cobordism theorem for compact one-manifolds**. If in addition each $\mathcal{F}_w$ is proper and $\operatorname{index} F = 0$, then the good-parameter counts $\#\mathcal{F}_{w_1}^{-1}(y)$ and $\#\mathcal{F}_{w_2}^{-1}(y)$ agree modulo two, because a generic path from $w_1$ to $w_2$ produces a compact one-dimensional cobordism between the two finite fibres. The extra ingredients are properness and the parity of the boundary of a compact one-manifold, and the payoff — worked out on [[Thm - The Generic Parametric Count Defines the Mod-2 Degree|the page defining the degree by the parametric count]] — is that $\#\mathcal{F}_w^{-1}(y) \bmod 2$ is a well-defined invariant, an alternative definition of the mod-2 degree that never mentions moving the value.

Combine the conclusion with **a determinant-line-bundle orientation and a compactness theorem**. In the oriented, index-zero, equivariant setting of Seiberg–Witten theory, the residual good parameters give a smooth moduli space, an orientation of it from the [[Def - Determinant Line Bundle of a Family of Fredholm Operators|determinant line bundle]] trivialises the count with signs, and the compactness theorem makes the signed count finite; the payoff is the integer Seiberg–Witten invariant and its independence of the perturbation. Parametric transversality is the transversality half of that package.

---

# Why Is It True

Set the formal proof aside and picture the two projections of the joint zero set $\mathcal{Z} \subset X \times W$. A point of $\mathcal{Z}$ is a pair $(x, w)$ solving $\mathcal{F}(x, w) = y$. The fibre of $\pi$ over a parameter $w$ is $\pi^{-1}(w) = \{(x, w) : \mathcal{F}_w(x) = y\}$, which is a copy of the sliced zero set $\mathcal{F}_w^{-1}(y)$. So $\pi$ organises all the sliced solution sets, one over each parameter, into a single manifold, and asking "for which $w$ is $\mathcal{F}_w^{-1}(y)$ cut out transversally?" is asking "for which $w$ is $\pi$ submersive over $w$?" — that is, "which $w$ are regular values of $\pi$?"

Now the crux, which is pure linear algebra at a single point $z = (x, w) \in \mathcal{Z}$. The tangent space $T_z\mathcal{Z}$ is $\ker d_z\mathcal{F}$, the pairs $(\dot{x}, \dot{w})$ with $A\dot{x} + B\dot{w} = 0$. The differential of $\pi$ just forgets $\dot{x}$: it sends $(\dot{x}, \dot{w}) \mapsto \dot{w}$. Two facts fall out. First, its kernel consists of the tangent vectors with $\dot{w} = 0$, i.e. $A\dot{x} = 0$, so $\ker d\pi_z$ is a copy of $\ker A = \ker d_x\mathcal{F}_w$ — finite-dimensional because the sliced map is Fredholm. Second, and this is the whole theorem, a parameter direction $\dot{w}$ is *reached* by $d\pi_z$ exactly when it can be completed to a tangent vector of $\mathcal{Z}$, i.e. when there is $\dot{x}$ with $A\dot{x} = -B\dot{w}$, i.e. when $B\dot{w}$ already lies in $\operatorname{Im} A$. So the parameter directions that $d\pi_z$ *misses* are measured by $B\dot{w}$ modulo $\operatorname{Im} A$ — that is, by the class $[B\dot{w}]$ in $\operatorname{coker} A$. Because the total differential $A\dot{x} + B\dot{w}$ is surjective (this is where hypothesis (C) enters, and only here), every class in $\operatorname{coker} A$ is realised as some $[B\dot{w}]$, and the map $\dot{w} \mapsto [B\dot{w}]$ is onto $\operatorname{coker} A$ with kernel exactly the reached directions. This is a surjection with kernel the image of $d\pi_z$; the first isomorphism theorem turns it into an isomorphism

$$\operatorname{coker} d\pi_z \;\cong\; \operatorname{coker} d_x\mathcal{F}_w.$$

**The cokernel of the projection to parameters, at any point, is naturally isomorphic to the cokernel of the sliced map at that point — and the isomorphism is transported across by the total surjectivity hypothesis (C).**

Everything follows. The cokernel is finite-dimensional, so $\pi$ is Fredholm; the index is $\dim\ker A - \dim\operatorname{coker} A = \operatorname{index}\mathcal{F}_w$; and $d\pi_z$ is surjective (that is, $\operatorname{coker} d\pi_z = 0$) exactly when $\operatorname{coker} d_x\mathcal{F}_w = 0$, i.e. when $d_x\mathcal{F}_w$ is surjective. Running this over all $x$ with $(x, w) \in \mathcal{Z}$ says that $w$ is a regular value of $\pi$ if and only if $y$ is a regular value of $\mathcal{F}_w$. And now the Sard–Smale theorem, applied to the Fredholm map $\pi$ — legitimately, because $\pi$ takes values in the parameter manifold $W$, which we are free to sweep — gives that its regular values are residual. Translated back through the equivalence just proved, the good parameters are residual.

---

# What Makes This Hard

The subtle step is not the topology but the linear algebra of the cokernel, and precisely which hypothesis makes it work. The natural map $\dot{w} \mapsto [B\dot{w}]$ from parameter directions to $\operatorname{coker} A$ exists for any family; what surjectivity of the *total* differential $d_z\mathcal{F} = A + B$ buys — and nothing weaker does — is that this map is onto, so that its induced map on the cokernel is an isomorphism rather than a mere injection. A common error is to invoke surjectivity of the individual $d_x\mathcal{F}_w$ (which is what we are trying to prove is generic) instead of surjectivity of the joint $d_z\mathcal{F}$ (which is hypothesis (C)); the argument would then be circular. A second trap is to forget that a finite-dimensional cokernel is not enough for the Fredholm property: one must also check that $\operatorname{Im} d\pi_z$ is *closed*, which here follows because it is the kernel of the continuous map $\dot{w} \mapsto [B\dot{w}]$, the continuity resting on $\operatorname{Im} A$ being closed (part of the Fredholm hypothesis (A) on the sliced map). A third is to conflate "$\pi$ Fredholm" with "$\mathcal{F}$ Fredholm": the two indices differ, and it is the projection's index, not the total map's, that equals $\operatorname{index} F$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Reduce the whole theorem to one pointwise linear-algebra computation — that the differential of $\pi$ has the same kernel dimension and cokernel dimension as the differential of the sliced map — and then feed the resulting Fredholm map $\pi$ into the Sard–Smale theorem. The projection $d\pi_z$ forgets the configuration direction, so its kernel and cokernel are read off from the split total differential $A\dot{x} + B\dot{w}$ under the surjectivity hypothesis (C).

**Subgoal decomposition:**

1. **Make $\mathcal{Z}$ a manifold and $\pi$ smooth.** Show $\mathcal{Z} = \mathcal{F}^{-1}(y)$ is a smooth submanifold with $T_z\mathcal{Z} = \ker d_z\mathcal{F}$, and that $\pi$ is smooth with $d\pi_z(\dot{x}, \dot{w}) = \dot{w}$.
   - *Hint:* Apply the regular-value theorem for Fredholm maps to $\mathcal{F}$, using (C). The projection $\operatorname{pr}_W$ is linear, hence its own differential; restrict it.
   - *Why needed:* Without the manifold structure there is no differential $d\pi_z$ to analyse and no Fredholm map to feed to Sard–Smale.

2. **Compute $\ker d\pi_z$.** Show $\ker d\pi_z = \ker A \times \{0\}$, finite-dimensional.
   - *Hint:* $(\dot{x}, \dot{w}) \in \ker d\pi_z$ means $\dot{w} = 0$ and $(\dot{x}, 0) \in \ker d_z\mathcal{F}$, i.e. $A\dot{x} = 0$.
   - *Why needed:* Finite-dimensional kernel is half of the Fredholm property of $\pi$ and one of the two numbers in its index.

3. **Compute $\operatorname{coker} d\pi_z$.** Show the map $\bar{B} : \dot{w} \mapsto [B\dot{w}] \in \operatorname{coker} A$ is a continuous surjection with kernel $\operatorname{Im} d\pi_z$, inducing $\operatorname{coker} d\pi_z \cong \operatorname{coker} A$.
   - *Hint:* $\dot{w} \in \operatorname{Im} d\pi_z$ iff $B\dot{w} \in \operatorname{Im} A$ iff $\bar{B}\dot{w} = 0$; surjectivity of $\bar{B}$ is surjectivity of $A + B$ (hypothesis (C)) pushed to the quotient.
   - *Why needed:* This is the crux — it makes $\operatorname{coker} d\pi_z$ finite-dimensional and $\operatorname{Im} d\pi_z$ closed, so $\pi$ is Fredholm, and it is what forces the regular-value equivalence.

4. **Read off index and the regular-value equivalence.** Conclude $\operatorname{index} d\pi_z = \operatorname{index} A$, and $d\pi_z$ surjective iff $A$ surjective; then quantify over the fibre.
   - *Hint:* $\operatorname{index} = \dim\ker - \dim\operatorname{coker}$; surjectivity of $d\pi_z$ is vanishing of $\operatorname{coker} d\pi_z \cong \operatorname{coker} A$.
   - *Why needed:* This is part (i) except for identifying $\operatorname{index}\mathcal{F}_w$ with $\operatorname{index} F$.

5. **Constancy of the sliced index.** Show $\operatorname{index}\mathcal{F}_w$ is the same integer $\operatorname{index} F$ for all $w$.
   - *Hint:* $(x, w) \mapsto d_x\mathcal{F}_w$ is a continuous family of Fredholm operators on the connected $X \times W$; the index is locally constant, hence constant, and equals its value at $w_0$.
   - *Why needed:* It turns the pointwise "$\operatorname{index}\pi = \operatorname{index}\mathcal{F}_w$" into the stated "$\operatorname{index}\pi = \operatorname{index} F$".

6. **Genericity.** Apply the Sard–Smale theorem to the Fredholm map $\pi$ and translate its regular values through subgoal 4.
   - *Hint:* Regular values of $\pi$ are residual in $W$; they are exactly $W_0$; residual implies dense by Baire.
   - *Why needed:* It is part (ii), the payoff.

---

# Lemma Decomposition

> [!note]- Lemma 1: Kernel and cokernel of the projection differential (the crux)
> **Statement:** Let $z = (x, w) \in \mathcal{Z}$, write $A = d_x\mathcal{F}_w : T_xX \to T_yY$ and $B = \partial_w\mathcal{F}(x, w) : T_wW \to T_yY$, so that $d_z\mathcal{F}(\dot{x}, \dot{w}) = A\dot{x} + B\dot{w}$, and let $d\pi_z : \ker d_z\mathcal{F} \to T_wW$, $(\dot{x}, \dot{w}) \mapsto \dot{w}$. Assume $A$ is a Fredholm operator (hypothesis (A)) and $d_z\mathcal{F}$ is surjective (hypothesis (C)). Then:
> > (a) $\ker d\pi_z = \ker A \times \{0\}$, so $\dim\ker d\pi_z = \dim\ker A < \infty$;
> > (b) $\operatorname{Im} d\pi_z = \{\dot{w} \in T_wW : B\dot{w} \in \operatorname{Im} A\}$ is a closed subspace of finite codimension, and $\dot{w} \mapsto [B\dot{w}]$ induces a linear isomorphism $\Phi : \operatorname{coker} d\pi_z \xrightarrow{\ \sim\ } \operatorname{coker} A$;
> > (c) consequently $d\pi_z$ is a Fredholm operator with $\operatorname{index} d\pi_z = \operatorname{index} A$, and $d\pi_z$ is surjective if and only if $A$ is surjective.
>
> **Hint:** The kernel is immediate. For the cokernel, push the surjectivity of $A + B$ through the quotient projection $q_A : T_yY \to \operatorname{coker} A$: the composite $\bar{B} := q_A \circ B$ is onto, and its kernel is exactly the image of $d\pi_z$.
>
> **Why needed:** It is the entire linear-algebraic content of part (i); everything else on the page is assembly and one application of Sard–Smale. It is precisely the snake-lemma computation the source omits.
>
> > [!note]- Full proof
> > We prove the three claims in order. Throughout, $q_A : T_yY \to \operatorname{coker} A = T_yY/\operatorname{Im} A$ is the quotient projection; it is continuous because $\operatorname{Im} A$ is closed (a [[Def - Fredholm Operator and Index|Fredholm operator]] has closed range, by hypothesis (A) on $A$), and $\operatorname{coker} A$ is a Banach space, finite-dimensional because $A$ is Fredholm.
> >
> > **Proof of (a).** By definition $d\pi_z(\dot{x}, \dot{w}) = \dot{w}$ for $(\dot{x}, \dot{w}) \in \ker d_z\mathcal{F} = T_z\mathcal{Z}$. Hence
> > $$(\dot{x}, \dot{w}) \in \ker d\pi_z \iff \dot{w} = 0 \text{ and } (\dot{x}, \dot{w}) \in \ker d_z\mathcal{F} \qquad \text{(definition of } d\pi_z\text{ and of the kernel)},$$
> > and with $\dot{w} = 0$ the membership $(\dot{x}, 0) \in \ker d_z\mathcal{F}$ reads $A\dot{x} + B\cdot 0 = A\dot{x} = 0$ (the split form of $d_z\mathcal{F}$). Therefore
> > $$\ker d\pi_z = \{(\dot{x}, 0) : A\dot{x} = 0\} = \ker A \times \{0\},$$
> > and the assignment $\dot{x} \mapsto (\dot{x}, 0)$ is a linear isomorphism $\ker A \to \ker d\pi_z$, so $\dim\ker d\pi_z = \dim\ker A$, which is finite because $A$ is Fredholm.
> >
> > **Proof of (b), the image.** A parameter direction $\dot{w} \in T_wW$ lies in $\operatorname{Im} d\pi_z$ if and only if it extends to a tangent vector of $\mathcal{Z}$, i.e.
> > $$\dot{w} \in \operatorname{Im} d\pi_z \iff \exists\, \dot{x} \in T_xX \text{ with } (\dot{x}, \dot{w}) \in \ker d_z\mathcal{F} \qquad \text{(definition of } d\pi_z \text{ as } (\dot{x},\dot{w})\mapsto\dot{w} \text{ on } \ker d_z\mathcal{F})$$
> > $$\iff \exists\, \dot{x} \text{ with } A\dot{x} + B\dot{w} = 0 \iff -B\dot{w} \in \operatorname{Im} A \iff B\dot{w} \in \operatorname{Im} A \qquad \text{(split form; } \operatorname{Im} A \text{ is a linear subspace, so closed under negation)}.$$
> > Introduce the continuous linear map $\bar{B} := q_A \circ B : T_wW \to \operatorname{coker} A$ (continuous as a composite of the bounded $B$ and the continuous $q_A$). Since $\ker q_A = \operatorname{Im} A$, we have $B\dot{w} \in \operatorname{Im} A \iff \bar{B}\dot{w} = 0$, so the displayed equivalences give
> > $$\operatorname{Im} d\pi_z = \ker \bar{B}, \qquad \text{which is closed, being the kernel of the continuous map } \bar{B}.$$
> >
> > **Proof of (b), the cokernel.** We first show $\bar{B}$ is surjective, and this is the only place hypothesis (C) is used. Let $c \in \operatorname{coker} A$ be arbitrary and write $c = q_A(\eta)$ for some $\eta \in T_yY$ (possible because $q_A$ is surjective). By hypothesis (C), $d_z\mathcal{F}$ is surjective, so there exist $\dot{x} \in T_xX$, $\dot{w} \in T_wW$ with $A\dot{x} + B\dot{w} = \eta$. Applying $q_A$,
> > $$c = q_A(\eta) = q_A(A\dot{x}) + q_A(B\dot{w}) = 0 + \bar{B}\dot{w} = \bar{B}\dot{w} \qquad \text{(since } q_A(A\dot{x}) = 0 \text{ as } A\dot{x} \in \operatorname{Im} A = \ker q_A\text{)}.$$
> > Thus every $c \in \operatorname{coker} A$ is $\bar{B}\dot{w}$ for some $\dot{w}$, i.e. $\bar{B}$ is onto. Now define
> > $$\Phi : \operatorname{coker} d\pi_z = T_wW/\operatorname{Im} d\pi_z \to \operatorname{coker} A, \qquad \Phi([\dot{w}]) := \bar{B}\dot{w} = [B\dot{w}].$$
> > This is well-defined and injective because its kernel-and-well-definedness both reduce to the identity $\operatorname{Im} d\pi_z = \ker\bar{B}$ just proved: if $[\dot{w}_1] = [\dot{w}_2]$ then $\dot{w}_1 - \dot{w}_2 \in \operatorname{Im} d\pi_z = \ker\bar{B}$, so $\bar{B}\dot{w}_1 = \bar{B}\dot{w}_2$ (well-defined); and if $\Phi([\dot{w}]) = 0$ then $\dot{w} \in \ker\bar{B} = \operatorname{Im} d\pi_z$, so $[\dot{w}] = 0$ (injective). It is surjective because $\bar{B}$ is. It is linear because $\bar{B}$ is. Hence $\Phi$ is a linear isomorphism $\operatorname{coker} d\pi_z \cong \operatorname{coker} A$. (This is exactly the first isomorphism theorem for the linear surjection $\bar{B}$, whose image is $\operatorname{coker} A$ and whose kernel is $\operatorname{Im} d\pi_z$.) In particular $\operatorname{coker} d\pi_z$ is finite-dimensional, of the same dimension as $\operatorname{coker} A$, so $\operatorname{Im} d\pi_z = \ker\bar{B}$ has finite codimension in $T_wW$.
> >
> > **Proof of (c).** By (a) the kernel of $d\pi_z$ is finite-dimensional; by (b) its image is closed of finite codimension, equivalently its cokernel is finite-dimensional. A bounded linear map with finite-dimensional kernel, closed range, and finite-dimensional cokernel is a [[Def - Fredholm Operator and Index|Fredholm operator]], so $d\pi_z$ is Fredholm. Its index is
> > $$\operatorname{index} d\pi_z = \dim\ker d\pi_z - \dim\operatorname{coker} d\pi_z = \dim\ker A - \dim\operatorname{coker} A = \operatorname{index} A \qquad \text{(by (a), by (b), and the definition of the Fredholm index)}.$$
> > Finally $d\pi_z$ is surjective if and only if $\operatorname{coker} d\pi_z = 0$, which by the isomorphism $\Phi$ of (b) holds if and only if $\operatorname{coker} A = 0$, i.e. if and only if $A = d_x\mathcal{F}_w$ is surjective. This proves (c). $\blacksquare$
> >
> > *Remark (this is the snake lemma).* The three parts are the kernel–cokernel exact sequence of the commutative diagram with exact rows
> > $$\begin{array}{ccccccccc} 0 &\to& T_xX &\xrightarrow{\ (\cdot,0)\ }& T_xX \times T_wW &\xrightarrow{\ \operatorname{pr}_W\ }& T_wW &\to& 0 \\ & & \downarrow{\scriptstyle A} & & \downarrow{\scriptstyle d_z\mathcal{F}} & & \downarrow{\scriptstyle 0} & & \\ 0 &\to& T_yY &\xrightarrow{\ \operatorname{id}\ }& T_yY &\xrightarrow{\ 0\ }& 0 &\to& 0 \end{array}$$
> > whose snake sequence $0 \to \ker A \to \ker d_z\mathcal{F} \xrightarrow{d\pi_z} T_wW \xrightarrow{\delta} \operatorname{coker} A \to \operatorname{coker} d_z\mathcal{F} \to 0$ has $\operatorname{coker} d_z\mathcal{F} = 0$ by (C), connecting map $\delta = \bar{B}$, and reproduces exactly (a) and (b). We have written the argument out directly rather than invoke a snake-lemma page, so the page is self-contained.

> [!note]- Lemma 2: The sliced Fredholm index is independent of the parameter
> **Statement:** Under hypotheses (A) and (B), with $X$ and $W$ connected, the integer $\operatorname{index}\mathcal{F}_w$ (the Fredholm index of $\mathcal{F}_w : X \to Y$) is the same for every $w \in W$, and equals $\operatorname{index} F$.
>
> **Hint:** The differentials $d_x\mathcal{F}_w$ form a continuous family of Fredholm operators parametrised by the connected space $X \times W$; the Fredholm index is locally constant, hence constant, on a connected parameter space.
>
> **Why needed:** It upgrades the pointwise identity $\operatorname{index} d\pi_z = \operatorname{index}\mathcal{F}_w$ from Lemma 1 to the stated $\operatorname{index}\pi = \operatorname{index} F$.
>
> > [!note]- Full proof
> > For a Fredholm map, the index of the differential is by definition the same at all points of a connected component of the domain, so for each fixed $w$ the value $\operatorname{index} d_x\mathcal{F}_w$ does not depend on $x$ (as $X$ is connected); call this common value $\iota(w) = \operatorname{index}\mathcal{F}_w$. We must show $\iota$ is constant on $W$.
> >
> > **The family is continuous.** Because $\mathcal{F}$ is smooth, its differential $d\mathcal{F}$ is continuous in the base point, and hence so is the partial differential
> > $$(x, w) \longmapsto A(x,w) := d_x\mathcal{F}_w = d_{(x,w)}\mathcal{F}\big|_{T_xX \times \{0\}},$$
> > read in local trivialisations of $TX$ and $TY$ as a map from $X \times W$ into the bounded operators $\operatorname{Hom}(T_xX, T_yY)$ with the operator norm. By hypothesis (A) each $A(x, w)$ is a Fredholm operator, so this is a continuous map from $X \times W$ into the space $\operatorname{Fred}(T_xX, T_yY)$ of Fredholm operators.
> >
> > **The index is locally constant.** By [[Thm - Stabilisation of Fredholm Operators and Continuity of the Kernel|the stabilisation theorem]] — which states, among other things, that the set of Fredholm operators is open in the operator norm and that the index $\operatorname{index} : \operatorname{Fred}(E, F) \to \mathbb{Z}$ is locally constant there — the composite $(x, w) \mapsto \operatorname{index} A(x, w)$ is a locally constant, integer-valued function on $X \times W$.
> >
> > **Constant on a connected space.** A locally constant function on a connected topological space is constant, and $X \times W$ is connected (a product of connected spaces $X$ and $W$). Therefore $(x, w) \mapsto \operatorname{index} A(x, w)$ is a single integer on $X \times W$. Restricting to a fixed $w$ recovers $\iota(w)$, so $\iota$ is that same integer for every $w$. Evaluating at the base parameter $w_0$, where $\mathcal{F}_{w_0} = F$ by hypothesis (B), gives $\iota(w) = \iota(w_0) = \operatorname{index} F$ for all $w$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We are given a smooth Fredholm map $\mathcal{F} : X \times W \to Y$ between Banach manifolds, with $X$ and $W$ connected, satisfying (A) each $\mathcal{F}_w$ is Fredholm, (B) $\mathcal{F}_{w_0} = F$, and (C) $y$ is a regular value of $\mathcal{F}$. We must prove (i) $\pi : \mathcal{Z} \to W$ is a smooth Fredholm map with $\operatorname{index}\pi = \operatorname{index} F$ and with regular values exactly $W_0$; and (ii) $W_0$ is residual, hence dense.
>
> **Step 0 — the universal zero set is a manifold and $\pi$ is smooth.** By hypothesis (C), $y$ is a regular value of the smooth Fredholm map $\mathcal{F}$. By part (i) of [[Thm - Regular Value and Transversality Theorems for Fredholm Maps|the regular-value theorem for Fredholm maps]] — *if $y$ is a regular value of a smooth Fredholm map $\mathcal{F} : X \times W \to Y$, then $\mathcal{F}^{-1}(y)$ is a smooth embedded Banach submanifold of $X \times W$ with $T_z\mathcal{F}^{-1}(y) = \ker d_z\mathcal{F}$ at each of its points* — the set $\mathcal{Z} = \mathcal{F}^{-1}(y)$ is a smooth embedded submanifold with $T_z\mathcal{Z} = \ker d_z\mathcal{F}$ for every $z \in \mathcal{Z}$. The projection $\operatorname{pr}_W : X \times W \to W$ is smooth (linear in charts), so its restriction $\pi = \operatorname{pr}_W|_{\mathcal{Z}}$ to the submanifold $\mathcal{Z}$ is smooth, and its differential at $z = (x, w)$ is the restriction of $d(\operatorname{pr}_W) = \operatorname{pr}_W$ to $T_z\mathcal{Z} = \ker d_z\mathcal{F}$, namely
> $$d\pi_z : \ker d_z\mathcal{F} \to T_wW, \qquad (\dot{x}, \dot{w}) \mapsto \dot{w}.$$
> As a submanifold of the second countable $X \times W$, the manifold $\mathcal{Z}$ is itself second countable, so $\pi$ is a smooth map between second countable Banach manifolds — the setting the Sard–Smale theorem requires in Step 4.
>
> **Step 1 — $\pi$ is Fredholm and its index equals the sliced index.** Fix $z = (x, w) \in \mathcal{Z}$ and set $A = d_x\mathcal{F}_w$, $B = \partial_w\mathcal{F}(x, w)$, so $d_z\mathcal{F}(\dot{x}, \dot{w}) = A\dot{x} + B\dot{w}$. Hypothesis (A) says $A$ is Fredholm and hypothesis (C) says $d_z\mathcal{F}$ is surjective, so Lemma 1 applies at $z$. By Lemma 1(c), $d\pi_z$ is a Fredholm operator with
> $$\operatorname{index} d\pi_z = \operatorname{index} A = \operatorname{index} d_x\mathcal{F}_w = \operatorname{index}\mathcal{F}_w \qquad \text{(by Lemma 1(c) and the definition of the sliced index)}.$$
> Since $z \in \mathcal{Z}$ was arbitrary, $d\pi_z$ is Fredholm at every point, so $\pi$ is a Fredholm map.
>
> **Step 2 — the index is $\operatorname{index} F$.** By Lemma 2, $\operatorname{index}\mathcal{F}_w = \operatorname{index} F$ for every $w$. Combining with Step 1,
> $$\operatorname{index}\pi = \operatorname{index} d\pi_z = \operatorname{index}\mathcal{F}_w = \operatorname{index} F \qquad \text{(by Step 1 and Lemma 2)},$$
> a single integer independent of $z$, as claimed in (i). (Consistency check: this is the Fredholm index of $\pi$, not of $\mathcal{F}$; the two differ, since $\pi$ forgets only the finitely-many cokernel directions the projection cannot reach, while $\mathcal{F}$ maps to $Y$.)
>
> **Step 3 — regular values of $\pi$ are exactly the good parameters.** Let $w \in W$. By definition $w$ is a regular value of $\pi$ if and only if $d\pi_z$ is surjective for every $z \in \pi^{-1}(w)$. Now $z \in \pi^{-1}(w)$ means $z = (x, w)$ with $\mathcal{F}(x, w) = y$, i.e. $x \in \mathcal{F}_w^{-1}(y)$. By Lemma 1(c), for such a $z$ the differential $d\pi_z$ is surjective if and only if $d_x\mathcal{F}_w = A$ is surjective. Hence
> $$w \text{ regular value of } \pi \iff d_x\mathcal{F}_w \text{ surjective for all } x \in \mathcal{F}_w^{-1}(y) \iff y \text{ regular value of } \mathcal{F}_w \qquad \text{(by Lemma 1(c) and the definition of a regular value)}.$$
> In the case $\mathcal{F}_w^{-1}(y) = \varnothing$ both sides hold vacuously, so the equivalence is uniform. This says precisely $W_0 = \{w : w \text{ is a regular value of } \pi\}$, and completes the proof of (i).
>
> **Step 4 — genericity via Sard–Smale.** The map $\pi : \mathcal{Z} \to W$ is, by Steps 0–1, a smooth Fredholm map between second countable Banach manifolds. By [[Thm - Sard-Smale Theorem|the Sard–Smale theorem]] — *the set of regular values of a smooth Fredholm map between second countable Banach manifolds is residual in the target, in particular dense* — the set of regular values of $\pi$ is residual in $W$. By Step 3 this set equals $W_0$. Therefore $W_0$ is residual in $W$. Since $W$ is a Banach manifold, hence a Baire space, [[Thm - Baire Category Theorem|Baire's theorem]] gives that a residual subset of $W$ is dense, so $W_0$ is dense. This proves (ii).
>
> Combining Steps 1–4 establishes both parts of the theorem. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Finite-dimensional transversality (the Thom parametric transversality theorem).** Take $X$, $W$, $Y$ finite-dimensional smooth manifolds and $\mathcal{F} : X \times W \to Y$ smooth with $y$ a regular value. Every differential is automatically Fredholm (index $\dim X - \dim Y$ for the sliced maps), so the theorem specialises to the classical Thom parametric transversality theorem: for almost every parameter $w$, the sliced map $\mathcal{F}_w$ has $y$ as a regular value. The theorem applies because the finite-dimensional Sard theorem is the base case of Sard–Smale; the non-obvious point is that the *same* cokernel computation drives both the finite- and infinite-dimensional statements, so one proof serves the whole hierarchy.

**Generic simplicity of eigenvalues.** Consider a smooth family of self-adjoint elliptic operators $L_w$ on a closed manifold, parametrised by $w$ in a Banach space of zeroth-order perturbations, and the map $\mathcal{F}(u, \lambda, w) = (L_w u - \lambda u,\, \|u\|^2 - 1)$ whose zero set records normalised eigenpairs. Parametric transversality applies to show that for a residual set of perturbations every eigenvalue is simple. It is non-obvious because "simple eigenvalue" is a transversality condition on the fibre of a projection, and the perturbation freedom in $w$ is exactly what surjects onto the obstruction cokernel.

**Generic metrics and the anti-self-duality operator.** With $W$ a Banach manifold of Riemannian metrics on a four-manifold and $\mathcal{F}$ the family of anti-self-duality operators coupled to a connection, parametric transversality is the analytic heart of the Freed–Uhlenbeck theorem that for a residual set of metrics the moduli space of anti-self-dual connections is a smooth manifold of the expected dimension. The application is subtle because one must verify hypothesis (C) — surjectivity of the total differential including the metric direction — which requires a unique-continuation argument showing a cokernel element orthogonal to all metric variations must vanish.

---

# Bridges

- **[[Thm - Sard-Smale Theorem|The Sard–Smale theorem]]** is the engine this theorem hands its work to. Sard–Smale is the "move the value" transversality statement; parametric transversality is the reduction that lets you apply it when the value is frozen, by moving the parameter instead. The bridge is the identity $\operatorname{coker} d\pi_z \cong \operatorname{coker} d_x\mathcal{F}_w$ of Lemma 1: it makes the regular values of the projection $\pi$ coincide with the good parameters, so that Sard–Smale for $\pi$ *is* genericity of good parameters. No further analysis is needed once the cokernel isomorphism is in hand.

- **[[Thm - Regular Value and Transversality Theorems for Fredholm Maps|The regular-value theorem for Fredholm maps]]** enters twice, in opposite roles. It first makes the universal zero set $\mathcal{Z}$ a manifold, from hypothesis (C) applied to the total map $\mathcal{F}$; it is then applied a *second* time, downstream, to each good sliced map $\mathcal{F}_w$ for $w \in W_0$, producing the smooth perturbed solution manifold $\mathcal{F}_w^{-1}(y)$ of dimension $\operatorname{index} F$. The theorem on this page is exactly the bridge from the first application to the second.

- **[[Thm - The Generic Parametric Count Defines the Mod-2 Degree|The parametric count as a definition of the degree]]** builds directly on this page. Adding properness (hypothesis (D)) and $\operatorname{index} F = 0$, the residual good parameters give finite fibres $\mathcal{F}_w^{-1}(y)$, and a generic path between two good parameters produces, again by parametric transversality applied to the path family $\mathbb{F}(x, \gamma, t) = \mathcal{F}(x, \gamma(t))$, a compact one-dimensional cobordism whose boundary is the two fibres. The parity of the count is therefore parameter-independent, which is the degree.

- **[[Thm - Stabilisation of Fredholm Operators and Continuity of the Kernel|The stabilisation theorem]]** supplies the one ingredient the pointwise computation cannot: that the sliced index $\operatorname{index}\mathcal{F}_w$ is one number and not a function of $w$. The construction is that the differentials $d_x\mathcal{F}_w$ form a norm-continuous family of Fredholm operators over the connected $X \times W$, and the index is locally constant on the open set of Fredholm operators; connectivity does the rest. This is Lemma 2.

- **Generic regularity of the Seiberg–Witten moduli space (chapter XI).** There the configuration space is a Sobolev completion of connection-and-spinor pairs, the parameter is a perturbing self-dual two-form, and $y = 0$ is the gauge-fixed value. Parametric transversality, applied to the perturbed Seiberg–Witten map, is the statement that for a residual set of perturbations the moduli space is a smooth manifold of the expected dimension; the surjectivity hypothesis (C) is verified by a Weitzenböck-and-unique-continuation argument that the construction on this page then converts into genericity.

---

# Unlocked by This

> [!tip] Generic Smoothness of Moduli Spaces *(from Gauge Theory)*
> Every moduli space in this series that is smooth "for a generic perturbation" — the anti-self-dual instanton moduli space, the Seiberg–Witten moduli space — is smooth *because* of this theorem: the perturbations form the parameter manifold $W$, the equation defines the family $\mathcal{F}$, and $W_0$ is the residual set of perturbations for which the moduli space is cut out transversally. See **Thm - Generic Regularity and Orientability of the Seiberg-Witten Moduli Space** (chapter XI).

> [!tip] The Parametric Mod-2 and Integer Degree *(from Fredholm Degree Theory)*
> Because the good-parameter count is parameter-independent (via the cobordism built on this page), it can *be* the definition of the degree of a proper Fredholm map, bypassing the direct construction that moves the value. This is the definition used in equivariant settings, where the value is not free to move. See [[Thm - The Generic Parametric Count Defines the Mod-2 Degree]].
