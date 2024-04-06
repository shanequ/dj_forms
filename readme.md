

## Brief Intro

This project shows how to -
* use django forms/ model forms
* customise Django admin site

To run this project - 
1. pull the code from Github
2. create a virtual environment and install packages listed in `requirements.txt`
3. run - `./manage.py makemigrations`, and `./manage.py migrate`
4. load data `./manage.py loaddata data`
5. run the test server `./manage.py runserver`

To see some performance profiling results, uncomment
`cProfile` lines in `djform_admin/admin.py`, view the admin
site once, and use `snakeviz` to view the result under directory `djform_admin`:   
> `snakeviz admin.prof`

## Use `ModelForm` and Field Dependency 

### ModelForm

There are three different cases - 

1. A bound form, the `city` field's `queryset` depends on the value of `country` field;
2. A unbound form, but has default value for `country` field, then, 
   similar to case 1, the city `queryset` uses the default value of `country` to get the
   list of cities;
3. A unbound form with no value of `country`, set `city`'s `queryset` to none.

In the front end, Javascript code catches the change of `country`, then 
1. call the server to get a list of cities of the selected country;
2. then reset the options of `city` option element. Note that an empty `country`
   field will get a empty list of `city`.


## Other Techniques

### Reuse admin and auth templates
Copy following templates into project templates/registratyion/directory 

* `venv/lib/python3.x/site-packages/django/contrib/admin/templates/registration/*`
* `venv/lib/python3.x/site-packages/django/contrib/admin/templates/admin/login.html`


### Access Session Info

```
import pprint
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session

session_store = SessionStore()
session_1 = Session.objects.last()
pprint.pp(session_store.decode(session_1.session_data))
```

### Cookie Packages
```
django-cookie-law
django-cookie-consent  # this one seems more popular
```

## Form Field Choices - dependent on other field
* [youtube tutorial](https://www.youtube.com/watch?v=LmYDXgYK1so) 
* [Gitbub Repo](https://www.youtube.com/watch?v=LmYDXgYK1so)

## Notes
1. use `getlist()` to get the value(s) from `QueryDict` of a `request` instead of
   `get()`, because a field may have multiple values (for example, values of 
   a multi-choice input);

   >   ```
   >      for name in request.POST: 
   >          value = request.POST.getlist(name)
   >   ```
   However, in most cases, only need to loop through form's `cleaned_data` which is  
   a normal dict.

2. To use `optgroup` for `select` input, define a nested choices tuple as -

   > ```
   > BOOK_CHOICES = (
   >     (
   >          "Non-fiction", (
   >              ("1", "Deep Learning with Keras"),
   >              ("2", "Wed Development with Django"),
   >         )
   >     ),
   >     (
   >         "Fiction", (
   >             ("3", "Brave New World"),
   >             ("4", "The Great Gatsby"),
   >         )
   >     ),
   > )       
   > ```

3. form field and bound field:

   > - `form['name']` is a bound field and is string representation of an HTML input:    
   >    `str(form['name'])` -> `<input type="text" value="init_value" id="id_name" name="name" required maxlength="64" />`
   > - `form.fields['name'].field == form['name']` is `True`.

4. if `instance` and `initial` both are provided when creating a `ModelForm`,
   the values in `initial` overwrite `instance`'s values in the rendered HTML form. 

5. Extra fields can be defined in `ModelForm`, which are not 
   saved by the `form.save()`. They are in `form.cleaned_data`
   and can be processed in view function.


## Customise Admin Site

1. Create a new app `djform_admin`, add `apps.py` and `admin.py`
> ```
> apps.py:
> 
> from django.contrib.admin.apps import AdminConfig  
> class DjFormAdminConfig(AdminConfig):  
>     default_site = 'djform_admin.admin.DjFormAdmin'
>  
> admin.py:
> 
> from django.contrib import admin
> class DjFormAdmin(admin.AdminSite):
>     site_header = 'DjForm Admin'
>     # other customisations ...
> ```

2. Add the admin app into `settings.py`
> ```
> INSTALLED_APPS = [
>     # 'django.contrib.admin',   <-- no need to install this!!!
>     # the customised Admin site will take the default admin site role
>     'djform_admin.apps.DjFormAdminConfig',
>     'django.contrib.auth',
>     ...
> ```
3. That's all! no other changes are required.
