from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TodoForms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
class Detailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class Tasklistview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task'

class Updateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('taskname','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})

class Deleteview(Detailview):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvlistview')

# Create your views here.
def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        taskname=request.POST.get('taskname','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Task(taskname=taskname,priority=priority,date=date)
        task.save()
    return render(request,'index.html',{'task':task1})

def delete(request,id):
    task = Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task = Task.objects.get(id=id)
    form = TodoForms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})