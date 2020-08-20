from django.shortcuts import render, HttpResponseRedirect, reverse
from ghostpost.models import BoastRoast
from ghostpost.forms import AddGhostpost

# Create your views here.


def index(request):
    ghostposts = BoastRoast.objects.all().order_by('-time_posted')
    return render(request, 'index.html', {"welcome": "Ghostpost: Roast and Boast", "ghostpost": ghostposts})


def create_post(request):
    if request.method == "POST":
        form = AddGhostpost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BoastRoast.objects.create(
                choices=data.get('choices'),
                user_input=data.get('user_input')
            ) 
            
            return HttpResponseRedirect(reverse("homepage"))
            
    form = AddGhostpost()
    return render(request, "generic_form.html", {"form": form})



def boast_view(request):
    boast = BoastRoast.objects.all().order_by('-time_posted')
    return render(request, 'boast.html', {"boast": boast})


def roast_view(request):
    roast = BoastRoast.objects.all().order_by('-time_posted')
    return render(request, 'roast.html', {"roast": roast})


def upvotes_view(request, upvote_id):
    vote = BoastRoast.objects.filter(id=upvote_id).first()
    vote.upvotes += 1
    vote.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvotes_view(request, downvote_id):
    vote = BoastRoast.objects.filter(id=downvote_id).first()
    vote.downvotes += 1
    vote.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def sortbyvote_view(request):
    sort = sorted(BoastRoast.objects.all(), key=lambda vote: vote.totalvotes, reverse=True)
    return render(request, 'sortbyvote.html', {"sort": sort, "topvotes": "Top Voted Ghostpost"})