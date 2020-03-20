from django.shortcuts import render

from .models import Tag, Startup

def tagList(request):
		tags = Tag.objects.all()
		
		context = {
			'tags': tags
		}

		return render(request, 'organizer/tag_list.html', context)


def tagDetails(request, slug):
		tag = Tag.objects.get(slug=slug)

		context = {
			'tag': tag
		}

		return render(request, 'organizer/tag_details.html', context)

def startupList(request):
		startups = Startup.objects.all()

		context = {
			'startups': startups
		}

		return render(request, 'organizer/startup_list.html', context)

def startupDetail(request, slug):
		startup = Startup.objects.get(slug=slug)

		context = {
			'startup': startup
		}

		return render(request, 'organizer/startup_detail.html', context)