% Initial state
at(monkey, door, s0).
at(banana, middle, s0).
at(box, window, s0).
on_floor(s0).

% Actions
move(P1, P2, S, S) :- 
    on_floor(S),
    at(monkey, P1, S),
    at(box, P2, S).

climb(S, S1) :- 
    on_floor(S), 
    at(monkey, P, S), 
    at(box, P, S),
    S1 = s1.

push(P1, P2, S, S) :- 
    on_floor(S),
    at(monkey, P1, S),
    at(box, P1, S),
    move(P1, P2, S, S).

grasp(S, S1) :- 
    at(monkey, P, S), 
    at(banana, P, S),
    on_floor(S),
    S1 = s3.

% Define state transitions
transition(s0, s1) :- climb(s0, s1).
transition(s1, s2) :- push(door, window, s1, s2).
transition(s2, s3) :- grasp(s2, s3).

% Solve the problem
solve(S, []) :- 
    at(banana, P, S),
    at(monkey, P, S),
    on_floor(S).

solve(S, [A | As]) :- 
    transition(S, S1),
    A = (climb(S, S1); push(_, _, S, S1); grasp(S, S1)),
    solve(S1, As).

% Example query
?- solve(s0, Actions).
