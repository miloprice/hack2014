@register.filter(name='priority_list')
def priority_list(list_of_tasks):
    def duedateCalc(year, month, day, hour):
        time_remaining = datetime.datetime(year=year, month=month, day=day, hour=hour) - datetime.datetime.now()
        return time_remaining.hours

    def tk_algorithm(task):
        due = float(duedateCalc(task.due))
        size = float(d1.size.ranking)
        return due + size

    sorted_list = [(tk_algorithm(task), task) for task in list_of_tasks)]
