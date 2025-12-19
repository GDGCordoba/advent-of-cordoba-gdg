def shortest_path(n, nodes, edges, start, end):
    """
    Calculates the minimum walking distance between two landmarks in Córdoba
    using the pedestrian map provided by the Mezquita Server.

    Args:
        n (int): Number of nodes (landmarks).
        nodes (list[int]): A list containing the names of all landmarks.
                        Each name appears exactly as referenced in edges.
        edges (list[tuple[str, str, int]]): A list of connections in the form
                        (A, B, W), where A and B are landmark names
                        and W is the walking distance in meters.
        start (str): Name of the starting landmark.
        end (str): Name of the destination landmark.

    Returns:
        int | str: The minimum distance in meters between start and end,
                or the string "INF" if no path exists.
    """
    # TODO: Write your code here

def main():
    """
    Main function that reads input from stdin, calls shortest_path,
    and prints the result.
    """
    # TODO: Write your code here


if __name__ == "__main__":
    main()
