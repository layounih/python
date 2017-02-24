#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Modifiez l'import pour référencer votre module de gestion bancaire sur le modèle
# from packages import bank_module as bank
# Utiliser l'alias évite de mettre à jour tous les namespaces.

import gestion_bancaire as bank


def display_help():
    print("Account manager ready")
    print("[i] - Print account information")
    print("[d] - Make a deposit")
    print("[w] - Make a withdraw")

if __name__ == "__main__":

    account = bank.Account("Test", 500)

    while True:
        display_help()

        try:
            char_choice = str(input("Your choice ? "))
            if char_choice not in 'idw' or len(char_choice) != 1:
                raise ValueError("Select option in current choices")
        except (TypeError, ValueError):
            print("Please choose a valid option")
            continue

        if char_choice == 'i':
            print(account)

        else:
            try:
                value = int(input("How much ? "))
            except ValueError:
                print("Please give a value")
                continue

            if char_choice == "d":
                try:
                    account.deposit(value)
                except ValueError:
                    print("valeur positive attendue")
                    continue

            else:
                try:
                    account.withdraw(value)
                except ValueError as e:
                    print (e)
                    continue
