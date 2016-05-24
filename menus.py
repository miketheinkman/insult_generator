#!/usr/bin/python


def three_prints():
    """A function tor create terminal space"""
    print
    print
    print


def main_menu():
    """These print statements make up the main menu"""
    three_prints()
    print "Welcome to Insult Generator"
    print
    print "What would you like to do?"
    print "--------------------------"
    print
    print "1) Configure database"
    print "2) Generate insults"
    print "3) Exit"
    three_prints()


def add_menu():
    """Gives you adding options"""
    three_prints()
    print "Add new insult data"
    print "--------------------------"
    print "1) Add new directive"
    print "2) Add new adjectives"
    print "3) Add new name"
    print "4) Main menu"
    print "5) Exit"
    three_prints()
