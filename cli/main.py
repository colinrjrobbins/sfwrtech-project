######################################################
# Filename: main.py
# Project Name: MovieList
# Created By: Colin Robbins
# Student ID: 400353539
# School: McMaster University
# Class: SFWRTECH 4SA3 - Software Architecture
# 
# Purpose: The is used to initialize the program
#          and start the main menu, initially to
#          check the users email with the database
#          connection and see if they have a previous
#          movie list stored, as well as to force a
#          system save upon exit. 
######################################################

# CUSTOM IMPORTS
from modules.menus import Menu

# Start of program.
if __name__ == '__main__':
    menu = Menu()
    menu.login_menu()
    menu.main_menu()