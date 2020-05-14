

burn(X) :- witch(X).
witch(X) :- wood(X).



wood(X) :- floats(X).

floats(X) :- equalWeight(duck, X).

equalWeight(duck, woman).

