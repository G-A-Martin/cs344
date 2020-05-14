
% 3.2

directlyIn(katarina, olga).
directlyIn(olga, natasha).
directlyIn(natasha, irina).

in(X, Y) :- directlyIn(X, Y).
in(X, Y) :- directlyIn(X, Z), in(Z, Y).

% Prolog recursively uses the in and directly in to expand backwards up the chain until it gets to the end

% 4.5
tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

% base case
listtran([],[]).
listtran([G | X], [E | Y]) :- tran(G, E), listtran(X, Y).


% ?- listtran([eins,neun,zwei],X).
% X  =  [one,nine,two].

% ?- listtran(X,[one,seven,six,two]).
% X  =  [eins,sieben,sechs,zwei].


%Prolog recursively fills up the english list with words by calling tran funnction and listtran function 

% b. Yes it does impliment modus ponens. It uses first order logic to acomplish this. Variables in prolog can be defined and used

human(gavin).
completely_corrupted_by_sin_becuase_of_fall(X) :- human(X).

% ?- completely_corrupted_by_sin_becuase_of_fall(gavin).
% -> "true"


