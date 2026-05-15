---
type: exercise
subject: group-theory
difficulty: "⭐"
prereqs:
  - "Def - Group Action"
  - "Def - Orbit and Stabiliser"
  - "Thm - Orbit-Stabiliser Theorem"
tags: [algebra, group-theory]
---

# Problem Statement

Let $G$ be the group of rotational symmetries of a cube — the rigid motions of three-dimensional space that carry the cube onto itself, with reflections excluded. Using the orbit-stabiliser theorem, show that $|G| = 24$.

**Recall:**

The objects in play are a group action, the orbit and stabiliser of a point, and the theorem that ties their sizes together.

![[Def - Group Action#The Definition]]

A [[Def - Group Action|group action]] of $G$ on a set $X$ is the precise sense in which "$G$ is a group of symmetries of $X$": each $g \in G$ permutes $X$, and composing the permutations matches multiplication in $G$. The rotation group of the cube acts on every natural collection of features at once — the $6$ faces, the $8$ vertices, the $12$ edges, the $4$ long diagonals — and we are free to pick whichever is most convenient.

![[Def - Orbit and Stabiliser#The Definition]]

For a point $x \in X$, its [[Def - Orbit and Stabiliser|orbit]] $G \cdot x = \{g \cdot x : g \in G\}$ is the set of all places $x$ can be sent, and its **stabiliser** $G_x = \{g \in G : g \cdot x = x\}$ is the set of group elements that leave $x$ fixed. The stabiliser is always a [[Def - Subgroup|subgroup]] of $G$. An action is **transitive** when the whole set $X$ is a single orbit — every point can be moved to every other.

![[Thm - Orbit-Stabiliser Theorem#Statement]]

The [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] states that for a finite group $G$ acting on $X$, and any $x \in X$,
$$|G| = |G \cdot x| \cdot |G_x|.$$
The size of the orbit times the size of the stabiliser recovers the order of the whole group. This is the tool the problem asks us to use: it lets us compute the unknown $|G|$ as a product of two numbers we can read directly off the geometry of the cube.

---

# Convergent Strategy

**Problem class.** This is a *count the order of a group of symmetries* problem — the first and most concrete problem class identified in the [[Group Theory II — §1.3–1.4#Problem-Solving Strategy|problem-solving strategy]] of the topic page. The group $G$ is presented geometrically and its order is unknown; the task is to make that order computable. The standard route for this entire class is: let $G$ act on a concrete feature of the object, then apply orbit-stabiliser.

**Assumption pattern.** The hypothesis is a *shape with symmetry* — the cube. A shape comes equipped with several finite sets that its symmetry group permutes, and the recognisable move is to choose one of those sets as $X$. The cube hands us the $6$ faces, the $8$ vertices, the $12$ edges, and the $4$ long diagonals. The assumption does its work the moment we name one of these as the set acted on: an abstract symmetry group becomes a permutation group of a small explicit set.

**Theorem routing.** The single theorem that converts the geometry into a number is the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]]. We let $G$ act on the $6$ faces. We then establish two facts geometrically — the action is transitive, so the orbit of any face has size $6$; and the stabiliser of a chosen face is the group of rotations about the axis through that face and its opposite, which has size $4$. Orbit-stabiliser multiplies these to give $|G| = 6 \times 4 = 24$.

**Key decision point.** The non-obvious choice is *which feature to act on*, and the realisation that the answer barely matters — every reasonable choice works, because $|G|$ is fixed and orbit-stabiliser will always reproduce it. Faces give $6 \times 4$; vertices give $8 \times 3$; edges give $12 \times 2$. The genuine content of the problem is not picking the "right" set but understanding *why* each computation is forced: the orbit size is the count of features (the action is transitive), and the stabiliser size is the number of rotations that fix one feature, which one sees by spinning the cube about the relevant axis. The decision point is recognising that "orbit size" and "stabiliser size" each have a transparent geometric meaning, so neither factor requires any group theory to evaluate.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory II — §1.3–1.4#Legal Operations|the topic page's Legal Operations]]:

1. **Let the group act on a cleverly chosen set** (operation 1). The cube's rotation group is abstract until we name a set for it to permute. We choose the $6$ faces. The cross-checks choose the $8$ vertices and the $12$ edges instead — each is a legitimate instance of the same operation, and the freedom of choice is exactly the point.

2. **Apply the orbit-stabiliser theorem** (operation 2). Once $G$ acts on the faces, the identity $|G| = |G \cdot x| \cdot |G_x|$ lets us compute the unknown $|G|$ from the orbit size (the number of faces) and the stabiliser size (the rotations fixing one face). This is the operation that produces the number.

3. **Compute a stabiliser by restricting to a sub-symmetry** (a specialisation of operation 1). The stabiliser of one face is itself a group of symmetries — the rotations about a single fixed axis — and we count it as a smaller, one-dimensional rotation problem. Reducing a stabiliser computation to a simpler symmetry count is the routine sub-move that makes orbit-stabiliser usable.

---

# Hints

<details>
<summary>Hint 1</summary>

You are asked to find the order of a group of symmetries, and you are told to use orbit-stabiliser. So the group must *act* on something. The cube has several natural finite sets attached to it that any rotation permutes. List them, and pick the simplest one.

</details>

<details>
<summary>Hint 2</summary>

Take $X$ to be the set of $6$ faces. Two questions: (a) Can every face be rotated to every other face? (b) Fix one face — how many rotations of the cube leave that face exactly where it is?

</details>

<details>
<summary>Hint 3</summary>

For (a): yes, the action is transitive — there is a rotation carrying any chosen face to any other, so the orbit of a face is all $6$ faces. For (b): the rotations fixing a face are precisely the spins about the axis through that face and the opposite face; there are $4$ of them (by $0°, 90°, 180°, 270°$). Orbit-stabiliser gives $|G| = 6 \times 4$.

</details>

---

# Solution

The plan is to let $G$ act on the $6$ faces of the cube, show the action is transitive so the orbit has size $6$, count the stabiliser of one face as the $4$ rotations about its axis, and multiply by the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]].

**Step 1: $G$ acts on the set of $6$ faces, and the action is transitive — every orbit has size $6$.**

Each rotation of the cube permutes its $6$ faces, so $G$ acts on the set $X$ of faces. Any face can be carried to any other by a suitable rotation, so there is a single orbit: for any face $x$, the orbit $G \cdot x$ is all of $X$ and $|G \cdot x| = 6$.

<details>
<summary>Derivation</summary>

A rotation of the cube is a bijection of three-dimensional space carrying the cube to itself; it sends faces to faces (a face is a flat square piece of the boundary, and rigid motions preserve this), and it does so bijectively. So restricting each $g \in G$ to its effect on faces gives a permutation of the $6$-element set $X$, and composition of rotations corresponds to composition of these permutations. The identity rotation fixes every face. Hence the two [[Def - Group Action|action axioms]] $e \cdot x = x$ and $g_1 \cdot (g_2 \cdot x) = (g_1 g_2) \cdot x$ hold, and $G$ acts on $X$.

The action is **transitive**: given any two faces, there is a rotation of the cube taking the first to the second. Concretely, label the faces top, bottom, front, back, left, right. A quarter-turn about the front-to-back axis cycles top $\to$ right $\to$ bottom $\to$ left $\to$ top, so the four side faces are all reachable from one another; a quarter-turn about a side axis swaps top with front. Composing such moves carries any face to any other. Therefore every face lies in the orbit of every other, the action has exactly one orbit, and for any face $x$,
$$|G \cdot x| = |X| = 6.$$

</details>

**Step 2: The stabiliser of a face is the group of rotations about the axis through it — it has order $4$.**

Fix the top face. A rotation fixes the top face (as a face, mapping it to itself) exactly when it is a spin about the vertical axis through the centres of the top and bottom faces. The spins by $0°, 90°, 180°, 270°$ are the only such rotations, so the stabiliser $G_x$ has order $4$.

<details>
<summary>Derivation</summary>

Let $x$ be the top face and consider $G_x = \{g \in G : g \cdot x = x\}$, the rotations sending the top face to itself. Such a rotation fixes the top face setwise, hence fixes its centre point; being a symmetry of the cube it also fixes the cube's centre. A rotation of space fixing two distinct points fixes the entire line through them — here, the vertical axis through the centres of the top and bottom faces. So every element of $G_x$ is a rotation *about that fixed axis*.

The rotations about a fixed axis that carry the cube to itself are exactly those that carry the square top face to itself, namely the rotations by multiples of $90°$:
$$0°, \quad 90°, \quad 180°, \quad 270°.$$
A rotation by any other angle would move the four edges of the top square to positions not occupied by edges, so it is not a symmetry. These four rotations are distinct and each fixes the top face, so
$$|G_x| = 4.$$
(As a sanity check, $G_x$ is the cyclic group $C_4$ generated by the quarter-turn about this axis, consistent with the general fact that a stabiliser is a [[Def - Subgroup|subgroup]] of $G$.)

</details>

**Step 3: Apply the orbit-stabiliser theorem to conclude $|G| = 24$.**

With $|G \cdot x| = 6$ and $|G_x| = 4$, the orbit-stabiliser theorem gives $|G| = 6 \times 4 = 24$.

<details>
<summary>Derivation</summary>

The [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] states that for a finite group $G$ acting on a set $X$ and any point $x \in X$,
$$|G| = |G \cdot x| \cdot |G_x|.$$
Take $x$ to be the top face. Step 1 gives $|G \cdot x| = 6$ and Step 2 gives $|G_x| = 4$. Therefore
$$|G| = 6 \cdot 4 = 24.$$
The rotation group of the cube has order $24$. $\blacksquare$

</details>

<details>
<summary>Cross-check via the 8 vertices</summary>

Run the identical argument on the set $X'$ of $8$ vertices of the cube. The action is again transitive — any vertex can be rotated to any other — so each orbit has size $|X'| = 8$. Fix one vertex $v$; a rotation fixing $v$ fixes both $v$ and the cube's centre, hence fixes the long diagonal through $v$, and is therefore a spin about that diagonal. The rotations about a long diagonal carrying the cube to itself are the three rotations by $0°, 120°, 240°$ (the diagonal is an axis of $3$-fold symmetry, since three faces meet at each vertex). So the stabiliser has order $3$, and orbit-stabiliser gives
$$|G| = 8 \cdot 3 = 24,$$
agreeing with Step 3. The same exercise on the $12$ edges gives $|G| = 12 \cdot 2 = 24$, since the stabiliser of an edge is the order-$2$ group containing the identity and the $180°$ rotation about the axis through that edge's midpoint and the opposite edge's midpoint.

</details>

<details>
<summary>Remark: the action on the 4 long diagonals gives an isomorphism with $S_4$</summary>

The cube has $4$ long diagonals (each joining a pair of opposite vertices), and every rotation permutes them, giving an action $G \to \operatorname{Sym}(X'') \cong S_4$ on a $4$-element set. This [[Thm - Actions Correspond to Homomorphisms|homomorphism]] is in fact an isomorphism. It is injective: a rotation fixing all four diagonals as lines must fix the cube pointwise or invert every diagonal, and a single rotation cannot invert all four simultaneously while fixing the cube, so only the identity acts trivially — the kernel is trivial. Since $|G| = 24 = |S_4|$, an injective homomorphism between finite groups of equal order is a bijection. Hence the rotation group of the cube is isomorphic to $S_4$. This is a recurring bonus of the action viewpoint: a well-chosen action does not merely *count* the group, it can *identify* it.

</details>

<details>
<summary><strong>Complete formal solution</strong></summary>

Let $G$ be the rotation group of the cube.

Each rotation permutes the $6$ faces, so $G$ acts on the set $X$ of faces. The action is transitive: any face can be carried to any other by a rotation (the four side faces cycle under a quarter-turn about a horizontal axis, and a quarter-turn about a side axis exchanges a side face with the top). Hence for any face $x$ the orbit $G \cdot x$ is all of $X$, so $|G \cdot x| = 6$.

Fix the top face $x$. A rotation in the stabiliser $G_x$ fixes the top face setwise, hence fixes its centre and the cube's centre, hence fixes the vertical axis through both face-centres, so it is a rotation about that axis. The rotations about this axis preserving the cube are exactly those by $0°, 90°, 180°, 270°$, so $G_x$ has order $4$.

By the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]], $|G| = |G \cdot x| \cdot |G_x| = 6 \cdot 4 = 24$.

(Cross-check: acting on the $8$ vertices gives orbit size $8$ and stabiliser size $3$, with $8 \cdot 3 = 24$; acting on the $12$ edges gives $12 \cdot 2 = 24$. Acting on the $4$ long diagonals gives an injective homomorphism $G \to S_4$, which is an isomorphism by equality of orders.) $\blacksquare$

</details>

---

# Key Takeaways

**To count a group of symmetries, make it act on the most concrete features of the object and apply orbit-stabiliser.** This exercise is the template for an entire problem class: a symmetry group is presented geometrically, its order is unknown, and the route to the order is always the same. Find a finite set the group visibly permutes — the faces, vertices, edges, or diagonals of a polyhedron; the cells of a pattern; the slots of a configuration — and apply the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] $|G| = |G \cdot x| \cdot |G_x|$. The trigger is the phrase "how many symmetries" together with a concrete object. The reason it works is that orbit-stabiliser splits the unknown order into two factors that are each *directly observable*: the orbit size is a count of features, and the stabiliser size is a smaller, more tractable symmetry count. The same method computes the order of the symmetry group of a tetrahedron ($12$), an octahedron ($24$, since the octahedron is the cube's dual), an icosahedron ($60$), or a regular polygon under the dihedral group — in every case by acting on the obvious features.

**The orbit size is the number of features when the action is transitive; verify transitivity rather than assume it.** The computation $|G \cdot x| = 6$ rests on the action on faces being transitive — every face reachable from every other. Whenever an object "looks the same from every face" (or vertex, or edge), transitivity holds and the orbit of a single feature is the entire set of features of that type, so the orbit factor is just a count. But transitivity is a genuine hypothesis: if the chosen features fall into geometrically distinct types — say, the faces of a non-cubical box, where the two square ends differ from the four oblong sides — the action has several orbits and orbit-stabiliser applies to each orbit separately. The discipline is to *check* that any feature can be moved to any other before declaring the orbit size equal to the total count. When it cannot, partition the features into orbits first.

**A stabiliser is itself a symmetry group, and computing it is a smaller copy of the original problem.** The step $|G_x| = 4$ was solved not by group theory but by a geometric observation: a rotation fixing a face must fix the axis through that face, so the stabiliser is the group of rotations about a single axis, which one counts by inspection. This recursion — "the stabiliser of a feature is the symmetry group of the object with that feature pinned down" — is what makes orbit-stabiliser tractable in practice. The pinned-down object is always simpler: fixing a face leaves a one-axis rotation problem; fixing a vertex of the cube leaves a $3$-fold axis; fixing an edge leaves a $2$-fold axis. Recognising the stabiliser as a reduced symmetry-counting problem, rather than something to compute element by element, is the move that turns orbit-stabiliser from a formula into a method.

**The choice of set is free, and cross-checking with a second choice both verifies the answer and can reveal more structure.** Because $|G|$ is a fixed number, *every* valid action of $G$ must reproduce it through orbit-stabiliser — faces give $6 \times 4$, vertices give $8 \times 3$, edges give $12 \times 2$, all equal to $24$. This gives a free internal consistency check: compute the order two different ways and confirm they agree. More than that, different sets expose different facts. Acting on the $4$ long diagonals does not just count $G$; because the resulting homomorphism $G \to S_4$ is injective and the orders match, it *identifies* $G$ as $S_4$. The general lesson is that the set you act on is a modelling choice with consequences: a small faithful set turns a counting problem into an identification, so when a group acts on a set barely larger than needed to be faithful, suspect an isomorphism and check the kernel.
