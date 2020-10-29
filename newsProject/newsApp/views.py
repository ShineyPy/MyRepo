from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsapp/index.html')

def moviesinfo(request):
    head_msg ='Movies Information'
    sub_msg1 ='Sonali slowly getting cured'
    sub_msg2 ='Bahubali-3 is just planning'
    sub_msg3 ='Salman Khan ready to marriage'
    #'photo':'images/Roses.jpg'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3}
    return render(request,'newsapp/news.html',context=my_dict)

def sportsinfo(request):
    head_msg ='Sports Information'
    sub_msg1 ='Anushka Sharma Firing Like anything'
    sub_msg2 ='Kohli updating in game anything can happend'
    sub_msg3 ='Worst Performance by India-Sehwag'
    #'photo':'images/Roses.jpg'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3}
    return render(request,'newsapp/news.html',context=my_dict)

def politicsinfo(request):
    head_msg ='politics Information'
    sub_msg1 ='kodali nani Firing Like anything'
    sub_msg2 ='roja updating jabardasth'
    sub_msg3 ='vamsi has changing his attitude'
    #'photo':'images/Roses.jpg'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3}
    return render(request,'newsapp/news.html',context=my_dict)
