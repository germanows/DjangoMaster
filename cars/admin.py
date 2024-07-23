from django.contrib import admin
from cars.models import Car
class carAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model','brand')

admin.site.register(Car, carAdmin)
#diz aqui o que será registrado, e com que parâmetros.
#os parâmetros são ModelAdmin e o que será registrado, é car.

