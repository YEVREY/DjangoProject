from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=60)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    is_auction = models.BooleanField("уместен ли торг", help_text="Отметьте, если торг по объявлению уместен.")
    updated_at = models.DateTimeField("дата обновления", auto_now=True)
    created_at = models.DateTimeField("дата публикации", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField("изображение", upload_to="advertisements", blank=True)

    @admin.display(description="дата публикации")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color: green; font-weight: bold'>Сегодня в {} </span>", created_time
            )
        return self.created_at.strftime("%d.%m.%Y - %H:%M")

    @admin.display(description="дата обновления")
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color: blue; font-weight: bold'>Сегодня в {} </span>", updated_time
            )
        return self.updated_at.strftime("%d.%m.%Y - %H:%M")

    @admin.display(description="изображение")
    def image_in_admin(self):

        return format_html(
            "<img src={} style='width: 50px; height: 50px'>", f"{settings.MEDIA_URL}{self.image}"
        )

    class Meta:
        db_table = "advertisements"

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"
