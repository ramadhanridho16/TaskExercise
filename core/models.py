from django.db import models


class Swim(models.Model):
    class Style(models.TextChoices):
        GAYA_BEBAS = "BE", "Gaya Bebas"
        GAYA_KATAK = "KA", "Gaya Katak"

    id = models.CharField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    swim_style = models.CharField(
        max_length=2, choices=Style.choices, default=Style.GAYA_KATAK)
    repetion = models.PositiveIntegerField(max_length=100)


class Category(models.Model):
    id = models.CharField(primary_key=True)
    category = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.category


class Calisthenic(models.Model):
    id = models.CharField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    calisthenic_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category')
    repetition = models.PositiveIntegerField()


class Run(models.Model):
    id = models.CharField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    distance = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    avg_speed = models.PositiveIntegerField()
    max_speed = models.PositiveIntegerField()


class Body(models.Model):
    id = models.CharField(primary_key=True)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    arm_circumference = models.PositiveIntegerField()
    leg_size = models.PositiveIntegerField()
    waist_size = models.PositiveIntegerField()
