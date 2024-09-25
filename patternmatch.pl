% Base case: an empty pattern matches an empty data list
match([], []) :- 
    write('true'), nl.

% A variable can match any element
match([Var|PatternTail], [_|DataTail]) :-
    Var \= _, % Ensure that Var is treated as a variable
    match(PatternTail, DataTail).

% Match specific elements in the pattern with the data
match([Head|PatternTail], [Head|DataTail]) :-
    match(PatternTail, DataTail).

% If the pattern does not match, print false
match(_, _) :- 
    write(' '), nl.

% Example usage:
% ?- match([a, b], [1, 2, a, b]).
