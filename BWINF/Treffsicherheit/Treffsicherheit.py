Ada =       [0, 0, 0, 0, 0, 0, 0]
Nancy =     [1, 0, 0, 1, 1, 0, 0]
Niklaus =   [2, 2, 2, 1, 2, 2, 2]
Grace =     [2, 1, 2, 2, 1, 0, 0]
Edsger =    [0, 1, 2, 2, 1, 0, 0]
Rosza =     [1, 2, 1, 2, 0, 1, 1]

Freunde = [Ada, Nancy, Niklaus, Grace, Edsger, Rosza]
anzahl = lambda x, y: x.count(y)



indexes_equal_0 = [index for Freund in Freunde for index, element in enumerate(Freund) if element == 0]

amoutn_0_in_each_day = dict(zip([0, 1, 2, 3, 4, 5, 6], [anzahl(indexes_equal_0, x) for x in [0, 1, 2, 3, 4, 5, 6]]))



Freunde_die_am_besten_tag_nicht_können = [(element, index) for index, element in enumerate(Freunde) if element[max(amoutn_0_in_each_day, key=lambda x: amoutn_0_in_each_day[x])] != 0]




# def multiple_index(array, value):
#     return [index for index, element in enumerate(array) if element == value]

