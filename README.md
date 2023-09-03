# Machine-Learning-with-Django

step 1: 

```bash
pip install virtualenv
```

step 2:

```bash
virtualenv env
```

step 3:

```bash
./env/bin/activate
```

step 4:

```bash
cd predictor
```

step 5:

```bash
pip install -r requirements.txt
```

step 6:

```bash
python manage.py makemigrations
```

step 7:

```bash
python manage.py migrate
```

step 8:

```bash
python manage.py migrate --run-syncdb
```

step 9:

```bash
python manage.py runserver
```
