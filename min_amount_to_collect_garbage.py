class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_minutes = 0  
        current_travel_time = 0  

        total_minutes += len(garbage[0])

        last_garbage_indices = [-1, -1, -1] 

        for house_index in range(1, len(garbage)):
            total_minutes += len(garbage[house_index])

            if "M" in garbage[house_index]:
                last_garbage_indices[0] = house_index - 1
            if "P" in garbage[house_index]:
                last_garbage_indices[1] = house_index - 1
            if "G" in garbage[house_index]:
                last_garbage_indices[2] = house_index - 1

        for travel_index in range(len(travel)):
            current_travel_time += travel[travel_index]

            for truck_index in range(3):
                if last_garbage_indices[truck_index] == travel_index:
                    total_minutes += current_travel_time

        return total_minutes