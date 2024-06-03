def calculate_enhanced_score(stats):
    clutch_score = stats['clutch_success_rate'] * 0.25
    utility_score = stats['utility_efficiency'] * 0.20
    entry_frag_score = stats['entry_frag_success'] * 0.20
    support_score = stats['support_metrics'] * 0.15
    economy_score = stats['economy_impact'] * 0.20
    return clutch_score + utility_score + entry_frag_score + support_score + economy_score

