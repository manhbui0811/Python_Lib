import time
from scheduler.scheduler_manager import create_scheduler

CONFIG_PATH = "config/config.json"

if __name__ == "__main__":
    scheduler = create_scheduler(CONFIG_PATH)
    scheduler.start()
    print("🚀 Scheduler đã khởi động!")

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("🛑 Scheduler đã dừng.")
