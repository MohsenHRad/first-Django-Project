from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان فعالیت')
    content = models.TextField(max_length=300, verbose_name='توضیجات')
    priority = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} is done : {self.is_done}'

    class Meta:
        db_table = 'todos'
