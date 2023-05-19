from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializer import NoteSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'EndPoint': '/notes/',
         'method': 'GET',
         'body': None,
         'description': 'Returns an array of notes'
         },
        {
            'EndPoint': '/notes/id',
         'method': 'GET',
         'body': None,
         'description': 'Returns a single note object'
         },
        {
            'EndPoint': '/notes/create/',
         'method': 'POST',
         'body': {'body': ""},
         'description': 'Creates a new note'
         },
        {
        'EndPoint': '/notes/update/',
         'method': 'PUT',
         'body': {'body': ""},
         'description': 'Updates a note with data sent in'
         },
        {
        'EndPoint': '/notes/delete/',
         'method': 'DELETE',
         'body': None,
         'description': 'Deletes an existing note'
         }
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data
    
    note = Note.objects.create(
        body = data['body']
    )
    
    serializer = NoteSerializer(note, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data = data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')