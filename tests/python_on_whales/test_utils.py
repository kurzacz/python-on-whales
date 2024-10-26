import python_on_whales.utils


def test_environment_variables_propagation(monkeypatch):
    monkeypatch.setenv("SOME_VARIABLE", "dododada")

    stdout = python_on_whales.utils.run(
        ["bash", "-c", "echo $SOME_VARIABLE && echo $OTHER_VARIABLE"],
        capture_stdout=True,
        env={"OTHER_VARIABLE": "dudu"},
    )
    assert stdout == "dododada\ndudu"

def test_format_mapping_for_cli_no_none():
    mapping = {"test_env_var": None}
    result = python_on_whales.utils.format_mapping_for_cli(mapping)
    assert result == ["test_env_var="]
