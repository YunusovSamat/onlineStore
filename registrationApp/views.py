from django.shortcuts import render, get_object_or_404

# from


def registration_form(request):
    template = 'registrationApp/registration.html'
    # context = {
    #
    # }
    return render(request, template)
