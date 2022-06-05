from . import parser, models
from django import forms


class ParserForm(forms.Form):
    MEDIA_CHOICE = (
        ("Plants", "Plants"),
        ("Dorama", "Dorama"),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        fields = [
            "media_type",
        ]

    def parse_data(self):
        if self.data["media_type"] == "Plants":
            plants_parser = parser.parser_func()
            for data in plants_parser:
                models.Plants.objects.create(**data)
        elif self.data["media_type"] == "Dorama":
            dorama_parser = parser.parser_func_dorama()
            for data in dorama_parser:
                models.Dorama.objects.create(**data)


            # if models.Plants.objects.filter(user=user).exists():
            #     pass
            # else:
            #     models.Plants.objects.create(user=user, count=count_number)