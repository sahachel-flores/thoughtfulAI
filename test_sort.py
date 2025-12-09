# test_sort.py
from sort import sort

def test_standard_package():
    # Not bulky, not heavy
    assert sort(10, 10, 10, 5) == "STANDARD"

def test_bulky_by_volume():
    # Volume = 100 * 100 * 100 = 1_000_000 -> bulky
    assert sort(100, 100, 100, 5) == "SPECIAL"

def test_bulky_by_dimension():
    # One dimension >= 150 -> bulky
    assert sort(150, 10, 10, 5) == "SPECIAL"

def test_heavy_only():
    # Mass >= 20 -> heavy
    assert sort(10, 10, 10, 20) == "SPECIAL"

def test_rejected_bulky_and_heavy_volume():
    # Bulky by volume and heavy by mass
    assert sort(100, 100, 100, 25) == "REJECTED"

def test_rejected_bulky_and_heavy_dimension():
    # Bulky by dimension and heavy by mass
    assert sort(200, 10, 10, 20) == "REJECTED"

def test_edge_volume_just_below_threshold():
    # Volume just below bulky threshold
    assert sort(100, 100, 99, 19) == "STANDARD"

def test_edge_volume_exact_threshold():
    # Volume exactly at 1_000_000
    assert sort(100, 100, 100, 19) == "SPECIAL"

def test_edge_mass_exact_threshold():
    # Mass exactly 20 -> heavy
    assert sort(10, 10, 10, 20) == "SPECIAL"
