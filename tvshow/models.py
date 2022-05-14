from django.db import models


class Shows(models.Model):
    GENRE_CHOICE = (
        ("Drama", "Drama"),
        ("Horror", "Horror"),
        ("Comedy", "Comedy"),
        ("Fantasy", "Fantasy"),
        ("Sci-Fi", "Sci-Fi"),
        ("Anime", "Anime"),
        ("Romantic", "Romantic"),
        ("Action", "Action")
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="")
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE)
    quantity = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    age_control = models.PositiveIntegerField()

    def __str__(self):
        return self.title
