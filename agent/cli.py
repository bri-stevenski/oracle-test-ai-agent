# agent/cli.py

import typer
from rich import print

app = typer.Typer()


@app.command()
def generate(
    prompt: str,
    recommend_only: bool = typer.Option(False, "--recommend-only", "-r", help="Only show the recommendation, skip generation.")
):
    """
    Generate test automation code from a natural language prompt.
    """
    from agent.core.orchestrator import OracleOrchestrator

    print("\n[bold cyan]🧠 Oracle Processing Request...[/bold cyan]\n")

    if recommend_only:
        from agent.core.classifier import TestClassifier
        from agent.core.recommender import FrameworkRecommender
        
        classifier = TestClassifier()
        recommender = FrameworkRecommender()
        
        classification = classifier.classify(prompt)
        result = recommender.recommend(classification)
        
        print("[bold green]✅ Oracle Recommendation (Draft Mode)[/bold green]\n")
        print(f"[bold]Test Type:[/bold] {classification.test_type}")
        print(f"[bold]Framework:[/bold] {result['framework']}")
        print("\n[bold]Reasoning:[/bold]")
        for r in result["reason"]:
            print(f" - {r}")
        print("\n[yellow]Note: Generation skipped due to --recommend-only flag.[/yellow]")
        return

    orchestrator = OracleOrchestrator()
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