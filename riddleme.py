from logic import *

# Propositions

J, P, R, C, a, c, b, u, t, r, p, w, s, k, v, l = vars('J', 'P', 'R', 'C', 'a',
                                                      'c', 'b',
                                                      'u','t','r','p','w', 's',
                                                      'k', 'v', 'l')

#J = vars('J') #joker
#P = vars('P') #penguin
#R = vars('R') #riddler
#C = vars('C') #common criminal
#
#a = vars('a') # acid
#c = vars('c') # cards
#b = vars('b') # buzzer
#
#u = vars('u') # umbrella
#
#t = vars('t') # tell-tale clue
#
#r = vars('r') # riddles
#p = vars('p') # puzzles
#w = vars('w') # word games

# s - small crime
# k - bank robbery
# v - supervillan
# l - large crime

# Formulas
f01 = t
f02 = t >> ~C
f03 = ~C >> (J | R | P)
f04 = R >> (r | p | w)
f05 = P >> u
f06 = J >> (a | c | b)

# ArgumentForms
joker = ArgumentForm(f01, f02, f03, f04, f05, f06, conclusion=J)
penguin = ArgumentForm(f01, f02, f03, f04, f05, f06, conclusion=P)
riddler = ArgumentForm(f01, f02, f03, f04, f05, f06, conclusion=R)
common = ArgumentForm(f01, f02, f03, f04, f05, f06, conclusion=C)

#joker.print_truth_table()

print('The Joker committed this crime:', joker.is_valid())
print('The Penguin committed this crime:', penguin.is_valid())
print('The Riddler committed this crime:', riddler.is_valid())
print('A common criminal committed this crime:', common.is_valid())
