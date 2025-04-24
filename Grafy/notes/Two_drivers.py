"""
Problem:
We have a map of a country in form of a graph, where vertexes are cities.
There are two drivers in a car, they change in every city on the way.
Find a path, where driver #1 drives for the shortest time (driver #2 can ride as lond as he wants)

Idea:
We can search for paths, but we have to count two things:
    1) sum length of even edges
    2) sum length of odd edges

    In the end we choose which length we prefer (shorter one)

Better:
Each city has two vertexes (doubles), one is for #1 entering city, second vertex is for #2"
"""