from celery import shared_task
from celery_progress.backend import ProgressRecorder
import datetime
from nasapy import Nasa
import random
import time

nasa = Nasa(key="Generate your API Key at https://api.nasa.gov/")

@shared_task(bind=True)
def get_nasa_image(self, seconds):
    progress_recorder = ProgressRecorder(self)
    result = 0
    for i in range(seconds):
        time.sleep(4)
        result += i

        start_date = datetime.datetime.strptime('06/16/1995', '%m/%d/%Y')
        end_date = datetime.datetime.now()
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        image_not_suitable = True

        while image_not_suitable:
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            nasa_image_result = nasa.picture_of_the_day(random_date)

            if 'url' in nasa_image_result and nasa_image_result['url'].endswith(('.bmp', '.gif', '.heif', '.jpeg', '.jpg', '.png', '.svg', '.webp')):
                break

        progress_recorder.set_progress(i + 1, seconds, description=nasa_image_result)
    return result
