from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import PublicNotice, Entry
from .forms import PublicNoticeForm






def index(request):
	"""The home page for Notices"""
	return render(request, 'publicnotices/index.html')

@login_required
def publicnotices(request):
	"""Show all notices"""
	publicnotices = PublicNotice.objects.order_by('date_posted')
	context = {'publicnotices': publicnotices}
	return render(request, 'publicnotices/publicnotices.html', context)


@login_required
def publicnotice(request, publicnotice_id):
	publicnotice = PublicNotice.objects.get(id=publicnotice_id)
	entries = publicnotice.entry_set.order_by('-date_added')
	# publicnotice = PublicNotice.objects.filter(id = publicnotice_id)
	# if publicnotice.exists():
	# 	single_notice = publicnotice[0]
	context = {'publicnotice': publicnotice, 'entries': entries}
	return render(request, 'publicnotices/publicnotice.html', context)

@login_required
def new_publicnotice(request):
	if request.method != 'POST':
		form = PublicNoticeForm
	else:
		form = PublicNoticeForm(data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('publicnotices:publicnotices'))

	context = {'form': form}
	return render(request, 'publicnotices/new_publicnotice.html', context)







