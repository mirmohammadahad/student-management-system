from django.apps import AppConfig


class StudentsConfig(AppConfig):
    name = 'students'
if __name__ == 'students.apps':
    app_run(host="0.0.0.0", debug=True)