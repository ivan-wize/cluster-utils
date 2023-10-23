from clusterUtils import reduce_clusters

def main():
    input_ctuples1 = [(0.5, 0.5, 0.5), (1.5, 1.5, 1.1), (0.7, 0.7, 0.4), (4, 4, 0.7)]
    result = reduce_clusters(input_ctuples1)
    print(result)

    input_ctuples2 = [(1.5, 01.5, 1.3), (4, 4, 0.7)]
    result = reduce_clusters(input_ctuples2)
    print(result)

    input_ctuples3 = [(1, 3, 0.7), (2, 3, 0.4), (3, 3, 0.9)]
    result = reduce_clusters(input_ctuples3)
    print(result)

if __name__ == "__main__":
    main()
