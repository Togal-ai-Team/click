import os
import uuid

import click


def test_var_name_preservation(runner):
    @click.command()
    @click.option('--modelFileCamelCase', '-m', type=click.Path())
    def cli(modelFileCamelCase):
        """Hello World!"""
        click.echo("I EXECUTED w/ a camelCaseVariable!")

    result = runner.invoke(cli, ["--help"])
    assert not result.exception
    assert "Hello World!" in result.output
    assert result.exit_code == 0
    assert "I EXECUTED" not in result.output

    result = runner.invoke(cli, [])
    assert not result.exception
    assert "I EXECUTED w/ a camelCaseVariable!" in result.output
    assert result.exit_code == 0


