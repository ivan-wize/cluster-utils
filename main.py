from cluster_utils import reduce_clusters

def main():
    input_ctuples = [(0.5, 0.5, 0.5), (1.5, 1.5, 1.1), (0.7, 0.7, 0.4), (4, 4, 0.7)]
    result = reduce_clusters(input_ctuples)
    print(result)

if __name__ == "__main__":
    main()
