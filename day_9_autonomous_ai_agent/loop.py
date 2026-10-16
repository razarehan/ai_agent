from state import (
    create_state,
    add_action,
    record_observation,
    next_step,
    can_continue,
    finish
)

async def run_agent_loop(
    user_request,
    planner,
    execute_action,
    format_answer,
    tools,
    client
):
    state = create_state(user_request)

    while can_continue(state):
        # Planner decide what to do next
        action = planner(state, tools)
        print("Planner Selected: ", action)

        if action.lower() == "finish":
            answer = format_answer(state)
            finish(state, answer)
            break

        # Execute action, if required again
        observation = await execute_action(action, client)

        # Add action in state
        add_action(state, action)
        # Record observation in state
        record_observation(state, action, observation)

        next_step(state)
    
    return state