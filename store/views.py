from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from store.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

def index(request):



    num_books = Book.objects.all().count()
    num_copy = BookCopy.objects.all().count()
    
    context = {
        'num_books': num_books,
        'num_copy' : num_copy,
    }
    return render(request, 'store/index.html', context=context)

"""def bookDetailView(request, bid):
    model = Book
    template_name='store/book_detail.html'
    queryset = Book.objects.all()

    context={
     "detail" : queryset,
        
    }
    # START YOUR CODE HERE
    
    
    return render(request,template_name, context=context) """

class Detailview(generic.DetailView):
    model = Book
    template_name = 'store/book_detail.html'
    def book_detail_view(request, primary_key):
      book = Book.objects.get(pk=primary_key)
      return render(request, template_name, context={'book': book})

def bookListView(request):
    model = Book
    template_name='store/book_list.html'
    queryset = Book.objects.all()
    
    context={
        "books" : queryset,


                    # set here the list of required books upon filtering using the GET parameters
    }
   
    # START YOUR CODE HERE
    return render(request,'store/book_list.html', context=context)

@login_required
def viewLoanedBooks(request):
    model = Book
    queryset = Book.objects.all()
    template_name='store/loaned_books.html'
    context={
        'copy': queryset,
    }
    '''
    The above key books in dictionary context should contain a list of instances of the 
    bookcopy model. Only those books should be included which have been loaned by the user.
    '''
    # START YOUR CODE HERE
    


    return render(request,template_name,context=context)

@csrf_exempt
@login_required
def loanBookView(request):
    response_data={
        'message':1,
    }
    '''
    Check if an instance of the asked book is available.
    If yes, then set message to 'success', otherwise 'failure'
    '''
    # START YOUR CODE HERE
    book_id = {{book.id}} # get the book id from post data


    return JsonResponse(response_data)

'''
FILL IN THE BELOW VIEW BY YOURSELF.
This view will return the issued book.
You need to accept the book id as argument from a post request.
You additionally need to complete the returnBook function in the loaned_books.html file
to make this feature complete
''' 
@csrf_exempt
@login_required
def returnBookView(request):
    pass







def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"NEW account created:{username}")
            login(request, user)
            messages.info(request, f"you are now logged in as {username}")
            return redirect("store:index")
        else:
           for msg in form.error_messages:
               messages.error(request, f"{msg}: {form.error_messages[msg]}")    


    form = UserCreationForm
    return render(request, "store/register.html",
                   context={"form":form})
    
def logout_req(request):
    logout(request)
    messages.info(request, "logged out succesfully!!")
    return redirect("store:book-list")


def login_req(request): 
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are now logged as {username}")
                return redirect("store:book-list")
            else:
               messages.error(request, f"invalid credentials")  

    else:
               messages.error(request, f"invalid credentials")  
           



    form = AuthenticationForm()
    return render(request, "store/login.html", {"form":form})

