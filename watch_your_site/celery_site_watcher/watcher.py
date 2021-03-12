# its just a blueprint i will use later

# import urllib.request
#
# from celery import Celery
#
# app = Celery()
#
#
# @app.task(bind=True)
# def watch(self, url):
#     self.update_state(state='PENDING')
#     response_code = urllib.request.urlopen(url).getcode()
#     self.update_state(state='COMPLETE')
#     return response_code
#
#
# @app.task(bind=True)
# def store_result(self, url, response_code):
#     self.update_state(state='PENDING')
#
#
#
# # https://stackoverflow.com/questions/38267525/how-to-make-celery-worker-return-results-from-task #
