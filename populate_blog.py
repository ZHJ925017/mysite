import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

import django
django.setup()
from blog.models import Category,Page

def populate():
    #First,we will create lists of dictionaries containing the pages
    #We want to add into each category.
    #Then we will create a dictionary of dictionaries for our categories.
    #This might seem a little bit confusing,but it allows us to iterate
    # Through each data structure, and add the data to our models.

    python_pages=[
        {'title':'Offical Python Tutorial','url':'http://docs.python.org/2/tutorial/'},
        {'title':'How to Think like a Computer Scientist','url':'http://www.greenteapress.com/thinkpython/'},
        {'title': 'Learn Python in 10 Minutes','url':'http://www.korokithakis.net/tutorials/python/'}
    ]

    django_pages=[
        {'title':'Offical Python Tutorial','url':'http://docs.djangoproject.com/en/1.9/intro/tutorial101/'},
        {'title':'Django Rocks','url':'http://www.djangorocks.com/'},
        {'title': 'How to Tango with Django','url':'http://www.tangowithdjango.com/'}
    ]

    other_pages = [
        {'title': 'Bottle', 'url': 'http://bottlepy.org/docs/dev/'},
        {'title': 'Flask', 'url': 'http://flask.pocoo.org/'}
    ]

    cats={
        'Python':{'pages':python_pages},
        'Django':{'pages':django_pages},
        'Other_Frameworks':{'pages':other_pages}
    }

    # If you want to add more catergories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    # if you are using Python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # for more information about how to iterate over a dictionary properly.

    for cat,cat_data in cats.iteritems():
        c=add_cat(cat)
        for p in cat_data['pages']:
            add_page(c,p['title'],p['url'])

    #Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print('- {0} - {1}'.format(str(c),str(p)))

def add_page(cat,title,url,views=0):
    p=Page.objects.get_or_create(category=cat,title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name):
    c=Category.objects.get_or_create(name=name,views=0,likes=0)[0]
    if name=='Python':
        c.views=128
        c.likes=64
    elif name=='Django':
        c.views=64
        c.likes=32
    else:
        c.views=32
        c.likes=16
    c.save()
    return c

#Start execution here!
if __name__=='__main__':
    print('Starting blog population script........')
    populate()
