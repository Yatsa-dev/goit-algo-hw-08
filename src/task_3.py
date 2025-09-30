import heapq


def main():
    cables = [1, 2, 3, 4, 10]
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)
        print(f"Cables {first} and {second} cost {cost}")
        print(f"Heap: {cables}")

    print(f"Total cost to connect cables: {total_cost}")


if __name__ == "__main__":
    main()