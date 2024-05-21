import asyncio
from metagpt.roles import (
    Architect,
    Engineer,
    ProductManager,
    ProjectManager,
)
from metagpt.team import Team

async def startup(idea: str):
    company = Team()
    company.hire(
        [
        Architect(),
        Engineer(),
        ProductManager(),
        ProjectManager(),
        ]
    )
    company.invest(investment=3.0)
    company.run_project(idea=idea)

    return await company.run(n_round=3)


async def main():
    result = await startup("A string of ideas")

    print(result)

if __name__ == "__main__":
    asyncio.run(main())

