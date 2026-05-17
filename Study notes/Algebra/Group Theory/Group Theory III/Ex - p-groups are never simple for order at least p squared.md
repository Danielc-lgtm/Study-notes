---
type: exercise
subject: group-theory
difficulty: "⭐"
prereqs:
  - "Def - p-group"
  - "Def - Simple Group"
  - "Def - Normal Subgroup"
  - "Def - Centraliser and Centre"
  - "Def - Abelian Group"
  - "Thm - p-Groups Have Non-Trivial Centre"
  - "Thm - Subgroups of a p-Group"
  - "Thm - Lagrange's Theorem"
tags: [algebra, group-theory]
---

# Problem Statement

Let $p$ be a prime and let $n \geq 2$. Show that no group of order $p^n$ is **simple** — equivalently, every [[Def - p-group|p-group]] of order at least $p^2$ has a proper, non-trivial [[Def - Normal Subgroup|normal subgroup]].

**Recall:**

The objects in play are a $p$-group, simplicity, the centre, and normal subgroups.

A [[Def - p-group|p-group]] is a finite group of order $p^n$ for a prime $p$ and $n \geq 1$.

![[Def - Simple Group#The Definition]]

So to prove $G$ is *not* simple, it suffices to exhibit a single normal subgroup $N$ with $N \neq \{e\}$ and $N \neq G$ — a normal subgroup that is *proper* (not the whole group) and *non-trivial* (not just the identity).

![[Def - Centraliser and Centre#The Definition]]

Two standard facts about the centre will be used. The centre $Z(G)$ is always a [[Def - Normal Subgroup|normal subgroup]] of $G$: it is a subgroup, and $gZ(G)g^{-1} = Z(G)$ because central elements are fixed by every conjugation. And by [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial centre theorem]], a non-trivial finite [[Def - p-group|p-group]] has $Z(G) \neq \{e\}$.

---

# Convergent Strategy

**Problem class.** This is a *prove a group is not [[Def - Simple Group|simple]]* problem — the dominant target of the whole topic, as the [[Group Theory III — §1.5–1.7#Sources and Targets|Sources and Targets]] section records. For a general order one runs the Sylow playbook; but when the order is a *prime power* the problem is far easier, because a [[Def - p-group|p-group]] hands you a normal subgroup almost for free. This exercise is the cleanly-stated reason that $p$-groups never appear on the list of candidate simple-group orders.

**Assumption pattern.** Two hypotheses. The order is a prime power $p^n$, which triggers [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial centre theorem]] — the source of a ready-made normal subgroup, since the centre is always normal. And $n \geq 2$, which guarantees the group is *strictly larger than* a group of order $p$; this is the hypothesis that gives the constructed normal subgroup room to be *proper*. Without $n \geq 2$ the claim is simply false: a group of order $p$ is simple, having no subgroups at all besides $\{e\}$ and itself.

**Theorem routing.** The centre $Z(G)$ is always a normal subgroup, and [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial centre theorem]] makes it non-trivial. If $Z(G) \neq G$, it is already the proper non-trivial normal subgroup we need, and we are done. The only escape is $Z(G) = G$, i.e. $G$ [[Def - Abelian Group|abelian]]; in that case route through [[Thm - Subgroups of a p-Group|the subgroup theorem for p-groups]], which produces a subgroup of order $p$, automatically proper (as $p < p^n$) and automatically normal (every subgroup of an abelian group is normal).

**Key decision point.** The non-obvious feature is that the obvious candidate $Z(G)$ *might be all of $G$*, and one must have a backup. The clean move is a case split on whether $Z(G) = G$. If not, $Z(G)$ itself works. If so, the very fact that broke the first plan — $G$ is abelian — *enables* the second: in an abelian group there is no normality obstruction at all, so *any* proper non-trivial subgroup is normal, and [[Thm - Subgroups of a p-Group|the subgroup theorem]] (or just [[Group Theory II — §1.3–1.4|Cauchy's theorem]]) supplies one of order $p$. The lesson is that the troublesome case is never a dead end here: abelian-ness is not an obstacle but a gift, because it makes normality free.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory III — §1.5–1.7#Legal Operations|the topic page's Legal Operations]]:

1. **Apply the class equation** (operation 5), in packaged form. The [[Thm - The Class Equation|class equation]] argument is bottled as [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial centre theorem]], which we invoke to obtain $Z(G) \neq \{e\}$ — the candidate normal subgroup.

2. **Produce a normal subgroup and check it is proper.** The defining task of a non-simplicity proof is to exhibit one proper non-trivial [[Def - Normal Subgroup|normal subgroup]]. Here the candidate is $Z(G)$, normal automatically; the work is the case analysis confirming a *proper* one exists.

3. **Quotient-by-a-central-element machinery** (operation 6), used only for its existence half. In the abelian case we do not quotient and induct — we simply take a central element of order $p$, exactly as [[Thm - Subgroups of a p-Group|the subgroup theorem]] does, and the subgroup it generates is the proper non-trivial normal subgroup.

4. **Constrain orders by Lagrange.** [[Thm - Lagrange's Theorem|Lagrange's theorem]] underlies two steps: $|Z(G)|$ divides $p^n$, and a subgroup of order $p$ is proper because $p < p^n$ when $n \geq 2$.

---

# Hints

> [!note]- Hint 1
> To prove a group is not [[Def - Simple Group|simple]] you need just one proper non-trivial [[Def - Normal Subgroup|normal subgroup]]. The order is a prime power — what subgroup does a [[Def - p-group|p-group]] always come equipped with, that is automatically normal?

> [!note]- Hint 2
> The centre $Z(G)$ is always normal, and by [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial centre theorem]] it is non-trivial. So if $Z(G) \neq G$ you are finished immediately. The only thing to worry about is the case $Z(G) = G$.

> [!note]- Hint 3
> If $Z(G) = G$ then $G$ is [[Def - Abelian Group|abelian]]. In an abelian group *every* subgroup is normal, so you just need any proper non-trivial subgroup. Use [[Thm - Subgroups of a p-Group|the subgroup theorem for p-groups]] to get a subgroup of order $p$ — it is proper because $p < p^n$ for $n \geq 2$, and normal because $G$ is abelian.

---

# Solution

The strategy is to offer $Z(G)$ as the proper non-trivial normal subgroup, with a case split as backup: $Z(G)$ is always normal and ([[Thm - p-Groups Have Non-Trivial Centre|by the centre theorem]]) non-trivial, so the only way it fails to finish the proof is $Z(G) = G$ — and in that case $G$ is abelian and a subgroup of order $p$ does the job.

**Step 1: The centre is normal and non-trivial.**

For any group, $Z(G)$ is a normal subgroup. As $G$ is a $p$-group with $n \geq 2 \geq 1$, the centre is also non-trivial: $Z(G) \neq \{e\}$.

> [!note]- Derivation
> The [[Def - Centraliser and Centre|centre]] $Z(G)$ is a subgroup of $G$ (it contains $e$ and is closed under products and inverses, since elements commuting with everything are stable under those operations). It is moreover a [[Def - Normal Subgroup|normal]] subgroup: for any $g \in G$ and $z \in Z(G)$, the conjugate $gzg^{-1}$ equals $z$ — because $z$ commutes with $g$, so $gzg^{-1} = gg^{-1}z = z$ — and hence $gZ(G)g^{-1} = Z(G)$. Normality holds for the centre of *every* group, with no hypothesis on $G$.
>
> Now use the hypothesis. The order is $|G| = p^n$ with $n \geq 2$, so $G$ is a [[Def - p-group|p-group]] and, since $|G| = p^n \geq p^2 > 1$, it is non-trivial. [[Thm - p-Groups Have Non-Trivial Centre|The non-trivial centre theorem]] then gives
> $$Z(G) \neq \{e\}.$$
> So $Z(G)$ is a normal subgroup that is certainly not trivial. The only remaining question is whether it is *proper*.

**Step 2: If $Z(G) \neq G$, the centre is the required subgroup.**

When $Z(G)$ is a proper subgroup, it is at once proper, non-trivial, and normal — exactly what is needed, and $G$ is not simple.

> [!note]- Derivation
> Suppose $Z(G) \neq G$. Collecting the three properties: by Step 1 the centre $Z(G)$ is [[Def - Normal Subgroup|normal]] in $G$ and satisfies $Z(G) \neq \{e\}$, and by the assumption of this case $Z(G) \neq G$. So $Z(G)$ is a normal subgroup that is neither $\{e\}$ nor $G$ — a *proper non-trivial* normal subgroup.
>
> The definition of a [[Def - Simple Group|simple]] group is one whose only normal subgroups are $\{e\}$ and itself. The existence of $Z(G)$ as a normal subgroup different from both shows $G$ fails that definition. Hence $G$ is not simple.

**Step 3: If $Z(G) = G$, then $G$ is abelian, and a subgroup of order $p$ works.**

When $Z(G) = G$ the group is abelian, so every subgroup is normal; [[Thm - Subgroups of a p-Group|the subgroup theorem]] supplies a subgroup of order $p$, which is proper (as $p < p^n$) and non-trivial.

> [!note]- Derivation
> Suppose instead $Z(G) = G$. By the definition of the [[Def - Centraliser and Centre|centre]], $Z(G) = G$ means every element of $G$ commutes with every other, so $G$ is [[Def - Abelian Group|abelian]].
>
> In an abelian group, *every* subgroup is [[Def - Normal Subgroup|normal]]: for any subgroup $H$ and any $g \in G$, the conjugate $gHg^{-1} = \{ghg^{-1} : h \in H\} = \{h : h \in H\} = H$, since $ghg^{-1} = h$ by commutativity. So the normality obstruction disappears entirely — to finish, it is enough to produce *any* proper non-trivial subgroup.
>
> [[Thm - Subgroups of a p-Group|The subgroup theorem for p-groups]] states that a group of order $p^n$ has a subgroup of order $p^b$ for every $0 \leq b \leq n$. Apply it with $b = 1$: there is a subgroup $H \leq G$ with $|H| = p$. (Alternatively, take any non-identity $x \in G$; its order divides $p^n$ by [[Thm - Lagrange's Theorem|Lagrange]] and exceeds $1$, so it is some $p^c$ with $c \geq 1$, and $x^{p^{c-1}}$ has order exactly $p$, generating such an $H$.)
>
> This $H$ is:
> - **non-trivial**, since $|H| = p \geq 2 > 1$;
> - **proper**, since $|H| = p$ while $|G| = p^n$ with $n \geq 2$, so $|H| = p < p^2 \leq p^n = |G|$ and $H \neq G$;
> - **normal**, since $G$ is abelian and every subgroup of an abelian group is normal.
>
> So $H$ is a proper non-trivial normal subgroup, and $G$ is not simple. $\blacksquare$

> [!note]- Complete formal solution
> Let $|G| = p^n$ with $p$ prime and $n \geq 2$.
>
> The [[Def - Centraliser and Centre|centre]] $Z(G)$ is a normal subgroup of $G$: it is a subgroup, and for $g \in G$, $z \in Z(G)$ one has $gzg^{-1} = z \in Z(G)$, so $gZ(G)g^{-1} = Z(G)$. Since $|G| = p^n \geq p^2 > 1$, the group $G$ is a non-trivial [[Def - p-group|p-group]], so by [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial centre theorem]], $Z(G) \neq \{e\}$.
>
> *Case 1: $Z(G) \neq G$.* Then $Z(G)$ is a normal subgroup with $Z(G) \neq \{e\}$ and $Z(G) \neq G$ — a proper non-trivial normal subgroup. By definition of a [[Def - Simple Group|simple]] group, $G$ is not simple.
>
> *Case 2: $Z(G) = G$.* Then every element of $G$ commutes with every other, so $G$ is [[Def - Abelian Group|abelian]], and consequently every subgroup of $G$ is [[Def - Normal Subgroup|normal]] (for any subgroup $H$ and $g \in G$, commutativity gives $gHg^{-1} = H$). By [[Thm - Subgroups of a p-Group|the subgroup theorem for p-groups]], $G$ has a subgroup $H$ of order $p$. Then $H$ is non-trivial ($|H| = p > 1$), proper ($|H| = p < p^2 \leq p^n = |G|$ since $n \geq 2$), and normal (as $G$ is abelian). So $G$ has a proper non-trivial normal subgroup and is not simple.
>
> In both cases $G$ is not simple. Hence no group of order $p^n$ with $n \geq 2$ is simple. $\blacksquare$

---

# Key Takeaways

**A $p$-group hands you a normal subgroup before you do any work — that is why $p$-groups are never on the simple-group shortlist.** The general non-simplicity problem is a hunt: factor the order, list candidate $n_p$, chase a prime with $n_p = 1$. None of that is needed for a prime-power order, because [[Thm - p-Groups Have Non-Trivial Centre|the non-trivial centre theorem]] *constructs* a normal subgroup directly — the centre — out of nothing but the order being a prime power. The reusable recognition is: the instant you see an order $p^n$ and a question about normal subgroups or simplicity, write down $Z(G)$, recall it is always normal and (for a $p$-group) non-trivial, and you are most of the way to the answer. This is the structural reason the classification of finite simple groups lists cyclic groups $C_p$ as the only abelian simple groups and never a larger $p$-group: prime-power order $p^n$ with $n \geq 2$ is incompatible with simplicity, and the centre is the witness.

**The obvious candidate may be the whole group — always carry a backup, and watch for the failure case to become the solution.** The natural normal subgroup to offer is $Z(G)$, but $Z(G)$ can equal $G$, and a one-line proof that stops there is incomplete. The disciplined habit is to split on whether the candidate is proper. What makes this particular split elegant is that the bad case is not a dead end: $Z(G) = G$ means $G$ is [[Def - Abelian Group|abelian]], and abelian-ness is precisely the condition under which *every* subgroup is normal — so the property that broke plan A is the property that makes plan B trivial. The transferable pattern: when a construction might degenerate, ask what the degeneration *tells you*, because a strong degenerate hypothesis (here, "abelian") often dissolves the remaining difficulty. This same "abelian kills the normality obstruction" move appears whenever one needs a normal subgroup of an abelian group — there, normality is never the issue and only *existence* of a proper non-trivial subgroup must be checked.

**"Not simple" reduces to one bullet: produce a single proper non-trivial normal subgroup.** It is worth internalising how low the bar for non-simplicity is. A [[Def - Simple Group|simple]] group is defined by having *no* normal subgroups other than $\{e\}$ and itself, so its negation is satisfied by the existence of just *one* normal subgroup that is neither — proper and non-trivial. Every non-simplicity proof, from this prime-power case to the hardest Sylow argument, terminates at exactly this point: name one such subgroup and verify the two adjectives, *proper* (not $G$) and *non-trivial* (not $\{e\}$). Keeping that endpoint sharply in view tells you what to aim at — you are never asked to classify all normal subgroups, only to find one good one — and it tells you what to check: the two ways a candidate can fail are by being everything or by being nothing, and both must be excluded, here by $n \geq 2$ ensuring $p < p^n$ and by the centre theorem ensuring non-triviality.
