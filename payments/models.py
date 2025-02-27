from django.db import models

NULLABLE = {"blank": True, "null": True}

class Item(models.Model):
    """Модель товара"""

    name = models.CharField(
        max_length=50, verbose_name="Название", help_text="Введите название"
    )

    description = models.TextField(
        verbose_name="Описание", **NULLABLE, help_text="Введите описание"
    )

    price = models.PositiveIntegerField(verbose_name="строимость")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"