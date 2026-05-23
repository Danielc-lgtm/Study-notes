---
type: definition
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Euclidean Domain"
  - "Def - Principal Ideal Domain"
  - "Def - Unique Factorization Domain"
  - "Def - Irreducible and Prime Elements"
tags: [algebra, ring-theory]
---

# Notation

The **Gaussian integers** are written $\mathbb{Z}[i]$, the set of complex numbers with integer real and imaginary parts. The symbol $i$ denotes a fixed square root of $-1$, so $i^2 = -1$. For $z = a + bi$ we write $\bar{z} = a - bi$ for the complex conjugate and $N(z)$ for the **norm**, $N(z) = z\bar{z} = a^2 + b^2 = |z|^2$. The notation $\leq$ means "is a subring of", $R^\times$ denotes the group of units of a ring $R$, and $u \sim v$ means $u$ and $v$ are **associates** ($v = uw$ for some unit $w$). For a prime $p$, the congruence $p \equiv 1 \pmod 4$ means $p$ leaves remainder $1$ on division by $4$. The full symbol registry for this chapter is on the parent page [[Rings III — §2.5–2.6]].

---

# Axiom Motivation

There is nothing to *invent* in the definition of $\mathbb{Z}[i]$ itself — it is simply the smallest [[Def - Subring|subring]] of $\mathbb{C}$ containing $i$, namely all $\mathbb{Z}$-linear combinations of $1$ and $i$. The genuine design question is the **norm**: why attach the function $N(a+bi) = a^2 + b^2$ to this [[Def - Ring|ring]], and why is it *this* function and not a nearby variant? Understanding that is understanding why the Gaussian integers are tractable at all.

Start from the problem. You have a new ring $\mathbb{Z}[i]$ and you want to do arithmetic in it: factor elements, find the units, decide irreducibility. In $\mathbb{Z}$ all of this is controlled by *size* — the absolute value $|n|$ — because $|n|$ is multiplicative, because it is a non-negative integer (so it cannot descend forever), and because $|n| = 1$ exactly for the units $\pm 1$. We want to import that machinery. So the desideratum is: a function $\mathbb{Z}[i] \to \mathbb{Z}_{\geq 0}$ that is **multiplicative** and that **detects units**. The naive candidate, the complex modulus $|a+bi| = \sqrt{a^2+b^2}$, is multiplicative and detects units — but it is irrational, it lands in $\mathbb{R}_{\geq 0}$, not $\mathbb{Z}_{\geq 0}$, and a real-valued size gives no terminating descent. The fix is forced: square it. The function $N(z) = |z|^2 = a^2 + b^2$ is the unique repair that keeps multiplicativity, keeps unit-detection, and lands in the non-negative integers.

Check that $N$ does what we asked. It is **multiplicative** because the complex modulus is: $N(zw) = |zw|^2 = |z|^2|w|^2 = N(z)N(w)$. Equivalently, and this is worth seeing algebraically without invoking $\mathbb{C}$, the Brahmagupta–Fibonacci identity
$$(a^2+b^2)(c^2+d^2) = (ac-bd)^2 + (ad+bc)^2$$
*is* the statement $N(z)N(w) = N(zw)$ written out in coordinates. It is **integer-valued and non-negative** by construction. And it **detects units**: if $z$ is a unit with inverse $z^{-1}$, then $N(z)N(z^{-1}) = N(1) = 1$, and since both factors are positive integers, $N(z) = 1$. Conversely if $N(z) = 1$ then $z\bar z = 1$, so $\bar z$ is an inverse and $z$ is a unit. So *unit $\iff$ norm $1$*, and solving $a^2 + b^2 = 1$ over $\mathbb{Z}$ gives exactly $\pm 1, \pm i$.

What breaks under a different choice? If you took $N(a+bi) = a + b$ you would lose non-negativity and multiplicativity at once — it is useless. If you took $|a+bi|$ itself you would lose the integer codomain, and with it the [[Def - Euclidean Domain|Euclidean]] descent argument that needs a well-ordered range. If you took $a^2 - b^2$ — the norm form for $\mathbb{Z}[\sqrt 2]$ — it is multiplicative but *indefinite*, so it cannot detect units by size and cannot drive a Euclidean algorithm. The positive-definite quadratic form $a^2 + b^2$ is the only choice meeting every requirement, and that is precisely why it is the norm: it is the multiplicative, unit-detecting, integer-valued size function, and there is no other.

The payoff that certifies the definition is the chain of theorems it unlocks. With $N$ as a [[Def - Euclidean Domain|Euclidean function]], $\mathbb{Z}[i]$ is a Euclidean domain (every complex number is within distance $< 1$ of a lattice point, so division with remainder works); hence a [[Def - Principal Ideal Domain|principal ideal domain]]; hence a [[Def - Unique Factorization Domain|unique factorization domain]] in which [[Def - Irreducible and Prime Elements|irreducible and prime coincide]]. Every link in that chain consumes the multiplicativity and integer-valuedness of $N$. Change the norm and the chain snaps.

---

# The Definition

The **Gaussian integers** form the subring
$$\mathbb{Z}[i] \;=\; \{\, a + bi : a, b \in \mathbb{Z} \,\} \;\leq\; \mathbb{C},$$
the set of complex numbers with integer real and imaginary parts, with addition and multiplication inherited from $\mathbb{C}$. It is a commutative ring with $1$, and being a subring of the field $\mathbb{C}$ it has no zero divisors, so it is an [[Def - Integral Domain|integral domain]].

The **norm** is the function
$$N : \mathbb{Z}[i] \longrightarrow \mathbb{Z}_{\geq 0}, \qquad N(a+bi) = a^2 + b^2 = (a+bi)(a-bi) = |a+bi|^2.$$
It satisfies the following, which together make $\mathbb{Z}[i]$ the principal example of §2.6:

1. **Multiplicativity.** $N(zw) = N(z)\,N(w)$ for all $z, w \in \mathbb{Z}[i]$.

2. **Units.** $z \in \mathbb{Z}[i]^\times$ if and only if $N(z) = 1$, and the units are exactly
$$\mathbb{Z}[i]^\times = \{\, 1,\ -1,\ i,\ -i \,\}.$$

3. **Euclidean structure.** $N$ is a [[Def - Euclidean Domain|Euclidean function]] on $\mathbb{Z}[i]$: for all $a, b \in \mathbb{Z}[i]$ with $b \neq 0$ there exist $q, r \in \mathbb{Z}[i]$ with $a = bq + r$ and either $r = 0$ or $N(r) < N(b)$.

Consequently $\mathbb{Z}[i]$ is a **Euclidean domain**, hence a **[[Def - Principal Ideal Domain|principal ideal domain]]**, hence a **[[Def - Unique Factorization Domain|unique factorization domain]]**. In particular, by the chain of implications, an element of $\mathbb{Z}[i]$ is [[Def - Irreducible and Prime Elements|irreducible if and only if it is prime]].

---

# Relate to Other Fields / Compression

The Gaussian integers are best compressed as **the integer lattice of the complex plane, made into a ring**. The set $\mathbb{Z}[i]$ is the unit square lattice $\mathbb{Z}^2 \subset \mathbb{R}^2 = \mathbb{C}$; what upgrades the lattice from an abelian group to a ring is that the lattice is *closed under complex multiplication* — multiplying by $i$ rotates the lattice by ninety degrees onto itself. So $\mathbb{Z}[i]$ is exactly "the points of $\mathbb{C}$ you can reach from $1$ and $i$ by ring operations", and its geometry as a lattice is not decoration: the Euclidean property is the purely geometric statement that *every point of the plane lies within distance $< 1$ of a lattice point* (the farthest you can be is the centre of a unit square, at distance $\tfrac{1}{\sqrt 2}$).

This places $\mathbb{Z}[i]$ in a family. It is the **ring of integers of the number field $\mathbb{Q}(i)$** — the analogue, for the field $\mathbb{Q}(i)$, of what $\mathbb{Z}$ is for $\mathbb{Q}$. Replace $i = \sqrt{-1}$ by another algebraic number and you get a sibling: $\mathbb{Z}[\omega]$ with $\omega = e^{2\pi i/3}$ (the **Eisenstein integers**, the triangular lattice) is again Euclidean, while $\mathbb{Z}[\sqrt{-5}]$ is *not* — its lattice is too stretched for the nearest-point argument, and unique factorization fails there. The Gaussian integers are the most accessible member of algebraic number theory's central object, the ring of integers of a number field, and the norm $N$ is the **field norm** of $\mathbb{Q}(i)/\mathbb{Q}$, the product of an element with its Galois conjugate.

There is also a clean compression of the *norm form* itself. The identity $N(z)N(w) = N(zw)$ is the **two-square identity** $(a^2+b^2)(c^2+d^2) = (ac-bd)^2 + (ad+bc)^2$: the statement that a product of two sums of two squares is again a sum of two squares. So "$\mathbb{Z}[i]$ has a multiplicative norm" and "sums of two squares are closed under multiplication" are the same fact in two languages, which is exactly why $\mathbb{Z}[i]$ is the right tool for the [[Thm - Sum of Two Squares|sum-of-two-squares problem]].

---

# Examples / Corollaries

**The units are exactly $\pm 1, \pm i$.** A unit has norm $1$, and $a^2 + b^2 = 1$ with $a, b \in \mathbb{Z}$ forces $\{a,b\} = \{\pm 1, 0\}$, giving the four elements $1, -1, i, -i$. Geometrically these are the four lattice points on the unit circle; algebraically they form the cyclic [[Def - Group|group]] $C_4$ generated by $i$. This is the calibration check on the norm: if you can recover the unit group from "norm $1$", you have understood why $N$ detects units.

**$2$ is not irreducible: $2 = (1+i)(1-i)$.** Both factors have norm $N(1\pm i) = 1^2 + 1^2 = 2 \neq 1$, so neither is a unit, and $2$ genuinely factors. Note moreover that $1 - i = -i(1+i)$ (check: $-i(1+i) = -i + 1$), so $1+i$ and $1-i$ are associates, and $2$ is, up to a unit, the *square* of the single Gaussian prime $1+i$: indeed $(1+i)^2 = 2i$, so $2 = -i(1+i)^2$. The rational prime $2$ **ramifies** in $\mathbb{Z}[i]$.

**$5$ is not irreducible: $5 = (2+i)(2-i)$.** Here $N(2 \pm i) = 4 + 1 = 5$, neither factor a unit, so $5$ splits. The two factors $2+i$ and $2-i$ are *not* associates (no unit carries one to the other), so $5$ **splits** into two distinct Gaussian primes. This is the generic behaviour for $p \equiv 1 \pmod 4$.

**$3$ stays irreducible (hence prime).** Suppose $3 = uv$ with $u, v$ non-units. Taking norms, $N(3) = 9 = N(u)N(v)$ with neither factor $1$, forcing $N(u) = N(v) = 3$. But $a^2 + b^2 = 3$ has *no* integer solution — squares are $0, 1, 4, 9, \dots$ and no two sum to $3$ — so there is no Gaussian integer of norm $3$. The factorization $3 = uv$ is impossible, $3$ is irreducible, and since $\mathbb{Z}[i]$ is a UFD, $3$ is prime. The same argument shows $7$ stays prime ($a^2 + b^2 = 7$ is unsolvable), and this is the generic behaviour for $p \equiv 3 \pmod 4$ — see [[Thm - Classification of Gaussian Primes]].

**Norm $1$ is not sufficient for "trivial" — but norm a rational prime is sufficient for irreducible.** If $N(z) = p$ is a rational prime, then $z$ is irreducible: any factorization $z = uv$ gives $p = N(u)N(v)$, forcing one factor to have norm $1$, i.e. to be a unit. This is the most useful one-line irreducibility test in $\mathbb{Z}[i]$: *prime norm forces irreducibility*. The converse fails — $3$ is irreducible with norm $9$ — which is exactly the subtlety the [[Thm - Classification of Gaussian Primes|classification]] resolves.

**Calibration check.** Verify that the norm of $1 + i$ is $2$, of $2 + i$ is $5$, of $3$ is $9$. Verify that $1 - i$, $-1+i$, $-1-i$, $1+i$ are all associates (multiply by the four units) and so define a *single* Gaussian prime. Verify that division with remainder is non-unique: dividing $3 + i$ by $1 + i$, the true quotient is $\tfrac{3+i}{1+i} = 2 - i$ exactly, so $r = 0$; but dividing $3 + 2i$ by $1 + i$ gives true quotient $\tfrac{5}{2} - \tfrac{1}{2}i$, within distance $< 1$ of more than one lattice point. If you can also explain why $a^2+b^2$ and not $|a+bi|$ is the norm — integer codomain for Euclidean descent — the definition has landed.

---

# Unlocked by This

> [!tip] Classification of Gaussian Primes *(from this topic)*
> Once $\mathbb{Z}[i]$ is known to be a UFD with multiplicative norm, the next question is *what* its primes are. The answer sorts rational primes by their residue mod $4$: $p \equiv 3$ stays prime, $p \equiv 1$ and $p = 2$ split. See [[Thm - Classification of Gaussian Primes]].

> [!tip] Sum of Two Squares *(from this topic)*
> Because $N(x+iy) = x^2 + y^2$, asking which integers are sums of two squares is asking which integers are norms from $\mathbb{Z}[i]$ — a factorization question. See [[Thm - Sum of Two Squares]], Fermat's two-squares theorem.
