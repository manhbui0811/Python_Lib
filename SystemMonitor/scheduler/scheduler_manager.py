from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from .job_loader import load_jobs_from_config, get_function_from_path

def create_scheduler(config_path: str) -> BackgroundScheduler:
    scheduler = BackgroundScheduler()

    jobs = load_jobs_from_config(config_path)
    for job in jobs:
        func = get_function_from_path(job["func"])
        cron_config = job["cron"]
        trigger = CronTrigger(**cron_config)
        scheduler.add_job(func, trigger, id=job["id"])

    return scheduler
