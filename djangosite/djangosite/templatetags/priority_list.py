from django import template
import datetime

register = template.Library()

@register.filter(name='priority_list')
def priority_list(list_of_tasks):
    def render(self, context):
        site_name = getarrr(settings, "/tasks/", False)
        if not site_name:
            return "<!-- error message -->"
        if settings.DEBUG:
            return 'debug|| '+ site_name
        return site_name

    def duedateCalc(year, month, day, hour):
        time_remaining = datetime.datetime(year=year, month=month, day=day, hour=hour) - datetime.datetime.now()
        return float(time_remaining.seconds) / 3600.0

    def tk_algorithm(task):
        due = float(duedateCalc(task.due.year, task.due.month, task.due.day, task.due.hour))
        size = float(task.size.ranking)
        return due + size

    list_comp = [(tk_algorithm(task), task) for task in list_of_tasks]
    sortlist =  sorted(list_comp,key=lambda x: x[0])
    return [item[1] for item in sortlist]
