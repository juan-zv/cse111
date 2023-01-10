from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full():
    assert make_full_name("Marie", "Toussaint") == "Toussaint;Marie"
    assert make_full_name("Jason", "Derulo") == "Derulo;Jason"
    assert make_full_name("Fabian", "Diaz") == "Diaz;Fabian"
    assert make_full_name("Alan", "Torres") == "Torres;Alan"

def test_extract_family():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Zurita; Juan") == "Zurita"
    assert extract_family_name("Fabian; Diaz") == "Fabian"
    assert extract_family_name("Alan; Torres") == "Alan"

def test_extract_given():
    assert extract_given_name("Marie; Toussaint") == "Toussaint"
    assert extract_given_name("Jason; Derulo") == "Derulo"
    assert extract_given_name("Zurita; Juan") == "Juan"
    assert extract_given_name("Zurita; Juan") == "Juan"
    assert extract_given_name("Zurita; Juan") == "Juan"


pytest.main(["-v", "--tb=line", "-rN", __file__])