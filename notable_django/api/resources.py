

from tastypie.resources import ModelResource
from api.models import Note
from tastypie.authorization import Authorization

#We import our model, and create a resource from it. The queryset (what models the resource is concerned with) is all note objects.
#we also name the resource appropriately: ‘note’. This will be important for URLs.
class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization = Authorization()
        fields = ['title', 'body']

