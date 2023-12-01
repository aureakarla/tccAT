from django.db import models


class Especies(models.Model):
    nome_especie = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to='especies/%y/%m/%d')
    introducao = models.TextField()
    origem = models.TextField()
    causa_efeito = models.TextField()
    prevencao = models.TextField()

    def __str__(self):
        return self.nome_especie
