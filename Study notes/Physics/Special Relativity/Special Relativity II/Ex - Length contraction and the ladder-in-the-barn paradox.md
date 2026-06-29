---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Length Contraction"
  - "Def - The Relativity of Simultaneity"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Problem Statement

A ladder of proper length $2L$ is run at speed $v$ towards a barn of proper length $L$ that has a door at each end. We ask: *can the ladder ever be entirely inside the barn, with both doors momentarily shut?* Work with $c = 1$.

1. **The barn's argument.** In the barn frame, compute the contracted length of the ladder and find the condition on $v$ (equivalently $\gamma$) under which the ladder fits entirely inside the barn. Describe the instant when both doors can be shut with the ladder fully enclosed.
2. **The ladder's argument.** In the ladder frame, compute the contracted length of the *barn* and show that the barn is *shorter* than the ladder, so the ladder can never fit. Two correct frames, opposite conclusions — this is the paradox.
3. **The resolution.** Define precisely what "the ladder is inside the barn with both doors shut" means as a pair of *events* (front door and back door each closing momentarily). Show that these two events are *simultaneous in the barn frame but not in the ladder frame*, and that in the ladder frame the far door opens-and-shuts before the near door — so the ladder is never enclosed by *both* shut doors at once in that frame. Resolve the contradiction.
4. Draw (in words, with explicit coordinates) the spacetime diagram in the barn frame: the two door worldlines, the ladder's front and back worldlines, and the barn-frame line of simultaneity on which both ends are inside. Then add the ladder-frame line of simultaneity through the far-door-shut event and show the near end has not yet entered.

**Recall:**

![[Thm - Length Contraction#Statement]]

![[Def - The Relativity of Simultaneity#The Definition]]

The [[Def - The Lorentz Transformation|Lorentz transformation]] relates the barn frame $S$ and the ladder frame $S'$ (ladder moving at $v$ in $S$). "Both doors shut with the ladder inside" is a statement about whether two door-closing events are simultaneous *and* whether the ladder's ends lie between the doors at that instant — and simultaneity is frame-dependent.

---

# Convergent Strategy

**Problem class.** A *resolve-a-paradox* problem — the most famous in the chapter. The [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction#Problem-Solving Strategy|topic strategy]] for paradoxes is diagnostic: locate the unstated assumption (here, that "both doors shut at once" is frame-independent), and the contradiction dissolves.

**Assumption pattern.** Two objects, each moving in the other's frame, each contracting the *other*. The barn frame contracts the ladder; the ladder frame contracts the barn. The buried assumption is that "the ladder is enclosed by both shut doors" means the same thing in both frames — it does not, because it hinges on the simultaneity of the two door-closings.

**Theorem routing.** Parts 1–2 apply [[Thm - Length Contraction]] in each frame, producing the apparent contradiction. Part 3 routes the resolution through [[Def - The Relativity of Simultaneity]]: the two door-closing events, simultaneous in $S$, are non-simultaneous in $S'$, with the far door closing first. Part 4 is the [[Def - The Lorentz Transformation|Lorentz transformation]] applied to the door-closing events and the simultaneity lines, made explicit on a diagram.

**Key decision point.** The crux is realising that "fits inside the barn" is not a property of lengths alone but of *events*: it means there exists an instant at which both ends lie between the doors, equivalently the two doors can be shut simultaneously with the ladder enclosed. "Simultaneously" is the loaded word. Once you treat the two door-closings as events and ask in which frame they coincide, the paradox evaporates: both shut at once (with the ladder inside) in the barn frame; not at once in the ladder frame, where the far door has reopened to let the ladder through before the near door shuts.

---

# Legal Operations Used

1. **Use length contraction: a moving rod is short by $\gamma$** (operation 4 from the topic page). Part 1 contracts the ladder to $2L/\gamma$ in the barn frame; part 2 contracts the barn to $L/\gamma$ in the ladder frame. Each frame contracts the *other* object.

2. **Tilt the line of simultaneity** (operation 5). The resolution is entirely this operation: the two door-closing events lie on a barn-frame simultaneity line but on two different ladder-frame simultaneity lines.

3. **Apply the Lorentz transformation to map events between frames** (operation 1). Part 3 transforms the two door-closing events from $S$ to $S'$ to show their times differ.

4. **Read off geometry from a spacetime diagram** (operation 9). Part 4 plots the door and ladder-end worldlines and the two frames' simultaneity lines, making the resolution visible.

---

# Hints

> [!note]- Hint 1
> Barn frame: the ladder moves at $v$, so its length is $2L/\gamma$. It fits inside the barn (length $L$) when $2L/\gamma \le L$, i.e. $\gamma \ge 2$. At the instant the contracted ladder is centred in the barn, both doors can be shut momentarily with the ladder wholly inside.

> [!note]- Hint 2
> Ladder frame: now the *barn* moves at $v$, so the barn is contracted to $L/\gamma$, while the ladder has its full proper length $2L$. Since $L/\gamma < 2L$ always, the barn is far too short — the ladder can never be enclosed. This flatly contradicts part 1. Do not try to decide which frame is "right"; both are.

> [!note]- Hint 3
> "Both doors shut with the ladder inside" means two events: door $D_1$ (say the far door) momentarily shut, and door $D_2$ (the near door) momentarily shut, *with the ladder between them*. In the barn frame these two closings are simultaneous. Transform them to the ladder frame: are they still simultaneous? Use $\Delta t' = \gamma(\Delta t - v\Delta x)$ with $\Delta t = 0$ and $\Delta x = L$ (the door separation in the barn frame).

> [!note]- Hint 4
> In the ladder frame the far door shuts *first* (and reopens to let the ladder's front through), then later the near door shuts (behind the ladder's back). At no ladder-frame instant are both doors shut *and* the ladder between them — the ladder is always poking through one door or the other. "Is the ladder in the barn?" has no frame-independent answer; what *is* frame-independent is that the ladder is never crushed, and that each door, in turn, is briefly shut when the corresponding end is clear.

---

# Solution

In the barn frame the contracted ladder fits and both doors shut simultaneously around it; in the ladder frame the contracted barn is too short and the ladder never fits. The contradiction is resolved by the relativity of simultaneity: the two door-closings are simultaneous in the barn frame but not in the ladder frame, where the far door closes (and reopens) before the near one.

**Step 1: In the barn frame, the ladder fits if $\gamma \ge 2$.**

> [!note]- Derivation
> In the barn frame $S$, the ladder moves at speed $v$, so by [[Thm - Length Contraction]] its length is
> $$L_{\text{ladder}}^{(S)} = \frac{2L}{\gamma}.$$
> It fits entirely within the barn (proper length $L$, at rest in $S$) when $2L/\gamma \le L$, i.e.
> $$\gamma \ge 2 \quad\Longleftrightarrow\quad v \ge \frac{\sqrt 3}{2} \approx 0.87c.$$
> At the instant when the contracted ladder is centred in the barn, its front end is at the far door and its back end at the near door simultaneously (in $S$), so both doors can be shut at that single $S$-instant with the ladder wholly enclosed and untouched. From the barn's point of view, the answer is an unambiguous **yes, the ladder fits** (for fast enough $v$).

**Step 2: In the ladder frame, the barn is too short.**

> [!note]- Derivation
> Transform to the ladder frame $S'$, where the ladder is at rest with its full proper length $2L$, and now the *barn* moves at speed $v$. By [[Thm - Length Contraction]] the barn is contracted:
> $$L_{\text{barn}}^{(S')} = \frac{L}{\gamma} < L < 2L.$$
> The barn ($L/\gamma$) is shorter than the ladder ($2L$) by a factor of at least $2\gamma$ — even more cramped than the barn frame thought. There is no instant in $S'$ at which both ends of the ladder are inside the barn: the ladder is always sticking out of at least one door. From the ladder's point of view, the answer is an unambiguous **no, the ladder never fits**. Two correct calculations in two valid frames reach opposite conclusions — **the paradox**.

**Step 3: The resolution — the door-closings are not simultaneous in the ladder frame.**

> [!note]- Derivation
> The error is in the question, not the physics: "both doors shut with the ladder inside" secretly assumes the two door-closings happen *at the same time*, and that is frame-dependent. Make the events explicit. In the barn frame $S$, let the far door (at $x = L$) and the near door (at $x = 0$) both shut momentarily at the same instant $t = 0$, with the centred ladder enclosed:
> $$D_{\text{far}} = (t = 0,\ x = L), \qquad D_{\text{near}} = (t = 0,\ x = 0).$$
> These are simultaneous in $S$ ($\Delta t = 0$). Transform to the ladder frame $S'$ using $t' = \gamma(t - vx)$:
> $$t'_{\text{far}} = \gamma(0 - vL) = -\gamma vL, \qquad t'_{\text{near}} = \gamma(0 - 0) = 0.$$
> So in $S'$, $t'_{\text{far}} = -\gamma vL < 0 = t'_{\text{near}}$: the **far door shuts first**, a time $\gamma vL$ *before* the near door. The sequence in the ladder frame is: the far door briefly shuts and *reopens* (while the ladder's front end has not yet reached it, or is passing through), the ladder slides forward through the (now open) far door, and only later does the near door shut behind the ladder's back end. At no $S'$-instant are *both* doors shut with the ladder between them. The ladder is never enclosed in $S'$ — exactly consistent with part 2 — because in $S'$ the "both doors shut" configuration of part 1 is not a single instant but two separated events.
>
> So both frames are right about their *own* observables. The barn frame correctly says: at $t = 0$, both doors are shut and the ladder is inside. The ladder frame correctly says: the doors are never both shut at once, so the ladder is never trapped. There is no contradiction, because "the ladder is inside the barn with both doors shut" is not a frame-independent event — it relies on a simultaneity the two frames do not share. What *both* agree on (the genuine observable) is that the ladder is never crushed: each door, in its turn, is briefly shut only when the nearby end of the ladder is clear of it.

**Step 4: The spacetime diagram.**

> [!note]- Derivation
> Draw the barn frame $S$ with $t$ vertical, $x$ horizontal. The **barn doors** are at rest: vertical worldlines $x = 0$ (near door) and $x = L$ (far door). The **ladder** moves at $v$: its back end follows $x = vt + b$ and its front end $x = vt + b + 2L/\gamma$ (separation $2L/\gamma$, the contracted length), for an offset $b$ chosen so the ladder is centred at $t = 0$, i.e. back end at $x = (L - 2L/\gamma)/2$ and front end at $x = (L + 2L/\gamma)/2$ when $t = 0$. For $\gamma \ge 2$, at $t = 0$ both ends lie in $[0, L]$: the **barn-frame simultaneity line** $t = 0$ (horizontal) cuts both ladder-end worldlines *between* the two door worldlines — the ladder is enclosed, and both doors may shut.
>
> Now overlay a **ladder-frame simultaneity line** through the far-door-shut event $D_{\text{far}} = (0, L)$. In $S$ this line has slope $v$ (it is the locus $t' = \text{const}$, i.e. $t - vx = -vL$, so $t = v(x - L)$). Follow it leftward (decreasing $x$) from $(0, L)$: it rises to *positive* $t$ as $x$ decreases below $L$. Where it crosses the ladder's back-end worldline, the back end is still *outside* the near door — because the ladder-frame "now" through $D_{\text{far}}$ catches the back end before it has entered. So in the ladder's simultaneity, when the far door shuts, the near end has not yet crossed the near door: the ladder straddles the barn, exactly as part 2 requires. The two simultaneity lines — horizontal (barn) and sloped (ladder) — slice the same worldsheet differently, and that single geometric fact is the whole resolution.

> [!note]- Complete formal solution
> Barn frame $S$: the ladder is contracted to $2L/\gamma$, fitting in the barn ($L$) iff $\gamma \ge 2$; at the centred instant $t = 0$ both doors (at $x = 0, L$) can shut simultaneously with the ladder enclosed. Ladder frame $S'$: the barn is contracted to $L/\gamma < 2L$, so the ladder never fits. The resolution is that "both doors shut with the ladder inside" is a claim about two door-closing events $D_{\text{near}} = (0,0)$ and $D_{\text{far}} = (0, L)$, simultaneous in $S$; transforming by $t' = \gamma(t - vx)$ gives $t'_{\text{near}} = 0$, $t'_{\text{far}} = -\gamma vL$, so in $S'$ the far door shuts (and reopens) a time $\gamma vL$ *before* the near door, and the doors are never both shut at once. Hence the barn frame truthfully reports the ladder enclosed at one instant, the ladder frame truthfully reports it never enclosed, and both are consistent because the configuration depends on a simultaneity the frames do not share. The frame-independent observable — the ladder is never crushed — holds in both. On the spacetime diagram, the horizontal barn-frame "now" cuts both ladder ends between the doors, while the sloped ladder-frame "now" through $D_{\text{far}}$ catches the back end still outside the near door. $\blacksquare$

---

# Key Takeaways

**"Fits inside" is a statement about events and simultaneity, not about lengths.** The entire paradox is manufactured by treating "the ladder is inside the barn with both doors shut" as if it were a frame-independent fact about which object is longer. It is not: it is a claim that two door-closing *events* are simultaneous *and* that the ladder's ends lie between the doors at that shared instant — and "simultaneous" is frame-dependent. The instant you recast the verbal claim as a pair of events and ask "in which frame are they simultaneous?", the contradiction dissolves, because the events that coincide in the barn frame are separated in the ladder frame. This is the master technique for every length-contraction paradox (the pole-vaulter, the train-in-the-tunnel, the rivet-and-hole): identify the two events whose simultaneity the verbal puzzle assumes, transform them, and watch the assumption fail. The trigger is any word — "fits", "encloses", "both at once", "before" — that smuggles in a shared "now".

**Each frame contracts the other object, and no frame contracts both — symmetry is the source of the puzzle and the key to it.** The reason the paradox feels forced is that length contraction is *mutual*: in the barn frame the ladder is short, in the ladder frame the barn is short, and there is no frame in which both are short, because each frame sees only the *other* object moving. Recognising this mutuality is the first step in any two-object relativity problem — never contract an object in its own rest frame, and never expect a single frame to contract two objects in relative motion to it differently than their own motion dictates. The symmetric-looking setup (a long thing and a short container) is exactly what makes the contradiction land, and the asymmetry that resolves it is not in the lengths but in the *simultaneity*: the two door-closings have a definite, frame-dependent order, and that order is what the two frames genuinely disagree about. See the [[Ex - The relativity of simultaneity (Einstein's train)|Einstein train]] for the bare simultaneity fact this paradox dresses up.

**Frames disagree about descriptions but agree about observables — find the observable to dissolve the paradox.** The deepest move in resolving any relativistic paradox is to ask what is *actually observable* — what could be photographed — and to confirm both frames agree on it. Here the observable is not "is the ladder inside the barn" (which is frame-dependent and hence not a clean observable) but "is the ladder ever crushed between two shut doors", and both frames answer *no*: in the barn frame the doors shut around the enclosed ladder and reopen without touching it; in the ladder frame each door shuts only when its nearby end is clear. The frame-dependent quantities (lengths, the simultaneity of the closings, whether "the ladder is inside") are bookkeeping; the frame-independent fact (no collision) is physics. Whenever two frames seem to predict contradictory *physical* outcomes, the contradiction is illusory and the resolution is to locate the genuine observable, which all frames must share — if they truly disagreed about an observable, relativity would be inconsistent, and it is not. This is the same principle that reconciles the [[Ex - Time dilation and the cosmic-ray muon|muon's]] two-frame accounts and that underlies the resolution of the [[Ex - The twin paradox|twin paradox]].
