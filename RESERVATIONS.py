RESERVATIONS = [
    {"guest": "Ada", "nights":2, "rate": 90},
    {"guest": "Brook", "nights":3, "rate": 120},
]

guest_counts = [2,0]

def compute_total(res, guests):
    return res["nights"] * res["rate"] / guests

def total_all(reservations, guest_counts):
    totalled = 0
    failed = 0
    for index, res in enumerate(reservations):
        guests = guest_counts[index]
        
        try:
            total = compute_total(res, guests)
        except ZeroDivisionError as error:
            print("Reservation", index, "for", res["guest"], "failed:", error)
            failed = failed + 1
            continue
        print("Reservation", index, "for", res["guest"], "costs", total, "per guest")
        totalled = totalled + 1
    return totalled, failed

def main():
    print(RESERVATIONS)
    for value in RESERVATIONS[0].values():
        print(type(value))
    print(RESERVATIONS[1]["guest"])
    totalled, failed = total_all(RESERVATIONS, guest_counts)
    print("Totalled ", str(totalled), ", failed ", str(failed))
if __name__ == "__main__":
    main()