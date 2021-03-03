from django.db import models

# Create your models here.


class KMeans(models.Model):
    n_clusters = models.IntegerField(verbose_name="簇的个数")

    n_init = models.IntegerField(verbose_name="")

    max_iter = models.FloatField(verbose_name="最大迭代次数")

    tol = models.IntegerField(verbose_name="容忍度")

    precompute_distancesChoices = (("Auto","Auto"),("True","True"),("False","False"))
    precompute_distances = models.CharField(choices=precompute_distancesChoices,max_length=5)

    algorithmChoices = (("Auto","Auto"),("Full","Full"),("Elkan","Elkan"))
    algorithm = models.CharField(choices=algorithmChoices,max_length=5)

