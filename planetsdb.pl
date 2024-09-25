% Planets Database
planet(mercury, terrestrial, 57.91, 0).
planet(venus, terrestrial, 108.2, 0).
planet(earth, terrestrial, 149.6, 1).
planet(mars, terrestrial, 227.9, 2).
planet(jupiter, gas_giant, 778.5, 79).
planet(saturn, gas_giant, 1427, 83).
planet(uranus, gas_giant, 2871, 27).
planet(neptune, gas_giant, 4497.1, 14).

% Rules
terrestrial_planet(Name) :- planet(Name, terrestrial, _, _).
gas_giant(Name) :- planet(Name, gas_giant, _, _).
moons(Name, Count) :- planet(Name, _, _, Count).


%?- terrestrial_planet(X).
%?- moons(saturn, Count).
