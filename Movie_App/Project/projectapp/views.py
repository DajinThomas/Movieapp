from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})


def add(request):
    message = None

    if request.method == "POST":
        title = request.POST.get('title', )
        genre = request.POST.get('genre', )
        release_date = request.POST.get('release_date', )
        synopsis = request.POST.get('synopsis', )

        try:
            image = request.FILES['image_url']
            load_data = Movie(title=title, genre=genre, release_date=release_date, synopsis=synopsis, image_url=image)
            load_data.save()
            message = "Data added successfully."
        except MultiValueDictKeyError:
            message = "Failed to upload image. Please ensure you selected a file."

    return render(request, 'movie_form2.html', {'message': message})


from django.shortcuts import render, redirect
from django.contrib import messages  # Import messages module
from .forms import MovieForm

def update_movie(request, id):
    # Retrieve the Movie object with the specified ID
    edit_id = Movie.objects.get(id=id)

    # Create a MovieForm instance, populating it with data from the Movie object
    form = MovieForm(request.POST or None, request.FILES, instance=edit_id)

    # Check if the form is valid after submitting the data
    if form.is_valid():
        # Save the updated data to the database
        form.save()

        # Add a success message
        messages.success(request, 'Movie updated successfully.')

        # Redirect to the desired URL (you may want to update this)
        return redirect('/')

    # Render the template with the form and Movie object
    return render(request, 'movie_form.html', {'form': form, 'edit_id': edit_id})


def delete_movie(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        messages.error(request, 'Movie not found')
        return redirect('/')

    if request.method == "POST":
        movie.delete()
        messages.success(request, 'Movie deleted successfully')
        return redirect('/')
    else:
        return render(request, 'delete_confirmation.html', {'movie': movie})