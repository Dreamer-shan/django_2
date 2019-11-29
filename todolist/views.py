from django.shortcuts import render,redirect

lst = [
    {'待办事项':'遛狗','已完成':False},
    {'待办事项':'逛街','已完成':True},
    {'待办事项':'玩游戏','已完成':True},
    {'待办事项':'出去玩','已完成':False},
]

# Create your views here.
def home(request):
    global lst
    if request.method == 'POST':
        # 如果不输入内容直接点击添加（待办事项为空的字符串）
        if request.POST['待办事项'] == '':
            #返回值  request html dictionary
            content = {'清单': lst, '警告': '内容为空，请输入内容'}
            return render(request,'todolist/home.html',content)
        else:
            lst.append({'待办事项':request.POST['待办事项'],'已完成':False})
            # content = {'用户的POST请求':str(request.POST) }
            # content = {'待办事项': request.POST['待办事项']}
            #传入一个字典，字典的值是lst 然后再传给网页
            content = {'清单': lst,'信息':'添加成功！'}
            return render(request,'todolist/home.html',content)
    elif request.method == 'GET':
        content = {'清单': lst,'警告': '内容为空，请输入内容'}
        return render(request,'todolist/home.html',content)


def about(request):
    return render(request,'todolist/about.html')


def edit(request,forloop_counter):
    if request.method == 'POST':
        if request.POST['已修改事项'] == '':
            return render(request, 'todolist/edit.html', {'警告': '内容为空，请输入内容'})
        else:
            lst[int(forloop_counter) - 1]['待办事项'] = request.POST['已修改事项']
            return redirect("todolist:主页")
    elif request.method == 'GET':
        content = {'待修改事项':lst[int(forloop_counter)-1]['待办事项']}
        return render(request,'todolist/edit.html',content)

def delete(request,forloop_counter):
    lst.pop(int(forloop_counter)-1)   #forloop_counter是str类型所以要转成整型
    return redirect("todolist:主页")  #网址的名字

def cross(request, forloop_counter):
    global lst
    if request.POST['完成状态'] == '已完成':
        lst[int(forloop_counter) - 1]['已完成'] = True
        return redirect('todolist:主页')
    elif request.POST['完成状态'] == '未完成':
        lst[int(forloop_counter) - 1]['已完成'] = False
        return redirect('todolist:主页')

