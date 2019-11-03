import os
from django.db import models
from django.conf import settings
from django.utils.timezone import now as timezone_now
from django.utils.translation import ugettext_lazy as _

def upload_to(instance, filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    return 'document/%s%s' %(
        now.strftime("%Y/%m/%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )

class Document(models.Model):
    """Dokument w formie obrazka - skan zadań z rozwiązaniami
    u góry powinien znajdowac się id dokumentu prawdopodobnie w formie kodu kreskowego"""
    code = models.CharField(max_length=255) # uniklany kod kreskowy dokumentu - moze być wprowadzany przez użytkownika
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # dopuszczam zmianę dokumentu    
    # using custom user model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, # autor który dodał dokument
                                on_delete=models.CASCADE,
                                related_name="documents")
    ### przechowywanie całgo dokumentu
    document_file = models.ImageField(_("Obraz"),
        upload_to=upload_to,
        blank=True,
        null=True,
    ) # ściezka do pliku graficznego

    class Meta:
        verbose_name = _(u"Dokumnet sprawdzianu")
        verbose_name_plural = _(u"Dokumenty sprawdzianów")
    
    def __str__(self):
        return self.code


class Task(models.Model):
    """Zadania będące fragmentami skanu, jeden nauczyciel (autor odpowiedzi) moze udzielić tylko jednej notatki/puntkowania zadania"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # dopuszczam aktualizację danych punktów/notatki
    max_points = models.IntegerField(null = False) # maksymalna ilośc punktów za zadanie
    score = models.IntegerField(default=0) # liczba otrzymanych punktów
    note = models.TextField(blank = True) #notatka nauczyciela co do rozwiązania, nieobowiązkowa
    document = models.ForeignKey(Document,
                                    on_delete=models.CASCADE,
                                    related_name="tasks") # wskazuje na główny dokuemnt
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    ### najtrudniejsza częśc - przechowywane fragmentów zadania (po narzedziu wycinania)
    # body = # fragment skanu zadania z treścią

