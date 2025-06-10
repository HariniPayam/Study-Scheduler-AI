def clean_subjects(subject_input):
    """
    Takes a comma-separated string and returns a clean list of subjects.
    """
    return [s.strip().title() for s in subject_input.split(',') if s.strip()]


def format_schedule(schedule):
    """
    Converts the schedule dictionary into a nicely formatted string.
    """
    return "\n".join([f"{subject}: {round(hours, 2)} hrs" for subject, hours in schedule.items()])
