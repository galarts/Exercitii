
# if __name__=="__main__":
#     print("Bun venit la lectia 05.04 - lucru cu fisiere, modulul os, modulul json")


#     # ==================== LUCRUL CU FISIERE ====================
#     """
#     Mod de acces | Descriere
#     -------------+---------------------------------------------------------
#     r            | Deschide un fisier pentru citire. (implicit)
#     w            | Deschide un fisier pentru scriere. Creeaza un fisier nou daca nu exista sau rescrie fisierul daca exista.
#     x            | Deschide un fisier exclusiv pentru creare. In cazul in care fisierul exista deja, operatiunea esueaza.
#     a            | Deschide un fisier pentru a adauga date la sfarsitul fisierului fara a-l rescrie. Creeaza un nou fisier daca acesta nu exista.
#     t            | Deschide fisierul in modul text (implicit).
#     b            | Deschide fisierul in modul binar.
#     +            | Deschide un fisier pentru actualizare (citire si scriere)
#     """

#     # --------------------- Exercitiul 1 ---------------------
#     print("Exercitiul 1: Citeste continutul intreg al unui fisier text.")
#     # Solutia:
# with open("catalog.txt", 'r') as catalog:
#     print(catalog.read())


#     # --------------------- Exercitiul 2 ---------------------
#     print("\nExercitiul 2: Scrie un mesaj intr-un fisier nou creat.")
#     # Solutia:
# with open("Artur.txt", "w") as artur_cat:
#     artur_cat.write("Salut sunt Artur")


#     # --------------------- Exercitiul 3 ---------------------
#     print("\nExercitiul 3: Adauga text la sfarsitul unui fisier existent.")
#     # Solutia:
# with open("Artur.txt", 'a') as artur_write:
#     artur_write.write("\nAntonela s-a alaturat")
# artur_write.close()
# with open("Artur.txt", 'r') as artur_read:
#     print(artur_read.read())


#     # --------------------- Exercitiul 4 ---------------------
#     print("\nExercitiul 4: Citeste fiecare linie dintr-un fisier intr-o lista.")
#     # Solutia:
# with open("catalog.txt", "r") as catlog_read:
#     print(catlog_read.readlines())

#     # --------------------- Exercitiul 5 ---------------------
#     print("\nExercitiul 5: Itereaza prin fiecare linie din fisier.")

# with open("catalog.txt", "r") as catlog_read:
#     for i in catlog_read.readlines():
#         print(i)

#     # --------------------- Exercitiul 6 ---------------------
#     print("\nExercitiul 6: Creeaza un fisier nou doar daca acesta nu exista deja.")
# try:
#     with open("catalog.tx", "x") as new_doc:
#         new_doc.write("Saluta bre")
# except IndexError:
#     print("Index error")
# except NameError:
#     print("Salut, eroare de nume")
# except:
#     pass
# finally:
#         print("nus sunt erori")
#     # --------------------- Exercitiul 7 ---------------------
#     print("\nExercitiul 7: Deschide un fisier pentru citire si scriere.")
#     # Solutia:
# with open("Artur.txt", "+r") as vlad:
#     print(vlad.read())
#     vlad.write("\nBuan am dat de capat")

# --------------------- Exercitiul 8 ---------------------
#     print("\nExercitiul 8: Copiaza continutul unui fisier in altul.")
#     # Solutia 1:
# with open("catalog.txt", "r") as f:
#     data = f.read()
#     with open("Artur.txt", "w") as file:
#         file.write(data)
# Solutia 2(Utilizare in afara):
# data = " "
# with open("catalog.txt", "r") as f:
#     data = f.read()
# with open("Artur.txt", "w") as file:
#     file.write(data)
#     # # --------------------- Exercitiul 12 ---------------------
#     # print("\nExercitiul 12: Scrie mai multe linii in fisier folosind o lista.")
#     # # Solutia:
# li = [344, "fgggg", True, 1999, ["cico"]]
# li = [str(x)+"\n" for x in li]

# with open("Artur.txt", "w") as f:
#     f.writelines(li)
#     # --------------------- Exercitiul 13 ---------------------
#     print("\nExercitiul 13: Citeste un numar specific de caractere din fisier.")
#     # Solutia:

#     # --------------------- Exercitiul 14 ---------------------
#     print("\nExercitiul 14: Muta cursorul la inceputul fisierului dupa scriere.")
#     # Solutia:

#     # --------------------- Exercitiul 15 ---------------------
#     print("\nExercitiul 15: Deschide un fisier pentru scriere binara.")
#     # Solutia:

#     # --------------------- Exercitiul 16 ---------------------
#     print("\nExercitiul 16: Citeste continutul unui fisier binar.")
#     # Solutia:

#     # --------------------- Exercitiul 20 ---------------------
#     print("\nExercitiul 20: Foloseste modul '+' pentru a deschide un fisier pentru actualizare (citire si scriere).")
#     # Solutia:

#     # # --------------------- Exercitiul 23 ---------------------
#     # print("\nExercitiul 23: Obtine informatii despre pozitia curenta a cursorului folosind functia tell().")
#     # # Solutia:
#     #
#     #

#     # # ==================== MODULUL OS ====================
#     # --------------------- Exercitiul 1 ---------------------
#     print("Obtineti si afisati directorul curent de lucru.")
#     # Solutia:

#     # --------------------- Exercitiul 2 ---------------------
#     print("Creati un nou director numit 'test_dir' in directorul curent.")

#     # --------------------- Exercitiul 3 ---------------------
#     print("Redenumiti un fisier 'old_name.txt' in 'new_name.txt'.")
#     # Solutia:

#     # --------------------- Exercitiul 4 ---------------------
#     print("Verificati daca un fisier numit 'test_file.txt' exista in directorul curent.")
#     # Solutia:

#     # --------------------- Exercitiul 5 ---------------------
#     print("Listati toate fisierele si folderele din directorul curent.")
#     # Solutia:

#     # --------------------- Exercitiul 6 ---------------------
#     print("Obtineti si afisati informatii despre sistemul de operare.")
#     # Solutia:

#     # --------------------- Exercitiul 7 ---------------------
#     print("Creati un set de directoare imbricate 'folder/subfolder/nume'.")
#     # Solutia:

#     # --------------------- Exercitiul 8 ---------------------
#     print("Stergeti fisierul 'temp.txt'. Daca nu exista, afisati un mesaj corespunzator.")
#     # Solutia:

#     # --------------------- Exercitiul 9 ---------------------
#     print("Stergeti recursiv directoarele 'folder/subfolder/nume'.")
#     # Solutia:

#     # # --------------------- Exercitiul 10 ---------------------
#     # print("Alipiti numele de fisier 'file.txt' la calea 'dir/subdir' folosind os.path.join.")
#     # # Solutia:

#     # --------------------- Exercitiul 11 ---------------------
#     print(
#         "Obtineti dimensiunea fisierului 'example.txt' in bytes. Daca fisierul nu exista, afisati un mesaj corespunzator.")
#     # Solutia:
