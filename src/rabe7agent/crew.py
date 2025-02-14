from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

# Initialize tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

@CrewBase
class Rabe7Agent:
	"""Rabe7Agent crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			allow_delegation=True,
			tools=[scrape_tool, search_tool],
			memory=True,
			model="gpt-3.5-turbo",
			verbose=True
		)

	@agent
	def data_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['data_analyst'],
			allow_delegation=True,
			tools=[scrape_tool, search_tool],
			memory=True,
			model="gpt-3.5-turbo",
			verbose=True
		)

	@agent
	def data_validation(self) -> Agent:
		return Agent(
			config=self.agents_config['data_validation'],
			allow_delegation=True,
			memory=True,
			model="gpt-4",
			verbose=True
		)

	@agent
	def trading_strategy(self) -> Agent:
		return Agent(
			config=self.agents_config['trading_strategy'],
			allow_delegation=True,
			memory=True,
			model="gpt-4",
			verbose=True
		)

	@agent
	def execution(self) -> Agent:
		return Agent(
			config=self.agents_config['execution'],
			allow_delegation=True,
			memory=True,
			model="gpt-4",
			verbose=True
		)

	@agent
	def risk_management(self) -> Agent:
		return Agent(
			config=self.agents_config['risk_management'],
			allow_delegation=True,
			memory=True,
			model="gpt-4",
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			allow_delegation=True,
			memory=True,
			model="gpt-4",
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
			return_type=JsonOutput,
			
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
