import random
import string

# -----------------------------two dimensional array--------------------------------- #

main_grid = []

grid_size_x = 40
grid_size_y = 32

for y in range(grid_size_x):            # building the two dimensional array

    row = []                            # create a array for the rows, that later
    main_grid.append(row)               # gonna be appended to the main_grid array.

    for x in range(grid_size_y):        # filling the rows with a place holder (0)
        row.append(None)

# -----------------------------------functions--------------------------------------- #


def print_main_grid():                  # printing the main grid
    for u in main_grid:
        print(*u)


def vertical_check(colum, start, stop):  # returns a vertical slice from the td-array
    return_array = []
    for cursor in range(start, start + stop):
        return_array.append(main_grid[cursor][colum])
    return return_array


def horizontal_check(row, start, stop):  # returns a horizontal slice from the td-array
    return_array = []
    for cursor in range(start, start + stop):
        return_array.append(main_grid[row][cursor])
    return return_array


def horizontal_word_placement(word, x, y):  # replaces horizontal the null object with the char form the word
    for itterator in range(0, len(word)):
        main_grid[x][y + itterator] = word[itterator]


def vertical_word_placement(word, x, y):    # replaces vertical the null object with the char form the word
    for itterator in range(0, len(word)):
        main_grid[x + itterator][y] = word[itterator]


def replace_placeholder():                  # goes through every char in the array and checks if it is a null object,
    for x in range(len(main_grid)):         # if it is a null object its gonna be replaced with a random ascii char.
        for y in range(len(main_grid[x])):
            if main_grid[x][y] is None:
                #main_grid[x][y] = random.choice(string.ascii_letters.lower())
                main_grid[x][y] = "."
            else:
                pass
# ----------------------------------------------------------------------------------- #


# takes a word form the vertical_words list.
# checks if something else than null objects is in the replacement area
# takes a random x and y coordinate and start and give the x and y coordinate to the replace function

def vertical_word(word):

    word_offset = len(word)

    cond = False
    while cond is False:

        x = random.choice(range(grid_size_x - word_offset))
        y = random.choice(range(grid_size_y))

        if all(ele is None for ele in vertical_check(colum=y, start=x, stop=len(word))):

            vertical_word_placement(word=word, x=x, y=y)
            cond = True

        else:
            pass

# ----------------------------------------------------------------------------------- #


# takes a word form the vertical_words list.
# checks if something else than null objects is in the replacement area
# takes a random x and y coordinate and start and give the x and y coordinate to the replace function

def horizontal_word(word):

    word_offset = len(word)

    cond = False
    while cond is False:

        x = random.choice(range(grid_size_x))
        y = random.choice(range(grid_size_y - word_offset))

        if all(ele is None for ele in horizontal_check(row=x, start=y, stop=len(word))):

            horizontal_word_placement(word=word, x=x, y=y)
            cond = True

        else:
            pass

# ----------------------------------------------------------------------------------- #


words = ["ABRUFDATUM" ,"ABSATZ","ACHTUNG","ALLMUSIC","ARCHIV","ARCHIVBOT","ARCHIVIERUNG","AUS","AUT","AUTOARCHIV","BABEL","BAUSTELLE","BBKL","BEGRIFFSKLÄRUNG","BEGRIFFSKLÄRUNGSHINWEIS","BEL","BELEGE","BENUTZER","BGR","BIBRECORD","BOOLAND","CAN","CENTER","CHARTS","COL","COMMONS","COMMONSCAT","COORDINATE","COORDINATEMAP","DDB","DEU","DISKUSSIONSSEITE","DOI","ERLEDIGT","FARBLEGENDE","FILM","FN","FNZ","FOLGENLEISTE","FRA","FUSSBALLDATEN","GEOQUELLE","GER","GNIS","HÖHE","IMDB","INFO","INFORMATION","INTERNETQUELLE","IPA","KALENDERSTIL","KASTEN","KATEGORIEGRAPH","LANG","LITERATUR","LIZENZUMSTELLUNG","MEDAILLENSPIEGEL","MULTILINGUAL","MUSIKCHARTS","NAVFRAME","NAVIGATIONSLEISTE","NOCOMMONS","ÖSTERREICHBEZOGEN","PERSONENLEISTE","PING","POSITIONSKARTE","PRO","SMILEY","SORT","TAXOBOX","TEXT","WAPPENRECHT","WEBARCHIV","WIKIDATA","WIKISOURCE","WIKTIONARY","ZITATION"]
for cursor in words:
    if random.choice(["vertical", "horizontal"]) == "vertical":
        vertical_word(cursor)
    else:
        horizontal_word(cursor)


replace_placeholder()   # replace the null objects with random ascii char
print_main_grid()       # printing the main_grid
