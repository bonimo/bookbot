# IDEOLOGIES_DRAFT.md (v0.3, 40 cards, influence payoff bumped 1.5x)

## Scale

Each axis runs -100 (full Influence pole) to +100 (full Control pole), 0 = neutral start. Cards never show a negative number, they name the actual pole and always give a positive amount. The engine converts pole name to axis + sign:

| Pole named on card | Axis | Effect on axis |
|---|---|---|
| Military | military | + (toward Control) |
| Contentment | military | - (toward Influence) |
| Government | government | + (toward Control) |
| Culture | government | - (toward Influence) |
| Capital | capital | + (toward Control) |
| Labor | capital | - (toward Influence) |

**Momentum:** Military, Government, Capital effects apply instantly. Contentment, Culture, Labor effects ramp over several ticks.

**Payoff asymmetry:** total Influence-pole payoff is 1.5x the equivalent Control-pole payoff, so the ramp is worth waiting for, not just a same-turn undo. Control tiers: 10 / 20 / 30 (instant). Influence tiers: 15 / 30 / 45 (ramped).

## Control-leaning

| # | Ideology | Effect | Fiction |
|---|---|---|---|
| 1 | Conscription Doctrine | Military +30 | Mandatory service swells the ranks and quells dissent through discipline. |
| 2 | Martial Curfew | Military +20 | Nightly curfews suppress unrest fast, and are resented quietly. |
| 3 | Codified Legal Order | Government +30 | Dense law and policing tighten the state's grip on daily life. |
| 4 | Loyalty Oaths | Government +20 | Public adherence is required and enforced. |
| 5 | Consolidate Industry | Capital +30 | Ownership concentrates in a select few, output rises, poverty deepens. |
| 6 | Company Towns | Capital +20 | Workers depend entirely on employer-controlled housing and wages. |
| 21 | Border Fortification | Military +20 | Fortified borders project strength and deter unrest through visible readiness. |
| 22 | State Broadcast Network | Government +30 | A single approved narrative reaches every household, dissent has nowhere to hide. |
| 23 | Resource Nationalization | Capital +20 | The state seizes key industries outright, wealth funnels upward fast. |
| 24 | Mandatory Registration | Government +10 | Every citizen is catalogued and accounted for. |

## Influence-leaning (amounts bumped 1.5x)

| # | Ideology | Effect | Fiction |
|---|---|---|---|
| 7 | Public Assemblies | Contentment +30 | The state steps back, lets people gather and speak freely. |
| 8 | Veterans' Grievance Council | Contentment +45 | Former soldiers are heard, militarism's grip cools. |
| 9 | Open Ideas Festival | Culture +45 | The state loosens its hold, ideas circulate freely. |
| 10 | Community Self-Governance | Culture +30 | Local councils replace top-down rule. |
| 11 | Profit Sharing Mandate | Labor +45 | Workers gain a real stake in what they produce. |
| 12 | Universal Basic Income | Labor +30 | A floor beneath everyone loosens capital's grip on necessity. |
| 25 | Harvest Festivals | Contentment +30 | Shared celebration builds goodwill the state didn't have to force. |
| 26 | Independent Press Charter | Culture +45 | A free press circulates ideas the state doesn't control, trust grows where fear used to sit. |
| 27 | Worker Cooperatives | Labor +30 | Ownership shifts into the hands of the people doing the work. |
| 28 | Open Petition Rights | Contentment +15 | Grievances get heard before they curdle into resentment. |

## Complex (two axes, influence-pole side of each bumped 1.5x)

| # | Ideology | Effect | Fiction |
|---|---|---|---|
| 13 | Cult of Personality | Government +20, Military +10 | A singular leader-myth binds law and army together, no room left for dissent. |
| 14 | Technocratic Council | Culture +15, Capital +20 | Experts run the state efficiently, but wealth still pools upward. |
| 15 | Popular Front | Contentment +15, Labor +30 | Soldiers and workers unite around shared grievance, a coalition built on trust, not pressure. |
| 16 | State Capitalism | Capital +20, Government +10 | The state and the owning class merge into one machine. |
| 29 | Garrison State | Military +20, Government +10 | Army and law fuse into a single machine, nothing moves without approval. |
| 30 | Enlightened Despotism | Government +20, Contentment +15 | A firm hand governs, but genuine care for public happiness softens the grip. |
| 31 | Solidarity Economy | Labor +30, Contentment +15 | Shared prosperity and shared goodwill reinforce each other. |
| 32 | Oligarch Compact | Capital +20, Culture +15 | Wealth concentrates while the state loosens its cultural grip to keep the deal quiet. |

## Expansion and absorption

| # | Ideology | Effect | Fiction |
|---|---|---|---|
| 17 | Conscript Legions [Absorb via Control] | Military +20 | Faster expansion, larger cultural shock on whoever you absorb. |
| 18 | Missionary Envoys [Absorb via Influence] | Culture +30 | Soft diplomacy wins hearts before you claim any land. Slower, no shock. |
| 33 | Colonial Levy [Absorb via Control] | Military +20 | Conscripted colonial troops swell the ranks fast, at the cost of trust in what you've taken. |
| 34 | Puppet Governance [Absorb via Control] | Government +20 | Installed local rulers answer to you first, the populace second. |
| 35 | Cultural Attaché Corps [Absorb via Influence] | Culture +30 | Diplomats embed early, softening the ground before any claim is made. |
| 36 | Shared Currency Pact [Absorb via Influence] | Labor +30 | Economic ties bind new populations to you gently, without a single soldier. |

## Rival empire interaction

| # | Ideology | Effect | Special | Fiction |
|---|---|---|---|---|
| 19 | Non-Aggression Pact | Contentment +15 | FragmentPressure -20 | A treaty buys time, but the army that isn't marching isn't feared either. |
| 20 | Espionage Network | Government +10 | — | Knowing your neighbor's weak point is its own kind of power. (flavor: rival reveal, not implemented) |
| 37 | Border Skirmish | Military +10 | RevoltPressure +10 | A probing strike shows strength, but risks the very tension you're trying to manage. |
| 38 | Trade Concordat | Labor +15 | — | A trade deal with a neighboring power spreads prosperity at home. |
| 39 | Defector Amnesty | Contentment +15 | FragmentPressure -15 | Welcoming those who flee a rival's control directly relieves the pressure of your own fraying edges. |
| 40 | Joint Military Exercise | Military +10 | RevoltPressure -10 | A show of shared strength with an ally eases domestic tension without a real fight. |

---

## How to hand-test (updated)

- Start all three axes at 0 (neutral).
- Each round, draw 3 random distinct cards, pick 1, apply its effect, advance a tick.
- Win: 2 axes at or beyond +/-70 toward one pole type, 1 axis at or beyond +/-70 toward the opposite pole type, held 3 ticks.
- Loss: RevoltPressure or FragmentPressure reaching 90 (not 100), built from repeated axis extremes, not a single touch.
- Watch specifically for: does the 1.5x influence payoff now make waiting actually feel worth it, or does it need to go higher.
