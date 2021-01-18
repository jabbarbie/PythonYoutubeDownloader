import pytest

# def fun(x):
#     return x + 5

# def test_fun():
#     assert fun(5) == 10

# def raised():
#     raise SystemExit(1)
#     # return 10

# def test_raised():
#     with pytest.raises(SystemExit):
#         raised()

class Test_String:
    
    def test_judul(self):
        judul = "Medley Lagu Opening Kartun 90an.mp4".lower()
        assert "lagu" in judul
    
    def test_indonesia(self):
        judul = "jakarta"
        assert hasattr(judul, "lower") # mempunyai attribut lower atau tidak

class Test_Null:
    def test_satu(self):
        assert 0
    def test_dua(self):
        assert 0