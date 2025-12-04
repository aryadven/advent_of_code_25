IDs = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

def find_invalid(IDs):
    IDs = IDs.split("-")
    invalids = []
    for i in range(int(IDs[0]), int(IDs[1])+1):
        i = str(i)
        l = len(i)
        if i[:int(l/2)] == i[int(l/2):]:
            invalids.append(str(i))
    return invalids
    
def validate_ids_range(IDs):
    IDs = IDs.replace("\n", "").split(",")
    for ID_range in IDs:
        invalids = find_invalid(ID_range)
        str_invalids =", " + " and ".join(invalids) if invalids else ""
        print(f"In range {ID_range} there are {len(invalids)} invalid ID{str_invalids}")

validate_ids_range(IDs)
