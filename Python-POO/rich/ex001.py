from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install
install()

vara = "hello [green]Word[/green] :earth_americas:"

caixa = Panel(f"[white]{vara}[/]", title="title", style="red", width=35);

print(caixa)