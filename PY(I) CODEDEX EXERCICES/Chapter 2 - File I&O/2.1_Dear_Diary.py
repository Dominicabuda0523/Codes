# Write code below 💖

file = open('dear_diary.txt', 'w')

file.write("Dear Diary,\n")
file.write(
    "Today was a wonderful day! I went to the park and had a picnic with my friends. \n" \
    "We played games, ate delicious food, and enjoyed the sunshine. I can't wait to do it again soon!\n")

file.close()

file = open('dear_diary.txt', 'r')
print(file.read())
file.close()