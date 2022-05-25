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


class ShowsUser(models.Model):
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class ShowComment(models.Model):
    shows = models.ForeignKey(Shows,
                              on_delete=models.CASCADE,
                              related_name="shows_comment")
    user = models.ForeignKey(ShowsUser,
                             on_delete=models.CASCADE,
                             related_name="shows_user",
                             null=True)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.shows.title
