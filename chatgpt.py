import openai
from tkinter import *
from tkinter import scrolledtext

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"  # Replace with your actual API key

def generate_response(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def display_response():
    input_text = input_field.get("1.0", END).strip()
    if input_text:
        response = generate_response(input_text)
        output_field.delete("1.0", END)
        output_field.insert(END, response)

# Create the main window
root = Tk()
root.title("ChatGPT Interface")
root.geometry("800x600")

# Create input field
input_label = Label(root, text="Enter your question:")
input_label.pack(pady=10)
input_field = scrolledtext.ScrolledText(root, width=80, height=10)
input_field.pack(pady=10)

# Create submit button
submit_button = Button(root, text="Submit", command=display_response)
submit_button.pack(pady=10)

# Create output field
output_label = Label(root, text="Response:")
output_label.pack(pady=10)
output_field = scrolledtext.ScrolledText(root, width=80, height=20)
output_field.pack(pady=10)

root.mainloop()