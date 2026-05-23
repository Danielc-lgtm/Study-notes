---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Direct Sum"
  - "Def - Basis"
  - "Def - Dimension"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V_1, \dots, V_m$ are vector spaces over the same field $\mathbb{F}$. The Cartesian product is $V_1 \times \cdots \times V_m$. Elements are tuples $(v_1, \dots, v_m)$ with $v_k \in V_k$. The full symbol registry is on [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

**Convention.** All vector spaces in any single product must be over the *same* field $\mathbb{F}$. Forming the "product" of a real vector space with a complex vector space is not defined — there is no single scalar action to put on the tuples.

---

# Axiom Motivation

The desideratum behind the product construction is the simplest one possible: take two vector spaces and put them next to each other, somehow producing a new vector space whose elements are pairs from the original two. The question is *which structure* to give the pairs.

The first axiom — that elements are tuples $(v_1, \dots, v_m)$ with $v_k \in V_k$ — is a labelling choice but a meaningful one. We are not identifying $\mathbb{F}^2 \times \mathbb{F}^3$ with $\mathbb{F}^5$ (the elements have different shapes: a pair-of-tuples versus a single tuple); we are keeping the components separately addressable. If we dropped this and identified, we would lose the natural projection maps $\pi_k : V_1 \times \cdots \times V_m \to V_k$, which are exactly what makes the product useful for building maps out of compound objects.

The second axiom — addition componentwise — is forced. If $(u_1, \dots, u_m) + (v_1, \dots, v_m)$ is to make the product a vector space, the result must again be a tuple, and the only operation we can perform on tuples using just the operations available is componentwise addition. What if we mixed components — say setting the first slot to $u_1 + v_2$? Then projection $\pi_1$ would fail to be linear: $\pi_1((u_1, u_2) + (v_1, v_2))$ would not equal $\pi_1(u_1, u_2) + \pi_1(v_1, v_2)$, so we would lose linearity of $\pi_1$. The componentwise definition is the *only* one consistent with making every projection linear.

The third axiom — scalar multiplication componentwise — is forced for the same reason. The only way to scale a tuple using the available operations is to scale each component; any other definition breaks linearity of projections.

What if we *strengthened* the axioms, say demanding that addition couple the components ($(u_1, u_2) + (v_1, v_2) = (u_1 + v_1 + u_2 + v_2, u_2 + v_2)$)? Then the result is again a vector space (one can check), but it is no longer the *product* — for instance, $\dim$ is preserved but the projection $\pi_1$ is no longer linear, breaking the universal property below. A weaker axiom — say allowing scalar multiplication to act only on the first slot — produces something that is not even a vector space.

The deeper motivation comes from a theorem the construction is built to enable. We want every list of linear maps $S_k : W \to V_k$, $k = 1, \dots, m$, to assemble into a single map $S : W \to V_1 \times \cdots \times V_m$ via $S(w) = (S_1(w), \dots, S_m(w))$ — and we want this $S$ to be linear, and to be the *unique* map whose projections give back the $S_k$. The componentwise definition is exactly what makes this work: linearity of $S$ reduces to linearity of each $S_k$ slot by slot, and the projections recover the $S_k$ by construction. This is the *universal property of the product* (see Categorical Definition below), and the axioms have been reverse-engineered from it.

---

# The Definition

Let $V_1, \dots, V_m$ be vector spaces over a field $\mathbb{F}$. The **product** $V_1 \times \cdots \times V_m$ is the set of tuples
$$V_1 \times \cdots \times V_m = \{(v_1, \dots, v_m) : v_k \in V_k \text{ for each } k\},$$
equipped with the operations
$$(u_1, \dots, u_m) + (v_1, \dots, v_m) := (u_1 + v_1, \dots, u_m + v_m),$$
$$\lambda \cdot (v_1, \dots, v_m) := (\lambda v_1, \dots, \lambda v_m).$$
With these operations $V_1 \times \cdots \times V_m$ is a vector space over $\mathbb{F}$:
- the **additive identity** is $(0_{V_1}, \dots, 0_{V_m})$;
- the **additive inverse** of $(v_1, \dots, v_m)$ is $(-v_1, \dots, -v_m)$;
- the vector-space axioms are verified slot by slot from those of each $V_k$.

The natural maps to and from the product are:
- the **projections** $\pi_k : V_1 \times \cdots \times V_m \to V_k$, $\pi_k(v_1, \dots, v_m) = v_k$, which are linear and surjective;
- the **inclusions** $\iota_k : V_k \to V_1 \times \cdots \times V_m$, $\iota_k(v) = (0, \dots, v, \dots, 0)$ with $v$ in the $k$-th slot, which are linear and injective.

When $V_1, \dots, V_m$ are *[[Def - Subspace|subspaces]]* of a common ambient $V$, there is also a natural linear map
$$\Gamma : V_1 \times \cdots \times V_m \to V_1 + \cdots + V_m, \qquad \Gamma(v_1, \dots, v_m) = v_1 + \cdots + v_m,$$
which is always surjective, and is an isomorphism if and only if $V_1 + \cdots + V_m$ is a [[Def - Direct Sum|direct sum]].

---

# Categorical Definition

The product is characterised — pinned down uniquely, up to canonical isomorphism — by a **universal property**, and stating it pays off because the same shape of definition produces products in every category.

A *universal property* describes an object by the maps into or out of it. For the product, the maps in matter. The universal property of $V_1 \times \cdots \times V_m$ is:

> $V_1 \times \cdots \times V_m$ is the universal target of "$m$ linear maps in" from a common source. Precisely: given any vector space $W$ and any list of linear maps $S_k : W \to V_k$ for $k = 1, \dots, m$, there exists a *unique* linear map $S : W \to V_1 \times \cdots \times V_m$ such that $\pi_k \circ S = S_k$ for every $k$, where $\pi_k$ is the $k$-th projection.

In a diagram:

$$\begin{array}{ccc} W & \xrightarrow{\;S_k\;} & V_k \\ {}_{\exists ! S}\!\searrow & {}_{\pi_k}\!\nearrow & \\ V_1 \times \cdots \times V_m & & \end{array}$$

The map $S$ is forced: it must be $S(w) = (S_1(w), \dots, S_m(w))$, and this is the only choice consistent with $\pi_k \circ S = S_k$. The content of the property is that the product is the *cleanest* vector space through which all $m$-tuples of maps factor.

In the language of category theory, this says the product is the **categorical product** (also called direct product) in the category of vector spaces over $\mathbb{F}$. The same universal property defines the product of any objects in any category — products of sets, products of [[Def - Group|groups]], products of topological spaces.

A subtle but important fact: in the category of vector spaces, the **categorical coproduct** coincides with the categorical product (for finite collections). The coproduct $V_1 \sqcup \cdots \sqcup V_m$ would be defined by the *dual* universal property — universal source of "$m$ linear maps out" via inclusions $\iota_k : V_k \hookrightarrow V_1 \sqcup \cdots \sqcup V_m$ — and one checks that $V_1 \times \cdots \times V_m$ also satisfies this universal property, with the inclusions $\iota_k(v) = (0, \dots, v, \dots, 0)$. This coincidence makes the category of vector spaces an **additive category** and is what makes "the [[Def - Direct Sum|direct sum]] $\oplus$" and "the product $\times$" interchangeable for finitely many vector spaces. In categories where they differ — sets, topological spaces, [[Def - Group|groups]] in general — the distinction matters.

---

# Relate to Other Fields / Compression

The product of vector spaces is one instance of the *categorical product*. The product of sets, $A \times B$ (Cartesian product), is the same thing in the category of sets — its universal property is "$f : C \to A$ and $g : C \to B$ assemble uniquely into $(f, g) : C \to A \times B$". The product of groups $G \times H$ is the same in the category of groups, with componentwise multiplication. The product of topological spaces $X \times Y$ is the same in topological spaces, with the product topology (the coarsest making both projections continuous). In each setting, the universal property is identical; only the category changes.

**True name:** the product is "the universal home for $m$-tuples of compatible maps in" — the place where a list of maps with a common source naturally lives.

What is special about *vector spaces*, distinguishing them from sets or topological spaces, is the coincidence of product and coproduct: the same object answers both universal properties. In the category of sets, the coproduct is the *disjoint union*, very different from the product. In the category of vector spaces, the disjoint union does not have a natural vector space structure, and instead the product takes over: $V \oplus W$ serves both as "all pairs $(v, w)$" (the product) and as "all linear combinations $v + w$" (the coproduct, via the inclusions). This phenomenon, called *biproduct*, is what makes additive and abelian categories well-behaved.

---

# Examples / Corollaries

**Is an instance — $\mathbb{F}^n$ as $\mathbb{F} \times \cdots \times \mathbb{F}$.** The coordinate vector space $\mathbb{F}^n$ is the $n$-fold product of the field $\mathbb{F}$ with itself. Addition is componentwise, scalar multiplication is componentwise, the projections are coordinate projections $\pi_k(x_1, \dots, x_n) = x_k$, and $\dim \mathbb{F}^n = n$ by the [[Def - Dimension|dimension]] theorem below. This is the *first* example one should hold in mind when meeting the product definition: $\mathbb{F}^n$ has been the product all along.

**Is an instance — $\mathcal{P}_5(\mathbb{R}) \times \mathbb{R}^3$.** Elements are pairs (polynomial of degree $\leq 5$, real triple), and operations are pairwise. $\dim (\mathcal{P}_5(\mathbb{R}) \times \mathbb{R}^3) = \dim \mathcal{P}_5(\mathbb{R}) + \dim \mathbb{R}^3 = 6 + 3 = 9$. A basis is the union of: each monomial $(1, (0,0,0)), (x, (0,0,0)), \dots, (x^5, (0,0,0))$ with zeros in the $\mathbb{R}^3$ slot, together with $(0, e_1), (0, e_2), (0, e_3)$ for the standard basis of $\mathbb{R}^3$ paired with zero polynomial.

**Is an instance — $\mathbb{R}^2 \times \mathbb{R}^3$ versus $\mathbb{R}^5$.** Elements of $\mathbb{R}^2 \times \mathbb{R}^3$ are pairs $((x_1, x_2), (x_3, x_4, x_5))$ — lists of length two, the first item itself a list of length two and the second a list of length three. Elements of $\mathbb{R}^5$ are flat lists of length five. The two spaces are not literally equal — the elements have different shapes — but the obvious bijection $((x_1, x_2), (x_3, x_4, x_5)) \mapsto (x_1, x_2, x_3, x_4, x_5)$ is a linear isomorphism. So they are *isomorphic* but not *equal*. The distinction matters in proofs: when you say "consider an element of $\mathbb{R}^2 \times \mathbb{R}^3$", you commit to a specific shape, and the projection maps are different from those on $\mathbb{R}^5$.

**Is NOT an instance — gluing vector spaces over different fields.** The "product" of $\mathbb{R}^2$ as a real vector space with $\mathbb{C}^2$ as a complex vector space is *not* defined as a vector space in the sense above. There is no single field whose scalars act on both slots. One can construct a real vector space $\mathbb{R}^2 \times (\mathbb{C}^2 \text{ as a real space of dimension } 4)$ of real [[Def - Dimension|dimension]] $6$, but this requires *forgetting* the complex structure on $\mathbb{C}^2$ first.

**Corollary — every linear map out of a product factors slot-by-slot.** If $T : V_1 \times \cdots \times V_m \to W$ is linear, then setting $T_k(v) = T(\iota_k(v)) = T(0, \dots, v, \dots, 0)$ defines linear maps $T_k : V_k \to W$, and $T(v_1, \dots, v_m) = T_1(v_1) + \cdots + T_m(v_m)$. This is the dual perspective on the product, exhibiting it also as a coproduct.

**Corollary — products commute with direct sums.** When $V_1, \dots, V_m$ are [[Def - Subspace|subspaces]] of $V$, the sum $V_1 + \cdots + V_m \subseteq V$ is a direct sum if and only if the natural map $\Gamma : V_1 \times \cdots \times V_m \to V_1 + \cdots + V_m$ is injective; in that case it is an isomorphism. So the *external* product and the *internal* direct sum coincide whenever they make sense.

**Calibration check.** Verify that the projection $\pi_k$ is linear and surjective: $\pi_k((u_1, \dots, u_m) + (v_1, \dots, v_m)) = u_k + v_k = \pi_k(u_1, \dots, u_m) + \pi_k(v_1, \dots, v_m)$, and given any $v_k \in V_k$, $\pi_k(\iota_k(v_k)) = v_k$. Verify that $V_1 \times V_2$ has dimension $\dim V_1 + \dim V_2$ when both are finite-dimensional, by exhibiting an explicit basis: $\{(b_i, 0) : b_i \in \text{basis of } V_1\} \cup \{(0, c_j) : c_j \in \text{basis of } V_2\}$. Confirm that this list is linearly independent and spans.

---

# Unlocked by This

> [!tip] Direct Sum Decompositions *(from this topic)*
> When $V_1, \dots, V_m$ are subspaces of $V$, the product $V_1 \times \cdots \times V_m$ is the "external" version of the [[Def - Direct Sum|direct sum]] $V_1 \oplus \cdots \oplus V_m \subseteq V$. They are isomorphic via $\Gamma$ exactly when the internal sum is direct. So the product gives you a way to build a direct sum from outside even before checking the internal condition.

> [!tip] Tensor Product *(from Linear Algebra IX)*
> The product $V \times W$ is **not** the tensor product $V \otimes W$. The product satisfies a universal property for *linear* maps from $W$ into $V \times W$ via inclusions, but the **tensor product** $V \otimes W$ satisfies a universal property for *bilinear* maps. Their dimensions are radically different: $\dim(V \times W) = \dim V + \dim W$, but $\dim(V \otimes W) = (\dim V)(\dim W)$. Tensor products are the right home for things linear in two arguments at once, and they will be introduced in [[Linear Algebra IX — §9 Multilinear Algebra and Determinants|Chapter 9]].

> [!tip] Module Direct Products *(from Module Theory)*
> Products of modules over a ring are defined identically — componentwise operations on tuples. The construction is fully functorial and the universal property is the same. Where modules differ from vector spaces is that not every short exact sequence splits; in particular, the inclusion $M_k \hookrightarrow M_1 \times \cdots \times M_m$ does not always have a retraction. But the product itself is unchanged.
