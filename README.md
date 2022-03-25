# Django_email_messaging
- This is Django messaging webapp/POC you can have only one gmail id .
- By using this gmail id you can sent message to as many other gmails as per google provided permission.
- You can only sent messages not file of any kind.
- You just have to put your your Gmail id and password in **core.settings.py** file but remove it after use because its insecure.
> Make sure you do not save your Gmail Id and password in your setting make use of python os library.
> I have used : 
> - os.environ["EMAIL_USER"] : here will be your gmail id (real)
> - os.environ["EMAIL_PASS"] : here will be your gmail password of that id (real)

TO install django use below command :
```
python -m pip install django
```
> **python -m** used to install packages as per your python version.
