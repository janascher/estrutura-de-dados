import numpy as np
from estrutura_de_dados.Aula_01.classification import ClassificationStudents


def test_insert_note():
    classification = ClassificationStudents()
    classification.insert_note(7.0)
    classification.insert_note(8.5)
    classification.insert_note(6.0)
    classification.insert_note(9.0)
    classification.insert_note(6.5)
    classification.insert_note(7.5)
    assert np.array_equal(classification.notes, np.array(
        [6.0, 6.5, 7.0, 7.5, 8.5, 9.0], dtype=np.float32))


def test_fetch_notes_greater_than():
    classification = ClassificationStudents()
    classification.insert_note(7.0)
    classification.insert_note(8.5)
    classification.insert_note(6.0)
    classification.insert_note(9.0)
    classification.insert_note(6.5)
    classification.insert_note(7.5)
    notes_bigger_than_7 = classification.fetch_notes_greater_than(7)
    assert np.array_equal(notes_bigger_than_7, np.array(
        [7.5, 8.5, 9.0], dtype=np.float32))


def test_fetch_notes_less_than():
    classification = ClassificationStudents()
    classification.insert_note(7.0)
    classification.insert_note(8.5)
    classification.insert_note(6.0)
    classification.insert_note(9.0)
    classification.insert_note(6.5)
    classification.insert_note(7.5)
    notes_less_than_7 = classification.fetch_notes_less_than(7)
    assert np.array_equal(notes_less_than_7, np.array(
        [6.0, 6.5], dtype=np.float32))


def test_fetch_notes_equal_to():
    classification = ClassificationStudents()
    classification.insert_note(7.0)
    classification.insert_note(8.5)
    classification.insert_note(6.0)
    classification.insert_note(9.0)
    classification.insert_note(6.5)
    classification.insert_note(7.5)
    notes_iguais_a_7 = classification.fetch_notes_equal_to(7)
    assert np.array_equal(notes_iguais_a_7, np.array([7.0], dtype=np.float32))
