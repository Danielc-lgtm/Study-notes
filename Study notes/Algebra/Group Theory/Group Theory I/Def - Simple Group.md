---
type: definition
subject: group-theory
prereqs:
  - "Def - Normal Subgroup"
  - "Def - Quotient Group"
  - "Def - Group"
tags: [algebra, group-theory]
---

# Notation

$G$ is a group with identity $e$; $\{e\}$ is the trivial group. We write $N \trianglelefteq G$ for a [[Def - Normal Subgroup|normal subgroup]]. A *proper* normal subgroup is one with $N \neq G$; a *non-trivial* one has $N \neq \{e\}$. $C_p$ denotes the cyclic group of order $p$, and $A_n$ the alternating group on $n$ letters. The full symbol registry is on [[Group Theory I — §1.1–1.2]].

---

# Axiom Motivation

The entire programme of §1.2 is *taking groups apart*. The tool for this is the [[Def - Quotient Group|quotient]]: given a [[Def - Normal Subgroup|normal subgroup]] $N \trianglelefteq G$, you split $G$ into two strictly smaller groups, the piece $N$ and the piece $G/N$, and study each. The arithmetic analogy, exact as always, is factoring an integer: $12 = 4 \times 3$, and you understand $12$ by understanding $4$ and $3$. Iterate, and you reach the *primes* — the numbers that cannot be factored further. The motivating desideratum is to identify the group-theoretic analogue: *the groups that cannot be taken apart, the atoms at which the splitting process terminates.*

So we want to name the groups for which the quotient construction yields *nothing new*. When does quotienting $G$ tell you nothing? Quotienting by $N$ produces the pair $(N,\ G/N)$. If $N = \{e\}$, the quotient $G/\{e\} \cong G$ is just $G$ again and $N$ is trivial — no progress. If $N = G$, the quotient $G/G$ is trivial and $N = G$ — again no progress, you have only recovered $G$ and the trivial group. These two normal subgroups, $\{e\}$ and $G$, are present in *every* group and *always* give a useless split. A *useful* split requires a normal subgroup that is *neither* — a **proper, non-trivial** normal subgroup. A group that cannot be taken apart is therefore exactly a group that has no proper non-trivial normal subgroup: a group whose only normal subgroups are the two unavoidable ones. That is the definition of **simple**, and it has been forced on us by the demand "name the unsplittable groups".

Two refinements pin the definition down precisely. First, why insist $G$ be *non-trivial*? Because we want simple groups to behave like primes, and the number $1$ is deliberately *not* prime — admitting it would wreck unique factorisation. The trivial group $\{e\}$ has only one subgroup, so it vacuously "has no proper non-trivial normal subgroup", but counting it as simple would similarly wreck the theory: [[Thm - Composition Series|composition series]] would no longer terminate cleanly and the factor multiset would not be an invariant. So the trivial group is excluded by fiat, exactly as $1$ is excluded from the primes. Second, why phrase the condition with *normal* subgroups rather than *all* subgroups? Because the splitting tool is the *quotient*, and quotients are formed by *normal* subgroups only. A group can have many proper non-trivial subgroups and still be unsplittable, provided none of them is normal: $A_5$ has subgroups galore but no normal one other than $\{e\}$ and $A_5$, so it cannot be quotiented and is simple. The condition must speak about exactly the subgroups the quotient construction can use.

What breaks if we *weaken* — say, define "simple" via *all* subgroups, demanding $G$ have no proper non-trivial subgroup whatsoever? Then by [[Thm - Lagrange's Theorem|Lagrange]] $|G|$ could have no proper divisors, forcing $|G|$ prime, and the *only* simple groups would be the $C_p$. We would lose $A_5, A_6, \dots$ and all the non-abelian simple groups — the entire substance of the [[#Unlocked by This|classification]] — because those groups *do* have proper non-trivial subgroups, just no normal ones. The weakened definition collapses a rich theory to a triviality. (The two definitions *do* coincide for [[Def - Abelian Group|abelian]] groups, since there every subgroup is normal — see the example below — which is exactly why abelian simple groups are so easy to classify and non-abelian ones so hard.) What breaks if we *strengthen* — demand the only normal subgroups be $\{e\}$ and $G$ *and* additionally that $G$ have prime order? Then again only the $C_p$ survive and the non-abelian atoms are excluded. The plain definition — non-trivial, no proper non-trivial *normal* subgroup — is exactly the one for which "every finite group is built from simple pieces" is true and the pieces form a genuine periodic table.

---

# The Definition

A group $G$ is **simple** if it is non-trivial and its only [[Def - Normal Subgroup|normal subgroups]] are $\{e\}$ and $G$ itself:
$$G \neq \{e\}, \qquad \text{and} \qquad \big(N \trianglelefteq G \ \Longrightarrow\ N = \{e\} \text{ or } N = G\big).$$

Equivalently — and this is the operative meaning — a simple group is one that admits *no non-trivial [[Def - Quotient Group|quotient]]*. The only quotients of a simple $G$ are $G/\{e\} \cong G$ and $G/G \cong \{e\}$; there is no quotient strictly between, so $G$ cannot be broken into smaller pieces. Equivalently again, via the kernel characterisation of normality: every [[Def - Homomorphism|homomorphism]] out of a simple group is either trivial or injective, since its [[Def - Kernel and Image|kernel]] is a normal subgroup and so must be $\{e\}$ (injective) or $G$ (trivial).

Simple groups are the **atoms** of finite group theory: the groups at which the take-apart process [[Thm - Composition Series|terminates]].

---

# Relate to Other Fields / Compression

Simplicity is the group-theoretic instance of *irreducibility* — the property of being an atom for a notion of decomposition. The pattern recurs throughout algebra, each time as "cannot be broken down by the relevant quotient/factoring operation". A **prime number** is an integer with no factorisation into smaller integers; a **prime ideal** (or maximal ideal) plays the atomic role for [[Def - Ideal|ideals]] of a ring, with the quotient $R/\mathfrak{m}$ by a maximal ideal being a *field* — the ring-theoretic echo of "$G/N$ simple". An **irreducible polynomial** is the atom of the polynomial ring under factorisation. An **irreducible representation** is a representation with no proper non-trivial *invariant subspace* — the representation-theoretic atom, where "invariant subspace" plays the role "normal subgroup" plays here. In every case the atoms are the building blocks and there is a structure theorem assembling general objects from them; the group case's structure theorem is the [[Thm - Composition Series|composition series]], and the analogue of unique factorisation is the Jordan–Hölder theorem.

The compression worth keeping: a simple group is *unquotientable* — it is to groups what a prime is to integers. But there is a twist that makes the analogy instructive rather than glib. Among integers the primes are the *simple* objects in the colloquial sense, small and easily listed. Among groups the simple groups are the *hardest* objects, because every tool of §1.2 is a tool for *breaking groups apart*, and a simple group is precisely the thing those tools cannot touch. So "simple" is a misnomer if read as "easy": it means *indecomposable*, and indecomposable groups can be enormous and intricate (the Monster, a sporadic simple group, has order roughly $8 \times 10^{53}$).

---

# Examples / Corollaries

**Is an instance — the cyclic group $C_p$ of prime order.** For a prime $p$, the cyclic group $C_p$ is simple. By [[Thm - Lagrange's Theorem|Lagrange]], the order of any subgroup divides $|C_p| = p$, hence is $1$ or $p$, so the only subgroups at all are $\{e\}$ and $C_p$; *a fortiori* the only normal subgroups are $\{e\}$ and $C_p$. The $C_p$ are the **abelian** simple groups — and in fact the *only* ones: an [[Def - Abelian Group|abelian]] simple group must be $C_p$ for some prime $p$ (see [[Thm - Abelian Simple Groups are Cyclic of Prime Order]]). The reason the abelian case is so easy is structural: in an abelian group *every* subgroup is automatically normal, so simplicity collapses to "no proper non-trivial subgroup at all", which by Lagrange forces prime order.

**Is an instance — the alternating group $A_n$ for $n \geq 5$.** The alternating group $A_n$ is simple for every $n \geq 5$; $A_5$, of order $60$, is the smallest non-abelian simple group. These are the first infinite family of non-abelian simple groups. $A_5$ has plenty of proper non-trivial *subgroups* — copies of $C_2, C_3, C_5, S_3, A_4$ — but *none of them is normal*, which is exactly why it is simple and why proving so (a conjugacy-class argument) is genuine work, far harder than the abelian case.

**Is NOT an instance — $C_4$, the cyclic group of order $4$.** $C_4$ is *not* simple: it has the subgroup $\{e, g^2\} \cong C_2$, which — since $C_4$ is abelian — is normal, and is proper and non-trivial. So $C_4$ can be quotiented: $C_4/C_2 \cong C_2$. More generally $C_n$ is simple if and only if $n$ is prime; a composite order always supplies a proper non-trivial (normal) subgroup. This contrasts sharply with the $C_p$ example and shows simplicity is a property of the *order's primality*, in the abelian world.

**Is NOT an instance — the symmetric group $S_n$ for $n \geq 3$.** No $S_n$ with $n \geq 3$ is simple: the alternating group $A_n$ is a proper non-trivial [[Def - Normal Subgroup|normal subgroup]] (it has index $2$, and index-$2$ subgroups are always normal). So $S_n$ can be split, $S_n/A_n \cong C_2$. Even though $A_5$ *itself* is simple, the larger group $S_5$ is not — simplicity is not inherited upward.

**Is NOT an instance — the trivial group $\{e\}$.** By the explicit non-triviality clause, $\{e\}$ is *not* simple, just as $1$ is not prime. This exclusion is deliberate and necessary: it is what makes the [[Thm - Composition Series|composition series]] terminate well-definedly and its factor multiset an invariant.

**Corollary — simple groups have no normal subgroups to quotient, so they are the leaves of every composition series.** A [[Thm - Composition Series|composition series]] of a finite group is a chain $G = H_1 \trianglerighteq H_2 \trianglerighteq \cdots \trianglerighteq H_n = \{e\}$ with every quotient $H_i/H_{i+1}$ simple. The simple groups are the *composition factors* — the "prime factorisation" of $G$ — and a group is simple precisely when its own composition series has length one.

**Corollary — homomorphisms out of a simple group are trivial or injective.** Since $\ker\varphi \trianglelefteq G$ and the only normal subgroups of a simple $G$ are $\{e\}$ and $G$, any [[Def - Homomorphism|homomorphism]] $\varphi$ from a simple group has $\ker\varphi = \{e\}$ (so $\varphi$ is injective, by the [[Def - Kernel and Image|injectivity criterion]]) or $\ker\varphi = G$ (so $\varphi$ is the trivial map). There is no middle ground — a frequently used dichotomy in proving non-simplicity of *other* groups.

**Calibration check.** Confirm $C_6$ is not simple by exhibiting a proper non-trivial normal subgroup, and confirm $C_7$ is simple. Explain why "$\{e\}$ is not simple" is part of the definition rather than a theorem. If you can also explain why the all-subgroups version of the definition would coincide with the normal-subgroups version for abelian groups but not in general, you have understood why simplicity is phrased with normal subgroups.

---

# Unlocked by This

> [!tip] The Classification of Finite Simple Groups *(from advanced Group Theory)*
> The single most monumental theorem in algebra: **every finite simple group** is one of (i) a cyclic group $C_p$ of prime order, (ii) an alternating group $A_n$ for $n \geq 5$, (iii) a group of Lie type, or (iv) one of $26$ exceptional *sporadic* groups (the largest being the Monster, of order $\approx 8\times 10^{53}$). The proof runs to tens of thousands of journal pages assembled over decades. It is the "periodic table" of finite group theory, and this definition is the entry it classifies.

> [!tip] Composition Series and the Jordan–Hölder Theorem *(from Group Theory III)*
> Every finite group decomposes, via a [[Thm - Composition Series|composition series]], into a multiset of simple composition factors, and the Jordan–Hölder theorem says that multiset is an invariant of the group. Simple groups are exactly the indivisible factors of this decomposition.

> [!tip] Solvable Groups and Galois' Theorem *(from Galois Theory)*
> A group is *solvable* when all its composition factors are abelian — equivalently all of the form $C_p$. Galois' theorem states a polynomial is solvable by radicals exactly when its Galois group is solvable; the non-solvability of $A_5$ is precisely why the general quintic has no radical formula.
