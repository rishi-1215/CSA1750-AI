% edge(Node1, Node2, Cost).
edge(a, b, 1).
edge(a, c, 2).
edge(b, d, 4).
edge(c, d, 1).
edge(c, e, 5).
edge(d, e, 2).
edge(d, goal, 6).
edge(e, goal, 1).

% heuristic(Node, HeuristicValue).
heuristic(a, 6).
heuristic(b, 5).
heuristic(c, 3).
heuristic(d, 2).
heuristic(e, 4).
heuristic(goal, 0).

% Best First Search Algorithm
best_first_search(Start, Goal, Path, Cost) :-
    best_first_search([[Start, 0]], Goal, [], Path, Cost).

best_first_search([[Goal, Cost|RestPath]|_], Goal, _, Path, Cost) :-
    reverse([Goal, Cost|RestPath], Path).

best_first_search([[Current, CurrentCost|RestPath]|Queue], Goal, Visited, Path, Cost) :-
    findall(
        [Next, NextCost, Current, CurrentCost|RestPath],
        (
            edge(Current, Next, StepCost),
            \+ memberchk(Next, Visited),
            NextCost is CurrentCost + StepCost,
            heuristic(Next, Heuristic)
        ),
        Children
    ),
    append(Queue, Children, NewQueue),
    sort(2, @=<, NewQueue, SortedQueue),
    best_first_search(SortedQueue, Goal, [Current|Visited], Path, Cost).

reverse(List, ReversedList) :-
    reverse(List, [], ReversedList).
reverse([], Acc, Acc).
reverse([H|T], Acc, ReversedList) :-
    reverse(T, [H|Acc], ReversedList).
