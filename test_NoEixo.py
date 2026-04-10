from src.logica import adicionar_tarefa, remover_tarefa, validar_data


def test_adicionar_tarefa_valida():
    tarefas = []
    resultado = adicionar_tarefa(tarefas, "Estudar", "10/10/2026", "Alta")
    assert resultado is True
    assert len(tarefas) == 1


def test_adicionar_tarefa_data_invalida():
    tarefas = []
    resultado = adicionar_tarefa(tarefas, "Estudar", "99/99/9999", "Alta")
    assert resultado is False
    assert len(tarefas) == 0


def test_remover_tarefa_inexistente():
    tarefas = []
    resultado = remover_tarefa(tarefas, 0)
    assert resultado is False


def test_validar_data():
    assert validar_data("10/10/2026") is True
    assert validar_data("99/99/9999") is False