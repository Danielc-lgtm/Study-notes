---
type: exercise
subject: group-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Homomorphism"
  - "Def - Kernel and Image"
  - "Def - Normal Subgroup"
  - "Def - Quotient Group"
  - "Thm - First Isomorphism Theorem"
tags: [algebra, group-theory]
---

# Problem Statement

Let $\mathbb{F}$ be a field and let $n \geq 1$. Write $\mathrm{GL}_n(\mathbb{F})$ for the [[Def - Group|group]] of invertible $n \times n$ matrices over $\mathbb{F}$ under multiplication, and $\mathrm{SL}_n(\mathbb{F})$ for the [[Def - Subgroup|subgroup]] of matrices of determinant $1$. Write $\mathbb{F}^\times = \mathbb{F} \setminus \{0\}$ for the group of nonzero elements of $\mathbb{F}$ under multiplication.

Prove that $\mathrm{SL}_n(\mathbb{F})$ is a normal [[Def - Subgroup|subgroup]] of $\mathrm{GL}_n(\mathbb{F})$ and that
$$\mathrm{GL}_n(\mathbb{F}) \big/ \mathrm{SL}_n(\mathbb{F}) \;\cong\; \mathbb{F}^\times.$$

**Recall:**

The problem mentions a quotient, so the objects to have in mind are [[Def - Homomorphism|homomorphisms]], their kernels and images, normality, and the quotient group.

![[Def - Homomorphism#The Definition]]

![[Def - Kernel and Image#The Definition]]

The two facts about kernels and images used below are that $\ker\varphi$ is always a [[Def - Normal Subgroup|normal subgroup]] of $G$, and that $\varphi$ is surjective exactly when $\operatorname{im}\varphi$ is the whole codomain.

A [[Def - Quotient Group|quotient group]] $G/N$, defined when $N \trianglelefteq G$, is the group whose elements are the [[Def - Coset|cosets]] $gN$, with multiplication $(g_1 N)(g_2 N) = g_1 g_2 N$. It is the group "$G$ with the distinctions $N$ erases collapsed away".

![[Thm - First Isomorphism Theorem#Statement]]

The two standard [[Def - Group|groups]] in the problem: $\mathrm{GL}_n(\mathbb{F})$ is a group because the product of invertible matrices is invertible and the identity matrix is invertible; $\mathbb{F}^\times$ is a group because in a field every nonzero element has a multiplicative inverse and the product of nonzero elements is nonzero (a field has no zero divisors).

---

# Convergent Strategy

**Problem class.** This is the central problem class of the chapter: *identify a quotient*. You are handed an abstract quotient group $\mathrm{GL}_n(\mathbb{F})/\mathrm{SL}_n(\mathbb{F})$ — a group whose elements are [[Def - Coset|cosets]] of matrices, which is hard to picture directly — and asked to recognise it as a familiar group, here the multiplicative group of the field. As the [[Group Theory I — §1.1–1.2#Problem-Solving Strategy|topic page strategy]] states, you never analyse such a quotient head-on; you route around it.

**Assumption pattern.** The recognisable signal is that the normal subgroup being quotiented out, $\mathrm{SL}_n(\mathbb{F})$, is *defined as a level set*: it is exactly the matrices whose determinant equals $1$. Whenever the subgroup you must quotient by is "the elements on which some natural quantity takes its trivial value", that quantity is secretly a homomorphism and the subgroup is secretly its kernel. The determinant is multiplicative, $\det(AB) = \det(A)\det(B)$ — that is precisely the homomorphism property — and $\mathrm{SL}_n(\mathbb{F})$ is the set where it equals the identity $1$ of $\mathbb{F}^\times$.

**Theorem routing.** The route is the [[Thm - First Isomorphism Theorem|first isomorphism theorem]], which converts a surjective homomorphism into an isomorphism of quotients: a surjection $\varphi : G \to Q$ with $\ker\varphi = N$ yields $G/N \cong Q$. The plan has exactly three checks. Take $\varphi = \det : \mathrm{GL}_n(\mathbb{F}) \to \mathbb{F}^\times$. (i) Verify $\det$ is a homomorphism. (ii) Verify $\det$ is surjective onto $\mathbb{F}^\times$. (iii) Verify $\ker(\det) = \mathrm{SL}_n(\mathbb{F})$. The theorem then delivers both conclusions at once — normality of $\mathrm{SL}_n(\mathbb{F})$ comes free because kernels are always normal, and the isomorphism is exactly the statement asked for.

**Key decision point.** The non-obvious move is *the guess*: deciding that the target group is $\mathbb{F}^\times$ and the homomorphism is $\det$. The first isomorphism theorem is mechanical once the map is chosen; all the creativity is concentrated in choosing it. The guidance is to look for a property of matrices that is "blind to $\mathrm{SL}_n$" — a quantity that two matrices share exactly when they differ by a determinant-$1$ matrix. Two matrices $A, B$ have $\det A = \det B$ precisely when $\det(AB^{-1}) = 1$, i.e. precisely when $AB^{-1} \in \mathrm{SL}_n(\mathbb{F})$. So the determinant is *exactly* the feature invisible to $\mathrm{SL}_n$, which is why it is the right homomorphism and $\mathbb{F}^\times$ is the right target.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory I — §1.1–1.2#Legal Operations|the topic page's Legal Operations]]:

1. **Build a homomorphism to expose structure** (operation 3). The whole solution turns on producing the determinant homomorphism $\det : \mathrm{GL}_n(\mathbb{F}) \to \mathbb{F}^\times$. The determinant is one of the standard stock [[Def - Homomorphism|homomorphisms]] the topic page explicitly recommends keeping on hand.

2. **Apply the first isomorphism theorem to identify a quotient** (operation 4). Once the surjection is in place with the correct kernel, this operation reads off $\mathrm{GL}_n(\mathbb{F})/\mathrm{SL}_n(\mathbb{F}) \cong \mathbb{F}^\times$ directly.

3. **Conjugate to test or exploit normality** (operation 6), in packaged form. We never conjugate a matrix by hand; instead we use the structural fact from [[Def - Kernel and Image]] that *every* kernel is automatically normal, which is the conjugation argument done once and for all.

---

# Hints

> [!note]- Hint 1
> Do not try to multiply cosets of matrices. To identify a quotient $G/N$ you build a homomorphism *out of* $G$. Which familiar quantity assigned to a matrix is multiplicative — that is, turns matrix products into products of numbers?

> [!note]- Hint 2
> The determinant satisfies $\det(AB) = \det(A)\det(B)$. Over a field $\mathbb{F}$ this makes $\det$ a homomorphism from $\mathrm{GL}_n(\mathbb{F})$ to some group of nonzero field elements. Which group, and why is the value never $0$?

> [!note]- Hint 3
> You now have a homomorphism $\det : \mathrm{GL}_n(\mathbb{F}) \to \mathbb{F}^\times$. Check it is *onto* (scale a single diagonal entry) and identify its *kernel* (the matrices sent to $1$). Then feed it to the [[Thm - First Isomorphism Theorem|first isomorphism theorem]]: $G/\ker\varphi \cong \operatorname{im}\varphi$.

---

# Solution

The plan is to exhibit one homomorphism, the determinant, and check three things about it — that it is a homomorphism, that it is surjective, and that its kernel is $\mathrm{SL}_n(\mathbb{F})$ — so that the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] delivers the result.

**Step 1: The determinant is a homomorphism $\det : \mathrm{GL}_n(\mathbb{F}) \to \mathbb{F}^\times$.**

The map $A \mapsto \det(A)$ sends invertible matrices to *nonzero* field elements and satisfies $\det(AB) = \det(A)\det(B)$, so it is a group homomorphism into $\mathbb{F}^\times$.

> [!note]- Derivation
> First, the codomain. A matrix $A$ is invertible over a field if and only if $\det(A) \neq 0$; concretely, $A \in \mathrm{GL}_n(\mathbb{F})$ has an inverse $A^{-1}$, and applying the multiplicativity of $\det$ to $A A^{-1} = I$ gives $\det(A)\det(A^{-1}) = \det(I) = 1$, so $\det(A)$ has a multiplicative inverse in $\mathbb{F}$ and is therefore nonzero. Hence $\det(A) \in \mathbb{F}^\times$ for every $A \in \mathrm{GL}_n(\mathbb{F})$, and the map genuinely lands in $\mathbb{F}^\times$.
>
> Next, the homomorphism property. A [[Def - Homomorphism|homomorphism]] is a map $\varphi$ with $\varphi(g_1 g_2) = \varphi(g_1)\varphi(g_2)$. The determinant satisfies exactly this — the multiplicativity of the determinant, $\det(AB) = \det(A)\det(B)$, is a standard fact of linear algebra valid over any field. The operation on the left is matrix multiplication in $\mathrm{GL}_n(\mathbb{F})$; the operation on the right is multiplication in $\mathbb{F}^\times$. So
> $$\det : \mathrm{GL}_n(\mathbb{F}) \longrightarrow \mathbb{F}^\times$$
> is a group homomorphism. (Consistency check: $\det(I) = 1$, the identity of $\mathbb{F}^\times$, as a homomorphism must satisfy.)

**Step 2: The determinant is surjective onto $\mathbb{F}^\times$.**

Every nonzero scalar $\lambda \in \mathbb{F}^\times$ is the determinant of some invertible matrix — for instance the diagonal matrix with one entry $\lambda$ and the rest $1$. So $\operatorname{im}(\det) = \mathbb{F}^\times$.

> [!note]- Derivation
> Fix any $\lambda \in \mathbb{F}^\times$. Let $D_\lambda$ be the diagonal matrix
> $$D_\lambda = \operatorname{diag}(\lambda, 1, 1, \ldots, 1),$$
> that is, the identity matrix with its top-left entry replaced by $\lambda$. Its determinant is the product of the diagonal entries, $\det(D_\lambda) = \lambda \cdot 1 \cdots 1 = \lambda$, which is nonzero, so $D_\lambda$ is invertible and $D_\lambda \in \mathrm{GL}_n(\mathbb{F})$.
>
> Thus every $\lambda \in \mathbb{F}^\times$ equals $\det(D_\lambda)$ for an explicit element $D_\lambda$ of the domain. Therefore the image of $\det$ is all of $\mathbb{F}^\times$:
> $$\operatorname{im}(\det) = \mathbb{F}^\times,$$
> and $\det$ is surjective. (For $n = 1$ this is immediate, since $\mathrm{GL}_1(\mathbb{F}) = \mathbb{F}^\times$ and $\det$ is the identity map.)

**Step 3: The kernel of the determinant is exactly $\mathrm{SL}_n(\mathbb{F})$.**

By the very definition of $\mathrm{SL}_n(\mathbb{F})$ as the determinant-$1$ matrices, $\ker(\det) = \mathrm{SL}_n(\mathbb{F})$. Since kernels are always normal, this already proves $\mathrm{SL}_n(\mathbb{F}) \trianglelefteq \mathrm{GL}_n(\mathbb{F})$.

> [!note]- Derivation
> The [[Def - Kernel and Image|kernel]] of $\det$ is the set of elements mapped to the identity of the codomain. The identity of $\mathbb{F}^\times$ is the number $1$, so
> $$\ker(\det) = \{\, A \in \mathrm{GL}_n(\mathbb{F}) : \det(A) = 1 \,\}.$$
> But the right-hand side is, word for word, the definition of the special linear group $\mathrm{SL}_n(\mathbb{F})$. Hence
> $$\ker(\det) = \mathrm{SL}_n(\mathbb{F}).$$
>
> Now invoke a structural fact from [[Def - Kernel and Image]]: the kernel of any group homomorphism is a *normal* subgroup of its domain. (Reason: for $A \in \ker\varphi$ and any $g$, $\varphi(g A g^{-1}) = \varphi(g)\varphi(A)\varphi(g)^{-1} = \varphi(g)\,e\,\varphi(g)^{-1} = e$, so $gAg^{-1} \in \ker\varphi$.) Applying this to $\varphi = \det$ shows immediately that
> $$\mathrm{SL}_n(\mathbb{F}) = \ker(\det) \trianglelefteq \mathrm{GL}_n(\mathbb{F}).$$
> This disposes of the normality claim with no conjugation calculation on matrices — the work was done once, generically, inside the kernel-is-normal lemma.

**Step 4: Apply the first isomorphism theorem.**

With $\det$ a surjective homomorphism whose kernel is $\mathrm{SL}_n(\mathbb{F})$, the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] gives $\mathrm{GL}_n(\mathbb{F})/\mathrm{SL}_n(\mathbb{F}) \cong \mathbb{F}^\times$.

> [!note]- Derivation
> The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] states that for any homomorphism $\varphi : G \to H$, the kernel is normal and
> $$G/\ker\varphi \;\cong\; \operatorname{im}\varphi,$$
> the isomorphism being the map $g \ker\varphi \mapsto \varphi(g)$.
>
> Apply it with $G = \mathrm{GL}_n(\mathbb{F})$, $H = \mathbb{F}^\times$, and $\varphi = \det$. By Step 3, $\ker(\det) = \mathrm{SL}_n(\mathbb{F})$. By Step 2, $\operatorname{im}(\det) = \mathbb{F}^\times$. Substituting,
> $$\mathrm{GL}_n(\mathbb{F}) \big/ \mathrm{SL}_n(\mathbb{F}) \;\cong\; \mathbb{F}^\times.$$
> Explicitly, the isomorphism sends the coset $A\,\mathrm{SL}_n(\mathbb{F})$ to the scalar $\det(A)$ — two invertible matrices lie in the same coset of $\mathrm{SL}_n(\mathbb{F})$ exactly when they have the same determinant. $\blacksquare$

> [!note]- Complete formal solution
> Define $\varphi = \det : \mathrm{GL}_n(\mathbb{F}) \to \mathbb{F}^\times$, $A \mapsto \det(A)$.
>
> *This is a well-defined homomorphism into $\mathbb{F}^\times$.* If $A \in \mathrm{GL}_n(\mathbb{F})$ then $A$ is invertible, and from $\det(A)\det(A^{-1}) = \det(AA^{-1}) = \det(I) = 1$ we see $\det(A) \neq 0$, so $\det(A) \in \mathbb{F}^\times$. The multiplicativity $\det(AB) = \det(A)\det(B)$ is exactly the homomorphism property.
>
> *$\varphi$ is surjective.* Given $\lambda \in \mathbb{F}^\times$, the matrix $D_\lambda = \operatorname{diag}(\lambda, 1, \ldots, 1)$ has $\det(D_\lambda) = \lambda \neq 0$, so $D_\lambda \in \mathrm{GL}_n(\mathbb{F})$ and $\varphi(D_\lambda) = \lambda$. Hence $\operatorname{im}(\varphi) = \mathbb{F}^\times$.
>
> *The kernel is $\mathrm{SL}_n(\mathbb{F})$.* The identity of $\mathbb{F}^\times$ is $1$, so $\ker(\varphi) = \{A \in \mathrm{GL}_n(\mathbb{F}) : \det(A) = 1\} = \mathrm{SL}_n(\mathbb{F})$, by the definition of $\mathrm{SL}_n(\mathbb{F})$.
>
> *Normality.* The kernel of any homomorphism is a normal subgroup of its domain, so $\mathrm{SL}_n(\mathbb{F}) = \ker(\varphi) \trianglelefteq \mathrm{GL}_n(\mathbb{F})$.
>
> *Identification.* By the [[Thm - First Isomorphism Theorem|first isomorphism theorem]], $G/\ker\varphi \cong \operatorname{im}\varphi$. Substituting the kernel and image computed above,
> $$\mathrm{GL}_n(\mathbb{F}) \big/ \mathrm{SL}_n(\mathbb{F}) \;\cong\; \mathbb{F}^\times,$$
> with the isomorphism $A\,\mathrm{SL}_n(\mathbb{F}) \mapsto \det(A)$. $\blacksquare$

---

# Key Takeaways

**The general method for identifying a quotient: build a surjection out of $G$ whose kernel is exactly $N$.** This exercise is the cleanest template for the most important technique in the chapter. To put a concrete name on an abstract quotient $G/N$, you do not study cosets of $G$ directly — you guess the answer $Q$, construct a surjective homomorphism $\varphi : G \to Q$, and verify $\ker\varphi = N$. The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] then certifies $G/N \cong Q$ with no further work. Three checks and you are done: $\varphi$ is a homomorphism, $\varphi$ is onto, $\ker\varphi = N$. The reason this works so reliably is that it shifts all the difficulty into one creative act — choosing $\varphi$ — after which everything is mechanical. The same three-check pattern identifies $\mathbb{Z}/n\mathbb{Z}$ via reduction mod $n$ from $(\mathbb{Z}, +)$, identifies $S_n/A_n \cong \{\pm 1\}$ via the sign homomorphism, identifies $\mathbb{C}/2\pi i \mathbb{Z} \cong \mathbb{C}^\times$ via $z \mapsto e^z$, and identifies the quotient of any group by a centre or commutator subgroup once the right map is found. Whenever a problem says "show $G/N \cong \ldots$" or "what is this quotient", reach for this template before anything else.

**A subgroup defined as a level set is secretly a kernel — find the homomorphism it is the kernel of.** The signal that told us which map to build was the *definition* of $\mathrm{SL}_n(\mathbb{F})$: it is "the matrices where the determinant equals $1$". Any time a normal subgroup is described as the elements on which some natural, structure-respecting quantity attains its trivial value — determinant $1$, sign $+1$, trace... no, trace is not multiplicative, but determinant, sign, evaluation, "reduction mod $n$ equals $0$", "winding number $0$" all are — that quantity is a homomorphism and the subgroup is its kernel. The recognition heuristic is sharp: ask whether the defining quantity turns the group operation into a target group operation. If it does, you have simultaneously found the homomorphism, learned the subgroup is normal for free (kernels are always normal, so no conjugation calculation is ever needed), and obtained the target group $Q$ as wherever that quantity takes its values. This reframing — "level set" becomes "kernel" — is what converts a static subgroup into the dynamic object the first isomorphism theorem can act on.

**The target group is read off from where the homomorphism's invariant lives.** Choosing $Q = \mathbb{F}^\times$ was not a separate guess on top of choosing $\det$; the two are the same decision. Once you decide to measure a matrix by its determinant, the determinant *takes values in* the nonzero field elements under multiplication, so $\mathbb{F}^\times$ is forced as the target — there is no freedom left. The deeper principle is that a quotient $G/N$ is isomorphic to the group of *possible values* of any invariant whose "trivial value" set is exactly $N$. The quotient is, intuitively, "$G$ seen only through that invariant", and the invariant's value group is therefore the quotient itself. This is why the search for the homomorphism and the search for the answer are one search: identify the right invariant of elements of $G$ — the feature that is blind to $N$, equal on $A$ and $B$ exactly when $AB^{-1} \in N$ — and both the map and the target $Q$ appear together. When stuck identifying a quotient, do not separately brainstorm "what group is it" and "what map proves it"; brainstorm the single question "what feature of elements of $G$ is invisible to $N$".
