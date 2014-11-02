import os
import datetime

def populate():
#    Priority(name="test",
#            ranking = 10)
    prio= Priority(name="test",
#            ranking = 10)
#
#    Status(quatativat = "some text")
    stat = Status(quatativat = "some text")
#
#    Size(name = "test",
#            ranking = 3)
    siz = Size(name = "test",
            ranking = 3)
#
#    Tag(name = "test",
#            color = "blue")
    tag = Tag(name = "test",
            color = "blue")
#
    Task(name = "tasking",
            assigned = datetime.datetime.now(),
            due = datetime.datetime.now() + datetime.timedelta(days=1),
            tags = tag,
            priority = prio,
            status = stat,
            size = siz,
            all_day = False,
            repeat = False,
            location = "school",
            desc = "a test")

#    Subgoal(name = "what, a test?",
#            complete = False,
#            task = "tasking")

def Task():
    p = Taks.objects.get_or_create(name=name, assigned=assigned, due=due, tags=tag, priority=priority, status=status, size=size, all_day=all_day, repeat=repeat, location=location, desc=desc)[0]
    return p

if __name__ == '__main__':
    print ("stargin population script")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangosite.settings') 
    from tasks.models import Task
    populate()
