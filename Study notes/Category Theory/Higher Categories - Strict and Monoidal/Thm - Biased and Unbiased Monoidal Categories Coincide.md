---
type: theorem
subject: higher-categories
prereqs:
  - "Def - Monoidal Category"
  - "Def - Unbiased Monoidal Category"
  - "Def - Weak and Lax Monoidal Functor"
  - "Thm - Mac Lane Coherence Theorem"
tags: [category-theory, higher-categories, foundations]
---

# Notation

A **biased** monoidal category is the usual [[Def - Monoidal Category|monoidal category]] $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$: a binary tensor $\otimes$, a unit $I$, associator $\alpha$, and unitors $\lambda, \rho$, subject to the pentagon and triangle. An **unbiased** monoidal category $(\mathcal{C}, (\otimes_n)_{n \geq 0}, \gamma, \iota)$ has an $n$-ary tensor for every $n$, composition isomorphisms $\gamma$ and unit isomorphism $\iota$, subject to associativity and unit coherence (see [[Def - Unbiased Monoidal Category]]). We write $\mathbf{MonCat}_{\mathrm{b}}$ and $\mathbf{MonCat}_{\mathrm{u}}$ for the $2$-categories of biased and unbiased monoidal categories, with weak (strong) [[Def - Weak and Lax Monoidal Functor|monoidal functors]] as $1$-cells and monoidal natural transformations as $2$-cells. The full registry is on [[Higher Categories — Strict n-Categories and Notions of Monoidal Category]].

---

# Statement

> **Theorem (Biased = Unbiased).** There is a $2$-equivalence of $2$-categories
> $$\mathbf{MonCat}_{\mathrm{u}} \;\simeq\; \mathbf{MonCat}_{\mathrm{b}}$$
> between unbiased monoidal categories and biased ([[Def - Monoidal Category|classical]]) monoidal categories. In particular, every unbiased monoidal category has an underlying biased one (take $\otimes := \otimes_2$, $I := \otimes_0()$), every biased monoidal category extends to an unbiased one (take $\otimes_n$ to be left-bracketed iterated $\otimes$), and these two operations are mutually inverse up to monoidal equivalence. The same holds in the braided and symmetric variants.

The content in one line: **specifying all arities at once carries exactly the same information as specifying the binary one and bracketing.**

---

# Motivation

The unbiased definition is conceptually cleaner — its coherence reduces to two "associativity is associative" axioms — but the binary, biased definition is the one everyone already uses and the one in which the standard examples are phrased. A theory is only useful if these two presentations describe the *same* objects; otherwise the unbiased framework would be a parallel world disconnected from ordinary monoidal category theory. This theorem is the bridge. It licenses moving freely between "I have a binary tensor and a pentagon" and "I have a coherent system of all tensors," using whichever is convenient for the problem at hand.

Its deeper role is to identify the biased data as a **presentation** of the unbiased object. A group can be given by generators and relations, but the group itself does not depend on the presentation; likewise a monoidal category can be *presented* by the binary tensor (generator) and the pentagon (relation), but the monoidal category itself is the unbiased object. The pentagon is not a mysterious five-sided coincidence — it is precisely the relation needed so that the binary generator generates the *correct* operad of arities, the one whose unique $n$-ary operation is the $n$-fold tensor. Understanding this is what makes the [[Thm - Coherence for Unbiased Monoidal Categories|coherence theorem]] feel inevitable rather than miraculous.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's literal input is "a biased (or an unbiased) monoidal category." The skill is recognising structures that *are* one of these in disguise, so that the equivalence can be invoked to switch presentations.

The first disguised source is **any structure defined by an $n$-ary universal property** — an $n$-fold [[Def - Tensor Product of Vector Spaces|tensor product]] representing $n$-linear maps, an $n$-fold [[Def - Limit and Colimit|product]] representing $n$-tuples of maps, an $n$-fold coproduct. Here the *unbiased* structure is the honest one: the $\otimes_n$ are given directly by universal properties, and the $\gamma$'s are canonical comparisons of representing objects. The non-obvious step is to realise you have an unbiased monoidal category for free and may therefore extract a binary one (with its pentagon supplied automatically by the theorem) without ever checking the pentagon by hand. *Example problem:* show $(\mathbf{Vect}_k, \otimes_k)$ is monoidal by defining $\otimes_n$ via the universal property of multilinear maps and invoking the theorem, rather than constructing $\alpha$ and verifying the pentagon directly.

The second disguised source is **a pseudo-algebra for the free-monoidal-category $2$-monad $M$**, or an algebra for the lists/As operad in $\mathbf{Cat}$. Any time a category carries a coherent "tensor a list" operation, it is unbiased monoidal, hence biased monoidal. The non-obviousness is that operad/$2$-monad algebra data does not look like a binary tensor with a pentagon; the theorem is what converts the operadic packaging into the familiar one. *Example problem:* given that $\mathbf{Cat}$-valued algebras for the As operad are exactly unbiased monoidal categories, conclude that they are ordinary monoidal categories.

The third disguised source is **a one-object [[Def - 2-Category and Bicategory|bicategory]] (for the weak case) or a one-object strict $2$-category (for the strict case)**. A bicategory with a single $0$-cell is a biased monoidal category; if instead it is presented with chosen composites of every length, it is unbiased. The theorem says these one-object descriptions agree, which is exactly what is needed to compare the two standard routes into monoidal categories from higher category theory. *Example problem:* identify the endomorphism monoidal category $\mathcal{B}(\star,\star)$ of a one-object bicategory, presented unbiasedly via $n$-fold pasting, with the classical monoidal category.

**Targets (Output Amplification)**

The bare conclusion is an equivalence of $2$-categories. Combined with other facts it does much more.

Combine the equivalence with **the unbiased coherence theorem**. Because the equivalence is monoidal, [[Thm - Coherence for Unbiased Monoidal Categories|coherence on the unbiased side]] — every diagram of $\gamma$'s commutes — transports across to give [[Thm - Mac Lane Coherence Theorem|Mac Lane's biased coherence theorem]]: every diagram of $\alpha$'s, $\lambda$'s, $\rho$'s commutes. This is the cleanest known *proof* of biased coherence: prove it trivially on the unbiased side, transport. The combination is non-obvious because it derives a hard biased theorem from an easy unbiased one purely by changing presentation.

Combine the equivalence with **a strictification theorem on either side**. Since the two $2$-categories are equivalent, [[Thm - Strictification of Monoidal Categories|strictification]] (every monoidal category is monoidally equivalent to a strict one) can be proved on whichever side is convenient and exported to the other. The further result is that "biased, unbiased, and strict" form a chain of equivalent notions: $\mathbf{MonCat}_{\mathrm{b}} \simeq \mathbf{MonCat}_{\mathrm{u}} \simeq \mathbf{StrMonCat}$ (the last as a non-full sub-$2$-category, equivalent via inclusion).

Combine the equivalence with **the theory of monoids**. A [[Def - Monoid in a Monoidal Category|monoid]] in a biased monoidal category and a monoid in the corresponding unbiased one are the same — the multiplication $M \otimes M \to M$ on the biased side corresponds to the binary instance $\otimes_2(M, M) \to M$ of an unbiased monoid (a coherent family $\otimes_n(M, \dots, M) \to M$). The target is that one may *define* a monoid by giving all-arity multiplications, which is sometimes the natural data (for instance an algebra over an operad), and know it agrees with the binary definition.

---

# Why Is It True

The honest reason is bookkeeping made precise: **the binary tensor generates all the others by bracketing, and the pentagon-plus-triangle is exactly the relation that makes the generated family unambiguous — which is exactly the unbiased coherence data.** Nothing is created or destroyed in passing between the two; one direction expands a list into a left-bracketed product, the other contracts an all-arity family to its binary part.

Go from unbiased to biased first, the easy direction. Given the all-arity family, simply forget everything except $\otimes_2$ and $\otimes_0()$. The associator is recovered as a composite of $\gamma$'s: $(A \otimes_2 B)\otimes_2 C = \otimes_2(\otimes_2(A,B), C)$ is $\gamma^{-1}$-related to $\otimes_3(A,B,C)$, which is $\gamma$-related to $\otimes_2(A, \otimes_2(B,C)) = A \otimes_2 (B \otimes_2 C)$; the pentagon for this $\alpha$ is the unbiased associativity axiom on a length-four list. So the biased structure is *contained in* the unbiased one, and its coherence is free.

The other direction is where the pentagon earns its keep. Given a biased monoidal category, define $\otimes_n$ by left-bracketing: $\otimes_n(A_1, \dots, A_n) = ((\cdots(A_1 \otimes A_2)\otimes A_3)\cdots)\otimes A_n$. The composition isomorphisms $\gamma$ must be built from associators and unitors — and here is the only place a theorem is needed: to *define* $\gamma$ we must choose a way to re-bracket, and to know $\gamma$ is well-defined and satisfies the unbiased axioms we must know that any two ways of re-bracketing give the same isomorphism. **That is precisely [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]].** So the round trip unbiased $\to$ biased $\to$ unbiased is the identity essentially by construction, and the round trip biased $\to$ unbiased $\to$ biased recovers the original up to the canonical coherence isomorphisms. The two operations are mutually inverse $2$-functors, hence a $2$-equivalence.

A useful slogan: a biased monoidal category is an unbiased one viewed through the bracketing $\otimes_2$, and the pentagon is the receipt proving the view loses no information.

---

# What Makes This Hard

The trap is circularity. The clean proof of the unbiased-to-biased coherence statement *uses* Mac Lane coherence, while a naive reader expects this theorem to *replace* it — so one must be careful about which coherence result is assumed where. The honest logical order is: prove unbiased coherence directly (it is nearly a tautology because the As operad has one operation per arity); use it to define the $\gamma$'s from a biased structure and verify the equivalence; and *deduce* biased coherence as a corollary. The second subtlety is that the equivalence is of $2$-categories, not mere categories: one must produce comparison weak [[Def - Weak and Lax Monoidal Functor|monoidal functors]] and check they are monoidal *equivalences*, tracking the coherence cells, which is where most of the actual work hides.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Build a $2$-functor $U : \mathbf{MonCat}_{\mathrm{u}} \to \mathbf{MonCat}_{\mathrm{b}}$ (forget to the binary part) and a $2$-functor $B : \mathbf{MonCat}_{\mathrm{b}} \to \mathbf{MonCat}_{\mathrm{u}}$ (left-bracket and supply $\gamma$ via coherence). Then exhibit monoidal natural isomorphisms $UB \cong \mathrm{id}$ and $BU \cong \mathrm{id}$. The only nontrivial input is that $\gamma$ is well-defined, which is Mac Lane coherence.

**Subgoal decomposition:**

1. **Define $U$ (unbiased $\to$ biased).** Set $\otimes := \otimes_2$, $I := \otimes_0()$, and build $\alpha, \lambda, \rho$ from $\gamma, \iota$.
   - *Hint:* $\alpha$ is $\gamma_{1,2} \circ \gamma_{2,1}^{-1}$ on the relevant length-three list; unitors come from $\iota$ and the $\gamma$'s involving $\otimes_0$.
   - *Why needed:* This produces the biased data; the pentagon for it is then an instance of the unbiased associativity axiom.

2. **Verify $U$ lands in biased monoidal categories.** Check the pentagon and triangle for the constructed $\alpha, \lambda, \rho$.
   - *Hint:* Each is a special case (length four for pentagon, the unit-insertion case for triangle) of the unbiased coherence axioms.
   - *Why needed:* Without this $U$ does not even have the right codomain.

3. **Define $B$ (biased $\to$ unbiased).** Set $\otimes_n$ to be left-bracketed iterated $\otimes$, and define $\gamma$ by re-bracketing via $\alpha, \lambda, \rho$.
   - *Hint:* Any composite of associators/unitors taking one bracketing of a list to another defines the candidate $\gamma$.
   - *Why needed:* This is the data of the unbiased structure; the next step makes it well-defined.

4. **Prove $\gamma$ is well-defined and coherent — invoke Mac Lane.** Show the choice of re-bracketing does not matter and that the unbiased axioms hold.
   - *Hint:* [[Thm - Mac Lane Coherence Theorem|Mac Lane coherence]]: any two formal composites of associators/unitors with the same source and target are equal.
   - *Why needed:* This is the single nontrivial input; it is what makes $B$ a functor into $\mathbf{MonCat}_{\mathrm{u}}$.

5. **Exhibit the equivalence.** Construct monoidal natural isomorphisms $UB \cong \mathrm{id}_{\mathbf{MonCat}_{\mathrm{b}}}$ and $BU \cong \mathrm{id}_{\mathbf{MonCat}_{\mathrm{u}}}$.
   - *Hint:* $UB$ returns left-bracketed $\otimes_2$, which is the original $\otimes$ on the nose; $BU$ returns the all-arity family, isomorphic to the original via the $\gamma$'s.
   - *Why needed:* Mutually inverse up to coherent isomorphism is exactly a $2$-equivalence.

---

# Lemma Decomposition

> [!note]- Lemma 1: The associator built from $\gamma$ satisfies the pentagon
> **Statement:** In any unbiased monoidal category, the morphism $\alpha_{A,B,C} := \gamma_{1,2} \circ \gamma_{2,1}^{-1} : (A\otimes_2 B)\otimes_2 C \to A \otimes_2(B\otimes_2 C)$ is a natural isomorphism satisfying Mac Lane's pentagon.
>
> **Hint:** Write each side of the pentagon as a composite of $\gamma$'s applied to the length-four list $(A,B,C,D)$; both reduce, by the unbiased associativity axiom, to the single comparison with $\otimes_4(A,B,C,D)$.
>
> **Why needed:** It shows $U$ lands among genuine biased monoidal categories (subgoal 2), so the forgetful map is well-typed.
>
> > [!note]- Full proof
> > Naturality of $\alpha$ follows from naturality of $\gamma$. For the pentagon, both routes from $((A\otimes B)\otimes C)\otimes D$ to $A\otimes(B\otimes(C\otimes D))$ are composites of instances of $\gamma_{k_1,\dots,k_n}^{\pm}$. Insert the common refinement $\otimes_4(A,B,C,D)$: each route equals the composite $\big(\text{compare top bracketing with } \otimes_4\big)$ followed by $\big(\text{compare } \otimes_4 \text{ with bottom bracketing}\big)$. By the unbiased *associativity coherence* axiom, contracting the $\gamma$'s in either order to reach $\otimes_4$ gives the same isomorphism. Hence the two routes agree, which is the pentagon.
>
> [!note]- Lemma 2: $\gamma$ is well-defined from a biased structure
> **Statement:** For a biased monoidal category, any two composites of associators and unitors taking the left-bracketing of a list $(A_1,\dots,A_n)$ to a given other bracketing are equal; hence the candidate $\gamma$ in subgoal 3 is well-defined.
>
> **Hint:** This is exactly the conclusion of Mac Lane's coherence theorem for the free monoidal category on $n$ generators.
>
> **Why needed:** Without well-definedness, $B$ does not produce an unbiased monoidal category (subgoal 4).
>
> > [!note]- Full proof
> > [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]] states that in the free monoidal category on a set of generators, any two morphisms built from the structural isomorphisms $\alpha, \lambda, \rho$ (and their inverses) with the same source and target are equal — equivalently, every diagram of structural isomorphisms commutes. The two re-bracketing composites are precisely two such morphisms in the free monoidal category on $\{A_1, \dots, A_n\}$ with the same source (the chosen source bracketing) and target. By coherence they are equal, so $\gamma$ does not depend on the chosen composite. Naturality and the unbiased axioms then follow because they too are equalities of structural composites, again forced by coherence.
>
> [!note]- Lemma 3: The round trips are monoidal natural isomorphisms
> **Statement:** $UB \cong \mathrm{id}_{\mathbf{MonCat}_{\mathrm{b}}}$ and $BU \cong \mathrm{id}_{\mathbf{MonCat}_{\mathrm{u}}}$ via monoidal natural isomorphisms.
>
> **Hint:** $UB$ returns the original binary $\otimes$ unchanged; for $BU$, the components are the $\gamma$'s comparing $\otimes_n$ with its left-bracketing.
>
> **Why needed:** This is the final assembly: mutually inverse up to coherent iso is a $2$-equivalence (subgoal 5).
>
> > [!note]- Full proof
> > For $UB$: starting from a biased $(\mathcal{C}, \otimes, I)$, $B$ produces $\otimes_n =$ left-bracketed iterate, and $U$ extracts $\otimes_2 = \otimes$ and $\otimes_0() = I$ with $\alpha$ rebuilt from $\gamma$. By construction $\gamma$ on a length-three list is built from $\alpha$, so $U$ recovers the original $\alpha$; thus $UB$ is the identity on objects and structure (no nontrivial comparison needed). For $BU$: starting from an unbiased $(\mathcal{C}, (\otimes_n), \gamma, \iota)$, $U$ extracts the binary part and $B$ re-expands by left-bracketing, yielding $\otimes_n' =$ left-bracketed $\otimes_2$. The original $\otimes_n$ and $\otimes_n'$ are compared by the isomorphism $\gamma_{2,1}\gamma_{2,1}\cdots$ assembling $\otimes_n$ from binary tensors; these are the components of a monoidal natural isomorphism $BU \cong \mathrm{id}$, monoidal because they are built from $\gamma$ which is coherent. Hence the $2$-functors are mutually pseudo-inverse, giving a $2$-equivalence.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — the $2$-categories.** $\mathbf{MonCat}_{\mathrm{b}}$ and $\mathbf{MonCat}_{\mathrm{u}}$ have monoidal categories as objects, weak (strong) [[Def - Weak and Lax Monoidal Functor|monoidal functors]] as $1$-cells, and monoidal natural transformations as $2$-cells. We construct mutually pseudo-inverse $2$-functors.
>
> **Step 1 — the forgetful $2$-functor $U$.** Define $U : \mathbf{MonCat}_{\mathrm{u}} \to \mathbf{MonCat}_{\mathrm{b}}$ on objects by $\otimes := \otimes_2$, $I := \otimes_0()$, $\lambda :=$ (the composite $\iota$-then-$\gamma$ for $\otimes_2(I,-)$), $\rho$ dually, and $\alpha_{A,B,C} := \gamma_{1,2;A,B,C} \circ \gamma_{2,1;A,B,C}^{-1}$. By Lemma 1, $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$ satisfies the pentagon, and the triangle follows from the unit coherence axiom; so $U$ is well-defined on objects. On a weak monoidal functor $(F, \varphi_n)$, $U$ keeps $F$ and the binary comparison $\varphi_2$ and unit comparison $\varphi_0$; the lax coherence axioms restrict correctly. $U$ is a strict $2$-functor.
>
> **Step 2 — the bracketing $2$-functor $B$.** Define $B : \mathbf{MonCat}_{\mathrm{b}} \to \mathbf{MonCat}_{\mathrm{u}}$ on objects by $\otimes_n :=$ left-bracketed iterated $\otimes$ (with $\otimes_0() = I$, $\otimes_1 = \mathrm{id}$ via $\lambda$/$\rho$). Define $\gamma_{k_1,\dots,k_n}$ as *any* composite of associators and unitors taking the left-bracketing of the concatenated list to the nested tensor on the left; by Lemma 2 (Mac Lane coherence) this is independent of the chosen composite, and the unbiased associativity and unit coherence axioms hold because they are equalities of structural composites, hence true by coherence. So $B$ lands in $\mathbf{MonCat}_{\mathrm{u}}$. On a weak monoidal functor it builds the all-arity comparison $\varphi_n$ from $\varphi_2, \varphi_0$ by the same bracketing, well-defined by coherence.
>
> **Step 3 — pseudo-inverse.** By Lemma 3, $UB \cong \mathrm{id}_{\mathbf{MonCat}_{\mathrm{b}}}$ and $BU \cong \mathrm{id}_{\mathbf{MonCat}_{\mathrm{u}}}$ via monoidal natural isomorphisms whose components are built from $\gamma$ (equivalently $\alpha,\lambda,\rho$). These witness that $U$ and $B$ are mutually pseudo-inverse $2$-functors.
>
> **Step 4 — conclude.** A pair of mutually pseudo-inverse $2$-functors is a $2$-equivalence. Therefore $\mathbf{MonCat}_{\mathrm{u}} \simeq \mathbf{MonCat}_{\mathrm{b}}$. The braided and symmetric variants are identical with the symmetric-group actions carried along, replacing the As operad by the braid/symmetric operad and Mac Lane coherence by its braided/symmetric counterpart. $\qquad \blacksquare$

---

# Cross-Field Exercise Suggestions

**Linear algebra — the $n$-fold tensor product.** Define $\otimes_n$ on $\mathbf{Vect}_k$ directly by the universal property of $n$-linear maps and verify it is unbiased monoidal; then use the theorem to extract the usual binary $\otimes_k$ with its pentagon *for free*, never computing an associator by hand. This is non-obvious because the natural object in multilinear algebra is the all-arity tensor, and the theorem certifies that the textbook binary tensor is the same data.

**Topology — the smash product and based spaces.** The smash product $\wedge$ on pointed spaces is notoriously fiddly to associate strictly. Phrasing it unbiasedly (the $n$-fold smash $X_1 \wedge \cdots \wedge X_n$ as a single quotient) sidesteps the bracketing headaches; the theorem returns the binary biased version with coherence guaranteed. The application is nonobvious because the $n$-fold smash is *more* natural than the binary one, reversing the usual intuition.

**Algebra — operad algebras as monoids.** An algebra over the associative operad $\mathrm{As}$ specifies $n$-ary multiplications $A^{\otimes n} \to A$ for all $n$ coherently; the theorem (its monoid corollary) says this is the same as an ordinary [[Def - Monoid in a Monoidal Category|monoid]] with a single binary multiplication. Recognising that "all-arity multiplications" collapses to "one binary multiplication" is exactly the categorified statement of the theorem, applied to monoids rather than monoidal categories.

---

# Bridges

- **[[Thm - Coherence for Unbiased Monoidal Categories|Coherence for unbiased monoidal categories]]** — the engine behind this equivalence. Coherence on the unbiased side is nearly a tautology (one operation per arity), and transporting it across the equivalence *is* the proof of [[Thm - Mac Lane Coherence Theorem|Mac Lane's biased coherence]]. So this theorem and unbiased coherence together explain why the pentagon suffices: the pentagon is the binary presentation of "one operation per arity."

- **[[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]]** — both an input and an output. As an input, it is what makes the $\gamma$'s well-defined when bracketing a biased structure (Lemma 2). As an output, it is recovered by transporting unbiased coherence across the equivalence. The two-way relationship is the heart of why "biased" and "unbiased" are interchangeable.

- **[[Thm - Strictification of Monoidal Categories|Strictification of monoidal categories]]** — the next refinement. Where this theorem says biased and unbiased are equivalent, strictification says *both* are equivalent to *strict* monoidal categories. Together they collapse the apparent zoo (biased weak, unbiased weak, strict) into one equivalence class, so any monoidal category may be treated as strict whenever convenient.

- **[[Def - 2-Category and Bicategory|One-object bicategories]]** — the higher-dimensional analogue. Just as biased and unbiased monoidal categories coincide, biased bicategories (binary composition with associator) and unbiased ones (chosen composites of pasting diagrams of every shape) coincide, by the same operadic argument one dimension up.

---

# Unlocked by This

> [!tip] Strictification and "Every Monoidal Category is Strict" *(from this chapter)*
> Combined with [[Thm - Strictification of Monoidal Categories|strictification]], this theorem licenses the working mathematician's habit of dropping all associators and unitors: every monoidal category, biased or unbiased, is monoidally equivalent to a strict one, so coherence lets you compute as if $\otimes$ were strictly associative.

> [!tip] Coherence for Higher Structures *(from Higher Category Theory)*
> The biased/unbiased dichotomy and its resolution recur at every level: for **bicategories**, for **tricategories**, and for **symmetric monoidal $(\infty,n)$-categories**. The principle "present by low-arity generators or take all arities as primitive — they agree by an operadic coherence theorem" is one of the load-bearing ideas of the whole subject.
