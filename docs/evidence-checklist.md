# TSA Rail SD 1580/82-2022-01E — CSW Evidence Checklist

A printable worklist for the evidence owner. For each item: **what** to export, **where** from in CSW, and the **cadence**. Tick as you collect; file exports to immutable storage (not screenshots taken during inspection week).

> Legend — 🟢 Direct · 🟠 Supporting · ⚪ Evidence Required *(supplied outside CSW)*. CSW evidence is an input to a TSA inspection, not a finding of compliance.

> **Before you start — two things that change everything downstream:**
> 1. **TSA inspects against your approved Cybersecurity Implementation Plan**, not the SD text. Map every item below to a measure in that plan, or it will not land.
> 2. **Confirm the active revision letter.** This series is renewed annually; 01E runs May 3, 2026 – May 2, 2027.
>
> See §1.2 and §7.4 of the [Reference Design](../CSW-TSA-Rail-Reference-Design.md).

---

## Phase 1 — Coverage (Days 1–10)

- [ ] IT workloads supporting Critical Cyber Systems reconciled to **CSW Inventory** (100% or documented exceptions)
- [ ] Labels applied: `compliance:tsa-rail`, `ccs_id`, `ccs_function`, `zone`, `ot_facing`, `ptc`, `managed_by`, `site`
- [ ] CSW scope tree created and **matched to the zone model in the approved plan** (III.B.1.c)
- [ ] **PTC back office** identified and labelled `ptc:true` (III.A.2 — mandatory CCS)
- [ ] Under-scoping check: **business services** whose loss causes operational disruption (crew scheduling, movement planning, consist/waybill) assessed for CCS status
- [ ] `managed_by` applied to every workload an MSSP or Authorized Representative touches (II.A.2–3)
- [ ] **Export:** inventory CSV + agent-status screenshot → `evidence/01-coverage/`

## Phase 2 — Baseline (Days 11–28)

- [ ] ADM running on `OT-Facing-IT` for a full operating cycle (≥ 2 weeks; extend across a maintenance window)
- [ ] **Interdependency list** produced for III.B.1.a
- [ ] **External-connection list** produced for III.B.1.b, with vendor and MSSP paths identified
- [ ] `Plaintext-Crossing-Zones` query run — findings routed to the encryption owner early (III.B.2.b)
- [ ] Unexpected flows documented (shadow IT, vendor egress, scope creep)
- [ ] Asset owners signed the cluster-to-system mapping
- [ ] **Export:** ADM diagram + flow samples with process context → `evidence/02-baseline/`

## Phase 3 — Policy (Days 29–45)

- [ ] Inter-zone default-deny defined per III.B.2.a
- [ ] Every allow rule carries a **business or operational justification** (III.B.1.d)
- [ ] ADM-imported rules refined; **Simulation run ≥ 30 days** for OT-facing tiers (rail traffic is seasonal and schedule-driven)
- [ ] Change tickets raised for false positives; exception register updated
- [ ] **Pre-staged isolation workspace** built for III.D.4 — and tested during a maintenance window, with the test recorded
- [ ] Section VI amendment impact assessed for any change to an approved segmentation measure
- [ ] **Export:** policy export + simulation report + isolation test record → `evidence/03-policy/`

## Phase 4 — Operate (ongoing)

- [ ] Enforcement enabled; negative test recorded in **Denied Connections**
- [ ] SIEM integration verified with sample events
- [ ] Quarterly binder assembled
- [ ] **Export:** enforcement screenshot + quarterly binder → `evidence/04-operate/`

---

## Recurring evidence pack

| # | Evidence item | CSW location | SD provision | Cadence | Collected |
|---|---|---|---|---|:--:|
| 1 | CCS scope + label export | Organize → Scopes | III.A, IV.C.2.a | Per inspection | ☐ |
| 2 | Interdependency map | Investigate → ADM | III.B.1.a | Quarterly | ☐ |
| 3 | External-connection inventory | Flow Search → `External-Connections` | III.B.1.b | Quarterly | ☐ |
| 4 | Zone model export | Scopes + label schema | III.B.1.c | Per plan update | ☐ |
| 5 | Policy workspace export | Defend → Policy Workspaces | III.B.1.d, III.B.2.a | Per inspection | ☐ |
| 6 | Denied Connections log | Defend → Enforcement | III.B.2.a | Continuous | ☐ |
| 7 | Plaintext-crossing-zones report | Flow Search → `Plaintext-Crossing-Zones` | III.B.2.b | Quarterly | ☐ |
| 8 | Simulation report | Defend → Policy Workspaces | III.B, Section VI | Per change | ☐ |
| 9 | Baseline-deviation report | Investigate → ADM diff | III.D.2.b | Monthly | ☐ |
| 10 | Flow + process telemetry | Flow / Process Search | III.D.3.a, IV.C.2.e.i | Continuous | ☐ |
| 11 | **East-west traffic record** | Flow Search, intra-zone filter | **IV.C.2.e.iii** | On request | ☐ |
| 12 | **North-south traffic record** | Flow Search, cross-zone filter | **IV.C.2.e.iv** | On request | ☐ |
| 13 | Isolation test record | `tsa-rail-emergency-isolation` | III.D.4 | Annually + per test | ☐ |
| 14 | KEV exposure report | Investigate → Vulnerability, KEV filter | III.E.2.b | Weekly | ☐ |
| 15 | Compensating-control register | Workspace notes + policy export | III.E.3 | Per exception | ☐ |
| 16 | Architecture-review input pack | ADM + inventory + flow logs | III.F.2.b | Every 2 years | ☐ |
| 17 | Workload inventory | Manage → Inventory | IV.C.2.a | Monthly | ☐ |
| 18 | CSW administrative audit log | Administration → Audit Log | III.D.3.a | Per inspection | ☐ |

Items 1, 5, 6, 11, and 12 are the ones an inspector reaches for first — and 11 and 12 are named verbatim in the SD. Item 7 is the one you want to run before the inspector does.

The full provision-by-provision mapping is in the [Reference Design](../CSW-TSA-Rail-Reference-Design.md).

```
evidence/
├── 01-coverage/   inventory.csv, agent-status.png, scope-export.csv
├── 02-baseline/   adm-map.pdf, interdependencies.csv, external-connections.csv
├── 03-policy/     policy-export.json, simulation-report.pdf, isolation-test.pdf, exceptions.xlsx
└── 04-operate/    QYYYY-Qn/  (quarterly binder: items 1–18)
```

> **SSI handling.** The SD text is not Sensitive Security Information, but **everything submitted to TSA under it is**, per 49 CFR part 1520. Once an export is incorporated into a plan, assessment, or report, store and transmit it as SSI.

---

## Evidence you must collect outside CSW

Do not file these in the CSW evidence tree — but do not forget them either. The inspector will ask.

- [ ] The **TSA-approved Cybersecurity Implementation Plan** itself, and its approval correspondence
- [ ] **Cybersecurity Assessment Plan**, annual update, and annual report (III.F) — including the one-third-per-year / 100%-over-three-years schedule
- [ ] **Cybersecurity Architecture Design Review** conclusions (CSW supplies the inputs; the review is an assessment)
- [ ] Cybersecurity Incident Response Plan and CISA incident reporting records
- [ ] Cybersecurity Coordinator designation
- [ ] **MFA** and authentication evidence, and OT compensating controls (III.C.1, III.C.2)
- [ ] Shared-account management and **domain trust review** records (III.C.4, III.C.5)
- [ ] **PTC locomotive physical security** measures relied upon under III.C.6
- [ ] Email and web/DNS security evidence (III.D.1.a, III.D.1.c)
- [ ] **Packet capture** capability, up to 24 hours as directed by TSA (IV.C.2.e.ii)
- [ ] Perimeter and **IT/OT boundary firewall rulesets** (IV.C.2.b — CSW policy is the workload-tier complement, not a substitute)
- [ ] Authoritative architecture drawings, switch/router configs, VLANs, publicly routable IPs (IV.C.2.c)
- [ ] **OT device layer** evidence in its entirety — from your OT-aware monitoring platform

*Validate sufficiency of every item against your approved plan and your TSA inspector's current guidance. See §7 of the [Reference Design](../CSW-TSA-Rail-Reference-Design.md) for the full evidence boundary.*
