class Election_Algo:
    def __init__(self, no_process):
        self.no_proccess = no_process
        self.alive_status = [True]*no_process

    def kill_process(self, id):
        self.alive_status[id] = False

    def start_process(self, id):
        self.alive_status[id] = True

    def Ring(self, initiator_id):
        if initiator_id > self.no_proccess-1:
            return
        if not self.alive_status[initiator_id]:
            print(f"Process {initiator_id} is dowm.")
            return

        start = initiator_id
        ptr = (start+1) % self.no_proccess
        last_alive_process = start

        while ptr != start:
            if self.alive_status[ptr]:
                print(
                    f"Process {last_alive_process} sends ELECTION MESSAGE to {ptr}")
                last_alive_process = ptr
            ptr = (ptr+1) % self.no_proccess
        print(f"Process {last_alive_process} sends ELECTION MESSAGE to {ptr}")

        bully_process = max(id for id in range(
            self.no_proccess) if self.alive_status[id])
        print(f"New Co-ordinator is {bully_process}")
        print(f"Process {bully_process} informs it is new co-ordinator")

    def Bully(self, initiator_id):
        if initiator_id > self.no_proccess-1:
            return
        if not self.alive_status[initiator_id]:
            print(f"Process {initiator_id} is dowm.")
            return

        print(f"Election Started by Process {initiator_id}")
        for i in range(initiator_id+1, self.no_proccess):
            print(
                f"Election Message send to process {i} by process {initiator_id}")
        for i in range(initiator_id+1, self.no_proccess):
            if self.alive_status[i]:
                print(f"Process {i} responded OK")
        for i in range(initiator_id+1, self.no_proccess):
            if self.alive_status[i]:
                self.Bully(i)
        bully_process = max(id for id in range(
            self.no_proccess) if self.alive_status[id])
        print(f"New Co-ordinator is {bully_process}")
        print(f"Process {bully_process} informs it is new co-ordinator")


obj = Election_Algo(5)
obj.kill_process(4)
obj.kill_process(1)
print("Ring Algorithm")
obj.Ring(0)
print("Bully Algorithm")
obj.Bully(0)
