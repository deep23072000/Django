from django.http import HttpResponse
def home(req):
    return HttpResponse('''
    <style type="text/css">
    .div1{
        border:5px solid red;
        border-radius:20px;
        padding:20px;
    }
    .div2{
        border:5px solid grey;
        border-radius:20px;
        margin:20px;
        height:700px;
        background-color:yellow;
    }

    .div3{
        border:5px solid grey;
        border-radius:20px;
        margin:20px;
        width:410px;
        height:620px;
        background-color:white;
        display:inline-block;
    }
    .nav{
        font-size:40px;
        margin:30px;
        
    }
    </style>
    <div>

    <div style="height:100px; display:inline-block">
    <img src="https://sulcdn.azureedge.net/biz-live/img/photos-4202970-16076009897437589.jpeg" style="display:flex;height:100px;">
    
    </div>

    <div class="div1">
    <center>
    <a href="home" class="nav">Home</a>
    <a href="/about" class="nav">About</a>
    <a href="/gallery" class="nav">Gallery</a>
    <a href="/contact" class="nav">Contact</a>
    <a href="/help" class="nav">Help</a>
    </center>
    </div>

    <div>
    <div class="div2">
    <div class="div3">
    </div>
    <div class="div3">
    </div>
    <div class="div3">
    </div>
    </div>
    </div>



    </div>
    ''')
def about(req):
    return HttpResponse('''
    <a href="/home">Home</a>
    <a href="about">About</a>
    <a href="/gallery">Gallery</a>
    <a href="/contact">Contact</a>
    <a href="/help">Help</a>''')
def gallery(req):
    return HttpResponse('''
    <a href="/home">Home</a>
    <a href="/about">About</a>
    <a href="gallery">Gallery</a>
    <a href="/contact">Contact</a>
    <a href="/help">Help</a>''')
def contact(req):
    return HttpResponse('''
    <a href="/home">Home</a>
    <a href="/about">About</a>
    <a href="/gallery">Gallery</a>
    <a href="contact">Contact</a>
    <a href="/help">Help</a>''')
def help(req):
    return HttpResponse('''
    <a href="/home">Home</a>
    <a href="/about">About</a>
    <a href="/gallery">Gallery</a>
    <a href="/contact">Contact</a>
    <a href="help">Help</a>''')
