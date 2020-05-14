% Gavin Martin
% lab_1.pl - lab 12


% Exercises 1.4

%Butch is a killer.
killer(butch).

%Mia and Marsellus are married.
married(mia, marsellus).

%Zed is dead.
dead(zed).

%Marsellus kills everyone who gives Mia a footmassage.
kills(marsellus, X) :- givesFootMassage(X, mia).

%Mia loves everyone who is a good dancer.
loves(mia, x) :- goodDancer(X).

%Jules eats anything that is nutritious or tasty.
eats(jules, X) :- nutritious(X).
eats(jules, X) :- tasty(X).

% The first three are facts, butch is a killer, they are married, and zed is dead. 
% THe last three are rules and conditions that make it true or false so I made them that way. 


%1.5: 

% Knowledge base: 
wizard(ron).
hasWand(harry).
quidditchPlayer(harry).
wizard(X):-  hasBroom(X),  hasWand(X).
hasBroom(X):-  quidditchPlayer(X).

% How does Prolog respond to the following queries?

% wizard(ron). - 
% responds true 
% This is because it is a fact that was recorded in the kb



% witch(ron). 
% - undefined procedure
% this is because witch was never defined in the kb so it can't query it.


% wizard(hermione). 
% - responds false
% - this is because herminoie isn't a quitttich player and is never said to have a wand
% - she can't be inffered to be a wizard, but she ins't explicitly called a wizard either, so she isn't one.


% witch(hermione).
% - responds undefined procedure
% - witch was never defined and therefore its query doesn't exist

% wizard(harry). - reponds true
% This is because it was inferred based on his quittich playing abilities, the fact that he has a wand and the 
% condition that he is one if he meets both criteria. 

% wizard(Y). - responds ron
% this responds Ron because he is the first to explicity be declared as a wizard

% witch(Y). - undefined procedure
% This is undefiend and so queries don't work with it. 


% b. 
% Yes these are represented. The If p then q is a feature of prolog and can be written like: 
q :- p
p.

% if q. is entered, then it will come back true because p was declared as true. 


% c. 
% - Horn clauses allow at most one positive literal which allows us to use variables we otherwise
% couldn't in propositional logic.

% d. 
% - It does support the distinction. We can tell the knowledge base certian facts like ron is a wizard with 
% facts and conditional rules. We can also ask certian things as well through queries. 

% wizard(X) :- magical(X) - TELL
% magical(harry) - TELL

% ? - wizard(harry). - ASK
% - true









