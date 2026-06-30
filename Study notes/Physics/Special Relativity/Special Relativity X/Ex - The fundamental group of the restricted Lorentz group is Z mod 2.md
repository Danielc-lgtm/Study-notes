---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Topology of the Lorentz Group"
  - "Thm - Polar Decomposition of the Lorentz Group"
  - "Def - The Lorentz Group"
tags: [physics, special-relativity, lie-groups, topology]
---

# Problem Statement

Prove that the restricted Lorentz group has fundamental group $\pi_1(SO^+(1,3)) \cong \mathbb{Z}/2$, and connect the result to the existence of spinors.

1. Using the polar decomposition $SO^+(1,3) \cong \mathbb{R}^3 \times SO(3)$ and the product formula for fundamental groups, reduce the computation to $\pi_1(SO(3))$.
2. Show $\pi_1(SO(3)) = \mathbb{Z}/2$ by exhibiting the non-contractible loop in $SO(3) \cong \mathbb{R}\mathbb{P}^3$ (the "belt trick" loop) and arguing that traversing it twice gives a contractible loop.
3. Conclude that $SO^+(1,3)$ has a connected double cover, the simply connected universal cover, and identify it as $SL(2,\mathbb{C})$.
4. Explain why this $\mathbb{Z}/2$ is the reason a spinor changes sign under a $2\pi$ rotation but returns to itself under $4\pi$.

**Recall:**

The **fundamental group** $\pi_1(X, x_0)$ is the group of homotopy classes of loops based at $x_0$, with concatenation as the operation; a space is **simply connected** if $\pi_1$ is trivial. For path-connected $X, Y$, $\pi_1(X \times Y) \cong \pi_1(X) \times \pi_1(Y)$. A **covering map** $p : \tilde X \to X$ with $\tilde X$ simply connected is the *universal cover*, and the number of sheets equals $|\pi_1(X)|$.

![[Thm - Topology of the Lorentz Group#Statement]]

$SO(3)$ is diffeomorphic to real projective $3$-space $\mathbb{R}\mathbb{P}^3$ (the solid ball of radius $\pi$ with antipodal boundary points identified), via the angle–axis parametrisation $\boldsymbol\theta = \theta\mathbf{n}$.

---

# Convergent Strategy

**Problem class.** A *structural / topological* problem — the deepest one in the chapter, computing a fundamental group. The [[Special Relativity X — The Lorentz Group as a Lie Group#Problem-Solving Strategy|topic strategy]] reduces every topological question to the product manifold $\mathbb{R}^3 \times SO(3)$, where the contractible boost factor drops out and all topology comes from the rotations.

**Assumption pattern.** The polar decomposition presents the group as a product with one *contractible* factor ($\mathbb{R}^3$, the boosts) and one factor carrying all the topology ($SO(3)$). The signpost is that a contractible factor contributes trivial $\pi_1$, so the entire fundamental group is that of the rotation subgroup — a famous $\mathbb{Z}/2$.

**Theorem routing.** Part 1: $\pi_1(\mathbb{R}^3 \times SO(3)) = \pi_1(\mathbb{R}^3) \times \pi_1(SO(3)) = \{1\} \times \pi_1(SO(3))$ ([[Thm - Topology of the Lorentz Group]]). Part 2: model $SO(3) = \mathbb{R}\mathbb{P}^3$ as the ball with antipodal boundary gluing; a diameter is a loop (endpoints identified) that is non-contractible, and two diameters compose to a contractible loop, so $\pi_1 = \mathbb{Z}/2$. Part 3: $\pi_1 = \mathbb{Z}/2$ gives a unique connected double cover, the universal cover, realised as $SL(2,\mathbb{C})$ (via the [[Def - The Spinor Map and SL(2,C)|spinor map]]). Part 4: a spinor is a representation of the cover; the non-contractible loop (a $2\pi$ rotation) lifts to a path between the two preimages of the identity, which differ by the sign $-1$.

**Key decision point.** The crux is part 2: seeing that a *diameter* of the ball — from a boundary point $\pi\mathbf{n}$ straight through the centre to the antipode $-\pi\mathbf{n}$ — is a closed *loop*, because the antipodal boundary identification glues its two endpoints to the same point of $\mathbb{R}\mathbb{P}^3$. The non-obvious part is that this loop cannot be contracted (any contraction would have to detach an endpoint from the gluing) but that *two* such loops *can* be contracted — the belt/plate trick. This is what makes $\pi_1 = \mathbb{Z}/2$ rather than $\mathbb{Z}$ or trivial.

---

# Legal Operations Used

1. **Read topology off the product manifold (operation 8 from the topic page).** Part 1 applies $\pi_1(X \times Y) = \pi_1(X) \times \pi_1(Y)$ to $\mathbb{R}^3 \times SO(3)$, killing the boost factor.

2. **Factor a transformation by the polar decomposition (operation 7 from the topic page).** The product structure that makes part 1 possible is the polar decomposition $\Lambda = BR$, presenting the group as boosts $\times$ rotations.

---

# Hints

> [!note]- Hint 1
> The boost factor is $\mathbb{R}^3$, which is contractible, so $\pi_1(\mathbb{R}^3) = \{1\}$. By the product formula, $\pi_1(SO^+(1,3)) = \{1\} \times \pi_1(SO(3)) = \pi_1(SO(3))$. The whole problem is now $\pi_1(SO(3))$.

> [!note]- Hint 2
> Parametrise a rotation by $\boldsymbol\theta = \theta\mathbf{n}$ with angle $\theta \in [0,\pi]$ and axis $\mathbf{n}$. This fills the solid ball of radius $\pi$. The only identification is at the boundary: rotation by $\pi$ about $\mathbf{n}$ equals rotation by $\pi$ about $-\mathbf{n}$, so the antipodal boundary points $\pi\mathbf{n}$ and $-\pi\mathbf{n}$ are the same rotation.

> [!note]- Hint 3
> Consider the path that starts at the boundary point $\pi\mathbf{n}$, goes straight through the centre $\mathbf{0}$ (the identity rotation), and continues to $-\pi\mathbf{n}$. Because $\pi\mathbf{n}$ and $-\pi\mathbf{n}$ are *identified*, this path is a loop. Argue it cannot be shrunk to a point.

> [!note]- Hint 4
> Now traverse two such diameters in succession. The combined loop *can* be slid off the boundary and contracted — this is the belt trick / Dirac's plate trick. So loops come in exactly two classes (one diameter = non-trivial, two diameters = trivial), giving $\pi_1 = \mathbb{Z}/2$.

> [!note]- Hint 5
> For part 4: a spinor lives in a representation of the *double cover* $SL(2,\mathbb{C})$, not of $SO^+(1,3)$. As you rotate by $2\pi$ — traversing the non-contractible loop in the group — the lift to the cover is a *path* from one identity-preimage to the other, and the two preimages of the identity act as $+1$ and $-1$. So a $2\pi$ rotation acts as $-1$, a $4\pi$ rotation (contractible loop) as $+1$.

---

# Solution

The polar decomposition reduces $\pi_1(SO^+(1,3))$ to $\pi_1(SO(3))$, since the boost factor $\mathbb{R}^3$ is contractible. The rotation group is $\mathbb{R}\mathbb{P}^3$, the ball with antipodal boundary gluing, whose diameter is a non-contractible loop that becomes contractible when doubled — so $\pi_1 = \mathbb{Z}/2$. This $\mathbb{Z}/2$ is the double cover $SL(2,\mathbb{C})$ and the spinor sign.

**Step 1: Reduce to $\pi_1(SO(3))$.**

> [!note]- Derivation
> By [[Thm - Topology of the Lorentz Group|the topology theorem]], the polar decomposition gives a homeomorphism $SO^+(1,3) \cong \mathbb{R}^3 \times SO(3)$. The fundamental group of a product of path-connected spaces is the product of their fundamental groups:
> $$\pi_1(SO^+(1,3)) = \pi_1(\mathbb{R}^3 \times SO(3)) = \pi_1(\mathbb{R}^3) \times \pi_1(SO(3)).$$
> The boost factor $\mathbb{R}^3$ is contractible (straight-line homotopy to the origin), so $\pi_1(\mathbb{R}^3) = \{1\}$. Hence
> $$\pi_1(SO^+(1,3)) = \{1\} \times \pi_1(SO(3)) = \pi_1(SO(3)).$$
> The boosts contribute nothing; the entire topology is in the rotations.

**Step 2: $\pi_1(SO(3)) = \mathbb{Z}/2$.**

> [!note]- Derivation
> Parametrise a rotation by its angle–axis vector $\boldsymbol\theta = \theta\mathbf{n}$, with $\theta \in [0,\pi]$ the angle and $\mathbf{n} \in S^2$ the axis. This fills the closed solid ball $\bar B_\pi$ of radius $\pi$ (the centre is the identity, $\theta = 0$). The map is two-to-one only on the boundary sphere $\theta = \pi$: a rotation by $\pi$ about $\mathbf{n}$ is the *same* rotation as by $\pi$ about $-\mathbf{n}$ (both send $\mathbf{n} \mapsto \mathbf{n}$ and flip the perpendicular plane), so the antipodal boundary points $\pi\mathbf{n}$ and $\pi(-\mathbf{n}) = -\pi\mathbf{n}$ are identified. The quotient is real projective $3$-space:
> $$SO(3) \cong \bar B_\pi / (\boldsymbol\theta \sim -\boldsymbol\theta \text{ on the boundary}) = \mathbb{R}\mathbb{P}^3.$$
>
> *A non-contractible loop.* Fix an axis $\mathbf{n}$ and let $\gamma$ run from the boundary point $\pi\mathbf{n}$, along the diameter through the centre, to $-\pi\mathbf{n}$. Since $\pi\mathbf{n}$ and $-\pi\mathbf{n}$ are identified, $\gamma$ is a *loop* (its two endpoints are the same point of $\mathbb{R}\mathbb{P}^3$). It is not null-homotopic: any homotopy contracting $\gamma$ to a constant would have to move the endpoints, but the endpoints are pinned to the antipodal identification, and a continuity/degree argument shows the loop crosses the boundary an odd number of times, an invariant preserved under homotopy. So $[\gamma] \ne 1$ in $\pi_1$.
>
> *Doubling makes it contractible.* Traverse $\gamma$ twice, giving a loop $\gamma^2$ that crosses the boundary an even number of times. This loop *can* be contracted: one slides the two boundary-crossing points around the sphere until they coincide and cancel, sweeping the loop into the interior where it shrinks to a point. (This is the physical content of the Dirac belt trick: a belt given two full twists can be untwisted without moving its ends, while one twist cannot.) So $[\gamma]^2 = [\gamma^2] = 1$.
>
> Thus $[\gamma]$ has order exactly $2$, and one shows it generates: every loop is homotopic to $\gamma^k$ for some $k$, with the class depending only on $k \bmod 2$ (the parity of boundary crossings). Hence $\pi_1(SO(3)) = \langle[\gamma]\rangle \cong \mathbb{Z}/2$.

**Step 3: The double cover $SL(2,\mathbb{C})$.**

> [!note]- Derivation
> Combining Steps 1 and 2, $\pi_1(SO^+(1,3)) = \mathbb{Z}/2$. A connected space with $\pi_1 = \mathbb{Z}/2$ has a unique connected covering space corresponding to the trivial subgroup of $\pi_1$ — its *universal cover* — and the number of sheets equals $|\pi_1| = 2$, so the universal cover is a connected **double cover**. For the Lorentz group this double cover carries its own group structure (it is the simply connected Lie group with the same Lie algebra $\mathfrak{so}(1,3) \cong \mathfrak{sl}(2,\mathbb{C})$) and is realised concretely as
> $$SL(2,\mathbb{C}) \xrightarrow{\ 2:1\ } SO^+(1,3),$$
> the covering map being the [[Def - The Spinor Map and SL(2,C)|spinor map]] $A \mapsto \Lambda(A)$ that sends $\pm A$ to the same Lorentz transformation. $SL(2,\mathbb{C})$ is simply connected (its maximal compact subgroup is $SU(2) \cong S^3$, which is simply connected, and the rest is a contractible factor), confirming it is the universal cover.

**Step 4: The spinor sign.**

> [!note]- Derivation
> A **spinor** is an object transforming under a representation of the double cover $SL(2,\mathbb{C})$ that does *not* descend to a representation of $SO^+(1,3)$ — it assigns *two* matrices $\pm A$ to each Lorentz transformation. Track a continuous $2\pi$ rotation $R(\alpha)$, $\alpha : 0 \to 2\pi$, about a fixed axis. In the group $SO^+(1,3)$ this is exactly the non-contractible loop $\gamma$ of Step 2 (start and end at the identity, but not contractibly). Its lift to the cover $SL(2,\mathbb{C})$ is a *path* $\tilde R(\alpha)$ starting at the identity $+\mathbf{1}$; because $\gamma$ is non-contractible, the lift does *not* close up — it ends at the *other* preimage of the identity, $-\mathbf{1}$. Concretely, the spinor rotation is $\exp(\tfrac{i}{2}\alpha\,\mathbf{n}\cdot\boldsymbol\sigma)$, which at $\alpha = 2\pi$ equals $\exp(i\pi\,\mathbf{n}\cdot\boldsymbol\sigma) = -\mathbf{1}$. So a $2\pi$ rotation acts on a spinor as $-\mathbf{1}$: the spinor changes sign. A *second* $2\pi$ rotation (total $4\pi$) is the doubled loop $\gamma^2$, which *is* contractible, so its lift closes up and returns to $+\mathbf{1}$: a $4\pi$ rotation acts as $+\mathbf{1}$, the spinor returns to itself. This $\pm$ is exactly the $\mathbb{Z}/2$ of $\pi_1$, seen now as a representation rather than a loop.

> [!note]- Complete formal solution
> By the polar decomposition $SO^+(1,3) \cong \mathbb{R}^3 \times SO(3)$, and since $\pi_1(\mathbb{R}^3) = \{1\}$, the product formula gives $\pi_1(SO^+(1,3)) = \pi_1(SO(3))$. Now $SO(3) \cong \mathbb{R}\mathbb{P}^3$, the solid ball of radius $\pi$ with antipodal boundary points identified (angle–axis coordinates, with rotation by $\pi$ about $\pm\mathbf{n}$ identified). A diameter from $\pi\mathbf{n}$ through the centre to $-\pi\mathbf{n}$ is a loop (identified endpoints), non-contractible (odd number of boundary crossings, a homotopy invariant); traversed twice it becomes contractible (even crossings, the belt trick). So $\pi_1(SO(3)) = \mathbb{Z}/2$, generated by the diameter loop. A space with $\pi_1 = \mathbb{Z}/2$ has a connected double cover that is its simply connected universal cover; for the Lorentz group this is $SL(2,\mathbb{C})$, the spinor map being the $2{:}1$ covering homomorphism. A spinor, transforming under the cover, picks up the lift of the non-contractible loop: a $2\pi$ rotation lifts to a path from $+\mathbf{1}$ to $-\mathbf{1}$ ($\exp(i\pi\,\mathbf{n}\cdot\boldsymbol\sigma) = -\mathbf{1}$), so it acts as $-1$, while a $4\pi$ rotation (contractible loop) acts as $+1$. $\blacksquare$

---

# Key Takeaways

**The fundamental group of the Lorentz group is the fundamental group of $SO(3)$, because the boosts are contractible.** The single structural move that makes this computation tractable is the polar decomposition: it presents the non-compact six-dimensional Lorentz group as a product of a contractible boost factor $\mathbb{R}^3$ and the compact rotation group $SO(3)$. A contractible factor contributes trivial $\pi_1$, so the entire fundamental group is inherited from the rotations. The reusable principle, transferable to any Lie group with a Cartan decomposition $G \cong \mathbb{R}^d \times K$, is that the topology of $G$ equals the topology of its maximal compact subgroup $K$ — the non-compact "boost" directions are always contractible and topologically inert. So "what is $\pi_1$ of the Lorentz group?" is, after this reduction, the classical question "what is $\pi_1$ of $SO(3)$?", whose answer $\mathbb{Z}/2$ is one of the most famous facts in topology.

**$\pi_1(SO(3)) = \mathbb{Z}/2$ is the belt trick, and the half-integer pattern is everywhere in physics.** The non-contractibility of a single $2\pi$ rotation, and the contractibility of a double $4\pi$ rotation, is the topological content of Dirac's belt trick and the plate trick — physical demonstrations that a $360°$ twist cannot be undone with fixed ends while a $720°$ twist can. The trigger for recognising this $\mathbb{Z}/2$ elsewhere is any configuration space that is $\mathbb{R}\mathbb{P}^3$ or has the rotation group as a factor: the order-parameter space of a spin system, the space of frames of a rigid body, the internal space of a nematic. The reusable diagnostic is to count, for a given loop, the parity of "boundary crossings" in the ball model — even is contractible, odd is not. This single $\mathbb{Z}/2$ is the seed of half-integer angular momentum, the spinor sign, and ultimately (via spin–statistics) the Pauli exclusion principle.

**Topology of the group plus representation of the cover equals the existence of spinors.** The deepest lesson is the interplay between this exercise and the algebra of the chapter: the *group* $SO^+(1,3)$ is not simply connected, so it has a *double cover* $SL(2,\mathbb{C})$, and the representations that live only on the cover — assigning $\pm A$ to each Lorentz transformation — are precisely the spinors. The sign change of a spinor under $2\pi$ rotation is not a mysterious quantum postulate; it is the statement that the lift of the non-contractible $\pi_1$-generating loop to the simply connected cover is an open path joining the two preimages of the identity, which differ by $-1$. The general principle: whenever a symmetry group has non-trivial $\pi_1$, its representations split into those that descend to the group (here, tensors, integer spin) and those faithful only to the cover (here, spinors, half-integer spin), and the dividing line is exactly the kernel $\mathbb{Z}/2$ of the covering map. The topology computed here and the $(j_A,j_B)$ algebra of the [[Thm - The Complexification of so(1,3) and the (A,B) Decomposition|complexification]] are two halves of one statement about why matter comes in bosons and fermions.
