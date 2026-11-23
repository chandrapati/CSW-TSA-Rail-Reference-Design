"""Framing text for this framework's diagrams.

Phase content comes from the reference design; only the framing below is
authored, and each line is drawn from that document's stated scope.
"""

FRAMING = {'kicker': 'SD 1580/82-2022-01E',
 'title_tail': '&mdash; TSA Rail',
 'sub': 'From agent coverage to continuous proof between inspections &mdash; exports '
        'map to SD provisions in the Evidence Package section.',
 'caution_label': 'IT side of the boundary &rsaquo;',
 'caution': 'CSW addresses the <b>IT side</b> of the IT/OT boundary. The <b>PTC Back '
            'Office Server</b> is the point worth emphasizing: Section III.A.2 makes '
            'PTC a mandatory Critical Cyber System, and the back office is a server '
            'workload &mdash; squarely in reach.',
 'takeaway': 'The directive names <b>East-West and North-South Traffic</b> as '
             'inspectable records, and CSW produces both as machine-generated '
             'evidence rather than documentation.',
 'rail': ['East-West and North-South traffic records, machine-generated',
          'Simulation proves the policy before anything is enforced',
          'OT device layer stays with your OT-aware controls']}

BOUNDARY = {'kicker': 'Section III.B',
 'title': 'What CSW Reaches',
 'title_tail': '&mdash; TSA Rail IT/OT Boundary',
 'sub': 'CSW addresses the IT side of the IT/OT boundary. The population it reaches '
        'is substantial and genuinely critical.',
 'exclusions': [{'head': 'The OT device layer is out of reach',
                 'body': 'CSW does not enforce on locomotive onboard PTC components, '
                         'wayside interface units, signal controllers, '
                         'grade-crossing devices, track circuits, switch machines, '
                         'traction power field devices, or the PLCs behind them.'},
                {'head': 'PTC Back Office is in reach',
                 'body': 'Section III.A.2 makes PTC a mandatory Critical Cyber '
                         'System, and the back office is a server workload. A '
                         'railroad can therefore produce genuine workload-level '
                         'Critical Cyber System evidence.'},
                {'head': 'Pair with OT-aware controls',
                 'body': 'Your IT/OT boundary firewalls and OT-aware sensors remain '
                         'the controlling artifacts at the device layer. CSW '
                         'complements them rather than replacing them.'}],
 'in_head': "In CSW's reach",
 'in_tag': 'IT side',
 'out_head': "Out of CSW's reach",
 'out_tag': 'OT device layer',
 'takeaway_tag': 'Key Takeaway',
 'takeaway': 'The directive names <b>East-West and North-South Traffic</b> as '
             'inspectable records, and both come from the IT-side population on the '
             'left. <b>Say the device-layer boundary early</b> rather than letting '
             'an inspector find it.',
 'rail': ['PTC Back Office Server is a server workload, squarely in reach',
          'East-West and North-South traffic records come from this tier',
          'Device-layer enforcement stays with your OT controls']}
