import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	FileReadTool, PDFSearchTool
)





@CrewBase
class SistemaDeAnaliseDeAlinhamentoCandidatoVagaCrew:
    """SistemaDeAnaliseDeAlinhamentoCandidatoVaga crew"""

    
    @agent
    def curriculum_analysis_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["curriculum_analysis_specialist"],
            tools=[FileReadTool(), PDFSearchTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def behavioral_assessment_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["behavioral_assessment_analyst"],
            tools=[FileReadTool(), PDFSearchTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def job_alignment_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config["job_alignment_evaluator"],
            tools=[FileReadTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @task
    def analyze_curriculum(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_curriculum"],
            markdown=False,
        )
    
    @task
    def analyze_behavioral_assessment(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_behavioral_assessment"],
            markdown=False,            
        )
    
    @task
    def evaluate_job_alignment(self) -> Task:
        return Task(
            config=self.tasks_config["evaluate_job_alignment"],
            markdown=True,
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the SistemaDeAnaliseDeAlinhamentoCandidatoVaga crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


