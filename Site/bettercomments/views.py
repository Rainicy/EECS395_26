from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from refine.models import SearchBox
from refine.models import CreateWordCloud 

def home(request):
    t = get_template("index.html")
    html = t.render(Context({}))
    return HttpResponse(html)

def about(request):
    t = get_template("about.html")
    html = t.render(Context({}))
    return HttpResponse(html)

def contact(request):
    t = get_template("contact.html")
    html = t.render(Context({}))
    return HttpResponse(html)

@csrf_exempt
def tryrefine(request):
    if (request.method == 'POST'):
        form = SearchBox(request.POST)
        search_comment_form = SearchBox()
        url = CreateWordCloud.trimURL(request.POST['Search'])
        request.session['posts'] = CreateWordCloud.getPosts(url)
        word_list = CreateWordCloud.listNGrams(url, request.session['posts'])
        request.session['wordcloud'] = word_list
        return render_to_response('test.html', {'word_list' : word_list,
            'search_comment_form': search_comment_form,},)
    else:
        form = SearchBox()
        return render_to_response('tryrefine.html', {'form' : form,})

@csrf_exempt
def test(request):
    if (request.method == 'POST'):
        form = SearchBox(request.POST)
        comment_search = request.POST['Search']
        session = request.session['posts']
        posts = CreateWordCloud.getPostsContaining(comment_search, session)
        word_list = request.session['wordcloud']
        return render_to_response('test.html', {'comment_search':
            comment_search, 'session': session, 'posts': posts, 'word_list'
            : word_list, 'search_comment_form' : form,},)
    else:
        form = SearchBox()
        return render_to_response('test.html', {'search_comment_form': form,},)

def comments(request):
    t = get_template("comments.html")
    html = t.render(Context({}))
    return HttpResponse(html)
