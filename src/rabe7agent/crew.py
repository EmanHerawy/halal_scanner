from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from rabe7agent.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
@CrewBase
class Rabe7Agent():
	"""Rabe7Agent crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			allow_delegation=True,
    tools = [scrape_tool, search_tool],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)
	@agent
	def data_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['data_analyst'],
			tools = [scrape_tool, search_tool],
			allow_delegation=True,
			verbose=True
		)

	@agent
	def data_validation(self) -> Agent:
		return Agent(
			config=self.agents_config['data_validation'],
			allow_delegation=True,
			verbose=True
		)

	@agent
	def trading_strategy(self) -> Agent:
		return Agent(
			config=self.agents_config['trading_strategy'],
			allow_delegation=True,
			verbose=True
		)

	@agent
	def execution(self) -> Agent:
		return Agent(
			config=self.agents_config['execution'],
			allow_delegation=True,
			verbose=True
		)

	@agent
	def risk_management(self) -> Agent:
		return Agent(
			config=self.agents_config['risk_management'],
			allow_delegation=True,
			verbose=True
		)
	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			allow_delegation=True,
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)
	@task
	def data_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['data_analysis_task'],
		)

	@task
	def data_validation_task(self) -> Task:
		return Task(
			config=self.tasks_config['data_validation_task'],
		)

	@task
	def strategy_development_task(self) -> Task:
		return Task(
			config=self.tasks_config['strategy_development_task'],
		)

	@task
	def execution_planning_task(self) -> Task:
		return Task(
			config=self.tasks_config['execution_planning_task'],
		)

	@task
	def risk_assessment_task(self) -> Task:
		return Task(
			config=self.tasks_config['risk_assessment_task'],
		)
	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Rabe7Agent crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
