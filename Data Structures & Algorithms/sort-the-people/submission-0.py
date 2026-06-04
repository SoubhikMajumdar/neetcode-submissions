class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Pair each person's height with their name
        people = list(zip(heights, names))

        # Sort by height in descending order
        people.sort(reverse=True)

        # Extract the names from the sorted pairs
        sorted_names = []
        for height, name in people:
            sorted_names.append(name)

        return sorted_names