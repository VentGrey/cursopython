from django.db import models

class Homework(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Título")
    description = models.TextField(verbose_name = "Descripción")
    notes = models.FileField(upload_to = "notes", null = True, blank = True, verbose_name = "Apuntes")

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Título", null = True, blank = True)
    image = models.ImageField(upload_to = "background", verbose_name = "imagen")

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imágenes"
        ordering = ["image"]

    def __str__(self):
        return self.title
