from django.db import models
import uuid

# Create your models here.
class Entreprise(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False # Prevents the UUID from being manually edited in the admin or forms
    )
    sigle = models.CharField(max_length=20,unique=True)
    denomination = models.CharField(max_length=255)
    description = models.TextField()
    secteursactivite = models.CharField(max_length=255)
    villescouvertes = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=10,unique=True)
    adresse = models.CharField(max_length=255)
    siteweb = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='entreprises/', blank=True, null=True)

    def whatsapp_link(self):
        tel = self.telephone.replace("+", "").replace(" ", "")
        return f"https://wa.me/{tel}"
    def __str__(self):
        return self.sigle