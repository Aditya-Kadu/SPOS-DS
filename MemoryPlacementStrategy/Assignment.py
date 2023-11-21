class MemoryPlacementStrategies:
    def __init__(self, processes, memory_blocks) -> None:
        self.processes = processes
        self.memory_blocks = memory_blocks

    def first_fit(self):
        allocation1 = [-1]*len(self.processes)
        self.processes = [212, 417, 112, 426]
        self.memory_blocks = [100, 500, 200, 300, 600]
        for i in range(len(self.processes)):
            for j in range(len(memory_blocks)):
                if self.processes[i] <= self.memory_blocks[j]:
                    allocation1[i] = j
                    self.memory_blocks[j] -= self.processes[i]
                    break
        print(allocation1)

    def next_fit(self):
        allocation2 = [-1]*len(self.processes)
        self.processes = [212, 417, 112, 426]
        self.memory_blocks = [100, 500, 200, 300, 600]
        j = 0
        t = len(self.memory_blocks)-1
        for i in range(len(self.processes)):
            while j < len(self.memory_blocks):
                if self.processes[i] <= self.memory_blocks[j]:
                    allocation2[i] = j
                    self.memory_blocks[j] -= self.processes[i]
                    t = (j-1) % len(self.memory_blocks)
                    break
                if t == j:
                    t = (j-1) % len(self.memory_blocks)
                    break
                j = (j+1) % len(self.memory_blocks)

        print(allocation2)

    def best_fit(self):
        allocation3 = [-1]*len(self.processes)
        self.processes = [212, 417, 112, 426]
        self.memory_blocks = [100, 500, 200, 300, 600]

        for i in range(len(self.processes)):
            best_index = -1
            for j in range(len(self.memory_blocks)):
                if self.processes[i] <= self.memory_blocks[j]:
                    if best_index == -1 or self.memory_blocks[j] < self.memory_blocks[best_index]:
                        best_index = j

            if best_index != -1:
                allocation3[i] = best_index
                self.memory_blocks[best_index] -= self.processes[i]

        print(allocation3)

    def worst_fit(self):
        allocation4 = [-1]*len(self.processes)
        self.processes = [212, 417, 112, 426]
        self.memory_blocks = [100, 500, 200, 300, 600]

        for i in range(len(self.processes)):
            worst_index = -1
            for j in range(len(self.memory_blocks)):
                if self.processes[i] <= self.memory_blocks[j]:
                    if worst_index == -1 or self.memory_blocks[j] > self.memory_blocks[worst_index]:
                        worst_index = j
            if worst_index != -1:
                allocation4[i] = worst_index
                self.memory_blocks[worst_index] -= self.processes[i]

        print(allocation4)


processes = [212, 417, 112, 426]
memory_blocks = [100, 500, 200, 300, 600]

obj = MemoryPlacementStrategies(processes, memory_blocks)
print("First Fit......")
obj.first_fit()
print()

print("Next Fit.......")
obj.next_fit()
print()

print("Best Fit......")
obj.best_fit()
print()

print("Worst Fit.......")
obj.worst_fit()
print()
