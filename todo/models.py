from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

user = get_user_model()


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان فعالیت')
    content = models.TextField(max_length=300, verbose_name='توضیجات')
    priority = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return f'{self.title} is done : {self.is_done}'

    class Meta:
        db_table = 'todos'
