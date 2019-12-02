from polls.models import Question, Choice, WordBook, Word
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import models
import random
from django import template

# Create your views here.

register = template.Library()

@register.simple_tag
def random_int():
    return random.randint(0, 1)

def main(request):
    wordbook_list = WordBook.objects.all()
    context = {'wordbook_list':wordbook_list}
    return render(request, 'polls/main.html', context)

def words(request, wordbook_id):
    #word_list = Word.objects.all().prefetch_related('wordbook').wordbook
    #word_list = get_object_or_404(Word, pk = wordbook_id)
    wordbook = get_object_or_404(WordBook, pk = wordbook_id)

    return render(request, 'polls/words.html',{'wordbook':wordbook})

def makebooks(request, latest_wordbook_id):
    new_book_name = request.POST['book_name']
    id = latest_wordbook_id + 1

    new_book = models.WordBook(book_name = new_book_name, id = id)
    new_book.save()
    return HttpResponseRedirect(reverse('polls:main', args=()))

def makewords(request, wordbook_id):
    wordbook = get_object_or_404(WordBook, pk = wordbook_id)
    new_eng_word = request.POST['eng_word']
    new_kor_word = request.POST['kor_word']

    new_word = models.Word(kor_word = new_kor_word, eng_word = new_eng_word, wordbook = wordbook)
    new_word.save()
    return HttpResponseRedirect(reverse('polls:words', args=(wordbook.id,)))

def study(request, wordbook_id, cnt):
    wordbook = get_object_or_404(WordBook, pk = wordbook_id)
    return render(request, 'polls/study.html', {'wordbook':wordbook, 'cnt':cnt})

def check(request, wordbook_id, eng_word, cnt):
    wordbook = get_object_or_404(WordBook, pk = wordbook_id)
    kor_word = request.POST['kor_word']

    for word in Word.objects.all:
        if word.wordbook.id == wordbook_id:
            if word.kor_word == kor_word and word.eng_word == eng_word:
                cnt = cnt + 1
                #맞음

    print(cnt)
    return HttpResponseRedirect(reverse('polls:study', args=(wordbook.id, cnt,) ))

def result(request, cnt):
    return render(request, 'polls/result.html', {'cnt':cnt})

def remove(request, wordbook_id):
    wordbook = get_object_or_404(WordBook, pk = wordbook_id)
    wordbook.delete()   

    return HttpResponseRedirect(reverse('polls:main', args=() ))

def removeword(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    wordbook_id = word.wordbook.id
    word.delete()

    return HttpResponseRedirect(reverse('polls:words', args=(wordbook_id, ) ))

            

