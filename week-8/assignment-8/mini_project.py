import csv

clean_data = []
skipped_rows = []
rows_attempted = 0

try:
    with open("../data/messy_data.csv", "r") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=1):
            rows_attempted += 1

            if None in row:
                skipped_rows.append(
                    f"Row {row_number}: extra column detected — skipped"
                )
                continue

            try:
                name = row["name"]
                category = row["category"]
                amount = float(row["amount"])

                if not name or not category:
                    raise ValueError("missing name or category")

                clean_data.append({
                    "name": name,
                    "category": category,
                    "amount": amount
                })

            except ValueError as error:
                skipped_rows.append(f"Row {row_number}: ValueError — {error}")

            except KeyError as error:
                skipped_rows.append(f"Row {row_number}: KeyError — {error}")

except FileNotFoundError:
    print("Oops! CSV file not found. Please check the file path.")
    exit()

print("\n=== CSV Report ===")
print("Rows attempted: ", rows_attempted)
print("Rows parsed:    ", len(clean_data))
print("Rows skipped:   ", len(skipped_rows))

print("\nSkipped rows:")
for error in skipped_rows:
    print(" ", error)

print("\nClean data:")
for row in clean_data:
    print(f"  {row['name']} | {row['category']} | ${row['amount']:.2f}")