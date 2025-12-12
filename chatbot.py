import requests, json

def ask_llm(prompt, model="gemma3:1b"):
    url = "http://localhost:11434/api/generate"
    payload = {"model": model, "prompt": prompt}
    response = requests.post(url, json=payload, stream=True)

    output = ""
    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            if "response" in data:
                output += data["response"]
    return output

print("Local LLM Chatbot! Type 'quit' to exit.\n")

while True:
    q = input("You: ")
    if q.lower() == "quit":
        break
    ans = ask_llm(q)
    print("\nBot:", ans, "\n")
