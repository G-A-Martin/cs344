% Gavin Martin - Lab12


% Exercise 2.1, questions 1, 2, 8, 9, 14 - Give the necessary instantiations.
bread.
food(X). 

% 1. bread  =  bread - true
% 2. ’Bread’  =  bread - false
% 8. food(X)  =  food(bread) - yes because X = bread
% 9. food(bread,X)  =  food(Y,sausage) - yes because X = sausage and Y = bread
% 14. meal(food(bread),X)  =  meal(X,drink(beer)) - false






% Exercise 2.2 - Explain how Prolog does its unification and reasoning. If you have 
% issues getting the results you’d expect, are there things you can do to game the system?

house_elf(dobby).
witch(hermione).
witch(mcGonagall).
witch(rita_skeeter).
magic(X):-  house_elf(X).
%magic(X):-  wizard(X).
magic(X):-  witch(X).

% ?-  magic(house_elf). - false
% ?-  wizard(harry). - undefined procedure because wizard was never defined
% ?-  magic(wizard). - false
% ?-  magic(’McGonagall’). - false, but when I changed it away from a string, to mcGonagall, it worked 
% ?-  magic(Hermione). - responded with Hermione = dobby ; hermione = hermione ; hermione = rita_skeeta
    % - adding the ; as an or operator gave it heriomine. 

% The program didn't work until I commneted out the error producing wizard line. 

% Hermione search tree: 

% - searchs: 
% -  magic(X) -> house_elf(X) -> dobby, 
% -  magic(X) -> witch(X) -> hermione, 
% -  magic(X) -> witch(X) -> mcGonagall,  (only when she's not a string)
% -  magic(X) -> witch(X) -> rita_skeeter



% Does inference in propositional logic use unification? Why or why not?

%  - Inference in propositional logic uses unfication because it gives us the abillity to combine overlapping rules. 

% Does Prolog inferencing use resolution? Why or why not?

% - Yes, this can be seen in the way that it breaks down problems from multiple clauses and reduces them to one clause. 

