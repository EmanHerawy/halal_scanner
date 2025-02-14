   # HadiAgent Crew


   <img width="300" alt="Screenshot 2025-02-08 at 18 08 56" src="https://github.com/user-attachments/assets/f3f9806a-10e4-462c-a38b-c91059c175f4" />



<!-- About the Project -->
## :star2: About the Project


Hadi is a multi-agent system, powered by [crewAI](https://crewai.com), designed to analyze, validate, and execute Shariah-compliant and ethical investments in Decentralized Finance (DeFi). Our system leverages autonomous AI agents to research, assess risk, ensure compliance, and develop investment strategies tailored to ethical finance principles.

Hadi aims to bridge the gap between DeFi innovation and responsible investing, allowing users to confidently participate in Halal and ethical financial opportunities while ensuring security, compliance, and profitability.




<!-- Problems -->
## :bomb: Problems
The decentralized finance space is growing rapidly, but ethical investment barriers still exist:

1️⃣ Lack of Shariah-Compliant DeFi Solutions
Many DeFi platforms engage in interest-based (riba) and speculative (maysir) practices, making them non-compliant with Islamic finance principles.

2️⃣ Complexity & Lack of Transparency in DeFi
Investors struggle to assess protocol risks, governance structures, and compliance due to the lack of structured verification systems.

3️⃣ Limited Awareness of ESG and Ethical Investment Opportunities
Ethical investors find it challenging to discover and validate sustainable DeFi projects aligned with environmental, social, and governance (ESG) values.


4️⃣ Manual Research & Inefficient Investment Strategies
Investors spend significant time analyzing DeFi protocols without AI-powered insights, making decision-making slow and inefficient.


<!-- Solution -->
## :woman_technologist: Solution

 
The decentralized finance space is growing rapidly, but ethical investment barriers still exist:

1️⃣ Lack of Shariah-Compliant DeFi Solutions
Many DeFi platforms engage in interest-based (riba) and speculative (maysir) practices, making them non-compliant with Islamic finance principles.


2️⃣ Complexity & Lack of Transparency in DeFi
Investors struggle to assess protocol risks, governance structures, and compliance due to the lack of structured verification systems.


3️⃣ High Volatility and Smart Contract Vulnerabilities
DeFi protocols often experience security exploits, market instability, and liquidity risks, leading to unexpected losses.


4️⃣ Limited Awareness of ESG and Ethical Investment Opportunities
Ethical investors find it challenging to discover and validate sustainable DeFi projects aligned with environmental, social, and governance (ESG) values.


5️⃣ Manual Research & Inefficient Investment Strategies
Investors spend significant time analyzing DeFi protocols without AI-powered insights, making decision-making slow and inefficient.


## How Hadi Works
Hadi introduces an agent-based system that automates the entire ethical investment process using CrewAI and blockchain plugins:

🔹 Communication Agent → Collects investment goals from users.

🔹 Manager Agent → Assigns tasks to other agents and manages execution.

🔹 Research Agent → Gathers real-time data on DeFi projects.

🔹 Validation Agent → Verifies if the projects comply with Shariah finance and ESG standards.

🔹 Trading Strategy Agent → Builds a profitable and ethical investment strategy.

🔹 Risk Advisor Agent → Assesses financial risks, smart contract vulnerabilities, and market conditions.

🔹 Reporting Agent → Compiles findings into a detailed investment report for user approval.




  
  



-------------------------------------------------------------------


🌍 **Beneficial Outcomes**
✔️ Enables Ethical & Shariah-Compliant DeFi Investing → Ensures investments align with moral finance principles.
✔️ Increases Transparency → AI-driven Shariah validation and risk assessment improves trust.
✔️ Reduces Investment Risks → AI agents automate risk management to protect user funds.
✔️ Saves Time & Resources → Automates DeFi research and strategy execution.
✔️ Supports ESG & Sustainable Finance → Identifies DeFi projects promoting environmental and ethical impact.



**#### 🔜 What’s Next for **Hadi**?**
🛠️ Expanding AI Agent Capabilities

Implement Machine Learning models to enhance DeFi prediction accuracy.
Train Trading Strategy Agents using real-world investment data.
🔗 Integrating with More Blockchains

Expand support for Polygon, Arbitrum, Optimism, and other L2 networks.
Develop cross-chain AI agents for multi-chain investment strategies.
🤖 Enhancing Security & Smart Contract Auditing

Implement on-chain security scanners for rug pull detection.
Improve automated Shariah compliance validation.
🚀 Building Hadi dApp

Launch a user-friendly web interface where investors can access AI-driven reports & strategies.
Integrate safe, one-click DeFi execution based on AI recommendations.

     


<!-- Env Variables -->
### :key: Environment Variables

To run **Hadi**, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`

<!-- Getting Started -->
## 	:toolbox: Getting Started

<!-- Prerequisites -->
### :bangbang: Prerequisites

This project uses Node as package manager

```bash
 npm install
```

<!-- Installation -->
### :gear: Installation

Install dependencies with npm

```bash
  npm install 
  cd app/client
```
   

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/rabe7agent/config/agents.yaml` to define your agents
- Modify `src/rabe7agent/config/tasks.yaml` to define your tasks
- Modify `src/rabe7agent/crew.py` to add your own logic, tools and specific args
- Modify `src/rabe7agent/main.py` to add custom inputs for your agents and tasks


## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the rabe7Agent Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The rabe7Agent Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Rabe7Agent Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

  

<!-- Team -->
## :wave: Team

| Member | Title | Description | Linkedin | GitHub   |
| ----------- | ----------- | ----------- |----------- |----------- |
| Eman Herawy      | Blockchain Developer & Smart Contract Security Auditor  | Setting-up agents            |   https://www.linkedin.com/in/emanherawy/    | Eman Herawy |
| Mohamed Sharabassy| Data Scientist     | Coordinate the project technicals | https://www.linkedin.com/in/mohamedsharabassy/                 | Mo-Sharabassy             |
| Lena Hierz   | Developer  | Designing the agent economy & front-end          | https://www.linkedin.com/in/lena-hierzi-8221151ab/ | GigaHierz       |
| Nada Jabr  | Business Developer | Defining agents' roles, needed tools and plug-ins           | https://www.linkedin.com/in/nada-jabr-15838b39/  | NJ-2021        |


 
   
   <!-- Demo -->
  - ## :cinema: Demo
    
https://www.loom.com/share/0c7076596f714f9c8c358d065ca01063?sid=e100e599-4305-4915-9f47-3a706c3fc7a3

  


![photo_2025-02-09_19-50-48](https://github.com/user-attachments/assets/36f1ebe8-66d2-4d42-aaf9-2d070747f1c5)




https://github.com/user-attachments/assets/118b695c-ade4-4df6-96da-feebb1d5501e





https://www.loom.com/share/e3febeca52e44995ac93c096fa23eb6a?sid=661057ee-9d9e-48df-b59b-22560a00fd88


  <!-- Presentation -->
  - ## :cinema: Presentation

https://www.canva.com/design/DAGeC97imJw/UxXM3Kdx_JXjo4hBiqcDig/view?utm_content=DAGeC97imJw&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h5702b42d5e
