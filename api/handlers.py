from piston.utils import rc
from piston.handler import BaseHandler
from todos.models import Task

class TaskHandler(BaseHandler):
    model = Task
    fields = ('id', 'text', 'done')

    def read(self, request, task_id = None):
        mpr = Task.objects

        if task_id is not None:
            return mpr.get(pk = task_id)
        else:
            return mpr.all()

    def create(self, request):
        return Task.objects.create(**request.data)

    def update(self, request, task_id):
        Task.objects.filter(pk = task_id).update(**request.data)
        return Task.objects.get(pk = task_id)

    def delete(self, request, task_id):
        Task.objects.filter(pk = task_id).delete()
        return rc.DELETED

    
