import math

class Circle:
    """
    Class to represent a circle
    """
    def __init__(self, x, y, r):
        """
        Initialize a circle with center at x/y coordinates and radius r
        """
        self.x = x
        self.y = y
        self.radius = r
        self.area = math.pi * r**2

    def distance(self, other):
        """
        Find distance between the circles' centers
        """
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def overlaps(self, other):
        """
        Check if cicles overlap
        """
        return self.distance(other) <= self.radius + other.radius

class Cluster:
    """
    Class to represent a cluster of circle
    """
    def __init__(self, circle):
        """
        Initialize a cluster with one circle.
        """
        self.circles = [circle]

    def add_circle(self, circle):
        """
        Add circle to cluster
        """
        self.circles.append(circle)

    def has_overlap(self, circle):
        """
        Check if a given circle overlaps with any circle in this cluster
        """
        return any(c.overlaps(circle) for c in self.circles)

def reduce_clusters(ctuple_list):
    circles = [Circle(x, y, r) for x, y, r in ctuple_list]
    clusters = []

    """
    Error handling
    """
    if not isinstance(ctuple_list, list):
        raise TypeError("Input should be a list of ctuples.")
    for ctuple in ctuple_list:
        if not isinstance(ctuple, tuple) or len(ctuple) != 3:
            raise ValueError("Each ctuple must be a tuple of three numbers.")
        if not all(isinstance(n, (int, float)) for n in ctuple):
            raise ValueError("Each element in ctuple must be a number.")

    """
    Reduce clusters to the circle with the maximum area in each cluster.

    :param ctuple_list: A list of ctuples representing circles.
    :return: A list of ctuples where each ctuple represents the circle with the maximum area in each cluster.
    """
    for circle in circles:
        added = False # flag to check if circle has been added to any cluster
        for cluster in clusters:
            if cluster.has_overlap(circle):
                cluster.add_circle(circle)
                added = True
                break
        if not added: # if the circle doesn't overlap with any existing clusters, create a new cluster with that circle
            clusters.append(Cluster(circle))
    reduced_clusters = []
    for cluster in clusters:
        max_area_circle = max(cluster.circles, key=lambda c: c.area)
        reduced_clusters.append((max_area_circle.x, max_area_circle.y, max_area_circle.radius))
    return reduced_clusters
