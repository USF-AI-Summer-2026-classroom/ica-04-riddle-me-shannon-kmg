from logic import *

# Propositions

J, P, R, C, a, c, b, u, t, r, p, w, s, k, v, l, i, o = vars(
    "J",
    "P",
    "R",
    "C",
    "a",
    "c",
    "b",
    "u",
    "t",
    "r",
    "p",
    "w",
    "s",
    "k",
    "v",
    "l",
    "i",
    "o",
)

# J = vars('J') #joker
# P = vars('P') #penguin
# R = vars('R') #riddler
# C = vars('C') #common criminal
#
# a = vars('a') # acid
# c = vars('c') # cards
# b = vars('b') # buzzer
#
# u = vars('u') # umbrella
#
# t = vars('t') # tell-tale clue
#
# r = vars('r') # riddles
# p = vars('p') # puzzles
# w = vars('w') # word games

# s - small crime
# k - bank robbery
# v - supervillan
# l - large crime
# i = crime
# o - hole in ground

# Formulas
# a crime has been committed
f01 = i

# the crime is either a small crime or a large crime
# (iff crime then small crime or large crime)
f02 = i.iff((s | l))

# the joker, penguin and riddler are supervillans
# (iff villan committed then joker committed or penguin committed or riddler committed)
f03 = v.iff((J | P | R))

# low level criminals commit small crimes
# (iff small crime then criminal committed)
f04 = C.iff(s)

# bank robbery is a small crime
# (if bank robbery then small crime)
f05 = k >> s

# villains commit large crimes and leave tell-tale clues
# (iff villain committed then large crime and tell-tale clue left)
f06 = v.iff((l)) & v.iff((t))

# the joker leaves acid burs or playing cards or joy buzzers
# (iff joker committed then acid burns left or playing cards left or joy buzzers left)
f07 = J.iff((a | c | b))

# the penguin leaves marks in the ground with his umbrella
# (iff penguin commited then umbrella marks left)
f08 = P.iff(u)

# the riddler only leaves riddles, puzzles or word games
# (iff riddler committed then riddles left or puzzles left or word games left)
f09 = R.iff((r | p | w))

# a hole in the ground was left
f10 = o

# a hole in the grand could be left from an umbrella or an acid burn
# (iff acid burn left or umbrella mark left then hole in the ground left)
f11 = o.iff((u | a))

# no other clues were found at the scene
f12 = ~c & ~b & ~r & ~p & ~w


# ArgumentForms
joker = ArgumentForm(
    f01, f02, f03, f04, f05, f06, f07, f08, f09, f10, f11, f12, conclusion=J
)
penguin = ArgumentForm(
    f01, f02, f03, f04, f05, f06, f07, f08, f09, f10, f11, f12, conclusion=P
)
riddler = ArgumentForm(
    f01, f02, f03, f04, f05, f06, f07, f08, f09, f10, f11, f12, conclusion=R
)
common = ArgumentForm(
    f01, f02, f03, f04, f05, f06, f07, f08, f09, f10, f11, f12, conclusion=C
)

# joker.print_truth_table()
print("Who definitely committed this crime:")
print("A low-level criminal: ", common.is_valid())
print("The Joker: ", joker.is_valid())
print("The Penguin: ", penguin.is_valid())
print("The Riddler: ", riddler.is_valid())
