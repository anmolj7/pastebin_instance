from django.shortcuts import render, redirect
from django.http import HttpResponse
from .db_operations import get_results, add_to_database


def home(request):
    return render(request, "index.html")


def save_text(request):
    text = request.POST['text_input']
    text_id = add_to_database(text)
    return redirect(f'/view_paste/{text_id}')


def get_texts(request):
    return HttpResponse(f'The Saved Values In database: {get_results()}')


def convert_list_to_dict(List: list):
    return {x[0]:x[1] for x in List}


def view_paste(request, text_id):
    return HttpResponse(convert_list_to_dict(get_results())[str(text_id)])