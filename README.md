This application isn't finished. Create PostgreSQL database with information from settings.py and clone this repo to test it. Run python manage.py runserver to start.

/index is a main page, where you can:
- Add new task
- Edit/Delete exiting tasks
- See results (you can filter them by task_id)

Alternatively you can use Django admin panel.

To import tasks from database, start redis-server and run:
- celery -A watch_your_site worker -l info
- celery -A watch_your_site beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

To reload tasks remove everything from Periodic Tasks in Django admin panel and run these commands again.

To improve:
- POST -> DELETE in task deletion
- run and reload tasks from /index
- sort bad results and show them in some list
- REST API
