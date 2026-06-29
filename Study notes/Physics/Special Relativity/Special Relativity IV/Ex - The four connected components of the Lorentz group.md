---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Lorentz Group"
  - "Thm - Invariance of the Spacetime Interval"
tags: [physics, special-relativity]
---

# Problem Statement

Let $O(1,3) = \{\Lambda : \Lambda^{\mathsf T}\eta\,\Lambda = \eta\}$, $\eta = \mathrm{diag}(1,-1,-1,-1)$.

1. Show that every $\Lambda \in O(1,3)$ has $\det\Lambda = \pm 1$ and $\Lambda^0{}_0 \ge 1$ or $\Lambda^0{}_0 \le -1$. Conclude these two signs split $O(1,3)$ into (at most) four disjoint pieces.
2. Exhibit one element of each piece: the identity, parity $P = \mathrm{diag}(1,-1,-1,-1)$, time reversal $T = \mathrm{diag}(-1,1,1,1)$, and the spacetime inversion $PT = -\mathrm{Id} = \mathrm{diag}(-1,-1,-1,-1)$. Compute $(\det, \mathrm{sgn}\,\Lambda^0{}_0)$ for each and place it.
3. Show that exactly one of the four pieces is a subgroup — the **restricted Lorentz group** $SO^+(1,3)$, with $\det = +1$ and $\Lambda^0{}_0 \ge 1$ — and that the other three are not. Show every $\Lambda \in O(1,3)$ is one of $\Lambda_0$, $P\Lambda_0$, $T\Lambda_0$, $PT\Lambda_0$ with $\Lambda_0 \in SO^+(1,3)$.
4. Show that $\{\mathrm{Id}, P, T, PT\}$ is a subgroup isomorphic to the Klein four-group $\mathbb{Z}/2 \times \mathbb{Z}/2$.

**Recall:**

![[Def - The Lorentz Group#The Definition]]

A subset of a group is a **subgroup** if it contains the identity and is closed under products and inverses. The Klein four-group $\mathbb{Z}/2 \times \mathbb{Z}/2$ is the group of order $4$ in which every non-identity element has order $2$ and the product of any two distinct non-identity elements is the third. The two scalar functions $\det\Lambda$ and $\mathrm{sgn}\,\Lambda^0{}_0$ are constant on each connected component of $O(1,3)$.

---

# Convergent Strategy

**Problem class.** A *structural / classification* problem: decompose a group into its connected components and identify the distinguished subgroup. The [[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group#Problem-Solving Strategy|topic strategy]]'s fourth target — verifying group structure and counting pieces.

**Assumption pattern.** The defining equation $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$, used to extract the two sign invariants ($\det = \pm 1$ from a determinant; $\Lambda^0{}_0 \ge 1$ or $\le -1$ from the $(0,0)$ component). Recognising that these two *independent* binary invariants give $2 \times 2 = 4$ pieces is the organising idea.

**Theorem routing.** Part 1 extracts the invariants from the defining equation; Part 2 evaluates them on $\{\mathrm{Id}, P, T, PT\}$; Part 3 checks the subgroup property (only $\det = +1$, orthochronous is closed) and the coset decomposition; Part 4 is a $4$-element multiplication table. The route is: defining equation $\to$ two sign invariants $\to$ four cosets of $SO^+(1,3)$.

**Key decision point.** The crux is to see that the *product of two improper* (or two antichronous) transformations is *proper* (resp. orthochronous): $\det(PT \cdot PT) = (+1)$, $(-1)(-1) = +1$ for the orthochronous product, so the non-identity pieces are not closed — only the piece where both invariants are $+1$ is a subgroup. This is why $SO^+(1,3)$ is singled out: it is the unique piece containing the identity and closed under the group law.

---

# Legal Operations Used

1. **Take determinants of a matrix equation (operation 2 from Ex - pseudo-orthogonal).** Applying $\det$ to $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ gives $(\det\Lambda)^2 = 1$.

2. **Extract a component condition from the defining equation.** Setting $\mu = \nu = 0$ in the index form $\eta_{\alpha\beta}\Lambda^\alpha{}_0\Lambda^\beta{}_0 = \eta_{00}$ yields $(\Lambda^0{}_0)^2 = 1 + \sum_i (\Lambda^i{}_0)^2 \ge 1$.

3. **Compose with discrete reflections (operation: classify a four-vector / use the light cone, applied to the group).** Multiplying by $P$, $T$, or $PT$ moves between components, which is how the coset decomposition and the Klein group arise.

---

# Hints

> [!note]- Hint 1
> For $\det$: take the determinant of both sides of $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$, using $\det\eta = -1$. For $\Lambda^0{}_0$: write the $(0,0)$ entry of the defining equation in index form and isolate $(\Lambda^0{}_0)^2$.

> [!note]- Hint 2
> $\det P = (1)(-1)(-1)(-1) = -1$ and $P^0{}_0 = 1$. $\det T = (-1)(1)(1)(1) = -1$ and $T^0{}_0 = -1$. $\det(PT) = +1$ and $(PT)^0{}_0 = -1$. The identity has $\det = +1$, $\mathrm{Id}^0{}_0 = 1$. Four distinct sign-pairs.

> [!note]- Hint 3
> A subgroup must contain the identity, whose invariants are $(+1, +)$. Check closure: is the product of two transformations with $\det = -1$ again $\det = -1$? No — it is $+1$. So no piece with $\det = -1$ is closed. Same for $\Lambda^0{}_0 \le -1$.

> [!note]- Hint 4
> $P^2 = T^2 = (PT)^2 = \mathrm{Id}$ (each is its own inverse), and $P\cdot T = PT$, $P\cdot PT = T$ (since $P^2 = \mathrm{Id}$), $T \cdot PT = P$. Every non-identity element has order $2$; the product of two distinct ones is the third.

---

# Solution

The exercise decomposes $O(1,3)$ by its two sign invariants. Step 1 extracts them from the defining equation and counts four pieces. Step 2 plants a flag in each piece with the discrete transformations. Step 3 shows only the all-$+$ piece is a subgroup and that the discrete transformations generate the cosets. Step 4 identifies the discrete part as the Klein four-group.

**Step 1: two sign invariants, four pieces.**

> [!note]- Derivation
> *Determinant.* Take $\det$ of $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$: $\det\Lambda^{\mathsf T}\det\eta\det\Lambda = \det\eta$, i.e. $(\det\Lambda)^2(-1) = -1$, so $(\det\Lambda)^2 = 1$ and $\det\Lambda = \pm 1$.
>
> *Time component.* In index form the defining equation is $\eta_{\alpha\beta}\Lambda^\alpha{}_\mu\Lambda^\beta{}_\nu = \eta_{\mu\nu}$. Set $\mu = \nu = 0$:
> $$\eta_{\alpha\beta}\Lambda^\alpha{}_0\Lambda^\beta{}_0 = \eta_{00} = +1.$$
> With $\eta = \mathrm{diag}(1,-1,-1,-1)$ the left side is $(\Lambda^0{}_0)^2 - \sum_{i=1}^3 (\Lambda^i{}_0)^2$, so
> $$(\Lambda^0{}_0)^2 = 1 + \sum_{i=1}^3 (\Lambda^i{}_0)^2 \ge 1.$$
> Hence $\Lambda^0{}_0 \ge 1$ or $\Lambda^0{}_0 \le -1$; the value $\Lambda^0{}_0 = 0$ and the band $(-1, 1)$ are forbidden.
>
> The two signs — $\mathrm{sgn}(\det\Lambda) \in \{+, -\}$ and $\mathrm{sgn}(\Lambda^0{}_0) \in \{+, -\}$ — are independent and each takes two values, so $O(1,3)$ splits into at most $2 \times 2 = 4$ disjoint pieces. (Each is in fact connected, being a continuous image of $SO^+(1,3)$; here we only need disjointness.)

**Step 2: a representative of each piece.**

> [!note]- Derivation
> All four matrices are diagonal with entries $\pm 1$, hence satisfy $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ (a diagonal $\pm 1$ matrix commutes with $\eta$ and squares to the identity, so $\Lambda\eta\Lambda = \eta$). Their invariants:
>
> | $\Lambda$ | $\det\Lambda$ | $\Lambda^0{}_0$ | component |
> |---|---|---|---|
> | $\mathrm{Id} = \mathrm{diag}(1,1,1,1)$ | $+1$ | $+1$ | proper orthochronous $SO^+$ |
> | $P = \mathrm{diag}(1,-1,-1,-1)$ | $-1$ | $+1$ | improper orthochronous |
> | $T = \mathrm{diag}(-1,1,1,1)$ | $-1$ | $-1$ | improper antichronous |
> | $PT = \mathrm{diag}(-1,-1,-1,-1)$ | $+1$ | $-1$ | proper antichronous |
>
> All four sign-pairs $(\pm, \pm)$ are realised, so there are exactly four non-empty components, and $\{\mathrm{Id}, P, T, PT\}$ is a transversal — one representative each.

**Step 3: only $SO^+(1,3)$ is a subgroup; the coset decomposition.**

> [!note]- Derivation
> A subgroup must contain the identity, which lives in the $(\det = +1, \Lambda^0{}_0 \ge 1)$ piece. That piece, $SO^+(1,3)$, *is* a subgroup: $\det$ is multiplicative so the product of two $\det = +1$ maps has $\det = +1$; the orthochronous maps are closed under products and inverses (a product of two future-preserving maps preserves the future, since each maps the forward cone into itself — this uses [[Thm - Invariance of the Spacetime Interval|interval invariance]] to control the time component); and the identity has both invariants $+$. So $SO^+(1,3)$ is closed under products and inverses and contains $\mathrm{Id}$.
>
> None of the other three pieces is a subgroup, because none contains the identity (their invariants differ from $(+, +)$). Equivalently, they fail closure: the product of two improper transformations is *proper* ($\det = (-1)(-1) = +1$), and the product of two antichronous transformations is *orthochronous*, so the improper or antichronous pieces are not closed under multiplication.
>
> *Coset decomposition.* Given any $\Lambda \in O(1,3)$, multiply by whichever of $\{\mathrm{Id}, P, T, PT\}$ restores both invariants to $+$:
> - if $\Lambda \in SO^+$, then $\Lambda = \mathrm{Id}\cdot\Lambda$;
> - if $\Lambda$ is improper orthochronous, then $P\Lambda$ is proper orthochronous (multiplying by $P$ flips $\det$, leaves $\Lambda^0{}_0 \ge 1$), so $\Lambda = P\Lambda_0$ with $\Lambda_0 = P\Lambda \in SO^+$;
> - if $\Lambda$ is improper antichronous, then $T\Lambda \in SO^+$, so $\Lambda = T\Lambda_0$;
> - if $\Lambda$ is proper antichronous, then $PT\Lambda \in SO^+$, so $\Lambda = PT\Lambda_0$.
>
> Thus $O(1,3) = SO^+(1,3) \sqcup P\,SO^+(1,3) \sqcup T\,SO^+(1,3) \sqcup PT\,SO^+(1,3)$: the four components are the four cosets of $SO^+(1,3)$, and $SO^+(1,3)$ is a normal subgroup of index $4$.

**Step 4: $\{\mathrm{Id}, P, T, PT\}$ is the Klein four-group.**

> [!note]- Derivation
> Each of $P, T, PT$ is diagonal with $\pm 1$ entries, so each squares to $\mathrm{Id}$: $P^2 = T^2 = (PT)^2 = \mathrm{Id}$. Thus every non-identity element has order $2$. The products:
> $$P\cdot T = \mathrm{diag}(1,-1,-1,-1)\,\mathrm{diag}(-1,1,1,1) = \mathrm{diag}(-1,-1,-1,-1) = PT,$$
> and since $P^2 = \mathrm{Id}$, $P\cdot(PT) = P^2 T = T$, and $T\cdot(PT) = T^2 P = P$. So the product of any two distinct non-identity elements is the third. This is exactly the multiplication table of the Klein four-group $\mathbb{Z}/2 \times \mathbb{Z}/2$ (the unique group of order $4$ that is not cyclic). The set is closed, contains the identity, and each element is its own inverse, so it is a subgroup of $O(1,3)$ isomorphic to $\mathbb{Z}/2 \times \mathbb{Z}/2$ — the discrete part of the Lorentz group.

> [!note]- Complete formal solution
> From $\Lambda^{\mathsf T}\eta\Lambda = \eta$: taking $\det$ gives $(\det\Lambda)^2 = 1$; setting $\mu = \nu = 0$ gives $(\Lambda^0{}_0)^2 = 1 + \sum_i(\Lambda^i{}_0)^2 \ge 1$. So $\det\Lambda = \pm 1$ and $\Lambda^0{}_0 \ge 1$ or $\le -1$, two independent binary invariants splitting $O(1,3)$ into four disjoint pieces. The diagonal $\pm 1$ matrices $\mathrm{Id}, P = \mathrm{diag}(1,-1,-1,-1), T = \mathrm{diag}(-1,1,1,1), PT = -\mathrm{Id}$ realise the four sign-pairs $(+,+), (-,+), (-,-), (+,-)$, one per piece. Only the $(+,+)$ piece $SO^+(1,3)$ contains the identity and is closed under products and inverses (a subgroup); the others fail closure because a product of two $\det = -1$ (resp. antichronous) maps is $\det = +1$ (resp. orthochronous). Multiplying any $\Lambda$ by the appropriate one of $\{\mathrm{Id}, P, T, PT\}$ lands in $SO^+(1,3)$, so $O(1,3) = SO^+ \sqcup P\,SO^+ \sqcup T\,SO^+ \sqcup PT\,SO^+$. Finally $P^2 = T^2 = (PT)^2 = \mathrm{Id}$ and $PT = P\cdot T$, with the product of any two distinct non-identity elements the third, so $\{\mathrm{Id}, P, T, PT\} \cong \mathbb{Z}/2 \times \mathbb{Z}/2$. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> It is tempting to think the four pieces are "rotations, boosts, reflections, and time-reversals" — but rotations and boosts both lie in the *single* component $SO^+(1,3)$ (both have $\det = +1$, $\Lambda^0{}_0 \ge 1$), and they are connected to the identity by continuous paths. The four *components* are distinguished only by the two discrete signs, not by the rotation/boost split, which is a decomposition *within* the identity component. Conflating "boost vs rotation" (a continuous, intra-component distinction) with "the four components" (a discrete inter-component distinction) is the standard confusion; the components are about parity and time direction, not about the type of continuous transformation.

---

# Key Takeaways

**Two independent discrete invariants partition a group into components.** The transferable structure is that $\det\Lambda = \pm 1$ and $\mathrm{sgn}\,\Lambda^0{}_0 = \pm$ are two functions, each locally constant and each taking two values, so together they cut $O(1,3)$ into $2 \times 2 = 4$ pieces. Whenever a matrix group is defined by a congruence and you want its component structure, hunt for the locally-constant invariants: the determinant (orientation) almost always gives one, and for indefinite signatures the sign of a diagonal block (here the time block) gives another. The number of components is the product of the ranges of these invariants, and the identity component is where all invariants take their "trivial" value. This is the finite-group shadow cast by a Lie group's topology.

**Only the all-trivial-invariant component is a subgroup; the rest are its cosets.** The reason $SO^+(1,3)$ is singled out is purely group-theoretic: a subgroup must contain the identity, and the identity has $\det = +1$ and $\Lambda^0{}_0 \ge 1$, so the identity component is the only candidate — and it is closed precisely because $\det$ is multiplicative and the orthochronous condition is preserved under products. The other three components are *cosets* of this subgroup, reached by multiplying by parity, time reversal, or both, and they fail to be subgroups because the product of two "odd" elements is "even" (two sign flips cancel). This coset picture — a distinguished connected subgroup with the discrete symmetries acting as coset representatives — recurs throughout physics: $SO^+(1,3)$ is to $O(1,3)$ as the connected component is to the full symmetry group, and the discrete quotient $O(1,3)/SO^+(1,3) \cong \mathbb{Z}/2 \times \mathbb{Z}/2$ encodes the physical operations of parity ($P$) and time reversal ($T$) whose violation or conservation is a central question in particle physics.

**Parity and time reversal generate the Klein four-group, the discrete skeleton of Lorentz symmetry.** The discrete part $\{\mathrm{Id}, P, T, PT\} \cong \mathbb{Z}/2 \times \mathbb{Z}/2$ is the seed of the discrete symmetries $C, P, T$ of quantum field theory (with $C$, charge conjugation, added when antiparticles enter). Each generator is an involution, and their combination $PT$ (spacetime inversion, $-\mathrm{Id}$) is the proper antichronous representative. Recognising this Klein-four structure inside the Lorentz group is what organises the discussion of which physical laws respect $P$, $T$, or only the combination $CPT$ — the $CPT$ theorem being the statement that the combined operation is always a symmetry of a local Lorentz-invariant quantum field theory. The continuous $SO^+(1,3)$ governs the kinematics of boosts and rotations; this finite quotient governs the discrete symmetries, and the two together are the full Lorentz group.
