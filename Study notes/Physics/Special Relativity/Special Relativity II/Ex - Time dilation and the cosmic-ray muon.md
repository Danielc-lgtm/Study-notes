---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Time Dilation"
  - "Thm - Length Contraction"
  - "Def - Proper Time"
tags: [physics, special-relativity]
---

# Problem Statement

Muons are unstable particles — heavy, short-lived cousins of the electron — created when cosmic rays strike the upper atmosphere, roughly $H = 15\ \text{km}$ above sea level. In their own rest frame a muon has a mean lifetime (half-life) of about $\tau \approx 2 \times 10^{-6}\ \text{s}$. They are produced moving downward at speed $v \approx 0.99c$, giving a Lorentz factor $\gamma \approx 10$ (more precisely $\gamma = (1 - 0.99^2)^{-1/2} \approx 7.1$; we use $\gamma \approx 10$ as Tong does, for the round-number estimate). Restore $c$ throughout, since real numbers are wanted.

1. Compute the time $t$ a muon takes to traverse the atmosphere as measured in the **Earth frame**, treating it as a journey of $15\ \text{km}$ at $0.99c$. Compare with $\tau$: naively, how many half-lives is this, and what fraction of muons would survive if there were no relativistic effect?
2. Resolve the puzzle in the **muon's rest frame**: show that the journey lasts only $t' = t/\gamma$ of the muon's proper time, that this is *less* than a half-life, and that a large fraction therefore survives. Identify which time is the proper time and which the dilated coordinate time.
3. Resolve the *same* puzzle in the **Earth frame** by length contraction instead of time dilation: the muon's lifetime is dilated to $\gamma\tau$ in the Earth frame, so it travels $\gamma\tau \cdot v$ before decaying — show this exceeds $15\ \text{km}$. Verify that the muon-frame and Earth-frame accounts agree.
4. Explain why the effect cannot be attributed to any internal "clock mechanism" of the muon slowing down, and state the magnitude of $\gamma$ for protons in the LHC ($\gamma \approx 3500$) as a calibration of how large these factors get.

**Recall:**

![[Thm - Time Dilation#Statement]]

![[Thm - Length Contraction#Statement]]

The **proper time** ([[Def - Proper Time]]) of the muon is the time between two events on its own worldline measured by a clock carried with it — here, "creation" and "decay" (or "reaching sea level"), which happen at the same place in the muon's frame. The Earth frame and the muon frame must agree on every *observable* fact, in particular on whether the muon reaches the ground.

---

# Convergent Strategy

**Problem class.** A *compute-an-effect plus two-frame-consistency* problem — the textbook demonstration that time dilation is real and that one observable has two equally valid frame-descriptions. The [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction#Problem-Solving Strategy|topic strategy]] says: identify the rest frame (the muon's), recognise its lifetime as a proper time, and then check the orthogonal frame for consistency.

**Assumption pattern.** The decisive datum is "rest-frame lifetime $\tau$": this is a proper time, because creation and decay occur at the same place in the muon's frame. The naive paradox ("muons can't survive the trip") arises from misapplying the rest-frame lifetime to the Earth-frame journey time. The resolution is to keep track of which frame measures the lifetime and which measures the distance.

**Theorem routing.** Part 1 is a Newtonian estimate, $t = H/v$, set against $\tau$. Part 2 routes through [[Thm - Time Dilation]]: the muon-frame journey time is $t/\gamma$, and the lifetime $\tau$ is the proper time to compare it against. Part 3 routes through [[Thm - Length Contraction]]: the Earth-frame lifetime is $\gamma\tau$, the distance travelled before decay is $\gamma\tau v$. Part 4 is conceptual — the mechanism-independence of time dilation — plus a calibration figure.

**Key decision point.** The crux is *not* mixing frames: the lifetime $\tau$ is measured in the muon frame and the distance $H$ in the Earth frame, and comparing them directly (part 1) is the error that manufactures the paradox. The non-obvious move is that there are two correct fixes — dilate the lifetime to $\gamma\tau$ and keep $H$ (Earth frame), or contract the distance to $H/\gamma$ and keep $\tau$ (muon frame) — and they must agree. Picking *one frame and staying in it* is the discipline; never compare a proper time in one frame with a distance in another.

---

# Legal Operations Used

1. **Work in the rest frame, then boost out** (operation 2 from the topic page). The muon's lifetime is simplest in its own frame (a proper time); part 2 works there and relates to the Earth frame by $\gamma$.

2. **Use time dilation: a moving clock runs slow by $\gamma$** (operation 3). Part 3's Earth-frame account dilates the muon's lifetime to $\gamma\tau$; the muon is the moving clock.

3. **Use length contraction: a moving rod is short by $\gamma$** (operation 4). Part 2's muon-frame account contracts the $15\ \text{km}$ atmosphere to $H/\gamma$; the atmosphere is the moving "rod".

4. **Compute an invariant in the most convenient frame** (operation 8). The consistency check in part 3 is the statement that the observable "muon reaches the ground" is frame-independent, computed two ways and matched.

---

# Hints

> [!note]- Hint 1
> Earth-frame time: $t = H/v = 15\ \text{km} / (0.99 \times 3\times10^5\ \text{km/s}) \approx 5\times10^{-5}\ \text{s}$. (Tong rounds the geometry to give $\approx 7\times10^{-6}\ \text{s}$ for a shorter effective path / lower altitude; either way the point is $t \gg \tau$.) Compare with $\tau = 2\times10^{-6}\ \text{s}$: that is many half-lives, so without relativity the surviving fraction $2^{-t/\tau}$ would be astronomically small.

> [!note]- Hint 2
> In the muon's frame, the muon is at rest and the *atmosphere rushes past*. The journey time in the muon frame is the Earth-frame time divided by $\gamma$ (the muon's clock runs slow as seen from Earth, so conversely the muon's own elapsed time is shorter): $t' = t/\gamma$. Compare *this* with the muon's lifetime $\tau$, which is itself a muon-frame (proper) time — now you are comparing two times measured in the same frame.

> [!note]- Hint 3
> In the Earth frame, do not change the distance; change the lifetime. The muon is a moving clock, so its lifetime is dilated: it lives, in Earth-frame time, for $\gamma\tau$. In that time it travels $\gamma\tau \cdot v$. Plug in $\gamma\approx 10$, $\tau = 2\times10^{-6}\ \text{s}$, $v \approx 3\times10^5\ \text{km/s}$ and compare with $15\ \text{km}$.

> [!note]- Hint 4
> The derivation of time dilation used nothing about *how* the muon decays — no internal spring, gear, or pendulum. A muon is structureless. So the slowing cannot be mechanical; it is time itself running slow. For scale: LHC protons have $\gamma \approx 3500$, and their unstable decay products live $3500\times$ longer in the lab than at rest — routinely exploited and confirmed.

---

# Solution

Naively the muon should decay long before reaching the ground; it does not, because time dilation (Earth frame) extends its lifetime, or equivalently length contraction (muon frame) shortens its journey. The two frames disagree about lifetimes and distances but agree on the observable fact that muons reach sea level.

**Step 1: The naive Earth-frame estimate predicts the muon cannot survive.**

> [!note]- Derivation
> The Earth-frame transit time for a $15\ \text{km}$ descent at $v = 0.99c$ is
> $$t = \frac{H}{v} = \frac{15\ \text{km}}{0.99 \times 3\times10^5\ \text{km/s}} \approx 5.1\times10^{-5}\ \text{s}.$$
> (Following Tong's round-number version with a shorter effective path, one gets $t \approx 7\times10^{-6}\ \text{s}$; the qualitative point is identical.) Set against the muon's rest-frame half-life $\tau \approx 2\times10^{-6}\ \text{s}$, this is
> $$\frac{t}{\tau} \approx \frac{5\times10^{-5}}{2\times10^{-6}} \approx 25 \ \text{half-lives} \qquad(\text{or } \approx 3.5 \text{ in Tong's version}).$$
> If the rest-frame lifetime applied directly to the Earth-frame journey, the surviving fraction would be $2^{-t/\tau}$ — utterly negligible (even $2^{-3.5} \approx 0.09$ in the conservative version, and $2^{-25} \approx 3\times10^{-8}$ in the literal one). Either way, far too few muons would reach the ground to match the abundant flux actually detected. **This is the paradox**, and its source is comparing a muon-frame lifetime with an Earth-frame travel time — two different frames.

**Step 2: In the muon frame, the journey is short and most muons survive.**

> [!note]- Derivation
> Transform to the muon's rest frame. The muon is now at rest and the atmosphere sweeps up past it at $0.99c$. The journey time in this frame is the Earth-frame time *contracted by* $\gamma$ — equivalently, the muon's own clock reads less than the Earth's by $\gamma$:
> $$t' = \frac{t}{\gamma} \approx \frac{7\times10^{-6}\ \text{s}}{10} \approx 7\times10^{-7}\ \text{s}$$
> (using Tong's $t \approx 7\times10^{-6}\ \text{s}$ and $\gamma \approx 10$). Now compare with the muon's lifetime $\tau = 2\times10^{-6}\ \text{s}$ — and crucially, *both* are muon-frame times, so the comparison is legitimate. Since $t' \approx 7\times10^{-7}\ \text{s} < \tau$, the journey lasts **less than one half-life**, and a large fraction of muons survive ($2^{-t'/\tau} \approx 2^{-0.35} \approx 0.78$). The muon-frame picture: the muon does not live unusually long; the atmosphere is unusually *thin*, contracted to $H/\gamma \approx 1.5\ \text{km}$, and crossing $1.5\ \text{km}$ at $0.99c$ takes only $5\times10^{-6}\ \text{s}$ of muon-frame time, comfortably within its lifetime. The proper time here is $t'$ (the muon's own elapsed time); the dilated coordinate time is $t$ (the Earth's).

**Step 3: The Earth frame agrees, via length contraction $\leftrightarrow$ time dilation.**

> [!note]- Derivation
> Now redo the Earth-frame account *correctly*, dilating the lifetime instead of misapplying it. The muon is a moving clock, so its lifetime in Earth-frame time is dilated ([[Thm - Time Dilation]]):
> $$\tau_{\text{Earth}} = \gamma\tau \approx 10 \times 2\times10^{-6}\ \text{s} = 2\times10^{-5}\ \text{s}.$$
> In that dilated lifetime it travels
> $$d = \gamma\tau \cdot v \approx 2\times10^{-5}\ \text{s} \times 0.99 \times 3\times10^5\ \text{km/s} \approx 6\ \text{km}$$
> per half-life, so over a couple of half-lives it easily covers the $15\ \text{km}$ (with the expected exponential attrition). *Consistency check.* The two accounts must agree, and they do: the muon frame contracts the distance to $H/\gamma$ and keeps the lifetime $\tau$, requiring $H/\gamma \lesssim v\tau$; the Earth frame keeps the distance $H$ and dilates the lifetime to $\gamma\tau$, requiring $H \lesssim v\gamma\tau$. These two conditions are *identical* — multiply the first by $\gamma$ — so both frames agree on the observable: the muon reaches the ground. One frame credits a slow clock, the other a short path, and the single factor $\gamma$ reconciles them. **The muon reaching sea level is frame-independent; only the explanation differs.**

**Step 4: The slowing is in time itself, not in the muon.**

> [!note]- Derivation
> The [[Thm - Time Dilation|time-dilation]] derivation used only the constancy of $c$ and the Lorentz transformation — *nothing* about the muon's internal workings, because it has none: a muon is an elementary, structureless particle with no springs, gears, or pendulum to run slow. Its decay is governed by quantum mechanics, not by a clock mechanism, yet it lives exactly $\gamma$ times longer when moving fast. The only consistent reading is that **time itself runs slow** in the muon's frame as seen from Earth; the muon's decay merely reports this faithfully, as would any process. For calibration of the scales involved: protons circulating in the LHC have $\gamma \approx 3500$, and the unstable particles produced in its collisions live thousands of times longer in the laboratory than in their rest frames — a daily, quantitatively confirmed working tool of particle physics, not a thought experiment.

> [!note]- Complete formal solution
> Earth-frame transit time $t = H/v \approx 7\times10^{-6}$–$5\times10^{-5}\ \text{s}$ exceeds the rest-frame half-life $\tau = 2\times10^{-6}\ \text{s}$ by several half-lives, so a direct application of $\tau$ to the journey predicts negligible survival — the paradox, caused by mixing a muon-frame lifetime with an Earth-frame distance. In the muon frame the journey takes $t' = t/\gamma \approx 7\times10^{-7}\ \text{s} < \tau$ (equivalently the atmosphere is contracted to $H/\gamma \approx 1.5\ \text{km}$), so most muons survive. In the Earth frame the lifetime is dilated to $\gamma\tau \approx 2\times10^{-5}\ \text{s}$, over which the muon travels $\gamma\tau v \approx 6\ \text{km}$ per half-life, covering $15\ \text{km}$ in a few half-lives. The two accounts agree because $H/\gamma \le v\tau \Leftrightarrow H \le v\gamma\tau$; both predict the muon reaches the ground, differing only in whether they credit a slow clock or a short path. The effect is not mechanical — a structureless muon has no internal clock — but a property of time itself, with $\gamma \approx 3500$ for LHC protons illustrating the scales reached. $\blacksquare$

---

# Key Takeaways

**The signature of a proper time is "two events at the same place", and a rest-frame lifetime always is one.** The muon's lifetime $\tau$ is a proper time because the muon's creation and decay happen at the same place in the muon's own frame — the muon is present at both. This is the universal trigger: any duration attached to an object *in its own frame* (a lifetime, a period, the time for an onboard process) is a proper time, and every *other* frame measures the dilated value $\gamma\tau$. The fatal error, which this problem is built to expose, is to take a rest-frame duration and compare it directly to a distance or time measured in a *different* frame; that mismatch manufactures every "paradox" of survival. The reflex to build: when you see "in its rest frame it lives $\tau$", immediately label $\tau$ a proper time and ask, before doing anything else, which frame the *other* quantities in the problem are measured in.

**One observable, two frames, one answer — and computing both ways is the surest check.** The deepest lesson of the muon is that "the muon reaches the ground" is a frame-independent fact with two equally valid explanations: the Earth frame says the muon's lifetime is dilated so it survives the long trip; the muon frame says the atmosphere is contracted so the trip is short. Neither is "more true"; they are the same physics sliced two ways, reconciled by the single factor $\gamma$ appearing once in each (dilating a time in one frame, contracting a length in the other). This is the prototype of the most reliable error-check in all of relativity: compute any genuine observable in two frames and verify the answers match — if they don't, a frame has been mixed somewhere. The condition $H/\gamma \le v\tau$ (muon frame) and $H \le v\gamma\tau$ (Earth frame) being algebraically identical is the check made explicit, and it is worth performing on every two-frame problem as a matter of habit.

**Time dilation is a property of time, proven by the muon's lack of moving parts.** Because the muon is structureless — no internal mechanism that motion could jam — its extended lifetime cannot be a mechanical artefact, and this is the cleanest possible argument that time dilation afflicts *time itself* rather than clocks. The same logic elevates the effect from a quirk of measuring instruments to a statement about the geometry of spacetime: the muon's decay, a beating heart, an atomic transition, and a quartz oscillator all dilate by the identical $\gamma$, because what slows is the parameter (proper time) all of them advance along. This is why the effect scales without limit — $\gamma \approx 10$ for atmospheric muons, $\approx 3500$ for LHC protons, $\approx 2\times10^5$ for the electrons of LEP — and why particle physicists size their detectors to the *dilated* decay length $\gamma v\tau$ of the unstable particles they produce. Carry away that "moving clocks run slow" is shorthand for "proper time elapses more slowly along a fast worldline", a fact about spacetime, not about hardware; see [[Ex - The light clock and the interval derivation of time dilation]] for the mechanism-free derivations that make this inescapable.
