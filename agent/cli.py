# agent/cli.py

import typer
from rich import print

from agent.core.orchestrator import OracleOrchestrator

app = typer.Typer()

orchestrator = OracleOrchestrator()


@app.command()
def generate(prompt: str):
    """
    Generate test automation code from a natural language prompt.
    """

    print("\n[bold cyan]🧠 Oracle Processing Request...[/bold cyan]\n")

    result = orchestrator.run(prompt)

    print("\n[bold green]✅ Oracle Result[/bold green]\n")

    print(f"[bold]Test Type:[/bold] {result['test_type']}")
    print(f"[bold]Framework:[/bold] {result['framework']}")

    print("\n[bold]Reasoning:[/bold]")
    for r in result["reason"]:
        print(f" - {r}")

    print("\n[bold yellow]Output File:[/bold yellow]")
    print(result["output_file"])


@app.command()
def version():
    """
    Show Oracle version info.
    """
    print("[bold green]Oracle AI v0.1 (MVP)[/bold green]")


if __name__ == "__main__":
    app()