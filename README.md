# About

Inspired by my work at JPL, I wrote a small utility that allows you to compare distances between two points using the two most common methods:

* [Great Circle Distance](https://en.wikipedia.org/wiki/Great-circle_distance)

* [Vincenty's Formulae](https://en.wikipedia.org/wiki/Vincenty%27s_formulae)

# Background

The basic idea is that the great circle distance (compared to regular Euclidean distance) method assumes that the Earth is a perfect sphere, but Vincenty's formulae more accurately approximates the Earth as an [oblate spheroid](https://en.wikipedia.org/wiki/Spheroid).

To see this effect in action, notice the error measurements for distances computed near the equator and those near the poles; for example, compare the distance between the Natal, Brazil (-5.733987, -35.209868) and Abidjan, Cote d'Ivore (5.415605, -4.022813) -- the percent error between Vincenty and GC is 0.081%. However, when comparing say, Saint Lewis, Canada (52.371317, -55.684063) to Alta, Norway (69.972182, 23.270742) -- the percent error is larger here, at 0.122%. 

Per Wikipedia, the Great Circle distance is roughly accurate to around 0.5% of the true value, whereas Vincety's method is accurate to 0.5 *milli*meters, anywhere on the Earth's surface.

# Usage

Enter comma-separated coordinates in the form:

``` (<latitude>, <longitude>)```

[Example input](https://i.imgur.com/WTjf7VA.png)

[Example output](https://i.imgur.com/2FZEOsm.png)