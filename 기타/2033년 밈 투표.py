promise = ["Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna stop"]
n = int(input())
result = "No"
for _ in range(n):
    sentence = input()
    if sentence not in promise: result = "Yes"

print(result)
