---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Algebra for a Monad"
  - "Def - Monad and Comonad"
  - "Def - Vector Space"
  - "Def - Free Module"
tags: [category-theory, foundations]
---

# Problem Statement

Fix a field $k$. Let $T : \mathbf{Set} \to \mathbf{Set}$ be the **free $k$-vector-space monad**: $T(X) = k[X]$ is the set of finite formal $k$-linear combinations $\sum_{x} c_x \cdot x$ of elements of $X$ (only finitely many $c_x \neq 0$), $\eta_X(x) = 1\cdot x$ (the basis element $x$), and $\mu_X : k[k[X]] \to k[X]$ "evaluates a formal combination of formal combinations" by expanding and collecting like terms.

Prove that the [[Def - Algebra for a Monad|Eilenberg–Moore category]] $\mathbf{Set}^T$ is equivalent to $\mathbf{Vect}_k$, the category of $k$-[[Def - Vector Space|vector spaces]] and linear maps.

**Recall:**

![[Def - Algebra for a Monad#The Definition]]

A $k$-[[Def - Vector Space|vector space]] is an abelian group $V$ with a scalar action $k \times V \to V$ that is associative, unital, and bilinear. The [[Def - Free Module|free vector space]] $k[X]$ on a set $X$ has $X$ as a basis; any function $X \to V$ extends uniquely to a linear map $k[X] \to V$.

---

# Convergent Strategy

**Problem class:** An "identify the category of algebras" problem, the same shape as [[Ex - Algebras for the free-group monad are groups]] but with linear combinations instead of words. The structure map evaluates a formal linear combination.

**Assumption pattern:** $T(X) = k[X]$ is "formal linear combinations," so a structure map $a : k[A] \to A$ is "actually compute the linear combination" (legal operation 3). The free-vector-space universal property is the adjunction (operation 1).

**Theorem routing:** Route through [[Def - Algebra for a Monad]]: extract addition and scalar multiplication from $a$ on two-term and scaled-one-term combinations, use the unit law to fix $a$ on basis elements, and the associativity law to force linearity and the vector-space axioms. Then exhibit mutually inverse functors with $\mathbf{Vect}_k$.

**Key decision point:** The crux is that the structure map is forced to be *the* linear-combination evaluation, so the addition $a(x + y)$ and scaling $a(c\cdot x)$ inherit commutativity, associativity, and distributivity directly from the formal arithmetic of $k[A]$ — there is no separate axiom to impose. Unlike the group case, no "reduction" is needed; the ring structure of $k$ is carried inside the monad.

---

# Legal Operations Used

1. **Operation 3 from the topic page (build the structure map of an algebra).** Read $a : k[A] \to A$ as "evaluate the formal linear combination," extracting $+$ and scalar multiplication.

2. **Operation 1 from the topic page (read a monad off an adjunction).** $T = UF$ for the free–forgetful adjunction $\mathbf{Set}\rightleftarrows\mathbf{Vect}_k$.

3. **Operation 5 from the topic page (Barr–Beck recognition), in spirit.** Concluding $\mathbf{Set}^T \simeq \mathbf{Vect}_k$ is the monadicity of $\mathbf{Vect}_k \to \mathbf{Set}$.

---

# Hints

> [!note]- Hint 1
> A structure map $a : k[A] \to A$ takes a formal combination $\sum c_x x$ and returns an element of $A$. Define $u + v := a(1\cdot u + 1\cdot v)$ and $c\cdot v := a(c\cdot v)$ (the scaled single term). The unit law gives $a(1\cdot x) = x$.

> [!note]- Hint 2
> The associativity law $a\circ\mu = a\circ Ta$ forces $a$ to respect formal arithmetic: $a$ of a combination of combinations equals the combination of the evaluations. So $a\big(\sum_i c_i (\text{formal } w_i)\big) = \sum_i c_i\, a(w_i)$, i.e. $a$ is linear.

> [!note]- Hint 3
> The vector-space axioms (commutativity and associativity of $+$, distributivity, $1\cdot v = v$) are inherited from the corresponding identities *among formal combinations in $k[A]$*, transported through $a$ by the associativity law. You do not impose them separately.

> [!note]- Hint 4
> The inverse functor sends $V \in \mathbf{Vect}_k$ to $(UV, a_V)$ where $a_V : k[UV] \to UV$ actually evaluates a formal combination of vectors — the underlying map of the counit $\varepsilon_V : k[UV] \to V$.

---

# Solution

The plan: extract $+$ and scalar action from $a$ (Step 1), use the associativity law to make $a$ the linear-combination evaluation (Step 2), inherit the vector-space axioms from formal arithmetic in $k[A]$ (Step 3), and build the equivalence with $\mathbf{Vect}_k$ (Step 4). The point is that $k$'s arithmetic lives inside the monad, so the axioms come for free.

**Step 1: Extract the vector-space operations.**

> [!note]- Derivation
> Let $(A, a)$ be a $T$-algebra, $a : k[A] \to A$. Define addition and scalar multiplication by
> $$u + v := a(1\cdot u + 1\cdot v), \qquad c \cdot v := a(c\cdot v),$$
> where the right-hand sides are formal combinations in $k[A]$ evaluated by $a$. The unit law $a\circ\eta_A = 1_A$ gives $a(1\cdot x) = x$ for each $x \in A$ (each basis element evaluates to itself), and in particular $0\cdot v$ and the empty combination give a zero element $0 := a(0)$.

**Step 2: The associativity law makes $a$ linear.**

> [!note]- Derivation
> The algebra associativity law $a\circ\mu_A = a\circ Ta$ says: for a formal combination of formal combinations $\Omega = \sum_i c_i\, w_i \in k[k[A]]$ (each $w_i \in k[A]$),
> $$a\big(\mu_A(\Omega)\big) = a\big(Ta(\Omega)\big) = a\Big(\sum_i c_i\, a(w_i)\Big),$$
> where $\mu_A(\Omega)$ is the expanded-and-collected combination and $Ta(\Omega) = \sum_i c_i\, a(w_i)$ replaces each inner $w_i$ by its evaluation. Reading the right side via Step 1, this is $\sum_i c_i\, a(w_i)$ computed with the extracted $+$ and $\cdot$. So
> $$a\Big(\sum_i c_i\, w_i\Big) = \sum_i c_i\, a(w_i),$$
> i.e. $a$ is $k$-linear: it evaluates a formal combination to the corresponding actual combination.

**Step 3: Inherit the vector-space axioms.**

> [!note]- Derivation
> All axioms now follow by transporting identities among formal combinations through the linear map $a$.
>
> *Commutativity:* $u + v = a(1u + 1v) = a(1v + 1u) = v + u$, since $1u+1v = 1v+1u$ as formal combinations in $k[A]$.
>
> *Associativity:* $(u+v)+w = a\big(1\cdot a(1u+1v) + 1w\big) = a(1u+1v+1w) = u+(v+w)$ by Step 2 applied to the nested combination.
>
> *Scalar axioms:* $1\cdot v = a(1\cdot v) = v$; $c\cdot(d\cdot v) = a(c\cdot a(d v)) = a((cd)v) = (cd)\cdot v$ (since $c(dv) = (cd)v$ in $k[A]$); and distributivity $c\cdot(u+v) = a(c(1u+1v)) = a(cu+cv) = c\cdot u + c\cdot v$, $(c+d)\cdot v = a((c+d)v) = a(cv+dv) = c\cdot v + d\cdot v$.
>
> Each is an identity of formal combinations in $k[A]$ pushed through the linear $a$. So $(A, +, \cdot, 0)$ is a $k$-[[Def - Vector Space|vector space]].

**Step 4: The equivalence $\mathbf{Set}^T \simeq \mathbf{Vect}_k$.**

> [!note]- Derivation
> Define $\Phi : \mathbf{Set}^T \to \mathbf{Vect}_k$ by $\Phi(A,a) = (A,+,\cdot,0)$. A $T$-algebra morphism $f$ satisfies $f\circ a = b\circ Tf$; on two-term combinations this gives $f(u+v) = f(u)+f(v)$ and on scaled terms $f(cv) = cf(v)$, so $f$ is linear. Define $\Psi : \mathbf{Vect}_k \to \mathbf{Set}^T$ by $\Psi(V) = (UV, a_V)$, $a_V$ the underlying map of the counit $\varepsilon_V : k[UV]\to V$ (genuine evaluation of a formal combination of vectors), whose algebra laws hold because $\varepsilon$ is linear and satisfies the triangle identities. Then $\Phi\Psi = 1$ (extracting $+,\cdot$ from $a_V$ recovers $V$) and $\Psi\Phi\cong 1$ (the evaluation map of the extracted space equals $a$ by Step 2). Hence $\mathbf{Set}^T \simeq \mathbf{Vect}_k$.

> [!note]- Complete formal solution
> For a $T$-algebra $(A,a)$ with $a : k[A]\to A$, set $u+v = a(1u+1v)$, $c\cdot v = a(cv)$, $0 = a(0)$. The unit law gives $a(1x) = x$; the associativity law gives $a(\sum c_i w_i) = \sum c_i a(w_i)$ (linearity of $a$). Every vector-space axiom is an identity of formal combinations in $k[A]$ transported through the linear $a$ (commutativity, associativity, $1\cdot v = v$, distributivity). So $(A,+,\cdot)$ is a $k$-vector space. The functors $\Phi(A,a) = (A,+,\cdot)$ and $\Psi(V) = (UV,\varepsilon_V)$ are mutually inverse, and morphisms match (the algebra square is linearity). Hence $\mathbf{Set}^T \simeq \mathbf{Vect}_k$. $\blacksquare$

> [!tip] Same argument over any ring
> Replacing $k$ by an arbitrary [[Def - Ring|ring]] $R$ gives the free $R$-module monad $X\mapsto R[X]$, whose algebras are $R$-[[Def - Module|modules]] by the identical argument. The field case is not special; the linear-combination evaluation works over any ring of scalars. This is why $\mathbf{Mod}_R \to \mathbf{Set}$ is monadic for every $R$.

---

# Key Takeaways

**When the monad carries a ring's arithmetic, the algebra axioms are inherited for free.** The contrast with [[Ex - Algebras for the free-group monad are groups|the free-group case]] is instructive: there, the inverse axiom had to be *manufactured* from the reduction relation $xx^{-1}\to\varnothing$ built into the syntax. Here, the entire arithmetic of $k$ — commutativity, distributivity, scalar associativity — already lives among the formal combinations in $k[A]$, so every vector-space axiom is just a true identity of formal combinations pushed through the linear evaluation map $a$. The transferable lesson is that the *equations* a monad's algebras satisfy are exactly the equations holding in the free objects, so a monad built from a ring's formal combinations gives algebras inheriting that ring's arithmetic without extra work.

**Linearity of the structure map is the associativity law in disguise.** The single computational step that does everything is recognizing that the algebra associativity law $a\circ\mu = a\circ Ta$ *is* the statement that $a$ is $k$-linear: $a(\sum c_i w_i) = \sum c_i a(w_i)$. Once $a$ is linear, it is determined by its values on the basis (the generators), which the unit law fixes to be the identity. So a $T$-algebra is nothing but "a set $A$ with a linear evaluation $k[A]\to A$ fixing the generators" — which is precisely the data of a vector-space structure on $A$. The diagnostic for any free-linear monad is: the structure map is forced to be linear, hence is the linear-combination evaluation, hence the algebras are the corresponding modules.

**Equivalence, not isomorphism, because the algebra and target objects differ.** The conclusion $\mathbf{Set}^T \simeq \mathbf{Vect}_k$ is an *equivalence*: a $T$-algebra is "a set with extra structure," a vector space is "a set with extra structure," and the functors match them up, but a given vector space and its algebra presentation are not literally the same object. This contrasts with [[Ex - The Kleisli category of the powerset monad is Rel|$\mathbf{Set}_P \cong \mathbf{Rel}$]], which is an *isomorphism* because the objects are literally the same sets. The general pattern: identifying a category of algebras with a known algebraic category yields an equivalence (objects are matched up to iso), while identifying a Kleisli category with a known category of generalized maps often yields an isomorphism on the nose (objects are identical). Recognizing which you are proving sets the right target.
