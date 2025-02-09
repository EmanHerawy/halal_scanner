#!/usr/bin/env python
import sys
import warnings
import json

from halal_scanner.crew import HalalScanner

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew and return structured JSON output.
    """
    inputs = {
        'token_name': 'Bitcoin'  # Example token name, replace dynamically
    }
    
    try:
        result = HalalScanner().crew().kickoff(inputs=inputs)

        # Ensure the result is valid JSON
        try:
            json_result = json.loads(result)
        except json.JSONDecodeError:
            json_result = {"error": "Invalid JSON format", "raw_output": result}

        # Print JSON for easy debugging
        print(json.dumps(json_result, indent=2))

    except Exception as e:
        print(json.dumps({"error": f"An error occurred: {str(e)}"}))


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "token_name": "Bitcoin"
    }
    try:
        HalalScanner().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        HalalScanner().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and return structured results.
    """
    inputs = {
        "token_name": "Bitcoin"
    }
    try:
        result = HalalScanner().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

        # Parse and print JSON
        try:
            json_result = json.loads(result)
        except json.JSONDecodeError:
            json_result = {"error": "Invalid JSON format", "raw_output": result}

        print(json.dumps(json_result, indent=2))

    except Exception as e:
        print(json.dumps({"error": f"An error occurred: {str(e)}"}))
