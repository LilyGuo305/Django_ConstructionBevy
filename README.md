## Prerequisite

In order to successfully build the project, the following packages are required before building the django server:

	pip3 install django-allauth # Using allauth for login page
	pip3 install django-crispy-forms # To make forms looks better

You could use the following command to create a admin to access Django administration:

	python3 manage.py createsuperuser

## Build Project

After having all prerequisite packages, you can simply build the project from the root app dir:

	cd ~/Django_ConstructionBevy/ConstructionBevy
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py runserver

The server would run locally on 

	http://localhost:8000/

## Project Structure

This project uses django-allauth to handle user sign up/login. Beyong that, there are three apps in the ConstructionBevy project:

### 1. ConstructionBevy

This is the root app. The urls for accessing all sub-apps are:

	urlpatterns = [
    	path('admin/', admin.site.urls), # Django administration
    	path('', include('Home.urls')), # Home app
    	path('accounts/', include('allauth.urls')), # django-allauth templates used for login pages
    	path('network/', include('Network.urls')), # Network app
	]

### 2. Home

This app contains all front-end/back-end logics related to home pages. The urls patterns for the home app are:

	urlpatterns = [
    	path('', Index.as_view(), name='index'), # root home page
	]

### 3. Network

This app contains all front-end/back-end logics related to inbox pages. The urls patterns for the network app are:

	urlpatterns = [
    	path('inbox/', ListThreads.as_view(), name='inbox'), # root inbox page
    	path('inbox/create-thread/', CreateThread.as_view(), name='create-thread'), # create channel between two users
    	path('inbox/<int:pk>', ThreadView.as_view(), name='thread'), # get channels
    	path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'), # create messages
    	path('inbox/delete/<int:pk>', DeleteThread.as_view(), name='delete-inbox'), # delete channel
    	path('inbox/<int:inbox_pk>/delete-message/<int:pk>', DeleteMessage.as_view(), name='delete-message') # delete messages
	]

Furthermore, there is another sub-folder called "templates", which stores all logics and the CSS styling templates from django-allauth and bootstrap4. For more details about django-allauth templates, please see: https://github.com/pennersr/django-allauth/tree/master/allauth. For more details about bootstrap4, see https://getbootstrap.com/docs/4.0/getting-started/introduction/
