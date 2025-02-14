#!/usr/bin/env python
import sys
import warnings

from rabe7agent.crew import Rabe7Agent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'stock_selection': 'AAPL',  # Example stock selection
        'topic': 'DeFi',            # Example topic if needed
        'risk_tolerance': 'medium',  # Example risk tolerance if needed
        'trading_strategy_preference': 'long_term'  # Example trading strategy preference if needed
    }
    Rabe7Agent().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'stock_selection': 'AAPL',  # Example stock selection
        'topic': 'DeFi',            # Example topic if needed
        'risk_tolerance': 'medium',  # Example risk tolerance if needed
        'trading_strategy_preference': 'long_term'  # Example trading strategy preference if needed
    }
    try:
        Rabe7Agent().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Rabe7Agent().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Rabe7Agent().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
