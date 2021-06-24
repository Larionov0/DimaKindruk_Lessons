from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.name}"


class Game(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    min_age = models.IntegerField(default=0)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return f'Гра {self.name} ({self.min_age})'


class Post(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    name = models.CharField(max_length=60)
    text = models.TextField(max_length=2000)

    rate = models.IntegerField()

    def __str__(self):
        return f"Пост про {self.game.name}: '{self.name}' ({self.rate} / 10)"
