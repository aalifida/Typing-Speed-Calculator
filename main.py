import time as t
import random as r

paragraphs = [
    "In a distant land, a wise old man knew the secrets of the universe. People sought his counsel, finding answers in his riddles. A young traveler asked about life's meaning, and the old man shared a story of a river changing lives, teaching that life's meaning is in the journey and connections.",
    "The city bustled as the sun rose. Street vendors set up stalls, children played, and a musician's lively tune drew a crowd. Amid the chaos, a sense of community and shared purpose brought harmony to the intricate dance of daily life.",
    "Deep in the forest, a secret garden bloomed with magic and wonder. Only those with pure hearts could find it. A lost traveler found peace and healing in this enchanted place, welcomed by a gentle spirit tending to the plants and animals.",
    "On the edge of a village stood an ancient oak tree believed to have magical properties. Villagers whispered wishes to its leaves. One summer, a girl's wish for her mother's recovery came true, renewing the village's faith in the oak's magic.",
    "In the heart of the mountains, a small cabin offered solitude and reflection. Visitors escaped modern life's noise, reconnecting with nature. They hiked, breathed crisp air, and read by the fire, finding comfort in the wilderness's simplicity and beauty.",
    "A young artist in a bustling city captured its vibrant life on her canvas. Her studio was filled with inspiration. She felt a deep connection to the people and places she portrayed, using her art to make sense of the world and share her perspective.",
    "In a coastal town, a lighthouse guided ships safely. The keeper maintained the light with care, knowing lives depended on it. On stormy nights, he felt a profound sense of duty. The lighthouse was a symbol of safety and home.",
    "A young scientist dedicated her life to understanding the universe's mysteries. Despite challenges, she remained passionate and determined. Gazing at the night sky through her telescope, she felt connected to the cosmos and found purpose in her quest for knowledge.",
    "In the desert, a nomadic tribe followed nature's rhythms, living in harmony with the land. Elders taught the young about survival and respect. Each evening, they shared stories by the campfire, finding freedom and belonging in the desert's timeless beauty."
]

def compare_strings(user_input, test_paragraph):
    mistakes = 0
    correct = 0
    min_length = min(len(user_input), len(test_paragraph))
    for i in range(min_length):
        if user_input[i] == test_paragraph[i]:
            correct += 1
        else:
            mistakes += 1

    mistakes += abs(len(user_input) - len(test_paragraph))
    return correct, mistakes

print("************ TYPING SPEED CALCULATOR ************")
testParagraph = r.choice(paragraphs)
print("You have to type this paragraph:\n")
print(testParagraph)
input("\nPress Enter to start...")

start_time = t.time()
userInput = input()
total_time = t.time() - start_time

words = len(userInput.split())
correct, mistakes = compare_strings(userInput, testParagraph)

wpm = (words / total_time) * 60
accuracy = (correct / len(testParagraph)) * 100 if len(testParagraph) else 0

print(f"\nYou typed {words} words in {total_time:.2f} seconds.")
print(f"Words per minute: {wpm:.2f}")
print(f"Mistakes: {mistakes}")
print(f"Accuracy: {accuracy:.2f}%")
