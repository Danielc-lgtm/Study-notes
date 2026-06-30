---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Equivalence of Categories"
  - "Thm - Characterization of Equivalence"
  - "Def - Full, Faithful, and Essentially Surjective Functor"
tags: [category-theory, foundations]
---

# Problem Statement

Let $k$ be a field. Define the **category of matrices** $\mathbf{Mat}_k$: its objects are the natural numbers $0, 1, 2, \dots$, a morphism $m \to n$ is an $n \times m$ matrix over $k$, composition is matrix multiplication, and the identity on $n$ is the $n \times n$ identity matrix. Show that $\mathbf{Mat}_k$ is [[Def - Equivalence of Categories|equivalent]] to $\mathbf{FinVect}_k$, the category of finite-dimensional [[Def - Vector Space|vector spaces]] and [[Def - Linear Map|linear maps]], but **not isomorphic** to it. Identify the equivalence functor explicitly and verify it is [[Def - Full, Faithful, and Essentially Surjective Functor|full, faithful, and essentially surjective]].

**Recall:**

![[Thm - Characterization of Equivalence#Statement]]

A functor is an equivalence iff it is full, faithful, and essentially surjective. An [[Def - Equivalence of Categories|isomorphism of categories]] additionally requires a bijection on objects.

---

# Convergent Strategy

**Problem class:** This is the canonical "exhibit an equivalence via the three local conditions" exercise. The route is to define the comparison functor $\mathbf{Mat}_k \to \mathbf{FinVect}_k$ and verify full + faithful + essentially surjective, then observe the object-counts differ to rule out isomorphism.

**Assumption pattern:** The decisive facts are (i) a [[Def - Linear Map|linear map]] $k^m \to k^n$ *is* an $n \times m$ matrix (full faithfulness, the bijection is essentially the identity), and (ii) every finite-dimensional space has a basis, hence is isomorphic to some $k^n$ (essential surjectivity). The first is linear algebra's matrix representation; the second is the existence of bases.

**Theorem routing:** Build $E : \mathbf{Mat}_k \to \mathbf{FinVect}_k$, $n \mapsto k^n$, matrix $\mapsto$ its linear map. Verify the three conditions, then invoke [[Thm - Characterization of Equivalence|the characterization]] to conclude $E$ is an equivalence — without constructing a quasi-inverse. Non-isomorphism follows from a cardinality mismatch on objects.

**Key decision point:** The non-obvious move is to *not* build the inverse functor $\mathbf{FinVect}_k \to \mathbf{Mat}_k$ directly (which would require choosing a basis of every space, a choice-laden mess), but instead verify the three local conditions on $E$ and let [[Thm - Characterization of Equivalence|the theorem]] manufacture the quasi-inverse. This is the whole point of the characterization theorem.

---

# Legal Operations Used

1. **Operation: prove an equivalence by full + faithful + essentially surjective** (topic page, Legal Operation 11; [[Thm - Characterization of Equivalence]]). Check the three local conditions on $E$, not the four-tuple.

2. **Operation: use existence of bases for essential surjectivity** (topic page, Legal Operation 4). Every finite-dim space is $\cong k^n$.

3. **Operation: refute isomorphism by an object-count mismatch** (topic page, Legal Operation 3). $\mathbf{Mat}_k$ has one object per [[Def - Dimension|dimension]]; $\mathbf{FinVect}_k$ has many.

---

# Hints

> [!note]- Hint 1
> Define $E : \mathbf{Mat}_k \to \mathbf{FinVect}_k$ on objects by $E(n) = k^n$ and on a matrix $A : m \to n$ by the linear map $x \mapsto Ax$. Check $E$ is a functor (matrix multiplication ↔ composition of linear maps).

> [!note]- Hint 2
> Faithful and full *together*: the linear maps $k^m \to k^n$ are *exactly* the $n \times m$ matrices, a bijection. So $E_{m,n} : \mathbf{Mat}_k(m,n) \to \mathbf{FinVect}_k(k^m, k^n)$ is a bijection.

> [!note]- Hint 3
> Essentially surjective: given a finite-dimensional $V$, choose a basis; this gives $V \cong k^{\dim V} = E(\dim V)$. So every object of $\mathbf{FinVect}_k$ is isomorphic to one in the image.

> [!note]- Hint 4
> Not isomorphic: $\mathbf{Mat}_k$ has exactly one object of each dimension, but $\mathbf{FinVect}_k$ has *many* spaces of each dimension (e.g. $k^2$ and $k[x]/(x^2)$ as a $k$-vector space). No object-bijection exists.

---

# Solution

The plan: define the comparison functor $E : \mathbf{Mat}_k \to \mathbf{FinVect}_k$, verify it is a functor, then check full + faithful (matrices *are* linear maps between coordinate spaces) and essentially surjective (bases exist), and invoke the characterization theorem. Non-isomorphism is a cardinality count on objects.

**Step 1: $E$ is a functor.**

> [!note]- Derivation
> Define $E(n) = k^n$ and, for a matrix $A \in \mathbf{Mat}_k(m, n)$ (an $n \times m$ matrix), $E(A) : k^m \to k^n$, $x \mapsto Ax$. Functoriality: $E(I_n) = (x \mapsto I_n x) = 1_{k^n}$, and for composable matrices $A : m \to n$, $B : n \to p$, the composite in $\mathbf{Mat}_k$ is $BA$ (matrix product), and $E(BA)(x) = (BA)x = B(Ax) = E(B)(E(A)(x))$, so $E(BA) = E(B)\circ E(A)$. Hence $E : \mathbf{Mat}_k \to \mathbf{FinVect}_k$ is a [[Def - Functor|functor]].

**Step 2: $E$ is full and faithful.**

> [!note]- Derivation
> Fix $m, n$. The action $E_{m,n} : \mathbf{Mat}_k(m, n) \to \mathbf{FinVect}_k(k^m, k^n)$ sends a matrix $A$ to the linear map $x \mapsto Ax$. This is a bijection: a [[Def - Linear Map|linear map]] $T : k^m \to k^n$ is uniquely determined by its values on the standard basis $e_1, \dots, e_m$, and the matrix whose $j$-th column is $T(e_j)$ is the unique matrix $A$ with $E(A) = T$. So $E_{m,n}$ is injective (faithful) and surjective (full) — indeed it is the standard bijection "matrix ↔ linear map between coordinate spaces". Hence $E$ is [[Def - Full, Faithful, and Essentially Surjective Functor|fully faithful]].

**Step 3: $E$ is essentially surjective.**

> [!note]- Derivation
> Let $V$ be a finite-dimensional [[Def - Vector Space|vector space]], say $\dim V = n$. Choosing a basis $v_1, \dots, v_n$ gives a [[Def - Linear Map|linear isomorphism]] $V \xrightarrow{\sim} k^n$ (send $\sum a_i v_i \mapsto (a_1, \dots, a_n)$). So $V \cong k^n = E(n)$, and every object of $\mathbf{FinVect}_k$ is isomorphic to one in the image of $E$. Thus $E$ is [[Def - Full, Faithful, and Essentially Surjective Functor|essentially surjective]].

**Step 4: $E$ is an equivalence but not an isomorphism.**

> [!note]- Derivation
> By [[Thm - Characterization of Equivalence|the characterization of equivalence]], a full, faithful, essentially surjective functor is an [[Def - Equivalence of Categories|equivalence]]. So $\mathbf{Mat}_k \simeq \mathbf{FinVect}_k$, and the theorem manufactures a quasi-inverse $G : \mathbf{FinVect}_k \to \mathbf{Mat}_k$ (which, traced through the construction, sends $V \mapsto \dim V$ after choosing a basis — the choice is exactly the axiom of choice in the theorem).
>
> It is *not* an [[Def - Equivalence of Categories|isomorphism of categories]]: an isomorphism requires a bijection on objects, but $\mathbf{Mat}_k$ has exactly one object of each dimension $n$, while $\mathbf{FinVect}_k$ has a proper class of distinct vector spaces of each dimension — for instance, of dimension $2$ there are $k^2$, the polynomial space $\{a + bx\}$, the space of $1\times 2$ matrices, and uncountably many more, all distinct as objects though pairwise isomorphic. No bijection of object-collections exists, so $\mathbf{Mat}_k \not\cong \mathbf{FinVect}_k$. The categories are equivalent but not isomorphic — the difference is exactly the redundant multiplicity of isomorphic copies.

> [!note]- Complete formal solution
> Define $E : \mathbf{Mat}_k \to \mathbf{FinVect}_k$, $E(n) = k^n$, $E(A) = (x \mapsto Ax)$. It is a functor: $E(I) = 1$, $E(BA) = E(B)E(A)$. It is fully faithful: $A \mapsto (x \mapsto Ax)$ is the bijection "matrices ↔ linear maps $k^m \to k^n$". It is essentially surjective: any $V$ with $\dim V = n$ satisfies $V \cong k^n = E(n)$ via a basis. By [[Thm - Characterization of Equivalence|the characterization]], $E$ is an equivalence, so $\mathbf{Mat}_k \simeq \mathbf{FinVect}_k$. It is not an isomorphism because $\mathbf{Mat}_k$ has one object per dimension while $\mathbf{FinVect}_k$ has many, so no object-bijection exists. $\blacksquare$

---

# Key Takeaways

**Prove equivalences by the three local conditions, never by hunting for the inverse.** The reusable method, and the entire reason [[Thm - Characterization of Equivalence|the characterization theorem]] exists, is that to show $\mathcal{C} \simeq \mathcal{D}$ you exhibit one functor and check full + faithful + essentially surjective — three checks that proceed one hom-set or one object at a time — rather than constructing a quasi-inverse and two natural [[Def - Isomorphism|isomorphisms]] by hand. Here, building $\mathbf{FinVect}_k \to \mathbf{Mat}_k$ directly would force a basis choice for every space and a verification of naturality; the characterization theorem does that choosing for you. Whenever you suspect two categories are equivalent, define the obvious comparison functor and run the three-condition checklist.

**$\mathbf{Mat}_k$ is the skeleton of $\mathbf{FinVect}_k$ — equivalence forgives isomorphic copies.** The conceptual content is that $\mathbf{Mat}_k$ is a [[Def - Subcategory|skeleton]]: it keeps exactly one object ($k^n$, encoded as the number $n$) per isomorphism class, discarding the redundant multiplicity of isomorphic spaces. Equivalence is precisely the relation that cannot see this multiplicity, while isomorphism of categories can. This is the cleanest illustration of "equivalence allows iso, not equality, on objects": the two categories carry identical morphism-structure but differ in how many copies of each object they keep, and that difference is invisible to equivalence and fatal to isomorphism.

**"Linear algebra is matrices, up to choosing bases" is a theorem about categories.** The folklore that "doing linear algebra in coordinates" loses nothing is made precise here: the equivalence $\mathbf{Mat}_k \simeq \mathbf{FinVect}_k$ says coordinate computations and abstract linear algebra carry exactly the same information, with the basis choice being the quasi-inverse's use of the axiom of choice. This is the template for every "concrete model up to choices" statement — representations as matrices, manifolds in charts, schemes from [[Def - Ring|rings]] — where an equivalence of categories certifies that the concrete model is faithful and the choices are harmless. Recognizing such a statement as "an equivalence with the choice living in the quasi-inverse" is the categorical reading of "without loss of generality, choose coordinates".
