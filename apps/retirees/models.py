from django.db import models


class Retired(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    modified_data = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class RetiredInfo(models.Model):
    retired = models.OneToOneField(Retired, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=6,
        choices=(
            ('male', 'Male'),
            ('female', 'Female'),
        ),
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.retired.first_name} {self.retired.last_name}'


class RetiredAddress(models.Model):
    retired = models.ForeignKey(Retired, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.retired.full_name}'
