from django.db import models

# Create your models here.
class ButtonCall(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True)
    vchr_button_name = models.CharField(max_length=150)
    int_count = models.IntegerField()
    dat_created = models.DateTimeField(blank=True, null=True, auto_now = True)

    def __str__(self) -> str:
        return self.pk_bint_id

class UserDetails(models.Model):
    user_ptr_id = models.BigAutoField(primary_key=True)
    vchr_user_name = models.CharField(max_length=150)
    int_count = models.IntegerField()
    dat_joined = models.DateTimeField(blank=True, null=True, auto_now = True)
    
    def __str__(self) -> str:
        return self.pk_bint_id
