from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
	request.session['contador']=0
	return redirect('/random_word')

def random_word(request):
	context={
		'counter':request.session['contador'],
		'random': get_random_string(length=14),
	}
	request.session['contador']+=1
	return render(request,'index.html',context)

def reset(request):
	request.session['contador']=0
	return redirect('/random_word')





# Create your views here.
