from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.

class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=60)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    is_auction = models.BooleanField("уместен ли торг", help_text="Отметьте, если торг по объявлению уместен.")
    updated_at = models.DateTimeField("дата обновления", auto_now=True)
    created_at = models.DateTimeField("дата публикации", auto_now_add=True)

    @admin.display(description="дата публикации")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                "<span style='color: green; font-weight: bold'>Сегодня в {} </span>", created_time
            )
        return self.created_at.strftime("%d.%m.%Y - %H:%M")

    class Meta:
        db_table = "advertisements"

    # def __str__(self):
    #     return '%s %s' % (self.title, self.price)
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

# from app_advertisements.models import Advertisement
# advertisement = Advertisement.objects.create(title="Test1", description="Test2", price=115.22, is_auction=True)
