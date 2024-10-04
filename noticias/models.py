from django.db import models


class Depoimentos(models.Model):
    DEPOIMENTOS_CHOICES = (
        ('depoimento', 'Depoimento'),
        ('discussao', 'Discussão')
    )
    email = models.EmailField(max_length=150)
    nome = models.CharField(max_length=150)
    depoimento_ou_discussao = models.CharField(
        max_length=11, choices=DEPOIMENTOS_CHOICES
    )
    relato = models.TextField()

    def __str__(self) -> str:
        return self.nome + ' - ' + self.email
