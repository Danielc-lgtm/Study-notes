---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Subgroups and Components of the Lorentz Group"
  - "Thm - The Restricted Lorentz Group is a Normal Subgroup"
tags: [physics, special-relativity]
---

# Problem Statement

Let $I = -\mathrm{Id}$, $P = \mathrm{diag}(1,-1,-1,-1)$, $T = \mathrm{diag}(-1,1,1,1)$ be the discrete reflections of the Lorentz group.

1. Show that $G = \{\mathrm{Id}, I, P, T\}$ is closed under composition, with the relations $P^2 = T^2 = I^2 = \mathrm{Id}$, $PT = TP = I$, $PI = IP = T$, $TI = IT = P$.
2. Conclude that $G$ is a group, that every nonidentity element has order two, and hence that $G \cong \mathbb{Z}/2 \times \mathbb{Z}/2$ (the Klein four-group), not $\mathbb{Z}/4$.
3. Show that $G$ is a *section* of the quotient $O(1,3) \to O(1,3)/SO^+(1,3)$ — that the composite $G \hookrightarrow O(1,3) \to O(1,3)/SO^+(1,3)$ is an isomorphism — so that $O(1,3)/SO^+(1,3) \cong \mathbb{Z}/2\times\mathbb{Z}/2$ and $O(1,3) = SO^+(1,3) \rtimes G$.

**Recall:**

![[Thm - The Restricted Lorentz Group is a Normal Subgroup#Statement]]

The Klein four-group $\mathbb{Z}/2\times\mathbb{Z}/2 = \{(0,0), (1,0), (0,1), (1,1)\}$ is the unique group of order four in which every nonidentity element is an involution; the only other group of order four is the cyclic $\mathbb{Z}/4$, which has elements of order four. A *section* of a quotient map $q : G' \to Q$ is a subgroup $S \le G'$ such that $q|_S : S \to Q$ is an isomorphism.

---

# Convergent Strategy

**Problem class.** A *structure-identification* problem from the [[Special Relativity IX — The Lorentz Group, Structure and Classification#Problem-Solving Strategy|topic strategy]]: identify an abstract group from its multiplication table, and locate it inside a larger group as a section of a quotient. The work is the multiplication table (a few diagonal-matrix products) and the order-counting that distinguishes the two groups of order four.

**Assumption pattern.** The four matrices are diagonal, so their products are computed entrywise — trivial. The key data are that each is an involution ($I^2 = P^2 = T^2 = \mathrm{Id}$) and that the product of any two distinct nonidentity ones is the third ($PT = I$, etc.). These two facts force the Klein four-group: a group of order four with three involutions cannot be cyclic.

**Theorem routing.** Part 3 routes through the [[Thm - The Restricted Lorentz Group is a Normal Subgroup|normal-subgroup theorem]]: the sign map $\sigma : O(1,3) \to \mathbb{Z}/2\times\mathbb{Z}/2$ has kernel $SO^+(1,3)$, and restricting $\sigma$ to $G$ is a bijection onto $\mathbb{Z}/2\times\mathbb{Z}/2$ (each reflection hits a distinct class), so $G$ is a section and the quotient is $\mathbb{Z}/2\times\mathbb{Z}/2$. Normality of $SO^+(1,3)$ then gives the semidirect product.

**Key decision point.** The non-obvious point is distinguishing $\mathbb{Z}/2\times\mathbb{Z}/2$ from $\mathbb{Z}/4$: both have order four, but the Klein four-group has *three* elements of order two while $\mathbb{Z}/4$ has *one*. The deciding computation is $P^2 = T^2 = I^2 = \mathrm{Id}$ — all three nonidentity elements square to the identity — which is impossible in $\mathbb{Z}/4$. The natural-but-wrong assumption is that "the group of four reflections" is cyclic; it is not, and the order-two-ness of every reflection is the proof.

---

# Legal Operations Used

1. **Reduce to a restricted transformation by a reflection** (operation 2 from the topic page): the reflections $I, P, T$ are the coset representatives, and this exercise establishes their group structure as the quotient $O(1,3)/SO^+(1,3)$.

---

# Hints

> [!note]- Hint 1
> The matrices are diagonal; multiply them entrywise. For instance $PT = \mathrm{diag}(1,-1,-1,-1)\cdot\mathrm{diag}(-1,1,1,1) = \mathrm{diag}(-1,-1,-1,-1) = I$.

> [!note]- Hint 2
> A group of order four is either $\mathbb{Z}/4$ (one element of order four, one of order two) or $\mathbb{Z}/2\times\mathbb{Z}/2$ (three elements of order two). Count the orders of $I, P, T$.

> [!note]- Hint 3
> For the section: the sign map $\sigma(\Lambda) = (\tfrac{1-\det\Lambda}{2}, \tfrac{1-\mathrm{sgn}\Lambda^0{}_0}{2})$ sends $\mathrm{Id}, P, T, I$ to $(0,0), (1,0), (0,1), (1,1)$ — a bijection onto $\mathbb{Z}/2\times\mathbb{Z}/2$. Since $\ker\sigma = SO^+(1,3)$, $\sigma|_G$ is the quotient map restricted to $G$.

---

# Solution

The solution computes the multiplication table (Step 1), distinguishes the Klein four-group from $\mathbb{Z}/4$ by order-counting (Step 2), and identifies $G$ with the quotient via the sign map (Step 3).

**Step 1: The multiplication table.**

> [!note]- Derivation
> All four matrices are diagonal, so products are entrywise. Compute:
> $$P^2 = \mathrm{diag}(1,-1,-1,-1)^2 = \mathrm{diag}(1,1,1,1) = \mathrm{Id},$$
> $$T^2 = \mathrm{diag}(-1,1,1,1)^2 = \mathrm{Id}, \qquad I^2 = \mathrm{diag}(-1,-1,-1,-1)^2 = \mathrm{Id}.$$
> $$PT = \mathrm{diag}(1,-1,-1,-1)\,\mathrm{diag}(-1,1,1,1) = \mathrm{diag}(-1,-1,-1,-1) = I = TP.$$
> $$PI = \mathrm{diag}(1,-1,-1,-1)\,\mathrm{diag}(-1,-1,-1,-1) = \mathrm{diag}(-1,1,1,1) = T = IP.$$
> $$TI = \mathrm{diag}(-1,1,1,1)\,\mathrm{diag}(-1,-1,-1,-1) = \mathrm{diag}(1,-1,-1,-1) = P = IT.$$
> Every product of elements of $G$ is again in $G$, so $G$ is closed; the products are commutative; and the relations $P^2 = T^2 = I^2 = \mathrm{Id}$, $PT = I$, $PI = T$, $TI = P$ hold.

**Step 2: $G$ is the Klein four-group.**

> [!note]- Derivation
> $G$ is closed (Step 1), contains $\mathrm{Id}$, and each element is its own inverse ($P^2 = T^2 = I^2 = \mathrm{Id}$, $\mathrm{Id}^2 = \mathrm{Id}$), so $G$ is a group of order four. The three nonidentity elements $I, P, T$ all have order two. A group of order four is either cyclic $\mathbb{Z}/4$ — which has a *unique* element of order two (and two of order four) — or the Klein four-group $\mathbb{Z}/2\times\mathbb{Z}/2$, which has *three* elements of order two. Since $G$ has three elements of order two, $G \cong \mathbb{Z}/2\times\mathbb{Z}/2$. Explicitly, $P \leftrightarrow (1,0)$, $T \leftrightarrow (0,1)$, $I = PT \leftrightarrow (1,1)$, $\mathrm{Id} \leftrightarrow (0,0)$ is an isomorphism (the relation $PT = I$ matches $(1,0)+(0,1) = (1,1)$).

**Step 3: $G$ is a section, and the quotient is Klein.**

> [!note]- Derivation
> The sign map $\sigma : O(1,3) \to \mathbb{Z}/2\times\mathbb{Z}/2$, $\sigma(\Lambda) = (\tfrac{1-\det\Lambda}{2}, \tfrac{1-\mathrm{sgn}\Lambda^0{}_0}{2})$, is a homomorphism with kernel $SO^+(1,3)$ (the [[Thm - The Restricted Lorentz Group is a Normal Subgroup|normal-subgroup theorem]]). On $G$:
> $$\sigma(\mathrm{Id}) = (0,0), \quad \sigma(P) = (1,0), \quad \sigma(T) = (0,1), \quad \sigma(I) = (1,1),$$
> using $\det P = -1, P^0{}_0 = 1$; $\det T = -1, T^0{}_0 = -1$; $\det I = (-1)^4 = 1, I^0{}_0 = -1$. So $\sigma|_G : G \to \mathbb{Z}/2\times\mathbb{Z}/2$ is a bijection, hence (being a homomorphism) an isomorphism. Since $\sigma$ is the quotient map $O(1,3) \to O(1,3)/SO^+(1,3) \cong \mathbb{Z}/2\times\mathbb{Z}/2$ composed with the identification, $G$ is a section: $G \cap SO^+(1,3) = \{\mathrm{Id}\}$ (since $\sigma|_G$ is injective) and $\sigma|_G$ is onto. By the splitting and normality of $SO^+(1,3)$, $O(1,3) = SO^+(1,3) \rtimes G$. $\blacksquare$

> [!note]- Complete formal solution
> The diagonal matrices $\mathrm{Id}, I, P, T$ multiply entrywise: $P^2 = T^2 = I^2 = \mathrm{Id}$ and $PT = TP = I$, $PI = IP = T$, $TI = IT = P$, so $G = \{\mathrm{Id}, I, P, T\}$ is a closed, abelian set in which every element is its own inverse — a group of order four. All three nonidentity elements have order two, which excludes $\mathbb{Z}/4$ (one element of order two), so $G \cong \mathbb{Z}/2\times\mathbb{Z}/2$. The sign map $\sigma$ sends $\mathrm{Id}, P, T, I$ to $(0,0), (1,0), (0,1), (1,1)$, a bijection onto $\mathbb{Z}/2\times\mathbb{Z}/2$, so $\sigma|_G$ is an isomorphism; as $\ker\sigma = SO^+(1,3)$, $G$ is a section of the quotient and $O(1,3)/SO^+(1,3) \cong \mathbb{Z}/2\times\mathbb{Z}/2$, with $O(1,3) = SO^+(1,3)\rtimes G$. $\blacksquare$

---

# Key Takeaways

**Three involutions in a group of order four force the Klein four-group.** The single computation that settles the structure is that $I, P, T$ all square to the identity: a group of order four with three elements of order two is $\mathbb{Z}/2\times\mathbb{Z}/2$, never $\mathbb{Z}/4$ (which has only one element of order two). This is the fastest way to recognise the Klein four-group in any context — count the involutions. The reflections of the Lorentz group are Klein because there are two independent things to reflect (time and space), and reflecting each is an involution; the product of the two reflections is the total inversion $I = PT$, the third involution. The trigger "a group of order four, several elements squaring to the identity" should immediately suggest $\mathbb{Z}/2\times\mathbb{Z}/2$.

**A section turns a quotient into a semidirect product.** Finding a subgroup $G$ that maps isomorphically onto the quotient $O(1,3)/SO^+(1,3)$ — a section — is exactly what is needed to write $O(1,3) = SO^+(1,3)\rtimes G$. The reflections $\{\mathrm{Id}, I, P, T\}$ form such a section, sitting inside $O(1,3)$ as a complement to the normal restricted subgroup. The general lesson: whenever a normal subgroup $N \trianglelefteq G'$ has a complementary subgroup $S$ (intersecting $N$ trivially and surjecting onto the quotient), the group is the semidirect product $N\rtimes S$, reconstructed from the normal part and the complement. Here the discrete symmetries $P, T$ are the complement, which is why every Lorentz transformation factors uniquely as a restricted transformation times a reflection — the content of the reduction exercise.

**The two reflections $P$ and $T$ are independent generators, and their product is the total inversion.** It is worth internalising that parity and time-reversal are not redundant: $P$ reflects space, $T$ reflects time, and neither can be obtained from the other within $SO^+(1,3)$ (they live in different components). Their product $PT = I = -\mathrm{Id}$ is the simultaneous reflection of all four coordinates, the total spacetime inversion. This is the group-theoretic content of the physical fact that parity violation and time-reversal violation are *independent* questions in particle physics — a theory can respect one and violate the other — because $P$ and $T$ generate independent $\mathbb{Z}/2$ factors of the Klein four-group. The structure $\mathbb{Z}/2\times\mathbb{Z}/2$ is the precise statement that there are two independent discrete symmetries, and the diagonal $CPT$ (combining charge conjugation with $PT$) is the one always unbroken.
