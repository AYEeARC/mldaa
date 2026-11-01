# Job Sequencing with Deadlines

def job_sequencing(jobs):
    # Sort jobs according to decreasing profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    # Time slots
    slots = [None] * (max_deadline + 1)

    total_profit = 0
    selected_jobs = []

    for job_id, deadline, profit in jobs:

        # Try to place job in latest available slot
        for slot in range(min(deadline, max_deadline), 0, -1):

            if slots[slot] is None:
                slots[slot] = job_id
                total_profit += profit
                selected_jobs.append(job_id)
                break

    print("Selected Jobs:", selected_jobs)
    print("Schedule:", slots[1:])
    print("Maximum Profit:", total_profit)


# Job = (Job ID, Deadline, Profit)

jobs = [
    ("J1", 2, 100),
    ("J2", 1, 19),
    ("J3", 2, 27),
    ("J4", 1, 25),
    ("J5", 3, 15)
]

job_sequencing(jobs)