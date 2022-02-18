from rich.console import Console # pip3 install Rich
from rich.table import Table
from speakListen import *


def print_menu():
    speak("I can do the following")
    table = Table(title="\nI can do the following :- ", show_lines = True) 

    table.add_column("Sr. No.", style="cyan", no_wrap=True)
    table.add_column("Task", style="yellow")
    table.add_column("Command", justify="left", style="green")

    table.add_row("1", "Speak Text entered by User", "Speak out the following text")
    table.add_row("2", "Search anything on Google", "Search on Google")
    table.add_row("3", "Search anything on Wikipedia", "Search on Wikipedia")
    table.add_row("4", "Read a MS Word(docx) document", "Read MS Word document")
    table.add_row("5", "Read a PDF document", "Read PDF document")
    table.add_row("6", "Read a book(PDF)", "Read a book ")
    table.add_row("7", "Quit the program", "Python close")

    console = Console()
    console.print(table)

#print_menu()