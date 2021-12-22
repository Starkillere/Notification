#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from win10toast import ToastNotifier
from datetime import datetime
import csv

class Notifsender(ToastNotifier):

	'''Notifsender permet de gérer les notification.
	   (Permet aussi d'associer un évenementt à une notification)
	   class mére: ToastNotifier()
	   -----------

	   Méthodes:
	   ---------
	   __init__(self, auteur:str, message:str):constructeur
	   affiche(self): appelle la méthode show_toast(...) de la class mére --> notification de l'evennement 
	   save(...): 
	'''

	def __init__(self, auteur:str=None, message:str=None):
		self.auteur:str = auteur
		self.message:str = message
		self.logo = None #A travailler
		self.duree:int = 10
		self.save_file:str = None
		self.date = str(datetime.now())
		self.is_from = None #Aplication d'où est issiue la notification (A travailler)
	
	def affiche(self, auteur:str=None, message:str=None):
		if self.auteur == None:
			self.auteur = auteur
		if self.message == None:
			self.message = message
		self.show_toast(self.auteur, self.message, threaded=True, icon_path=None, duration=self.duree)

	def save(self, save_file:str, auteur:str=None, message:str=None):
		if self.auteur == None:
			self.auteur = auteur
		if self.message == None:
			self.message = message
		self.save_file = save_file
		with open(self.save_file, 'a',  encoding='utf-8') as file:
			csv_writer = csv.writer(file, delimiter=',')
			csv_writer.writerow([self.auteur, self.message, self.date])
