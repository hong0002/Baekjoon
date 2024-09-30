def check_voting_eligibility(birthdays):
    election_year = 1989
    election_month = 2
    election_day = 27

    results = []
    
    for birthday in birthdays:
        y, m, d = birthday
        
        # Check the year first
        if y < election_year:
            results.append("Yes")
        elif y > election_year:
            results.append("No")
        else:
            # Year is exactly 1989, so we check the month and day
            if m < election_month:
                results.append("Yes")
            elif m > election_month:
                results.append("No")
            else:
                # Month is February, check the day
                if d <= election_day:
                    results.append("Yes")
                else:
                    results.append("No")
    
    return results

# Read input
n = int(input())
birthdays = [tuple(map(int, input().split())) for _ in range(n)]

# Check eligibility for each birthday and print the results
results = check_voting_eligibility(birthdays)
for result in results:
    print(result)
