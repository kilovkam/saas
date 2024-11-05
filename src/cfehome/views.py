import pathlib
from django.shortcuts import render
from django.http import HttpResponse

this_dir=pathlib.Path(__file__).resolve().parent



def home_page_view(request , *args , ** kwargs):
    my_tiltle="My Page"
    my_context={
        "page_title": my_tiltle
    }
    html_templates="home.html"
    return render(request , html_templates , my_context)

def home_page_view3(request , *args , ** kwargs):
    my_tiltle="My Page"
    my_context={
        "page_title": my_tiltle
    }
    html_="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Inline is kilo Works 22 !!!! </h1>
</body>
</html>""".format(**my_context)
    return HttpResponse(html_)



def home_page_view2(request , *args , ** kwargs):
    my_tiltle="My Page"
    html_=""
    html_file_path =this_dir / "home.html"
    html_ = html_file_path.read_text()
    return HttpResponse(html_)