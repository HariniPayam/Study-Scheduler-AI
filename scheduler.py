def generate_schedule(subjects, total_hours, important_subjects):
    schedule = {}
    normal_subjects = [s for s in subjects if s not in important_subjects]

    if important_subjects:
        imp_ratio = 0.6
    else:
        imp_ratio = 0

    imp_hours = total_hours * imp_ratio
    norm_hours = total_hours - imp_hours

    
    for subject in important_subjects:
        schedule[subject] = imp_hours / len(important_subjects)

    for subject in normal_subjects:
        schedule[subject] = norm_hours / len(normal_subjects)

    return schedule
