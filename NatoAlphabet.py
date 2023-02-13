import sys
import subprocess

Alphabeth = {
'A':"Alfa",
'B':"Bravo",
'C':"Charlie",
'D':"Delta",
'E':"Echo",
'F':"Foxtrot",
'G':"Golf",
'H':"Hotel",
'I':"India",
'J':"Juliet",
'K':'Kilo',
'L':"Lima",
'M':"Mike",
'N':"November",
'O':"Oscar",
'P':"Papa",
'Q':"Quebec",
'R':"Romeo",
'S':"Sierra",
'T':"Tango",
'U':"Uniform",
'V':"Victor",
'W':"Whiskey",
'X':"X-ray",
'Y':"Yankee",
'Z':"Zulu",
' ':"___",
'0':"Zero",
'1':"One",
'2':"Two",
'3':"Three",
'4':"Four",
'5':"Five",
'6':"Six",
'7':"Seven",
'8':"Eight",
'9':"Nine",
'-':"-",
}
def header():
    print("==========================================")
    print("    NATO ALPHABET 1.0 BY IGOR MITROVIC    ")
    print("==========================================")
    print("Enter ! to quit, % to clear screen\n")

header()

while(True):
    text = input("Enter a word: ").upper()
    if(text == '!'):
        quit()
    elif(text == '%'):
        operating_system = sys.platform
        if operating_system == 'win32':
            subprocess.run('cls',shell=True)
            header()
            continue
        elif operating_system == 'linux' or operating_system == 'darwin':
            subprocess.run('clear',shell=True)
            header()
            continue
    else:
        if(all(n in Alphabeth for n in text) == True):
            NATOO = ' '.join([Alphabeth[n] for n in text])
            print("\n",NATOO,"\n")
        else:
            print("String contains non NATO characters ")

