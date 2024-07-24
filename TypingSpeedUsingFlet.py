import random as r
import flet as ft
import time
import threading
from paragraphs import paragraphs

def main(page: ft.Page):
    page.title = "Typing Speed Test"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Initialize variables
    selected_paragraph = r.choice(paragraphs)
    start_time = None

    # Define functions before using them
    def update_timer():
        while True:
            if start_time is not None:
                elapsed_time = int(time.time() - start_time)
                timer_text.value = f"Elapsed Time: {elapsed_time} seconds"
                page.update()
                time.sleep(1)

    def calculate_results(e):
        user_input = textBox.value  # Get the user input from the text field
        correct, mistakes, wrong_words = compare_strings(user_input, selected_paragraph)
        
        # Calculate accuracy and WPM
        total_words = len(user_input.split())
        accuracy = (correct / total_words) * 100 if total_words > 0 else 0
        elapsed_time = int(time.time() - start_time)
        wpm = (correct / elapsed_time) * 60 if elapsed_time > 0 else 0

        # Format result as a table with a line-like structure
        result_text = f"Results:\n{'-'*60}\n"
        result_text += f"Correct words: {correct}\nMistakes: {mistakes}\n"
        result_text += f"Accuracy: {accuracy:.2f}%\nWords per minute (WPM): {wpm:.2f}\n\n"
        result_text += "{:<20} {:<20}\n".format("Your Input", "Expected")
        result_text += '-'*40 + '\n'
        for wrong_pair in wrong_words:
            result_text += "{:<20} {:<20}\n".format(wrong_pair[0], wrong_pair[1])
        
        result_paragraph.value = result_text

        # Hide other elements and show results
        page.controls = [result_paragraph, retryButton]
        page.update()

    def reset_test(e):
        nonlocal selected_paragraph, start_time
        selected_paragraph = r.choice(paragraphs)
        paragraph.value = selected_paragraph
        textBox.value = ""
        checkButton.disabled = False  # Re-enable the Calculate Results button
        start_time = time.time()
        # Show initial UI elements
        page.controls = [container]
        page.update()

    def start_test(e):
        nonlocal start_time
        # Hide the start button and show the test UI
        page.controls = [paragraph, textBox, timer_text, row_buttons]
        page.update()
        start_time = time.time()
        threading.Thread(target=update_timer, daemon=True).start()

    # Initialize UI elements
    paragraph = ft.Text(value=selected_paragraph, weight="Bold", size=16)
    textBox = ft.TextField(label="Type the Paragraph Here", multiline=True, width=600)
    timer_text = ft.Text(value="Elapsed Time: 0 seconds", size=14)
    checkButton = ft.ElevatedButton("Calculate Results", on_click=calculate_results, width=150)
    resetButton = ft.ElevatedButton("Reset", on_click=reset_test, width=150)
    startButton = ft.ElevatedButton("Start", on_click=start_test, width=150)
    retryButton = ft.ElevatedButton("Retry", on_click=reset_test, width=150)

    # Container for initial UI
    container = ft.Column(
        controls=[
            ft.Text(value="Typing Speed Test", weight="Bold", size=24),
            ft.Text(value=" ", height=20),  # Spacer
            ft.Text(value="Click 'Start' to begin the test:", size=16),
            ft.Text(value=" ", height=10),  # Spacer
            startButton
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    # Row for buttons (calculate and reset) when the test is active
    row_buttons = ft.Row(
        controls=[checkButton, resetButton],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    # Result display
    result_paragraph = ft.Text(value="", size=14)
    
    page.controls.append(container)
    page.update()

def compare_strings(user_input, test_paragraph):
    mistakes = 0
    correct = 0
    wrong_words = []
    test_words = test_paragraph.split()
    user_words = user_input.split()

    min_length = min(len(user_words), len(test_words))
    for i in range(min_length):
        if user_words[i] == test_words[i]:
            correct += 1
        else:
            mistakes += 1
            wrong_words.append((user_words[i], test_words[i]))

    mistakes += abs(len(user_words) - len(test_words))
    return correct, mistakes, wrong_words

# Initialize the flet application
ft.app(target=main)
import random as r
import flet as ft
import time
import threading
from paragraphs import paragraphs

def main(page: ft.Page):
    page.title = "Typing Speed Test"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Initialize variables
    selected_paragraph = r.choice(paragraphs)
    start_time = None

    # Define functions before using them
    def update_timer():
        while True:
            if start_time is not None:
                elapsed_time = int(time.time() - start_time)
                timer_text.value = f"Elapsed Time: {elapsed_time} seconds"
                page.update()
                time.sleep(1)

    def calculate_results(e):
        user_input = textBox.value  # Get the user input from the text field
        correct, mistakes, wrong_words = compare_strings(user_input, selected_paragraph)
        
        # Calculate accuracy and WPM
        total_words = len(user_input.split())
        accuracy = (correct / total_words) * 100 if total_words > 0 else 0
        elapsed_time = int(time.time() - start_time)
        wpm = (correct / elapsed_time) * 60 if elapsed_time > 0 else 0

        # Format result as a table with a line-like structure
        result_text = f"Results:\n{'-'*60}\n"
        result_text += f"Correct words: {correct}\nMistakes: {mistakes}\n"
        result_text += f"Accuracy: {accuracy:.2f}%\nWords per minute (WPM): {wpm:.2f}\n\n"
        result_text += "{:<20} {:<20}\n".format("Your Input", "Expected")
        result_text += '-'*40 + '\n'
        for wrong_pair in wrong_words:
            result_text += "{:<20} {:<20}\n".format(wrong_pair[0], wrong_pair[1])
        
        result_paragraph.value = result_text

        # Hide other elements and show results
        page.controls = [result_paragraph, retryButton]
        page.update()

    def reset_test(e):
        nonlocal selected_paragraph, start_time
        selected_paragraph = r.choice(paragraphs)
        paragraph.value = selected_paragraph
        textBox.value = ""
        checkButton.disabled = False  # Re-enable the Calculate Results button
        start_time = time.time()
        # Show initial UI elements
        page.controls = [container]
        page.update()

    def start_test(e):
        nonlocal start_time
        # Hide the start button and show the test UI
        page.controls = [paragraph, textBox, timer_text, row_buttons]
        page.update()
        start_time = time.time()
        threading.Thread(target=update_timer, daemon=True).start()

    # Initialize UI elements
    paragraph = ft.Text(value=selected_paragraph, weight="Bold", size=16)
    textBox = ft.TextField(label="Type the Paragraph Here", multiline=True, width=600)
    timer_text = ft.Text(value="Elapsed Time: 0 seconds", size=14)
    checkButton = ft.ElevatedButton("Calculate Results", on_click=calculate_results, width=150)
    resetButton = ft.ElevatedButton("Reset", on_click=reset_test, width=150)
    startButton = ft.ElevatedButton("Start", on_click=start_test, width=150)
    retryButton = ft.ElevatedButton("Retry", on_click=reset_test, width=150)

    # Container for initial UI
    container = ft.Column(
        controls=[
            ft.Text(value="Typing Speed Test", weight="Bold", size=24),
            ft.Text(value=" ", height=20),  # Spacer
            ft.Text(value="Click 'Start' to begin the test:", size=16),
            ft.Text(value=" ", height=10),  # Spacer
            startButton
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    # Row for buttons (calculate and reset) when the test is active
    row_buttons = ft.Row(
        controls=[checkButton, resetButton],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    # Result display
    result_paragraph = ft.Text(value="", size=14)
    
    page.controls.append(container)
    page.update()

def compare_strings(user_input, test_paragraph):
    mistakes = 0
    correct = 0
    wrong_words = []
    test_words = test_paragraph.split()
    user_words = user_input.split()

    min_length = min(len(user_words), len(test_words))
    for i in range(min_length):
        if user_words[i] == test_words[i]:
            correct += 1
        else:
            mistakes += 1
            wrong_words.append((user_words[i], test_words[i]))

    mistakes += abs(len(user_words) - len(test_words))
    return correct, mistakes, wrong_words

# Initialize the flet application
ft.app(target=main)
