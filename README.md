# Machine-Learning-with-Django



    Title: BUPA liver disorders

    Source information:

    -- Creators: BUPA Medical Research Ltd.

    Past usage:

    -- None known other than what is shown in the PC/BEAGLE User's Guide (written by Richard S. Forsyth).

    Relevant information:

    -- The first 5 variables are all blood tests which are thought to be sensitive to liver disorders that might arise from excessive alcohol consumption. Each line in the bupa.data file constitutes the record of a single male individual. -- It appears that drinks>5 is some sort of a selector on this database. See the PC/BEAGLE User's Guide for more information.

    Number of instances: 345

    Number of attributes: 7 overall

    Attribute information:
        mcv mean corpuscular volume
        alkphos alkaline phosphotase
        sgpt alamine aminotransferase
        sgot aspartate aminotransferase
        gammagt gamma-glutamyl transpeptidase
        drinks number of half-pint equivalents of alcoholic beverages drunk per day
        selector field used to split data into two sets

    Missing values: none



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
