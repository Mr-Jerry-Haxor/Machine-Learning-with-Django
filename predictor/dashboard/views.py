from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data
from sklearn.linear_model import LogisticRegression
import joblib
# Create your views here.


def index(request):
    return render(request, 'home.html')

def prediction(request):
    return render(request, 'prediction.html')

def bupa_liver(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            name = form.instance.name
            mcv = form.instance.mcv
            alkphos = form.instance.alkphos
            sgpt = form.instance.sgpt
            sgot = form.instance.sgot
            gammagt = form.instance.gammagt
            drinks = form.instance.drinks
            
            ml_model = joblib.load('ml_models/ml_bupa_model.joblib')
            prediction = ml_model.predict( [[mcv,alkphos,sgpt, sgot, gammagt, drinks]])
            prediction = prediction[0]
            if prediction == 1:
                prediction ="The patient is likely to have liver disease."
                remedies = "Maintain a Healthy Diet, Stay Hydrated, Limit Alcohol Consumption, Exercise Regularly, Maintain a Healthy Weight,Avoid Overuse of Medications."
            else:
                prediction= "The patient is not likely to have liver disease."
                remedies = ""
            data=Data(
                name = name,
                mcv = mcv,
                alkphos = alkphos,
                sgpt  = sgpt,
                sgot    = sgot,
                gammagt = gammagt,
                drinks = drinks,
                predictions = prediction,
                remedies = remedies
            )
            data.save()
            
            return redirect('dashboard-predictions')
    else:
        form = DataForm()
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)


def predictions(request):
    predicted_sports = Data.objects.all()
    context = {
        'predicted_sports': predicted_sports
    }
    return render(request, 'predictions.html', context)
