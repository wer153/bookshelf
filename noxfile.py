import nox  # type: ignore


_TARGET_PYTHON_VERSION = "3.12"
nox.options.error_on_external_run = True
nox.options.report = ".nox-report.json"


class _Poetry:
    def __init__(self, session: nox.Session):
        self._session = session
        self._session.run(
            "poetry",
            "install",
            "--sync",
            "--no-root",
            external=True,
        )

    def run(self, *args: str, **kwargs: dict) -> None:
        self._session.run("poetry", "run", *args, **kwargs, external=True)


@nox.session(python=_TARGET_PYTHON_VERSION)
def ci(session: nox.Session):
    CI_INSTRUCTION_MAP: dict[str, list[str]] = {
        "ruff": ["ruff format --diff .", "ruff check app"],
        "mypy": ["mypy app"],
        "unittest": ["coverage run -m pytest tests", "coverage report -m"],
    }
    poetry = _Poetry(session)
    for kind, instructions in CI_INSTRUCTION_MAP.items():
        print(f"running {kind} with poetry run")
        for instruction in instructions:
            poetry.run(*instruction.split())
