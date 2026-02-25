# This project repo is for OAuth implementation in Django with JWT by using django-allauth for social login.
## I took here Google as a OAuth service provider.

## Let's taste this implementation for getting the help in cooking your recipe of Authorization:

### Firstly take the items of recipe such as code:

so clone my repo -->

```
git clone https://github.com/mangalji/Oauth_implementation_3_self.git

cd Oauth_implementation_3_self
```
Now create the virtual environment and activate it:
```
python3 -m venv .venv

source .venv/bin/activate
```

then search, found and ready your spices means install the dependencies:

```
pip install -r requirements.txt
```

now bring that special utensil you'll use to make this recipe means the Google OAuth client id and secret.
for this you need to go to :
> [Google OAuth provider](console.cloud.google.com).

There, select a new project with **no organization**. Then search got "**Credentials**" in the search box. You'll see an option called **New Credentials** - click on it. If it's already created, that's fine. If not, see on the left side bar, click on **Overview**, and then click on the **Get Started**. After that, select **External**, enter your Email id, and then choose your application type.

Next, add your **URIs**, including the login and logout redirect **URIs**. Then click create. From there, you'll get the **Cliend ID** and **Client Secret** - make sure to store them safely somewhere secure lie **.env** and this **.env** in **.gitignore**

## Now run the migrations and then migrate:

```
python3 manage.py runserver
```


# Thanks for visiting my GitHub.......... 
## Ram Ram 🙏🙏