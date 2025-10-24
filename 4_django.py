# Configurar apps:
## project/project/apps/name/apps.py > name = 'apps.name'
## project/project/settings.py > INSTALLED_APPS = [..., 'apps.name']

# Organizar apps:
## DJANGO_APPS = ['django...']
## LOCAL_APPS = ['apps...']
## THIRD_PARTY_APPS = []
## INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Modelos:
## Crear modelos:
## Class Materia(models.Model):
##  nombre = models.CharField(max_length=255)

## Class Carrera(models.Model):
##  nombre = models.CharField(max_length=255)

# Relacionar modelos:
## Class Materia(models.Model):
##  nombre = models.CharField(max_length=255)
##  carrera = models.ForeignKey('carrera.Carrera', on_delete=models.DO_NOTHING, null=True, related_name='materias')
##  docente = models.ForeignKey('docente.Docente', on_delete=models.DO_NOTHING, null=True, related_name='materias')

# Manager (Model.objects):
## Model.objects.all()
## Model.objects.first()
## Model.objects.last()
## Model.objects.filter(nombre="name")
## Model.objects.create(data)
## Model.objects.create(nombre="name", carrera=Carrera.objects.get(id=1))
## ...

# Admin Model (admin.ModelAdmin)
## Crear tabla
## from apps.carrera.models import Carrera

## Registrar -> mostrar en admin-panel
## @admin.register(Carrera)
## class CategoryAdmin(admin.ModelAdminj):
##  list_display = ('name', 'description')

## @admin.register(CategoryItem)
## class CategoryItem(admin.ModelAdmin):
##  list_display = ('category', 'item')

## Template View
# from django.views.generic import ListView

## class ItemTemplateView(ListView):
##   template_name = "items.html"
##   model = Item
##   context_object_name = "items"
##   ordering = ["-name"]
##   paginate_by = 2
##   queryset = Item.objects.filter(name__icontains="Type")

## from apps.item.views import ItemTemplateView
## ItemTemplateView.as_view()
##   .../items/list/?page=2
