class MNT:
    def __init__(self):
        self.macro_name = ""
        self.kpd_count = 0
        self.pp_count = 0
        self.kpd_ptr = 0
        self.mdt_ptr = 0


class MDT:
    def __init__(self):
        self.mnemonic = ""
        self.operand1 = ""
        self.operand2 = ""
        self.op1_index = -1
        self.op2_index = -1


mntab: list[MNT] = []
mdtab: list[MDT] = []
kpdtab: list[tuple[str, str]] = []
pntab_map: dict[str, list[str]] = {}

source_file = input("Enter File Name: ")
with open(source_file, "r") as file:
    source_contents = file.read()
    source_lines: list[str] = source_contents.split("\n")
    source_tokens: list[str] = [token.split() for token in source_lines]

kpdtab_ptr = 0
mdtab_ptr = 0
is_macro_running = False
curr_macro_name = ""

for i in range(1, len(source_tokens)):
    line_token = source_tokens[i]
    if source_tokens[i-1][0] == "MACRO":
        curr_macro_name = line_token[0]
        parameters = line_token[1:]
        kpd_count = 0
        pp_count = 0
        pntab: list[str] = []
        for parameter in parameters:
            if "=" in parameter:
                parameter_name, default_value = parameter.split("=")
                kpdtab.append((parameter_name, default_value))
                kpd_count += 1
            else:
                parameter_name = parameter
                pp_count += 1
            pntab.append(parameter_name)
        mntab_entry = MNT()
        mntab_entry.macro_name = curr_macro_name
        mntab_entry.kpd_count = kpd_count
        mntab_entry.pp_count = pp_count
        mntab_entry.kpd_ptr = kpdtab_ptr
        mntab_entry.mdt_ptr = mdtab_ptr
        kpdtab_ptr += kpd_count
        pntab_map[curr_macro_name] = pntab
        mntab.append(mntab_entry)
        is_macro_running = True

    elif is_macro_running and line_token[0] != "MEND" and line_token[0] != "MACRO":
        mdtab_entry = MDT()
        mdtab_entry.mnemonic = line_token[0]
        pntab = pntab_map[curr_macro_name]
        param = line_token[1]
        if param in pntab:
            mdtab_entry.op1_index = pntab.index(param)
        mdtab_entry.operand1 = param
        param = line_token[2]
        if param in pntab:
            mdtab_entry.op2_index = pntab.index(param)
        mdtab_entry.operand2 = param
        mdtab.append(mdtab_entry)
        mdtab_ptr += 1
    elif line_token[0] == "MEND":
        mdtab_entry = MDT()
        mdtab_entry.mnemonic = "MEND"
        mdtab.append(mdtab_entry)
        mdtab_ptr += 1
        is_macro_running = False

# print(mntab)
# print(mdtab)
# print(kpdtab)
# print(pntab_map)


print("------------ MNTAB ----------------")
print("Name".ljust(10), "#PP".ljust(5), "#KP".ljust(
    5), "KPDTAB_PTR".ljust(10), "MDTAB_PTR".ljust(10))
for entry in mntab:
    print(
        entry.macro_name.ljust(10),
        str(entry.pp_count).ljust(5),
        str(entry.kpd_count).ljust(5),
        str(entry.kpd_ptr).ljust(10),
        str(entry.mdt_ptr).ljust(10)
    )
print()

print("------------ MDTAB ----------------")
for entry in mdtab:
    print(
        entry.mnemonic.ljust(10),
        (entry.operand1 if entry.op1_index == -
         1 else f"(P,{entry.op1_index})").ljust(10),
        (entry.operand2 if entry.op2_index == -
         1 else f"(P,{entry.op2_index})").ljust(10),
    )
print()

print("------------ KPDTAB ----------------")
print("Name".ljust(10), "Default Value".ljust(15))
for param in kpdtab:
    print(param[0].ljust(10), param[1].ljust(15))
print()

print("------------- PNTAB -----------------")
for (macro_name, pntab) in pntab_map.items():
    print("PNTAB for macro", macro_name)
    for param in pntab:
        print(param[1:])
