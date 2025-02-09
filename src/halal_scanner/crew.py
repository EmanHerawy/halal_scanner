from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

# ✅ Research tools for speed and efficiency
search_tool = SerperDevTool()
scraper_tool = ScrapeWebsiteTool()

# 🔹 Shariah Compliance Analyst (Fast Model)
shariah_analyst = Agent(
    role="Shariah Compliance Analyst",
    goal="Determine if {token_name} is compliant with Islamic finance principles.",
    backstory=(
        "A finance professional with deep knowledge of Islamic financial laws, "
        "capable of evaluating whether a cryptocurrency aligns with Shariah principles. "
        "You analyze the token's business model, affiliations, and how it generates revenue."
    ),
    tools=[search_tool, scraper_tool],
    memory=True,
    model="gpt-3.5-turbo"  # ✅ Uses a faster model for research
)

# 🔹 Risk Assessment Analyst (Fast Model)
risk_analyst = Agent(
    role="Crypto Risk Assessment Analyst",
    goal="Analyze {token_name}'s market history, trends, and investment risks.",
    backstory=(
        "An expert in cryptocurrency markets, specializing in evaluating risk. "
        "You analyze price fluctuations, social media sentiment, news articles, and financial trends "
        "to assess whether investing in {token_name} is advisable or risky."
    ),
    tools=[search_tool, scraper_tool],
    memory=True,
    model="gpt-3.5-turbo"  # ✅ Uses a faster model for research
)

# 🔹 JSON Formatter Agent (High-Quality Model)
formatter_agent = Agent(
    role="Shariah & Risk Report Formatter",
    goal="Summarize findings from Shariah and Risk Analysts into a well-structured JSON response.",
    backstory=(
        "An AI assistant skilled in summarizing complex research into clear and user-friendly reports. "
        "You take the findings from compliance and risk analysts and format them into a structured, professional JSON output "
        "that is easy for users to understand."
    ),
    memory=True,
    model="gpt-4"  # ✅ Uses a high-quality model for clarity & structuring
)

# 🔹 Task: Check Shariah Compliance
check_compliance_task = Task(
    description=(
        "Research the token {token_name} and determine if it complies with Islamic finance principles. "
        "Analyze its revenue model, whether it involves interest-based lending (riba), gambling (maysir), "
        "or unethical industries (e.g., adult content, alcohol, weapons). "
        "Provide a JSON object with 'IsHalal' (boolean) and 'justification' (string)."
    ),
    expected_output="A JSON object with 'IsHalal' (boolean) and 'justification' (string).",
    agent=shariah_analyst,
)

# 🔹 Task: Assess Investment Risks
analyze_risk_task = Task(
    description=(
        "Conduct market research on {token_name}. "
        "Analyze its price history, social media mentions (Twitter), financial reports, and related news articles. "
        "Provide a JSON object with 'riskAssessment' (string)."
    ),
    expected_output="A JSON object with 'riskAssessment' (string).",
    agent=risk_analyst,
)

# 🔹 Task: Put Results in JSON Format
format_json_task = Task(
    description=(
        "Take the results from the Shariah Compliance Analyst and Risk Assessment Analyst "
        "and generate a JSON response in the following format:\n\n"
        "```json\n"
        "{{\n"
        "  'IsHalal': true/false,\n"
        "  'justification': 'Clear and professional reasoning',\n"
        "  'riskAssessment': 'Concise and insightful risk evaluation'\n"
        "}}\n"
        "```\n\n"
        "Ensure that the response is:\n"
        "- Professional yet easy to understand\n"
        "- Concise and to the point\n"
        "- Avoids overly technical jargon but remains precise\n"
        "Deliver a user-friendly but well-informed response."
    ),
    expected_output="A well-structured JSON object matching the required format.",
    agent=formatter_agent,
)


# 🔹 Crew Configuration
final_crew = Crew(
    agents=[shariah_analyst, risk_analyst, formatter_agent],
    tasks=[check_compliance_task, analyze_risk_task, format_json_task],
    process=Process.sequential,  # ✅ Shariah & Risk Analysis run in parallel, then formatted
    memory=True,
    verbose=True
)
