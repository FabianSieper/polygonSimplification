# Simplification of a Polygon

This project deals with the simplification of polygons. This is used, for example, in the illustration of maps. If the scale is small, for example, streets are shown in a simplified way.

## Usage
To try out the different simplification algorithms, the file `main.py` must be started. This performs the calculations either on the .gpx file attached via the command line arguments (`python main.py --file path/to/file.gpx`) or on a supplied default file and draws the results.

## Used Algorithms

The optimization of the polygons is done by using the following algorithms:

- Douglas-Peucker
- Imai-Iri
- Chan-Chin