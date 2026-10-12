from planner import choose_tool

while True:
  user_input = input("\nYou: ")

  if user_input.lower() == "quit":
    print("Goodbye!")
    break
  chosen_tool = choose_tool(user_input)
  print(f"Chosen Tool: {chosen_tool}")
  