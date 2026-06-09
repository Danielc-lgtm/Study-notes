---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Integral Element and Integral Extension"
  - "Def - Algebraic Integer and Minimal Polynomial"
  - "Thm - The Integral Closure is a Subring"
  - "Thm - Characterizations of Integrality (Module-Finite Criterion)"
  - "Thm - Transitivity of Integrality and Finiteness"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $a, b \in \mathbb{C}$ be [[Def - Algebraic Integer and Minimal Polynomial|algebraic integers]] — each a root of a monic polynomial with integer coefficients. Prove that $a + b$ and $ab$ are algebraic integers. Deduce that the set of all algebraic integers in $\mathbb{C}$ forms a ring.

Then (Example Sheet 1 Q15(b)): describe an *algorithm* that, given monic $f, g \in \mathbb{Z}[T]$ with $f(a) = g(b) = 0$, produces monic $p, q \in \mathbb{Z}[T]$ with $p(a + b) = 0$ and $q(ab) = 0$.

**Recall:**

The objects in play are integral elements (algebraic integers), the module-finite criterion, transitivity of finiteness, and the integral-closure-is-a-subring theorem.

![[Def - Algebraic Integer and Minimal Polynomial#The Definition]]

An [[Def - Algebraic Integer and Minimal Polynomial|algebraic integer]] is exactly an element of $\mathbb{C}$ [[Def - Integral Element and Integral Extension|integral over ℤ]].

![[Thm - The Integral Closure is a Subring#Statement]]

![[Thm - Characterizations of Integrality (Module-Finite Criterion)#Statement]]

The key equivalence: $x$ is integral over $\mathbb{Z}$ iff $\mathbb{Z}[x]$ is a finitely generated $\mathbb{Z}$-module, iff $x$ lies in some finite faithful module.

---

# Convergent Strategy

**Problem class.** This is the *flagship application of the module-finite criterion*: proving a closure property (sums and products of integral elements are integral) where no direct formula for the combined equation is available. It is the proof that $\mathcal{O} = \{$algebraic integers$\}$ is a ring, and it drills operation 2 (work inside $A[x, y]$) from the [[Commutative Algebra VI — Integral Extensions#Legal Operations|topic page]].

**Assumption pattern.** The leverable fact is that $a$ and $b$ are *each* integral — so $\mathbb{Z}[a]$ and $\mathbb{Z}[b]$ are each finite $\mathbb{Z}$-modules. The trigger for the criterion is "I have integral elements and want a combination to be integral, but combining the monic equations has no formula". The recognition is that finiteness is the right currency: put $a$ and $b$ into one finite module.

**Theorem routing.** The route is: $a$ integral $\Rightarrow \mathbb{Z}[a]$ finite ([[Thm - Characterizations of Integrality (Module-Finite Criterion)|criterion]]); $b$ integral over $\mathbb{Z}$ hence over $\mathbb{Z}[a]$ $\Rightarrow \mathbb{Z}[a, b]$ finite over $\mathbb{Z}[a]$; [[Thm - Transitivity of Integrality and Finiteness|transitivity]] $\Rightarrow \mathbb{Z}[a, b]$ finite over $\mathbb{Z}$; then $a + b, ab \in \mathbb{Z}[a, b]$, a finite faithful module, so they are integral by the criterion again. This is precisely the proof of [[Thm - The Integral Closure is a Subring]] specialised to $\mathbb{Z} \subseteq \mathbb{C}$.

**Key decision point.** The decisive move is *refusing to construct the combined equation* and instead producing the *module* $\mathbb{Z}[a, b]$. For the algorithm part, the non-obvious choice is realising the combined monic polynomial concretely as a *characteristic polynomial*: $a + b$ and $ab$ are eigenvalues of $a \otimes 1 + 1 \otimes b$ and $a \otimes b$ acting on $\mathbb{Z}[a] \otimes \mathbb{Z}[b]$, so their monic equations are the characteristic polynomials of explicit integer matrices (Kronecker sum and Kronecker product of companion matrices).

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra VI — Integral Extensions#Legal Operations|the topic page's Legal Operations]]:

1. **Turn monic equations into finite modules (operation 1).** Each of $\mathbb{Z}[a]$, $\mathbb{Z}[b]$ is finite because $a, b$ are integral.

2. **Prove closure under $+, \times$ inside $\mathbb{Z}[a, b]$ (operation 2).** Place $a, b$ in one finite module and integralise everything in it at once.

3. **Stack finiteness through a tower (operation 3).** $\mathbb{Z} \subseteq \mathbb{Z}[a] \subseteq \mathbb{Z}[a, b]$, with each step finite; transitivity assembles finiteness over $\mathbb{Z}$.

4. **Realise the combined equation as a characteristic polynomial.** For the algorithm, exhibit $a + b$, $ab$ as eigenvalues of integer matrices (Kronecker sum/product of companion matrices), whose characteristic polynomials are the desired monic $p, q$.

---

# Hints

> [!note]- Hint 1
> Do *not* try to write down a monic polynomial killing $a + b$ from those killing $a$ and $b$ — there is no simple formula. Instead, recall the operational meaning of "integral": $x$ integral over $\mathbb{Z}$ $\iff \mathbb{Z}[x]$ is a *finite* $\mathbb{Z}$-module. What finite module naturally contains both $a$ and $b$ (and hence $a + b$ and $ab$)?

> [!note]- Hint 2
> Consider $\mathbb{Z}[a, b]$. Show it is a finite $\mathbb{Z}$-module by building the tower $\mathbb{Z} \subseteq \mathbb{Z}[a] \subseteq \mathbb{Z}[a, b]$: each step is finite (because the new generator is integral), and finite-over-finite is finite. Then $a + b$ and $ab$ live in this finite module — apply the module-finite criterion to conclude they are integral.

> [!note]- Hint 3
> For the *algorithm*: if $f$ has degree $m$ and $g$ has degree $n$, then $\mathbb{Z}[a]$ has $\mathbb{Z}$-basis $1, a, \dots, a^{m-1}$ and $\mathbb{Z}[b]$ has basis $1, b, \dots, b^{n-1}$, so $\mathbb{Z}[a, b]$ is spanned by the $mn$ products $a^i b^j$. Multiplication by $a + b$ (resp. $ab$) is a $\mathbb{Z}$-linear map on this rank-$mn$ module — write its matrix and take the characteristic polynomial. Concretely these are the **Kronecker sum** $C_f \otimes I_n + I_m \otimes C_g$ and **Kronecker product** $C_f \otimes C_g$ of the companion matrices.

---

# Solution

The plan: prove the closure abstractly by the module-finite criterion (put $a, b$ in the finite module $\mathbb{Z}[a, b]$, which integralises $a + b, ab$), then make the proof *constructive* by realising the combined monic polynomials as characteristic polynomials of explicit integer matrices. The whole point is that the existence of the equation comes from finiteness, while the algorithm comes from writing "multiply by $a+b$" as a matrix.

**Step 1: $\mathbb{Z}[a, b]$ is a finite $\mathbb{Z}$-module.**

Build the tower $\mathbb{Z} \subseteq \mathbb{Z}[a] \subseteq \mathbb{Z}[a, b]$; each step is finite, so the whole is finite over $\mathbb{Z}$.

> [!note]- Derivation
> Since $a$ is integral over $\mathbb{Z}$, satisfying a monic $f$ of degree $m$, the [[Thm - Characterizations of Integrality (Module-Finite Criterion)|module-finite criterion]] gives $\mathbb{Z}[a] = \mathbb{Z} + \mathbb{Z}a + \cdots + \mathbb{Z}a^{m-1}$, a finite $\mathbb{Z}$-module (spanned by $m$ elements).
>
> Since $b$ is integral over $\mathbb{Z}$, it is integral over the larger ring $\mathbb{Z}[a]$ (the same monic $g \in \mathbb{Z}[T] \subseteq \mathbb{Z}[a][T]$ works). So $\mathbb{Z}[a][b] = \mathbb{Z}[a, b] = \mathbb{Z}[a] + \mathbb{Z}[a]\,b + \cdots + \mathbb{Z}[a]\,b^{n-1}$ is a finite $\mathbb{Z}[a]$-module ($n = \deg g$).
>
> By [[Thm - Transitivity of Integrality and Finiteness|transitivity of finiteness]], $\mathbb{Z}[a, b]$ is a finite $\mathbb{Z}$-module, spanned by the $mn$ products $\{a^i b^j : 0 \leq i < m,\ 0 \leq j < n\}$.

**Step 2: $a + b$ and $ab$ are integral over $\mathbb{Z}$.**

They lie in the finite faithful module $\mathbb{Z}[a, b]$, which they stabilise; the criterion makes them integral.

> [!note]- Derivation
> The elements $a + b$ and $ab$ both lie in the ring $\mathbb{Z}[a, b]$. This ring is a finite $\mathbb{Z}$-module (Step 1), it contains $1$ (so it is faithful as a $\mathbb{Z}[a+b]$- and $\mathbb{Z}[ab]$-module), and it is stabilised by multiplication by any of its elements (it is a ring). By condition (4) of the [[Thm - Characterizations of Integrality (Module-Finite Criterion)|module-finite criterion]], *every* element of $\mathbb{Z}[a, b]$ is integral over $\mathbb{Z}$ — in particular $a + b$ and $ab$. (This is exactly [[Thm - The Integral Closure is a Subring|"the integral closure is a subring"]] for $\mathbb{Z} \subseteq \mathbb{C}$.)
>
> Since $a, b$ were arbitrary algebraic integers and the algebraic integers contain $0, 1$ and are closed under $+, -, \times$, they form a *subring* of $\mathbb{C}$.

**Step 3: The algorithm — combined equations as characteristic polynomials.**

Multiplication by $a + b$ (resp. $ab$) on the rank-$mn$ module $\mathbb{Z}[a, b]$ is an integer matrix; its characteristic polynomial is the desired monic $p$ (resp. $q$).

> [!note]- Derivation
> Let $C_f \in M_m(\mathbb{Z})$ be the companion matrix of $f$ (so $C_f$ represents "multiply by $a$" on $\mathbb{Z}[a]$ in the basis $1, a, \dots, a^{m-1}$, and $a$ is an eigenvalue of $C_f$). Likewise $C_g \in M_n(\mathbb{Z})$ for $g$ and $b$.
>
> On the tensor product $\mathbb{Z}[a] \otimes_{\mathbb{Z}} \mathbb{Z}[b] \cong \mathbb{Z}^{mn}$ (with basis $a^i \otimes b^j$, matching $a^i b^j$), the operators behave as:
> - multiplication by $a + b$ acts as the **Kronecker sum** $M_+ = C_f \otimes I_n + I_m \otimes C_g$, whose eigenvalues are $\lambda_i + \mu_j$ over all eigenvalues $\lambda_i$ of $C_f$ and $\mu_j$ of $C_g$ — in particular $a + b$ is an eigenvalue;
> - multiplication by $ab$ acts as the **Kronecker product** $M_\times = C_f \otimes C_g$, whose eigenvalues are $\lambda_i \mu_j$ — in particular $ab$ is an eigenvalue.
>
> (These are the eigenvalue facts of Example Sheet 1 Q15(a): $A \otimes B$ has eigenvalue $\lambda\mu$, and $A \otimes I + I \otimes B$ has eigenvalue $\lambda + \mu$.)
>
> Set $p(T) = \det(T I_{mn} - M_+)$ and $q(T) = \det(T I_{mn} - M_\times)$. Both are **monic** of degree $mn$ with **integer** coefficients (the matrices $M_+, M_\times$ have integer entries). By Cayley–Hamilton, $p(M_+) = 0$ and $q(M_\times) = 0$; since $a + b$ is an eigenvalue of $M_+$ and $ab$ of $M_\times$, we have $p(a + b) = 0$ and $q(ab) = 0$. This is an explicit algorithm: form the companion matrices, compute the Kronecker sum/product, take the characteristic polynomial.

> [!note]- Complete formal solution
> **Claim.** If $a, b \in \mathbb{C}$ are algebraic integers, so are $a + b$ and $ab$; the algebraic integers form a ring; and the combined monic polynomials are computable.
>
> Since $a$ is integral over $\mathbb{Z}$ (monic $f$, degree $m$), $\mathbb{Z}[a] = \sum_{i<m}\mathbb{Z}a^i$ is finite over $\mathbb{Z}$. Since $b$ is integral over $\mathbb{Z}$, hence over $\mathbb{Z}[a]$, $\mathbb{Z}[a,b] = \sum_{j<n}\mathbb{Z}[a]\,b^j$ is finite over $\mathbb{Z}[a]$ ($n = \deg g$). By [[Thm - Transitivity of Integrality and Finiteness|transitivity]], $\mathbb{Z}[a,b]$ is a finite $\mathbb{Z}$-module spanned by $\{a^i b^j\}_{i<m, j<n}$.
>
> The elements $a+b, ab \in \mathbb{Z}[a,b]$, a finite faithful module they stabilise, so by the [[Thm - Characterizations of Integrality (Module-Finite Criterion)|module-finite criterion]] (condition (4)) they are integral over $\mathbb{Z}$ — algebraic integers. As $0, 1$ are algebraic integers and the set is closed under $+, -, \times$, it is a subring of $\mathbb{C}$.
>
> *Algorithm.* With $C_f, C_g$ the companion matrices of $f, g$, set $M_+ = C_f \otimes I_n + I_m \otimes C_g$ and $M_\times = C_f \otimes C_g$ (integer matrices). Then $p(T) = \det(TI - M_+)$ and $q(T) = \det(TI - M_\times)$ are monic integer polynomials of degree $mn$ with $p(a+b) = 0$, $q(ab) = 0$, since $a+b$, $ab$ are eigenvalues of $M_+$, $M_\times$ respectively. $\blacksquare$

---

# Key Takeaways

**The hallmark move: prove a closure property by exhibiting a module, never a formula.** When asked to show that some combination of integral elements is integral, the instinct to manipulate the given monic equations is a dead end — there is no closed-form polynomial for $a + b$ in terms of those for $a$ and $b$ (its degree can be as large as $mn$). The correct and far easier move is to *place all the elements in one finite module* and invoke the [[Thm - Characterizations of Integrality (Module-Finite Criterion)|module-finite criterion]], which integralises *every* element of that module at once. This is the single most important technique in the chapter: convert "satisfies a monic equation" (an existence statement about one element) into "lives in a finite module" (a structural statement closed under operations). The trigger is "combine integral things"; the reaction is "build $\mathbb{Z}[a, b]$ and apply the criterion".

**Existence (the criterion) and construction (the characteristic polynomial) are different jobs.** The module argument *proves* the combined monic polynomial exists but tells you nothing about it. To actually *compute* it, you realise the combination as an operator on the finite module and take its characteristic polynomial — and the eigenvalue calculus of the Kronecker sum and product ($\lambda + \mu$ for $A \otimes I + I \otimes B$, $\lambda\mu$ for $A \otimes B$) gives explicit integer matrices whose characteristic polynomials kill $a + b$ and $ab$. This is the constructive content of "integral $=$ eigenvalue of an integer matrix": every algebraic integer is an eigenvalue of an integer matrix (its companion matrix), and combinations of algebraic integers are eigenvalues of the corresponding combinations of matrices. When a problem asks for an *algorithm* rather than mere existence, switch from the module to its matrix representation.

**This is the foundational fact that $\mathcal{O}_K$ is a ring — provable no other way.** The result "algebraic integers form a ring" is the bedrock on which all of algebraic number theory rests: the ring of integers $\mathcal{O}_K$ of a number field is *defined* as the algebraic integers in $K$, and that it is closed under addition and multiplication is exactly this theorem. There is no elementary proof — you cannot, for instance, see that $\sqrt2 + \sqrt[3]3$ is an algebraic integer by guessing its degree-$6$ minimal polynomial without the module argument or the resultant. This is why the module-finite criterion, abstract as it looks, is *the* indispensable tool: it is the only route to the ring structure that the entire subject takes for granted. The same argument, run over a general base, gives that the integral closure of any ring in any extension is a ring ([[Thm - The Integral Closure is a Subring]]).
