from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import View
from django.http import HttpResponseRedirect, Http404
import pandas as pd
from .models import *

# Create your views here.
def startPage(requests):
	atp = Assotiationtennisplayers.objects.all()
	grandslams = Grandslamtournament.objects.all()
	return render(requests, 'startpage.html', context={'organization': atp, 'grandslams': grandslams})



temp = 0
def login(request):
	global temp
	if request.POST:
		username = request.POST.get('login','')
		password = request.POST.get('password','')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect(temp)
		else:
			login_error = "User not found!"
			return render(request, 'login.html', context={'error' : login_error})
	temp = request.META.get('HTTP_REFERER')
	return render(request, 'login.html', context={'error' : ''})


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def toCsv(request, slug):
	grandslamtournament = Grandslamtournament.objects.filter(name__iexact=slug)
	necessary_id = -1
	for tournament in grandslamtournament:
		necessary_id = tournament.id
	stadiums = Stadium.objects.filter(grandslamtournament = necessary_id)
	games = Game.objects.select_related('player1', 'player2').filter(grandslamtournament = necessary_id)
	
	# Сохранение в csv
	numberRound = []
	dateTime = []
	player1 = []
	player2 = []
	score = []
	for item in games:
		numberRound.append(item.numberround)
		dateTime.append(item.date +' '+ item.time)
		player1.append(item.player1.fio)
		player2.append(item.player2.fio)
		score.append(str(item.score))

	filename = slug + ' Stats'
	columns = ['Number_round', 'Date & Time', 'Player1', 'Player2', 'Score']
	
	records = {columns[0]:numberRound, columns[1]:dateTime, 
				columns[2]:player1, columns[3]:player2,
				columns[4]:score}

	dataframe = pd.DataFrame(records)
	dataframe.to_csv(filename + '.csv', index=None, header=columns, sep=";")

	return HttpResponseRedirect('/{}'.format(slug))


def allNews(requests):
	news = News.objects.all()
	return render(requests, 'news.html', context={'news': news})

def createNews(requests):
	if requests.user.username == 'Player_writer' or not (requests.user.is_authenticated) :
		raise Http404
	if requests.method == 'POST':
		text = requests.POST.get('text')
		shortdescription = requests.POST.get('shortdescription')
		photo = requests.POST.get('photo')
		newNews = News(assotiationtennisplayers = 1, textnews=text, shortDescription=shortdescription, photo=photo)
		newNews.save()
		return HttpResponseRedirect('/news/{}'.format(str(newNews.id)))
	return render(requests, 'createNews.html')


def deleteNews(requests, slug):
	if requests.user.username == 'Player_writer' or not (requests.user.is_authenticated):
		raise Http404
	News.objects.filter(id__iexact=slug).delete()
	return HttpResponseRedirect('/news')


def updateNews(requests, slug):
	if requests.user.username == 'Player_writer' or not (requests.user.is_authenticated):
		raise Http404
	if requests.method == 'POST':
		id = slug
		text = requests.POST.get('text')
		shortdescription = requests.POST.get('shortdescription')
		photo = requests.POST.get('photo')
		newNews = News(id=slug, assotiationtennisplayers = 1, textnews=text, shortDescription=shortdescription, photo=photo)
		newNews.save(force_update=True)
		return HttpResponseRedirect('/news/{}'.format(str(newNews.id)))
	news = News.objects.filter(id__iexact=slug)
	return render(requests, 'updateNews.html', context={'news' : news})


def currentNews(requests, slug):
	oneNews = News.objects.filter(id__iexact=slug)
	return render(requests, 'oneNews.html', context={'oneNews': oneNews})


def players(requests):
	players = Player.objects.order_by('-countpoints')
	nations = Player.objects.values('nationality').distinct()
	flagList = True
	return render(requests, 'players.html', context={'players': players, 'nations':nations, 'flagList':flagList})


def playersTop10(requests):
	players = Player.objects.order_by('-countpoints')[:10]
	nations = Player.objects.values('nationality').distinct()
	flagList = True
	return render(requests, 'players.html', context={'players': players, 'nations':nations, 'flagList':flagList})


def playersTop20(requests):
	players = Player.objects.order_by('-countpoints')[:20]
	nations = Player.objects.values('nationality').distinct()
	flagList = True
	return render(requests, 'players.html', context={'players': players, 'nations':nations, 'flagList':flagList})


def playersTop30(requests):
	players = Player.objects.order_by('-countpoints')[:30]
	nations = Player.objects.values('nationality').distinct()
	flagList = True
	return render(requests, 'players.html', context={'players': players, 'nations':nations, 'flagList':flagList})


def playersTopCountry(requests, slug):
	players = Player.objects.filter(nationality__iexact=slug)
	nations = Player.objects.values('nationality').distinct()
	flagList = False
	return render(requests, 'players.html', context={'players': players, 'nations':nations, 'flagList':flagList})


def currentPlayer(requests, slug):
	player = Player.objects.filter(fio__iexact=slug)
	necessary_id = -1
	for human in player:
		necessary_id = human.id
	games = Game.objects.select_related('player1', 'player2').filter(Q(player1=necessary_id) | Q(player2=necessary_id))
	grandslamtournament = Grandslamtournament.objects.all()
	return render(requests, 'player.html', context={'player': player, 'games': games, 'grandslams':grandslamtournament})


def updatePlayer(requests, slug):
	if requests.user.username == 'News_writer' or not (requests.user.is_authenticated) :
		raise Http404
	if requests.method == 'POST':
		id = slug
		fio = requests.POST.get('fio')
		agedatebirth = requests.POST.get('agedatebirth')
		photo = requests.POST.get('photo')
		positionrating = requests.POST.get('positionrating')
		nationality = requests.POST.get('nationality')
		flag = requests.POST.get('flag')
		countpoints = requests.POST.get('countpoints')
		updatedPlayer = Player(id=slug, fio = fio, agedatebirth=agedatebirth, photo=photo, positionrating=positionrating, nationality=nationality, flag=flag, countpoints=countpoints)
		updatedPlayer.save(force_update=True)
		return HttpResponseRedirect('/player/{}'.format(str(updatedPlayer.fio)))
	player = Player.objects.filter(id__iexact=slug)
	return render(requests, 'updatePlayer.html', context={'player' : player})


def structure(requests):
	translators = Director.objects.select_related('divisioncontinent')
	sponsors = Sponsor.objects.all()
	return render(requests, 'structure.html', context={'translators': translators, 'sponsors': sponsors})


def grandslam(requests, slug):
	grandslamtournament = Grandslamtournament.objects.filter(name__iexact=slug)
	necessary_id = -1
	for tournament in grandslamtournament:
		necessary_id = tournament.id
	stadiums = Stadium.objects.filter(grandslamtournament = necessary_id)
	games = Game.objects.select_related('player1', 'player2').filter(grandslamtournament = necessary_id)
	return render(requests, 'grandslam.html', context={'grandslam': grandslamtournament, 'stadiums':stadiums, 'games':games})


def fourRound(requests, slug):
	grandslamtournament = Grandslamtournament.objects.filter(name__iexact=slug)
	necessary_id = -1
	for tournament in grandslamtournament:
		necessary_id = tournament.id
	stadiums = Stadium.objects.filter(grandslamtournament = necessary_id)
	games = Game.objects.select_related('player1', 'player2').filter(Q(grandslamtournament=necessary_id) & Q(numberround='4 round'))
	return render(requests, 'grandslam.html', context={'grandslam': grandslamtournament, 'stadiums':stadiums, 'games':games})


def quaterfinal(requests, slug):
	grandslamtournament = Grandslamtournament.objects.filter(name__iexact=slug)
	necessary_id = -1
	for tournament in grandslamtournament:
		necessary_id = tournament.id
	stadiums = Stadium.objects.filter(grandslamtournament = necessary_id)
	games = Game.objects.select_related('player1', 'player2').filter(Q(grandslamtournament=necessary_id) & Q(numberround='1/4 Finals'))
	return render(requests, 'grandslam.html', context={'grandslam': grandslamtournament, 'stadiums':stadiums, 'games':games})


def semifinal(requests, slug):
	grandslamtournament = Grandslamtournament.objects.filter(name__iexact=slug)
	necessary_id = -1
	for tournament in grandslamtournament:
		necessary_id = tournament.id
	stadiums = Stadium.objects.filter(grandslamtournament = necessary_id)
	games = Game.objects.select_related('player1', 'player2').filter(Q(grandslamtournament=necessary_id) & Q(numberround='1/2 Finals'))
	return render(requests, 'grandslam.html', context={'grandslam': grandslamtournament, 'stadiums':stadiums, 'games':games})


def final(requests, slug):
	grandslamtournament = Grandslamtournament.objects.filter(name__iexact=slug)
	necessary_id = -1
	for tournament in grandslamtournament:
		necessary_id = tournament.id
	stadiums = Stadium.objects.filter(grandslamtournament = necessary_id)
	games = Game.objects.select_related('player1', 'player2').filter(Q(grandslamtournament=necessary_id) & Q(numberround='Finals'))
	return render(requests, 'grandslam.html', context={'grandslam': grandslamtournament, 'stadiums':stadiums, 'games':games})