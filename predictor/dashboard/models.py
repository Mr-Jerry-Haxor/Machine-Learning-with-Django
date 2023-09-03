from decimal import Decimal
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.linear_model import LogisticRegression
import joblib

# Create your models here.



class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    mcv = models.PositiveIntegerField(
        validators=[MinValueValidator(65), MaxValueValidator(103)], null=True)
    alkphos = models.PositiveIntegerField( validators=[MinValueValidator(23), MaxValueValidator(138)], null=True)
    sgpt = models.PositiveIntegerField(validators=[MinValueValidator(4), MaxValueValidator(155)], null=True)
    sgot = models.PositiveIntegerField(validators=[MinValueValidator(5), MaxValueValidator(82)], null=True)
    gammagt = models.PositiveIntegerField(validators=[MinValueValidator(5), MaxValueValidator(297)], null=True)
    drinks = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(20.0)],null=True)
    predictions = models.CharField(max_length=200, blank=True)
    remedies = models.CharField(max_length=200, blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     ml_model = joblib.load('ml_models/ml_bupa_model.joblib')
    #     self.predictions = ml_model.predict(
    #         [[self.mcv, self.alkphos, self.sgpt, self.sgot, self.gammagt, self.drinks]])
    #     return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']

    # def __str__(self):
    #     return self.name
