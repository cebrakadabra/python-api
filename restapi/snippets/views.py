from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

# Create your views here.

# [1 step] view refactored as a class based view --> better separation between different HTTP methods
# [2 step] view refactored --> using mixins to use generic class based views
# [3 step] The base class provides the core functionality, and the mixin classes provide the .list() and .create() actions.
# Then explicitly bind the get and post methods to the appropriate actions.

# [4 step] REST framework provides a set of already mixed-in generic views

# method for showing all (GET ALL) and insert one (POST new)
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

# method for showing a specific one (GET/:id) or update a specific one (PUT/:id)
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
