from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics

# Create your views here.

# view refactored as a class based view --> better separation between different HTTP methods
# view refactored --> using mixins to use generic class based views
#The base class provides the core functionality, and the mixin classes provide the .list() and .create() actions.
# Then explicitly bind the get and post methods to the appropriate actions.

# method for showing all (GET ALL) and insert one (POST new)
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Pretty similar. Again we're using the GenericAPIView class to provide the core functionality,
# and adding in mixins to provide the .retrieve(), .update() and .destroy() actions.

# method for showing a specific one (GET/:id) or update a specific one (PUT/:id)
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
