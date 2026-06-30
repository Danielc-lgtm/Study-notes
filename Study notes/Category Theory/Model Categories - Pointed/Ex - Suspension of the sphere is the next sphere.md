---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Pointed Model Category Suspension and Loop"
  - "Def - Pullback and Pushout"
  - "Def - Higher Homotopy Group"
  - "Def - Cylinder Object, Path Object, and Homotopy"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Work in $\mathbf{Top}_*$, pointed spaces with the Quillen model structure.

1. Compute the [[Def - Pointed Model Category Suspension and Loop|suspension]] $\Sigma S^n$ from the cone-and-collapse (homotopy pushout) construction and show $\Sigma S^n \simeq S^{n+1}$ for all $n \ge 0$.
2. Deduce the **suspension isomorphism**: for any pointed space $Z$ and any (reduced) cohomology theory $E^*$, the suspension induces $\widetilde{E}^{\,k}(\Sigma X) \cong \widetilde{E}^{\,k-1}(X)$, and on homotopy $[\Sigma X, Z] \cong [X, \Omega Z]$ specializes for $X = S^n$ to $\pi_{n+1}(\Sigma\text{-shift})$.
3. Explain why iterating gives every sphere from $S^0$: $S^{n} = \Sigma^{n} S^0$.

**Recall:**

The [[Def - Pointed Model Category Suspension and Loop|suspension]] $\Sigma X$ is the homotopy pushout of $* \leftarrow X \rightarrow *$; in $\mathbf{Top}_*$ it is the reduced suspension $X \wedge S^1$, obtained by taking the cylinder $X \times [0,1]$, collapsing both ends $X \times \{0\}$ and $X \times \{1\}$, and reducing along the basepoint arc. The [[Def - Higher Homotopy Group|homotopy group]] is $\pi_n(Z) = [S^n, Z]$, the based homotopy classes of maps from the $n$-sphere. A reduced cohomology theory $\widetilde{E}^*$ is a sequence of contravariant homotopy functors with a suspension isomorphism and exactness on cofiber sequences. The $n$-sphere $S^n$ is the one-point compactification of $\mathbb{R}^n$, with $S^0 = \{x_0, p\}$ two points.

---

# Convergent Strategy

**Problem class:** This is a "compute a derived (co)limit and read off its consequences" exercise. The computation of $\Sigma S^n$ is a direct homotopy-pushout calculation; the consequences are the standard structural facts (suspension isomorphism, building spheres) that follow once the computation is in hand.

**Assumption pattern:** The assumption is that we are in $\mathbf{Top}_*$, where the cylinder is the literal $X \times [0,1]$ and every space is suspended by smashing with $S^1$. This concreteness is what makes the sphere computation a hands-on gluing rather than an abstract homotopy colimit. The sphere $S^n$ being the suspension of $S^{n-1}$ is geometrically visible: $S^{n}$ is two hemispheres (cones) glued along the equator $S^{n-1}$.

**Theorem routing:** Part (1) routes through the cone-and-collapse construction and the [[Def - Homeomorphism|homeomorphism]] $S^{n-1} \ast S^0 \cong S^n$ (join), or equivalently $S^{n-1} \wedge S^1 \cong S^n$. Part (2) routes through the [[Thm - The Suspension-Loop Adjunction|suspension–loop adjunction]] and the exactness of a cohomology theory on cofiber sequences. Part (3) is induction on $n$ using part (1).

**Key decision point:** The non-obvious choice is to recognize the *equator* $S^{n-1}$ as the object being suspended: $S^n$ is the double cone (suspension) on its equator. Seeing this turns "compute $\Sigma S^n$" into "recognize $S^{n+1}$ as the double cone on $S^n$," which is immediate once the picture is right. The alternative — computing the smash $S^n \wedge S^1$ from the smash definition — works but is less illuminating.

---

# Legal Operations Used

1. **Operation 1 from the topic page (replace a strict (co)limit by its homotopy version).** The suspension is the homotopy pushout; the computation uses the cylinder model rather than the strict pushout.

2. **Operation 8 from the topic page (specialize to the enriched formula $\Sigma = -\wedge S^1$).** Part (1) uses $\Sigma S^n = S^n \wedge S^1$ and the homeomorphism $S^n \wedge S^1 \cong S^{n+1}$.

3. **Operation 5 from the topic page (apply $[-, Z]$ to a cofiber sequence).** Part (2) uses exactness of a cohomology theory on the cofiber sequence $S^{n-1} \to D^n \to S^n$ to obtain the suspension isomorphism.

---

# Hints

> [!note]- Hint 1
> The sphere $S^n$ is the union of two closed hemispheres (each a disk $D^n$, hence contractible, i.e. a cone) glued along the equator $S^{n-1}$. What construction takes an object and glues two cones on it?

> [!note]- Hint 2
> The double cone on $X$ — glue $CX$ on each side along $X$ — is exactly the (unreduced) suspension. So $S^n =$ double cone on $S^{n-1} = \Sigma S^{n-1}$.

> [!note]- Hint 3
> For part (2), use the cofiber sequence $S^{n-1} \hookrightarrow D^n \to S^n$ with $D^n \simeq *$. Exactness of $\widetilde{E}^*$ and the contractibility of $D^n$ force $\widetilde{E}^k(S^n) \cong \widetilde{E}^{k-1}(S^{n-1})$ — that is the suspension isomorphism in disguise.

---

# Solution

The solution computes $\Sigma S^n = S^{n+1}$ by recognizing the sphere as a double cone, then reads off the suspension isomorphism from exactness and the building of all spheres by iteration.

**Step 1: $\Sigma S^n \simeq S^{n+1}$ via the double-cone picture.**

> [!note]- Derivation
> The (unreduced) [[Def - Pointed Model Category Suspension and Loop|suspension]] of $X$ is the double cone: glue a cone $CX = (X \times [0,1])/(X \times \{1\})$ on each side of $X$, i.e. $\Sigma X = CX \cup_X CX$, which is the homotopy pushout of $* \leftarrow X \rightarrow *$ (each $*$ being a cone point). Now take $X = S^n$. The sphere $S^{n+1} = \{v \in \mathbb{R}^{n+2} : |v| = 1\}$ is the union of its upper hemisphere $\{v_{n+2} \ge 0\}$ and lower hemisphere $\{v_{n+2} \le 0\}$, glued along the equator $\{v_{n+2} = 0\} = S^n$. Each closed hemisphere is homeomorphic to the disk $D^{n+1}$, which is the cone $CS^n$ on the equatorial sphere (radial contraction to the pole). Hence
> $$S^{n+1} = D^{n+1} \cup_{S^n} D^{n+1} = CS^n \cup_{S^n} CS^n = \Sigma S^n.$$
> Reducing along the basepoint arc changes the result only up to weak equivalence, so $\Sigma S^n \simeq S^{n+1}$. Equivalently in smash terms, $\Sigma S^n = S^n \wedge S^1 \cong S^{n+1}$, since $S^a \wedge S^b \cong S^{a+b}$.

**Step 2: The suspension isomorphism.**

> [!note]- Derivation
> Consider the cofiber sequence of the boundary inclusion $S^{n-1} \hookrightarrow D^n$. The homotopy cofiber is $D^n/S^{n-1} = S^n$, giving the cofiber sequence
> $$S^{n-1} \to D^n \to S^n \to \Sigma S^{n-1} = S^n.$$
> Apply a reduced cohomology theory $\widetilde{E}^*$ (a contravariant homotopy functor sending cofiber sequences to long exact sequences). Since $D^n \simeq *$, all its reduced cohomology vanishes, so the long exact sequence
> $$\widetilde{E}^{k}(D^n) \to \widetilde{E}^{k}(S^{n-1}) \to \widetilde{E}^{k+1}(S^n) \to \widetilde{E}^{k+1}(D^n)$$
> has zeros at both ends, forcing the middle map to be an isomorphism: $\widetilde{E}^{k}(S^{n-1}) \cong \widetilde{E}^{k+1}(S^n)$. Replacing $S^n$ by $\Sigma S^{n-1}$, this is the suspension isomorphism $\widetilde{E}^{k}(X) \cong \widetilde{E}^{k+1}(\Sigma X)$ for $X = S^{n-1}$. On homotopy, the [[Thm - The Suspension-Loop Adjunction|adjunction]] $[\Sigma X, Z] \cong [X, \Omega Z]$ specializes with $X = S^n$ to $[\Sigma S^n, Z] = [S^{n+1}, Z] = \pi_{n+1}(Z)$ and $[S^n, \Omega Z] = \pi_n(\Omega Z)$, recovering $\pi_{n+1}(Z) \cong \pi_n(\Omega Z)$.

**Step 3: All spheres are iterated suspensions of $S^0$.**

> [!note]- Derivation
> By Step 1, $\Sigma S^n \simeq S^{n+1}$ for all $n \ge 0$. Starting from $S^0$ and applying $\Sigma$ repeatedly,
> $$\Sigma^n S^0 \simeq \Sigma^{n-1} S^1 \simeq \cdots \simeq \Sigma S^{n-1} \simeq S^n.$$
> So every sphere is an iterated suspension of $S^0$. This is why $S^0$ generates the spheres under suspension, and (after stabilization) why the sphere *spectrum* is the unit of the stable homotopy category.

> [!note]- Complete formal solution
> **(1)** The suspension $\Sigma X$ is the double cone $CX \cup_X CX$ (homotopy pushout of $* \leftarrow X \rightarrow *$). The sphere $S^{n+1}$ is its two hemispheres $D^{n+1} \cong CS^n$ glued along the equator $S^n$, so $S^{n+1} = CS^n \cup_{S^n} CS^n = \Sigma S^n$. Up to reduction, $\Sigma S^n \simeq S^{n+1}$.
>
> **(2)** From the cofiber sequence $S^{n-1} \to D^n \to S^n$ with $D^n \simeq *$, a reduced cohomology theory gives $\widetilde{E}^{k}(S^{n-1}) \cong \widetilde{E}^{k+1}(S^n) = \widetilde{E}^{k+1}(\Sigma S^{n-1})$, the suspension isomorphism. The adjunction $[\Sigma S^n, Z] \cong [S^n, \Omega Z]$ is $\pi_{n+1}(Z) \cong \pi_n(\Omega Z)$.
>
> **(3)** Iterating $\Sigma S^n \simeq S^{n+1}$ gives $\Sigma^n S^0 \simeq S^n$. $\blacksquare$

---

# Key Takeaways

**A sphere is the suspension of its equator, and this is the geometric face of $\Sigma X =$ double cone.** The single most useful picture for the suspension is "glue two cones," and the sphere makes it concrete: $S^{n+1}$ is two hemispherical caps (cones on the equator) glued along $S^n$. Once this is internalized, the abstract homotopy pushout $* \leftarrow X \rightarrow *$ stops being a formal definition and becomes the obvious double-cone construction. The transferable trigger is: whenever you must suspend an object you can see as an "equator," realize the suspension as the two cones it bounds. This same picture explains why suspension raises [[Def - Dimension|dimension]] by one — each cone adds a coordinate, and the two cones share the original object as a face.

**The suspension isomorphism is exactness applied to a contractible-cone cofiber sequence.** The clean way to get $\widetilde{E}^k(\Sigma X) \cong \widetilde{E}^{k-1}(X)$ is not to define cohomology axiomatically and impose it, but to derive it from the cofiber sequence $X \to CX \to \Sigma X$ with $CX \simeq *$: exactness plus the vanishing of cohomology on the contractible cone forces the connecting map to be an isomorphism. The reusable diagnostic is that a cofiber sequence with a contractible middle term *always* yields an isomorphism between the cohomology of the two flanking terms, shifted by one. This pattern — "kill the middle, get an isomorphism" — recurs whenever a cofiber or fiber sequence has a contractible term, and it is the workhorse behind most suspension and connecting-map computations.

**Spheres are the free objects under suspension, which is why $S^0$ is the seed of stable homotopy theory.** That every $S^n$ is $\Sigma^n S^0$ is not a curiosity; it is the reason the spheres organize all of homotopy theory. [[Def - Homotopy|Homotopy]] [[Def - Group|groups]] $\pi_n = [S^n, -]$ are "maps out of iterated suspensions of $S^0$," and after one inverts suspension (passing to spectra) the iterated suspensions of $S^0$ assemble into the **sphere spectrum**, the unit of the stable homotopy category. The takeaway for problem-solving is that any question about spheres can be reduced to a question about $S^0$ plus a count of suspensions, and the suspension–loop adjunction is what lets you trade a suspension on the source for a loop on the target at each step.
