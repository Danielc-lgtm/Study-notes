---
type: exercise
subject: algebraic-topology
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Singular Homology"
  - "Thm - Singular and Simplicial Homology Agree on Triangulable Spaces"
  - "Def - Euler Characteristic"
tags: [geometry, algebraic-topology, projective-space, torsion]
---

# Problem Statement

Compute $H_*(\mathbb{RP}^2; G)$ for $G = \mathbb{Z}$, $G = \mathbb{R}$, and $G = \mathbb{Z}/2\mathbb{Z}$, using the disk-with-antipodal-identifications model of $\mathbb{RP}^2$ (Frankel Figure 13.19). Observe explicitly how the answer depends on the coefficient group: $\mathbb{Z}$-homology has torsion ($H_1 = \mathbb{Z}/2$); $\mathbb{R}$-homology has the same Betti numbers as a point (Betti numbers $(1, 0, 0)$); $\mathbb{Z}/2$-homology has rank pattern $(1, 1, 1)$.

**Recall:**

The real projective plane $\mathbb{RP}^2$ is the quotient of the closed unit disk $D^2$ by the antipodal identification on the boundary: $(x, y) \sim (-x, -y)$ for $(x, y) \in S^1 = \partial D^2$. Equivalently, $\mathbb{RP}^2 = S^2 / \mathbb{Z}_2$ where $\mathbb{Z}_2$ acts by $x \mapsto -x$.

Frankel triangulates $\mathbb{RP}^2$ using the disk model with $1$-cell $A$ — the boundary loop (each half of the boundary $S^1$ becomes one loop of $A$ after identification). The fundamental chain $[\mathbb{RP}^2]$ is the sum of the disk's triangles with consistent orientation.

By [[Thm - Singular and Simplicial Homology Agree on Triangulable Spaces]], the simplicial homology computed from this triangulation equals the singular homology.

---

# Convergent Strategy

**Problem class:** This is a triangulation-based computation of homology for a non-orientable space, with explicit attention to how the answer depends on the coefficient group. The class is "compute $H_*(M; G)$ for varying $G$" — a problem that exposes the role of torsion in integer homology. $\mathbb{RP}^2$ is the simplest non-trivial example exhibiting torsion: $H_1(\mathbb{RP}^2; \mathbb{Z}) = \mathbb{Z}/2$, a torsion group invisible to $\mathbb{R}$-coefficients but visible (in fact doubled) by $\mathbb{Z}/2$-coefficients.

**Assumption pattern:** $\mathbb{RP}^2$ has the disk-with-antipodal-identification triangulation, with one $1$-cycle $A$ (the boundary loop after identification) and a fundamental chain $[\mathbb{RP}^2]$ summing the disk's triangles. The boundary of $[\mathbb{RP}^2]$ is computed: the result is $2A$, not zero, reflecting non-orientability.

**Theorem routing:** Compute $\partial[\mathbb{RP}^2] = 2A$ directly, using the disk-model triangulation and tracking the orientation on the boundary. With $G = \mathbb{Z}$: $A$ is a $1$-cycle but $2A = \partial[\mathbb{RP}^2]$ is a boundary, so $A$ has order $2$ in $H_1$ — torsion. With $G = \mathbb{R}$: $A$ is a $1$-cycle and $2A$ is a boundary, so $A = \frac{1}{2} \partial[\mathbb{RP}^2]$ is also a boundary (using that we can divide by $2$ in $\mathbb{R}$), hence $[A] = 0$. With $G = \mathbb{Z}/2$: $2A = 0$ in $\mathbb{Z}/2$ coefficients, so $A$ is a non-trivial $1$-cycle, and $[\mathbb{RP}^2]$ becomes a non-trivial $2$-cycle (its $\mathbb{Z}/2$-boundary is $2A = 0$).

**Key decision point:** The non-obvious step is recognising that the same chain $[\mathbb{RP}^2]$ has different homological meaning over different coefficient groups: it is a non-cycle (boundary $2A$) over $\mathbb{Z}$, hence does not contribute to $H_2$; it is also a non-cycle over $\mathbb{R}$ for the same reason; but it becomes a cycle ($2A = 0$) over $\mathbb{Z}/2$, hence $H_2(\mathbb{RP}^2; \mathbb{Z}/2) = \mathbb{Z}/2$. Similarly, the loop $A$ has order $2$ in $\mathbb{Z}$-homology (torsion), order $1$ in $\mathbb{R}$-homology (trivial, because $\mathbb{R}$ allows division by $2$), and order $2$ but non-trivial in $\mathbb{Z}/2$-homology.

---

# Legal Operations Used

1. **Triangulate the space and use simplicial = singular homology** (operation 11). $\mathbb{RP}^2$ has the disk-with-antipodal triangulation; simplicial homology of this triangulation equals singular homology.

2. **Compute $\partial[\mathbb{RP}^2]$ explicitly** (operation 3). Track the orientation on the boundary disc — the two halves of the boundary $S^1$ become the same loop $A$ on $\mathbb{RP}^2$, with the same induced orientation (because of antipodal identification, the orientation does not reverse), giving $\partial[\mathbb{RP}^2] = 2A$.

3. **Switch coefficient groups to extract different information** (operation 9). Compute with $\mathbb{Z}$, $\mathbb{R}$, $\mathbb{Z}/2$ separately to see torsion behavior.

4. **Use top homology and orientability** (operation 8). $\partial[\mathbb{RP}^2] = 2A \neq 0$ over $\mathbb{Z}$ confirms non-orientability; $H_2(\mathbb{RP}^2; \mathbb{Z}) = 0$ over $\mathbb{Z}$. Over $\mathbb{Z}/2$, $2A = 0$, so $[\mathbb{RP}^2]$ is a cycle and $H_2(\mathbb{RP}^2; \mathbb{Z}/2) = \mathbb{Z}/2$.

---

# Hints

> [!note]- Hint 1
> Set up the triangulation: think of $\mathbb{RP}^2$ as a disk $D^2$ with antipodal points on the boundary identified. Triangulate the disk in any convenient way (any simplicial triangulation of the disk works), respecting the boundary identification.
>
> Now compute $\partial[\mathbb{RP}^2]$, where $[\mathbb{RP}^2]$ is the sum of all triangles with consistent orientation (counterclockwise, say). The interior edges cancel as for the torus. The boundary edges of the disk become *the same loop* $A$ after identification — but with what orientation pattern?

> [!note]- Hint 2
> The boundary of the disk is $S^1$. After antipodal identification, the upper half of $S^1$ and the lower half become the same loop $A$ on $\mathbb{RP}^2$. The orientations of the two halves (as parts of the disk's boundary, traversed counterclockwise) are *both* in the same direction along $A$ — because the antipodal map reverses both the direction *and* the labelling. So the boundary of $[\mathbb{RP}^2]$ becomes $A + A = 2A$, not $A - A = 0$.

> [!note]- Hint 3
> So $\partial[\mathbb{RP}^2] = 2A$ over $\mathbb{Z}$. This means:
> - With $\mathbb{Z}$ coefficients: $[\mathbb{RP}^2]$ is not a cycle ($\partial \neq 0$), so $H_2(\mathbb{RP}^2; \mathbb{Z}) = 0$. The loop $A$ is a $1$-cycle but $2A = \partial[\mathbb{RP}^2]$ is a boundary, so $A$ has order $2$ in $H_1(\mathbb{RP}^2; \mathbb{Z}) = \mathbb{Z}/2$.
> - With $\mathbb{R}$ coefficients: $2A$ is a boundary, but in $\mathbb{R}$ we can divide by $2$, so $A = \frac{1}{2} \partial[\mathbb{RP}^2] = \partial(\frac{1}{2} [\mathbb{RP}^2])$ is also a boundary. Hence $[A] = 0$ in $H_1(\mathbb{RP}^2; \mathbb{R}) = 0$.
> - With $\mathbb{Z}/2$ coefficients: $2A = 0$, so $\partial[\mathbb{RP}^2] = 0$, and $[\mathbb{RP}^2]$ is a non-trivial $2$-cycle. The loop $A$ is still a cycle, and is not a boundary (no $2$-chain has $A$ as its $\mathbb{Z}/2$-boundary, since the only candidate $[\mathbb{RP}^2]$ has boundary $0$).

---

# Solution

The proof breaks into three steps. Step 1 triangulates $\mathbb{RP}^2$ and computes $\partial[\mathbb{RP}^2] = 2A$. Step 2 computes $H_*(\mathbb{RP}^2; \mathbb{Z})$, identifying the torsion in $H_1$. Step 3 computes $H_*$ over $\mathbb{R}$ and $\mathbb{Z}/2$, showing how the coefficient group changes the answer.

**Step 1: Triangulate $\mathbb{RP}^2$ and compute $\partial[\mathbb{RP}^2] = 2A$.**

Following Frankel Figure 13.19: $\mathbb{RP}^2$ is the unit disk $D^2$ with antipodal identifications on the boundary. Triangulate the disk into a finite number of triangles, with vertices on the boundary respecting the antipodal identification (so each pair of antipodal boundary vertices becomes a single vertex on $\mathbb{RP}^2$). Let $[\mathbb{RP}^2]$ be the sum of all triangles with counterclockwise orientation.

Compute $\partial[\mathbb{RP}^2]$: interior edges cancel (each shared by two triangles with opposite induced orientations), as for the torus. The boundary contributions come from the disk's boundary $S^1$. The boundary $S^1$ consists of two halves: an upper arc and a lower arc. After antipodal identification, these become the same loop $A$ on $\mathbb{RP}^2$ — both traversed in the same direction along $A$.

Therefore $\partial[\mathbb{RP}^2] = A + A = 2A$, where $A$ is the boundary $1$-cycle obtained from a single half of the disk's boundary $S^1$.

> [!note]- Derivation
> The boundary of the disk $S^1$ is a single closed loop. After the antipodal identification, $S^1$ folds onto itself (each pair of antipodal points becoming a single point on $\mathbb{RP}^2$), and the resulting loop on $\mathbb{RP}^2$ — call it $A$ — is exactly half of the original $S^1$. (The other half maps to the same loop $A$ via the identification.)
>
> The orientation: as we traverse $S^1$ counterclockwise (the boundary of the disk), the upper half goes from the right point $(1, 0)$ to the left point $(-1, 0)$, while the lower half goes from $(-1, 0)$ back to $(1, 0)$. After identification, both halves traverse $A$ in the *same* direction on $\mathbb{RP}^2$: the upper half from $[(1, 0)]$ to $[(-1, 0)]$ (which are the same point on $\mathbb{RP}^2$), and the lower half from $[(-1, 0)] = [(1, 0)]$ back to itself via the same loop. So both halves contribute $+A$ to $\partial[\mathbb{RP}^2]$.
>
> Total: $\partial[\mathbb{RP}^2] = (+A) + (+A) = 2A$. This is Frankel's equation 13.27 made explicit.
>
> Compare with the torus: there, the boundary identifications $(0, y) \sim (1, y)$ give $+A$ and $-A$ contributions to $\partial$, summing to zero. The Klein bottle is intermediate: one identification preserves orientation ($+B - B = 0$) and the other reverses it ($+A + A = 2A$), giving total $\partial = 2A \neq 0$. $\mathbb{RP}^2$ has both identifications reversing orientation, giving $2A$.

**Step 2: Compute $H_*(\mathbb{RP}^2; \mathbb{Z})$.**

*$H_0(\mathbb{RP}^2; \mathbb{Z}) = \mathbb{Z}$:* $\mathbb{RP}^2$ is path-connected (the disk is, and the quotient preserves connectedness).

*$H_2(\mathbb{RP}^2; \mathbb{Z}) = 0$:* Any $2$-cycle $w$ must be a $\mathbb{Z}$-multiple of $[\mathbb{RP}^2]$ (by edge-cancellation arguments, all triangles in $w$ have equal coefficients). But $\partial(n [\mathbb{RP}^2]) = n \cdot 2A = 2nA$, which equals zero only if $n = 0$. So $Z_2 = 0$, and $H_2 = 0$.

*$H_1(\mathbb{RP}^2; \mathbb{Z}) = \mathbb{Z}/2$:* The $1$-cycle $A$ satisfies $\partial A = 0$ (the loop has no boundary). But $2A = \partial[\mathbb{RP}^2]$ is a boundary. So in $H_1$, the class $[A]$ has order dividing $2$. Since $A$ itself is not a boundary (no $2$-chain has $A$ as its boundary — the only candidate $[\mathbb{RP}^2]$ has boundary $2A$, not $A$, and there's no way to extract "half" of $[\mathbb{RP}^2]$ as an integer chain), the class $[A] \neq 0$. Hence $[A]$ has exact order $2$, generating $H_1(\mathbb{RP}^2; \mathbb{Z}) = \mathbb{Z}/2$.

> [!note]- Derivation
> *$H_2$:* Any element of $Z_2(\mathbb{RP}^2; \mathbb{Z}) = \ker \partial_2$ is a $2$-chain $w = \sum n_i \tau_i$ with $\partial w = 0$. The interior edges of the triangulation cancel in $\partial w$ iff the coefficients $n_i$ are constant — say $n_i = n$ for all $i$. So $w = n[\mathbb{RP}^2]$. Then $\partial w = n \cdot 2A = 2nA$, which is zero only if $n = 0$. Hence $Z_2 = 0$, and $H_2 = Z_2/B_2 = 0/0 = 0$.
>
> *$H_1$:* The cycle group $Z_1$ contains $A$ (since $\partial A = 0$ from the loop structure) and is spanned by $A$ modulo boundaries (a deformation argument like the torus case shows every $1$-cycle is homologous to a multiple of $A$). The boundary group $B_1 = \mathrm{im}(\partial_2) = \mathbb{Z} \cdot 2A \subset Z_1 = \mathbb{Z} \cdot A$. So $H_1 = Z_1 / B_1 = \mathbb{Z}\langle A \rangle / \langle 2A \rangle = \mathbb{Z}/2$.
>
> The generator of $H_1(\mathbb{RP}^2; \mathbb{Z}) = \mathbb{Z}/2$ is $[A]$, the class of the boundary loop. The loop has the property: traversing it twice gives a contractible loop ($\partial[\mathbb{RP}^2] = 2A$); traversing once gives a non-contractible loop. This is the classical "rotation by $360^\circ$ in $\mathrm{SO}(3)$" relation: a single rotation is non-trivially in $\pi_1(\mathrm{SO}(3))$, but two rotations are contractible.

**Step 3: Compute $H_*(\mathbb{RP}^2; \mathbb{R})$ and $H_*(\mathbb{RP}^2; \mathbb{Z}/2)$.**

*Over $\mathbb{R}$:* The chain complex is the same (with $\mathbb{R}$-coefficients). $Z_2 = 0$ as before. $B_1 = \mathbb{R} \cdot 2A = \mathbb{R} \cdot A = Z_1$ (since $\mathbb{R}$ contains $1/2$, multiplying through gives all of $\mathbb{R} \cdot A$). So $H_1 = Z_1 / B_1 = 0$. $H_0(\mathbb{RP}^2; \mathbb{R}) = \mathbb{R}$.

So $H_*(\mathbb{RP}^2; \mathbb{R}) = (\mathbb{R}, 0, 0)$ — the same Betti numbers as a point.

*Over $\mathbb{Z}/2$:* Now $2A = 0$ in $\mathbb{Z}/2$-coefficient chains, so $\partial[\mathbb{RP}^2] = 2A = 0$. Hence $[\mathbb{RP}^2]$ is a non-trivial $\mathbb{Z}/2$-cycle, and $Z_2 = (\mathbb{Z}/2) \cdot [\mathbb{RP}^2] = \mathbb{Z}/2$. There are no $3$-chains, so $B_2 = 0$ and $H_2(\mathbb{RP}^2; \mathbb{Z}/2) = \mathbb{Z}/2$.

For $H_1$: $Z_1 = (\mathbb{Z}/2) \cdot A$, and $B_1 = \mathrm{im}(\partial_2 : C_2(\mathbb{Z}/2) \to C_1(\mathbb{Z}/2)) = \langle 2A \rangle = 0$ (since $2 = 0$ in $\mathbb{Z}/2$). So $H_1(\mathbb{RP}^2; \mathbb{Z}/2) = (\mathbb{Z}/2) / 0 = \mathbb{Z}/2$.

$H_0(\mathbb{RP}^2; \mathbb{Z}/2) = \mathbb{Z}/2$ (connectedness).

So $H_*(\mathbb{RP}^2; \mathbb{Z}/2) = (\mathbb{Z}/2, \mathbb{Z}/2, \mathbb{Z}/2)$ — rank pattern $(1, 1, 1)$ in mod-$2$.

> [!note]- Derivation
> *Over $\mathbb{R}$:* the chain complex is now $C_*(M; \mathbb{R})$, a complex of $\mathbb{R}$-vector spaces. $\partial[\mathbb{RP}^2] = 2A$ is still non-zero. But the cycle $A$ satisfies $A = \frac{1}{2} \cdot 2A = \frac{1}{2} \partial[\mathbb{RP}^2] = \partial(\frac{1}{2} [\mathbb{RP}^2])$, so $A$ is a boundary (over $\mathbb{R}$). Hence $[A] = 0$ in $H_1(\mathbb{RP}^2; \mathbb{R}) = 0$.
>
> The same reasoning: $Z_1 = \mathbb{R} \cdot A$, $B_1 = \mathbb{R} \cdot 2A = \mathbb{R} \cdot A$ (since $2$ is invertible in $\mathbb{R}$), so $H_1 = 0$.
>
> $H_2 = 0$ as before (no $\mathbb{R}$-cycles).
>
> *Over $\mathbb{Z}/2$:* now $2 = 0$ in $\mathbb{Z}/2$, so $\partial[\mathbb{RP}^2] = 2A = 0$. $[\mathbb{RP}^2]$ becomes a cycle. There are no higher chains, so $H_2 = Z_2 / 0 = (\mathbb{Z}/2) \cdot [\mathbb{RP}^2] = \mathbb{Z}/2$.
>
> $H_1$: $Z_1 = (\mathbb{Z}/2) \cdot A$. $B_1 = \mathrm{im}(\partial_2) = (\mathbb{Z}/2) \cdot 2A = 0$. So $H_1 = (\mathbb{Z}/2) \cdot A / 0 = \mathbb{Z}/2$.
>
> $H_0 = \mathbb{Z}/2$ from connectedness.
>
> The pattern $(1, 1, 1)$ in mod-$2$ versus $(1, 0, 0)$ in $\mathbb{R}$ is the **universal coefficient theorem** in action: $H_*(\mathbb{RP}^2; \mathbb{Z}/2) = H_*(\mathbb{RP}^2; \mathbb{Z}) \otimes \mathbb{Z}/2 \oplus \mathrm{Tor}(H_{*-1}(\mathbb{RP}^2; \mathbb{Z}), \mathbb{Z}/2)$ adds an extra $\mathbb{Z}/2$ from torsion, while $H_*(\mathbb{RP}^2; \mathbb{R}) = H_*(\mathbb{RP}^2; \mathbb{Z}) \otimes \mathbb{R}$ deletes the torsion.

> [!note]- Complete formal solution
> **Theorem.** $H_*(\mathbb{RP}^2; G)$ for $G = \mathbb{Z}, \mathbb{R}, \mathbb{Z}/2$:
> $$
> H_*(\mathbb{RP}^2; \mathbb{Z}) = (\mathbb{Z}, \mathbb{Z}/2, 0), \quad H_*(\mathbb{RP}^2; \mathbb{R}) = (\mathbb{R}, 0, 0), \quad H_*(\mathbb{RP}^2; \mathbb{Z}/2) = (\mathbb{Z}/2, \mathbb{Z}/2, \mathbb{Z}/2).
> $$
>
> *Proof.* Triangulate $\mathbb{RP}^2$ as the disk $D^2$ with antipodal identifications on the boundary. The fundamental chain $[\mathbb{RP}^2]$ — the sum of all triangles with counterclockwise orientation — has boundary $\partial[\mathbb{RP}^2] = 2A$, where $A$ is the boundary loop on $\mathbb{RP}^2$ (the image of a half-arc of the disk's boundary $S^1$, with both halves identified via antipodal).
>
> *Over $\mathbb{Z}$:* $Z_2 = 0$ (no integer multiple of $[\mathbb{RP}^2]$ has zero boundary, since $\partial(n[\mathbb{RP}^2]) = 2nA \neq 0$). So $H_2 = 0$. $Z_1 = \mathbb{Z} \cdot A$ (boundary cycle); $B_1 = \mathbb{Z} \cdot 2A$ (image of $\partial_2$). $H_1 = \mathbb{Z}/2$, generated by $[A]$. $H_0 = \mathbb{Z}$ (connected).
>
> *Over $\mathbb{R}$:* same as integer except $B_1 = \mathbb{R} \cdot 2A = \mathbb{R} \cdot A = Z_1$ (using $1/2 \in \mathbb{R}$). So $H_1 = 0$. $H_2 = 0$ as before. $H_0 = \mathbb{R}$.
>
> *Over $\mathbb{Z}/2$:* $\partial[\mathbb{RP}^2] = 2A = 0$ (since $2 = 0$ in $\mathbb{Z}/2$). So $[\mathbb{RP}^2]$ is a $\mathbb{Z}/2$-cycle, generating $Z_2 = (\mathbb{Z}/2) \cdot [\mathbb{RP}^2]$. $B_2 = 0$, $H_2 = \mathbb{Z}/2$. $Z_1 = (\mathbb{Z}/2) \cdot A$, $B_1 = (\mathbb{Z}/2) \cdot 2A = 0$. $H_1 = \mathbb{Z}/2$. $H_0 = \mathbb{Z}/2$.
>
> $\qquad\blacksquare$

---

# Key Takeaways

**Coefficient groups carry different topological information.** This exercise is the most direct demonstration of the principle that different coefficient groups reveal different facets of a space's topology. $\mathbb{Z}$ is the universal choice — it sees both the free part (Betti numbers) and the torsion. $\mathbb{R}$ (or any field of characteristic zero) kills torsion, leaving only the Betti numbers. $\mathbb{Z}/2$ sees torsion of order $2$ and free parts modulo $2$; in particular, it makes non-orientable manifolds carry a fundamental class (which they lack with $\mathbb{Z}$-coefficients). The full integer answer $H_*(M; \mathbb{Z})$ is the most refined and determines the others via the **universal coefficient theorem**.

**Non-orientability and torsion go hand in hand.** For a closed connected $n$-manifold $M$:
- If $M$ is orientable: $H_n(M; \mathbb{Z}) = \mathbb{Z}$, generated by the fundamental class $[M]$.
- If $M$ is non-orientable: $H_n(M; \mathbb{Z}) = 0$ (no integer fundamental class) but $H_n(M; \mathbb{Z}/2) = \mathbb{Z}/2$ (the mod-$2$ fundamental class always exists), and $H_{n-1}(M; \mathbb{Z})$ has $\mathbb{Z}/2$ torsion (the "obstruction to orientability"). For $\mathbb{RP}^2$: $H_2 = 0$, $H_1 = \mathbb{Z}/2$ — the $\mathbb{Z}/2$ in $H_1$ encodes the orientation-reversing loop. The Klein bottle has the same pattern: $H_2(K; \mathbb{Z}) = 0$, $H_1(K; \mathbb{Z}) = \mathbb{Z} \oplus \mathbb{Z}/2$ — with the torsion piece being the orientation-reversing loop.

**Euler characteristic and Betti numbers can be very lossy.** The Betti number pattern $(1, 0, 0)$ of $\mathbb{RP}^2$ is the same as that of a single point! Yet $\mathbb{RP}^2$ is a non-trivial surface — it has a non-trivial fundamental group $\pi_1(\mathbb{RP}^2) = \mathbb{Z}/2$, and it cannot be embedded in $\mathbb{R}^3$. The Betti numbers (or equivalently $\mathbb{R}$-cohomology) miss this entire structure. The torsion in $\mathbb{Z}$-homology, and the rank pattern of $\mathbb{Z}/2$-cohomology, are what distinguish $\mathbb{RP}^2$ from a point. This is the canonical illustration of why "homology over a field" is not sufficient — we need integer homology (or at least mod-$p$ homology for various primes $p$) for a complete invariant.

**The relation $\partial[\mathbb{RP}^2] = 2A$ has a deep group-theoretic interpretation.** The loop $A$ generates $\pi_1(\mathbb{RP}^2) = \mathbb{Z}/2$ — it is the non-trivial loop in the fundamental group. The relation $2A = \partial[\mathbb{RP}^2]$ says: going around the loop $A$ twice is *homologically* trivial. This is the abelianised form of the relation $A^2 = e$ in $\pi_1(\mathbb{RP}^2)$. The connection comes via the **Hurewicz theorem**: for a non-simply-connected space, $H_1(X; \mathbb{Z}) = \pi_1(X)^{\mathrm{ab}}$, the abelianisation of the fundamental group. For $\mathbb{RP}^2$, $\pi_1 = \mathbb{Z}/2$ is already abelian, so $H_1 = \mathbb{Z}/2$ matches. The story extends to $\mathrm{SO}(3) \cong \mathbb{RP}^3$, whose $\pi_1 = \mathbb{Z}/2$ encodes "a $360^\circ$ rotation is non-trivial, but a $720^\circ$ rotation is contractible" — the geometric origin of the spin-$1/2$ representations in quantum mechanics. See [[Spinors and the Dirac Equation]] and [[Algebraic Topology II — Fundamental Group and Covering Spaces]].
