# Simplification of a Polygon

This project deals with the simplification of polygons. This is used, for example, in the illustration of maps. If the scale is small, for example, streets are shown in a simplified way.

## Used Algorithms

The optimization of the polygons is done by using the following algorithms:

- Douglas-Peucker
- Imai-Iri
- Chan-Chin

## Usage

To try out the different simplification algorithms, the file `main.py` must be started. This starts the computation of each of the algorithms on a predefined file (`project/src/test/sample.gpx`).

The results of each of the algorithms is plottet as well as some plots according the run time of them. The run time is measured by using a range of files which were especially created for this purpose.