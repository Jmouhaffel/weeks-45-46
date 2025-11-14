from complex import Complex


def test_default_constructor():
    z = Complex()
    assert z.re == 0
    assert z.im == 0
    assert str(z) == "0+0i"


def test_constructor_with_real_only():
    z = Complex(5)
    assert z.re == 5
    assert z.im == 0
    assert str(z) == "5+0i"


def test_constructor_with_real_and_imag():
    z = Complex(1, 2)
    assert z.re == 1
    assert z.im == 2
    assert str(z) == "1+2i"


def test_str_positive_and_negative_imag():
    z = Complex(1, 2)
    w = Complex(1, -2)
    assert str(z) == "1+2i"
    assert str(w) == "1-2i"


def test_repr():
    z = Complex(1, 2)
    assert repr(z) == "Complex(1, 2)"


def test_add_complex_complex():
    z = Complex(1, 2)
    y = Complex(3, 4)
    result = z + y
    assert isinstance(result, Complex)
    assert result.re == 4
    assert result.im == 6


def test_add_complex_int():
    z = Complex(1, 2)
    result = z + 3
    assert isinstance(result, Complex)
    assert result.re == 4
    assert result.im == 2


def test_radd_int_complex():
    z = Complex(1, 2)
    result = 3 + z
    assert isinstance(result, Complex)
    assert result.re == 4
    assert result.im == 2


def test_sub_complex_complex():
    z = Complex(1, 2)
    y = Complex(3, 4)
    result = z - y
    assert isinstance(result, Complex)
    assert result.re == -2
    assert result.im == -2


def test_sub_complex_int():
    z = Complex(5, 2)
    result = z - 3
    assert isinstance(result, Complex)
    assert result.re == 2
    assert result.im == 2


def test_rsub_int_complex():
    z = Complex(1, 2)
    result = 3 - z
    assert isinstance(result, Complex)
    assert result.re == 2
    assert result.im == -2


def test_mul_complex_complex():
    z = Complex(1, 2)
    y = Complex(3, 4)
    result = z * y
    assert isinstance(result, Complex)
    # (1+2i)(3+4i) = (1*3 - 2*4) + (1*4 + 2*3)i = -5 + 10i
    assert result.re == -5
    assert result.im == 10


def test_mul_complex_int():
    z = Complex(1, -2)
    result = z * 3
    assert isinstance(result, Complex)
    assert result.re == 3
    assert result.im == -6


def test_rmul_int_complex():
    z = Complex(1, -2)
    result = 3 * z
    assert isinstance(result, Complex)
    assert result.re == 3
    assert result.im == -6


def test_equality_true():
    z1 = Complex(1, 2)
    z2 = Complex(1, 2)
    assert z1 == z2
    assert not (z1 != z2)


def test_equality_false():
    z1 = Complex(1, 2)
    z2 = Complex(2, 1)
    assert z1 != z2
    assert not (z1 == z2)
