---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Yoneda Lemma"
  - "Def - Hom-Functor and Representable Functor"
  - "Def - Group"
tags: [category-theory, foundations]
---

# Problem Statement

Use the [[Thm - The Yoneda Lemma|Yoneda lemma]] to compute the following sets of natural transformations, in each case by identifying a representable domain and evaluating the codomain at the representing object.

1. Natural endomorphisms of the forgetful functor $U : \mathbf{Grp} \to \mathbf{Set}$.
2. Natural endomorphisms of the forgetful functor $U : \mathbf{Ring} \to \mathbf{Set}$.
3. Natural transformations $\mathbf{Set}(A, -) \Rightarrow \mathbf{Set}(B, -)$ between two representable functors on $\mathbf{Set}$.

**Recall:**

![[Thm - The Yoneda Lemma#Statement]]

The [[Thm - The Yoneda Lemma|Yoneda lemma]] gives $\mathrm{Nat}(\mathcal{C}(A, -), F) \cong F(A)$, $\alpha \mapsto \alpha_A(1_A)$. The forgetful functor $U : \mathbf{Grp} \to \mathbf{Set}$ is representable by $\mathbb{Z}$ (see [[Def - Group]]), and $U : \mathbf{Ring} \to \mathbf{Set}$ by $\mathbb{Z}[x]$.

---

# Convergent Strategy

**Problem class:** This is a direct "compute a natural transformation set" exercise, the bread-and-butter application of the Yoneda lemma. The topic page's strategy is: recognize the domain as representable, then the answer is "evaluate the codomain at the representing object" — no naturality-square bookkeeping required.

**Assumption pattern:** Each domain functor is *representable*: $U \cong \mathbf{Grp}(\mathbb{Z}, -)$, $U \cong \mathbf{Ring}(\mathbb{Z}[x], -)$, and $\mathbf{Set}(A, -)$ is representable by definition. The decisive assumption is therefore "the domain is a hom-functor", which is exactly the precondition that lets Yoneda apply.

**Theorem routing:** The route is uniform: rewrite the domain as $\mathcal{C}(A, -)$, then $\mathrm{Nat}(\mathcal{C}(A, -), F) \cong F(A)$ by the [[Thm - The Yoneda Lemma|Yoneda lemma]]. For part 3, with $F = \mathbf{Set}(B, -)$, this is [[Thm - The Yoneda Embedding is Fully Faithful|full faithfulness]]: the answer is $\mathbf{Set}(B, A)$. Then *interpret* the resulting set concretely (the $n$-th power map, the constant ring maps, the precomposition functions).

**Key decision point:** The interesting step is the *interpretation* of the abstract bijection. Yoneda tells you the set, but you must then read off what each transformation *does*: for $\mathbf{Grp}$ the answer set is $U(\mathbb{Z}) = \mathbb{Z}$, and the transformation indexed by $n$ is the $n$-th power map $g \mapsto g^n$ — recognizing this concrete operation behind the abstract element is the payoff. Choosing the right representing object is what makes the codomain-evaluation easy.

---

# Legal Operations Used

1. **Operation 9 from the topic page (apply the Yoneda lemma to compute a natural transformation set).** We rewrite each domain as a hom-functor and read off $\mathrm{Nat} \cong F(A)$.

2. **Operation 3 from the topic page (use the universal element to interpret the transformation).** The element $\alpha_A(1_A) \in F(A)$ is unwound into the explicit operation the transformation performs.

---

# Hints

> [!note]- Hint 1
> $U : \mathbf{Grp} \to \mathbf{Set}$ is representable by $\mathbb{Z}$. So $\mathrm{Nat}(U, U) \cong \mathrm{Nat}(\mathbf{Grp}(\mathbb{Z}, -), U) \cong U(\mathbb{Z}) = \mathbb{Z}$.

> [!note]- Hint 2
> Each integer $n$ indexes a natural endomorphism. Which natural operation on group elements does $n \in \mathbb{Z} = U(\mathbb{Z})$ correspond to? Trace the Yoneda bijection: the element $n$ comes from the transformation $\Psi(n)_G(\varphi) = U(\varphi)(n)$, and a group homomorphism $\varphi : \mathbb{Z} \to G$ sends $n \mapsto \varphi(1)^n$.

> [!note]- Hint 3
> For $\mathbf{Ring}$, the representing object is $\mathbb{Z}[x]$ and $U(\mathbb{Z}[x]) = \mathbb{Z}[x]$ as a set, so $\mathrm{Nat}(U, U) \cong \mathbb{Z}[x]$ — one natural endomorphism per integer polynomial $p(x)$, acting by $r \mapsto p(r)$.

> [!note]- Hint 4
> For part 3, $F = \mathbf{Set}(B, -)$ so $F(A) = \mathbf{Set}(B, A)$, and $\mathrm{Nat}(\mathbf{Set}(A,-), \mathbf{Set}(B,-)) \cong \mathbf{Set}(B, A)$; the transformation indexed by $h : B \to A$ is precomposition $f \mapsto f \circ h$.

---

# Solution

In each part the move is identical: recognize the domain as a hom-functor, apply $\mathrm{Nat}(\mathcal{C}(A,-), F) \cong F(A)$, then interpret the resulting elements as concrete natural operations.

**Step 1: Natural endomorphisms of $U : \mathbf{Grp} \to \mathbf{Set}$.**

> [!note]- Derivation
> Since $U \cong \mathbf{Grp}(\mathbb{Z}, -)$, the Yoneda lemma gives $\mathrm{Nat}(U, U) \cong U(\mathbb{Z}) = \mathbb{Z}$. Unwinding: the element $n \in \mathbb{Z} = U(\mathbb{Z})$ corresponds to the transformation $\alpha^{(n)}$ with $\alpha^{(n)}_G(\varphi) = U(\varphi)(n)$ for $\varphi : \mathbb{Z} \to G$; since $\varphi(n) = \varphi(1)^n$, identifying $g = \varphi(1) \in U(G)$, we get $\alpha^{(n)}_G(g) = g^n$. So the natural endomorphisms of $U$ are exactly the **power maps** $g \mapsto g^n$, one per integer $n$. (Naturality of $g \mapsto g^n$ is automatic from Yoneda; one could check directly that homomorphisms preserve powers.)

**Step 2: Natural endomorphisms of $U : \mathbf{Ring} \to \mathbf{Set}$.**

> [!note]- Derivation
> Since $U \cong \mathbf{Ring}(\mathbb{Z}[x], -)$, the Yoneda lemma gives $\mathrm{Nat}(U, U) \cong U(\mathbb{Z}[x]) = \mathbb{Z}[x]$ (the underlying set of the polynomial ring). The polynomial $p(x) \in \mathbb{Z}[x]$ corresponds to the transformation $\alpha^{(p)}_R(r) = p(r)$ — the **polynomial map** $r \mapsto p(r)$. So natural endomorphisms of the underlying-set functor on rings are exactly evaluation of integer polynomials. (For instance $p(x) = x^2$ gives the squaring operation $r \mapsto r^2$, which is natural because ring homomorphisms preserve squares.)

**Step 3: Natural transformations between representables on $\mathbf{Set}$.**

> [!note]- Derivation
> With $F = \mathbf{Set}(B, -)$, the Yoneda lemma gives
> $$\mathrm{Nat}(\mathbf{Set}(A, -), \mathbf{Set}(B, -)) \cong F(A) = \mathbf{Set}(B, A).$$
> This is [[Thm - The Yoneda Embedding is Fully Faithful|full faithfulness]]: natural transformations between representables correspond to functions between the representing objects, *reversed*. The function $h : B \to A$ corresponds to the transformation $\alpha^{(h)}_X(f) = f \circ h$ — precomposition by $h$. So every natural transformation between covariant representables is precomposition by a fixed function, and there are exactly $|A|^{|B|}$ of them.

> [!note]- Complete formal solution
> Recognize each domain as a hom-functor and apply $\mathrm{Nat}(\mathcal{C}(A,-), F) \cong F(A)$. (1) $U \cong \mathbf{Grp}(\mathbb{Z}, -)$ gives $\mathrm{Nat}(U,U) \cong U(\mathbb{Z}) = \mathbb{Z}$, the transformation indexed by $n$ being the power map $g \mapsto g^n$. (2) $U \cong \mathbf{Ring}(\mathbb{Z}[x], -)$ gives $\mathrm{Nat}(U,U) \cong \mathbb{Z}[x]$, the polynomial $p$ acting by $r \mapsto p(r)$. (3) $\mathrm{Nat}(\mathbf{Set}(A,-), \mathbf{Set}(B,-)) \cong \mathbf{Set}(B,A)$, the function $h : B \to A$ acting by precomposition $f \mapsto f \circ h$. In each case the explicit operation is read off from the universal element $\alpha_A(1_A)$. $\blacksquare$

---

# Key Takeaways

**The Yoneda lemma converts a hard-looking computation (find all natural maps) into a trivial one (evaluate a functor at one object).** Counting or classifying natural transformations directly would require checking a naturality square for every morphism in the category — an infinite task. Yoneda collapses it to "what is $F(A)$?" the moment the domain is recognized as representable by $A$. The trigger is *any* request to find natural transformations out of a forgetful functor, an identity functor, or a hom-functor; the reaction is to rewrite the domain as $\mathcal{C}(A, -)$ and read off the answer as $F(A)$. This is the single most common use of the lemma in practice.

**Interpreting the abstract element is the real content, and it always means "trace where the universal element goes".** Yoneda hands you a *set* of transformations, but the insight is in identifying what each one *does*: the integer $n$ is the $n$-th power map, the polynomial $p$ is evaluation of $p$, the function $h$ is precomposition. The mechanical recipe is $\alpha = \Psi(a)$ with $\Psi(a)_X(f) = F(f)(a)$, and unwinding this for the specific $F$ produces the explicit formula. Mastering this unwinding — universal element in, concrete operation out — is what turns Yoneda from a slogan into a computational tool.

**"Natural operations are scarce" is the surprising upshot.** One might expect a forgetful functor to admit a wild variety of natural self-maps, but Yoneda pins them down exactly: only power maps on groups, only polynomial maps on rings, only precompositions between representable set-functors. There are no exotic natural operations hiding anywhere. This scarcity is what makes naturality such a strong constraint and is the reason categorical arguments are so rigid: once you demand naturality, the space of possibilities shrinks to a single hom-set or functor value. The same scarcity, applied to the identity functor and to forgetful functors, classifies all natural unary operations in algebra.
