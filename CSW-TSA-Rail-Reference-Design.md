# Cisco Secure Workload — TSA Rail Cybersecurity Compliance Framework
## Reference Design | Freight & Passenger Railroad Owner/Operators

**Version:** 1.0 | **Standard:** TSA Security Directive 1580/82-2022-01E, *Rail Cybersecurity Mitigation Actions and Testing* — effective May 3, 2026 through May 2, 2027

---

> **Coverage legend** — this reference design and its compliance report use three words:
> - 🟢 **Direct** — CSW produces the primary evidence artifact.
> - 🟠 **Supporting** — CSW produces an input that feeds or complements another control.
> - ⚪ **Evidence Required** *(supplied outside CSW)* — CSW produces nothing here; the item is in scope for compliance but out of scope for CSW, so the customer evidences it via another control, tool, or process. A scope boundary, not a gap or "unsupported."

---

## Reader's Guide

**Who this is for.** Freight railroad Owner/Operators subject to
49 CFR 1580.101, TSA-designated freight and passenger railroads, and
rail transit agencies working to the sister SD 1582-21-01 series —
plus the cybersecurity, IT, and OT teams and the TSA inspectors
supporting them.

**Why this framework is unusually good news for CSW.** Most compliance
frameworks require you to argue that network telemetry is relevant
evidence. This one names it. Section IV.C.2.e of the Security
Directive lists, among the records TSA inspectors may demand,
**"East-West Traffic" of Operational Technology systems** and
**"North-South Traffic" between Information and Operational Technology
systems** — and Section VII defines both terms. Section III.B then
makes network segmentation the first substantive requirement. You are
not translating CSW output into the regulator's language; the
regulator is already using it.

**Questions this reference design helps you answer:**

- *Section III.A — do I have a current, defensible inventory of my
  Critical Cyber Systems, including the PTC systems the SD makes
  mandatory?*
- *Section III.B.1 — can I produce the list of IT/OT
  interdependencies, external connections, and zone boundaries the SD
  requires, generated from observed behaviour rather than drawn by
  hand?*
- *Section III.B.2 — can I prove that unauthorized communication
  between zones is actually prevented, not merely prohibited on
  paper?*
- *Section III.D.2.b — can I document and audit communications
  between OT and external systems that deviate from my identified
  baseline?*
- *Section III.F.2.b — when the two-yearly Cybersecurity Architecture
  Design Review needs "verification and validation of network
  traffic," where does that come from?*
- *Section IV.C.2 — when an inspector asks for east-west and
  north-south traffic, what exactly do I hand over?*

**What you'll need.** Your TSA-approved **Cybersecurity
Implementation Plan** (this is the document TSA inspects against — not
the SD itself), your Critical Cyber System register, your current
**Cybersecurity Assessment Plan**, your most recent Cybersecurity
Architecture Design Review, and your PTC system documentation.

**Where to start.** Read §1.2 first — the IT/OT scope boundary
determines what CSW can and cannot claim here, and getting it wrong is
the fastest way to lose an inspector's confidence. §2 maps the SD
provision by provision. §3–4 build the scope tree and the Section
III.B zone-enforcement policy set. §7 is the honest boundary. Go to §6
if you are assembling the evidence package now.

---

## CSW primer — if you are new to Cisco Secure Workload

Cisco Secure Workload (CSW) is a **workload protection platform**. A lightweight **agent** on each server/VM/container observes processes and network flows; **cloud connectors** add AWS/Azure/GCP inventory where agents are not deployed.

| CSW term | Meaning | Why compliance teams care |
|----------|---------|---------------------------|
| **Scope** | Logical boundary (CJI enclave, CDE, OT-facing IT tier) | Defines the systems you must prove are isolated |
| **Label / filter** | Tag or query assigning workloads to scopes | Automates scope membership — reduces drift |
| **ADM** | Application Dependency Mapping from observed traffic | **Live** network/data-flow diagram for inspectors |
| **Workspace** | Policy container for one scope or application | Where allow/deny rules are authored |
| **Monitor → Simulation → Enforce** | Safe rollout sequence | Simulation = change-board evidence before blocking traffic |
| **Denied Connections** | Log of flows blocked by policy | Primary proof that enforcement **operates** |

**Console areas:** Investigate (inventory, flows, vulns) · Defend/Segmentation (policy) · Manage (agents) · Platform (connectors) · Administration (audit log)

**Read next:** [Compliance evidence playbook](https://github.com/chandrapati/CSW-Compliance-Reference-Designs/blob/main/docs/compliance-evidence-playbook.md) (full step-by-step) · [About CSW](https://github.com/chandrapati/CSW-Compliance-Reference-Designs/blob/main/docs/about-csw.md) (platform intro)

---

## Universal evidence workflow

Execute these phases for **this framework's** compliance boundary. Map exports to SD provisions in the **Evidence Package** section below.

| Phase | Goal | Key CSW actions | Typical duration |
|-------|------|-----------------|------------------|
| **1 — Coverage** | Every in-scope workload in CSW | Install agents/connectors; apply compliance labels; create scope | Days 1–10 |
| **2 — Baseline** | Machine-generated flow map | Run ADM ≥2 weeks; export clusters; app-owner signoff | Days 11–28 |
| **3 — Policy** | Designed isolation before enforce | Build workspace; Simulation mode; fix false positives | Days 29–45 |
| **4 — Operate** | Continuous proof between inspections | Enforce; quarterly export pack; ADM refresh every 90 days | Ongoing |

### Phase 1 checklist (coverage)

- [ ] IT workloads supporting Critical Cyber Systems reconciled to CSW Inventory (100% or documented exceptions)
- [ ] Labels applied: `compliance:tsa-rail`, `ccs_id`, `ccs_function`, `zone`, `ot_facing`, `ptc`
- [ ] CSW scope created matching the Cybersecurity Implementation Plan's zone model
- [ ] **Export:** inventory CSV + agent status screenshot

### Phase 2 checklist (baseline)

- [ ] ADM running on the OT-facing IT tier for a full operating cycle (≥2 weeks; extend across a maintenance window)
- [ ] Unexpected flows documented (shadow IT, vendor egress, scope creep)
- [ ] IT/OT interdependencies and external connections enumerated for Section III.B.1
- [ ] App and asset owners signed the cluster-to-system mapping
- [ ] **Export:** ADM diagram + flow samples with process context

### Phase 3 checklist (policy)

- [ ] Default-deny posture defined between zones per Section III.B.2.a
- [ ] ADM-imported rules refined; Simulation run ≥1 week (≥30 days for OT-facing tiers)
- [ ] Change tickets for false-positive fixes; exception register updated
- [ ] **Export:** policy export + simulation report

### Phase 4 checklist (operate)

- [ ] Enforcement enabled on pilot zone; negative test recorded in Denied Connections
- [ ] Quarterly pack: inventory, policy, denies, vulns, audit log (see playbook)
- [ ] SIEM integration verified (sample events)
- [ ] **Export:** enforcement screenshot + quarterly binder

### What CSW evidence does not replace

Multi-factor authentication, shared-account management, domain trust
review, email and web filtering, physical security of locomotive PTC
components, personnel programmes, and the Cybersecurity Implementation
Plan itself still require separate programmes. CSW addresses the
**workload-resident** slice on the **IT side**: segmentation, flows,
process context, vulnerability reachability, and change drift. §7
enumerates the boundary in full.

---

## CSW effectiveness for this framework

- Section III.B.1 interdependency, external-connection, and zone-boundary lists generated from observed behaviour
- Section III.B.2.a inter-zone enforcement with a denied-connections log proving the control operates
- Section III.D.2.b baseline-deviation detection for OT-to-external communications
- Section IV.C.2.e east-west and north-south traffic records, which the SD names explicitly

**Compared to manual programmes:** a railroad's network diagram is
typically accurate on the day it is drawn and progressively less so
afterwards, while the Cybersecurity Assessment Plan requires that at
least one-third of the plan's measures be assessed every year and
100 percent over three years. CSW ties the evidence to **live workload
behaviour** and regenerates it on demand, which is what turns an
annual assessment from an archaeology project into a query.

---

## 1. Overview

**Security Directive 1580/82-2022-01E**, *Rail Cybersecurity
Mitigation Actions and Testing*, imposes mandatory, performance-based
cybersecurity requirements on freight railroad carriers identified in
49 CFR 1580.101 and on additional TSA-designated freight and passenger
railroads. The requirements were first issued in October 2022 and have
been renewed annually since; revision **E** is effective **May 3, 2026
through May 2, 2027**.

Unlike most frameworks in this series, the SD does not prescribe
controls directly. It requires the Owner/Operator to establish a
**TSA-approved Cybersecurity Implementation Plan** describing the
specific measures and schedule for achieving the outcomes in Sections
III.A through III.E, plus a **Cybersecurity Assessment Plan** under
Section III.F. **The approved plan — not the SD — is what TSA inspects
against.** Every CSW artifact in this design should therefore be
mapped to a measure in your plan, not to the SD text alone.

### 1.1 What the SD requires

| Provision | Requirement |
|---|---|
| **III.A** | Identify Critical Cyber Systems. **PTC systems are mandatory** Critical Cyber Systems for operators required to install or voluntarily operating PTC |
| **III.B** | Network segmentation policies and controls preventing operational disruption to OT if IT is compromised, **or vice versa** — including interdependency, external-connection, and zone-boundary documentation |
| **III.C** | Access control measures for local and remote access, covering authentication, MFA, least privilege, shared accounts, and domain trusts |
| **III.D** | Continuous monitoring and detection, including baseline-deviation auditing and the ability to isolate OT when an IT incident creates risk |
| **III.E** | Reduce risk of exploitation of unpatched systems, prioritizing the **CISA Known Exploited Vulnerabilities Catalog** |
| **III.F** | Cybersecurity Assessment Plan — architecture design review within 12 months then at least every two years; **one-third of measures assessed annually, 100 percent over three years**; annual report to TSA |

A defined term worth noting early: a **Critical Cyber System** is "any
Information or Operational Technology system or data that, if
compromised or exploited, could result in **operational disruption**,"
and the definition explicitly **includes business services**. Crew
scheduling, consist and waybill management, and movement planning can
therefore be Critical Cyber Systems even though they are not
signaling systems. Railroads routinely under-scope here.

### 1.2 The IT/OT scope boundary — read this before claiming anything

**CSW is a workload protection platform for IT estate** — servers,
virtual machines, containers, and cloud workloads. CSW does **not**
enforce policy on wayside interface units, signal and interlocking
controllers, locomotive onboard PTC hardware, grade-crossing
predictors, or any other Level 0–2 device. It does not perform deep
packet inspection of rail or OT protocols.

CSW's contribution is on the **IT side of the IT/OT boundary** and
within the IT systems that support rail operations. For rail that is a
substantial and genuinely critical population:

| In CSW's reach (IT-side) | Out of CSW's reach (OT device layer) |
|---|---|
| **PTC Back Office Server** and its supporting hosts | Locomotive onboard PTC components |
| Dispatch / computer-aided dispatch (CAD) servers | Wayside interface units, signal controllers |
| Signaling-support and interlocking-support servers | Grade-crossing warning devices |
| Historians, reporting and analytics databases | Track circuits, switch machines |
| Engineering and maintenance workstations | Traction power field devices |
| Train management, movement planning, crew scheduling | Programmable logic controllers |
| Vendor and MSSP remote-access hosts | — |
| Identity, PKI, logging, and patch infrastructure | — |

The **PTC Back Office Server is the point worth emphasizing.** Section
III.A.2 makes PTC a mandatory Critical Cyber System, and the back
office is a server workload — squarely in CSW's reach. A railroad can
therefore produce genuine, workload-level Critical Cyber System
evidence for its single most inspection-sensitive system.

Your OT-aware monitoring stack (Cisco Cyber Vision, Claroty, Nozomi,
Dragos, or equivalent) and your IT/OT boundary firewalls remain the
controlling artifacts at and below the boundary. CSW complements them;
it does not replace them, and claiming otherwise in front of a TSA
inspector will cost you credibility you need elsewhere.

### 1.3 Version and renewal discipline

The SD series is renewed annually and the revision letter advances
(01, 01A through 01E to date). TSA has stated it intends to codify
these requirements permanently through rulemaking. Two practical
consequences:

- **Confirm the active revision letter** before customer delivery. The
  May 1, 2026 renewal memo states there are no substantive revisions
  in 01E — changes are limited to dates, series letter, and formatting
  — but that will not hold indefinitely.
- **TSA determined this SD is not Sensitive Security Information**, so
  the requirement text may be discussed openly. **Everything you
  submit to TSA under it *is* SSI** and must be handled under 49 CFR
  part 1520. Treat your CSW evidence exports accordingly once they are
  incorporated into a plan or report.

Note also that if an Owner/Operator has delegated measures to a
**Managed Security Service Provider** or an **Authorized
Representative**, the Owner/Operator **retains sole responsibility**
for compliance. Both the Owner/Operator and the Authorized
Representative are liable for the representative's non-compliance.

---

## 2. SD Provision Mapping

Each row carries a **Coverage** verdict from the legend at the top of
this document. Provision numbering follows SD 1580/82-2022-01E.

### III.A — Critical Cyber System Identification

| Provision | Requirement | Coverage | CSW Implementation |
|---|---|---|---|
| III.A | Identify Critical Cyber Systems | 🟠 Supporting | CSW hosts the inventory and labels that make the register operational and continuously reconciled; the **designation itself is an operational risk decision** your accountable officer signs |
| III.A.2 | PTC systems must be included as a Critical Cyber System | 🟠 Supporting | CSW instruments the PTC **back office** and its dependencies as first-class workloads; the mandate and the locomotive-side components are outside CSW |

**CSW Implementation:**
```
CSW UI → Inventory → Bulk Label
  → Per IT workload supporting a Critical Cyber System:
      ccs_id        reference to your CIP register entry
      ccs_function  ptc-bos | dispatch-cad | signaling-support |
                    historian | engineering-wks | train-mgmt |
                    identity | patch-repo | vendor-access
      ot_facing     true | false
      ptc           true | false
      site          subdivision / yard / facility
  → Reconcile CSW scope membership against the CCS register
  → Export the delta for the accountable officer before sign-off
```

### III.B — Network Segmentation

This is the section where CSW produces primary evidence, and it is the
most prescriptive part of the SD.

| Provision | Requirement | Coverage | CSW Implementation |
|---|---|---|---|
| III.B.1.a | List and describe IT and OT system **interdependencies** | 🟢 Direct | ADM derives the dependency graph from observed traffic, which is the definition of an interdependency the SD uses — "relationships of reliance that must be maintained for those systems to operate" |
| III.B.1.b | List and describe **all external connections** to IT and OT systems | 🟢 Direct | Flow search against the external scope enumerates every observed external connection, including the ones absent from the documented architecture |
| III.B.1.c | Describe **zone boundaries** and how systems are organized into logical zones by criticality, consequence, and operational necessity | 🟢 Direct | The CSW scope tree **is** the logical zone model, and labels make criticality and consequence queryable rather than narrative (§3) |
| III.B.1.d | Policies ensuring IT and OT services transit the other **only when necessary for validated business or operational purposes** | 🟢 Direct | Allowlist policy where each rule carries a business justification; everything unjustified is denied and logged (§4) |
| III.B.2.a | Security controls to **prevent unauthorized communications between zones** | 🟢 Direct | Enforced inter-zone deny with the Denied Connections log as proof the control operates, not merely exists |
| III.B.2.b | Prohibit OT services traversing IT and vice versa **unless the content is encrypted** or otherwise secured | 🟠 Supporting | CSW **detects** cleartext traversal across the boundary with flow-level evidence (§3.2 `Plaintext-Crossing-Zones`); it does not encrypt anything — see §7.2 |

### III.C — Access Control Measures

CSW's contribution here is narrower than operators often assume. The
SD's access-control section is predominantly about **identity**, which
is not CSW's layer.

| Provision | Requirement | Coverage | CSW Implementation |
|---|---|---|---|
| III.C.1 | Memorized-secret authenticator reset policy and documented mitigations for components outside it | ⚪ Evidence Required | Identity provider and OS policy; see §7.1 |
| III.C.2 | **MFA**, or compensating controls where MFA is not applied to OT components | ⚪ Evidence Required | Cisco ISE, Duo, or the operator's equivalent; CSW neither performs nor evidences authentication |
| III.C.3 | Manage access rights by **least privilege and separation of duties** | 🟠 Supporting | Delivers *network* least privilege between zones and functions; user and administrative least privilege is evidenced in the IdP and OS |
| III.C.4 | Limit availability and use of **shared accounts** | ⚪ Evidence Required | Account management and privileged-access tooling |
| III.C.5 | Regularly review **domain trust relationships** | ⚪ Evidence Required | Directory services review |
| III.C.6 | PTC locomotive components may rely on **physical security** in lieu of III.C.1–5 | ⚪ Evidence Required | Physical security programme; cite the locomotive sealing and housing-locking measures in your plan |

Worth flagging to the customer: III.C.6 is a genuine relief valve.
Operators subject to 49 CFR 232.105(h)(1–4), 236.3, or 236.553 may
rely on the physical measures already used for those rules for PTC
components **installed on locomotives**, rather than implementing
III.C.1–5 there. It applies only to those components, and the plan
must say which physical measures are relied upon.

### III.D — Continuous Monitoring and Detection

| Provision | Requirement | Coverage | CSW Implementation |
|---|---|---|---|
| III.D.1.a | Defend against malicious email | ⚪ Evidence Required | Email security gateway |
| III.D.1.b | Block ingress/egress with known or suspected malicious IP addresses | 🟠 Supporting | Policy can deny the addresses; the reputation feed and its currency come from threat intelligence or the perimeter |
| III.D.1.c | Control impact of malicious web domains and applications | ⚪ Evidence Required | DNS and web security — Cisco Umbrella or equivalent |
| III.D.1.d | Block and prevent **unauthorized code**, including macro scripts, from executing | 🟠 Supporting | Process and hash visibility identifies execution; *blocking* it is EDR and application control |
| III.D.1.e | Monitor and/or block connections to malicious command-and-control, Tor exit nodes, anonymizers | 🟠 Supporting | Flow visibility plus policy denial; the node list is external |
| III.D.2.a | Audit unauthorized access to internet domains and addresses | 🟠 Supporting | Egress flow records per workload; domain-level attribution needs DNS logging |
| III.D.2.b | **Document and audit any communications between the OT system and an external system that deviates from the identified baseline** | 🟢 Direct | This is precisely the ADM baseline plus deviation detection. CSW establishes the baseline, detects the deviation, and exports both — the SD's own wording describes the artifact |
| III.D.2.c | Identify and respond to execution of unauthorized code | 🟠 Supporting | Process telemetry and forensic rules identify it; response is EDR and IR process |
| III.D.2.d | Implement SOAR-style capabilities to drive standardized incident response | 🟠 Supporting | Alert export feeds the SOAR platform; the playbooks are the operator's |
| III.D.3.a | **Continuous collection and analysis** of data for intrusions and anomalous behaviour on Critical Cyber Systems and systems directly connected to them | 🟢 Direct | Continuous flow, process, and policy-violation telemetry across the instrumented estate |
| III.D.3.b | Maintain data for sufficient periods for effective investigation | 🟠 Supporting | CSW retention is configurable; long-term immutable retention belongs to the SIEM or archive |
| III.D.4 | Mitigation measures or manual controls to **isolate industrial control systems** when an IT incident creates risk to OT safety and reliability | 🟢 Direct | A pre-staged quarantine workspace lets you sever the IT-side paths into the OT-facing tier in one action, with the denied-connection log as proof it took effect |

III.D.4 deserves a deliberate design decision rather than an ad-hoc
response. Build the isolation policy **before** you need it, test it
during a maintenance window, and record the test — that record is the
evidence that the mitigation measure exists and works.

### III.E — Unpatched System Risk

| Provision | Requirement | Coverage | CSW Implementation |
|---|---|---|---|
| III.E.1 | Patch management strategy keeping critical patches current | 🟠 Supporting | Continuous per-workload CVE and package inventory reports currency; the patching itself is the config-management tool |
| III.E.2.a | Risk methodology for categorizing patch criticality with an implementation timeline | 🟠 Supporting | Supplies the per-workload risk inputs — severity, exploitability, and whether the service is reachable; the methodology is the operator's |
| III.E.2.b | **Prioritize all patches on the CISA Known Exploited Vulnerabilities Catalog** | 🟢 Direct | CVE inventory filtered to KEV and intersected with the Critical Cyber System labels, so prioritization is a query rather than a spreadsheet merge |
| III.E.3 | Where patching would **severely degrade operational capability**, describe additional mitigations and a timeline | 🟢 Direct | The compensating-control case: restrict the source set for the vulnerable port, log every flow touching it, and export the policy as the documented mitigation |

III.E.3 is where CSW is most valuable in a rail context, because
railroads genuinely cannot patch on an IT cadence. A vulnerable
service that policy has made unreachable from everywhere except one
justified source is a materially different risk from the same service
left open, and CSW produces the evidence for that distinction.

### III.F — Cybersecurity Assessment Plan

| Provision | Requirement | Coverage | CSW Implementation |
|---|---|---|---|
| III.F.1 / III.F.2.a | Proactively assess Critical Cyber Systems and the effectiveness of the approved plan | 🟠 Supporting | Per-provision evidence pack with prior-period deltas; the assessment and its conclusions are the operator's and the assessor's |
| III.F.2.b | Architecture design review containing **verification and validation of network traffic, a system log review**, and analysis of design, configuration, and interconnectivity | 🟢 Direct | CSW produces all three input artifacts — traffic verification, flow and process logs, and the interconnectivity graph. The review *conclusion* remains a human assessment |
| III.F.2.d | Schedule assuring **one-third of measures assessed annually, 100 percent over three years** | 🟠 Supporting | Because each CSW artifact is re-exportable on demand, the sampling schedule becomes a reporting cadence rather than a fresh evidence-collection exercise each cycle |

### IV.C.2 — Records TSA May Inspect

The SD enumerates what inspectors may request. Four of these are
CSW outputs, and two are named in CSW's own vocabulary.

| Provision | Record | Coverage | CSW Implementation |
|---|---|---|---|
| IV.C.2.a | Hardware/software asset inventory | 🟢 Direct | Workload inventory with installed packages, reconciled to the CCS register |
| IV.C.2.b | Firewall rules | 🟠 Supporting | CSW policy is the workload-tier equivalent and exports cleanly, but it is not your perimeter or IT/OT firewall ruleset — supply both |
| IV.C.2.c | Network diagrams, architecture diagrams, VLANs, publicly routable IPs | 🟢 Direct | The ADM dependency map is a generated, dated network diagram; pair it with your authoritative architecture drawings |
| IV.C.2.e.i | Log files | 🟢 Direct | Flow and process logs with timestamps and process attribution |
| IV.C.2.e.ii | Packet capture, not exceeding 24 hours, as directed by TSA | ⚪ Evidence Required | CSW records flow metadata, **not packet payloads** — PCAP comes from a capture appliance or OT sensor |
| IV.C.2.e.iii | **"East-West Traffic" of OT systems/sites/environments** | 🟢 Direct | Lateral flow records within a zone — the SD defines east-west traffic as "lateral movement of network traffic within a trust zone or local area network," which is CSW's native output |
| IV.C.2.e.iv | **"North-South Traffic" between IT and OT systems, and the perimeter boundaries between them** | 🟢 Direct | Cross-zone flow records — the SD defines north-south as traffic "through a perimeter boundary into another trust level" |

**Coverage summary:** 🟢 Direct for **16** provisions, 🟠 Supporting
for **16**, and ⚪ Evidence Required for **8**. The boundary is
enumerated in §7.

---

## 3. Scope Architecture and Labeling

Section III.B.1.c requires you to describe how IT and OT systems are
"defined and organized into logical zones based on criticality,
consequence, and operational necessity." That sentence is a
specification for a scope tree. Build it so that the tree *is* the
zone model in your Cybersecurity Implementation Plan — if the two
diverge, the CSW export stops being evidence and becomes a
contradiction an inspector will pursue.

### 3.1 Suggested Scope Architecture

```
Root Scope
└── Rail-Critical-Cyber-Systems
    ├── OT-Facing-IT                      (reaches into the signaling / PTC domain)
    │   ├── PTC-Back-Office               (mandatory CCS — III.A.2)
    │   ├── Dispatch-and-CAD
    │   ├── Signaling-Support
    │   ├── Historians
    │   └── Engineering-Workstations
    ├── CCS-Supporting-IT                 (CCS, but not OT-facing)
    │   ├── Train-Mgmt-and-Planning       (business critical functions)
    │   ├── Identity-and-PKI
    │   ├── Logging-and-Monitoring
    │   └── Patch-Repositories
    ├── Privileged-Access-Paths           (III.C local and remote access)
    ├── Corporate-IT                      (default-deny source)
    └── External
        ├── Internet-Edge
        └── Vendor-and-MSSP-Access        (Authorized Representatives / MSSPs)
```

Three branches are deliberate. **`PTC-Back-Office`** is separated
because III.A.2 makes PTC a mandatory Critical Cyber System and
inspectors will ask about it specifically. **`Train-Mgmt-and-Planning`**
exists because the Critical Cyber System definition explicitly
includes business services whose loss causes operational disruption,
and that branch is where under-scoping usually hides.
**`Vendor-and-MSSP-Access`** is named inside the tree even though it
sits outside the operator's estate — Section III.B.1.b requires a list
of *all* external connections, and you cannot enumerate a connection
to a system the tree refuses to name.

### 3.2 Inventory Filters

```
Filter: PTC-Back-Office
  - Tag: ptc = true
  - Tag: ccs_function = ptc-bos
  - Hostname / application pattern matches the PTC back-office inventory

Filter: OT-Facing-IT
  - Tag: ot_facing = true
  - Observed flows to documented OT network ranges

Filter: Vendor-and-MSSP-Access
  - Tag: managed_by = authorized-rep | mssp
  - Observed inbound on tcp/22, tcp/3389, tcp/443 from outside operator ranges

Filter: External-Connections
  - Source or destination outside the documented operator ranges
  - Supports the Section III.B.1.b external-connection list

Filter: Plaintext-Crossing-Zones
  - Source zone != destination zone
  - Protocol / port: tcp/80, tcp/21, tcp/23, tcp/389, tcp/1433, udp/161

Filter: KEV-Exposed-CCS
  - Tag: ccs_id is set
  - Vulnerability present in the CISA Known Exploited Vulnerabilities Catalog
```

Two of these filters exist purely to answer a specific SD provision.
`Plaintext-Crossing-Zones` is the Section III.B.2.b evidence item —
the SD permits IT/OT traversal only where content is encrypted or
otherwise protected, so finding the cleartext crossings yourself is
materially better than having an inspector find them.
`KEV-Exposed-CCS` is the Section III.E.2.b prioritization list.

### 3.3 Labeling Strategy

| Label key | Example values | Why it matters for the SD |
|---|---|---|
| `ccs_id` | <CIP register entry> | The join key between CSW and your TSA-approved plan — the single most important label here, because TSA inspects against the plan |
| `ccs_function` | ptc-bos, dispatch-cad, signaling-support, historian, engineering-wks, train-mgmt, identity, patch-repo, vendor-access | Drives III.B zone assignment and III.E patch prioritization |
| `zone` | ot-facing-it, ccs-supporting-it, corporate, external | Makes III.B.1.c logical zones a queryable attribute instead of a diagram |
| `ot_facing` | true, false | The III.B.2.b IT/OT traversal rule depends on knowing which workloads cross the boundary |
| `ptc` | true, false | III.A.2 makes PTC a mandatory Critical Cyber System — flag it explicitly |
| `operational_disruption_impact` | high, moderate, low | The Critical Cyber System definition turns on operational disruption; record the judgment where the evidence lives |
| `interdependency_group` | <named group> | Supports the III.B.1.a interdependency list |
| `managed_by` | internal, authorized-rep, mssp | II.A.2–3 — responsibility stays with the Owner/Operator, so know which workloads a third party touches |
| `site` | <subdivision / yard / facility> | Rail estates are geographically distributed; inspections are often site-scoped |
| `compliance` | tsa-rail | Filters every CSW export to the SD boundary |

`ccs_id` and `managed_by` are the two worth enforcing at onboarding.
The first makes every export reconcilable to the approved plan; the
second answers the MSSP and Authorized Representative question before
an inspector raises it.

---

## 4. Policy Design — Section III.B Zone Enforcement

Section III.B.2.a requires controls that *prevent* unauthorized
communication between zones, and III.B.1.d requires that cross-zone
transit occur "only when necessary for validated business or
operational purposes." Together those make an allowlist with
documented justifications the natural implementation — and they make
the policy export a compliance artifact rather than an operational
one. Write each rule to be read by an inspector.

### 4.1 SD-Aligned Policy Framework

**Absolute policies:**

```
DENY  Corporate-IT                   → OT-Facing-IT                  (III.B.2.a — no unauthorized inter-zone communication)
DENY  OT-Facing-IT                   → Internet-Edge                 (III.B.1.d — no unvalidated egress from the OT-facing tier)
DENY  Vendor-and-MSSP-Access         → PTC-Back-Office               (third-party paths stop short of the PTC back office)
DENY  External                       → Rail-Critical-Cyber-Systems   (III.B.1.b — external connections are enumerated, never implicit)
DENY  OT-Facing-IT                   → OT-Facing-IT                  (no implicit east-west inside the OT-facing tier)
```

The last rule is the one that most often gets dropped and most often
matters. Section IV.C.2.e.iii makes **east-west traffic within a trust
zone** an inspectable record, which means "it is all inside one zone"
is not an answer. Denying implicit intra-zone traffic and allowlisting
the justified paths is what produces a defensible east-west record.

**Allowlist policies (least privilege):**

```
ALLOW Dispatch-and-CAD               → PTC-Back-Office               tcp/<ptc-port-tls>
ALLOW PTC-Back-Office                → Historians                    tcp/<db-port-tls>
ALLOW Rail-Critical-Cyber-Systems    → Identity-and-PKI              tcp/636, tcp/88
ALLOW Privileged-Access-Paths        → OT-Facing-IT                  tcp/22, tcp/3389
ALLOW Rail-Critical-Cyber-Systems    → Logging-and-Monitoring        tcp/443, udp/514
ALLOW Patch-Repositories             → Rail-Critical-Cyber-Systems   tcp/443
```

Every port is specified in its TLS-bearing form deliberately, because
Section III.B.2.b conditions cross-boundary traversal on the content
being encrypted. If the only rule that makes a system work is the
cleartext port, you have documented a III.B.2.b gap rather than closed
one — which is useful, but record it as such.

**Catch-all:**

```
LOG   Any                            → OT-Facing-IT                  (unmatched inbound — III.D.3.a)
LOG   OT-Facing-IT                   → Any                           (unmatched outbound — III.D.2.b baseline deviation)
LOG   Any                            → Any                           (plaintext crossing zones: tcp/80, tcp/21, tcp/23, tcp/389, udp/161 — III.B.2.b)
```

### 4.2 Policy Workspace Lifecycle

| Phase | Mode | Duration | Purpose |
|---|---|---|---|
| 1 | Simulation | 30 days | Validate against a full operating cycle including a maintenance window — longer than this series' usual 2 weeks, because rail traffic patterns are seasonal and schedule-driven |
| 2 | Enforcement (absolute denies only) | 2 weeks | Enforce the inter-zone deny rules first |
| 3 | Full Enforcement | Ongoing | Zone allowlist enforced; monthly exception review |

Workspace snapshots are the Section III.B implementation evidence; the
simulation report is what shows the policy was assessed before it was
enforced; and the Denied Connections log is the proof that III.B.2.a
**operates** rather than merely exists. Exceptions belong in the
workspace exception register, which is also the input to your plan
amendment process under Section VI.

> **Change-control note.** Section VI requires an amendment request
> when you make permanent changes — defined as 45 or more days — to
> the policies, procedures, or measures TSA approved, filed no later
> than 50 days after the change takes effect. A CSW policy change that
> alters an approved segmentation measure can therefore trigger a plan
> amendment. Wire your CSW change history into that process rather
> than discovering the obligation afterwards.

### 4.3 Pre-Staged Isolation for Section III.D.4

Section III.D.4 requires mitigation measures or manual controls to
isolate industrial control systems when an IT-side incident threatens
OT safety and reliability. Build this as a standing, unapplied
workspace:

```
Workspace: tsa-rail-emergency-isolation   (staged, not enforced)
  DENY  Corporate-IT             → OT-Facing-IT
  DENY  CCS-Supporting-IT        → OT-Facing-IT
  DENY  Vendor-and-MSSP-Access   → Rail-Critical-Cyber-Systems
  ALLOW Privileged-Access-Paths  → OT-Facing-IT             tcp/22, tcp/3389
```

Test it during a planned maintenance window, record the test, and keep
the record. The evidence an inspector wants for III.D.4 is not that
you *could* isolate — it is that you have, and that you know how long
it took.

---

## 5. Rollout Guidance by Railroad Profile

| Profile | CSW configuration |
|---|---|
| **Class I freight** | Full ADM per region; enforce absolute denies on `OT-Facing-IT` and `PTC-Back-Office` first; site-scoped evidence packs because inspections are often regional |
| **Class II / III, TSA-designated** | Prioritize the PTC back office and dispatch; monitor and simulation may be sufficient for the first plan cycle if the approved plan says so |
| **Passenger rail / commuter** | Add traction-power SCADA support systems and fare-collection servers to the CCS analysis; coordinate with the SD 1582-21-01 series obligations |
| **Rail transit agency** | Working to the sister SD 1582-21-01 series; the zone model and policy set here transfer directly, but confirm provision numbering against that series |
| **Operator using an MSSP** | Enforce `managed_by` labeling before anything else — II.A.2 leaves responsibility with the Owner/Operator, so you must be able to show precisely what the MSSP reaches |

---

## 6. Evidence Package

| Evidence Item | CSW Source | SD Provision | Frequency |
|---|---|---|---|
| CCS scope + label export | Organize → Scopes | III.A, IV.C.2.a | Per inspection |
| Interdependency map | Investigate → ADM | III.B.1.a | Quarterly |
| External-connection inventory | Flow Search → `External-Connections` | III.B.1.b | Quarterly |
| Zone model export | Organize → Scopes + label schema | III.B.1.c | Per plan update |
| Policy workspace export | Defend → Policy Workspaces | III.B.1.d, III.B.2.a | Per inspection |
| Denied Connections log | Defend → Enforcement | III.B.2.a | Continuous |
| Plaintext-crossing-zones report | Flow Search → `Plaintext-Crossing-Zones` | III.B.2.b | Quarterly |
| Simulation report | Defend → Policy Workspaces | III.B, Section VI | Per policy change |
| Baseline-deviation report | Investigate → ADM diff | III.D.2.b | Monthly |
| Flow + process telemetry | Investigate → Flow / Process Search | III.D.3.a, IV.C.2.e.i | Continuous |
| **East-west traffic record** | Flow Search, intra-zone filter | **IV.C.2.e.iii** | On request |
| **North-south traffic record** | Flow Search, cross-zone filter | **IV.C.2.e.iv** | On request |
| Isolation test record | Defend → `tsa-rail-emergency-isolation` | III.D.4 | Annually + per test |
| KEV exposure report | Investigate → Vulnerability, KEV filter | III.E.2.b | Weekly |
| Compensating-control register | Workspace notes + policy export | III.E.3 | Per exception |
| Architecture-review input pack | ADM + inventory + flow logs | III.F.2.b | Every 2 years |
| Workload inventory | Manage → Inventory | IV.C.2.a | Monthly |
| CSW administrative audit log | Administration → Audit Log | III.D.3.a | Per inspection |

---

## 7. Evidence Boundary — What You Must Supply Outside CSW

This section exists because a vendor mapping that claims everything is
not believable to an inspector. Marking the boundary honestly is what
makes the 32 mapped provisions in §2 credible.

### 7.1 Provisions where CSW produces nothing

| Provision | Topic | Who evidences it |
|---|---|---|
| III.C.1 | Memorized-secret authenticator reset policy | Identity provider and OS policy, aligned to NIST SP 800-63 |
| III.C.2 | Multi-factor authentication and OT compensating controls | Cisco ISE, Duo, or equivalent |
| III.C.4 | Shared-account management | Account management and privileged-access tooling |
| III.C.5 | Domain trust relationship review | Directory services |
| III.C.6 | PTC locomotive physical security alternative | Physical security programme under 49 CFR 232.105(h), 236.3, 236.553 |
| III.D.1.a | Malicious email defence | Email security gateway |
| III.D.1.c | Malicious web domain and application control | DNS / web security — Cisco Umbrella or equivalent |
| IV.C.2.e.ii | Packet capture up to 24 hours as directed by TSA | Capture appliance or OT sensor — CSW records flow metadata, not payloads |

**Also entirely outside CSW:** the Cybersecurity Implementation Plan
and its TSA approval, the Cybersecurity Assessment Plan and its annual
report, the Cybersecurity Incident Response Plan, incident reporting
to CISA, the Cybersecurity Coordinator designation, personnel and
training programmes, and the OT device layer in its entirety (§1.2).

### 7.2 Encryption — the most commonly misread boundary

Section III.B.2.b permits OT services to traverse IT, and vice versa,
only where "the content is encrypted or, if not technologically
feasible, otherwise secured and protected to ensure integrity and
prevent corruption or compromise while the content is in transit."

**CSW does not encrypt application data.** What CSW contributes is
detection: the `Plaintext-Crossing-Zones` filter and the matching LOG
rule in §4.1 identify, with flow-level evidence, which cross-zone
paths are still running cleartext protocols. That is a genuinely
useful input to the III.B.2.b narrative in your plan — and it is not
the same thing as satisfying the provision.

Where encryption is not technologically feasible — common with legacy
rail protocols — the SD allows the content to be "otherwise secured
and protected." A tightly scoped, enforced, and logged path is a
credible component of that argument, but the argument is yours to
make in the plan, not CSW's to assert.

### 7.3 The OT device layer

Restating §1.2 because it is the boundary most likely to be
over-claimed: CSW does not enforce policy on wayside units, signal
controllers, locomotive onboard PTC hardware, grade-crossing
equipment, or PLCs, and does not inspect rail or OT protocols. Your
OT-aware monitoring platform and IT/OT boundary firewalls remain the
controlling artifacts there. The SD's segmentation requirement runs in
**both** directions — IT protected from OT as well as OT from IT — and
CSW addresses the IT side of that requirement only.

### 7.4 Plan-relative evidence and SSI handling

- **TSA inspects against your approved Cybersecurity Implementation
  Plan, not against the SD.** An evidence pack that maps to SD
  provisions but not to your plan's measures will not land. Map every
  artifact in §6 to a plan measure.
- **Everything submitted to TSA under this SD is Sensitive Security
  Information** under 49 CFR part 1520, even though the SD text itself
  is not. Once a CSW export is incorporated into a plan, assessment,
  or report, handle it as SSI.
- **Delegation does not transfer responsibility.** If an MSSP or
  Authorized Representative operates CSW on the operator's behalf, the
  Owner/Operator retains sole responsibility for compliance, and both
  parties are liable for the representative's non-compliance.

---

## 8. TSA Inspector Response Guide

| If the inspector asks… | Produce |
|---|---|
| "Show your Critical Cyber System inventory." | Scope + label export with `ccs_id`, `ccs_function`, `ptc`, and `site`, reconciled to the register (§6) |
| "Demonstrate your Section III.B segmentation." | Policy workspace export plus the Denied Connections log showing blocked inter-zone attempts |
| "Provide your IT/OT interdependency list." | ADM dependency map with its generation date (§III.B.1.a) |
| "List all external connections." | External-connection inventory from flow search, with the vendor and MSSP paths identified (§III.B.1.b) |
| "Describe your zone boundaries." | Scope tree and label schema, cross-referenced to the zone model in your approved plan |
| **"Give me east-west traffic for this OT environment."** | **Intra-zone flow records for the site — named in IV.C.2.e.iii and native CSW output** |
| **"Give me north-south traffic between IT and OT."** | **Cross-zone flow records at the boundary — IV.C.2.e.iv** |
| "Show communications that deviated from your baseline." | Baseline-deviation report from ADM diff (§III.D.2.b) |
| "How would you isolate OT if IT were compromised?" | The pre-staged isolation workspace plus the dated test record (§4.3, III.D.4) |
| "How are you prioritizing KEV vulnerabilities?" | KEV exposure report intersected with CCS labels (§III.E.2.b) |
| "You cannot patch this system. What mitigates it?" | Compensating-control register plus the enforced policy restricting the vulnerable port (§III.E.3) |
| "Provide input for the architecture design review." | Traffic verification, flow and process logs, and the interconnectivity graph (§III.F.2.b) |
| "Provide a 24-hour packet capture." | **Not a CSW answer** — capture appliance or OT sensor; CSW records flow metadata, not payloads (§7.1) |
| "Show your MFA implementation." | **Not a CSW answer** — identity provider evidence (§7.1) |

---

## Related Frameworks

- [TSA Pipeline Security Directive](https://github.com/chandrapati/CSW-TSA-Pipeline-Reference-Design) — the sister TSA mode; the four performance-based outcomes are harmonized, so the zone model and evidence pack transfer closely.
- [NERC CIP](https://github.com/chandrapati/CSW-NERC-CIP-Reference-Design) — the bulk-electric-system analogue; identical IT-side ESP-enclave patterns apply.
- [IEC 62443](https://github.com/chandrapati/CSW-IEC62443-Reference-Design) — zones and conduits, the engineering vocabulary behind the SD's Section III.B zone language.
- [NIST SP 800-82](https://github.com/chandrapati/CSW-NIST-800-82-Reference-Design) — OT security guidance for the estate surrounding the devices CSW does not reach.
- [NIST SP 800-53 Rev 5](https://github.com/chandrapati/CSW-NIST-800-53-Reference-Design) — AC-4, SC-7, SI-4, RA-5, CM-8 are the control-catalog analogues of Sections III.B through III.E.

---

*Replace [Customer Name], [Owner/Operator], and bracketed fields before customer delivery.*

---

## References & official sources

Authoritative source(s) for the **TSA Rail Security Directive**. Always validate provision references and the active revision letter against the current official text before customer use — this SD series is renewed annually.

- [TSA Security Directives and Emergency Amendments](https://www.tsa.gov/sd-and-ea) — the authoritative index, including the current revision letter
- [SD 1580/82-2022-01E and transmittal memo](https://www.tsa.gov/sites/default/files/signed_security_directive_1580_82-2022-01e_and_transmittal_memo_508c.pdf)
- [SD 1582-21-01 series](https://www.tsa.gov/sites/default/files/security_directive_1582-21-01c_and_memo_508c.pdf) — public transportation and passenger railroad
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — referenced directly by Section III.E.2.b
- [NIST SP 800-63 Digital Identity Guidelines](https://csrc.nist.gov/publications/detail/sp/800-63/3/final) — referenced by Section III.C.1
- Cisco Secure Workload — [product documentation](https://www.cisco.com/c/en/us/support/security/secure-workload/series.html)

---

## Disclaimer

This repository is for informational and planning purposes. It is **not** legal, regulatory, audit, or certification advice, and it is **not** a finding of compliance with any TSA Security Directive. TSA Security Directives are issued and revised by the Transportation Security Administration under its regulatory authority; designated Owner/Operators are required to comply, and **TSA inspects against the Owner/Operator's TSA-approved Cybersecurity Implementation Plan**, not against a vendor document. Validate all provision references and the active revision letter against the current official text. Designation as a covered Owner/Operator is a TSA determination. CSW does not enforce policy on OT devices and is not an OT-protocol inspection or architecture-review tool. Replace any bracketed fields before customer delivery, and obtain subject-matter-expert review for both regulatory accuracy and current Cisco product capability before relying on this in a formal compliance engagement.

---

*Part of the Cisco Secure Workload compliance reference-design series. Umbrella index: [CSW-Compliance-Mapping](https://github.com/chandrapati/CSW-Compliance-Reference-Designs).*
