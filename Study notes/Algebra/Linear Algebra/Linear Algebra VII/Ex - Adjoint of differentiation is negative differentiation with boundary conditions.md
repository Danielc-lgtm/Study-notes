---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Adjoint of a Linear Map"
  - "Def - Inner Product Space"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be the inner product space of complex polynomials of degree at most $n$ on $[0, 1]$, with inner product
$$\langle f, g \rangle = \int_0^1 f(x) \overline{g(x)} \, dx.$$
Let $D : V \to V$ be the differentiation operator $D f = f'$.

(a) Compute the [[Def - Adjoint of a Linear Map|adjoint]] $D^*$ explicitly, including any boundary contributions.

(b) Identify the [[Def - Subspace|subspace]] of $V$ on which $D^* = -D$ holds without boundary contributions.

(c) On the subspace of polynomials vanishing at both endpoints $0$ and $1$, is the operator $D^2 = D D$ self-adjoint?

---

**Recall:**

![[Def - Adjoint of a Linear Map#The Definition]]

For functions in $L^2$, **integration by parts** is the basic identity:
$$\int_0^1 f'(x) \overline{g(x)} \, dx = f(x) \overline{g(x)} \Big|_0^1 - \int_0^1 f(x) \overline{g'(x)} \, dx.$$
The boundary term $f(x) \overline{g(x)} \big|_0^1$ is the source of all the subtlety.

A subspace $W \leq V$ on which an operator $T$ is *symmetric* satisfies $\langle Tf, g \rangle = \langle f, Tg \rangle$ for $f, g \in W$. This is weaker than being self-adjoint as an unbounded operator (the full self-adjointness requires equality of certain *domains*).

---

# Convergent Strategy

**Problem class.** This is an adjoint computation for a differential operator, the prototype of operator-theoretic calculations on function spaces. The problem class is: given an explicit linear operator on a function space, integrate by parts to find the "formal adjoint" — the operator one would naively call $D^*$ — and then identify the boundary terms that distinguish the formal adjoint from the actual adjoint on the given inner product space.

**Assumption pattern.** The operator is $D = d/dx$ on polynomials on $[0, 1]$. The inner product is the standard $L^2$ inner product. The hypothesis to leverage is that integration by parts gives an explicit formula relating $\int (Df) \overline{g}$ and $\int f \overline{(Dg)}$, with a difference equal to a boundary term $[f \overline{g}]_0^1$.

**Theorem routing.** The route is direct application of integration by parts. From $\int (Df) \overline g = [f \overline g]_0^1 - \int f \overline{g'} = [f \overline g]_0^1 - \int f \overline{(Dg)}$. Rearranging, $\int (Df) \overline g + \int f \overline{(Dg)} = [f \overline g]_0^1$, equivalently $\langle Df, g \rangle = -\langle f, Dg \rangle + [f \overline g]_0^1$. So $D^* = -D + (\text{boundary contribution})$. The boundary contribution depends on the function space; on the *full* polynomial space it is nontrivial.

**Key decision point.** The non-obvious move is treating the "boundary terms" carefully. On the *full* polynomial space, the boundary contributions are non-zero and prevent $D^* = -D$. On the *subspace* of polynomials vanishing at endpoints, the boundary terms vanish and $D^* = -D$ holds. The decision is to specify *which* subspace makes the operator behave nicely, and then verify that the further operator $D^2$ on this subspace is self-adjoint.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra VII — §7 Operators on Inner Product Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Use the defining relation of the adjoint** — Compute $\langle Df, g \rangle$ and identify the resulting linear functional $f \mapsto \langle Df, g \rangle$ in the form $\langle f, T^* g \rangle$. The discovery of $T^* g$ comes from integration by parts.

2. **Integration by parts** — The fundamental identity for adjoints of differential operators, producing both the "formal adjoint" and the boundary contribution.

3. **Restrict to a subspace where boundary terms vanish** — Identify the natural domain (polynomials vanishing at endpoints) on which the formal adjoint is the true adjoint.

---

# Hints

> [!note]- Hint 1
> The fundamental tool is integration by parts: $\int_0^1 (Df) \overline g \, dx = [f \overline g]_0^1 - \int_0^1 f \overline{(Dg)} \, dx$. The boundary terms are the source of non-triviality.

> [!note]- Hint 2
> Rearrange integration by parts to see $\langle Df, g \rangle = -\langle f, Dg \rangle + [f \overline g]_0^1$. If you want this to equal $\langle f, T^* g \rangle$ for some operator $T^*$, the boundary term must vanish — or be encoded as part of $T^* g$ in some other way.

> [!note]- Hint 3
> On the *full* polynomial space $V$, the boundary terms generally do not vanish, so $D^*$ on $V$ is not simply $-D$. On the subspace $W = \{f \in V : f(0) = f(1) = 0\}$, the boundary terms vanish, and $D^* = -D$ holds *on this subspace*. The price of the simple formula is restricting the domain.

---

# Solution

The proof revolves around integration by parts and the resulting boundary term. The "formal adjoint" of $D$ is $-D$, but the actual adjoint on the full polynomial space includes a boundary contribution. On the subspace of polynomials vanishing at endpoints, the boundary term disappears and $D^* = -D$ becomes literally true.

**Part (a): Compute $\langle Df, g \rangle$ via integration by parts.**

$$\langle Df, g \rangle = \int_0^1 f'(x) \overline{g(x)} \, dx = [f(x) \overline{g(x)}]_0^1 - \int_0^1 f(x) \overline{g'(x)} \, dx.$$

> [!note]- Derivation
> Direct application of integration by parts to $\int_0^1 f'(x) \overline{g(x)} \, dx$. Differentiate the boundary product: $\frac{d}{dx}(f \overline g) = f' \overline g + f \overline{g'}$ (using that $\overline g$ is a polynomial whose derivative is $\overline{g'}$, since complex conjugation commutes with real differentiation). Integrate over $[0, 1]$: $\int_0^1 (f' \overline g + f \overline{g'}) = [f \overline g]_0^1$. Rearrange.

So $\langle Df, g \rangle = [f(x) \overline{g(x)}]_0^1 - \langle f, g' \rangle$. On the full polynomial space, the adjoint $D^*$ does not have a simple closed form because of the boundary term — the linear functional $f \mapsto \langle Df, g \rangle$ is *not* of the form $f \mapsto \langle f, T^* g \rangle$ for any operator $T^*$ defined only by its values on $g$, since the boundary term depends on $f$ as well.

To make $D^*$ well-defined as an operator on $V$, one must reinterpret. Specifically, on the polynomial space, the Riesz representation theorem still gives a unique vector $u_g \in V$ with $\langle Df, g \rangle = \langle f, u_g \rangle$ for all $f \in V$, and the assignment $g \mapsto u_g$ is the adjoint $D^*$. To compute $u_g$ explicitly: the boundary term $[f \overline g]_0^1 = f(1) \overline{g(1)} - f(0) \overline{g(0)}$ is a linear functional of $f$, and by Riesz it equals $\langle f, b_g \rangle$ for some unique polynomial $b_g$ depending on $g$. Then $D^* g = -g' + b_g$ (where $-g'$ is the "$-D$" part and $b_g$ is the boundary contribution).

**Part (b): Identify the subspace on which $D^* = -D$.**

On the subspace $W = \{f \in V : f(0) = f(1) = 0\}$ — polynomials vanishing at both endpoints — the boundary term $[f \overline g]_0^1$ vanishes for $f \in W$ regardless of $g$. So $\langle Df, g \rangle = -\langle f, g' \rangle = \langle f, -g' \rangle$ for $f \in W, g$ arbitrary. Hence on the subspace $W$, $D^* = -D$ acts as the negative-differentiation operator.

> [!note]- Derivation
> For $f \in W$, $f(0) = f(1) = 0$. Then $[f(x) \overline{g(x)}]_0^1 = f(1) \overline{g(1)} - f(0) \overline{g(0)} = 0 \cdot \overline{g(1)} - 0 \cdot \overline{g(0)} = 0$.
>
> So integration by parts simplifies to $\langle Df, g \rangle = -\langle f, g' \rangle = \langle f, -Dg \rangle$ for $f \in W$. This says: the adjoint of $D|_W$ (as a map from $W$ into the full space $V$) is $-D$ acting on the second slot — the operator $-D$ pulls back into $W$ when restricted appropriately. To make this a well-defined adjoint of an operator $W \to W$, we also need to restrict $g \in W$.
>
> On $W$, with $D : W \to V$ (note that $D$ does not in general map $W$ to $W$ — derivatives of polynomials vanishing at endpoints do not vanish at endpoints), the "adjoint" computation produces $-D$. To get $D^* = -D$ as operators $W \to W$, one would need $W$ to be $D$-invariant, which it is not. The clean statement is that $D$ on the larger space, restricted in this sense, has $-D$ as its formal action; the rigorous statement requires distinguishing operator domains carefully (a subtlety addressed in unbounded operator theory).

**Part (c): Is $D^2$ self-adjoint on $W$?**

$D^2 f = f''$ — the second derivative. Compute $\langle D^2 f, g \rangle$ for $f, g \in W$ via integration by parts *twice*:
$$\langle D^2 f, g \rangle = \int_0^1 f''(x) \overline{g(x)} \, dx = [f'(x) \overline{g(x)}]_0^1 - \int_0^1 f'(x) \overline{g'(x)} \, dx.$$
The boundary term $[f' \overline g]_0^1$ involves $g$, not $f$, at the endpoints. For $g \in W$, $g(0) = g(1) = 0$, so $[f' \overline g]_0^1 = 0$. Hence
$$\langle D^2 f, g \rangle = - \int_0^1 f'(x) \overline{g'(x)} \, dx.$$

Apply integration by parts again, this time on the $f'$ term:
$$-\int_0^1 f'(x) \overline{g'(x)} \, dx = -[f(x) \overline{g'(x)}]_0^1 + \int_0^1 f(x) \overline{g''(x)} \, dx = \int_0^1 f(x) \overline{g''(x)} \, dx = \langle f, D^2 g \rangle.$$
The boundary term $[f \overline{g'}]_0^1$ vanishes because $f \in W$ has $f(0) = f(1) = 0$.

So $\langle D^2 f, g \rangle = \langle f, D^2 g \rangle$ for $f, g \in W$. **$D^2$ is self-adjoint on $W$.**

> [!note]- Derivation
> The integration by parts on $f''$ produces the boundary term $[f' \overline g]_0^1$, which kills against $g \in W$ (since $g$ vanishes at endpoints — note $f'$ need not).
>
> The next integration by parts on the cross-derivative $\int f' \overline{g'}$ produces the boundary term $[f \overline{g'}]_0^1$, which kills against $f \in W$ (since $f$ vanishes at endpoints — $g'$ need not).
>
> The two integrations by parts effectively replace $\int f'' \overline g$ with $\int f \overline{g''}$ — the operator $D^2$ "passes through" to the second slot without boundary contributions, on the subspace $W$. This is precisely self-adjointness.

> [!note]- Complete formal solution
> Define $W = \{f \in V : f(0) = f(1) = 0\}$ and $D f = f'$.
>
> *(a)* By integration by parts, $\langle Df, g \rangle = [f \overline g]_0^1 - \langle f, Dg \rangle$ for any $f, g \in V$. On the full polynomial space, the boundary term is generally non-zero, so $D^*$ is the negative-differentiation operator $-D$ plus a boundary contribution.
>
> *(b)* On $W$, the boundary terms vanish: $[f \overline g]_0^1 = f(1) \overline{g(1)} - f(0) \overline{g(0)} = 0$ since $f \in W$. So $\langle Df, g \rangle = -\langle f, Dg \rangle = \langle f, -Dg \rangle$ for $f \in W$, $g \in V$. Restricting to $g \in W$ gives the formal statement $D^* = -D$ on $W$ (where the equality is formal because $D$ does not in general preserve $W$).
>
> *(c)* For $f, g \in W$, compute $\langle D^2 f, g \rangle$ by integrating by parts twice:
> $$\langle D^2 f, g \rangle = [f' \overline g]_0^1 - \langle Df, Dg \rangle = -\langle Df, Dg \rangle$$
> (boundary term vanishes since $g \in W$ has $g(0) = g(1) = 0$).
>
> $$-\langle Df, Dg \rangle = -([f \overline{g'}]_0^1 - \langle f, D^2 g \rangle) = \langle f, D^2 g \rangle$$
> (boundary term vanishes since $f \in W$ has $f(0) = f(1) = 0$).
>
> So $\langle D^2 f, g \rangle = \langle f, D^2 g \rangle$ for $f, g \in W$, hence $D^2$ is self-adjoint on $W$. $\blacksquare$

---

# Key Takeaways

**Boundary terms are the source of all adjoint subtlety on function spaces.** On a function space with inner product given by integration, the adjoint of a differential operator is computed by integration by parts, and the boundary terms are what distinguish the "formal adjoint" from the actual adjoint. On the full space, boundary terms generally do not vanish, and the adjoint includes a boundary contribution that is not a differential operator. On [[Def - Subspace|subspaces]] where the functions satisfy specific boundary conditions, the boundary terms vanish, and the formal adjoint becomes the actual adjoint. The choice of function space — equivalently, the choice of boundary conditions — determines the adjoint. This is the heart of operator theory on function spaces: the "operator" is incomplete without specifying its domain.

**Self-adjoint differential operators require boundary conditions.** The Laplacian $-\Delta$ on $L^2$ is self-adjoint only with appropriate boundary conditions (Dirichlet $u = 0$ on the boundary, Neumann $\partial u / \partial n = 0$ on the boundary, periodic, etc.). Each set of boundary conditions gives a different self-adjoint operator with a different spectrum. On $[0, 1]$ with Dirichlet boundary conditions, $-D^2$ has eigenvalues $(n \pi)^2$ for $n = 1, 2, \ldots$; with Neumann, eigenvalues $(n \pi)^2$ for $n = 0, 1, 2, \ldots$; with periodic, eigenvalues $(2 n \pi)^2$ for $n = 0, \pm 1, \pm 2, \ldots$. The spectra differ — and so do the eigenfunctions, the heat kernels, and every physical phenomenon governed by the operator.

**The formal computation extends to general PDE operators.** The technique used here — integration by parts to find the formal adjoint — generalises to PDE operators in higher [[Def - Dimension|dimensions]] via Green's identity, which is the multidimensional integration by parts. The Laplacian $-\Delta = -\sum \partial^2 / \partial x_i^2$ has formal adjoint equal to itself (every second-order derivative is its own formal self-adjoint by two integrations by parts). The first-order operators (like the gradient $\nabla$ or the divergence $\nabla \cdot$) have non-self-adjoint formal adjoints: $\nabla^* = -\nabla \cdot$ and $(\nabla \cdot)^* = -\nabla$. The whole theory of elliptic operators and Hodge theory rests on these formal adjoint computations.
